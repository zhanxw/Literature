# Paper Summary

### Authors
- Russell J. S. Orr
- Ola Brynildsrud
- Kari O. Boifot
- Jostein Gohli
- Gunnar Skogan
- Frank J. Kelly
- Mark T. Hernandez
- Klas Udekwu
- Patrick K. H. Lee
- Christopher E. Mason
- Marius Dybwad

### Journal
- Microbiome (BMC)

### Publication Date
- 2026

### DOI
- https://doi.org/10.1186/s40168-025-02303-7

## Keywords
- public transit aerobiome
- shotgun metagenomics
- low-biomass contamination control
- city-specific microbiome
- fungal profiling
- interannual stability
- core microbiome

## Main Idea
- This study characterizes spatial and temporal structure of airborne microbiomes in public transit systems across multiple global cities using shotgun metagenomics.
- The authors test whether transit aerobiomes have city-specific signatures, whether these signatures are stable across years, and whether a global species-level core exists.

## Evidence Supporting the Main Idea
- Sampling/evidence scale: 750 transit air samples from six cities over three summers (2017-2019), plus 22 negative controls and 5 positive controls.
- Strong contamination handling in low-biomass data: 290 contaminant taxa were identified (265 bacterial, 25 fungal), and 62.7% of reads were removed as contamination before ecological interpretation.
- Fungal signal increased compared with earlier analyses by using expanded fungal references: reported fungal classified reads were 25.3% (vs much lower values in prior database-limited analyses).
- Statistical analyses indicate city is a major driver of community structure (reported as highly significant, p < 1.0E-4).
- A strict global core at >97% prevalence was not found; the most prevalent species did not reach universal presence across all cities.
- Figures/tables in the paper report city-separated diversity/community patterns and prevalence-based core/sub-core outcomes, supporting city-specific and not globally uniform aerobiomes.

## Main Novelty
- First large-scale interannual (3-year) multi-city transit aerobiome metagenomic analysis with species-level bacterial and fungal emphasis.
- An explicit low-biomass contamination workflow combining field/lab controls and statistical filtering before downstream ecological inference.
- Demonstration that local (city-level) cores are detectable while a strict global species-level core is not, refining expectations for urban airborne microbiome structure.

## Datasets Used for Evaluation
- Public transit air metagenomes:
- 750 samples total from Denver (38), Hong Kong (239), London (117), New York (125), Oslo (191), Stockholm (40).
- Time coverage: summers of 2017, 2018, and 2019 (Stockholm not sampled in 2019).
- Controls:
- 22 negative controls (field and lab blanks).
- 5 positive controls (ZymoBIOMICS standard).
- Sequencing:
- Illumina NovaSeq 6000, 150 bp paired-end reads.
- Mean depth reported by year: about 9.4M (2017), 76.4M (2018), 71.2M (2019) reads/sample.
- Public repositories:
- BioProjects PRJNA561080, PRJNA1129830, PRJNA1132165.

## Experimental Procedure
- Collect transit air using high-volume electret filter sampling at standardized height/orientation and runtime.
- Extract DNA from filters with lysis + enzymatic/mechanical disruption + cleanup, then quantify DNA.
- Prepare sequencing libraries and run NovaSeq paired-end sequencing.
- Perform QC/trimming and remove host (human) reads.
- Classify reads using Kraken2/Bracken with cross-kingdom and FBAV-oriented reference resources including expanded fungal genomes.
- Use negative controls plus rule-based/statistical filtering to remove likely contaminants.
- Compute alpha/beta diversity and multivariate statistics to test effects of city/year/environmental covariates.
- Define core/sub-core taxa by prevalence thresholds and compare local vs global core structure.

## Key Biology Insights
- Public transit aerobiomes are strongly city-structured rather than globally homogeneous at species level.
- Interannual sampling indicates relative stability of city-level diversity/community patterns across the studied summers.
- Fungi are a substantial component of transit aerobiomes when fungal references are sufficiently represented.
- Local city cores likely reflect regional environmental and human-activity influences on airborne microbial exposure.

## Implications
- Urban airborne microbiome surveillance should prioritize city-specific baselines over assumptions of a universal species core.
- Low-biomass contamination control is essential; conclusions can change substantially without rigorous control filtering.
- Improved fungal reference databases materially increase interpretability and should be standard in aerobiome metagenomics.
