# Paper Summary

### Authors

Masahiro Hiraizumi, Januka S. Athukoralage, Nicholas T. Perry, Eisuke Tsujimoto, Nami Shiojiri, Naoto Nagahata, Lauren Lee, Gwanggyu Sun, Matthew G. Durrant, Sita S. Chandrasekaran, Silvana Konermann, Keitaro Yamashita, Patrick D. Hsu, and Hiroshi Nishimasu. Hiraizumi, Athukoralage, Perry, and Tsujimoto contributed equally.

### Journal

Nature

### Publication Date

2026-08-12 (version of record; received 2025-11-05, accepted 2026-07-10)

### DOI

[10.1038/s41586-026-10903-y](https://doi.org/10.1038/s41586-026-10903-y)

## Keywords

IS110 transposons; IS621; bridge RNA (bRNA); bridge recombinase; programmable recombination; excision; insertion; top-strand exchange; handshake guides; cryo-electron microscopy; genome editing.

## Main Idea

The study explains why IS621, an IS110-family bridge recombinase, naturally favors insertion over excision. Excision and insertion use the same overall catalytic logic—bRNA guide segments recognize DNA, composite RuvC–Tnp active sites cleave the top strands at conserved CT cores, and the cleaved strands exchange—but the DNA substrates assemble differently.

During insertion, donor and target DNA adopt bent U-shaped conformations. During excision, the two junction substrates (LH = LT–RD and RH = LD–RT) bind across both bRNA loops as extended, X-shaped DNA. This geometry, together with alternative/non-productive complex assembly routes and the native handshake-guide (HSG) sequence configuration, makes top-strand exchange much less favorable. Low bRNA expression from linear genomic elements further suppresses excision.

## Evidence Supporting the Main Idea

- **Native expression and excision:** RNA-seq detected low-level transcription through the linear IS621 element in *E. coli* and transcripts extending into the bRNA region. In *E. coli* Mach1, which contains three IS621 copies, transcription was detected from all three loci.
- **Cellular excision:** PCR detected both the circular RE–LE intermediate and post-excision LT–RT junctions from native Mach1 loci. A strain lacking IS621, *E. coli* BL21(DE3), was negative. Transcription through the element was required: an upstream terminator or deletion of the bRNA region eliminated detectable products.
- **Large efficiency asymmetry:** With purified recombinase, a 177-nt bRNA and defined DNA substrates, excision was approximately 0.03% while insertion was approximately 63% under the reported assay conditions—about a 2,000-fold difference.
- **bRNA sequence is a major bottleneck:** Every bRNA modification that improved insertion reduced excision. Conversely, an engineered bRNA with post-TSE HSGs, RTG/RDG extensions and an LTG G53A substitution increased excision approximately 13,000-fold over wild-type bRNA in the no-T7-promoter condition; adding a T7 promoter did not further improve the engineered construct.
- **Top-strand exchange, not initial cleavage, limits excision:** Fluorescent-substrate assays showed similar accumulation of top-strand-cleaved intermediates in excision and insertion, but far less final excision product.
- **Structures:** The pre-TSE excision complex was resolved at 2.53 Å and the post-TSE complex at 2.55 Å. Both contain four recombinase molecules, the TBL and DBL modules of bRNA, and LH/RH DNA. The pre-TSE structure shows ordered catalytic S241 loops for top-strand cleavage and disordered loops for the subsequent bottom-strand cleavage.
- **DNA geometry and recognition:** In excision, each TBL- or DBL-bound dimer can bind both LH and RH, whereas insertion dimers preferentially bind tDNA or dDNA, respectively. MST measurements supported this different assembly behavior.
- **HSG pairing:** Wild-type HSGs form fewer RNA–DNA base pairs before top-strand exchange and more after exchange, favoring insertion while disfavoring excision. Engineered pre-TSE/post-TSE HSG configurations reversed this preference as predicted.

## Main Novelty

This paper provides the missing structural mechanism for the excision half of the IS110 transposition cycle. It links three levels of explanation—bRNA expression, productive complex assembly and substrate geometry, and HSG-controlled strand exchange—to the insertion/excision asymmetry. It also identifies concrete bRNA engineering principles for favoring either reaction direction.

## Datasets Used for Evaluation

- **Native *E. coli* Mach1-T1R:** A strain containing three highly homologous IS621 loci. Whole-transcriptome RNA-seq measured locus-associated transcription; PCR tested circular intermediates and post-excision junctions. Whole-genome nanopore sequencing at 100× coverage confirmed three IS621 copies.
- **Plasmid-borne IS621 in *E. coli* BL21(DE3):** BL21(DE3) lacks endogenous IS621. Constructs represented the RE–LE circular configuration, the linear LE–recombinase–RE configuration, wild-type or engineered bRNA, bRNA deletion, and an upstream transcriptional terminator. RNA-seq and PCR/qPCR tested expression and excision.
- **In-vitro DNA substrates:** For qPCR assays, excision used 51-bp LH and 121-bp RH substrates; insertion used 86-bp tDNA and 86-bp dDNA. Reactions used purified IS621 recombinase and 177-nt bRNAs, including guide and HSG variants.
- **Fluorescent DNA substrates:** Shorter substrates (38-bp LH/tDNA and 44-bp RH/dDNA) included Cy5-labelled top strands and either wild-type or four-nucleotide top-strand mismatches. Denaturing gels tracked cleavage intermediates and products.
- **Cryo-EM complexes:** Pre- and post-TSE complexes used engineered 177-nt bRNA scaffolds and LH/RH substrates with four-nucleotide top-strand mismatches to promote structural capture.
- **MST binding panel:** TBL- and DBL-bound recombinase dimers were tested against LH, RH, tDNA and dDNA to compare substrate affinities and assembly preferences.

Public data:

- Cryo-EM maps: EMDB **EMD-65978** (pre-TSE) and **EMD-65979** (post-TSE).
- Atomic coordinates: PDB **9WHX** (pre-TSE) and **9WHY** (post-TSE).
- Raw cryo-EM images: EMPIAR **EMPIAR-13446**.
- RNA-seq and reference assembly: NCBI BioProject **PRJNA1455502**; GEO **GSE328474**; Mach1-T1R assembly GenBank **JCAHTY000000000**.

## Experimental Procedure

- Transform BL21(DE3) with plasmids encoding circular-like or linear IS621 arrangements; grow on kanamycin agar and extract RNA or plasmid DNA.
- Perform paired-end RNA-seq on plasmid constructs and *E. coli* Mach1-T1R. Align reads with BWA-MEM, filter/quantify coverage with SAMtools and pysam, and separate uniquely mapped from nonspecific reads at the three homologous Mach1 loci.
- Use PCR to detect the RE–LE circular intermediate and LT–RT post-excision junction. Sequence PCR products by Sanger sequencing.
- Reconstitute purified IS621 recombinase with synthetic bRNAs and annealed LH/RH or tDNA/dDNA substrates. Incubate at 37 °C for 2 h in Tris/NaCl/MgCl2/DTT buffer, then quantify products by qPCR against standards containing the expected unligated bottom-strand structure.
- Compare wild-type, split, extended, RTG/RDG-engineered, and HSG-variant bRNAs; test wild-type versus engineered bRNA in cells with or without a T7 promoter and quantify population-level excision by multiplexed TaqMan qPCR.
- Run Cy5-labelled substrates for 1 h and resolve products/intermediates on 18% TBE–urea gels.
- Purify pre-TSE and post-TSE excision complexes by size-exclusion chromatography and collect cryo-EM data on a Titan Krios G3i/K3 detector. Process movies in cryoSPARC, build/refine models in COOT/Servalcat, validate with MolProbity, and report maps at 2.53 Å and 2.55 Å.
- Measure DNA binding of TBL- and DBL-bound dimers by microscale thermophoresis using labelled recombinase and 0.3 nM–10 µM DNA ligand titrations.

## Key Biology Insights

- IS621 excision occurs under native bacterial conditions, but it is normally rare because linear elements produce little bRNA and because the native bRNA/DNA sequence configuration disfavors the strand-exchange step.
- The IS621 transposition cycle has a self-reinforcing direction: rare excision creates the RE–LE junction promoter, which boosts recombinase and bRNA expression from the circular intermediate; the resulting system preferentially supports insertion at a new target.
- Excision and insertion share CT-core cleavage and top-strand exchange, but their DNA architectures are distinct: X-shaped/linear for excision versus U-shaped/bent for insertion.
- The excision complex can assemble through multiple substrate-binding combinations, including non-productive ones. This is an additional kinetic penalty beyond the unfavorable DNA geometry.
- DBL alone was sufficient to support both excision and insertion in the tested assay, indicating that substrate recognition and productive tetramer formation can be achieved without an intact TBL in that context.
- HSG dinucleotides are a general directionality switch. The relevant base-pairing pattern determines whether top-strand exchange is favored before or after exchange, and the native IS110 pattern is conserved.

## Implications

The results provide a design framework for programmable bridge editing: choose HSGs and guide extensions according to whether insertion or excision is desired, and consider substrate geometry and bRNA expression separately. The findings help explain why insertion-oriented bRNA designs can support persistent genome modification while suppressing reverse excision.

The paper does not establish that every IS110 element has identical kinetics or that the engineered excision designs are efficient in mammalian cells. Cellular genome-editing performance, off-target behavior and generalization across IS110 orthologues require separate experiments.

Source: [Nature article](https://www.nature.com/articles/s41586-026-10903-y) (open access, CC BY 4.0).
