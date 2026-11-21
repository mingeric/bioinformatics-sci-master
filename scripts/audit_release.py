#!/usr/bin/env python3
"""Technical integrity audit for one canonical SCI submission release.

Not a scientific truth verifier. Require substantive human review for statistical,
biological and provenance validity. No network or nonstandard packages required.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
import struct
import sys
import zlib

REQUIRED_FIG_COLUMNS = {"figure_id", "filename", "scientific_question", "dataset_id", "source_table", "script", "status", "sha256"}
REQUIRED_EVIDENCE_COLUMNS = {"claim_id", "figure_id", "panel_id", "claim_text", "dataset_id", "source_table", "script", "evidence_tier", "status"}


def rows(path: Path, required: set[str], failures: list[str]):
    if not path.is_file():
        failures.append(f"Missing: {path}")
        return []
    try:
        with path.open(newline="", encoding="utf-8-sig") as fp:
            reader = csv.DictReader(fp)
            missing = required - set(reader.fieldnames or [])
            if missing:
                failures.append(f"Columns missing from {path.name}: {sorted(missing)}")
                return []
            return list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        failures.append(f"Invalid CSV: {path} ({exc})")
        return []


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def check_png(path: Path) -> tuple[int, int]:
    """Validate signature, PNG chunk CRCs, IHDR, and IEND; detect truncation."""
    signature = b"\x89PNG\r\n\x1a\n"
    with path.open("rb") as f:
        if f.read(8) != signature:
            raise ValueError("Invalid PNG signature")
        width, height = None, None
        seen_end = False
        chunks = 0
        while True:
            length_data = f.read(4)
            if not length_data:
                break
            if len(length_data) != 4:
                raise ValueError("Truncated chunk length")
            length = struct.unpack(">I", length_data)[0]
            if length > 256 * 1024 * 1024:
                raise ValueError("Suspicious PNG chunk length")
            tag = f.read(4)
            data = f.read(length)
            crc = f.read(4)
            if len(tag) != 4 or len(data) != length or len(crc) != 4:
                raise ValueError("Truncated PNG chunk")
            actual = zlib.crc32(tag + data) & 0xffffffff
            stored = struct.unpack(">I", crc)[0]
            if actual != stored:
                raise ValueError("PNG CRC mismatch")
            if chunks == 0:
                if tag != b"IHDR" or length != 13:
                    raise ValueError("No first IHDR")
                width, height = struct.unpack(">II", data[:8])
                if min(width, height) == 0:
                    raise ValueError("Invalid dimensions")
            if tag == b"IEND":
                seen_end = True
                if f.read(1):
                    raise ValueError("Unexpected bytes after IEND")
                break
            chunks += 1
        if not seen_end:
            raise ValueError("IEND not found")
        return width, height


def safe_resolve(root: Path, raw: str, failures: list[str], label: str) -> Path | None:
    if not raw or not raw.strip():
        failures.append(f"Empty path: {label}")
        return None
    p = (root / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    try:
        p.relative_to(root)
    except ValueError:
        failures.append(f"Source outside project root: {label} -> {p}")
        return None
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--profile", choices=["generic", "smc56-p1"], default="generic")
    ap.add_argument("--json", action="store_true", help="Print JSON report")
    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()
    release = root / "FINAL_SUBMISSION"
    failures, warnings = [], []
    if not root.is_dir():
        failures.append(f"Project root missing: {root}")
    figs = rows(release / "figure_manifest.csv", REQUIRED_FIG_COLUMNS, failures)
    evid = rows(release / "evidence_ledger.csv", REQUIRED_EVIDENCE_COLUMNS, failures)
    manuscript = release / "manuscript.md"
    if not manuscript.is_file() or manuscript.stat().st_size < 250:
        failures.append(f"Missing/too-short manuscript: {manuscript}")
    else:
        content = manuscript.read_text(encoding="utf-8", errors="replace")
        if re.search(r"\b(TODO|TBD|PLACEHOLDER|LOREM IPSUM)\b|\[INSERT\b", content, flags=re.I):
            failures.append("Unresolved manuscript placeholder")
    if not figs:
        failures.append("No complete figure rows")
    if not evid:
        failures.append("No panel-level evidence rows")

    observed, tested, passed_png = set(), 0, 0
    for i, rec in enumerate(figs, 1):
        fid = rec["figure_id"].strip()
        filename = rec["filename"].strip()
        tag = f"figure row {i}: {fid or '?'}"
        if not fid or fid in observed:
            failures.append(f"Blank/duplicate figure ID: {tag}")
        observed.add(fid)
        if filename != f"{fid}.png":
            failures.append(f"Filename/ID mismatch: {tag} -> {filename}")
        if rec["status"].strip().upper() != "COMPLETE":
            failures.append(f"Figure is not COMPLETE: {tag}")
        if len(rec["scientific_question"].strip()) < 15:
            failures.append(f"Scientific question missing or too short: {tag}")
        if not rec["dataset_id"].strip():
            failures.append(f"Missing dataset_id: {tag}")
        path = safe_resolve(root, f"FINAL_SUBMISSION/figures/{filename}", failures, tag)
        if path:
            if not path.is_file():
                failures.append(f"PNG missing: {tag} -> {path}")
            else:
                tested += 1
                try:
                    w, h = check_png(path)
                    passed_png += 1
                    if w < 1600 or h < 900:
                        warnings.append(f"Low pixel dimensions: {tag} ({w}x{h})")
                    expected = rec["sha256"].strip().lower()
                    actual = sha256(path)
                    if not re.fullmatch("[0-9a-f]{64}", expected) or actual != expected:
                        failures.append(f"Missing/wrong SHA256: {tag}")
                except (OSError, ValueError) as exc:
                    failures.append(f"Corrupt PNG {tag}: {exc}")
        for field in ("source_table", "script"):
            p = safe_resolve(root, rec[field], failures, f"{tag}.{field}")
            if p and not p.is_file():
                failures.append(f"Source missing: {tag}.{field}={p}")

    claims_by_figure = set()
    observed_claim_ids = set()
    for i, rec in enumerate(evid, 1):
        cid, fid = rec["claim_id"].strip(), rec["figure_id"].strip()
        tag = f"evidence row {i}: {cid or '?'}"
        if not cid or cid in observed_claim_ids:
            failures.append(f"Blank/duplicate claim_id: {tag}")
        observed_claim_ids.add(cid)
        if fid not in observed:
            failures.append(f"Evidence points to unlisted figure: {tag} -> {fid}")
        claims_by_figure.add(fid)
        if not rec["panel_id"].strip() or not rec["claim_text"].strip():
            failures.append(f"Missing panel ID/claim text: {tag}")
        if not rec["dataset_id"].strip() or not rec["evidence_tier"].strip():
            failures.append(f"Missing dataset or evidence tier: {tag}")
        if rec["status"].strip().upper() != "COMPLETE":
            failures.append(f"Evidence row not COMPLETE: {tag}")
        for field in ("source_table", "script"):
            p = safe_resolve(root, rec[field], failures, f"{tag}.{field}")
            if p and not p.is_file():
                failures.append(f"Source missing: {tag}.{field}={p}")
    for fid in sorted(observed - claims_by_figure):
        failures.append(f"Figure missing panel evidence: {fid}")

    if args.profile == "smc56-p1":
        expected = {f"Fig{i:02d}" for i in range(1, 9)} | {f"FigS{i:02d}" for i in range(1, 5)}
        for missing in sorted(expected - observed):
            failures.append(f"Required SMC56 figure missing: {missing}")
        for extra in sorted(observed - expected):
            failures.append(f"Unexpected SMC56 final figure: {extra}")
        # Enforce only approved output names, not merely only listed names
        figdir = release / "figures"
        if figdir.is_dir():
            extras = {p.stem for p in figdir.glob("*.png")} - expected
            if extras:
                failures.append(f"Unlisted or extra release PNG: {sorted(extras)}")

    report = {
        "profile": args.profile,
        "project_root": str(root),
        "release_root": str(release),
        "figure_count": len(figs),
        "panel_evidence_count": len(evid),
        "pngs_tested": tested,
        "pngs_integrity_passed": passed_png,
        "pass": not failures,
        "failures": failures,
        "warnings": warnings,
        "scientific_truth_independently_verified": False,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("TECHNICAL RELEASE AUDIT:", "PASS" if report["pass"] else "FAIL")
        print(f"Figures: {len(figs)} | Panel evidence: {len(evid)} | Valid PNG: {passed_png}/{tested}")
        for x in failures: print("FAIL:", x)
        for x in warnings: print("WARN:", x)
        print("Scientific inference/provenance still requires independent human review.")
    return 0 if report["pass"] else 2

if __name__ == "__main__":
    sys.exit(main())
