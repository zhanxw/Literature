# The MicrobeAtlas database: Global trends and insights into Earth's microbial ecosystems

## Paper Information

- **Title:** The MicrobeAtlas database: Global trends and insights into Earth's microbial ecosystems
- **Authors:** João Frederico Matias Rodrigues, Janko Tackmann, Lukas Malfertheiner, David Patsch, Eugenio Perez-Molphe-Montoya, Nicolas Näpflin, Daniela Gaio, Gregor Rot, Mihai Danaila, Matteo Eustachio Peluso, Marija Dmitrijeva, Thomas Sebastian Benedikt Schmidt, and Christian von Mering
- **Journal:** Cell
- **Year:** 2026
- **DOI:** https://doi.org/10.1016/j.cell.2026.01.021

---

## Summary

**MicrobeAtlas (www.microbeatlas.org)** is an integrated, reference-based resource for truly planet-wide microbiomics, analyzing **2.4 million** uniformly analyzed microbial communities across diverse environments, conditions, and technologies. This study presents the largest collection of cross-study compatible microbial community profiles to date, enabling global-scale ecological insights into Earth's microbial ecosystems.

---

## Keywords and Main Ideas

### 1. Global Microbial Community Database
- MicrobeAtlas unifies **2,390,937 microbial community samples** from 52,950 studies in a single resource
- Data sourced from NCBI Sequence Read Archive (SRA) with comprehensive metadata extraction
- Covers microbial communities from 16S, 18S, and metagenomic experiments across diverse technologies
- Hierarchical OTU clustering at 90%-99% sequence identity thresholds (651,275 OTUs total)

### 2. Unified Reference-Based Analysis
- Custom database of **1,536,850 full-length 16S/18S marker gene sequences**
- Reference-based approach enables tracking OTUs across different sequencing strategies (amplicon vs. WGS)
- Quality-filtered dataset of **1,153,349 comparable community profiles** used for analysis
- Hierarchical community clustering into 356,182 microbial community clusters

### 3. Global Biogeographic Patterns
- Communities structured by environment (animal, aquatic, soil, plant) with distinct niche partitioning
- **Marine diversity peaks at equator** consistent with latitudinal diversity gradients
- Soil and aquatic microbiomes are global richness hotspots with many uncharacterized members
- **88.7% of OTUs lack cultured isolates, genomes, or detailed taxonomy** - representing "microbial dark matter"

### 4. Habitat Generalism and Specialism
- Developed entropy-based habitat generalism scores for hundreds of thousands of OTUs
- **Soil and plant-associated microbes show higher generalism** than animal or aquatic specialists
- Generalists have significantly larger genomes (36.4% more genes) than specialists
- Anaerobes show higher specialism; aerobes tend to thrive across diverse environments

### 5. Taxonomic and Environmental Insights
- Classification depth negatively correlates with richness: well-classified phyla are OTU-rich and abundant
- Environmental samples have lower taxonomic coverage (down to 35% classified at genus level vs. 78% in humans)
- **Enterobacteriaceae (including pathogens) show high generalism scores**, suggesting broad environmental reservoirs

---

## Main Novelty

1. **Largest Cross-Study Compatible Microbiome Resource**: 2.4 million samples with unified processing pipeline, surpassing the Earth Microbiome Project (~27,000 samples) by two orders of magnitude

2. **Reference-Based Cross-Technology Integration**: Mapping to common full-length reference enables tracking OTUs across sequencing strategies (metagenomic and amplicon) and protocols

3. **Hierarchical Multi-Resolution Analysis**: OTUs clustered at 90%-99% identity + hierarchical community clustering enables analysis at flexible taxonomic and ecological scales

4. **Global Generalism Score Framework**: Novel entropy-based metric quantifying habitat generalism across four major environments (animal, aquatic, soil, plant)

5. **Rich Metadata Integration**: Geographic coordinates, IUCN ecosystem annotations, keyword extraction, and links to genome/phenotype resources (proGenomes3, BacDive)

---

## Datasets Used for Evaluation

### Primary Dataset
- **NCBI Sequence Read Archive (SRA)**: 2,390,937 samples from 52,950 studies
- Selection criteria: metadata keywords "metagen*", "microbi*", "bacteria", or "archaea"
- Final analyzed dataset: 1,153,349 quality-filtered samples (24,349 studies)

### Reference Databases
- **MAPref 2.2b**: 1,425,265 16S sequences + 111,585 18S sequences
- **proGenomes3**: 753,909 representative 16S rRNA sequences from 907,388 genomes
- **BacDive**: 28,227 culture strain 16S sequences

### Geographic and Ecological Resources
- **IUCN Global Ecosystem Typology**: 65 sub-environments, 7 terrestrial biomes, 34 Ecosystem Functional Groups (EFGs)
- **RESOLVE Ecoregions**: 22 distinct biogeographic ecoregions for savanna analysis
- **Remote sensing data**: SoilGrids, Copernicus, Global Fire Emissions Database

### Environmental Coverage
- **Animal**: 63.5% (human 23.0%)
- **Aquatic**: 19.3% (marine 4.3%)
- **Soil**: 14.3% (agricultural 2.8%)
- **Plant**: 2.9% (rhizosphere 0.6%)

---

## Experimental Procedure

### 1. Data Retrieval and Quality Control
- Downloaded raw reads from NCBI SRA
- Quality filtering: bases with quality < 10 trimmed; reads < 75bp or > 5% low-quality bases discarded
- Final dataset: 6.87 trillion raw reads → 214 billion SSU rRNA sequences

### 2. OTU Assignment Pipeline
- **Tool**: MAPseq (high-performance read mapper)
- Mapped against MAPref reference database
- Hierarchical clustering at 90%, 96%, 97%, 98%, 99% identity thresholds
- Confidence cutoff: 0.5 for read assignments
- Taxonomic assignment: 90% consensus annotation from RefSeq and LTP

### 3. Community Clustering
- Bray-Curtis dissimilarity on log-transformed relative abundances
- Average linkage hierarchical clustering (threshold: 0.5)
- Result: 356,182 community clusters → 26,487 robust clusters (≥5 samples)

### 4. Metadata Extraction
- Geographic coordinates: parsed from 31 distinct SRA annotation fields using 11 regular expressions
- Environmental ontology: two-tiered manual annotation (4 main, 65 sub-environments)
- IUCN ecosystem mapping: 98,642 soil samples linked to Ecosystem Functional Groups
- Keyword extraction: automated from sample metadata with semantic clustering using LLM (Llama-3.2-3B)

### 5. Statistical Analyses
- **Diversity estimation**: Good-Turing frequency estimator extrapolation
- **Beta diversity**: Bray-Curtis, weighted/unweighted UniFrac
- **Latitudinal analyses**: Pearson correlations with binned latitudes
- **Generalism scores**: Normalized Shannon entropy across four environments
- **Visualization**: UMAP projections, PERMANOVA, Mantel tests

### 6. Genome and Culture Mapping
- proGenomes3: 97.3% of 16S sequences mapped to MicrobeAtlas OTUs (at 97% identity)
- BacDive: 92.6% of strains mapped to MicrobeAtlas OTUs
- Gene counting: Prodigal for genome size analysis

---

## Key Figures and Evidence

### Figure 1: Pipeline Overview
- Shows data retrieval from SRA → quality filtering → OTU assignment → community clustering → web resource
- Highlights: 214 billion SSU rRNA reads, 651,275 hierarchical OTUs, interactive web resource

### Figure 2: Global Microbiome Structure (UMAP)
- Communities cluster by main and sub-environment (PERMANOVA R² = 14.7% main, 21.7% sub)
- Animal (red) clusters separate from environmental (aquatic: teal, soil: green)
- Community clusters do not saturate with sampling, indicating undiscovered diversity
- OTU richness: soil/freshwater highest (715-1,257 OTUs), insects lowest (281 OTUs)

### Figure 3: Taxonomic Characterization
- 88.7% of OTUs lack cultures or genomes (ncg-OTUs)
- ncg-OTUs more common in environmental samples (>77% of reads at phylum+ level)
- Classification depth vs. richness negative correlation (Pearson ρ = -0.36)
- Phylum-level OTUs often highly diverse and abundant (e.g., Candidatus Marinimicrobia)

### Figure 4: Biogeographic Patterns
- Global sampling coverage: 61% of 9° × 9° latitude-longitude bins
- Marine diversity peaks at equator (consistent with latitudinal diversity gradient)
- Terrestrial diversity peaks at 20°N-40°N (temperate-boreal forests, deserts, intensive land-use)
- Examples: Pelagibacter (marine) vs. Fonsibacter (freshwater) niche separation
- 37,393 OTUs with significant latitudinal preferences: 93.3% equatorial, 6.7% polar

### Figure 5: Habitat Generalism
- Generalists inhabit more community clusters than specialists (1,239.5 vs. 263.9)
- Generalists 6.85× more likely to have cultured representatives
- Genome size increases with generalism (36.4% more genes for high generalists)
- Specialist families: Lachnospiraceae, Prevotellaceae, Desulfobacteraceae
- Generalist families: Pseudomonadaceae, Bacillaceae

---

## Major Findings

1. **Scale**: 2.4 million uniformly analyzed samples - largest cross-study microbiome resource
2. **Dark Matter**: 88.7% of OTUs lack cultures/genomes; concentrated in environmental samples
3. **Biogeography**: Strong latitudinal trends; marine equatorial diversity peaks; soil sampling biases
4. **Ecology**: Soil/plant microbes more generalist; animal/aquatic more specialist; oxygen tolerance drives patterns
5. **Genomics**: Generalists have larger genomes suggesting metabolic flexibility
6. **Blind Spots**: Northern mid-latitudes over-represented; Southern Hemisphere, tropics, polar regions under-sampled

---

## Limitations

- Reference-based approach may miss understampled microbial groups
- Generalism scores based on coarse-grained habitat classifications
- Metadata heterogeneity restricts analyses to confident subsets
- Taxonomic classification lags for eukaryotes

---

## Resource Availability

- **Website**: https://microbeatlas.org
- **Download**: https://microbeatlas.org/download
- **Updates**: Regular updates planned (next release: 6.3 million samples)

---

## Software and Tools Used

- **Read mapping**: MAPseq (high-performance SSU rRNA mapper)
- **Clustering**: HPC-CLUST v1.2
- **Visualization**: UMAP, matplotlib, seaborn
- **Statistical analysis**: PERMANOVA, Mantel tests, GLMs
- **Genome analysis**: Prodigal, Barrnap

---

## Citation

```
Matias Rodrigues et al., The MicrobeAtlas database: Global trends and insights into Earth's microbial ecosystems, 
Cell (2026), https://doi.org/10.1016/j.cell.2026.01.021
```