# Paper Summary

### Authors
Casey N. Grun, Ruchi Jain, Maren Schniederberend, Charles B. Shoemaker, Bryce Nelson, and Barbara I. Kazmierczak.

### Journal
Nature Communications, 15, 7502.

### Publication Date
29 August 2024.

### DOI
[10.1038/s41467-024-51912-7](https://doi.org/10.1038/s41467-024-51912-7)

## Keywords
Pseudomonas aeruginosa; bacterial surfaceome; phage display; Phage-seq; nanobodies; VHH; antimicrobial resistance; virulence factors; high-throughput sequencing.

## Main Idea
The authors introduce **Phage-seq**, which combines camelid VHH phage-display panning against live bacterial cells with high-throughput sequencing of VHH CDR regions. By comparing antigen-positive selection cells with matched counter-selection mutants, the method profiles native bacterial surface features without requiring the antigens to be known in advance, while also generating single-domain antibodies for follow-up experiments.

## Evidence Supporting the Main Idea
- An alpaca-derived library contained approximately 80,000 clones. Conventional panning against purified flagellin and Type IV pilus (T4P) produced antigen-binding clones, but many recognized fixed rather than live cells, motivating native-cell selection (Fig. 1).
- In live-cell panning, CDR3-clonotype richness and evenness generally declined over rounds, with more gradual convergence than in purified-protein panning. Extended selection with more cells, stricter washing/counter-selection, or a 100-fold lower phage input produced stronger population shifts (Fig. 2; Fig. 3f–g).
- The high-throughput campaign tested approximately 180 pairs of *P. aeruginosa* genotypes in 96-well format. PCA, canonical correspondence analysis, and enrichment profiles separated or associated selections according to growth conditions and expected biological features, including flagella, pili, exopolysaccharides, efflux pumps, and secretion systems (Fig. 6a–c).
- Of 83 selected VHHs targeting five antigens, 55 were expressed and 28 showed the predicted specificity by flow cytometry. The validated reagents recognized the flagellar hook-basal body, FliC, and the RND-efflux-associated porins OprM, OprJ, and OprN; several stained multidrug-resistant clinical isolates (Figs. 4–5).
- Classifiers distinguishing antigen-positive from antigen-negative selections achieved mean AUROCs of 0.70–0.86, whereas shuffled-label controls had AUROCs no higher than 0.52 (Fig. 6d–g).

## Main Novelty
This is a genotype-linked, multiplexed approach to bacterial surface characterization that does not depend on prior antigen purification or identification. The same experiment yields a high-dimensional VHH abundance/enrichment dataset and candidate nanobodies against native structures on intact cells.

## Datasets Used for Evaluation
- **Alpaca VHH phage-display library:** approximately 80,000 clones; generated from one adult male alpaca immunized with mixed soluble, membrane, and biofilm-derived *P. aeruginosa* antigens. Used as the input repertoire for all panning experiments.
- **Purified-antigen panning dataset:** purified flagellin and T4P, with matched mock preparations from antigen-deletion mutants; four rounds of solid-phase selection and clonal ELISA/flow-cytometry validation. Used to compare purified-protein and native-cell selection.
- **Small-scale live-cell panning dataset:** isogenic antigen-positive/antigen-negative *P. aeruginosa* pairs, including flagellar and T4P mutants; four rounds of cell-based selection, with approximately 2,500 to more than 40,000 VHH clones detected per sample and approximately 100–2,500 CDR3 clonotypes per sample. Used to characterize selection dynamics.
- **High-throughput Phage-seq dataset:** approximately 180 pairs of *P. aeruginosa* genotypes, mostly isogenic pairs differing in one antigen or structure, assayed in 96-well format. Four selection rounds were sequenced; a subset of 11 selections was extended for three additional rounds in triplicate. Used for surface-feature mapping and VHH discovery.
- **Recombinant-VHH validation set:** 83 VHHs selected against five targets (FliC, the flagellar hook-basal body, OprM, OprN, and OprJ); 55 expressed and 28 validated by flow cytometry. Used to test predicted specificity on antigen-positive and antigen-negative cells.
- **Clinical-isolate panel:** *P. aeruginosa* clinical isolates with multidrug-resistant phenotypes, used for exploratory flow-cytometry testing of selected anti-efflux VHHs. The paper does not specify a single total panel size in the main text.
- **Sequencing and assay repositories:** raw sequencing reads, NCBI SRA BioProject [PRJNA1073972](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1073972); processed sequencing data, [Zenodo 11246657](https://doi.org/10.5281/zenodo.11246657); raw and processed flow-cytometry data, [Zenodo 12826667](https://doi.org/10.5281/zenodo.12826667).

## Experimental Procedure
- Immunize an alpaca with mixed *P. aeruginosa* antigen preparations and construct an approximately 80,000-clone VHH phage-display library.
- Perform control panning against purified flagellin and T4P, and compare binding to purified antigens, fixed cells, and live cells.
- For native-cell selection, expose the library first to counter-selection cells lacking the target feature, then to antigen-positive selection cells; elute bound phage and amplify in *E. coli*.
- Repeat panning for four rounds, with extended campaigns adding higher cell-to-phage ratios, more counter-selection, and more stringent washing.
- Sequence VHH CDR1–3 amplicons on Illumina platforms; denoise with DADA2, map reads to VHH amino-acid sequences, group CDR3 clonotypes, calculate relative abundance/enrichment, and analyze diversity and ordination.
- Select candidate clonotypes using enrichment across antigen-positive versus antigen-negative samples; synthesize consensus VHHs as human IgG1-Fc fusions.
- Test recombinant VHH binding by ELISA and flow cytometry on engineered strains, clinical isolates, and appropriate negative controls.
- Train per-antigen classifiers with repeated five-fold cross-validation and compare their AUROCs with shuffled-label controls.

## Key Biology Insights
- Native bacterial surface antigens can select antibodies that are missed or misrepresented by purified, surface-immobilized antigen panning.
- Phage populations retain information about bacterial growth state and surface architecture even when selections remain relatively diverse and do not converge on a few dominant clones.
- The method recovered VHHs against multiple virulence- and resistance-associated structures: flagella, the flagellar hook-basal body, T4P-related features, and RND efflux porins.
- Distinct VHHs can discriminate related flagellar structures or recognize multiple related efflux porins, suggesting sensitivity to native complex composition and conformation.
- Anti-OprM, anti-OprJ, and anti-OprN VHHs may support rapid detection or targeting of multidrug-resistant *P. aeruginosa*, although therapeutic utility was not demonstrated in this study.

## Implications
Phage-seq offers a scalable route to compare bacterial surface phenotypes across mutants, clinical isolates, growth states, and longitudinal adaptation during infection. Its main near-term value is simultaneous discovery of surface-binding reagents and hypotheses about genotype-to-surface relationships. The approach remains indirect: VHH enrichment does not by itself identify the binding antigen, selections can be biased by phage amplification and antigen abundance, and most high-throughput selections were not replicated. Larger reference datasets and improved modeling could enable de novo surface-feature assignment and multiplexed profiling of unknown isolates.

### Source
Grun et al., “Bacterial cell surface characterization by phage display coupled to high-throughput sequencing,” *Nature Communications* (2024).

