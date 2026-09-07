# Paper Summary

### Authors
- Alessandro Gerada, Yinzheng Zhong, Nicholas Harper, Anoop Velluva, Nada Reza, Vineet Dubey, Alex Howard, Peter L. Green, Steve Paterson, and William Hope

### Journal
- npj Antimicrobials and Resistance

### Publication Date
- May 26, 2026

### DOI
- https://doi.org/10.1038/s44259-026-00217-4

## Keywords
- antimicrobial resistance
- minimum inhibitory concentration
- whole-genome sequencing
- *Escherichia coli*
- machine learning
- XGBoost
- k-mers
- Progressive Genome Segment Enhancement
- genomic antimicrobial susceptibility testing
- interpretable machine learning
- external validation

## Main Idea
- The authors introduce Progressive Genome Segment Enhancement (PGSE), a machine-learning algorithm that predicts antimicrobial minimum inhibitory concentrations (MICs) directly from bacterial whole-genome sequences without requiring a predefined database of resistance genes.
- PGSE iteratively converts short k-mers into a compact set of informative, variable-length genome segments. In *E. coli*, it approached the internal accuracy of resistance-gene annotation models, outperformed conventional fixed-length k-mer models, generalized best overall to an external dataset, used less memory and time, and produced features that mapped to recognizable resistance biology.

## Evidence Supporting the Main Idea
- **Clinically measured training labels:** The internal dataset contained 762 clinical *E. coli* isolates and 6,080 quality-controlled agar-dilution MIC measurements across 10 antimicrobials. The primary comparison focused on ceftazidime, ciprofloxacin, cefepime, gentamicin, and meropenem because their MIC distributions were less imbalanced than those of the other five drugs.
- **Efficient feature refinement:** PGSE starts with canonical 6-mers, partitions the feature space into subsets of about 5,000 features, trains XGBoost models, retains the 10,000 highest-importance segments, removes redundant subsequences, and extends retained segments by up to two nucleotides per round. It repeats this cycle until extension no longer improves feature importance (Figure 1).
- **Competitive internal MIC prediction:** When measurements were pooled across all tested antimicrobials, 71.6% of PGSE predictions were within one doubling dilution of the agar-dilution MIC. Pooled essential agreement was 75.6% for annotation models and 67.5% for fixed 10-mer models. Among the five primary drugs, PGSE essential agreement ranged from 52.6% for cefepime to 88.2% for meropenem (Table 3; Figures 5 and 6).
- **Lower computational cost:** In the ceftazidime benchmark, PGSE required 36 minutes and 23.6 GB peak RAM, compared with 71 minutes and 38.8 GB peak RAM for a 10-mer model; the k-mer time excluded hyperparameter tuning. Fixed k-mer models with k greater than 10 could not run within 64 GB RAM. Figure 7 also shows that PGSE performance was much less sensitive to its starting k than conventional k-mer performance was to k-mer length.
- **Strong external generalization:** On 4,755 external BV-BRC *E. coli* genomes, PGSE achieved the highest pooled F1 score (0.85), compared with 0.82 for annotation models and 0.74 for fixed k-mer models. Its median external F1 was 0.83 across the five drugs, and its generalization gaps were particularly small for ceftazidime, ciprofloxacin, cefepime, and gentamicin (Table 5).
- **Important boundary case:** External meropenem F1 was only 0.56 for both PGSE and annotation models, versus 0.32 for the k-mer model. PGSE fell from 0.70 internally because *bla*<sub>OXA-48</sub> occurred in 18.4% of internal strains but only 0.04% of external strains, demonstrating sensitivity to shifts in resistance-mechanism prevalence.
- **Interpretable genomic features:** Almost every manually examined top segment had a plausible direct or indirect relationship to resistance. Gentamicin segments localized to or near *aac(3)-IId* and *rmtB*; four leading ciprofloxacin segments tracked *gyrA* or *parC* variation; and ceftazidime segments captured several extended-spectrum or AmpC beta-lactamases (Table 2; Figure 3).
- **Mechanistic resolution beyond a binary gene call:** One ceftazidime segment distinguished the *bla*<sub>CTX-M-3</sub> phylogenetic cluster from the *bla*<sub>CTX-M-14</sub> cluster (Figure 4). The top meropenem segment marked conserved plasmid contexts associated with either *bla*<sub>OXA-48</sub> or *bla*<sub>NDM</sub> and detected those two carbapenemases with 99% sensitivity and 96% specificity in the internal dataset.

## Main Novelty
- PGSE occupies a useful middle ground between two common genomic prediction strategies: it does not depend on a curated resistance-gene catalog, yet it avoids the full dimensionality and limited interpretability of fixed-length whole-genome k-mer models.
- Its progressive extension step learns variable-length sequence motifs at the resolution supported by predictive performance instead of forcing the analyst to choose one large k in advance.
- The output is both a trained MIC regression model and a ranked, compact collection of sequence segments that can be mapped back to genes, plasmid neighborhoods, phylogenetic clusters, or candidate mechanisms.
- The study evaluates generalization on a genuinely separate public dataset rather than only reporting internal cross-validation or pooling external isolates into training.
- The authors provide open-source Python and R implementations, an online interface, the study data, raw sequence accessions, and analysis code, making the approach unusually reproducible.

## Datasets Used for Evaluation
- **Liverpool clinical strain bank (internal development and validation):** 762 *E. coli* isolates collected by Liverpool Clinical Laboratories, UK, from 2017 to 2021. Blood isolates accounted for 515/762 (68%) and urine for 158/762 (21%). Isolates were sampled across eight susceptibility phenotypes to preserve uncommon but clinically important resistance patterns.
- **Internal MIC dataset:** 6,080 post-quality-control MICs for 10 drugs: amoxicillin, amikacin, amoxicillin-clavulanic acid, ceftazidime, cefepime, chloramphenicol, ciprofloxacin, gentamicin, meropenem, and tigecycline. The primary five-drug evaluation used 721, 703, 722, 532, and 711 MICs, respectively, for ceftazidime, ciprofloxacin, cefepime, gentamicin, and meropenem.
- **Internal WGS dataset:** Illumina paired-end whole-genome sequences for the 762 isolates, assembled with SPAdes and annotated with AMRFinderPlus. The authors identified 187 unique known AMR genes. Raw reads are available in NCBI SRA project PRJNA1297298.
- **BV-BRC external validation dataset:** 4,755 public *E. coli* genomes with MIC metadata for at least one study drug. Available per-drug sample sizes were 4,260 for ceftazidime, 4,501 for ciprofloxacin, 2,877 for cefepime, 4,643 for gentamicin, and 4,207 for meropenem.
- **Public resources:** Processed study data are available from the University of Liverpool Data Catalogue (record 300855); PGSE source code is at https://github.com/yinzheng-zhong/PGSE; and analysis code is at https://github.com/agerada/molecular_mic_analysis.

## Experimental Procedure
- Retrieve stored clinical *E. coli* isolates and their routine disk-susceptibility results from 2017-2021; identify isolates by MALDI-TOF and stratify them into eight phenotypic resistance groups before sampling 762 strains without replacement.
- Measure reference MICs by agar dilution for 10 antimicrobials, using doubling dilution plates, *E. coli* ATCC 25922 controls, standardized inocula, 18-hour incubation, and AIgarMIC-assisted growth annotation.
- Extract genomic DNA, prepare Illumina libraries, sequence 2 x 150-bp reads on a NovaSeq 6000, trim reads, assemble genomes with SPAdes, and identify known AMR determinants with AMRFinderPlus.
- Uncensor extreme MIC values, log2-transform them, and exclude experiments that failed growth-control or EUCAST quality-control criteria.
- Train 30 XGBoost regression submodels: one annotation model, one fixed k-mer model, and one PGSE model for each of the 10 drugs. All models use the same log2 MIC labels.
- For PGSE, begin with short canonical k-mers; repeatedly partition features, rank them by XGBoost gain, retain the top 10,000, eliminate redundant nested segments, extend promising sequences, recount them across genomes, and stop when no extension improves importance.
- Use stratified five-fold cross-validation for internal evaluation. Tune the annotation and k-mer models by grid search and early stopping; evaluate multiple fixed k values and PGSE starting values.
- Convert continuous predictions back to doubling-dilution MICs. Evaluate essential agreement (within plus or minus one dilution), categorical agreement, minor/major/very-major errors, and Pearson correlation using agar dilution as the reference.
- Apply each fold-specific model to the independent BV-BRC genomes, use the median of five predictions, convert MICs to susceptible versus intermediate/resistant status with EUCAST 2023 breakpoints or epidemiological cutoffs, and compare F1 score, sensitivity, specificity, and generalization gap.
- Map the five most important PGSE segments per primary drug to nearby annotated genomic elements to assess whether the data-driven features recover established or potentially novel resistance biology.

## Key Biology Insights
- Ciprofloxacin MIC was strongly encoded by canonical quinolone-resistance mutations: PGSE recovered segments associated with *gyrA* and *parC*, while the annotation model assigned 95.6% of total importance to *parC* S80I, *gyrA* D87N, and *gyrA* S83L.
- Gentamicin prediction was dominated by aminoglycoside-modifying and target-modifying mechanisms, including *aac(3)-IId* and the 16S rRNA methylase *rmtB*.
- Ceftazidime resistance was genetically heterogeneous. The same predictive segments occurred in or near multiple beta-lactamases, including *bla*<sub>CTX-M-15</sub>, *bla*<sub>CMY-42</sub>, and *bla*<sub>SHV-12</sub>, suggesting that short optimized motifs can capture shared functional or evolutionary structure across distinct enzymes.
- Meropenem features often represented the mobile genomic context around carbapenemases rather than the enzyme sequence alone. Signals in *trbA*, *dsbD*, and *trpF* linked PGSE predictions to conserved *bla*<sub>OXA-48</sub>- and *bla*<sub>NDM</sub>-bearing plasmid regions.
- A ciprofloxacin-associated segment within *paeA* is a candidate noncanonical signal because previous deletion experiments linked that gene to increased nalidixic-acid sensitivity. In this paper, however, the relationship is associative and was not functionally validated.
- The phylogenetic tree (Figure 2) shows resistance distributed across a diverse strain collection, but predictive segments can still encode lineage or linkage effects. Consequently, feature importance does not by itself prove a causal resistance mechanism.

## Implications
- PGSE could support genomic antimicrobial susceptibility testing when a comprehensive resistance-gene catalog is unavailable or when emerging mechanisms need to be discovered rather than prespecified.
- Predicting quantitative MICs is potentially more useful than predicting only susceptible/resistant labels for surveillance, pharmacodynamic target assessment, and comparison across changing clinical breakpoints.
- The compact segment set could guide candidate-mechanism discovery or development of targeted molecular assays. Any novel segment would still require epidemiological replication and laboratory validation before being treated as causal.
- The method is efficient enough for workstation-scale training and may enable continuous retraining as paired WGS-MIC datasets grow. In clinical laboratories, the authors envision it complementing phenotypic testing and prioritizing second-line MIC panels rather than immediately replacing culture-based AST.
- External validation is a major strength, but the meropenem result illustrates dataset-shift risk: performance can deteriorate when resistance mechanisms and MIC methods differ across populations. Prospective validation should therefore be geographically diverse, species-specific, and laboratory-aware.
- The study remains a proof of concept: it uses only 762 training strains, one bacterial species, and one UK region; enriches the training collection for selected resistance phenotypes; externally evaluates categorical rather than fully comparable quantitative MICs; and benchmarks only two alternative feature strategies. It does not demonstrate turnaround time, patient-level clinical benefit, or safety for treatment decisions.
