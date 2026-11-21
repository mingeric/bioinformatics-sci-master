#!/usr/bin/env python3
"""Create a minimal, non-fictional research project scaffold.

Creates folders and empty *schema* files only. No scientific results or figures
are synthesized. Existing files are never overwritten.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

DIRS = ["data/raw", "data/processed", "metadata", "code", "results", "figures", "manuscript", "staging"]
COPY = {
    "cohort_ledger.csv": "metadata/cohort_ledger.csv",
    "figure_manifest.csv": "metadata/figure_manifest.csv",
    "evidence_ledger.csv": "metadata/evidence_ledger.csv",
    "analysis_plan.md": "metadata/analysis_plan.md",
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Path to project root")
    ap.add_argument("--profile", choices=["generic", "smc56-p1"], default="generic")
    args = ap.parse_args()
    root = Path(args.root).expanduser().resolve()
    templates = Path(__file__).resolve().parents[1] / "templates"
    for directory in DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)
    for filename, target in COPY.items():
        dst = root / target
        if not dst.exists():
            shutil.copy2(templates / filename, dst)
            print("CREATED", dst)
        else:
            print("PRESERVED", dst)
    profile_file = root / "metadata" / "skill_profile.txt"
    if not profile_file.exists():
        profile_file.write_text(args.profile + "\n", encoding="utf-8")
    print("SCAFFOLD_CREATED; no analyses, figures or paper were generated")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
