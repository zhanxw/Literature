# Paper Summary

### Authors

- Rayan Chikhi, Téo Lemane, Raphaël Loll-Krippleber, Mercè Montoliu-Nerin, Brice Raffestin, Antonio Pedro Camargo, Carson J. Miller, Mateus Bernabe Fiamenghi, Daniel Paiva Agustinho, Sina Majidian, Greg Autric, Maxime Hugues, Junkyoung Lee, Roland Faure, Kristen D. Curry, Jorge A. Moura de Sousa, Eduardo P. C. Rocha, David Koslicki, Paul Medvedev, Purav Gupta, Jessica Shen, Alejandro Morales-Tapia, Kate Sihuta, Peter J. Roy, Grant W. Brown, Robert C. Edgar, Anton Korobeynikov, Martin Steinegger, Caleb A. Lareau, Pierre Peterlongo, and Artem Babaian

### Journal

- bioRxiv preprint, version 2; not certified by peer review

### Publication Date

- September 1, 2025 (version 2; version 1 was posted July 31, 2024)

### DOI

- https://doi.org/10.1101/2024.07.30.605881

## Keywords

- Logan
- Sequence Read Archive
- planetary-scale genomics
- de novo assembly
- de Bruijn graphs
- k-mer search
- metagenomics
- protein diversity
- plastic-degrading enzymes
- PETase
- HHV-6 reactivation
- plasmids
- mobile genetic elements
- antimicrobial resistance
- cloud computing

## Main Idea

- Logan converts nearly the entire December 2023 public Sequence Read Archive (SRA) from raw short reads into per-accession unitig and contig assemblies, creating a compressed and searchable representation of tens of petabases of sequencing data.
- The associated Logan-Search system indexes 31-mers from 23.4 million accessions and lets researchers search a nucleotide query across most of the SRA in minutes, while cloud-based DIAMOND searches support deeper protein-homology analysis in hours.
- The authors demonstrate the resource through diverse applications: discovery and experimental testing of plastic-active enzymes, retrospective detection of HHV-6 reactivation in cell-therapy products, expansion of known protein and mobile-element diversity, and global mapping of antimicrobial-resistance genes. These demonstrations establish utility, but Logan remains affected by SRA sampling, metadata and assembly biases and the manuscript is a preprint.

## Evidence Supporting the Main Idea

- **Near-comprehensive assembly (Figure 1 and Table 1):** From 27,764,168 public SRA accessions containing reads at least 31 bp long and totaling 50.3 petabases, Logan generated unitigs for 27.31 million accessions and contigs for 26.79 million. The authors describe this as 96% and 88% of the December 2023 SRA by input bases, respectively.
- **Compression and scale (Figure 1b):** Logan contains 4.59 petabases of unitigs compressed to 2.18 PB and 0.90 petabases of contigs compressed to approximately 0.31 PB. The contig collection represents more than 100-fold compression relative to raw base storage and is reported as 36-fold larger than GenBank WGS.
- **Massively parallel construction (Extended Data Figure 1):** Assembly took approximately 30 hours of wall-clock time, about 30 million aggregate CPU hours and a peak of 2.18 million CPU cores. Each accession was independently downloaded, assembled and uploaded in a containerized AWS Batch workflow.
- **Interactive search (Figure 1c and Table 1):** Logan-Search indexes approximately 2 × 10^15 distinct 31-mers from 23,404,655 accessions in a roughly 1-PB index. A 1-kb query takes about 6 minutes on twelve 4-vCPU machines, and the public web interface returns matching accessions plus SRA metadata and can recover the matching assembled sequences.
- **Deep homology search:** Streaming all Logan contigs through DIAMOND2 against protein queries completes in roughly 11 wall-clock hours using 60,000 vCPUs, with the manuscript estimating an almost 20-fold cost reduction relative to the earlier Serratus strategy.
- **Previously inaccessible metagenomic diversity:** Logan includes more than 130 terabases of assembled metagenome contigs from over 5.7 million accessions, 144-fold more bases than the compared MGnify short-read assemblies. Sketching estimated 33.9 trillion recurrent 31-mers, of which 32.3 trillion (95%) were absent from GenBank WGS (Figure 1d).
- **Plastic-enzyme expansion (Figure 2a-c):** Starting from 213 experimentally supported PAZy enzymes across 11 CATH domains, searches found 1.05 million nonredundant homologs in NCBI nr, then 1.12 billion matching sequences in Logan. After removing close nr matches and clustering, PETadex contained 215.7 million nonredundant candidates, a reported 205-fold expansion over nr.
- **Wet-lab PETase validation (Figure 2d-g and Extended Data Figures 3-4):** Yeast-based BHET screens identified activity in 35 of 161 natural candidates (22%) and 8 of 21 ancestral reconstructions (38%). Resampling an activity-enriched clade yielded 9 active enzymes among 13 tested (69%). HPLC confirmed that two leading enzymes exceeded IsPETase for selected products and generated approximately fourfold more terephthalic acid than engineered FAST-PETase.
- **HHV-6 discovery (Figure 3):** Two HHV-6B transcripts were queried against 1,476,236 human RNA-seq datasets in less than 5 minutes each, identifying 13 BioProjects above the coverage threshold: 4 known positive controls and 9 not previously annotated for HHV-6. In melanoma tumor-infiltrating lymphocyte products, 5 of 16 RNA-seq donors were positive, and ChIP-seq detected viral signal across all three represented clinical trials. Donor-specific viral variants argued against a shared library contaminant, but the analysis does not establish clinical consequences.
- **Protein-universe expansion (Figure 4a and Extended Data Figure 5):** Gene prediction on Logan contigs yielded 109.4 billion proteins and 3.0 billion nonredundant clusters at 90% amino-acid identity, representing almost 30-fold more diversity than UniRef50 at the compared clustering level. For 100 poorly modeled viral proteins, Logan-enriched alignments increased mean effective sequence count from 2.19 to 4.89 and AlphaFold/ColabFold pLDDT from 46.7 to 88.6; 90 of 100 models reached high predicted quality.
- **Subviral and plasmid diversity (Figure 4b-g):** Logan added 2,964 Obelisk species and increased the sequence collection to 26,263, a 3.7-fold expansion. It increased known P4-like phage-satellite diversity 4.5-fold. The plasmid analysis recovered 468,614 putatively complete circular plasmids representing 264,160 unique sequences, grouped them into 60,331 clusters and detected them across 2,095,914 samples.
- **Environmental plasmid signal:** Of Logan plasmid clusters, 92.5% contained only metagenomic sequences, and only 17.5% of metagenomic plasmids could be assigned to known replicon families versus 78.3% of isolate-derived plasmids. Logan increased measured plasmid phylogenetic diversity by as much as 21.8-fold over PLSDB and 7.0-fold over IMG/PR (Figure 4f,g).
- **Global AMR mining (Extended Data Figure 7):** Alignment to CARD identified 7.9 million AMR-positive SRA accessions and approximately 13,000 AMR-positive plasmids. Wastewater, livestock and human metagenomes were enriched for AMR genes, but this reflects deposited samples rather than a population-representative surveillance design.

## Main Novelty

- Performs independent de novo assembly at essentially SRA-wide scale rather than indexing only a selected organism, assay or subset of deposited reads.
- Publishes two complementary representations: near-lossless unitigs for sensitive k-mer discovery and more contiguous consensus contigs for gene, protein and mobile-element analyses.
- Couples the underlying assemblies to a public, interactive nucleotide search engine capable of returning SRA-scale results in minutes without requiring users to operate petabyte infrastructure.
- Demonstrates that a single open assembly resource supports experimental bioprospecting, clinical-data reanalysis, structural-biology improvement, ecological discovery and AMR mapping.
- Makes assemblies, derived datasets and most analysis or infrastructure code openly available, framing public sequence diversity as a shared scientific resource rather than a proprietary training corpus.

## Datasets Used for Evaluation

- **NCBI SRA December 10, 2023 snapshot:** 27,764,168 public accessions with average read length at least 31 bp, totaling 50.3 petabases. Unitigs were completed for 27,311,279 accessions and contigs for 26,788,829.
- **Logan v1 unitigs and v1.1 contigs:** Per-accession assembly graphs comprising 4.59 petabases of unitigs and 0.90 petabases of contigs. Associated assembly statistics include sequence counts, N50, total assembly length, longest sequence and compressed size.
- **Logan-Search index:** Roughly 2 quadrillion 31-mers from 23,404,655 accessions, grouped by library source and broad taxonomy and stored in an approximately 1-PB Bloom-filter-based index.
- **Reference sequence resources:** GenBank WGS and its FracMinHash sketches for diversity comparisons; NCBI nr, UniRef50, MGnify, BFD and other public or commercial protein collections for homology and clustering comparisons; and SRA/STAT and BioSample metadata for assay, taxonomy and geography.
- **PAZy and PETadex:** A 213-sequence query set of validated plastic-active enzymes, 1.05 million nonredundant nr homologs and 215.7 million clustered Logan-derived candidates. Experimental evaluation included 161 natural candidates, 21 ancestral reconstructions and 13 targeted clade members.
- **HHV-6 human transcriptome search:** 1,476,236 human RNA-seq accessions screened with U83 and U91 transcripts. Follow-up datasets included 26 patients receiving anti-CD19/CD22 CAR T cells, a lung-organoid dataset, and melanoma TIL products from 16 RNA-seq and 19 ChIP-seq donors across three trials.
- **Logan protein catalog:** 109.4 billion predicted proteins and 3.0 billion 90%-identity clusters. A case study used 100 viral proteins with sparse baseline multiple-sequence alignments to test effects on structure prediction.
- **Mobile-element resources:** Legacy Obelisk sequences; RefSeq P4 satellites; PLSDB and IMG/PR plasmids; and 468,614 Logan circular plasmid assemblies from 195,347 metagenome, 57,148 bacterial-isolate and 12 archaeal-isolate accessions.
- **AMR resources:** CARD for contig-level resistance-gene screening and AMRFinderPlus for plasmid annotation, combined with available SRA collection dates, geography and sample-type metadata.

## Experimental Procedure

1. Select all public SRA accessions in the December 2023 snapshot with reads at least 31 bp, then process each accession independently in a Docker container scheduled through AWS Batch.
2. Stream reads directly from the AWS SRA mirror, discard singleton 31-mers, and construct abundance-annotated unitigs with modified Cuttlefish2 and KMC3.
3. Simplify each unitig graph with Minia3 to generate consensus contigs, retain connected contigs longer than 150 bp, compress outputs with the random-access f2sz/Zstandard format and upload them with assembly statistics to public object storage.
4. Build Logan-Search by indexing approximately 2 × 10^15 unitig 31-mers with kmtricks and kmindex Bloom filters. Return accessions according to query k-mer coverage, join results to SRA metadata and optionally retrieve and BLAST the matching assembled sequence.
5. Run SRA-wide deep searches by streaming Logan contigs through DIAMOND2 for translated protein homology or minimap2 for nucleotide alignment on cloud batches.
6. Construct PETadex by searching 213 PAZy proteins against nr, clustering nr homologs at 90% amino-acid identity, searching their representatives across Logan contigs and clustering Logan-only candidates.
7. Select natural and reconstructed PETase candidates, express them on the surface of or secrete them from *Saccharomyces cerevisiae*, quantify BHET-conversion halos over time and validate leading products and enzymes by HPLC and mass spectrometry.
8. Query HHV-6B U83 and U91 transcripts against human RNA-seq accessions, require greater than 50% k-mer coverage for both genes, review BioProject metadata and confirm selected CAR T, organoid and TIL signals with read-level RNA-seq, single-cell or ChIP-seq analyses and viral-variant comparisons.
9. Predict proteins from all Logan contigs with Prodigal, cluster them through staged MMseqs2/Linclust workflows and compare the resulting diversity with existing databases. Add Logan homologs to viral-protein alignments and evaluate structure-prediction confidence.
10. Search circular contigs for Obelisks; detect P4 satellites by their conserved multi-gene modules; and identify, cluster, geographically map and functionally annotate complete plasmids, including replicons, AMR genes and antimicrobial peptides.
11. Align Logan contigs to CARD and integrate hits with SRA sample type, collection date and geographic metadata to describe the deposited-data distribution of antimicrobial resistance.

## Key Biology Insights

- Public sequencing archives contain vastly more biological diversity than curated reference databases: most recurrent metagenomic 31-mers in Logan were absent from GenBank WGS, and protein-family space expanded by orders of magnitude.
- Natural sequence diversity is directly useful for biotechnology. The PETadex screen found active enzymes at substantial hit rates and candidates whose product profiles or terephthalic-acid production exceeded commonly used natural or engineered PETases.
- Increasing homolog depth can transform protein-structure inference. For the 100-protein viral case study, expanded evolutionary information shifted most predictions from very low to high confidence without changing the structure model itself.
- HHV-6 reactivation appeared in rare proliferating CD4-positive T cells across organoid, CAR T-cell and TIL culture settings, supporting the hypothesis that prolonged ex vivo T-cell proliferation can awaken latent virus independently of the engineered receptor target. This remains an observational reanalysis requiring dedicated clinical validation.
- Environmental plasmids occupy a largely uncharacterized evolutionary space and differ from cultured-isolate plasmids: known replicons and AMR genes were less common, whereas antimicrobial-peptide genes were relatively enriched.
- P4 satellites and Obelisks are far more diverse than previously recognized, indicating that small mobile and viroid-like elements remain undersampled even in modern reference catalogs.
- AMR genes are broadly distributed across deposited human, livestock and wastewater metagenomes, but uneven sampling and incomplete metadata prevent direct inference of prevalence or temporal trends in real-world populations.

## Implications

- Logan lowers the barrier to testing sequence-level hypotheses across nearly all public short-read data and may support enzyme discovery, pathogen surveillance, mobile-element biology, protein modeling and construction of biological foundation-model training corpora.
- The unitig and contig layers serve different purposes: unitigs retain more within-sample variation for sensitive detection, whereas contigs improve interpretability and gene recovery at the cost of collapsing alleles and potentially introducing assembly errors.
- Search hits are discovery signals, not automatically biological truth. Users must confirm sequence identity, assembly context, contamination, sample metadata and appropriate controls, especially for clinical or ecological conclusions.
- SRA composition is opportunistic rather than representative. Taxonomic, geographic, assay and funding biases, inconsistent BioSample annotation and missing dates can propagate into apparent diversity and AMR patterns.
- Assembly at this scale also inherits technical limitations: singleton k-mers are discarded, contigs shorter than 150 bp can be removed, highly complex accessions may not complete contig assembly and short-read graphs can merge repeats, strains or related organisms.
- The public web search democratizes querying, but full local analysis still involves petabyte storage and substantial cloud resources. The one-time assembly infrastructure itself is described as too expensive for general external use, so maintenance and updating are important sustainability questions.
- PETase activity was measured initially with a BHET-based yeast assay rather than degradation of diverse real-world plastics under industrial conditions. Enzyme stability, expression, substrate breadth, kinetics and environmental performance require further testing.
- The manuscript is bioRxiv version 2 and has not been peer reviewed. Its very large derived resources and biological claims should be independently reproduced before high-stakes use.
