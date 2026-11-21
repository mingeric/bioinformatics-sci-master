---
name: bioinformatics-sci-master
description: Design, execute, audit, visualize and write reproducible SCI-grade computational biology papers from genuine public or user-supplied omics and clinical data. Use for pan-cancer biomarker discovery, multi-omics, bulk RNA-seq, survival/ML, WGCNA, scRNA-seq, spatial, virtual perturbation, immune analysis, drug response and journal submission. Invoke for study design, analysis expansion, manuscript revision, figure integration or final release. Do not invoke for wet-lab-only protocols or generic prose editing unrelated to bioinformatics.
---

# Bioinformatics SCI Master — evidence-first paper engine

## Mission and non-negotiable contract
Turn one testable biological or clinical question into a coherent, independently supported, publication-grade computational study. Deliver actual computations and editable scripts, high-resolution PNG figures, machine-readable evidence tables and manuscript text that all agree. **Depth of evidence outranks number of tools.** Add methods only when they address an unanswered question and appropriate source data exist.

1. **Inspect before proposing:** inspect accessible project files, data dictionaries, completed figures, scripts, logs and statistical tables. Preserve supported analyses; do not start redundant pipelines. Do not claim access to a local path on another computer.
2. **Execute, not narrate:** when input data and tools exist, run analyses, generate figure PNGs, validate and package in this turn/session. If blocked, provide a precise runnable command/config and identify missing files. Never describe planned work as completed.
3. **Never invent:** patients, datasets, p values, event counts, AUC, risk ratios, DEGs, coordinates, pseudo-spatial data, cell annotations, drug effects or validation. Every quantitative claim must link to its exact source table, code, parameters and sample denominator.
4. **Prevent leakage:** external folds are untouched until model lock. Feature selection, preprocessing, imputation, scaling, DEG-derived filtering, batch adjustment and hyperparameter optimization are performed inside training folds when outcome-informed. For time-to-event data define index date, censoring and prediction horizon.
5. **Separate evidence levels:** expression association, adjusted association, prediction, network inference, virtual perturbation, spatial co-localization and experimentally supported causality are different claims. Label them accordingly. No drug-screen hit is a therapeutic recommendation.
6. **Protect canonicals:** before overwriting any current deliverable, inventory files + SHA256 and keep one versioned backup. Rebuild only from source; atomic replacement after validation. Archive obsolete drafts only after dependency audit. No blanket recursive deletion.
7. **Results precede writing:** generate tables -> analyses -> panels -> legends -> Results -> Discussion -> Abstract -> title. Do not choose a positive storyline and cherry-pick outputs. Record null/negative findings and thresholds.
8. **Source-of-truth release:** maintain one canonical submission root, not nested competing 'FINAL' directories. Distinguish COMPLETE, PARTIAL, BLOCKED and NOT RUN accurately.

## Routing: load only the relevant reference
- **Study design and endpoint:** `references/01-study-design-and-evidence.md`.
- **Algorithm selection and runnable analysis logic:** `references/02-methods-and-algorithms.md`.
- **Visualizations and publication layout:** `references/03-figures-and-design.md`; optional 100+ panel candidate catalog: `references/08-figure-panel-library.md`.
- **Natural, high-precision manuscript writing:** `references/04-scientific-writing-and-review.md`.
- **Data release, auditing and reporting:** `references/05-release-and-quality-gates.md`.
- **SMC5/6 human pan-cancer project only:** `references/06-smc56-p1-profile.md`.
- **Source papers and living standards:** `references/07-verified-sources.md`.

## Six-pass execution protocol
**PASS 0 — audit:** list input datasets, raw files, accession IDs, builds, cohort IDs, unique patients, endpoints, software environments, existing figures and conflicting canonical versions. Export `data_inventory.csv`, `cohort_ledger.csv`, `assumptions.md`, `analysis_plan.md`. Never silently substitute simulated or processed values for missing real data.

**PASS 1 — questions and feasibility:** define one primary endpoint, one principal hypothesis, falsifiable null and relevance criterion; predefine outcomes and covariates. Assign each analysis to a question and unique output panel. Branch by endpoint: binary classification, survival, continuous response, cancer-vs-normal, cell-state or treatment response. Choose cohort-level independence and proper unit of replication.

**PASS 2 — computation:** perform normal baseline -> discovery -> cross-cancer/cross-cohort replication -> feature/complex/module analyses -> clinically adjusted models -> bulk/immune/WGCNA -> single cell/spatial -> virtual perturbation -> drug-response triangulation, only as justified. Favor contrasting independent sources and matched negative controls over stacking correlated analyses.

**PASS 3 — model evaluation:** compare simple clinical baseline, regularized Cox/logistic model and justified alternatives (elastic net, random forest/RSF, XGBoost). Use nested CV or bootstrap optimism correction; held-out cohorts for transportability; add calibration, confidence intervals, clinical utility and ablation; record feature stability and missing-gene strategy. SHAP is explanatory about the fitted model, not proof of mechanism.

**PASS 4 — figure production:** write independent panel-level source tables and scripts. All panels show question, statistical estimand, N/events/cohorts, adjustment and uncertainty where appropriate. Export archival PNG only if PNG is requested; normally PNG + SVG/PDF optionally. Fixed style, color scales and figure geometry; use a contact sheet and inspect it visually. Avoid generic workflow cartoons in place of real biology.

**PASS 5 — writing and release:** write IMRaD narrative that follows evidence and makes testable claims; synchronize Methods, Results, legends, tables and source data. Run release audit and produce `FINAL_SUBMISSION/` with canonical `Fig01..`, `FigS01..`, manuscript, extended Methods, supplemental tables, source code and provenance. Stop with an accurate gate report.

## Use this decision rule for every new algorithm
`Question -> necessary input -> experimental/statistical unit -> comparison and confounders -> method -> quantitative estimand -> independent validation -> figure -> evidence classification -> manuscript claim`.
If any required component is missing, omit/downgrade the claim instead of fabricating or using decorative analysis.

## Typical module selection
- **Clinical event & multi-cohort:** TARGET, GDC/TCGA, GEO, ICGC or disease-specific clinical collections; assess harmonization and endpoint comparability.
- **Normal baseline & tumor changes:** GTEx, paired TCGA/GDC normal, HPA; prefer matched tumor-adjacent comparisons, distinguish assay scales.
- **Multi-omics:** CPTAC, ProteomeXchange, mutation, CNV, methylation, phosphorylation, co-dependencies; claim replication only when measuring appropriately matched biological effects.
- **ML & prognostics:** penalized regression, CoxNet, RSF, XGBoost, SHAP, time-dependent ROC, C-index, IPCW Brier/calibration and net benefit when defensible.
- **Modules & microenvironment:** WGCNA, pathway activity, immune signatures and deconvolution; check purity/proliferation and confounding.
- **Cellular evidence:** Seurat/Scanpy, donor-level pseudobulk, trajectory only where identifiable, spatial only with genuine coordinates and tissue-level files.
- **In silico perturbation:** scTenifoldKnk, CellOracle, Geneformer, scTenifoldNet and CellChat are optional hypothesis-generation tools, not interchangeable experimentally validated knockouts.
- **Drug evidence:** GDSC/DepMap, LINCS/CMap, PRISM/CTRP when accessible; separate sensitivity measurements from transcriptional reversal predictions.

## Required outputs and truthful status
When execution is possible: `analysis_plan.md`, `data_inventory.csv`, `cohort_ledger.csv`, `results/`, `figures/`, `scripts/`, `figures/figure_manifest.csv`, `evidence_ledger.csv`, `manuscript/`, `FINAL_SUBMISSION/`, `QA_REPORT.md`. All outputs must be real artifacts, not empty compliance placeholders. Use `scripts/init_project.py` for scaffolding; `scripts/audit_release.py` for acceptance testing. Scaffolding alone does not count as a completed scientific figure or paper.

## Handoff response format
Report: (a) scientific claim supported; (b) actual computations and exact artifacts; (c) figures rendered and passed; (d) unresolved blockers and claim downgrades; (e) the shortest executable next action if blocked. No indefinite 'running in background' promises.
