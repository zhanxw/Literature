# Paper Summary

**Title:** The immunometabolic topography of cellular organization and bacterial control in tuberculosis granulomas

**Source:** [Nature Immunology](https://www.nature.com/articles/s41590-026-02431-8)

### Authors

Erin F. McCaffrey; Alea C. Delmastro; Isobel Fitzhugh; Jolene S. Ranek; Sarah Douglas; Joshua M. Peters; Christine Camacho Fullaway; Marc Bosse; Candace C. Liu; Craig Gillen; Noah F. Greenwald; Sarah Anzick; Craig Martens; Seth Winfree; Yunhao Bai; Cameron Sowers; Mako Goldston; Alex Kong; Potchara Boonrat; Carolyn L. Bigbee; Roopa Venugopalan; Pauline Maiello; Edwin Klein; Mark A. Rodgers; Charles A. Scanga; Philana Ling Lin; Sean C. Bendall; Denise E. Kirschner; Sarah M. Fortune; Bryan D. Bryson; J. Russell Butler; Joshua T. Mattila; JoAnne L. Flynn; Michael Angelo.

### Journal

Nature Immunology, volume 27, pages 867–880 (2026).

### Publication Date

23 February 2026 (online); April 2026 issue.

### DOI

[10.1038/s41590-026-02431-8](https://doi.org/10.1038/s41590-026-02431-8)

## Keywords

- Tuberculosis (TB)
- *Mycobacterium tuberculosis* (Mtb)
- Granuloma
- Hypoxia
- Immunometabolism
- Macrophage
- T-cell exclusion
- MIBI-TOF
- Spatial transcriptomics
- Single-cell RNA sequencing
- Nonhuman primate
- Spatial cellular niche

## Main Idea

Tuberculosis granulomas contain a reproducible radial immunometabolic architecture. The macrophage-rich myeloid core separates into an outer, IDO1-rich normoxic zone and an inner, GLUT1-high hypoxic zone surrounding necrosis. Across individually quantified granulomas, greater representation of the hypoxic program is associated with macrophage states linked to dysfunctional immunity, near-exclusion of T cells from the inner myeloid core, and higher Mtb burden. The authors therefore propose that hypoxia helps create a spatially organized, infection-tolerant niche.

This conclusion is principally associative: the study links hypoxia, tissue organization and bacterial burden but does not experimentally perturb hypoxia to establish causality.

## Evidence Supporting the Main Idea

- **Direct tissue observation (Fig. 1):** In situ pimonidazole labeling co-localized with GLUT1 in a sharply demarcated peri-necrotic ring. IDO1 marked the adjacent outer part of the myeloid core, establishing two metabolic subzones. The normoxic/IDO1-rich zone occurred across granulomas, whereas the hypoxic zone was found in necrotic lesions (44 of 52) and occupied more of the myeloid core as necrosis increased.
- **Cellular atlas and bacterial burden (Fig. 2):** MIBI-TOF profiling generated 1,979 images and enumerated 1,202,041 cells from 52 granulomas. CD11c+ macrophage frequency correlated with higher bacterial burden (Spearman rho = 0.45, FDR-adjusted P = 0.02), as did CD4+ T-cell frequency (rho = 0.42, adjusted P = 0.02). CD11c+ and CD68+ macrophages associated with high burden were enriched in the hypoxic zone, whereas CD14+ macrophage/monocytes favored the normoxic zone. T cell–macrophage proximity, especially for CD8+ T cells, fell markedly in the hypoxic zone.
- **Transcriptional state (Fig. 3):** Reanalysis of published NHP granuloma scRNA-seq data separated macrophage populations corresponding to hypoxic and normoxic zones. Hypoxic-zone macrophages showed glycolysis, hypoxic signaling and angiogenesis programs and higher *PKM*, *VEGFA*, *IL1RN* and *IL6*. One-granuloma 10x Visium profiling spatially confirmed the concentric expression patterns.
- **Radial organization (Fig. 4):** A GIS-inspired buffer analysis aligned features across lesions from the granuloma center outward. The inner hypoxic module contained neutrophils, MMP9, CHIT1, GLUT1 and high-burden-associated macrophages, together with reduced HLA-DR. T cells and activation/inflammatory signals such as pS6, iNOS, IFN-gamma and DC-LAMP were displaced toward outer regions.
- **Cellular neighborhoods (Fig. 5):** QUICHE identified 98 cellular niches differing between high- and low-burden granulomas using a median cutoff of log10 CFU = 3.26. High-burden networks were dominated by hypoxia-associated CD11c+ and CD68+ macrophage niches. Low-burden networks showed more CD8+ T-cell, endothelial-cell, fibroblast and normoxic-zone myeloid interactions. High-burden lesions also concentrated neutrophils centrally, whereas low-burden lesions placed them more peripherally.
- **Human relevance (Fig. 6):** Archival pulmonary TB tissue showed the same broad arrangement of an IDO1-rich outer myeloid zone, a GLUT1-rich inner zone, restricted lymphocyte penetration and distinct macrophage localization. This supports conservation of the architecture in human disease, although the human analysis was confirmatory and not linked to lesion-level CFU.

## Main Novelty

- Connects the metabolic state of a granuloma to its radial cellular organization and lesion-specific bacterial burden at single-cell spatial resolution.
- Refines the canonical granuloma anatomy by dividing the myeloid core into normoxic and hypoxic metabolic subzones.
- Introduces “immunotopography,” a GIS-inspired radial buffer framework for integrating protein expression, cell density and metabolic zones across irregular tissue lesions.
- Shows that bacterial control is associated with the configuration of multicellular neighborhoods, not merely the abundance of individual immune-cell types.
- Provides a mechanistic hypothesis for the long-recognized failure of T cells to reach infected macrophages: the hypoxic inner core may act as a topographical and metabolic immune-exclusion trap.

## Datasets Used for Evaluation

- **Primary NHP MIBI-TOF cohort:** 52 archival lung granuloma specimens from 16 cynomolgus macaques infected bronchoscopically with low-dose Mtb Erdman and collected 9–12 weeks later. One to eight granulomas were sampled per animal. Each lesion had individual CFU, PET/CT, size, inflammatory and detection-time metadata. Bacterial burdens ranged from 0 to 104,400 CFU. The imaging dataset comprised 1,979 38-plex images and 1,202,041 segmented cells assigned to 19 cell subsets.
- **In situ hypoxia-validation tissue:** Archival granuloma tissue from one Mtb-infected macaque given pimonidazole before necropsy, used to validate GLUT1 as a spatial correlate of hypoxia and distinguish the normoxic and hypoxic zones.
- **Published NHP granuloma scRNA-seq dataset:** Previously published single-cell RNA-seq data from macaque granulomas at approximately 10 weeks after infection, reanalyzed to compare recruited macrophage clusters corresponding to the two metabolic zones. The number of animals, granulomas and cells in this reused dataset is not specified in this paper.
- **10x Visium spatial transcriptomics:** One serial section from one NHP granuloma (NHP6, granuloma 3), used to validate spatial expression of zone-associated genes. This is a focused validation sample, not an independent cohort.
- **Human pulmonary TB tissue:** Archival pulmonary TB tissue assembled as a tissue microarray and analyzed with MIBI-TOF; Fig. 6 presents a representative human granuloma. The number of patients and tissue cores is not specified in the paper, and no human lesion-level bacterial burden was available.
- **Public outputs:** Multiplexed imaging and histology are deposited in BioImage Archive ([S-BIAD2359](https://doi.org/10.6019/S-BIAD2359)); single-cell data, computational masks and spatial transcriptomics are deposited in Mendeley Data ([6cddmnmwh9.1](https://doi.org/10.17632/6cddmnmwh9.1)); analysis code is available in the [Angelo Lab publications repository](https://github.com/angelolab/publications/tree/main/2024-McCaffrey-Delmastro_etal_NHP-TB).

## Experimental Procedure

- **Establish the lesion cohort:** Select archival FFPE lung granulomas from 16 cynomolgus macaques infected with 2–13.5 CFU Mtb Erdman and necropsied 9–12 weeks post-infection; link each lesion to CFU and PET/CT metadata.
- **Validate the hypoxia marker:** Co-stain pimonidazole-exposed tissue for pimonidazole, GLUT1 and IDO1. Demonstrate a GLUT1+/pimonidazole+ peri-necrotic zone adjacent to an IDO1-rich outer myeloid zone.
- **Generate multiplexed spatial images:** Develop and validate macaque-reactive metal-tagged antibodies, stain tissue with a 38-plex panel, and acquire subcellular-resolution MIBI-TOF images in randomized 400 × 400 micrometer fields of view.
- **Process and segment images:** Denoise and normalize images; annotate necrotic and cellular regions; segment cells with Mesmer; manually add multinucleated giant cells; cluster pixels and cells with Pixie; assign cells to 19 phenotypic subsets.
- **Annotate metabolic zones:** Construct IDO1-based normoxic-zone masks and GLUT1-based hypoxic-zone masks after excluding IDO1/GLUT1 overlap; map each segmented cell to a zone.
- **Relate composition to bacterial control:** Correlate cell frequencies with lesion CFU using Spearman tests and 5% FDR correction; compare high versus low burden at the median log10 CFU cutoff of 3.26; compute cell-type enrichment in each metabolic zone.
- **Quantify T-cell access:** Measure CD4+ and CD8+ T-cell proximity to macrophages within 10 micrometers and compare interaction scores across the normoxic and hypoxic zones.
- **Resolve macrophage programs:** Reanalyze published scRNA-seq macrophage clusters using *IDO1*, *SLC2A1* and *SLC2A3*; score glycolysis; test differential expression and pathway enrichment; validate selected spatial expression patterns with 10x Visium.
- **Build radial immunotopography:** Generate concentric GIS buffer rings from each necrotic core or granuloma centroid, quantify protein intensity and cell density per ring, normalize lesion geometry into 20 radial bins, and compare consensus spatial patterns.
- **Identify discriminating cellular niches:** Use QUICHE to find spatial neighborhoods differentially enriched in high- versus low-CFU lesions, then construct condition-specific cellular interaction networks.
- **Assess translation to humans:** Apply the same MIBI-TOF panel to archival human pulmonary TB tissue and verify that the principal metabolic and cellular architecture is present.

## Key Biology Insights

- Granulomas are not metabolically uniform: their macrophage core is spatially partitioned into adjacent but functionally distinct environments.
- The inner hypoxic zone is characterized by glycolytic and angiogenic stress responses, immunoregulatory factors such as IL1RN, and reduced HLA-DR, consistent with impaired antigen presentation and immune activation.
- Hypoxia-associated macrophages and peri-necrotic neutrophils co-occupy lesions with higher bacterial burden, whereas low-burden lesions show richer interactions among CD8+ T cells, endothelial cells and normoxic-zone myeloid cells.
- T cells can enter the outer myeloid region but are nearly absent from the hypoxic inner zone where infected macrophages are likely to reside. Spatial access, not only T-cell abundance, may therefore limit bacterial control.
- IDO1 is widespread even in granulomas that control infection, so its role may be context-dependent: it can suppress adaptive immunity but may also restrain damaging inflammation. Hypoxia showed the stronger association with the permissive architecture.
- The proposed progression—early macrophage activation and glycolysis, oxygen depletion, necrosis, hypoxic reinforcement and immune exclusion—is a biologically plausible model, but the temporal sequence was not directly tested.

## Implications

- Host-directed TB therapy may need to alter lesion physiology and architecture, not just stimulate systemic immunity. Candidate approaches include improving vascular integrity, increasing local oxygenation or reducing fibrotic diffusion barriers.
- Restoring oxygenation could potentially improve antigen presentation, T-cell penetration and local antimicrobial activity, and might also improve antibiotic performance in poorly perfused lesions.
- Spatial biomarkers such as GLUT1-high peri-necrotic zones, macrophage neighborhood composition or T-cell exclusion may help distinguish permissive from controlling granulomas when lesion-level sampling is feasible.
- The work provides a reusable analytical framework for studying other radially organized inflammatory lesions.
- Intervention studies are required before treating hypoxia as causal. Important next steps include longitudinal sampling, direct oxygen/metabolite measurements and experimental perturbation of hypoxia in granuloma organoids or animal models.
