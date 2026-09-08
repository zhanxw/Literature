# Paper Summary

### Authors

- Jessica J. King, Alireza Mowla, Jessica A. Kretzmann, Nishka Bhalla, Giselle Sugianto, Marck Norret, Ulrich D. Kadolsky, Munir Iqbal, Alka Saxena, Sebastian E. Amos, Yu Suk Choi, Brendan F. Kennedy, K. Swaminathan Iyer, Nicole M. Smith, and Cameron W. Evans

### Journal

- Nature Communications, volume 17, article 7735

### Publication Date

- June 19, 2026

### DOI

- https://doi.org/10.1038/s41467-026-74587-8

## Keywords

- single-cell RNA sequencing
- spatial transcriptomics
- scTECH-seq
- short barcode oligonucleotides
- 3D cell culture
- multilayer spheroids
- drug response
- irinotecan
- HeLa cells
- cell hashing
- mechano-microscopy
- tumour models

## Main Idea

- The study adapts single-cell transfection-enabled cell hashing (scTECH-seq) to build spatially encoded three-dimensional spheroids. HeLa cell populations are transfected with distinct short barcode oligonucleotides (SBOs), assembled layer by layer, imaged through barcode-linked fluorophores and later assigned back to their original spatial layer during droplet-based single-cell RNA sequencing.
- In a proof-of-concept irinotecan experiment, the method resolves both baseline radial gene-expression differences and layer-dependent drug responses. It therefore offers a direct way to retain coarse spatial provenance after dissociating engineered 3D cultures for scRNA-seq.
- This is a controlled HeLa spheroid study, not a validation in patient-derived tumours or complex organoids. The authors performed only one sequencing replicate per sample, so the results establish technical feasibility rather than broad biological or translational generalizability.

## Evidence Supporting the Main Idea

- **Efficient, persistent intracellular labelling (Figure 1a-c and Supplementary Figure 2):** Fluorescence microscopy and flow cytometry showed greater than 99.9% SBO labelling efficiency after a 4-hour transfection. The barcodes passed to daughter cells and had an apparent half-life of 28 ± 4 hours, approximately matching the HeLa population-doubling time.
- **Fluorophores did not measurably compromise sequencing (Figure 1d,e):** Cy5-modified and unmodified SBO groups had comparable RNA and SBO counts. The reported one-tailed tests gave p = 0.9995 for RNA counts and p = 1 for SBO counts (595 Cy5-labelled and 1,239 unmodified-SBO cells).
- **Layer identity survived assembly and dissociation (Figure 1f-k):** Confocal images resolved the Cy3- and Cy5-labelled layers, flow cytometry found no detectable barcode loss or exchange between cells, and scRNA-seq demultiplexed the layers. The sequenced two-layer example contained 4,783 Cy5-SBO and 1,717 Cy3-SBO cells with similar RNA and SBO count distributions.
- **Three-layer spatial recovery (Figure 2):** Three independently barcoded populations were added over three days to form an interior, middle and peripheral layer. D-score assigned 82.5% of cells unambiguously to one of the three SBOs. A 7.0% cell-death-associated cluster was removed from downstream interpretation because it could reflect dissociation damage.
- **Baseline spatial biology (Figure 2d-g):** The authors detected 117 differentially expressed genes across untreated layers using |log2 fold change| > 0.25 and adjusted p < 0.05. Interior cells showed enrichment of KEAP1–NFE2L2 oxidative-stress pathways, whereas peripheral cells were enriched for glycolysis, glucose metabolism and extracellular-matrix programs. Eight of the 11 top layer-associated genes were also differential in an independent two-layer analysis.
- **Drug penetrance and cell-cycle response (Figure 3):** Three-layer spheroids were exposed to 5-100 μM irinotecan for 24 hours, after which 50 μM was selected for transcriptomic studies. Fluorescent SN-38 was observed throughout the spheroid. Fucci imaging and flow cytometry showed accumulation in S phase or at the G2 checkpoint, with a stronger arrest in SN-38-high than SN-38-low cells.
- **Single-cell drug-response map (Figure 4):** A total of 11,921 cells were sequenced and assigned an SBO; 9,422 passed analysis filters, including 3,748 vehicle-control and 5,674 irinotecan-treated cells. Drug-treated and control cells separated transcriptionally, irinotecan increased G2/M markers and the eight retained expression clusters contained 3,970 DEGs.
- **Spatially dependent response genes (Figure 5a):** Filtering out genes that already varied by layer in controls identified 197 spatially uniform irinotecan-responsive genes and 39 genes with a layer-dependent response. The latter group included PARP14, IFITM2 and BCAP31, although their relevance as response or resistance markers was not functionally tested here.
- **Concordance with perturbational references (Figure 5b):** Layer-specific profiles were compared with 24-hour HeLa perturbations in LINCS L1000. Correlation with topoisomerase-inhibitor signatures was strongest at the spheroid periphery and weakened toward the core; unrelated drug classes showed little similarity. This supports, but does not by itself prove, a radial gradient in effective drug activity.
- **Mechanical structure was not an evident confounder (Figure 5c,d):** Mechano-microscopy found relatively uniform Young's modulus across the three constructed layers (38,566 interior, 97,531 middle and 189,204 peripheral image pixels; two spheroids). The authors therefore attribute layer-dependent response more plausibly to drug penetration or cellular metabolism than to a discontinuity in layer stiffness.

## Main Novelty

- Physically encodes spatial origin before spheroid construction, allowing spatial labels to remain associated with individual transcriptomes after the 3D culture is dissociated.
- Combines intracellular SBO hashing with fluorophore conjugation, so the same labels support imaging, flow cytometry, 5-prime scRNA-seq multiplexing and correlative mechanical measurements.
- Uses a modular layer-by-layer assembly rather than inferring location solely from gene expression or dye penetration, making the approach applicable to engineered architectures that lack a spatial reference atlas.
- Demonstrates that coarse spatial drug-response gradients can be measured in a small 3D culture without serially sectioning and separately profiling every slice.

## Datasets Used for Evaluation

- **Two-layer HeLa spheroids:** Cy3- and Cy5-SBO-labelled cell populations used to validate imaging, barcode retention and sequencing compatibility. Figure 1 reports 4,783 Cy5-labelled and 1,717 Cy3-labelled sequenced cells; the representative cross-section came from two independently prepared spheroids.
- **Untreated three-layer HeLa spheroids:** Interior, middle and peripheral populations built with 2,000, 3,000 and 5,000 cells per well on successive days. These cultures supported D-score layer assignment, baseline DEG analysis and pathway comparisons; 82.5% of recovered cells were assigned unambiguously to a layer.
- **Irinotecan dose and cell-cycle experiments:** Three-layer spheroids treated for 24 hours with 5, 20, 50 or 100 μM irinotecan, alongside 0.1% DMSO and untreated controls. Viability and Fucci assays used eight spheroids per condition; selected microscopy panels were representative of two or four spheroids as reported in the figure captions.
- **Vehicle-versus-irinotecan scRNA-seq dataset:** 11,921 SBO-assigned cells generated with 10x Genomics 5-prime chemistry; 9,422 cells passed downstream filters, comprising 3,748 vehicle and 5,674 irinotecan-treated cells. The dataset is deposited as GEO GSE245416, with raw and processed materials also archived at Zenodo (10.5281/zenodo.20373611).
- **LINCS L1000 perturbational profiles:** Public 24-hour HeLa drug-expression signatures used to compare each spheroid layer with irinotecan, camptothecin, related topoisomerase II inhibitors and mechanistically distinct control drugs.
- **Mechano-microscopy data:** Young's-modulus maps from fluorescently delineated three-layer spheroids, reported for two spheroids, used to test whether physical discontinuities at engineered layer boundaries explained transcriptional differences.

## Experimental Procedure

1. Design 69-nt 10x-compatible SBOs, add Cy3 or Cy5 fluorophores to selected sequences and complex the oligonucleotides with a dendritic polymer at an amine-to-phosphate ratio of 30.
2. Transfect HeLa populations for 4 hours with 23 pmol SBO per 150,000 cells, then quantify labelling by fluorescence microscopy and flow cytometry and measure barcode inheritance and longevity through imaging and qPCR.
3. Seed one labelled population into low-adhesion wells, then transfer each spheroid into newly seeded, differently barcoded cells on successive days. Use 2,000, 3,000 and 5,000 cells for the three successive layers.
4. Validate spatial organisation by imaging cryosections, and test whether SBO identity persists after spheroid dissociation using flow cytometry and two-layer scRNA-seq.
5. Characterize untreated three-layer spheroids by 10x Genomics Chromium 5-prime gene-expression and feature-barcode sequencing. Assign cells to SBOs with D-score, process expression matrices with Cell Ranger and Seurat, and test layer-associated genes with Wilcoxon rank-sum tests and multiple-testing correction.
6. Treat three-layer spheroids for 24 hours across an irinotecan dose range, measure viability with propidium iodide, image the fluorescent metabolite SN-38 and quantify cell-cycle arrest with a stable HeLa Fucci reporter line.
7. Compare vehicle-treated spheroids with spheroids receiving 50 μM irinotecan for 24 hours. Sequence to as many as 50,000 reads per cell, retain cells passing transcript and mitochondrial-read filters, then identify expression clusters, cell-cycle states and drug-responsive DEGs.
8. Remove baseline layer-variable genes to distinguish general drug-response genes from the 39 genes whose irinotecan response depends on layer. Correlate layer-level profiles with LINCS L1000 HeLa drug signatures using Kendall's tau.
9. Embed fluorescently barcoded spheroids in hydrogels and use combined optical-coherence and confocal mechano-microscopy to map Young's modulus to each layer and assess whether mechanical boundaries explain spatial response patterns.

## Key Biology Insights

- Even a single-cell-type spheroid develops radial transcriptional heterogeneity: its core exhibits greater oxidative-stress signalling, while its periphery favors metabolic and extracellular-matrix programs.
- Irinotecan produces broad cell-cycle and transcriptional effects throughout HeLa spheroids, but the expression response is strongest at the periphery and becomes less similar to 2D perturbation signatures toward the interior.
- The 39 layer-dependent drug-response genes are candidate spatial biomarkers rather than validated mediators of sensitivity or resistance. Their roles require perturbation experiments and confirmation in disease-relevant models.
- Uniform measured elasticity across engineered layers argues against stiffness discontinuities as the principal explanation for the observed radial response, but it does not distinguish drug diffusion from oxygen, nutrient, proliferation or metabolic gradients.
- Internalized SBO abundance decreases as cells divide, placing a practical time limit on transient spatial barcoding in rapidly proliferating cultures.

## Implications

- scTECH-seq could provide a relatively scalable bridge between conventional pooled scRNA-seq and section-based spatial transcriptomics for engineered spheroids, drug screens, time courses and perturbation panels.
- The method is especially useful when researchers control the initial architecture: different cell types, perturbations or spatial compartments can be separately barcoded before assembly and later analyzed together.
- Spatial resolution is determined by the preassembled populations, not continuously measured coordinates. Cell migration, barcode dilution, barcode degradation or death during culture and dissociation can weaken the relationship between an SBO and a cell's final position.
- Evidence is limited to HeLa spheroids and a single drug. Patient-derived cells, co-cultures, organoids, additional drug classes and direct measurements of irinotecan–TOP1 cleavage complexes are needed to establish biological and translational validity.
- Only one sequencing replicate was generated for each sample because of cost; sample sizes were not predetermined statistically, and most experiments and outcome assessments were not blinded. DEG counts and spatial gradients should therefore be reproduced independently.
- The study's main contribution is a technically integrated proof of concept. It does not demonstrate that scTECH-seq outperforms current high-resolution spatial transcriptomic methods in accuracy, throughput or cost under matched conditions.
