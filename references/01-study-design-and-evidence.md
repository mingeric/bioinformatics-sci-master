# Study design: from clinical problem to independent evidence

## Fundamental proposal
State primary clinical/biological question in a sentence, not a method list. Example: "Does a pre-treatment SMC5/6 coordination score carry prognostic information beyond stage, grade, purity and proliferation in independent cancer cohorts?" Distinguish biomarker of state (association), prognostic (natural history), predictive (treatment interaction), and causal mechanism (intervention).

Before any model, capture:
- Population/inclusion/exclusion, tumor entity, assay, diagnosis/treatment timing, repeated measures, covariates and measurement windows.
- Endpoint type: diagnosis, metastasis, recurrence, treatment response, OS/PFS/DSS/DFS; time zero, event/censor coding, competing events, longitudinal structure.
- Discovery/validation cohorts and why they are independent (not the same GDC samples repackaged in GEO).
- Target estimand and covariate set fixed before comparing results.
- Confounding strategy: tumor purity, tissue composition, histology, age, stage, grade, treatment, proliferation, TMB/aneuploidy, gene copy number; do not adjust for mediators blindly.
- Primary and secondary outcomes with multiplicity plan (BH FDR within declared test family or hierarchical hypothesis testing).

## Evidence hierarchy
E0: descriptive atlas. E1: differential association adjusted for documented confounders. E2: independent cohort/platform directional replication. E3: independent modality concordance (protein/RNA/spatial/function). E4: out-of-sample discrimination + calibration + clinical incremental value. E5: experimentally demonstrated perturbation or prospective clinical validation. Computational virtual knockouts are E1-like inferred mechanism hypotheses, **never E5**.

## Independent cohort and assay rules
- Always show N participants, sample number, event number, disease and whether matched/pseudorepeated; avoid pooling heterogeneous cancers without explicit partial pooling/interaction.
- Quantification: raw RNA counts -> DESeq2/edgeR; normalized logs for modeling, with train-only preprocessing. GTEx TPM and TCGA counts cannot be combined as raw counts.
- Platform transport: missing genes alter the model. A 7/9-gene score with retained coefficients is an abbreviated implementation, not full 9-gene external validation; report both definitions and avoid pretending endpoints agree.
- RNA-to-protein replication requires measuring the same biologically meaningful contrast in an appropriate independent cohort; correlation alone is not phenotype replication.
- Negative evidence is publishable: show distribution of unsupported candidates and maximal replication tiers rather than hiding them.

## Candidate triage
Candidate ranking may integrate: effect/CI/FDR, direction and independent cohort reproducibility; module-specificity; tumor-vs-normal effect; clinically adjusted contribution; protein and single-cell concordance; dependency/drug sensitivity; targetability. Do not convert a weighted ranking into a probability unless trained/calibrated as one.

## Research design families
**Focused modest-scale paper:** one clinical endpoint, discovery + independent validation, compact multi-method screening, WGCNA as interpretation, one compelling cell state, one hypothesis-generating perturbation, exploratory drug match. Emphasize coherent story not breadth.
**Comprehensive multiomics study:** normal atlas -> tumor-paired and cancer-specific effects -> coexpression/coordination -> multi-omics independent evidence -> sc/spatial localization -> adjusted prognosis -> ML -> experimental public validation -> drug response and short biomarker list.

## Anti-circularity rule
WGCNA based on the same feature matrix used to derive a score will often correlate with that score by construction. For inference, test eigengene associations with independent outcomes/immune programs, residualize major confounders, assess module preservation across cohorts and distinguish discovery from replication.
