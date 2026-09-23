# Paper Summary

### Authors
David B. Li, Garyk Brixi, Alexandra S. Kim, Mateus B. Fiamenghi, Claudia L. Driscoll, Simone A. Evans, Alex Gao, Natalia N. Ivanova, Nikos C. Kyrpides, Karl Deisseroth, Max E. Wilkinson, Michael A. Fischbach, and Brian L. Hie. Li and Brixi contributed equally; Fischbach and Hie are corresponding authors.

### Journal
Not specified in paper (manuscript/preprint).

### Publication Date
Not specified in paper. The supplied manuscript PDF is dated September 2026 in its file metadata; this is not treated as a publication date.

### DOI
Not specified in paper.

## Keywords
Minerva; genome language model; coevolutionary mining; non-coding RNA; RNA base pairing; repetitive DNA; CRISPR; reverse transcriptase; prophage; cDNA synthesis; bacterial genomes.

## Main Idea
The authors introduce Minerva, an alignment-free framework that converts genome-language-model representations into interpretable pairwise coevolutionary maps. Minerva uses attention-based interaction heads for fast genome-scale scanning and categorical Jacobian fingerprinting for more flexible locus-level analysis. It predicts conserved RNA base pairing, protein contacts, and repetitive sequence motifs directly from genomic sequence, enabling discovery of structured non-coding elements without requiring a protein query or a pre-existing multiple-sequence alignment.

## Evidence Supporting the Main Idea
- On three held-out benchmark classes—RNA base pairing, prokaryotic protein contacts, and repetitive genomic motifs—Minerva's interaction heads and Jacobian fingerprinting outperformed earlier straight-to-scalar categorical-Jacobian approaches by area under the precision-recall curve (AUPRC) (Fig. 1E; figs. S7–S11). Interaction heads were best on more than 84% of tested Rfam families.
- Interaction heads required about 79 ms per 8,192-token sequence, compared with more than 1.5 hours for an accelerated mask-based Jacobian implementation and 6 hours for the original implementation (Fig. 1F).
- A scan of 150 bacterial genomes completed in 100 minutes on one H100 GPU and identified 57,787 loci with at least two neighboring predicted hairpins; 40,175 (69.5%) were outside existing annotations. With a threshold of at least four hairpins, 9,044 loci were identified, 41.1% unannotated (Fig. 3).
- Minerva recovered known structured regions, including CRISPR arrays and rRNAs, and its aggregate signals were enriched near known nucleic-acid-associated proteins (Fig. 3B–D).
- In DRT2 antiphage systems, base-model predictions detected a hidden three-nucleotide periodicity corresponding to an unannotated ORF; family-specific fine-tuning on 13,034 loci recovered additional RNA structure, including a cryo-EM-supported pseudoknot (Fig. 2).
- In Pseudomonadota, Minerva-guided analysis extended the TwoAYGGAY RNA architecture and found 16,086 matches across 1,148 of 1,324 Pseudomonas strains. In Pseudomonas fluorescens SBW25, all 11 tandem group I/III REP arrays were downstream of a TwoAYGGAY match; 68.4% of nearby TwoAYGGAY doublets were divergently oriented, with both doublet formation and orientation enriched over empirical nulls (p < 10^-4).
- For five UG27 reverse-transcriptase systems, heterologous expression in *E. coli* produced RT-dependent 50–100-nt single-stranded DNA products mapping to central hairpins in the Minerva-guided ncRNA array. Mutation of the RT active-site YSDD motif to YSAA eliminated products, and deletion of either accessory ORF also abolished synthesis (Fig. 6).

## Main Novelty
Minerva treats model-derived pairwise interaction patterns—not only scalar scores—as discovery signals. This provides one framework for base pairing, protein contacts, and repeat interactions, combining rapid attention-head scanning with more expressive Jacobian fingerprints and optional family-specific fine-tuning. The study further shows that these maps can guide covariance-model construction and experimentally testable discoveries in highly sequence-diverse ncRNAs.

## Datasets Used for Evaluation
- **Genome-language-model pretraining:** the Open MetaGenomic (OMG) corpus and GlobDB release r226; the mixture sampled OMG at 25% and GlobDB at 75%. Minerva-MLM was continued-pretrained for 1.2 million steps at 4,096 tokens; Minerva-MLM-8k was trained for a further 620,000 steps at 8,192 tokens.
- **Protein contacts:** a curated prokaryotic subset of the trRosetta training set derived from Protein Data Bank structures. It contained 118 proteins (23 training, 95 evaluation), 200–1,024 amino acids long; long-range contacts were separated by at least 24 residues and defined using an 8 Å Cα distance threshold.
- **Conserved RNA base pairing:** Rfam-derived bacterial ncRNA families. After filtering and retrieval, 680 families had sufficient alignment depth; the common benchmark contained 673 families (27 training, 646 held-out evaluation), with up to 10 sequences sampled per family and at least four qualifying reference base pairs per evaluated sequence.
- **Repetitive genomic motifs:** 50 loci across five natural repeat classes, with 10 loci per class. Training used 20 CRISPR or type III toxin–antitoxin loci; the held-out set used 30 REP, SsnA-associated non-template-strand repeat, or TIGR-Tas loci.
- **Genome-scale discovery:** 150 bacterial genomes—116 human-gut bacteria from hCom2, 25 pathogens/select agents, and 9 laboratory model organisms—annotated with mettannotator.
- **System-specific fine-tuning and discovery:** 13,034 DRT2 loci, 2,549 deduplicated UG27 loci, and 6,884 TwoAYGGAY loci. The extended TwoAYGGAY model was then scanned across complete Pseudomonas genomes and broader prokaryotic genomes containing an original Rfam hit.
- **UG27 experimental validation:** five UG27 systems from the 150-genome scan, cloned and expressed in *E. coli* for denaturing PAGE, strand-specific sequencing, active-site mutagenesis, and accessory-ORF deletion tests.

## Experimental Procedure
- Continue-pretrain the 650-million-parameter mixed-modality gLM2 architecture on metagenomic and genome data, representing coding regions as amino acids and intergenic regions as nucleotides.
- Extract pairwise dependencies either by categorical Jacobian fingerprinting (in silico saturation mutagenesis) or by logistic-regression interaction heads over selected transformer attention heads.
- Train/evaluate the interaction heads and fingerprints on disjoint protein-contact, Rfam base-pairing, and repetitive-motif benchmarks using AUPRC.
- Tile 150 annotated bacterial genomes into overlapping windows, scan them with the fast interaction heads, and aggregate predicted base-pairing and repeat interactions by intergenic region.
- Fine-tune Minerva-MLM on DRT2, UG27, or TwoAYGGAY locus collections; compare base and fine-tuned maps and use predictions to construct/refine covariance models.
- Analyze the resulting TwoAYGGAY and UG27 architectures across genomes and metagenomic databases using covariance-model searches, repeat enrichment, phylogenetics, and predicted protein-complex structure.
- Clone five UG27 systems in *E. coli*, sequence products strand-specifically, mutate the RT active site, delete accessory ORFs, and predict product secondary structures with DNA parameters in ViennaRNA.

## Key Biology Insights
- Bacterial genomes contain many structured intergenic loci that are missed by current annotations; Minerva predicts hundreds of candidate multi-hairpin loci per genome.
- TwoAYGGAY RNAs have lineage-specific structural extensions in Pseudomonadota, including extra hairpins, elongated stems, pseudoknots, and associations with upstream short repeats and downstream REP arrays. Their copy-number variation and divergent doublets suggest a mobile-element-like expansion mechanism, although the connection to regulation remains unresolved.
- UG27 prophage systems encode variable, sequence-diverse ncRNA arrays whose units retain a common predicted structure. Each unit is approximately 135–167 nt in the major classes and contains a central hairpin.
- UG27 proteins reverse-transcribe the central hairpin of each ncRNA unit into short, diverse cDNA hairpins. All three system proteins and RT catalytic activity are required, but the biological function of the cDNA products remains unknown.
- Genome language models can learn signals beyond their explicitly supervised interaction classes: codon periodicity revealed hidden ORFs, while fine-tuning exposed additional family-specific RNA interactions.

## Implications
Minerva provides a scalable complement to homology- and alignment-based annotation, especially for ncRNAs whose structures are conserved but whose sequences are divergent. Its interaction maps can prioritize unannotated loci, support alignment and covariance-model construction, and generate hypotheses for experimental testing. Important limitations are the relatively short model context window, weaker protein-contact performance than specialized protein models, difficulty with RNA–protein interactions, and trade-offs introduced by fine-tuning: stronger RNA-structure signals can attenuate repeat- or ORF-associated signals. The UG27 cDNA function and the biological role of many genome-wide candidates remain open questions. Code is available at https://github.com/garykbrixi/minerva, with Minerva-MLM checkpoints on Hugging Face.
