# Paper Summary

### Authors
Hyunbin Lee, Sofia Luengo-Woods, Jianxiu Zhang, Kira S. Makarova, Yuri I. Wolf, Collin Chiu, Simone A. Evans, Junyi Chen, Haopeng Xiao, Liang Feng, Eugene V. Koonin and Alex Gao. Lee, Luengo-Woods and Zhang contributed equally.

### Journal
Nature 657, 735–743 (2026).

### Publication Date
29 July 2026 (updated 17 August 2026).

### DOI
[10.1038/s41586-026-10852-6](https://doi.org/10.1038/s41586-026-10852-6)

## Keywords
Bacterial immunity; bacteriophages; STAND NTPases; antiviral defence; pattern recognition; cryo-EM; protein structure; NLR-like receptors.

## Main Idea
The authors show that bacterial antiviral STAND NTPases use structure-based pattern recognition to detect conserved bacteriophage proteins. A systematic survey identifies at least 90 structurally distinct antiviral-associated families. Avs7 recognizes the major capsid protein (MCP), assembles with MCP and host elongation factor Tu (EF-Tu) into an active nuclease complex, and 13 additional families recognize conserved phage structural or replication proteins.

## Evidence Supporting the Main Idea
- Genome mining began with 656 seed STAND proteins and expanded to 359,879 representatives in 589 clades; 198 clades were classified as defence-associated (Fig. 1; Supplementary Tables 1–5).
- In *E. coli*, *Salmonella enterica* Avs7 protected against nine Drexlerviridae phages. Proteomics enriched the T1 MCP and *E. coli* EF-Tu in Avs7 pulldowns, while a 73-gene ZL19 screen identified MCP as the specific trigger (Fig. 2; Extended Data Fig. 3).
- Reconstituted Avs7, MCP and EF-Tu formed an approximately 1:1:1 complex. DNA degradation required Avs7 and MCP and was enhanced by EF-Tu.
- Cryo-EM resolved a roughly 1-MDa asymmetric, butterfly-shaped tetramer at 3.43 Å and a roughly 250-kDa monomeric complex at 3.40 Å (Fig. 3; Extended Data Fig. 4).
- A screen of 600 phage genes from 36 diverse phages and viruses found 13 more responsive STAND families. A follow-up panel of 218 target homologues measured 4,360 Avs–target pairs and showed broad cognate recognition with minimal cross-reactivity (Fig. 5).
- AlphaFold2/3 models gave high-confidence complexes for 11 of 13 new Avs–target pairs (ipTM 0.71–0.91), supporting recognition of conserved core folds rather than sequence identity (Fig. 6).

## Main Novelty
This work expands bacterial phage sensing to a broad, phylogenetically distributed repertoire. It identifies host-factor repurposing—recruitment of inactive EF-Tu by Avs7—as part of receptor assembly, and establishes recognition of conserved three-dimensional protein folds as a general antiviral strategy.

## Datasets Used for Evaluation
- **STAND sequence survey:** 656 seed proteins expanded to 359,879 representatives clustered at 75% identity across 589 clades; used for phylogeny and defence classification.
- **Avs7 phage panel:** nine Drexlerviridae coliphages, including ZL19 and T1; used for plaque-based protection assays in *E. coli*.
- **Avs7 trigger library:** 73 barcoded genes from phage ZL19; used to identify MCP as the activation trigger.
- **Broad trigger library:** 600 genes from 36 diverse phages and viruses, including ssRNA, ssDNA, tailed dsDNA and tailless dsDNA phages; used to discover 13 additional Avs families.
- **Homologue interaction panel:** 218 phage-protein homologues plus 27 additional genes; 4,360 pairwise tests with 18 Avs representatives; used to assess specificity and breadth.
- **Structural datasets:** Avs7 cryo-EM maps EMD-73001–EMD-73006, EMD-48771 and EMD-48772; atomic models 9YIX, 9N01 and 9N00; used to resolve receptor assembly.
- **Proteomics:** three biological replicates of Avs7 pulldowns with TMT mass spectrometry (PXD079457); used to identify MCP and EF-Tu.

## Experimental Procedure
- Mine genomes for STAND NTPases, expand homologues with PSI-BLAST, construct phylogenies and classify defence-associated clades.
- Cluster sensor domains by sequence and predicted structure, then select Avs7 for functional analysis.
- Express Avs systems in *E. coli*, challenge cells with phages, and measure protection by plaque assays and toxicity screens.
- Use affinity pulldown, TMT mass spectrometry and barcoded phage-gene libraries to identify triggers and host factors.
- Purify Avs7, MCP and EF-Tu; reconstitute complexes and test ATP/Mg2+-dependent dsDNA nuclease activity.
- Determine apo, monomeric and tetrameric Avs7 complexes by cryo-EM and test interfaces by mutagenesis.
- Validate 13 additional Avs families, test homologue panels by barcode sequencing, and model interactions with AlphaFold2/3.

## Key Biology Insights
- Bacterial STAND receptors are structurally diverse: defence-associated sensors include TPR-like repeats, WD40 β-propellers and sulfatase-like domains.
- Avs7 recognizes the conserved HK97-fold MCP surface through extensive shape and charge complementarity.
- Avs7 co-opts the inactive, open GDP-like conformation of EF-Tu; EF-Tu enhances MCP sensitivity and stabilizes the active nuclease complex.
- Avs8 and Avs10 detect MCPs; Avs11–18 detect portal or tail-assembly proteins; Avs19–21 detect DNA polymerase, RecA/primase-helicase ATPase and ssDNA annealing proteins.
- Avs20 recognizes a conserved RecA-type ATPase fold independent of catalytic activity, while Avs21 recognizes unrelated ERF- and RecT-family ssDNA annealing proteins through a shared structural feature.

## Implications
Bacterial immunity can survey conserved phage architecture rather than rely only on rapidly evolving sequence motifs. Since core phage folds are constrained by assembly and replication, structure-based sensing may provide broad protection across phages. The catalogue also supplies candidates for discovering new defence systems. The paper does not establish the natural prevalence of each Avs system or behaviour during mixed infections.

Source: [Nature article](https://www.nature.com/articles/s41586-026-10852-6).
