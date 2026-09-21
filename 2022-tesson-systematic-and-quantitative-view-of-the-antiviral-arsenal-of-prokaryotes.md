# Paper Summary

### Authors
Florian Tesson, Alexandre Hervé, Ernest Mordret, Marie Touchon, Camille d’Humières, Jean Cury, and Aude Bernheim

### Journal
Nature Communications, 13:2561

### Publication Date
2022-05-10

### DOI
[10.1038/s41467-022-30269-9](https://doi.org/10.1038/s41467-022-30269-9)

## Keywords
Prokaryotes; bacteria; archaea; bacteriophages; antiviral defense; DefenseFinder; comparative genomics; prophages; CRISPR-Cas; restriction-modification

## Main Idea
The authors introduce DefenseFinder, a MacSyFinder-based tool that detects known antiviral defense systems from prokaryotic protein or nucleotide sequences. They use it to produce a genome-scale census of antiviral defenses and show that the composition and diversity of these defenses vary strongly across genomes, species, and phyla. Genome size, prophage burden, genomic location, and lifestyle-associated phylogeny are associated with this variation.

## Evidence Supporting the Main Idea
- DefenseFinder models 60 antiviral-system families and 151 system/subsystem types using 845 HMM profiles plus system-specific genetic-organization rules (Fig. 1; Supplementary Data 1–2).
- In 21,738 complete prokaryotic genomes, the tool detected 113,955 systems involving 301,372 genes. Genomes contained an average of 5.2 systems and 3 distinct system families; counts ranged from zero to 57 (Fig. 2; Supplementary Data 5–7).
- Restriction-modification (RM) systems were present in 83% of genomes and CRISPR-Cas in 39%. The next most common systems occurred in only about 10–17% of genomes, while 21 of the 60 families occurred in fewer than 1% of genomes (Fig. 3a).
- System counts correlated positively with genome size (Spearman rho = 0.25 for total systems; rho = 0.44 for system families) and prophage count (rho = 0.16 and 0.27, respectively; Fig. 2b–c). These associations remained significant after accounting for genome size.
- Prophage-encoded systems were shorter than chromosomal systems (median 2,569 bp versus 3,596 bp; Wilcoxon P < 0.0001), and several systems were enriched in prophages, whereas large systems such as Dnd, BREX, and DISARM were rarely prophage-encoded (Fig. 3c–d).
- Defense arsenals were species-specific. The 558 Bordetella pertussis genomes had no detected anti-phage system, whereas Helicobacter pylori strains averaged 18 systems. In Pseudomonas aeruginosa, closely related strains could carry markedly different arsenals, consistent with frequent horizontal transfer (Fig. 4).
- Model validation against existing datasets gave reported sensitivities of 97.4–99.4% and specificities of 96.7–99.97% for evaluated systems. RM detection had 91.9% sensitivity on REBASE; the authors accepted under-detection of some distant RM type IV sequences to preserve specificity (Supplementary Fig. 3; Supplementary Data 3).

## Main Novelty
This study combines a reusable, updateable detector for complete antiviral systems with a broad comparative analysis across bacteria and archaea. It extends previous system-by-system surveys into a quantitative, genome-centric view of antiviral-defense diversity at multiple phylogenetic scales.

## Datasets Used for Evaluation
- **NCBI RefSeq complete-genome dataset:** 21,738 genomes downloaded in May 2021, comprising 21,364 bacterial and 374 archaeal genomes from 4,374 and 260 species, respectively. This was the principal dataset for detecting and comparing antiviral systems (Supplementary Data 4–7).
- **Prophage predictions:** 51,582 putative prophages in 16,315 of the RefSeq genomes, identified with VirSorter2 and filtered for high-confidence predictions. These were used to test associations between prophage burden, system abundance, and genomic location (Supplementary Data 10).
- **Published system-detection datasets:** Datasets from Doron et al., CBASS, and DISARM studies were used to evaluate DefenseFinder sensitivity and specificity; CasFinder v2 was used for CRISPR-Cas comparison, and REBASE was used for RM evaluation (Supplementary Figs. 1–4; Supplementary Data 3).
- **Species-level subset:** Species represented by more than 100 genomes were used for arsenal comparisons; 15 bacterial species were analyzed with core-genome phylogenies, including *Escherichia coli*, *Pseudomonas aeruginosa*, *Streptococcus pyogenes*, *Salmonella enterica*, *Listeria monocytogenes*, *Helicobacter pylori*, *Mycobacterium tuberculosis*, and *Neisseria meningitidis* (Fig. 4; Supplementary Figs. 8–10).

## Experimental Procedure
- Survey the literature for prokaryotic antiviral systems with experimental evidence available before November 2021; exclude families whose antiviral role was unresolved and host factors or superinfection-exclusion mechanisms.
- Build HMM profiles from PFAM/COG resources or curated protein sequences, align sequences with MAFFT, generate profiles with HMMER, and set manually curated gathering thresholds.
- Encode the expected genetic architecture of each system as MacSyFinder rules containing mandatory, accessory, and interchangeable protein components.
- Validate the models against published detections, CasFinder, and REBASE; refine thresholds and rules to balance sensitivity and specificity.
- Run DefenseFinder v1.0.2 with models v1.0 on the RefSeq complete-genome collection and record detected systems, subtypes, proteins, genome locations, and phylogenetic metadata.
- Detect high-confidence prophages with VirSorter2, compare prophage and chromosomal systems, and test associations with genome size and prophage number using Spearman correlations and regression.
- Build species core-genome phylogenies with PanACoTA/IQ-TREE for 15 species, map defense-system presence/absence, and compare arsenals using system frequencies and Bray–Curtis distances.

## Key Biology Insights
- Prokaryotic antiviral defense is generally modular and redundant: most genomes with defenses carry multiple systems, often from multiple families, but a small number of families—especially RM and CRISPR-Cas—account for much of the observed prevalence.
- Nucleic-acid degradation is the most common broad mechanism among detected systems; many systems still have unknown molecular mechanisms.
- Defense-system diversity is not evenly distributed. Intracellular or endosymbiotic lineages such as Chlamydiae have very few detected systems, while some phyla show enrichment of particular systems, such as BREX in Fusobacteria and Wadjet in Actinobacteria.
- Prophage-associated defenses appear subject to different size and evolutionary constraints from chromosomal defenses, with some systems preferentially associated with prophages.
- Species-level arsenals can be stable in total size but differ in composition, or vary widely among closely related strains. This supports a role for horizontal gene transfer and lineage-specific ecological or viral pressures.

## Implications
DefenseFinder provides a practical framework for screening large genome collections and can support studies of phage–host interactions, defense-island evolution, and phage therapy. The results suggest that antiviral diversity—not simply the number of systems—may reflect viral exposure and lifestyle. The census should be interpreted as a lower bound: it is based on known systems, favors cultivated and overrepresented taxa in RefSeq (Proteobacteria comprise 57% of the dataset), and uses conservative full-system detection. Unknown systems, divergent homologs, false prophage assignments, and species exposed to virulent but not prophage-forming viruses may therefore be missed or underrepresented.

