# Paper Summary

**Paper:** A trimethoprim derivative impedes antibiotic resistance evolution  
**Source:** [Nature Communications](https://www.nature.com/articles/s41467-021-23191-z)  
**Article number:** 2949, volume 12

### Authors

Madhu Sudan Manna; Yusuf Talha Tamer; Ilona Gaszek; Nicole Poulides; Ayesha Ahmed; Xiaoyu Wang; Furkan C. R. Toprak; DaNae R. Woodard; Andrew Y. Koh; Noelle S. Williams; Dominika Borek; Ali Rana Atilgan; John D. Hulleman; Canan Atilgan; Uttam Tambar; Erdal Toprak

### Journal

Nature Communications

### Publication Date

May 19, 2021

### DOI

[10.1038/s41467-021-23191-z](https://doi.org/10.1038/s41467-021-23191-z)

## Keywords

- Antibiotic resistance evolution
- Trimethoprim (TMP)
- 4′-desmethyltrimethoprim (4′-DTMP)
- Dihydrofolate reductase (DHFR)
- *Escherichia coli*
- L28R mutation
- Mutant-selective inhibitor
- Morbidostat
- Experimental evolution
- Evolutionary steering
- Clonal interference
- Structure-guided drug design

## Main Idea

The study tests whether an antibiotic can be redesigned to suppress a common evolutionary route to resistance rather than merely inhibit the ancestral pathogen. Trimethoprim resistance in *E. coli* frequently depends on the DHFR mutation L28R, which weakens trimethoprim inhibition while improving affinity for the natural substrate dihydrofolate. Guided by crystal structures of wild-type and L28R DHFR, the authors identified 4′-desmethyltrimethoprim (4′-DTMP), a trimethoprim derivative that retains activity against wild-type cells but is substantially more active than trimethoprim against L28R cells.

In laboratory populations, 4′-DTMP selected against L28R-containing genotypes and redirected evolution toward alternative DHFR mutations with lower catalytic performance. Resistance still evolved and was cross-resistant with trimethoprim, but it accumulated more slowly and reached lower levels. The paper therefore demonstrates **evolutionary steering by targeting a high-value resistance mutation**, while also showing that this approach delays rather than prevents resistance.

## Evidence Supporting the Main Idea

### Direct experimental observations

- **L28R is a recurrent evolutionary route:** Across 40 independently evolved *E. coli* populations exposed to trimethoprim—seven from this study and 33 from earlier studies—L28R was among the most frequently observed coding mutations in `folA`, the gene encoding DHFR (Figure 1d).
- **Structural rationale:** X-ray structures of trimethoprim/NADPH-bound wild-type DHFR at 1.9 Å and L28R DHFR at 2.1 Å showed only subtle active-site changes. The R28 side chain points toward trimethoprim's trimethoxy aryl tail, motivating modifications at that end while retaining the shared 2,4-diaminopyrimidine head group (Figure 1f–i; PDB 6XG5 and 6XG4).
- **Mutant-selective antibacterial activity:** 4′-DTMP had approximately **30–90-fold greater activity** than trimethoprim against isogenic L28R *E. coli*, while the two drugs were indistinguishable against wild-type cells (Figure 2b–c). In the main comparison, the improvement against L28R was about 30-fold with p = 9.597 × 10⁻⁴.
- **Specificity among common resistance mutations:** Across 11 individually reconstructed, trimethoprim-resistance-associated DHFR point mutants, increased 4′-DTMP activity was specific to L28R (Figure 2d). 4′-DTMP also performed better against most tested combinatorial genotypes containing L28R (Supplementary Figure 2 and Supplementary Table 2).
- **Biochemical binding evidence:** Purified-protein kinetics showed that 4′-DTMP had nearly twofold greater steady-state binding affinity for L28R DHFR than trimethoprim, whereas the two compounds had comparable affinities for wild-type DHFR (Supplementary Figure 3).
- **Not explained by general efflux changes:** Removing `tolC` did not selectively improve 4′-DTMP efficacy. LC–MS/MS nevertheless showed greater 4′-DTMP accumulation in L28R cells after 24 hours, which the authors attribute to stronger intracellular target binding rather than altered efflux (Supplementary Figures 4–5).
- **L28R was purged from a mixed resistant population:** Six previously evolved, trimethoprim-resistant polyclonal populations were mixed and propagated for 32 hours. At 500 µM trimethoprim, L28R rapidly increased and plateaued; at 500 µM 4′-DTMP, L28R initially rose but was then displaced by D27E- and F153S-containing genotypes (Figure 3).
- **Long-term resistance evolved more slowly:** In 21-day morbidostat experiments, seven trimethoprim-selected populations increased resistance by approximately **2,000-fold**, whereas eight 4′-DTMP-selected populations increased resistance by approximately **100-fold**. Estimated final resistance was about tenfold lower under 4′-DTMP, and the evolutionary rate was significantly reduced (Figure 4a–c; final-level p = 2.10 × 10⁻⁸, rate p = 0.0016).
- **The targeted trajectory was strongly suppressed:** Six of seven trimethoprim-evolved populations acquired L28R, compared with one of eight 4′-DTMP-evolved populations (p = 0.017). Final L28R frequency fell from approximately 80% under trimethoprim to below 15% under 4′-DTMP (Figure 4d–f).
- **Fitness remained lower under the derivative:** Final populations evolved with 4′-DTMP doubled more slowly than trimethoprim-evolved populations (63.7 ± 12.5 versus 49.8 ± 10 minutes; p = 0.04), consistent with diversion toward mutations carrying larger catalytic costs.
- **Resistance was delayed, not prevented:** Populations evolved under either drug were cross-resistant to the other. Thus, 4′-DTMP changed which trajectories were favored and reduced the pace and endpoint of resistance, but did not create an evolution-proof treatment (Supplementary Figure 9).
- **Potential toxicity requires attention:** 4′-DTMP and trimethoprim had similar toxicity in confluent ARPE-19 cells up to 1,000 µM, but 4′-DTMP showed significant toxicity above 500 µM in dividing ARPE-19, HEK293A, and CHO-DHFR cells (Supplementary Figure 6).

### Authors' interpretation

- L28R is unusually important because it both increases trimethoprim resistance and compensates for catalytic defects caused by other resistance mutations; suppressing it removes several high-fitness paths simultaneously.
- 4′-DTMP redirects evolution toward alternative DHFR substitutions that confer resistance but impose larger functional costs, slowing population adaptation.
- Detailed knowledge of recurrent target mutations can guide drugs that reshape the future resistance landscape, not just inhibit the present genotype.
- The study does not establish clinical efficacy. Whether 4′-DTMP slows resistance in clinical isolates, animal infections, or other bacterial species remains unknown.

## Main Novelty

- The paper provides experimental biological validation of a previously proposed evolutionary strategy: design an antimicrobial to target a recurrent resistance-conferring mutation and thereby block common evolutionary trajectories.
- Instead of avoiding cross-resistance by alternating unrelated drugs, it exploits **collateral sensitivity of a specific mutant**—L28R is resistant to trimethoprim but selectively vulnerable to 4′-DTMP.
- It connects atomic structure, medicinal chemistry, enzyme kinetics, bacterial susceptibility, mixed-population competition, and long-term experimental evolution in one mechanistic workflow.
- The work measures both immediate activity and evolutionary consequences. 4′-DTMP's key advantage is not superior activity against wild-type *E. coli* but its ability to reduce access to L28R-dependent, high-fitness resistance paths.
- Time-resolved sequencing shows that evolutionary steering is a population-genetic process: L28R lineages are removed and replaced by multiple alternative genotypes rather than by one universal successor mutation.

## Datasets Used for Evaluation

### 1. Historical and current trimethoprim evolution dataset

- **Content:** Frequencies of recurrent DHFR resistance mutations in morbidostat-evolved *E. coli*.
- **Sample size:** **40 independent populations**: seven trimethoprim-evolved populations from this work plus 33 from prior studies.
- **Use:** Establish L28R as a frequent and high-value resistance trajectory (Figure 1d).

### 2. DHFR mutant susceptibility panel

- **Content:** Isogenic chromosomal `folA` replacements in an MG1655-derived NDL47 background, including wild type and 11 common resistance-associated point mutations.
- **Evaluation:** IC95 measurements for trimethoprim and 4′-DTMP; seven replicates for wild type and most point mutants, and 14 replicates for the principal L28R comparison.
- **Additional library:** A combinatorial DHFR library spanning P21L, A26T, L28R, W30G, W30R, and I94L substitutions; the exact number of successfully assayed genotypes is not stated in the main paper.

### 3. Cross-species susceptibility panel

- **Content:** A clinical *E. coli* isolate, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*, and *Staphylococcus aureus* in addition to laboratory *E. coli*.
- **Sample size:** Three replicates per comparison.
- **Result:** 4′-DTMP and trimethoprim had similar activity in these non-L28R backgrounds (Figure 2e).

### 4. Mixed resistant-population competition dataset

- **Content:** A near-equal mixture of six previously evolved polyclonal populations carrying distinct `folA` promoter and coding mutations.
- **Conditions:** No drug (n = 3), 500 µM trimethoprim (n = 7), or 500 µM 4′-DTMP (n = 7).
- **Duration and sampling:** 32 hours, six sampling time points, with serial dilution every 4–8 hours.
- **Measurements:** Growth rate and deep amplicon sequencing of `folA` mutation frequencies (Figure 3).

### 5. Long-term morbidostat evolution dataset

- **Starting strain:** Drug-sensitive, isogenic MG1655-derived TB194.
- **Conditions:** Trimethoprim, seven independent populations; 4′-DTMP, eight independent populations.
- **Duration:** 21 days, approximately 10–15 generations per day.
- **Measurements:** Daily archived samples, time-resolved IC50, growth/doubling time, and `folA` amplicon sequencing (Figure 4).
- **Raw sequencing accession:** [NCBI BioProject PRJNA717019](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA717019/).

### 6. Structural and biochemical datasets

- **Crystal structures:** Wild-type DHFR–TMP–NADPH at 1.9 Å ([PDB 6XG5](https://www.rcsb.org/structure/6XG5)) and L28R DHFR–TMP–NADPH at 2.1 Å ([PDB 6XG4](https://www.rcsb.org/structure/6XG4)).
- **Biochemistry:** Steady-state inhibition measurements across 0.1 nM–100 µM inhibitor using purified wild-type and L28R DHFR.
- **Cellular pharmacology:** LC–MS/MS measurements of intracellular and extracellular trimethoprim and 4′-DTMP in wild-type, L28R, BW25113, and `ΔtolC` strains at 1 and 24 hours, with three replicates per condition.
- **Cytotoxicity:** ARPE-19, HEK293A, and CHO-DHFR cells treated with 31.25–2,000 µM compound.

### 7. Reproducibility resources

- **Figure and table data:** [GitHub repository](https://github.com/erdaltoprak-zz/NatureCommunication2021_Manna).
- **Analysis and plotting code:** [Zenodo record 4630929](https://doi.org/10.5281/zenodo.4630929).
- **Crystallographic diffraction data:** Integrated Resource for Reproducibility in Macromolecular Crystallography, linked through the deposited structures.

## Experimental Procedure

- **Identify a target resistance mutation:** Aggregate prior and current morbidostat data to determine that L28R is a frequent, strongly beneficial trimethoprim-resistance mutation with positive epistatic effects on other DHFR mutants.
- **Solve target structures:** Purify wild-type and L28R DHFR, co-crystallize each with trimethoprim and NADPH, collect X-ray diffraction data, and refine structures at 1.9 and 2.1 Å.
- **Design a mutant-selective derivative:** Preserve trimethoprim's polar 2,4-diaminopyrimidine head and modify the aryl tail positioned near R28; synthesize and screen candidate derivatives, identifying 4′-DTMP.
- **Measure antibacterial specificity:** Determine IC95 values for trimethoprim and 4′-DTMP against wild type, 11 individual DHFR mutants, combinatorial DHFR genotypes, an efflux-deficient strain, a clinical *E. coli* isolate, and additional bacterial species.
- **Test direct target binding:** Measure steady-state inhibition constants using purified wild-type and L28R DHFR to compare the two drugs' binding affinities.
- **Assess cellular exposure:** Quantify intracellular and extracellular compounds by LC–MS/MS to evaluate whether uptake, efflux, or target retention could explain mutant-selective activity.
- **Evaluate mammalian-cell toxicity:** Treat confluent and dividing human/hamster cell lines with concentration gradients of each compound and quantify viability using ATP-dependent luminescence.
- **Challenge a heterogeneous resistant population:** Mix six evolved trimethoprim-resistant populations, propagate them under no drug, trimethoprim, or 4′-DTMP, and use time-resolved `folA` sequencing to observe clonal replacement.
- **Run long-term evolution:** Evolve 15 initially sensitive populations in morbidostats for 21 days under dynamically adjusted trimethoprim or 4′-DTMP concentrations.
- **Quantify evolutionary outcomes:** Fit time-resolved resistance trajectories, compare final resistance and adaptation rates, and deep-sequence `folA` to reconstruct mutation frequencies and evolutionary paths.

## Key Biology Insights

- **L28R is a resistance-and-compensation mutation.** Unlike many DHFR substitutions that weaken both drug and substrate binding, L28R reduces trimethoprim sensitivity while increasing affinity for dihydrofolate and can compensate for catalytic deficiencies elsewhere.
- **A resistance mutation can create a druggable vulnerability.** The new arginine changes the local chemical environment near trimethoprim's aryl tail, allowing 4′-DTMP to recover target engagement selectively in L28R cells.
- **Evolutionary trajectories have unequal value.** Blocking a common compensatory mutation has a larger effect than blocking a rare mutation because it removes several downstream, epistatically supported genotypes.
- **Evolution adapts around the block.** D27E, F153S, promoter changes, and other DHFR substitutions provide alternate paths, but the resulting populations grow more slowly and achieve less resistance during the experiment.
- **Target overexpression remains available.** The `c-35t` promoter mutation persisted under both drugs, showing that a mutant-selective inhibitor does not suppress all resistance mechanisms.
- **Cross-resistance and fitness are separate outcomes.** Final populations resisted both compounds, yet 4′-DTMP-evolved cells had poorer growth and lower resistance levels than trimethoprim-evolved cells.

## Implications

- Resistance surveillance and experimental-evolution maps could become inputs to drug design: medicinal chemistry can prioritize compounds active against both the ancestral target and the most evolutionarily enabling target mutants.
- Mutant-targeting drugs might be used to delay resistance, steer populations toward costly genotypes, or selectively remove resistant subclones. The optimal clinical schedule—replacement, combination, or sequence—was not tested here.
- The approach is most promising when resistance repeatedly funnels through a small number of high-fitness, compensatory mutations. It may be less effective for targets with many equivalent escape routes or resistance dominated by horizontal gene transfer.
- 4′-DTMP itself is not demonstrated to be clinically superior. Resistance still evolved, cross-resistance emerged, the experiments used laboratory evolution rather than infections, and toxicity appeared in dividing mammalian cells above 500 µM.
- Follow-up work should test pharmacokinetics, therapeutic index, animal infection models, clinical isolates, plasmid-mediated trimethoprim resistance, and treatment schedules that exploit L28R collateral sensitivity without rapidly selecting alternative escape routes.
