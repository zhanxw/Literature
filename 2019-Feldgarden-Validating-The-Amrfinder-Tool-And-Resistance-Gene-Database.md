# Paper Summary

## Keywords
- antimicrobial resistance
- AMRFinder
- resistance gene database
- genotype-phenotype correlation
- NARMS
- bacterial genomics

## Main Idea
- The study validates **AMRFinder** and the NCBI Bacterial Antimicrobial Resistance Reference Gene Database as a high-accuracy system for AMR gene detection from bacterial genomes.
- It tests whether AMR genotypes inferred from WGS match phenotypic susceptibility results at surveillance scale.

## Evidence Supporting the Main Idea
- Database/tool scope reported: 4,579 AMR proteins and >560 HMMs, with curated nomenclature and family hierarchy.
- Validation cohort: 6,242 NARMS isolates (5,425 *Salmonella enterica*, 770 *Campylobacter* spp., 47 *E. coli*).
- Phenotype concordance: 87,679 AST tests; 98.4% genotype-phenotype consistency.
- Predictive values reported: PPV 95.5%, NPV 99.2%.
- Organism-level consistency examples:
- *E. coli*: 99.7% consistency in tested set.
- *S. enterica*: 98.0% consistency.
- Comparative analysis with 2017 ResFinder version:
- 1,229 gene-symbol differences observed.
- AMRFinder missed 16 loci found by ResFinder; ResFinder missed 216 loci identified by AMRFinder.
- These results support robust AMR gene calling and naming performance for high-throughput surveillance.

## Main Novelty
- Integrates curated AMR protein references + validated HMMs + hierarchical naming logic to improve specificity and gene-symbol assignment quality.
- Provides large-scale, publicly anchored genotype-phenotype validation across major foodborne pathogen surveillance isolates.
- Offers a local, automatable AMR detection workflow for genomic surveillance programs.

## Datasets Used for Evaluation
- Primary validation dataset:
- NARMS isolate collection with both WGS and AST phenotypes.
- Sample size: 6,242 isolates after quality filtering.
- Taxa: 5,425 *Salmonella enterica*, 770 *Campylobacter* spp., 47 *Escherichia coli*.
- Phenotype tests: 87,679 antimicrobial susceptibility tests.
- Reference resources:
- NCBI Bacterial Antimicrobial Resistance Reference Gene Database.
- Comparative benchmark against ResFinder (2017 version).

## Experimental Procedure
- Curate AMR protein/HMM reference data with standardized nomenclature.
- Assemble and annotate bacterial genomes from surveillance isolates.
- Run AMRFinder to identify AMR genes/alleles and infer resistance genotypes.
- Compare predicted resistance against AST phenotypes for each antimicrobial test.
- Compute overall and per-organism consistency metrics (including PPV/NPV).
- Compare gene-calling outputs with ResFinder to quantify call differences and missed loci.
