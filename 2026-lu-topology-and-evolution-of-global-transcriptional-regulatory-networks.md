# Paper Summary

### Authors

Beifang Lu, Tongtong Feng, Letong Xu, Na Liu, Tianmin Li, Zhihao Guo, Jing Wang, Runsheng Li, Xuemei Yang, Sheng Chen, and Xin Deng.

### Journal

Nature Communications.

### Publication Date

22 October 2026.

### DOI

[10.1038/s41467-026-78154-z](https://doi.org/10.1038/s41467-026-78154-z)

## Keywords

Klebsiella pneumoniae; carbapenem-resistant hypervirulent K. pneumoniae; transcription factors; DAP-seq; gene regulatory network; virulence; antimicrobial resistance; pan-genome; deep learning.

## Main Idea

The study builds a global transcriptional regulatory network (GRN) for the clinically relevant carbapenem-resistant hypervirulent K. pneumoniae isolate CR-HvKP4 and tests how well that network generalizes across the K. pneumoniae pan-genome. The authors characterize 370 transcription factors (TFs) by DAP-seq, identify network hubs and hierarchical information flow, connect TFs to virulence and antimicrobial-resistance pathways, validate four regulators experimentally, and develop a sequence-based predictor for TF-DNA binding in other isolates.

## Evidence Supporting the Main Idea

- DAP-seq identified 72,336 TF-DNA peaks for 370 TFs; 56.4% of binding events were promoter-proximal, and 239 TFs had high-affinity peaks under the study's signal-value threshold (Fig. 1 and Supplementary Data 1).
- The CR-HvKP4 GRN contained 365 TFs, 26,019 potential regulatory relationships, and 4,068 target genes. Its degree distribution and closeness-centrality profile were consistent with a hub-containing, hierarchical biological network (Fig. 2).
- Twenty-five TFs were connected to eight major virulence pathways, including capsule, LPS, siderophore, secretion, pilus/fimbriae, biofilm, peptidoglycan, and toxin-antitoxin systems. EMSA supported selected TF-promoter interactions (Fig. 2d-f and Supplementary Fig. 5).
- The antimicrobial-resistance subnetwork highlighted seven resistance-associated hubs. The efflux-pump gene oqxB had binding co-localization with 34 TFs, while RS00760 showed the densest connectivity among the prioritized regulators (Fig. 3).
- Growth-phase RNA-seq at 2, 4, 9, and 24 hours found that more than 88% of TFs maintained relatively steady expression across the time course. Sixty-one middle-layer TFs generally had higher expression than bottom-layer TFs before the death phase, suggesting that they act as regulatory signal-processing hotspots (Fig. 4).
- Four TF deletions—RS00760, RS12175, VmrR/RS15210, and FtrA/RS21375—were profiled by RNA-seq at mid-log and early stationary phases. VmrR controlled a 170-gene regulon, including 39 directly bound genes and 28 promoter-bound genes (Fig. 5).
- In female mice, deletion of vmrR reduced lung pathology and lung colonization relative to wild type; complementation restored the phenotype. The histology experiment used three mice per group, and the CFU colonization experiment used 6 wild-type, 6 ΔvmrR, and 8 complemented animals (Fig. 5h-i).
- Across 2,059 genomes, 366 of the 370 TFs met the pan-genome inclusion criteria and 63.1% were core or soft-core. TFs were more conserved in presence frequency than non-TF genes (Mann–Whitney U test, p = 4.9 × 10^-5), while SNP frequencies were comparable (Fig. 6).
- A deep-learning model trained on 96 TFs achieved AUROC 0.84, AUPRC 0.74, and MCC 0.508 on an independent test set. Fifty of the 96 TFs had AUROC > 0.80, and 81 had F1-score > 0.50 (Fig. 7).

## Main Novelty

This is a broad, experimentally anchored map of the K. pneumoniae transcriptional regulatory landscape that integrates high-throughput TF binding, network topology, growth-phase transcriptomics, mutant validation, cross-strain conservation, and predictive modeling. A notable conceptual result is the three-tier hierarchy—90 top-layer, 61 middle-layer, and 213 bottom-layer TFs—with dominant downward information flow and top-layer TFs acting as frequent intermediates. The study also names RS15210 VmrR and links it mechanistically to virulence and colonization.

## Datasets Used for Evaluation

- **CR-HvKP4 reference isolate:** A clinical carbapenem-resistant hypervirulent K. pneumoniae strain; its genome was used for TF selection, DAP-seq, GRN construction, RNA-seq, mutant studies, and virulence assays.
- **DAP-seq dataset:** Binding profiles for 370 TFs in CR-HvKP4, yielding 72,336 peaks overall (70,564 peaks were used in the signal-value distribution shown in Fig. 1c, with plasmid-associated peaks excluded there).
- **Growth-phase transcriptomes:** CR-HvKP4 RNA-seq at 2 h (early exponential), 4 h (mid-log), 9 h (stationary), and 24 h (death) to quantify temporal TF and target-gene expression.
- **TF-deletion transcriptomes:** RNA-seq for four TF mutants at 4 h and 9 h, used to define direct, indirect, and full regulons.
- **Mouse acute lung infection dataset:** Female mice infected intranasally with wild-type, ΔvmrR, or complemented bacteria; histology used n = 3 per group, and lung CFU used n = 6, 6, and 8, respectively.
- **K. pneumoniae pan-genome:** 2,058 NCBI-published strains plus CR-HvKP4 (2,059 total), comprising 73,234 genes; used to assess TF conservation, sequence-type structure, and geography.
- **Cross-strain validation panel:** HKU57 (ST15), MGH78578 (ST38), and SH12 (ST11), compared with CR-HvKP4. Genome comparisons showed at least 92% gene conservation, and DAP-seq for three TFs tested conservation of binding patterns.
- **Machine-learning binding dataset:** Filtered CR-HvKP4 DAP-seq data for 96 TFs with at least 30 significant peaks each. Negative examples combined unbound coding/intergenic regions with peaks shuffled across TFs; the final negative-to-positive event ratio was 2:183. The independent test set evaluated TF-DNA binding prediction.

## Experimental Procedure

- Select TF candidates from the CR-HvKP4 genome using annotation keywords and DNA-binding domain validation.
- Express and purify TF proteins, construct genomic-DNA libraries, and perform DAP-seq against the CR-HvKP4 genome.
- Call TF binding peaks, quantify signal values, identify motifs with MEME, and map peaks to nearby genomic features.
- Assemble the GRN and analyze degree, closeness centrality, COG modules, virulence pathways, antimicrobial-resistance loci, and three-node regulatory cascades.
- Validate selected TF-promoter interactions by EMSA and examine regulatory effects using targeted expression assays.
- Measure transcriptomes at four growth phases, classify temporal TF-expression patterns, and validate selected trends by RT-qPCR.
- Construct four TF deletion strains, perform RNA-seq at 4 h and 9 h, and combine differential expression with DAP-seq binding to define direct and indirect regulons.
- Test VmrR function using biofilm and string assays, late-stationary-phase RT-qPCR, and an acute mouse lung infection/colonization model with complementation.
- Build a 2,059-strain pan-genome with Prokka and Roary, compare TF conservation and SNP frequencies, and analyze sequence-type and geographic patterns with Kleborate.
- Train a two-stream deep-learning model using one-hot DNA sequences and ESM-DBP protein embeddings, followed by cross-attention and transformer layers; evaluate it on an independent test set with AUROC, AUPRC, MCC, F1-score, and feature-attribution analysis.

## Key Biology Insights

- K. pneumoniae regulation is organized as a hierarchical, hub-rich network rather than a flat collection of isolated TF-target interactions.
- Twenty-five TFs connect strongly to virulence programs, with VmrR/RS15210 spanning all nine COG functional categories and regulating capsule, LPS, siderophore, fimbrial, and secretion-associated genes.
- VmrR activity is growth-phase dependent: direct binding to capsule genes was not reflected at the earlier RNA-seq time points but became functionally evident at 16 h, illustrating that TF abundance and regulatory output are not equivalent.
- The high conservation of TFs across strains supports transfer of parts of the CR-HvKP4 regulatory framework to other K. pneumoniae backgrounds, although sequence-type-specific and geographic patterns remain.
- Regulatory conservation is experimentally supported for selected TFs across four strains, but not every regulator is equally transferable; for example, RS18490 showed limited motif-peak overlap compared with RS00760 and RS12175.
- The model suggests that protein sequence and local DNA sequence can jointly predict regulatory interactions in new isolates, enabling rapid hypothesis generation for virulence-network studies.

## Implications

The study provides a resource for prioritizing K. pneumoniae regulators as potential anti-virulence or antimicrobial-resistance intervention targets and for transferring regulatory hypotheses to newly sequenced clinical isolates. VmrR is a particularly promising candidate because its deletion reduced biofilm-associated phenotypes, lung pathology, and colonization. The released data and predictor may support strain-specific GRN reconstruction from a TF sequence, genome FASTA, and GFF annotation.

Interpretation should remain cautious: DAP-seq is an in-vitro binding assay, many TFs were functionally unannotated, and the authors did not comprehensively resolve plasmid regulation despite the importance of plasmid-borne elements such as blaKPC-2 and rmpA2. The antimicrobial-resistance connections were primarily regulatory associations and were not all validated as changes in clinical drug susceptibility.

Data are available through GEO accession **GSE306886**, processed data through [Zenodo](https://doi.org/10.5281/zenodo.21786623), the trained model through [Hugging Face](https://huggingface.co/Dylan-LE/KP-GRM-predictor/tree/main/96TF), and code through [Kleb-TF](https://github.com/LuBeifang/Kleb-TF).
