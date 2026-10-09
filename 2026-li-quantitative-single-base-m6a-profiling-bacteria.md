# Paper Summary

### Authors
Youyue Li, Letong Xu, Na Liu, Xiangkai You, Jiadai Huang, Yue Sun, Beifang Lu, Chunyan Yao, and Xin Deng.

### Journal
Cell Reports

### Publication Date
25 August 2026

### DOI
[10.1016/j.celrep.2026.117831](https://doi.org/10.1016/j.celrep.2026.117831)

## Keywords
Bacterial RNA modification; N6-methyladenosine (m6A); GLORI sequencing; single-base resolution; RNA stability; methyltransferases; evolutionary conservation; bacterial epitranscriptomics; *Pseudomonas syringae*.

## Abstract
N6-methyladenosine (m6A) is widespread in eukaryotic RNA, but its bacterial distribution and function have been poorly defined. Li et al. apply GLORI sequencing to generate transcriptome-wide, single-base-resolution m6A maps in seven bacterial species. They identify 2,845 m6A sites during exponential growth, extensive condition-dependent dynamics in three strains, and virulence-pathway-associated remodeling in *Pseudomonas syringae*. Comparative analysis identifies 455 conserved m6A site pairs enriched in genes involved in growth, energy metabolism, and transmembrane transport. Integrated methylation, transcript-abundance, and RNA-stability analyses associate m6A with reduced mRNA abundance and increased RNA stability. The study further identifies the rRNA methyltransferases RlmF and RlmJ as bacterial mRNA m6A writers, providing a quantitative atlas and a foundation for studying bacterial m6A regulation and evolution.

## Main Idea
GLORI can reproducibly quantify bacterial m6A at single-base resolution. Bacterial m6A is species-specific, locally clustered, dynamically reprogrammed across growth and culture conditions, and associated with conserved physiological functions and RNA-fate regulation.

## Evidence Supporting the Main Idea
- The study profiles *Escherichia coli*, *Pseudomonas aeruginosa*, *Pseudomonas syringae*, *Klebsiella pneumoniae*, *Staphylococcus aureus*, *Bacillus cereus*, and *Bacillus subtilis*, spanning Gram-negative and Gram-positive bacteria.
- Two biological replicate libraries were generated for each sample. Candidate sites required coverage >15× and modification fraction >0.1, and were retained only when reproducibly detected at identical genomic positions in both replicates.
- Replicate m6A levels were highly reproducible, with Pearson correlations >0.88 across all seven species.
- Exponential-growth m6A site counts ranged from 97 in *K. pneumoniae* to 874 in *S. aureus*, spanning 67–467 modified genes per species; the combined survey identified 2,845 sites.
- Bacterial m6A was generally enriched in coding regions, showed species-specific distribution patterns, and lacked the strong single-motif preference typical of eukaryotic m6A. CRAUC was the most prevalent context, representing 7.1% of mRNA m6A sites.
- Stationary-phase site counts increased by 6.2%–128.0% relative to exponential phase in *E. coli*, *P. aeruginosa*, and *P. syringae*; 15.5%–65.7% of sites showed phase-dependent methylation changes.
- In *P. syringae*, virulence-related m6A patterns differed between virulence-repressing King’s B medium and virulence-inducing minimal medium, including changes affecting type III secretion system-associated genes.
- Comparative analysis identified 455 conserved m6A site pairs, enriched in genes supporting growth, energy metabolism, and transmembrane transport.
- Integration with RNA abundance and lifetime data associated m6A with lower mRNA abundance but longer RNA lifetime.

## Main Novelty
This is a quantitative, single-base-resolution atlas of bacterial m6A across seven species. It combines reproducible site calling, growth- and condition-dependent methylome analysis, cross-species conservation, RNA-fate measurements, and writer-enzyme validation in one study.

## Datasets Used for Evaluation
- **Seven-species GLORI survey:** total RNA and rRNA-depleted RNA libraries from the seven bacterial species listed above; two biological replicates per sample. Used for baseline m6A mapping, distribution, abundance, and motif analysis.
- **Growth-phase dataset:** *E. coli*, *P. aeruginosa*, and *P. syringae* profiled during exponential and stationary phases. Used to measure growth-phase reprogramming.
- **Virulence-condition dataset:** *P. syringae* grown in King’s B medium and minimal medium; *P. aeruginosa* and *P. syringae* virulence genes were cross-referenced with VFDB 2025. Used to assess virulence-associated methylation.
- **Cross-species orthology dataset:** orthologs identified with OrthoFinder and aligned at conserved adenines using ±2-nt flanking sequences. Used to identify 455 conserved m6A site pairs.
- **Public RNA lifetime dataset:** *E. coli* RNA lifetime data from GSE144943. Used to assess the relationship between m6A and RNA stability.
- **Public translation dataset:** *P. syringae* translation-efficiency data from GSE216157. Used in analyses of m6A-associated transcript behavior.
- **RNA-seq datasets generated in this study:** *P. aeruginosa* and *P. syringae* expression measurements used with m6A calls for transcript-abundance analyses.

## Experimental Procedure
- Validate GLORI on known 23S rRNA m6A sites A1618 and A2030 across four Gram-negative and three Gram-positive species.
- Deplete bacterial rRNA and apply GLORI chemical conversion; sequence two biological replicates per sample.
- Call reproducible sites using coverage and modification-fraction thresholds, then quantify site abundance, stoichiometry, genomic distribution, gene length, and sequence context.
- Compare exponential and stationary phases in three species and compare King’s B versus minimal medium in *P. syringae*.
- Perform virulence-gene overlap and Gene Ontology enrichment analyses.
- Identify conserved sites with OrthoFinder-based orthology and cross-species sequence alignment.
- Integrate m6A calls with public RNA lifetime and translation-efficiency data and study-generated expression data.
- Test RlmF and RlmJ using knockout/overexpression comparisons, m6A quantification, and locus-specific SELECT validation; FTO treatment was used as an additional validation assay.

## Key Biology Insights
- Bacterial m6A is not uniformly distributed: species differ in site counts, methylation levels, genomic localization, and sequence context.
- m6A sites tend to cluster locally and exhibit elevated methylation levels; modified genes are generally longer than unmodified genes.
- m6A methylomes are dynamically reprogrammed between exponential and stationary growth and across virulence-related culture conditions.
- Conserved sites preferentially occur in core physiological genes, supporting an evolutionary component to bacterial m6A regulation.
- m6A is associated with decreased transcript abundance but increased RNA lifetime, indicating that abundance and stability effects can coexist.
- RlmF and RlmJ contribute to bacterial mRNA m6A methylation in addition to their established rRNA functions.

## Implications
The work establishes GLORI as a reproducible method for bacterial single-base m6A profiling and provides a reference atlas for bacterial epitranscriptomics. The condition-sensitive and conserved sites, together with RlmF/RlmJ validation, offer targets for mechanistic studies of growth, stress adaptation, virulence, and RNA turnover. The reported associations remain primarily correlative for transcript abundance and stability; causal effects will require targeted site and enzyme perturbation experiments.

**Source:** Li et al., Cell Reports (2026), DOI [10.1016/j.celrep.2026.117831](https://doi.org/10.1016/j.celrep.2026.117831). Full text accessed through the open-access Cell Reports article page.
