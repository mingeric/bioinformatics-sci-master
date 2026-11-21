# Bioinformatics SCI Master Skill

**Evidence-first execution skill for SCI-grade computational biology papers.**

A single Skill (Agent Skills / Codex-compatible) that turns one testable biological or clinical question into a coherent, independently supported, publication-grade computational study — with real computations, audited figures, machine-readable evidence tables, and manuscript text that all agree.

> **Core principle:** not "stack LASSO + WGCNA + XGBoost + SHAP + CellChat + virtual knockout", but every analysis answers the question left open by the previous one, forming an evidence chain that can be independently verified and written directly into an SCI paper.

---

## What it does

| Capability | Reference file |
|---|---|
| Study design, endpoints, evidence tiers | `references/01-study-design-and-evidence.md` |
| Algorithm selection & runnable analysis logic (ML, survival, WGCNA, scRNA-seq, spatial, perturbation, drug response) | `references/02-methods-and-algorithms.md` |
| Publication figure layout & design rules | `references/03-figures-and-design.md` |
| Natural, high-precision manuscript writing & review | `references/04-scientific-writing-and-review.md` |
| Release, auditing, quality gates & truthful status reporting | `references/05-release-and-quality-gates.md` |
| SMC5/6 human pan-cancer project profile (8 main + 4 supplementary figures) | `references/06-smc56-p1-profile.md` |
| Verified source papers & living standards | `references/07-verified-sources.md` |
| 117-candidate figure panel library | `references/08-figure-panel-library.md` |

**Report standard** follows TRIPOD+AI / PROBAST+AI thinking for prediction-model reporting and bias review, plus biological-replicate principles for single-cell analysis.

## Non-negotiable contract

1. **Never invent** — no patients, p-values, AUCs, DEGs, cell annotations or validation. Every quantitative claim links to its exact source table, code, parameters and sample denominator.
2. **Prevent leakage** — outcome-informed feature selection, preprocessing and hyperparameter tuning stay inside training folds; external cohorts untouched until model lock.
3. **Separate evidence levels** — expression association ≠ adjusted association ≠ prediction ≠ network inference ≠ virtual perturbation ≠ experimentally supported causality. Claims are labeled accordingly.
4. **Results precede writing** — tables → analyses → panels → legends → Results → Discussion → Abstract → title. No cherry-picking a storyline.
5. **Truthful status** — COMPLETE / PARTIAL / BLOCKED / NOT RUN are reported accurately. Scaffolding alone never counts as a completed analysis.

## Installation (Codex / macOS)

```bash
mkdir -p ~/.agents/skills
unzip -q ~/Downloads/Bioinformatics_SCI_Master_Skill_v1.zip \
  -d ~/.agents/skills/
# or: git clone https://github.com/mingeric/bioinformatics-sci-master \
#       ~/.agents/skills/bioinformatics-sci-master
```

Then invoke in a Codex project:

```
$bioinformatics-sci-master

Execute an evidence-first SCI bioinformatics paper.
Audit existing data and figures, run supported analyses,
generate publication-grade PNGs, and synchronize the
manuscript, methods, legends and evidence tables.

For SMC5/6 P1: exactly 8 main + 4 supplementary figures.

Validate the canonical release. Never invent results.
```

A ready-to-paste task prompt is included at `templates/CODEX_EXECUTION_PROMPT.md`.

## Tools included

- `scripts/init_project.py` — project scaffolding (`analysis_plan.md`, `data_inventory.csv`, `cohort_ledger.csv`, `results/`, `figures/`, `scripts/`, `manuscript/`, `FINAL_SUBMISSION/`, …)
- `scripts/audit_release.py` — technical integrity audit for one canonical release: manifest/evidence CSV schema checks, PNG signature + chunk-CRC validation, SHA256 verification. **Not** a scientific truth verifier — substantive human review of statistical/biological validity is still required.

Tested behavior: empty project correctly triggers acceptance failure; 12-PNG integrity audit passes. This verifies tool behavior only — it does not mean any real biological analysis has been run for your project.

## Quick start

```bash
python scripts/init_project.py --root ./my-study   # scaffold
# ... run your analyses ...
python scripts/audit_release.py --root ./my-study  # gate report (PASS/FAIL)
```

## The decision rule behind every analysis

```
Question -> necessary input -> experimental/statistical unit -> comparison & confounders
-> method -> quantitative estimand -> independent validation -> figure
-> evidence classification -> manuscript claim
```

If any required component is missing, the claim is omitted/downgraded instead of fabricating or adding decorative analysis.

## Module coverage

TARGET · GDC/TCGA · GEO · ICGC · GTEx · HPA · CPTAC · ProteomeXchange · DepMap · GDSC · PRISM/CTRP · LINCS/CMap · Seurat/Scanpy · WGCNA · penalized Cox/logistic · RSF · XGBoost · SHAP · time-dependent ROC · IPCW Brier · calibration · net benefit · scTenifoldKnk · CellOracle · Geneformer · CellChat · PROGENy · DoRothEA

## License

MIT — see [LICENSE](LICENSE).
