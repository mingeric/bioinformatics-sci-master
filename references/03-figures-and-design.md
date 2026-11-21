# Publication-grade figure system (PNG-centric)

## Visual design contract
White/light background; scientific grid; consistent sans-serif; subtle muted strokes; aligned panels with no clipping and sufficient legend legibility. Use a restrained color palette with stable mapping for risk groups, cell types and modules. Colorblind-safe continuous diverging schemes with one *global* common range for comparable matrices. Do not force global scale when measurement units differ; label assay-specific units. White means missing only with separate missing legend; zero expression must remain distinguishable from missing.

## Figure engineering
Each figure must be evidence dense, but a panel only earns space if it answers a different question. Favor 5–10 coherent panels per main figure where data justify it; prefer heatmaps, paired effect plots, ridgelines, raincloud/violin, volcano, forest, Sankey, oncoprint, GSEA ES traces, Kaplan–Meier, calibration, decision curves, network layouts, UMAP, spatial spots, beeswarm SHAP, dependency/interaction/ablation plots. Avoid repeated bar plots, oversized text panels, 3D cones, radial radar charts and illegible strings.

Suggested journal layout: 180–190 mm wide main figures, font readable after placement (~7–9 pt labels, ~9–11 pt panel headers) and 300–600 dpi PNG as target; inspect pixel dimensions and target journal requirements. Prefer Matplotlib/ggplot2 with layout grids, not full-slide raster screenshot re-export. Use significance annotation with test, correction, N, CI/effect size. Use per-panel English title limited to a scientific clause.

## Panel provenance schema
`figure_id, panel_id, scientific_question, input_table, dataset_id, n_patients, n_events, n_donors, n_cells, method, comparison, effect, ci, p_value, q_value, unit, code, output_png, status, evidence_tier`. Empty fields must mean not applicable/unavailable, never fabricated zeros.

## Recommended plot library, categorized by question
- **Cohort and data identity:** Sankey/consort, UpSet, paired coverage heatmap, cohort x assay matrix, QC ridges, tissue distribution small multiples.
- **Normal-vs-tumor atlas:** tissue x gene heatmap, ridge/violin, paired slope, volcano, forest by cancer, cancer x gene effect matrix, GTEx tissue specificity tau, patient-level dot.
- **Molecular context:** oncoprint, CNV dosage scatter, methylation vs expression hexbin, mutation burden forest, gene-gene partial correlation network, WGCNA TOM/dendrogram and preservation map.
- **Pathways:** preranked GSEA traces, ranked barcode, signed pathway matrix, leading-edge overlap, network enrichment with readable node/edge counts.
- **Protein/phospho:** concordance forests, peptide coverage, site-level volcano, assay scatter with CI and cohort label; no protein claim from RNA data.
- **Single-cell:** UMAP with cells, cell fractions by donor, gene violin/dotplot with detection rates, differential-state forests, module states across cell types, patient pseudobulk heatmap, trajectory with confidence where valid.
- **Spatial:** real tissue H&E + spot coordinates, gene/module overlay on actual sections, neighborhood effect distribution by tissue, ligand-receptor proximity test.
- **Survival:** 30+ cancer forest (rows sorted logically), KM with numbers at risk, time-dependent AUC, baseline vs adjusted model performance, calibration and decision-curve where estimable.
- **ML:** nested-CV score distribution, ROC/PR with CIs, XGBoost/RSF/CoxNet comparison, SHAP beeswarm/dependence/interaction, stability heatmap, bootstrap CI, learning curves, missing-feature ablation.
- **Virtual perturbation and drug:** target-on/target-off GRN change graph, perturbation ranked effect vs null, cross-method overlap, drug reversal connectivity plot, observed GDSC response distribution, CRISPR dependency lineage comparisons.

## Integrative figure rule
Story: panel A cohort and denominator -> panel B main observation -> panel C effect size/uncertainty -> panel D complementary evidence -> panel E negative control -> panel F conclusion linked to next figure. Recompute layout after content selection rather than shrink everything to fit. Render a contact sheet and inspect every panel at page display size for typography, label overlap, gradients, false-colour meaning and crop.

## Reviewer defense
Precalculate negative controls, leave-one-cohort/cancer-out, null distributions and calibration. Report chart semantics (x/y, scaling, missing values), per-group N, FDR family, and whether biological unit is patient/donor/cell. Never hide the number of untestable cancers.
