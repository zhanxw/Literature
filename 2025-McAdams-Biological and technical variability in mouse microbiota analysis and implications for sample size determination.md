# Biological and technical variability in mouse microbiota analysis and implications for sample size determination

**Authors:** Zachary McAdams, Kevin Gustafson, Aaron Ericsson  
**Publication:** Lab Animal, Volume 55, January 2026  
**DOI:** [10.1038/s41684-025-01664-8](https://doi.org/10.1038/s41684-025-01664-8)

---

## Main Idea

This study investigates the sources of biological and technical variability in mouse gut microbiota (GM) analysis using 16S rRNA sequencing. The authors employ a hierarchical sampling strategy to quantify the effect sizes of different variance sources and provide practical guidance for microbiome study design, particularly regarding sample size determination and the cost-benefit analysis of repeated sampling from individual mice.

## Novelty

1. **Hierarchical Variance Quantification**: The study uniquely dissects variance at four nested levels: technical replicates (library preparation), individual fecal pellets, individual mice, and cages
2. **Effect Size Comparison**: First systematic comparison of biological/technical variance versus experimental variable effect sizes in mouse microbiome studies
3. **Practical Sampling Guidance**: Provides evidence-based recommendations on the utility (or lack thereof) of repeated sampling strategies for reducing animal numbers in microbiome research
4. **Open Data/Analysis**: All code and data publicly available for reproducibility

## Datasets Used

### Primary Dataset
- **Source**: Two C57BL/6J mouse colonies maintained at University of Missouri Mutant Mouse Resource and Research Center (MMRRC)
  - **GMLow**: Jackson Laboratory-origin gut microbiota (low richness)
  - **GMHigh**: Inotiv-origin gut microbiota (high richness)
  - Both colonies: 7th generation descendants from founder mice

### Sample Structure
| Level | Count |
|-------|-------|
| Mice | 32 (8 mice/sex/origin, 2 mice/cage, 4 cages/sex/origin) |
| Fecal pellets | 96 (3 pellets/mouse) |
| 16S rRNA libraries | 288 (3 technical replicates/pellet) |

### Experimental Factors
- **Sex**: Male and Female (2 levels)
- **GM Origin**: Jackson Lab vs Inotiv (2 levels)
- **Biological nesting**: Cage → Mouse → Pellet
- **Technical replicates**: Triplicate 16S library preparations

## Experimental Procedure

### Sample Collection
1. Fecal collection: 3 pellets/mouse collected within 15 minutes (06:30-07:00)
2. Storage: −80°C until processing
3. DNA extraction: Modified QIAamp PowerFecal Pro kit (Qiagen)
4. Normalization: DNA yields normalized to 3.51 ng/μL

### Sequencing Protocol
- **Target**: V4 region of 16S rRNA gene
- **Primers**: U515F/806R with Illumina adapters
- **Platform**: Illumina MiSeq (2×250 bp paired-end)
- **PCR**: 25 cycles, Phusion high-fidelity polymerase
- **Library prep**: Technical triplicates per DNA extraction

### Bioinformatics Pipeline (QIIME2 v2021.8)
1. Adapter/primer trimming: Cutadapt
2. Denoising: DADA2 (150 bp truncation, 12 bp minimum overlap)
3. Length filtering: 249-257 bp
4. Taxonomy: SILVA v138 99% database, sklearn classifier
5. Rarefaction: 39,293 features/sample

### Statistical Analysis
- **Variance decomposition**: Nested ANOVA/PERMANOVA (GM/cage/mouse/replicate)
- **Effect size**: Eta squared (η²)
- **Distance metrics**: Bray-Curtis (weighted), Jaccard (unweighted)
- **Precision**: Coefficient of variation (CV)
- **Power analysis**: Simulation with Cohen's d for sample size estimation

## Key Findings

### 1. Variance Hierarchy
- **Experimental variable (GM)**: η² = 0.62 ± 0.20 (dominant effect)
- **Cage effects**: η² = 0.21 ± 0.12 (3× lower than GM)
- **Individual mouse**: η² = 0.13 ± 0.086 (5× lower than GM)
- **Technical replicates**: η² = 0.027 ± 0.014 (23× lower than GM)

### 2. Precision Patterns
- Low-richness community (GMLow) shows higher variability in presence-based metrics
- Technical replicates: highest precision
- Intramouse dissimilarity: ~50% greater than technical replicates
- Intracage dissimilarity: ~4× greater than technical replicates
- Presence-based metrics (richness, Jaccard) more susceptible to variation

### 3. Sample Size Recommendations
**Repeated sampling impractical**: Simulation showed collecting 5 fecal samples/mouse:
- Increases effect size by only 2-3%
- Reduces minimum animals by only 5% (e.g., 74 → 70 mice/group)
- Increases sequencing costs ~5× (e.g., $3,700 → $17,500 per group)

**Recommended strategy**: Single fecal sample per mouse, single library preparation

## Practical Implications

1. **For study design**: One sample per mouse is sufficient for most microbiome studies
2. **For low-richness communities**: Consider repeated measurements for presence-based metrics
3. **For 3Rs (Reduction)**: Repeated sampling offers minimal benefit at current sequencing costs
4. **For power analysis**: Use paper's variance estimates for sample size calculations (Supplementary Fig. 5)

## Data Availability

- **Sequencing data**: NCBI SRA - BioProject PRJNA1083462
- **Analysis code**: https://github.com/ericsson-lab/intrafecal_variation

## Ethics

- **IACUC Protocol**: #36781 (University of Missouri)
- **Funding**: NIH U42 OD010918
