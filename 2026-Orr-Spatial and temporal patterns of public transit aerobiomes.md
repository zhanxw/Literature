# Spatial and temporal patterns of public transit aerobiomes

**Authors:** Russell J. S. Orr*, Ola Brynildsrud*, Kari O. Bøifot, Jostein Gohli, Gunnar Skogan, Frank J. Kelly, Mark T. Hernandez, Klas Udekwu, Patrick K. H. Lee, Christopher E. Mason, Marius Dybwad

**Journal:** Microbiome (BMC)  
**Year:** 2026 (Volume 14, Article 64)  
**DOI:** [10.1186/s40168-025-02303-7](https://doi.org/10.1186/s40168-025-02303-7)  
**Open Access:** Yes (CC BY 4.0)

---

## Summary

This study presents the first large-scale interannual analysis of public transit aerobiomes (airborne microbiomes) across six global cities over a 3-year period (2017-2019), utilizing shotgun metagenomic sequencing to characterize bacterial and fungal community structure at the species level.

---

## Main Idea

The study examines **spatial and temporal patterns in the species diversity of public transit aerobiomes**, with emphasis on both bacteria and fungi. Public transit systems are critically important for public health (subways alone carry ~190 million daily travelers globally), yet their airborne microbial communities remain poorly characterized. Previous studies were limited by:
- Small sample sizes
- Single-city focus (limited spatial comparison)
- Lack of interannual temporal studies
- Bacterial bias with poor fungal database coverage
- Insufficient contamination control in low-biomass samples

The objective was to determine whether public transit aerobiomes exhibit:
1. City-specific "signatures" or community structures
2. Temporal (interannual) stability
3. A global or local "core" microbiome
4. Correlations with environmental/human factors

---

## Main Novelty

1. **First 3-year interannual study** of public transit aerobiomes (2017-2019), demonstrating stability over time despite seasonal/daily variation reported in other studies

2. **Improved fungal classification** through enhanced databases including fungal genomes (3,049 accessions), achieving 25.3% fungal read classification vs. 0.2% in prior studies

3. **Stringent bioinformatics pipeline** for low-biomass contamination control:
   - 290 contaminant taxa identified (265 bacterial, 25 fungal)
   - Combined field and lab negative controls
   - Statistical testing (Z-test) to distinguish contaminants from true environmental signals
   - 62.7% of reads identified as contaminants and removed

4. **First local public transit aerobiome cores** defined for each city, relating species to ecological niches

5. **Rejection of a ubiquitous global species core** - No single species present in >97% of samples across all cities, though a sub-core of 44 bacterial and 1 fungal species was confirmed

6. **City-specific microbial signatures** with potential correlation between geographic distance and genetic similarity of aerobiomes

---

## Main Datasets

### Sampling
- **750 air samples** from public transit hubs in **6 global cities**:
  - Denver (38 samples)
  - Hong Kong (239 samples)
  - London (117 samples)
  - New York (125 samples)
  - Oslo (191 samples)
  - Stockholm (40 samples)

- **Temporal coverage**: Summer months (June-August) across 3 years:
  - 2017: 250 samples (reanalyzed from prior study)
  - 2018: 261 samples from 6 cities
  - 2019: 239 samples from 5 cities (excluding Stockholm)

### Controls
- **22 negative controls**: Field blanks + lab reagent blanks
- **5 positive controls**: ZymoBIOMICS Microbial Community Standard

### Metadata Collected
- Temperature (°C)
- Relative humidity (%)
- Number of travelers
- Enclosed vs. open areas
- Above-ground vs. underground

### Sequencing
- **Platform**: Illumina NovaSeq 6000
- **Read type**: 150 bp paired-end
- **Mean depth**: 
  - 2017: 9.4M reads/sample
  - 2018: 76.4M reads/sample
  - 2019: 71.2M reads/sample

### Data Availability
- NCBI BioProjects: PRJNA561080 (2017), PRJNA1129830 (2018), PRJNA1132165 (2019)

---

## Experimental Procedure

### 1. Air Sampling
- **Equipment**: SASS3100 high-volume electret filter air sampler (300 L/min for 30 min)
- **Setup**: Tripod-mounted, 45° downward angle, 1.5m above floor
- **Filters**: Sterilized electret filters stored at -80°C

### 2. DNA Isolation
- Protocol adapted from Bøifot et al. for electret filter aerobiome samples
- Steps: Lysis buffer extraction → centrifugation → enzymatic lysis (MetaPolyzyme) → bead beating → inhibitor removal → magnetic bead DNA purification
- DNA quantification: Qubit Fluorometer 3.0

### 3. Library Preparation & Sequencing
- Qiagen GeneRead DNA Library Prep Kit I
- Covaris sonication (500nt fragments)
- Bead cleanup, A-tailing, adapter ligation, PCR amplification
- Sequencing: NovaSeq 6000 (150bp PE)

### 4. Bioinformatics Pipeline
- **QC**: FastQC v0.11.9
- **Trimming**: TrimGalore v0.6.7 (min length 130bp, Phred 30)
- **Human read removal**: Bowtie2 vs. GRCh38
- **Diversity estimation**: Nonpareil 3 (estimated coverage: ~50% for 2018-2019, ~25% for 2017)

### 5. Classification Databases
- **Cross-kingdom**: Kraken2 protein database (entire NCBInr)
- **Species-level (FBAV)**: 
  - Archaea: 871 genomes
  - Bacteria: 63,568 genomes
  - Viruses: 14,018 genomes
  - Fungi: 3,049 reference/representative genomes
- **Classification**: Kraken2 (confidence 0.1, min-hit-groups 4) + Bracken
- **Threshold**: 0.005% read abundance cutoff for species-level assignment

### 6. Contamination Removal
- Aggregated Kraken2 reports from 22 negative controls
- Taxa flagged as contaminants if present in ≥2 negative samples with >10,000 reads
- Statistical Z-test to ensure air sample prevalence significantly exceeded negative controls

### 7. Statistical Analysis
- **Alpha diversity**: Shannon Diversity Index (vegan R package)
- **Beta diversity**: UMAP visualization
- **MANOVA**: Effect of city, year, environmental factors on community structure
- **Core microbiome**: Prevalence analysis at >97% (core) and 70-97% (sub-core) thresholds

---

## Key Findings

1. **City is the dominant factor** shaping aerobiome diversity and community structure (p < 1.0E-4), with clear city-specific signatures

2. **Interannual stability**: Species diversity was consistent across the 3-year sampling period within cities

3. **Population density correlation**: Bacterial diversity positively correlated with city population density; Hong Kong (highest density) had richest bacterial diversity

4. **Dominance patterns**: Bacteria comprised 74.4% of classified reads; fungi 25.3%; archaea and viruses <1% each

5. **No global core**: No single species present in >97% of all samples. Most prevalent: *Dietzia* sp. oral taxon 368 (95.2% prevalence)

6. **Sub-core confirmed**: 44 bacterial species + 1 fungal species (*Cladosporiaceae* sp.) in 70-97% of samples

7. **Local cores identified**: Each city had distinct core microbiomes (27-69 species at >97% prevalence):
   - Denver: Dominated by fungus *Ustilago bromivora* (grass pathogen, 100% prevalence)
   - Hong Kong: Dominated by *Roseomonas mucosa* (8.0% abundance, 100% prevalence)
   - London: Dominated by *Kocuria rhizophila* (5.8% abundance)
   - Oslo: Dominated by *Nocardioides aquaticus* + fungal species
   - Stockholm: Similar to Oslo with *N. aquaticus* dominance
   - New York: Multiple bacterial species at 100% prevalence + fungus *Epicoccum nigrum*

---

## Implications

The study demonstrates that public transit aerobiomes are diverse, city-specific ecosystems with stable interannual patterns during summer months. The findings highlight:

1. **Importance of robust contamination control** for low-biomass environmental metagenomics
2. **Potential for microbial forensics** - city-specific signatures could have applications in environmental monitoring and public health
3. **Need for improved fungal databases** - the 25% fungal contribution was