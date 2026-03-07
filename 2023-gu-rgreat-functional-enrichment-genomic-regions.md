# Paper Summary

### Authors
- - Zuguang Gu
- Daniel Hubschmann

### Journal
- - Bioinformatics (Applications Note)

### Publication Date
- - 2023 (Advance Access: November 17, 2022)

### DOI
- - https://doi.org/10.1093/bioinformatics/btac745

## Keywords
- genomic regions enrichment
- GREAT
- rGREAT
- Bioconductor
- Gene Ontology
- Ensembl BioMart
- background regions
- Not specified in paper

## Main Idea
- The paper introduces `rGREAT`, an R/Bioconductor implementation of the GREAT algorithm for functional enrichment on genomic regions that runs locally rather than only through the GREAT web server.
- It addresses key limitations of the web service, especially limited organism/gene-set support, older annotations, and limited extensibility for user-defined resources.
- Not specified in paper

## Evidence Supporting the Main Idea
- The authors report local support for more than 600 organisms and integration of GO gene sets plus MSigDB for human analyses.
- `rGREAT` exposes programmatic support for both online GREAT (`submitGreatJob()`, `getEnrichmentTables()`) and local GREAT (`great()`, `shinyReport()`).
- The method section details enrichment modeling with binomial tests for region-centric association domains and discusses the hypergeometric setting when strict background subsets are used.
- The paper shows local GREAT can use updated GO annotations from Bioconductor (`GO.db`, updated twice yearly) and compares online vs local results across multiple TFBS datasets, reporting generally consistent outcomes.
- Supplementary analyses discuss practical background handling (including exclusion of gap/unsequenced regions) and show these choices materially affect enriched-term calls.
- Not specified in paper
- PDF front-matter/context line: Advance Access Publication Date: 17 November 2022
- PDF front-matter/context line: rGREAT: an R/bioconductor package for functional
- PDF front-matter/context line: Molecular Precision Oncology Program, National Center for Tumor Diseases (NCT), Heidelberg 69120, Germany, 2Heidelberg Institute

## Main Novelty
- A local, extensible GREAT workflow in R/Bioconductor with modern annotation integration and user-defined organism/gene-set support.
- A generalized and practical framework for background-region handling in enrichment analysis within the GREAT paradigm.
- Distribution of `BioMartGOGeneSets` to enable GO-based enrichment for many non-model organisms.
- Not specified in paper

## Datasets Used for Evaluation
- Demonstration datasets include TFBS region sets and chromatin-state-based backgrounds in supplementary analyses.
- Public annotation resources include GO annotations, MSigDB (human), and Ensembl BioMart-derived gene sets.
- Exact per-dataset sample sizes for the TFBS demonstrations are not specified in the paper text.
- Not specified in paper

## Experimental Procedure
- Implement GREAT web-service wrappers for reproducible programmatic submissions and result retrieval.
- Implement local GREAT (`great()`) with organism- and gene-set-specific enrichment.
- Construct gene regulatory domains around TSS (basal + extension rules), map input regions, and compute enrichment statistics.
- Evaluate background modeling options (`background`, `exclude`) and compare local binomial-based treatment to hypergeometric assumptions.
- Compare local vs web GREAT outputs and assess sensitivity to alternative TSS annotations.
- Compile and package GO gene sets from Ensembl BioMart for broad-species support.
- Not specified in paper

## Key Biology Insights
- The paper is primarily a computational-methods/software contribution.
- Biological discoveries are not the main outcome; the key insight is that annotation freshness and proper background definition can substantially change downstream biological interpretation of genomic-region enrichment.
- Not specified in paper

## Implications
- `rGREAT` enables reproducible, scalable enrichment analysis directly inside Bioconductor workflows.
- The package is especially useful for non-model organisms and custom gene sets where web-tool limitations are restrictive.
- Better control of annotation versions and background definitions can reduce false positives and improve interpretability in genomics/epigenomics studies.
- Not specified in paper
