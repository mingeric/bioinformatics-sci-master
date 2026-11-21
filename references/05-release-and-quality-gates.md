# Execution and acceptance gates

## Canonical hierarchy
project/
  data/raw/ (immutable; do not ship controlled raw data)
  data/processed/ (content-addressed, versioned)
  metadata/ (cohort_ledger.csv, data_inventory.csv)
  code/ (reproducible scripts, environment lock, workflow commands)
  results/ (tested tables/objects)
  figures/ (Fig01.png... and optional panel sources)
  manuscript/ (manuscript text, full legends, supplementary methods)
  FINAL_SUBMISSION/ (only validated deliverables, not logs/cache)
  QA_REPORT.md

## Mandatory checks
**Q0 Input:** accession, download source, assay, condition, patient/event/donor N, checksum and genome/gene IDs. **Q1 Correct inference:** statistical unit, leak-free nested resampling, covariate set, censoring and multiple testing. **Q2 Independent replication:** distinct cohort ID, phenotype consistency and platform feature coverage. **Q3 Claim level:** separate measurement from inference; no unvalidated drug efficacy, no physical spatial claims from UMAP. **Q4 Figures:** parse PNG, pixel dimensions, orientation, legibility, panel manifest/legend and units, n, p/q. **Q5 Manuscript:** every figure and number has ledger path, DOI/PMID references verified, no placeholder. **Q6 Release:** exactly one canonical release; only approved figure count and no broken links.

Every figure has complete panel-source records and a machine-readable `figure_manifest.csv`. Status vocabulary: COMPLETE (input, calculation, output + inspection exist), PARTIAL, BLOCKED, NOT_RUN. Do not mark COMPLETE for 'template drawn' or 'process launched'.

## Safe replacement
1. Record `sha256sum` manifest of existing canonical files.
2. Build into staging directory (never directly onto approved files).
3. Validate source data, figure pixels, labels, style, dimensions, numeric cross-check and textual claims.
4. Snapshot original into dated backup / archive, and atomically swap staged outputs.
5. Confirm all expected files exist, counts match, hashes stable and obsolete outputs have no live references.
6. Delete duplicates only from an explicit reviewed list of SHA256-identical or verified superseded paths. Preserve raw, processed and unique data and scripts.

## Fatal scientific errors (fail release)
- Training set called external validation; leakage from global feature screening or scaler fitted on all patients; same patients across cohorts called independent.
- Survival data missing event/censor definition; stratified KM portrayed as independent effect without appropriate adjustment.
- Cell-level t-test as patient-level differential analysis; nonexistent spatial coordinates; virtual knockout represented as wet-lab.
- RNA values labeled protein or phosphorylation; pseudo-color rank treated as true abundance.
- Drug reversal predicted as efficacy; citations generated without checking; manually invented values or panel source missing.

## Test and deliver
- Optional `scripts/init_project.py --root PATH --profile generic|smc56-p1` creates scaffolding without fake research outputs.
- `scripts/audit_release.py --root PATH --profile generic|smc56-p1` checks completeness/manifest metadata and PNG validity. Exit code 0 only if all required checks pass.
- The validation script checks metadata existence and technical consistency; it **cannot independently certify biological truth, raw data identity or inferential validity**. Manual statistical review remains required.

## Structured final report
"Input datasets: X confirmed, Y inaccessible; primary endpoint: ...; models computed: ...; main PNG: N/N; supplement PNG: N/N; numerical provenance: N/N; full validation: PASS/FAIL with failure details; manuscript synchronized: yes/no; known scientific limitations: ...". Use direct citations or source file references.
