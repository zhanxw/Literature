# Paper Summary: Deep-learning-based de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes

### Authors
Jing Xing, Mingdian Tan, Dmitry Leshchiner, Mengying Sun, Mohamed Abdelgied, Li Huang, Shreya Paithankar, Katie Uhl, Rama Shankar, Erika Lisabeth, Bilal Aleiwi, Tara Jager, Cameron Lawson, Ruoqiao Chen, Matthew Giletto, Reda Girgis, Richard R. Neubig, Samuel So, Edmund Ellsworth, Xiaopeng Li, Mei-Sze Chua, Jiayu Zhou, Bin Chen

### Journal
Cell

### Publication Date
April 30, 2026

### DOI
10.1016/j.cell.2026.02.016

## Keywords
- transcriptomics-based drug discovery
- deep learning
- virtual screening
- hepatocellular carcinoma
- idiopathic pulmonary fibrosis
- single-cell RNA-seq
- hit-to-lead optimization

## Main Idea
The paper presents `GPS` (gene expression profile predictor on chemical structures), a deep-learning platform that predicts compound-induced transcriptional responses directly from chemical structure, then uses those predicted profiles for large-scale virtual screening, hit prioritization, mechanism analysis, and lead optimization. The central claim is that disease-signature reversal can be extended from repurposing to de novo small-molecule discovery by imputing transcriptomic effects for compounds that have never been experimentally profiled.

## Evidence Supporting the Main Idea
- `GPS` was trained on LINCS Phase I perturbational data and predicts upregulation, downregulation, or no effect for each gene from compound fingerprints; the model was built with an `RCL` strategy to handle noisy transcriptomic labels.
- The authors report `307` predictable landmark genes out of `978`, and show stronger internal and external validation performance than baseline machine-learning and deep-learning methods in Figure 1B and supplementary benchmarking.
- The predicted profiles preserved biological structure beyond chemistry alone: compounds sharing targets or pathways clustered together in transcriptomic space, and predicted profiles aligned with shRNA knockdown signatures for `17` of `20` tested targets (Figure 2J).
- In hepatocellular carcinoma (`HCC`), the refined reversal score `Z-RGES` correlated with anti-HCC cellular activity (`Spearman R = -0.554`, `p = 0.0049`; Figure 3B), whereas raw `RGES` did not.
- Screening GPS-imputed profiles yielded an estimated `40%` top-hit rate in HCC validation (Figure 3D). One-third of `18` structurally diverse candidates from a seven-million-compound library showed significant inhibition across three HCC cell lines.
- The top HCC hit `44443110` achieved `2-3 uM` `IC50` values, and another hit `PB56874852` retained low-micromolar activity while sparing primary hepatocytes even at `100 uM`, supporting the selectivity claim.
- Hit-to-lead optimization with Monte Carlo tree search produced `MSU45302`, which showed nanomolar-level activity in three HCC cell lines and reduced xenograft tumor volume after oral dosing at `100 mg/kg` (Figure 4H).
- Mechanistic analysis linked anti-HCC activity to predicted downregulation of cell-cycle genes including `CDC25A`, `MCM2`, `MCM4`, `UHRF1`, and `MCM6`, and the paper backs this with xenograft RNA-seq, knockdown experiments, patient survival analysis, and spatial transcriptomics.
- For idiopathic pulmonary fibrosis (`IPF`), the platform combined bulk and single-cell disease signatures, identified the repurposing candidate `pyrithyldione`, showed efficacy in human precision-cut lung slices comparable to `nintedanib`, and observed anti-fibrotic activity in a bleomycin-induced mouse model.
- GPS-driven screening of the Enamine HTS library for IPF produced `19` novel compounds for testing, of which `4` showed anti-fibrotic effects in patient-derived lung-slice assays.

## Main Novelty
- Extends transcriptomic reversal from drug repurposing into de novo virtual screening by predicting transcriptomic signatures directly from chemical structure.
- Couples screening with transcriptome-aware molecular optimization instead of treating hit discovery and medicinal chemistry as separate workflows.
- Introduces `SGAR` (structure-gene-activity relationship) analysis to connect predicted transcriptional perturbations with candidate mechanisms of action.
- Demonstrates the same framework across both oncology and fibrotic disease, including integration of single-cell transcriptomics for disease-signature construction.

## Datasets Used for Evaluation
- `LINCS Phase I perturbation data`
  - Content: drug-induced gene-expression profiles used to train the predictor.
  - Size: about `1.3 million` normalized profiles across roughly `11,000` small molecules.
- `HCC disease signatures`
  - Content: previously defined hepatocellular carcinoma transcriptomic signatures used for reversal scoring.
  - Validation systems: `HepG2`, `Huh7`, and `Hep3B` HCC cell lines, primary hepatocytes, and xenograft mouse models.
- `Virtual screening libraries`
  - Content: large chemical libraries scored with GPS.
  - Size: about `6,857,774` compounds for HCC screening from ZINC; more than `1 million` compounds from the Enamine HTS library for IPF screening.
- `IPF transcriptomic datasets`
  - Content: bulk RNA-seq plus single-cell RNA-seq signatures capturing mesenchymal, epithelial, and other disease-relevant cell states.
  - Single-cell example: a dataset containing `114,396` cells from `10` healthy donors and `12` patients with IPF.
- `Ex vivo and in vivo validation datasets`
  - IPF human tissue: precision-cut lung slices from explanted lungs of `14` patients.
  - IPF animal model: bleomycin-induced lung fibrosis mouse model.

## Experimental Procedure
- Train `GPS` on chemical fingerprints and LINCS-derived perturbation labels, using recursive learning to improve robustness to noisy transcriptional measurements.
- Aggregate predicted compound effects into transcriptomic signatures and compute disease-reversal scores against disease-specific upregulated and downregulated gene sets.
- For HCC:
  - rank large libraries by `Z-RGES`
  - test shortlisted compounds in `HepG2`, `Huh7`, and `Hep3B`
  - assess selectivity in primary hepatocytes
  - validate promising compounds in xenograft models
  - optimize a lead scaffold with Monte Carlo tree search under reversal-score and medicinal-chemistry constraints
- For mechanism analysis:
  - cluster active compounds by predicted transcriptomic signatures
  - associate gene-expression changes with potency using `SGAR`
  - validate candidate genes with RNA-seq, knockdown, survival analysis, and spatial transcriptomics
- For IPF:
  - build disease signatures from bulk and single-cell RNA-seq
  - prioritize repurposing and novel compounds by reversal of cell-type-specific signatures
  - test candidates in human precision-cut lung slices
  - advance selected compounds to bleomycin mouse-model validation

## Key Biology Insights
- Transcriptomic reversal captures therapeutically relevant biology that target-centric or structure-only screening can miss, especially for complex diseases without a single dominant target.
- In HCC, GPS-linked mechanism analysis converged on cell-cycle control and `UHRF1`-associated programs as a likely driver of the most active compounds.
- In IPF, myofibroblast and distal epithelial transcriptional programs emerged as especially informative disease components, supporting multi-cell-state therapeutic design rather than single-cell-type targeting alone.
- The IPF analyses suggest that reversing epithelial as well as mesenchymal pathology may matter for anti-fibrotic efficacy, consistent with the observed activity of pyrithyldione across relevant cell populations.

## Implications
- The study provides a practical route to use transcriptomics for novel-compound discovery at library scale, not just for ranking already-profiled drugs.
- Its workflow could reduce the dependence on expensive wet-lab profiling during early screening by using predicted perturbational signatures as the first-pass filter.
- The framework is particularly relevant for diseases with rich transcriptomic data but limited tractable target knowledge, and it offers a way to connect discovery, optimization, and mechanism interpretation within one computational stack.
