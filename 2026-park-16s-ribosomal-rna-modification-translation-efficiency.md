# Paper Summary

### Authors

Zachory M. Park, Christina R. Savage, Amanda R. Decker-Farrell, Chin-Hsien Tai, Tapan K. Maity, Weiming Yang, Lisa M. Jenkins and Kumaran S. Ramamurthi.

### Journal

Cell Reports

### Publication Date

22 September 2026 (Volume 45, Issue 9; open access)

### DOI

[10.1016/j.celrep.2026.117887](https://doi.org/10.1016/j.celrep.2026.117887)

## Keywords

16S rRNA modification; MraW/RsmH; RsmI/YabC; ribosome heterogeneity; translation efficiency; structured mRNA; *Bacillus subtilis*; sporulation; SpoIVA; CmpA.

## Main Idea

MraW/RsmH-mediated methylation of 16S rRNA helps ribosomes translate difficult, structured transcripts. In *Bacillus subtilis*, the effect is especially important for mRNAs whose 5′ region forms a stem-loop over the ribosome-binding/start-codon region or early coding sequence. The authors show that loss of MraW lowers translation of the negative sporulation regulator CmpA, allowing cells with defective SpoIVA to bypass the coat-assembly checkpoint. They propose that rRNA modifications and transcript structures form a gene-specific system for tuning protein dosage.

## Evidence Supporting the Main Idea

- A SpoIVA-L59P variant had an approximately 1,000-fold sporulation defect and failed to hydrolyze ATP normally; spontaneous suppressors carried a truncating *mraW* mutation.
- Deleting *mraW* increased sporulation of the SpoIVA-L59P strain by approximately 10-fold, and complementation restored the defect. *mraW* deletion also partially suppressed other defective *spoIVA* alleles, while deletion of the predicted RsmI homolog *yabC* produced a weaker suppression.
- Purified Δ*mraW* ribosomes translated reporter RNAs at approximately half the efficiency of wild-type ribosomes. The defect was larger for *cmpA* RNA than for an optimized control transcript.
- Δ*mraW* reduced CmpA protein production but did not reduce *cmpA* transcription, and the effect persisted when *cmpA* was expressed from a constitutive promoter, supporting translational regulation.
- The *cmpA* 5′ untranslated region plus early coding sequence forms a conserved stem-loop involving the intervening sequence between the ribosome-binding site and start codon and the first six codons. Disrupting the stem relieved MraW dependence; stabilizing it reduced expression in both wild-type and Δ*mraW* cells.
- The proteomic screen identified MraW-sensitive proteins. Applying a two-fold-change threshold, detection in all strain backgrounds and reproducibility across three replicates with p < 0.05 identified Isp and YukJ for follow-up. Both have early structured RNA elements and showed MraW-dependent translation.
- For *isp*, changing the predicted stem altered translation as expected: disrupting the stem increased Δ*mraW* expression, whereas strengthening it strongly reduced expression. For *yukJ*, promoter-only fusions were not MraW dependent, indicating that the translational effect resides in the transcript sequence.

## Main Novelty

The study connects a conserved 16S rRNA modification to transcript-specific translation through RNA secondary structure and links this mechanism to a bacterial developmental checkpoint. It moves beyond a global ribosome-efficiency model: MraW improves translation generally, but structured, dosage-sensitive transcripts experience the largest effect.

## Datasets Used for Evaluation

- **Laboratory strains:** The study used *B. subtilis* PY79 and derivatives carrying *spoIVA*, *mraW*, *yabC*, *cmpA*, reporter and complementation alleles. All experiments used at least three independent biological replicates; exact n values are given in individual figure legends.
- **Sporulation and growth assays:** Heat-resistant colony counts after 24 h in Difco Sporulation Medium measured sporulation efficiency relative to wild-type PY79. Cultures were heated at 80°C for 20 min before plating.
- **Purified-ribosome translation assays:** Ribosomes were purified from exponentially growing or sporulating PY79 and Δ*mraW* cells and tested with optimized, *cmpA*, *cmpA*-stem-disrupted and reporter transcripts in cell-free transcription/translation reactions.
- **Reporter and transcript constructs:** *cmpA*, *isp* and *yukJ* promoter/5′-UTR/ORF fragments were fused to GFP or lacZ. Stem-disrupting, stem-strengthening and compensatory sequence substitutions tested whether RNA structure caused the MraW dependence.
- **Proteomics:** Wild-type and mutant *spoIVA* backgrounds with or without MraW were profiled during vegetative growth and sporulation by LC-MS/MS. The deposited mass-spectrometry dataset is available through ProteomeXchange/MassIVE as **PXD074358**; the article also provides Dataset S1.
- **Sequence and structure analyses:** *cmpA*, *isp* and *yukJ* sequences were compared across relevant orthologs, and RNA structures were predicted with mFold and ViennaRNA. The article reports that all other supporting data are in the paper and supplemental information; no original code was reported.

## Experimental Procedure

- Characterize SpoIVA-L59P by measuring sporulation, protein abundance, localization and ATP hydrolysis.
- Select spontaneous suppressors by repeated sporulation, heat treatment and regrowth; identify mutations by whole-genome sequencing.
- Delete, complement or catalytically alter *mraW*, and delete *yabC*, then test suppression across several defective *spoIVA* alleles.
- Purify ribosomes from PY79 and Δ*mraW* cells grown vegetatively or induced to sporulate; compare in vitro translation of optimized and structured reporter RNAs.
- Measure CmpA protein and *cmpA* transcript output using immunoblotting, reporter fusions and constitutive-expression constructs to distinguish translation from transcription.
- Truncate the *cmpA* ORF and mutate its intervening sequence, early codons and predicted stem to map the minimal MraW-sensitive element.
- Profile proteins by mass spectrometry, apply the stated two-fold/all-backgrounds/three-replicates criteria, and select Isp and YukJ for mechanistic validation.
- Test *isp* and *yukJ* promoter, 5′-UTR and coding-sequence fusions, including mutations that disrupt or stabilize predicted stem-loops.
- Analyze results with means/medians, standard deviations and figure-specific statistical tests; statistical significance was defined as p < 0.05.

## Key Biology Insights

- Loss of a conserved rRNA modification can produce a developmental phenotype by selectively reducing translation of a checkpoint regulator rather than by causing a general growth defect.
- The CmpA stem-loop normally limits translation enough to keep CmpA low but still permits checkpoint function. Without MraW-modified ribosomes, CmpA falls below the level needed to eliminate cells with defective coat assembly.
- MraW-dependent translation is transcript specific: the proteomic effect is relatively sparse despite a general reduction in translation efficiency.
- Structured regions can act within or immediately adjacent to the coding sequence, affecting initiation when the start region is occluded and potentially elongation when the structure forms after the start codon.
- The authors suggest that the mechanism may be favored in organisms such as *B. subtilis* with functionally uncoupled transcription and translation, because transcripts can fold before ribosome engagement.

## Implications

Ribosome modifications may be part of a broader bacterial strategy for maintaining precise levels of proteins involved in development, stress responses and other dosage-sensitive processes. The findings also suggest why MraW loss can have little effect in standard growth conditions but become important during sporulation or cold stress, when inhibitory RNA structures may be more stable. The proposed mechanism should be tested across additional species and transcript classes; the study establishes validated examples in *B. subtilis*, not a genome-wide prevalence estimate.

Source: [Park et al., Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(26)00965-4)
