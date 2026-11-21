# Optional 100-panel visual vocabulary — choose by question, never by quota

This is a **catalog of candidates**, NOT an instruction to draw 100 ungrounded panels. For each selected panel, insist on real input, distinct scientific hypothesis, inference/uncertainty, panel-source table and a claim in Results. Combine related panels into coherent main figures. Reject unsupported or redundant ones.

## A. Clinical cohort and data lineage
A01 cohort inclusion Sankey; A02 cohort-by-modality coverage matrix; A03 patient overlap UpSet; A04 specimen timing strip; A05 event-time distribution; A06 missing-clinical-covariate map; A07 baseline characteristics dot/raincloud; A08 cohort-batch PCA; A09 disease-by-platform coverage heatmap; A10 primary endpoint decision diagram.

## B. Normal atlas and tumor-vs-normal biology
B01 GTEx tissue clustered gene matrix; B02 GTEx tissue ridgelines; B03 GTEx tissue-specificity tau; B04 normal tissue multi-gene dot; B05 paired tumor-adjacent slope chart; B06 tumor-adjacent paired effect forest; B07 cancer-by-gene logFC matrix; B08 cancer-by-gene adjusted q matrix; B09 paired volcano with multiple testing; B10 consistency by tissue and assay platform; B11 transcript ranks across all cancers; B12 genotype/expression context paired strips.

## C. Complex coherence, genomics and multi-omics
C01 gene-group membership matrix; C02 module score heatmap; C03 pairwise residual expression correlation; C04 tumor-vs-normal coordination delta; C05 leave-one-tissue-out module effects; C06 CNV dosage-expression plot; C07 oncoprint; C08 methylation-expression partial scatter; C09 mutation-exposure forest; C10 RNA-protein concordance forest; C11 protein differential expression matrix; C12 site-resolved phosphoproteomics volcano; C13 study-aware module preservation map; C14 protein vs transcript effect scatter; C15 orthogonal data evidence ladder.

## D. Pathways, WGCNA and immune state
D01 signed GSEA Hallmark matrix; D02 running enrichment scores; D03 leading-edge barcode; D04 enriched pathway-network graph; D05 WGCNA sample dendrogram and outliers; D06 soft-threshold scale-free/connectivity curves; D07 module dendrogram with assignments; D08 module-trait association map; D09 eigengene vs clinical risk adjusted forest; D10 module-preservation null plot; D11 immune-signature landscape; D12 tumor purity residual plot; D13 PROGENy activities; D14 DoRothEA TF regulon matrix; D15 cross-cohort pathway replication forest.

## E. scRNA and legitimate spatial biology
E01 cell count/donor QC distribution; E02 donor-integrated global UMAP; E03 cell label marker dotplot; E04 ten-gene cell-type dotplot; E05 gene UMAP panels; E06 grouped module-score ridge; E07 cell-type abundance by patient; E08 donor-pseudobulk differential state forest; E09 condition-specific cell-type distributions; E10 candidate detection fraction by cell subtype; E11 pseudo-bulk vs bulk rank concordance; E12 cell-type WGCNA/module expression heatmap; E13 actual tissue morphology + spatial spot overlay; E14 spatial neighborhood co-occurrence null; E15 spatial cell-state proximity effect by tissue; E16 true spatial ligand-receptor adjacency with tissue-level replication.

## F. Clinical survival and prognosis
F01 30+ cancer Cox forest (all reportable types); F02 gene x cancer adjusted HR matrix; F03 core vs accessory module HR contrasts; F04 continuous-risk spline; F05 KM + at-risk table; F06 time-dependent ROC at multiple horizons; F07 optimism-corrected C-index; F08 IPCW Brier over follow-up; F09 horizon-specific calibration; F10 clinical baseline vs biomarker incremental value; F11 stage/purity/proliferation-adjusted models; F12 external-cohort transport and heterogeneity; F13 subgroup interaction forest; F14 competing-risk cumulative incidence, if indicated; F15 all cancers no-data/negative matrix.

## G. ML and explainability
G01 train/outer-test partition flow; G02 nested-CV score distribution; G03 held-out ROC with CI; G04 held-out PR-AUC with prevalence; G05 model comparison forest; G06 stable feature-selection consensus; G07 model coefficients and CI; G08 SHAP beeswarm; G09 SHAP dependence; G10 SHAP interaction matrix; G11 SHAP combined interaction plot; G12 leave-one-gene-out ablation; G13 random-gene matched null; G14 label permutation null; G15 partial dependence/ICE with distribution; G16 train size learning curves; G17 calibration/threshold utility; G18 missing-gene platform transfer heatmap.

## H. Perturbations, pharmacogenomics and translational filtering
H01 virtual KO network effect ranking; H02 virtual KO perturbed network graph; H03 KO enrichment/leading edge; H04 donor/subtype perturbation stability; H05 matched null targets versus actual target; H06 CellChat outgoing/incoming signal balance; H07 ligand-receptor dotplot with cell pair direction; H08 network differential edge forest; H09 DepMap dependency lineage violin; H10 GDSC/PRISM response association; H11 gene score vs observed IC50 partial correlation; H12 drug-signature reversal rank; H13 reversal-vs-sensitivity triangulation; H14 multi-modal biomarker evidence matrix; H15 target nomination volcano; H16 final shortlist/negative list funnel.

## Layout selection rules
Each main figure should have one question and (when possible) 5–10 panels: context -> main effect -> robustness -> independent validation -> interpretation. Never place a UMAP, volcano, or forest just for aesthetic diversity. Different questions can justify different panel counts; text remains subordinate to data.
