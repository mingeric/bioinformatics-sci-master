# Scientific writing: natural, precise, rigorous, not machine-generic

## Evidence-grounded writing order
1. Freeze results and analysis definitions, generate `results_master.tsv` with validated numbers and figure references.
2. Construct claim-evidence matrix: for each paragraph one question, one result, one limitation/interpretation, relevant source data.
3. Write Results in figure order, by inference level. Start paragraph with observation, follow with effect/CI/N/assay, then clear biological interpretation. Do not inflate a computational association into a mechanism.
4. Write Methods in actual execution order: accession/version, inclusion, preprocessing, full formulas, covariates, splits, algorithms/hyperparameters/seeds, software versions, QC thresholds, multiple testing, inference/ablation, availability.
5. Write Discussion as: central contribution, comparison with best available literature, mechanistic alternatives, source of heterogeneity, external validity/limits, discriminating future validation. Null findings should alter interpretation.
6. Write Abstract and title last, using only validated terms (risk association vs prognostic marker vs predictive biomarker, inferred knockout vs functional test).

## Natural prose rubric
Use field-specific nouns and strong factual verbs; vary sentence rhythm and paragraph structure; keep a single thread of logic. Avoid formulaic 'In the rapidly evolving landscape', 'notably/remarkably' repeated, grand claims, vague promises, repeated synonyms, generic AI-sounding abstracts and ritual self-congratulation. Do not aim to deceive AI detectors; aim for transparent human-readable scientific precision. Use active voice when the actor/method matters. Quantify rather than 'significantly higher' without effect. Explicitly distinguish independently replicated vs circularly cross-confirmed results.

## Claim strength vocabulary
- Association: "was associated with", "correlated with", "displayed higher expression".
- Prediction: "discriminated outcomes in the held-out cohort", "improved out-of-sample calibration".
- Inference: "was consistent with", "suggested", "prioritized a regulatory hypothesis".
- Experiment/causal: only use "demonstrated", "mediated", "caused", "restored" when actual intervention and proper controls warrant it.
- Drug: "transcriptional signature reversal candidate" versus "increased drug sensitivity in cell lines" versus "clinical treatment benefit" are different claims.

## Paragraph template (adapt, never copy blindly)
"Among [N patients] with [event definition], [model/exposure] was associated with [effect, CI, q]. The association [persisted/attenuated] after adjusting for [predefined covariates]. [Independent dataset/platform] showed [effect or lack of replication], delimiting the finding to [context]."

## Manuscript coherence checks
- Every numerical statement appears in a real source table and figure panel; no hand-typed stale AUC or N.
- Every figure legend states modality, cohorts, adjustment, effect direction, significance convention and inferential status.
- Each manuscript claim matches its computed statistical unit and whether a result was in discovery, internal validation or independent validation.
- Missing genes, unavailable spatial input, prior genome build mismatch and insufficient biological replicates are disclosed exactly.
- Abstract and conclusions match strongest validated evidence, not strongest-looking plot.

## Reporting and references
- Model papers: apply TRIPOD+AI reporting and PROBAST+AI quality/bias assessment; REMARK for tumor-marker studies when relevant; STROBE for observational study descriptions as appropriate.
- Avoid citing a paper you have not checked; capture DOI/PMID and validate claim-to-reference match. Use references/07-verified-sources.md as a starting point, not as evidence that a dataset was downloaded.
- Provide Data Availability, Code Availability, Ethics/consent context, software/environment lock and sensible limitations.

## Editorial final pass
Delete redundant openings, generic bridge phrases, overbroad mechanistic verbs, repeated interpretation and unnecessary wordiness. Preserve specialized biology, nuance and supported quantitative detail. Never rewrite away real negatives to make a smoother narrative.
