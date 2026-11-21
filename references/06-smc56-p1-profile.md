# Optional project profile: HUMAN SMC5/6 pan-cancer P1 ONLY

Use this module only for the Homo sapiens pan-cancer SMC5/6 P1 project. Do not import Candida albicans expression or structural subunit experiments into human RNA/protein cancer analyses. Respect the project's confirmed `figure_manifest` if one exists and preserve approved canonical figures; the mapping below is a default only. Exactly **8 main figures + 4 supplementary figures** in FINAL_SUBMISSION. Keep additional analyses as panel-source datasets until integrated, not unbounded extra main figures. PNG is the required final figure format.

## Biological scope
Audit all ten nominated SMC5/6-related genes with frozen gene symbols, gene aliases and Ensembl mappings from the real project dictionary, not an invented symbol list. Treat SMC5/SMC6 core, NSMCE1/2/3/4, SLF1/SLF2 and SIMC1/EID3 as project-defined members **only after checking actual dictionary**. Distinguish core physical complex membership from accessory/functional groups. Four pre-defined module combinations: C1 SMC5+SMC6; C2 SMC5/6+NSMCE1/2/3/4A; C3 SLF1+SLF2; C4 SIMC1+SLF2. Verify whether each denominator/score is consistent with the project's frozen implementation.

## Evidence progression
GTEx/HPA normal baseline -> paired tumor/adjacent TCGA/GDC effect -> per-cancer module coordination/decoupling and purity/proliferation-adjusted effects -> CNA, mutation, methylation and protein/phospho replicates -> tumor and immune cell subtypes in public scRNA -> real spatial if sources exist -> 30+ cancer-specific survival analyses (N/events and no-data rows) -> train-test-out-of-sample ML explanatory comparison -> DepMap/GDSC response/CRISPR support -> short biomarker list and long negative list.

## Suggested 8 + 4 map (override only if audit requires)
- Fig01 — GTEx baseline, GDC pan-cancer atlas, paired tumor-adjacent effects, cohort denominators and negative result overview.
- Fig02 — SMC5/6 core-complex coherence, C1–C4 module decoupling, residuals after purity/proliferation, genetic and epigenetic determinants; optional WGCNA module preservation.
- Fig03 — protein and phosphoprotein concordance, external verification, cross-modality specificity and unresolved findings.
- Fig04 — single-cell cell-state distribution, donor-level differential states, robust signature mapping and (only if real coordinates) spatial biology.
- Fig05 — GSEA/immune/DNA-repair pathway evidence, WGCNA networks, module/phenotype links and alternative explanations.
- Fig06 — pan-cancer OS/PFS/DSS/DFS with clinically adjusted Cox forests, event counts, heterogeneity, external replication and calibration where feasible.
- Fig07 — nested CV and independent ML comparisons, SHAP, stability/ablation/null controls, incremental value beyond simple clinical models.
- Fig08 — CRISPR dependencies, measured drug response, virtual perturbation hypothesis, translational prioritization and biomarker evidence matrix.
- FigS01 — input audit and GTEx/tumor-normal tissue quality controls; 30+ cancer negative inventory.
- FigS02 — module statistical sensitivity and genetic confounder analyses.
- FigS03 — cell/spatial QC, negative perturbation controls and cohort replication caveats.
- FigS04 — detailed prognostic/ML robustness, drug-screen source coverage and rejected candidates.

## Existing asset handling
Known previously reported assets include a GDC pan-cancer atlas, a large single-cell atlas of 391,963 cells/132 donors/13 studies, and earlier P1A/P1B drafts. These numbers are **historical project context only** and must be re-read from current source files before insertion in the paper. If a current approved Fig01 GDC atlas or Fig06 single-cell atlas exists, preserve its approved content and figure number (do not silently override with the suggested map). Re-index the remaining mapping around verified canonicals. Preserve genuinely independent P1A paired discovery versus P1B network/residual insight without declaring correlated evidence independent.

## Specific downgrades and pitfalls
- LUAD S68 phosphopeptide previously had limited phosphosite-localization/replication evidence; no claim of validated S68 function without source PSM and independent proof.
- If Visium HD or other spatial coordinates/source matrices are unavailable, do not simulate real spatial data or call embeddings spatial.
- Use leave-one-tissue-out/leave-one-cancer-out, proliferative genes matched null, independent batch/technology cohort checks, and evidence-traceable negative results.
- No forced universal pan-cancer biomarker: phenotype-specific shortlists are often scientifically stronger.
