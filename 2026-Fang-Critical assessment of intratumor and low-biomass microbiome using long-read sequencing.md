# Critical assessment of intratumor and low-biomass microbiome using long-read sequencing

**Authors:** Yanchun Zhang, Edward A. Mead, Mi Ni, Magdalena Ksiezarek, Yujie Liu, Lei Cao, Hao Chen, Yu Fan, Wanjin Qiao, Yangmei Li, Laura Zuluaga, Gintaras Deikus, Robert Sebra, Rachel Brody, Raymund L. Yong, Ketan K. Badani, Xue-Song Zhang, Gang Fang

**Institution:** Icahn School of Medicine at Mount Sinai, Rutgers University, and collaborating institutions

**DOI:** https://doi.org/10.64898/2026.02.02.703393

**Date:** February 4, 2026 (bioRxiv preprint)

---

## Main Idea

This study addresses the long-standing controversy over detecting low-biomass microbial DNA in human tissues (placenta, brain, blood, and tumors). The central claim is that **genomic DNA fragment length serves as an informative discriminator** between genuine microbiome and contamination: while genuine microbiome genomes have long genomic DNA fragments, contaminant DNA is typically short and fragmented. The authors developed a metric called Median Length-Adjusted (Median(L)adj) that normalizes microbial read length to host read length, enabling differentiation between genuine microbiome signals and contamination in long-read sequencing data.

Key findings indicate that genuine microbial signals in human tissues are largely limited to biopsy sites with natural microbial exposure (gastrointestinal tract, cervix, vagina, and skin), while traditionally "sterile" tissues (kidney, brain, lung, blood, placenta) showed no evidence of resident microbiome.

---

## Main Novelty

1. **Median(L)adj Metric**: A novel normalization approach that calculates the ratio of median bacterial read length to median host read length within the same sample. This accounts for technical variability across samples while preserving biological signal of bacterial gDNA fragment size.

2. **Fragment-Length-Based Quality Control**: Demonstrates that long-read sequencing can distinguish intact microbial cells (long fragments) from degraded contamination (short fragments), addressing a key limitation of short-read sequencing which fragments all DNA to similar lengths.

3. **Systematic Evaluation of Low-Biomass Microbiome Claims**: Comprehensive analysis across multiple tissue types using both positive controls (germ-free mouse with bacterial spike-ins) and negative controls (cell lines, germ-free tissues) to validate the approach.

---

## Datasets Used for Evaluation

### Generated Datasets (This Study)
- **Germ-free mouse (GFM) tissues**: 7 tissue samples from multiple organs (brain, lung, stomach, colon)
- **Bacterial spike-ins**: 20 ATCC species (MSA-2002) spiked into GFM tissues at varying concentrations
- **Human cancer samples**:
  - 6 colorectal cancer (CRC) tumors + 8 matched normal tissues
  - 5 glioma tumors
  - 18 kidney cancer tumors
  - 4 gastric biopsy samples (H. pylori positive patients)
- **Human blood samples**: 8 samples sequenced with PacBio

### Public Datasets Analyzed
- **Human cell lines**: 7 cell lines with matched ONT and Illumina sequencing (accession PRJNA1086849)
- **Colorectal cancer ONT data**: 21 matched tumor-normal pairs from Xu et al., 2023 (CNCB HRA002638)
- **Lung cancer dataset**: 23 lung cancer-normal pairs from Sakamoto et al., 2022 (NBDC JGA)
- **Pan-cancer ONT dataset**: 161 tumor samples (123 metastatic, 38 local) from 25 cancer types across 36 biopsy sites from O'Neill et al., 2024 (EGA EGAS00001001159)
- **Placenta PacBio dataset**: From Yu et al., 2021 (EGA EGAS00001005515)
- **The Cancer Genome Atlas (TCGA)**: Referenced for prior controversy on intratumor microbiome

**Total**: 249 human primary tumor and normal tissue samples

---

## Experimental Procedure

### Sample Collection and Processing

#### Animal Samples
- Germ-free mice (C57BL/6J, 8-week-old males) maintained at Rutgers University Gnotobiotic Core
- Tissues collected: brain, lung, stomach, colon
- Aseptic dissection with UV sterilization between samples
- Samples flash-frozen in liquid nitrogen, stored at -80°C
- Bacterial spike-ins: 3.5×10⁵ (1x) or 3.5×10⁴ (0.1x) cells per tissue

#### Human Tissue Samples
- **CRC samples**: From Mount Sinai Biorepository; tumor core and adjacent normal (1-9 cm from tumor)
- **Glioma samples**: Glioblastoma Multiforme (GBM) from various brain regions
- **Kidney cancer**: Primarily Renal Cell Carcinomas (RCC)
- **Gastric biopsies**: From H. pylori positive patients in Germany
- **Blood samples**: 3-10 mL in EDTA tubes; plasma depleted, DNA isolated from blood cells

### DNA Extraction
- **Wizard Genomic DNA Purification Kit** (Promega) for most samples
- **DNeasy Blood and Tissue kit** (Qiagen) for gastric biopsies
- Optional RNase treatment included
- Final elution in 0.1x IDTE (1:9 dilution of TE in nuclease-free water)
- DNA quantity assessed by Qubit 4 fluorometer

### Library Preparation and Sequencing

#### Oxford Nanopore Technology (ONT)
- **Library prep**: Native Barcoding Kit 24 V14 (SQK-NBD114.24) or Rapid kit (SQK-RPB004)
- **DNA shearing**: gTUBE to ~10 kb (6000 RPM)
- **Modifications**: 
  - DNA repair/end prep: 30 min at 20°C
  - Barcoding/adapter ligation: 1 hour each
  - Bead elution: 45 min to improve yields
  - Ampure PB beads at 0.37x for size selection
- **Sequencing**: MinION or PromethION flow cells, 96-hour runs
- **Washes/reloads**: Daily using Flow Cell Wash Kit XL
- **Basecalling**: dorado v0.5.3 with 5mCG/5hmCG methylation calling

#### PacBio
- **Library prep**: SMRTbell prep kit 3.0
- **DNA shearing**: gTUBE to 20 kb (4200 RPM)
- **Modifications**:
  - End repair: 1 hour
  - Ligation: 3 hours to overnight
  - Bead elution: 45 min at 37°C
  - Ampure PB beads at 0.5x
  - No BluePippin size selection for blood samples
- **Sequencing**: Revio platform, 30-hour runs per SMRT Cell 25M
- **Consensus reads**: Generated using ccs command from subreads

#### Illumina (for comparison)
- Paired-end sequencing
- Bowtie2 alignment to hg38

### Bioinformatics Pipeline

1. **Host read removal**: 
   - Align to human reference (hg38 or CHM13v2.0 T2T) using minimap2 or bowtie2
   - Extract unmapped reads

2. **Microbial classification**:
   - KrakenUniq v1.0.4 with MicrobialDB database
   - Blastn megablast validation against nt database (v2024-08-31)
   - Filters: >50% target coverage, >100 bp length

3. **Median(L)adj calculation**:
   - For each genus with ≥5 reads per sample
   - Formula: Median(L)adj = Median(L)_bacteria / Median(L)_host
   - Excludes known reagent contaminants

4. **Long-read analysis (>5 kb)**:
   - Focus on reads >5 kb to enrich for high-integrity fragments
   - Compared exposure-associated sites vs. non-exposure sites

### Key Findings
- Germ-free mouse tissues and human cell lines: bacterial reads significantly shorter than host DNA
- Spike-in bacteria: long fragments comparable to host DNA (~5 kb median)
- CRC and gastric biopsies: high Median(L)adj values for Fusobacterium and H. pylori
- Glioma, kidney, lung cancer: no credible microbial signals
- Placenta and blood: only short, fragmented microbial reads (contamination)

---

## Data Availability

- **New sequencing data**: NCBI SRA PRJNA1401852
- **Code and analysis scripts**: Available from authors upon request

---

## Funding

National Institutes of Health grant R35 GM139655 (G.F.)

---

## Competing Interests

The authors declare no competing interests.
