# Statistical and computational algorithm playbook

## 1. Data processing / DEG
Use versioned manifests (URL/accession, downloaded timestamp, checksum, human genome build, mapping release). For RNA-seq counts run DESeq2/edgeR using count-aware design, include known batch and biological covariates. Predeclare filtering and contrasts, use BH FDR, effect sizes and shrinkage if supported. Use `limma` with appropriate normalized continuous microarray/log expression data. Avoid DESeq2 on TPM/FPKM. For tumor vs adjacent, respect pairing via patient design. Validate sample identity and survival encoding.

## 2. ML screening with stability
- Compare LASSO, elastic net, random forest, SVM-RFE and XGBoost where appropriate; do not treat five highly correlated selectors as five independent replications.
- Outcome-guided DEG screening is part of feature selection and must occur **inside each resampling training set** when evaluating prediction. Do not perform DEG on all patients before CV and claim resulting CV as unbiased.
- Outer stratified group CV / temporal splits / leave-one-cohort-out; inner folds for all data-dependent preprocessing, selection and tuning; donors/patients are groups.
- Stability: feature selection frequency under bootstrap/repeated inner CV; null label-permutation (full training pipeline repeated), random feature controls with matched expression/prevalence, deletion of single feature and cancer/cohort holdout.
- Estimate optimism-corrected or nested-CV AUC/AUPRC as relevant, confidence intervals by participant bootstrap. Never call training-set AUC external validation.
- For cross-platform scores, lock coefficients, gene order, normalization reference, assay mapping, missing-gene rule and thresholds **prior** to reading test labels. Report reestimated/abbreviated scores separately.

## 3. Survival
Use Cox with PH diagnostic and nonlinearity checks; consider penalized CoxNet, RSF, boosted survival methods only with sufficient events. Evaluate Harrell/Uno C as applicable, horizon-specific IPCW AUC and Brier, calibration at prespecified horizons, DCA after proper probability calibration, adjusted HR/CI, external validation. KM is descriptive after locked threshold; a prognostic classifier trained with future outcome cannot be treated as a causal exposure. Avoid pooling OS and DFS. For 30+ cancer types, output all N/event strata, model failures, multiple-testing family, forest plot, meta-analysis or hierarchical estimates and heterogeneity (not cherry-picked positive cancers).

## 4. WGCNA
Construct on properly normalized, outlier-screened samples with relevant variance and sufficient independent subjects (authors recommend not fewer than 15, prefer >=20). Choose soft power with fit/connectivity tradeoff, show module dendrogram, preservation and eigengene correlation. Relate modules to **external phenotype/immune variables**, adjust confounders, cross-validate findings. Candidate gene module membership kME and gene significance are exploratory; never assert hub causality from degree alone. Consider robust bicor and cross-cohort preservation.

## 5. Immune and molecular mechanisms
GSVA/ssGSEA/UCell, ESTIMATE, MCP-counter/xCell/CIBERSORTx when data licensing permits, with purity and cell-composition caveats. Hallmark/Reactome/GO/KEGG pre-ranked GSEA with explicit ranking metric, background gene universe, permutation strategy, FDR and NES. PROGENy infers signaling activity; DoRothEA infers TF regulon activity. Report direction and cross-cohort concordance; avoid pretending pathway inference is phosphoproteomic measurement.

## 6. Single-cell and spatial
Use donor-resolved QC (genes/counts/mitochondrial fraction/doublets) with dataset-specific thresholds, ambient RNA and donor-batch integration; verify cell labels with multiple markers. Give donor counts and cell counts separately; cells are not independent biological replicates. Differential states between groups: pseudobulk by donor x cell type with edgeR/DESeq2/limma or mixed models with donor effect. Map bulk classifier only where its gene-set coverage and expression scale are appropriate; distinguish single-gene expression vs signature-score projection. Spatial only with genuine spatial count matrices/coordinates; infer neighborhood effects with tissue-level biological replication; do not call UMAP coordinates anatomical space.

## 7. Virtual perturbation
scTenifoldKnk: infer wild-type scGRN, virtually remove target regulatory influence and rank manifold/network changes. Use adequate target detection and cell count, fixed seeds, sampling stability, negative control target genes matched on expression/network degree, cell-subtype and donor sensitivity. It does not perform a physical knockout or quantify experimental DEG or overexpression. CellOracle/Geneformer/scTenifoldNet have different prerequisites and prediction semantics; use only compatible models and clearly report input and output. If expression or inferred GRN is inadequate, mark NOT RUN rather than make a synthetic KO plot.

## 8. Cell-cell communication
CellChat/CellPhoneDB/NicheNet infer putative ligand-receptor links from expression, not demonstrated secreted signaling. Perform group- and donor-aware comparisons, minimum cell counts, randomization/robustness, connect to spatial neighborhoods if genuine tissue coordinates exist. Distinguish source, receptor and responding cell types, include source genes and database versions.

## 9. Pharmacogenomics and in silico reversal
GDSC, PRISM, CTRP, DepMap CRISPR provide different endpoints; distinguish IC50/AUC direction and expression confounders, use cell-line lineage conditioning and multiple testing. LINCS/CMap/DSigDB reverse disease gene signatures: rank perturbagens with cell-line, time, dose and signature coverage; this is **hypothesis generation**, not measured drug sensitivity or clinical efficacy. Require independent sensitivity/dependency support to upgrade the candidate.

## 10. Optional advanced methods
Only if extra evidence exists: matched tumor-normal proteomics/phosphoproteomics, mutation-CNV-expression mediation hypotheses, multi-omics latent factors (MOFA+/DIABLO), tumor subtyping with held-out reproducibility, causal inference when assumptions and time order are defensible, domain adaptation without test-label leakage, leave-tissue-out or leave-cohort-out transfer, spatial colocalization, validated functional QTL. A larger algorithm menu does not strengthen a weak endpoint.
