# Paper Summary

### Authors
Jakob Jung, Linda Popella, Phuong Thao Do, Patrick Pfau, Jörg Vogel, and Lars Barquist

### Journal
RNA, volume 29, pages 570–583

### Publication Date
February 7, 2023

### DOI
10.1261/rna.079263.122

## Keywords
Peptide nucleic acid; antisense oligomers; antisense antibiotics; RNA sequencing; web server; off-targets

## Main Idea
The authors introduce MASON (make antisense oligomers now), a web server and command-line tool for designing bacterial antisense oligomers—especially peptide nucleic acids (PNAs)—and predicting their melting temperature and off-target sites. Experiments show that a PNA can remain biologically active despite two terminal mismatches when at least seven consecutive bases can pair with an mRNA. Therefore, off-target prediction should account for mismatch position and the length of uninterrupted complementarity, rather than simply counting mismatches.

## Evidence Supporting the Main Idea
- MASON designs ASOs overlapping a target translation initiation region, reports sequence properties and predicted RNA–ASO melting temperatures, and screens both the transcriptome and translation initiation regions of other genes (Fig. 1).
- In *Salmonella enterica* SL1344, the fully matched 10-mer acpP PNA had a MIC of 1.25 µM. PNAs with two mismatches at terminal positions remained more inhibitory than variants with central mismatches; mm1 and mm9 had MICs of 5 µM, whereas central variants were ≥10 µM or inactive at the tested concentrations (Fig. 2; Supplemental Fig. S6).
- After 15 min at 5 µM, mm1 and mm9 significantly depleted acpP and fabF transcripts (log2FC −1.6/−1.2 and −2.1/−1.9, respectively; FDR <0.001). mm8 also depleted both transcripts, showing that seven consecutive matching bases can be sufficient for activity (Fig. 2C).
- Across Salmonella RNA-seq samples, 68 of 160 significantly depleted genes had predicted off-target sites. In the independent UPEC comparison, 176 of 369 depleted genes had translation-initiation-region off-target matches.
- Off-targets with at least seven consecutive matches were significantly enriched among depleted genes (15.8% in Salmonella and 17.7% in UPEC; hypergeometric P < 10^-23 and P < 10^-28). Requiring predicted melting temperature above 20°C increased the depleted fractions to 23.7% and 25.9% (Supplemental Fig. S11).
- Terminal mismatches were especially consequential: 50% of Salmonella and 57% of UPEC off-target genes with terminal mismatches were significantly depleted, with the fraction falling as the mismatch moved toward the center (Fig. 5A,D). Fewer than 5% of sites with six or fewer consecutive matches were depleted.

## Main Novelty
MASON combines bacterial PNA design, sequence-property reporting, melting-temperature prediction, and organism-specific off-target analysis in an accessible web interface and a higher-throughput command-line tool. The study also provides an experimentally supported operational definition of a critical off-target: at least seven consecutive matching nucleobases, with terminal mismatch placement retained in the assessment.

## Datasets Used for Evaluation
- *S. enterica* serovar Typhimurium SL1344: bacterial growth and RNA-seq experiments using one fully matched acpP PNA, nine 10-mer acpP variants with adjacent double mismatches, a scrambled control, and untreated/water controls. The study does not specify the number of biological replicates in the article text.
- Uropathogenic *Escherichia coli* (UPEC): a published RNA-seq dataset in which cells were treated with 11 PNAs targeting different essential genes; used as an independent comparison of transcript depletion and off-target patterns.
- MASON reference genomes: four preloaded strains—*E. coli* K-12 MG1655, *S. enterica* SL1344, *Clostridioides difficile* 630, and *Fusobacterium nucleatum* ATCC 23726—plus user-supplied FASTA/GFF genomes.
- Human microbiome reference collection: 2,179 complete genomes and 5,515,510 annotated transcript start regions from the Human Microbiome Project, used for optional cross-organism off-target screening.
- Human genome: GRCh38 transcript sequences, used for optional human off-target screening.
- RNA-seq accessions: GSE199542 and GSE191313.

## Experimental Procedure
- Build MASON using annotated bacterial genomes, gene coordinates, ASO length, and an allowed mismatch count; generate candidates around the start codon and optionally upstream RBS sequence.
- Predict RNA–ASO melting temperatures with a nearest-neighbor RNA–RNA model and exclude candidates with more than 60% self-complementarity.
- Screen coding sequences and translation initiation regions for off-target matches with user-specified mismatches; retain matches with at least seven consecutive bases.
- Synthesize KFFKFFKFFK-conjugated 10-mer PNAs targeting the *Salmonella* acpP start region, including nine serial double-mismatch variants with 40% GC content.
- Measure 24-hour growth inhibition by broth microdilution over 0.3–10 µM and define MIC as the lowest concentration with OD600 <0.1.
- Expose *Salmonella* to 5 µM PNA for 15 min, isolate total RNA, deplete rRNA, sequence 1 × 75-bp single-end libraries on an Illumina NextSeq 500, and quantify differential expression with edgeR.
- Compare predicted off-targets with depleted transcripts, analyze mismatch position and consecutive-match length, and repeat the analysis on the published UPEC dataset.

## Key Biology Insights
- Short PNAs are not reliably specific solely because they contain one or two mismatches to an off-target.
- Mismatch position matters: terminal mismatches preserve activity more often than central mismatches, presumably because they leave a longer contiguous pairing segment.
- Off-target binding near translation initiation regions can reduce non-target mRNA levels and can affect neighboring genes in operons.
- KFF-conjugated PNAs also induce a broad envelope-stress response, so transcriptomic effects include both sequence-dependent depletion and treatment-associated stress responses.
- The results suggest that shorter ASOs may remain feasible, but their specificity and uptake must be evaluated experimentally rather than inferred from mismatch counts alone.

## Implications
MASON provides a practical pre-experimental filter for bacterial ASO/PNA design and is likely applicable to related antisense chemistries such as PMOs. Researchers should inspect terminal mismatches, contiguous complementarity, predicted melting temperature, and translation-initiation-region matches across the target organism and relevant microbiomes. The tool is available at https://www.helmholtz-hiri.de/en/datasets/mason, with code under the MIT license at https://github.com/BarquistLab/mason and https://github.com/BarquistLab/mason_commandline.
