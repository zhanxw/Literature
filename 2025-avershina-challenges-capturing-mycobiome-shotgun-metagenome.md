# Challenges in capturing the mycobiome from shotgun metagenome data: lack of software and databases

**Authors:** Ekaterina Avershina, Arfa Irej Qureshi, Hanne C. Winther-Larsen, Trine B. Rounge  
**Journal:** *Microbiome* (2025), 13:66  
**DOI:** [10.1186/s40168-025-02048-3](https://doi.org/10.1186/s40168-025-02048-3)  
**Source:** [PMC11887097](https://pmc.ncbi.nlm.nih.gov/articles/PMC11887097/)

## Summary

The gut mycobiome—the fungal component of the microbiome—is biologically important but remains much less studied than the bacterial microbiome. A major bottleneck is the lack of robust software and sufficiently comprehensive reference databases for identifying fungi and estimating their abundance from shotgun metagenomic data. This study benchmarks currently available tools using simulated fungal communities with known composition.

The authors surveyed tools claiming to perform fungal taxonomic classification. FindFungi was excluded because it was outdated and could not be made functional without substantial modification. Six tools were evaluated: Kraken2, MetaPhlAn4, EukDetect, FunOMIC, MiCoP, and HumanMycobiomeScan (HMS). FunOMIC and HMS also required source-code modifications to run reliably.

The benchmark used 18 mock communities containing 10, 50, 100, or 165 fungal genomes from Ascomycota and Basidiomycota, with either equal-read or equal-coverage abundance profiles. The authors also tested communities containing 90% or 99% bacterial background to mimic the low abundance of fungi in real gut metagenomes.

## Main findings

- The tools showed limited agreement. *Candida orthopsilosis* was the only species consistently identified by every tool whenever it was present.
- FunOMIC detected the largest number of species, but it required code changes and was not consistently the closest to the known abundance profile.
- EukDetect and MiCoP produced the most accurate overall predictions for taxonomic identification and relative abundance; among the whole-genome reference tools, MiCoP performed best when the same reference database was used.
- MetaPhlAn4 correctly identified all genera in the mock communities, although species-level performance was less complete.
- Increasing community richness improved Kraken2 precision and improved abundance estimates for all tools at species, genus, and family levels.
- Adding 90% or 99% bacterial reads did not significantly reduce the performance of EukDetect, FunOMIC, or MiCoP.
- Reference-database composition was a major determinant of performance, limiting comparisons between tools and constraining detection of poorly represented or uncatalogued fungi.

## Interpretation

The study shows that automated mycobiome profiling from shotgun data is feasible, but current tools are not yet interchangeable or sufficiently robust for routine use. The central limitation is not only algorithmic accuracy: software maintenance, reproducibility, database completeness, and inconsistent abundance-estimation procedures are equally important problems. The results support using more than one classifier and interpreting species-level calls cautiously, especially for low-abundance or poorly represented taxa.

## Limitations

The benchmark used simulated reads generated from curated NCBI RefSeq genomes, so it does not capture all experimental biases, strain diversity, DNA-extraction effects, sequencing errors, or host-derived contamination found in clinical samples. The study evaluated taxonomic profiling rather than fungal functional profiling, and the conclusions depend partly on the selected genomes and databases.

## Take-home message

Current mycobiome profilers can recover useful signal from shotgun metagenomes, but none produced a fully concordant community profile. EukDetect and MiCoP were closest to the expected compositions, while FunOMIC had strong species-detection capacity. Progress will require better-maintained software and substantially broader, better-curated fungal reference databases.
