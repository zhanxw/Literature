# Paper Summary

### Authors

Lejla Daruka, Márton Simon Czikkely, Petra Szili, Zoltán Farkas, Dávid Balogh, Gábor Grézal, Elvin Maharramov, Thu-Hien Vu, Levente Sipos, Szilvia Juhász, Anett Dunai, Andreea Daraba, Mónika Számel, Tóbiás Sári, Tamás Stirling, Bálint Márk Vásárhelyi, Eszter Ari, Chryso Christodoulou, Máté Manczinger, Márton Zsolt Enyedi, Gábor Jaksa, Károly Kovács, Stineke van Houte, Elizabeth Pursey, Lajos Pintér, Lajos Haracska, Bálint Kintses, Balázs Papp, and Csaba Pál.

### Journal

Nature Microbiology, 10, 313–331.

### Publication Date

13 January 2025 (online); February 2025 issue.

### DOI

[10.1038/s41564-024-01891-8](https://doi.org/10.1038/s41564-024-01891-8)

## Keywords

Antimicrobial resistance; antibiotic evolution; ESKAPE pathogens; adaptive laboratory evolution; functional metagenomics; mobile resistance genes; cross-resistance.

## Main Idea

Antibiotics introduced after 2017 or still in development are generally no less vulnerable to resistance evolution than long-used antibiotics. Across *Escherichia coli*, *Klebsiella pneumoniae*, *Acinetobacter baumannii* and *Pseudomonas aeruginosa*, resistance emerged rapidly in vitro through overlapping chromosomal mechanisms and transferable resistance genes. Resistance risk nevertheless depended strongly on the specific antibiotic–strain combination, suggesting that candidate selection should evaluate resistance evolution across multiple pathogens and using complementary genomic and metagenomic assays.

## Evidence Supporting the Main Idea

- A susceptibility panel of 40 clinical strains was tested against 22 established control antibiotics and 13 recent or developmental antibiotics. Recent compounds such as cefiderocol, SPR-206, eravacycline and delafloxacin often had lower MICs than within-class controls, and recent and control drugs clustered by mode of action (Fig. 1).
- In frequency-of-resistance assays, mutants with at least a fourfold MIC increase appeared in 49.8% of populations. Recent and control antibiotics did not differ significantly in mutant appearance frequency (*P* = 0.9) or resistance fold change (*P* = 0.68).
- Adaptive laboratory evolution (ALE) for approximately 120 generations (60 days) produced a median approximately 64-fold MIC increase. MICs reached or exceeded peak plasma concentrations in 87% of populations and exceeded available clinical breakpoints in 88.3% of adapted lines (Fig. 2).
- Resistance gains varied by as much as 65,000-fold across antibiotic–strain combinations. Antibiotic identity and strain background explained 24.4% and 8.9% of variation separately; including their interaction increased explained variation from 32.6% to 58.6%.
- Whole-genome sequencing of 381 ALE lines and 135 frequency-of-resistance lines identified 1,817 unique mutational events in 506 non-mutator lines, including 1,212 SNPs and 605 indels. Of 604 mutated protein-coding genes, 69.4% of parallel-mutated genes were altered under more than one antibiotic treatment (Fig. 3).
- Laboratory-observed nonsynonymous mutations were already present in natural-isolate genomes: up to 31.4% of 245 *E. coli* mutations occurred in at least one of 20,786 genomes, and 27.3% of 216 *A. baumannii* mutations occurred in at least one of 15,185 genomes.
- Functional metagenomic screening recovered 690 independent resistance-conferring DNA fragments, producing resistance increases of up to 256-fold. The number and mobility of hits did not differ significantly between recent antibiotics and matched controls; no hit was found for tridecaptin M152-P3. Clinical microbiomes contributed 57.8% of fragments, compared with 25.5% from soil and 24.8% from gut libraries (Fig. 4).
- The 690 fragments contained 642 non-redundant ORFs; 77% resembled known ARGs, 20.7% had evidence of mobility, and 24.5% of the 642 ARGs met at least two potential-risk criteria. Potential-risk counts included 22 for cefiderocol, 26 for ceftobiprole and 16 for sulopenem.

## Main Novelty

The study integrates comparative susceptibility testing, short-term mutant-selection assays, long-term ALE, whole-genome sequencing, targeted deep mutagenesis and functional metagenomics across four priority Gram-negative pathogens. This exposes both pre-existing chromosomal variants and mobile resistance genes that would be missed by susceptibility testing or single-species mutation studies alone, and it combines these measurements into an antibiotic resistance landscape (Fig. 5).

## Datasets Used for Evaluation

- **Clinical pathogen panel:** 40 clinically relevant strains: *E. coli*, *K. pneumoniae*, *A. baumannii* and *P. aeruginosa*. Used for MIC profiling against 35 antibiotics; eight strains were selected for FoR and ALE (one susceptible and one MDR strain per species).
- **Laboratory-evolved lines:** 10 parallel ALE populations per antibiotic–ancestor combination, followed for up to approximately 120 generations; 381 ALE-derived and 135 FoR-derived resistant lines were used for genomic analysis. Cephalosporins were excluded from ALE because of instability in liquid medium.
- **Natural-isolate genome collections:** 20,786 *E. coli* genomes and 15,185 *A. baumannii* genomes. Used to measure the prevalence of laboratory-observed adaptive mutations in nature.
- **Functional metagenomic libraries:** libraries from anthropogenic soil and river sediment at seven antibiotic-polluted industrial sites, stool from 10 Europeans without antibiotic exposure for at least one year, and a pool of 68 MDR clinical bacterial isolates. Each library contained up to 5 million fragments, with approximately 25 Gb total coverage.
- **Global Microbial Gene Catalog (GMGCv1):** more than 13,000 metagenomes across 14 major habitats. Used to assess habitat distribution, human-association and potential mobility of resistance genes.
- **Deep-scanning mutagenesis:** targeted *gyrA* and *parC* QRDR libraries in *E. coli* K-12 MG1655 and *K. pneumoniae* ATCC 10031. Used to test cross-resistance among topoisomerase inhibitors.

## Experimental Procedure

- Measure MICs by broth microdilution for 40 strains against recent/developmental and established within-class antibiotics; cluster susceptibility profiles and compare paired MICs.
- Expose approximately 10^10 cells from eight selected ancestral strains to multiple antibiotic concentrations for 48 h, calculate spontaneous frequency of resistance, and characterize selected colonies by MIC testing and sequencing.
- Propagate 10 parallel populations per antibiotic–strain combination through escalating drug concentrations for about 20 transfers (approximately 120 generations), then compare evolved and ancestral MICs.
- Whole-genome sequence resistant lines, call SNPs and indels relative to ancestors, identify recurrent genes and compare mutations with natural-isolate genomes.
- Apply targeted deep-scanning mutagenesis to topoisomerase targets and measure cross-resistance to moxifloxacin, delafloxacin and gepotidacin.
- Express metagenomic DNA fragments in susceptible *E. coli* and *K. pneumoniae* hosts, select on 18 antibiotics, sequence resistance-conferring inserts, and annotate ARGs, mobility and host/pathogen associations.
- Combine seven resistance-related metrics—initial reduced susceptibility, ALE resistance tendency, mutation diversity, natural-mutation prevalence, mobile-contig diversity and potential-risk ARG prevalence—into an antibiotic resistance landscape.

## Key Biology Insights

- Resistance can arise within clinically relevant exposure windows even for dual-target, membrane-targeting or otherwise resistance-sparing candidates.
- Resistance evolution is highly dependent on genetic background and drug–strain pairing; a broad average ranking is therefore insufficient for clinical prediction.
- Efflux regulation and target alteration were common chromosomal routes, while antibiotic inactivation was more prominent among mobile metagenomic hits. Shared mobile contigs frequently involved the BaeR and RamA efflux-regulatory systems.
- Structural similarity predicted overlap in mobile resistance profiles (Spearman *R* = 0.43, *P* < 0.01), but uptake or target changes could create exceptions, as seen for cefiderocol and SPR-206.
- Several candidate-specific expectations were challenged: resistance to SCH-79797, delafloxacin, gepotidacin, omadacycline, cefiderocol, eravacycline and SPR-206 arose through efflux, target or regulatory mechanisms under the tested conditions.
- Among antibiotic classes, membrane-targeting candidates had lower predicted resistance susceptibility than tetracyclines and topoisomerase inhibitors, but no tested compound met all criteria for an ideal antibiotic.

## Implications

Antibiotic development should assess immediate activity and long-term evolutionary durability together. Before clinical use, candidates should be evaluated across multiple clinically relevant species and strains with mutant-selection assays, long-term evolution, genome sequencing and functional metagenomics. The results support prioritizing compounds with broad activity, low genomic and mobile-ARG risk, low prevalence of associated resistance mechanisms in human microbiomes and pathogens, and sufficiently distinct uptake or target biology. The authors note that fitness and virulence trade-offs were not systematically measured, so the in vitro resistance landscape should not be treated as a complete clinical forecast.
