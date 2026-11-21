# Verified methodology and inspiration sources (checked 2026-11-21)

1. **Li Z et al.**, *Integrative bulk and single-cell transcriptomics identifies a HERC5-linked immune-attenuated risk program for pulmonary metastasis/relapse in osteosarcoma*. Translational Oncology. Online 2026-10-10, issue volume 74 (Dec 2026); DOI: https://doi.org/10.1016/j.tranon.2026.103070 ; PMCID: PMC13677953. Discovery TARGET-OS nine-gene apparent AUC=0.922; GSE21257 seven-gene reduced implementation AUC=0.728; cross-cohort endpoint and feature set differ. The design is inspiration, not a reproducibility benchmark.
2. **Collins GS et al.**, TRIPOD+AI statement. BMJ (2024), 385:e078378. https://doi.org/10.1136/bmj-2023-078378 ; transparent reporting of prediction model research.
3. **Moons KGM et al.**, PROBAST+AI. BMJ (2025), 388:e082505. https://doi.org/10.1136/bmj-2024-082505 ; risk of bias, applicability, prediction-model development/evaluation.
4. **Osorio D et al.**, scTenifoldKnk: virtual knockout via scGRN. Patterns (2022), 3:100434. https://doi.org/10.1016/j.patter.2022.100434 ; computational network inference, not wet-lab knockout/overexpression.
5. **Langfelder P and Horvath S**, WGCNA package FAQ. https://edo98811.github.io/WGCNA_official_documentation/faq.html ; discourage WGCNA with fewer than 15 samples; prefer >=20.
6. **muscat differential state vignette**, Bioconductor (consult version corresponding to installed R). https://bioconductor.org/packages/release/bioc/vignettes/muscat/inst/doc/analysis.html ; donor-by-cell-type pseudobulk and biological replication.
7. **OpenAI Codex skill format**, https://learn.chatgpt.com/docs/build-skills ; `SKILL.md` metadata and progressive disclosure.

These sources verify *methodological rules*. They do not provide user-project results. Check the journal's current figure, ethical and data-availability policies at time of submission.
