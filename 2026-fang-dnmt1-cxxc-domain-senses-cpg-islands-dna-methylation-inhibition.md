# Paper Summary

### Authors
Jian Fang, Bo Pan, Wendan Ren, Jiuwei Lu, Ting Zhao, Yiran Guo, Ling Cai, Yinsheng Wang, Gang Greg Wang, and Jikui Song. Fang, Pan, and Ren contributed equally.

### Journal
Nature Communications

### Publication Date
2026-09-18 (online publication; the accessible page labels this an early accepted-research version subject to replacement by the Version of Record)

### DOI
[10.1038/s41467-026-77872-8](https://doi.org/10.1038/s41467-026-77872-8)

## Keywords
DNMT1; CXXC domain; CpG islands; DNA methylation; nucleosomes; cryo-EM; whole-genome bisulfite sequencing; mouse embryonic stem cells.

## Main Idea
The DNMT1 CXXC domain preserves CpG-island hypomethylation by sensing unmodified CpG sites on nucleosomes. The interaction strengthens DNMT1 association with CpG-rich chromatin while placing CXXC in front of the target-recognition domain (TRD), restricting access to DNA substrates. This couples DNMT1 localization with catalytic restraint.

## Evidence Supporting the Main Idea
- Cryo-EM structures show DNMT1³351–1600 bound to an H3K18/K23-di-monoubiquitinated, H4K20me3 nucleosome containing unmodified CpGs. The WT complex was resolved at 3.12 Å overall resolution and 3.02 Å locally for the CXXC–nucleosome component.
- The CXXC domain recognizes an unmodified CpG at SHL −0.5 through K683 and Q684, while the domain sits in front of the TRD. The TRD, methyltransferase core, BAH domains, and toggle switch make additional nucleosome contacts.
- K683A/Q684A (MutKQ) weakens binding: the dissociation constant rises from 140 to 330 nM for unmodified nucleosomes and from 1.3 to 2.3 nM for H3Ub2-modified nucleosomes.
- MutKQ increases methylation of unmethylated linker CpGs and increases maintenance methylation of hemi-CpGs near unmodified CpGs in cis and trans. For a trans configuration, WT kcat is 2.6-fold lower than MutKQ; for a cis substrate, MutKQ changes kcat from 3.1 to 5.1 h−1 and Km from 36.1 to 53.6 nM.
- In cells, stringent WGBS calling found 96.6% of differential methylated CpG sites to be hypermethylated in MutKQ versus WT; about 27% of hyper-DMCs were in CpG islands or adjacent regions. Average methylation differences were modest genome-wide (3.33% at CGI shores and 2.94% at CGIs) but concentrated at high-CpG-density regions.
- MutKQ-associated hyper-DMRs were enriched at CGIs, promoters, and 5'-UTRs and at developmental gene sets. RNA-seq, embryoid-body assays, and retinoic-acid neuronal differentiation showed disrupted lineage programs and smaller embryoid bodies.

## Main Novelty
The work assigns the DNMT1 CXXC domain an active protective role: it is not only a chromatin-targeting module but also a structural brake that prevents DNMT1 from methylating hypomethylated CpG-island chromatin. The study connects nucleosome recognition, catalytic restraint, genome-wide methylation patterns, and developmental consequences.

## Datasets Used for Evaluation
- **Cryo-EM structures:** WT DNMT1³351–1600–unmodified nucleosome core particle and hyperactive MutMHKKKQ DNMT1³351–1600–unmodified nucleosome complexes. Coordinates: PDB 9Z07 and 9MYS. Maps: EMDB EMD-73698, EMD-73713, EMD-73701–EMD-73708, EMD-48749, and EMD-77709–EMD-77711.
- **In-vitro biochemical assays:** purified DNMT1³351–1600 WT or MutKQ, DNA/nucleosome binding, BLI, EMSA, and methylation kinetics on nucleosomes containing unmodified, hemi-methylated, or CpA-substituted sites. Figure 2 kinetic measurements used n=3 biological replicates where stated.
- **Mouse embryonic stem cells:** Dnmt1-knockout (1KO-mESC) parental cells, three independent WT-DNMT1 rescue clones, and three independent MutKQ rescue clones. Each rescue group was measured in three technical replicates for global 5mC (n=9 measurements/group); the parental knockout had n=3 technical replicates for that assay.
- **CUT&Tag:** DNMT1 and H3K27me3 binding profiles in rescued mESCs, with 0.5 million cells per sample and 5% human spike-in cells. Selected genomic-locus tracks report n=2 replicated samples. GEO: GSE287117.
- **WGBS:** genomic methylation in the rescue groups; approximately 400 million paired-end reads per sample, mean 17-fold genome coverage, and 99.5%–99.8% bisulfite conversion. GEO: GSE287140.
- **RNA-seq:** WT, MutKQ, and parental 1KO mESCs across embryoid-body differentiation at days 0, 3, and 5; biological replicates n=3 per time point/genotype. GEO: GSE338522.
- **Differentiation phenotypes:** embryoid-body formation after LIF/feeder withdrawal and retinoic-acid-induced neuronal differentiation. RT–qPCR results represent three independent experiments; embryoid-body counts are reported in Fig. 6.

## Experimental Procedure
- Reconstitute H3Ub2/H4K20me3-modified nucleosome particles with unmodified CpGs and solve WT and MutMHKKKQ DNMT1 complexes by cryo-EM; compare them with apo-DNMT1 and prior DNMT1–DNA structures.
- Use K683A/Q684A (MutKQ), EMSA, BLI, and methylation kinetics to test CXXC-dependent nucleosome binding and catalytic inhibition on cis and trans CpG configurations.
- Reconstitute 1KO-mESCs with 3×Flag-tagged WT or MutKQ DNMT1, establish independent clones, and measure global 5mC by LC–MS/MS.
- Profile DNMT1/H3K27me3 occupancy by spike-in-normalized CUT&Tag and methylation by WGBS; call DMCs/DMRs and annotate CGIs, shores, promoters, and developmental genes.
- Perform RNA-seq through embryoid-body formation, pathway/GSEA analyses, embryoid-body size assays, lineage-marker RT–qPCR, and retinoic-acid neuronal differentiation assays.

## Key Biology Insights
- DNMT1 maintenance methylation is restrained in CpG islands through direct recognition of their unmodified CpGs.
- The CXXC domain couples localization and inhibition: the same interaction that supports enrichment at CpG-rich regions limits access to potential DNA substrates.
- Loss of this restraint preferentially disrupts CpG-island methylation homeostasis rather than uniformly increasing methylation across the genome.
- MutKQ reduces DNMT1 binding at the highest-CpG-density regions while leaving broad targeting patterns and global 5mC comparatively similar.
- CpG-island hypermethylation is associated with altered developmental gene regulation, reduced H3K27me3 at CGIs, and impaired embryonic-stem-cell lineage specification.

## Implications
The findings provide a structural and cellular mechanism for how DNMT1 maintains methylation patterns while protecting active CpG islands from inappropriate methylation. Defects in DNMT1–CXXC–CpG recognition can produce localized epigenetic dysregulation at developmental regulatory elements without a large shift in global 5mC, identifying this interface as a useful point for studying aberrant DNA methylation.

## Data Availability
The paper reports source data with the article, GEO accessions GSE338522 (RNA-seq), GSE287117 (CUT&Tag), and GSE287140 (WGBS), PDB entries 9Z07 and 9MYS, and EMDB map accessions listed above. Supplementary Data 1–7 and source data are available from the article page.

Source: https://www.nature.com/articles/s41467-026-77872-8 (open-access full text and PDF accessed 2026-09-21)
