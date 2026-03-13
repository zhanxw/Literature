# Paper Summary

### Authors
- Elisa Sorrenti et al.

### Journal
- Cell Host & Microbe

### Publication Date
- March 11, 2026

### DOI
- https://doi.org/10.1016/j.chom.2026.02.006

## Keywords
- colorectal cancer (CRC)
- intratumoral microbiota
- Fusobacterium nucleatum
- Bacteroides fragilis
- tumor-associated neutrophils (TANs)
- Siglec-14
- neutrophil cytotoxicity
- host genotype

## Main Idea
- The paper argues that intratumoral microbiota composition and host `SIGLEC14` genotype jointly determine whether colorectal-cancer-associated neutrophils become tumoricidal. Specifically, `Fusobacterium nucleatum`, but not `Bacteroides fragilis`, drives neutrophil recruitment and triggers a Siglec-14-dependent cytotoxic program that correlates with better patient survival.

## Evidence Supporting the Main Idea
- Human CRC tissues showed elevated expression of neutrophil-recruiting chemokine genes `CXCL1`, `CXCL2`, `CXCL5`, and `CXCL8` versus adjacent tissue in cohort 1 (`n = 61`), and epithelial-cell enrichment of these chemokines was supported by a public scRNA-seq dataset with `108,131` tumoral and `60,164` non-tumoral epithelial cells.
- In cohort 2 (`n = 145`), chemokine-gene expression correlated with the neutrophil marker `CEACAM8`, and TCGA-based analyses linked this chemokine program to prolonged survival.
- In NSG xenografts using LS180 cells, intra-cecal tumors exposed to gut microbiota expressed higher neutrophil-recruiting chemokines than near-sterile intraperitoneal tumors; antibiotic treatment removed this difference, supporting a microbiota-dependent effect.
- In vitro coculture of CRC cells with live bacteria showed that both species could induce chemokines, but `F. nucleatum` drove stronger chemokine expression and secretion than control conditions and promoted stronger chemokine-dependent neutrophil migration than `B. fragilis`.
- In immunocompetent mouse CRC models, gut colonization with `F. nucleatum`, but not `B. fragilis`, increased TAN density; in human CRC tissues, `F. nucleatum` abundance correlated with neutrophil infiltration.
- Exposure of human peripheral blood neutrophils to `F. nucleatum` caused rapid activation-marker changes (`CD66b`, `CD54`, `CD16`, `CD62L`) and a distinct secretome containing elastase, defensin A3, lipocalin-2, myeloperoxidase, MMP8, MMP9, and cathelicidin, consistent with degranulation and cytotoxic function.
- Conditioned media from `F. nucleatum`-stimulated neutrophils killed LS180 tumor cells in vitro using neutrophils from healthy donors (`n = 9`) and CRC patients (`n = 10`), whereas media from `B. fragilis`-stimulated neutrophils did not.
- In NRG mice bearing subcutaneous Luc-LS180 xenografts, intratumoral injection of conditioned media from `F. nucleatum`-stimulated human neutrophils reduced tumor growth and increased cleaved-caspase-3-positive tumor-cell death; conditioned media from `B. fragilis`-stimulated neutrophils had no significant effect.
- Blocking experiments separated two mechanisms: TLR4 blockade prevented the phenotypic activation program, while Siglec-5/14 blockade abolished tumor-killing activity, indicating that cytotoxicity specifically depends on Siglec-14-family engagement.
- Soluble-receptor assays showed strong binding of Siglec-14, but minimal binding of Siglec-5, to `F. nucleatum`-derived LPS, supporting a direct molecular link.
- Donor genotype mattered functionally: neutrophils from `SIGLEC14` null donors still showed phenotypic modulation but lost tumor-killing capacity, and cytotoxicity scaled from WT to heterozygous to null genotypes.
- scRNA-seq of stimulated neutrophils showed that `F. nucleatum` induced MAPK/ERK, NF-kB, cytokine-signaling, and migration programs, and that these signatures were attenuated or altered in `SIGLEC14`-null cells.
- In primary CRC tissues, TANs expressed Siglec-14 and showed phenotypes and ultrastructural features resembling `F. nucleatum`-activated neutrophils, including evidence of bacterial internalization.
- Prognostic analyses across a CRC tissue microarray (`444` primary cases) and TCGA-related datasets showed that high TAN density predicted better overall survival, and this favorable prognostic effect was strongest when `F. nucleatum` abundance was also high; tumors lacking `SIGLEC14` expression had worse survival.

## Main Novelty
- The main novelty is the mechanistic link between a specific CRC-associated bacterial species and a host innate-immune polymorphism: `F. nucleatum` engages Siglec-14 to convert neutrophils into tumoricidal effectors, explaining why neutrophil infiltration and bacterial load can associate with favorable rather than uniformly adverse prognosis in CRC.

## Datasets Used for Evaluation
- Human CRC cohort 1:
  - Main content: matched tumor and adjacent non-tumoral tissues analyzed for chemokine-gene expression by qRT-PCR.
  - Sample size: `n = 61`.
- Human CRC cohort 2:
  - Main content: primary CRC samples used for chemokine expression, `F. nucleatum` load, and neutrophil-infiltration correlations.
  - Sample size: `n = 145`.
- Human CRC cohort 3:
  - Main content: patient blood and fresh tumor tissues used for neutrophil phenotyping and functional assays.
  - Sample sizes reported in the paper include `n = 10` CRC-patient neutrophil donors for stimulation assays and `n = 34` fresh clinical specimens for tissue analyses.
- Public epithelial scRNA-seq dataset from Pelka et al.:
  - GEO accession: `GSE178341`.
  - Main content: tumoral versus non-tumoral epithelial-cell chemokine expression.
  - Sample size in extracted text: `108,131` tumoral epithelial cells and `60,164` non-tumoral epithelial cells.
- Neutrophil scRNA-seq generated in this study:
  - GEO accession: `GSE311000`.
  - Main content: single-cell transcriptional response of untreated, `F. nucleatum`-stimulated, and `B. fragilis`-stimulated neutrophils from `SIGLEC14` WT and null donors.
  - Total cells after QC and merging: `157,248`.
- Proteomics dataset generated in this study:
  - PRIDE accession: `PXD069316`.
  - Main content: LC-MS/MS profiling of proteins released by stimulated neutrophils.
- Tissue microarray (TMA):
  - Main content: prognostic analysis of TAN density and `F. nucleatum` abundance in primary CRC.
  - Sample size: `444` primary CRC cases in the main figure analysis; the methods describe a source set of more than `500` cases for TMA construction.
- TCGA / related public survival resources:
  - Main content: `CEACAM8`, chemokine genes, `SIGLEC14`, and microbiome-associated survival analyses across COAD/READ cohorts.
  - Sample sizes explicitly stated in extracted text include `n = 597` for `CEACAM8` survival analysis, `n = 170` for TCMA-based `F. nucleatum` abundance, and `n = 382` for `SIGLEC14` expression analysis.
- Mouse models:
  - NSG intra-cecal and intraperitoneal LS180 xenografts for microbiota-exposure experiments (`i.c. n = 17`, `i.p. n = 66`, with antibiotic-treated subgroups).
  - NRG subcutaneous Luc-LS180 xenografts for testing neutrophil-conditioned media (`10-13` mice per group).
  - Immunocompetent MC38 and CT26 models for colonization and TAN-recruitment readouts.

## Experimental Procedure
- Quantify neutrophil-recruiting chemokines in human CRC tumors and adjacent tissues by qRT-PCR, and cross-check epithelial expression patterns using public scRNA-seq data.
- Compare microbiota-exposed versus near-sterile LS180 xenografts in NSG mice using intra-cecal and intraperitoneal implantation, with antibiotic perturbation as a control.
- Coculture human and murine CRC cell lines with live `F. nucleatum` or `B. fragilis` at a `50:1` bacteria:tumor-cell ratio and measure chemokine induction by qRT-PCR and ELISA.
- Test neutrophil migration toward tumor-cell supernatants in transwell assays, including chemokine-neutralization controls.
- Isolate human peripheral blood neutrophils from healthy donors and CRC patients, stimulate them with live bacteria at a `50:1` bacteria:neutrophil ratio, and profile phenotype by flow cytometry and live imaging.
- Analyze neutrophil secretomes by LC-MS/MS and test filtered conditioned media for tumor-killing activity on LS180 cells in vitro.
- Inject conditioned media from stimulated human neutrophils intratumorally into Luc-LS180 xenografts in NRG mice and monitor tumor burden by caliper, bioluminescence, and cleaved-caspase-3 staining.
- Dissect signaling using TLR2, TLR4, and Siglec-5/14 blocking reagents, receptor-localization imaging, TEM, and Fc-chimera binding assays with `F. nucleatum` LPS.
- Stratify donors by `SIGLEC14` genotype and compare neutrophil cytotoxicity plus downstream signaling (`p38`, `ERK`, `SYK`) after bacterial stimulation.
- Perform single-cell RNA-seq on neutrophils from WT and null donors under untreated, `F. nucleatum`, and `B. fragilis` conditions.
- Characterize fresh human CRC TANs by flow cytometry, RNAscope, IHC, confocal microscopy, and TEM, then relate TAN abundance, `F. nucleatum` load, and `SIGLEC14` expression to survival in TMA and TCGA-linked analyses.

## Key Biology Insights
- CRC-associated bacteria are not functionally interchangeable for neutrophil biology; `F. nucleatum` and `B. fragilis` can both influence chemokines, but only `F. nucleatum` consistently triggers a tumoricidal neutrophil program.
- Neutrophil recruitment and neutrophil cytotoxicity are separable processes: TLR4 is important for phenotypic activation, whereas Siglec-14 is required for effective tumor killing.
- Host innate-immune genotype materially changes the consequence of bacterial colonization. `SIGLEC14` loss weakens the anti-tumor neutrophil response even when bacterial exposure still alters neutrophil phenotype.
- High TAN density is not intrinsically pro-tumoral in CRC; its meaning depends on microbial context and receptor genotype.
- The work suggests that some reported population-level differences in CRC-neutrophil prognosis could be influenced by the variable prevalence of the `SIGLEC14` null polymorphism.

## Implications
- The study reframes `F. nucleatum` as context-dependent in CRC: although often considered pathogenic, it can support anti-tumor innate immunity when Siglec-14-competent neutrophils are present.
- Microbiota composition and innate-immune polymorphisms may need to be considered together when interpreting prognosis or designing neutrophil-directed CRC therapies.
- Siglec-14 and its downstream pathway represent candidate biomarkers for stratification and possible therapeutic exploitation.
- Translation remains limited by species differences between human and murine neutrophils and by incomplete definition of the precise `F. nucleatum` glycans that trigger Siglec-14.
