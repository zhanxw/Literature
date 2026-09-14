# Paper Summary

### Authors
Domiziana Cecchini, Akshat Kumar Nigam, Ming Tang, Joana Reis, Matt Koop, Andrea Gottinger, Callum Robert Nicoll, Yao Wang, Abhilash Jayaraj, Süleyman Selim Çınaroglu, Ricarda Törner, Yehor Malets, Minko Gehev, Krishna M. Padmanabha Das, Kelly Churion, Jongwan Kim, Nidhin Thomas, Yong Li, Hyuk-Soo Seo, Sirano Dhe-Paganon, Christopher Secker, Mohammad Haddadnia, Alexander Hasson, Minkai Li, Abhishek Kumar, Roni Levin-Konigsberg, Eun-Bee Choi, Geoffrey I. Shapiro, Huel Cox 3rd, Luke Sebastian, Chelsea Braithwaite, Puspalata Bashyal, Dmytro S. Radchenko, Aditya Kumar, Lei Yang, Pierre-Yves Aquilanti, Henry Gabb, Amr Alhossary, Eric O’Neill, Gerhard Wagner, Alán Aspuru-Guzik, Yurii S. Moroz, Charalampos G. Kalodimos, Konstantin Fackeldey, John D. Schuetz, Andrea Mattevi, Haribabu Arthanari, and Christoph Gorgulla.

### Journal
Nature Biotechnology

### Publication Date
2026-09-01 (online)

### DOI
10.1038/s41587-026-03217-x

## Keywords

Ultralarge virtual screening; adaptive target-guided virtual screening; molecular docking; active learning; artificial intelligence; Enamine REAL Space; FSP1; PARP1; ferroptosis.

## Main Idea

The authors introduce AdaptiveFlow, an open-source platform for scalable ultralarge virtual screening (ULVS). Its key strategy, Adaptive Target-Guided Virtual Screening (ATG-VS), partitions a ready-to-dock version of the Enamine REAL Space into an 18-dimensional molecular-property matrix, screens representative molecules from each occupied tranche, and then fully screens only target-enriched tranches. Optional active learning further prioritizes compounds. The resulting workflow combines ligand preparation, more than 1,500 docking-protocol combinations, machine-learning docking, GPU support, and cloud-scale execution.

## Evidence Supporting the Main Idea

- AdaptiveFlow prepared 31,507,987,117 enumerated REAL Space molecules into approximately 68.7 billion ready-to-dock molecular forms after stereoisomer and tautomer enumeration. The library has approximately 12 million occupied tranches in an 18-dimensional property grid and includes 28 calculated molecular properties (Fig. 2 and Supplementary Table 2).
- In the default ATG-VS configuration, one representative per tranche requires approximately 12 million prescreen dockings for the 69-billion-compound library, over 5,000-fold fewer evaluations than exhaustive screening. The paper reports up to 1,000-fold cost reduction for ATG-VS relative to exhaustive searches, with a further 10–100-fold throughput gain from GPU and deep-learning methods.
- In a five-million-compound benchmark across ten proteins (kinases, phosphatases, a GPCR, and protein–protein interaction targets), 100,000-compound ATG screens, with or without active learning, generally matched the top-50 docking performance of one-million-compound random screens (Fig. 4), a tenfold reduction in screened compounds.
- The production-scale comparison on the full REAL Space showed comparable or better top-50 docking scores for ATG-VS than standard ULVS while using far fewer docking evaluations (Extended Data Figs. 6 and 7). Property-based binning remained effective with Smina/Vinardo and GWOVina/flexible-side-chain docking (Supplementary Fig. 13).
- AdaptiveFlow demonstrated near-linear AWS scaling to 5.6 million virtual CPUs (Supplementary Fig. 2).
- For FSP1, 33 synthesized virtual hits yielded two compounds with at least 1.5 °C thermal-shift stabilization and at least 50% inhibition at 10 µM. The best compounds had competitive Ki values of 0.283 ± 0.05 µM (afi-FSP1-1) and 0.777 ± 0.22 µM (afi-FSP1-2), engaged human FSP1 in cells, and were supported by co-crystal structures (Table 1 and Fig. 5).
- For PARP1, screening and experimental testing produced seven inhibitors; four had IC50 values below 250 nM. iParp1 had an IC50 of 8.8 nM, direct binding was supported by protein NMR, and a 2.05-Å PARP1–inhibitor crystal structure validated the predicted binding mode.

## Main Novelty

- A unified, open-source ULVS platform that combines massive ready-to-dock chemical space, adaptive target-specific navigation, classical and ML-based docking, and heterogeneous CPU/GPU/cloud execution.
- ATG-VS uses a chemically interpretable 18-dimensional tranche map to replace much of the brute-force search with representative prescreening and selective expansion.
- The platform makes the prepared 69-billion-compound REAL Space available in structure-ready formats and supports SELFIES, active learning, and modular development of AI-driven screening workflows.

## Datasets Used for Evaluation

- **Enamine REAL Space 2022q1-2:** 31,507,987,117 enumerated compounds before preparation and approximately 68.7 billion ready-to-dock forms after preparation; derived from 137,000 building blocks and 167 one-pot synthetic protocols. It served as the primary ultralarge library for ATG-VS, production benchmarks, and FSP1/PARP1 discovery.
- **Five-million-compound REAL Space subset:** 5,000,000 molecules sampled from the prepared REAL Space. It was used for controlled comparisons of random screening, ATG-VS, and ATG-VS with active learning across ten protein targets.
- **Ten-protein benchmark panel:** Ten diverse protein targets, including kinases, phosphatases, a GPCR, and protein–protein interaction interfaces; the paper uses the panel to compare docking-score enrichment and screening depth. Individual target names shown in Fig. 4 include KRAS-G12V, CB1, PTPRB, JNK3, TLR8, PIK3CG, NTR1, MED15-KIX, KEAP1, and RPTO.
- **FSP1 validation set:** 42 candidates from 37 clusters were ordered after property and safety filters; 33 compounds were synthesized and experimentally tested. The set evaluated virtual-hit binding and inhibition of FSP1.
- **PARP1 validation set:** 160 promising candidates were synthesized after the ATG prescreen and a 100-million-molecule primary screen. Enzymatic high-throughput screening identified seven inhibitors, with four selected for deeper characterization.
- **Cellular validation models:** FSP1 compounds were tested in FSP1-expressing HEK293 cells and Jurkat T-cell acute lymphoblastic leukemia cells; iParp compounds were assessed in BRCA1-deficient triple-negative breast cancer cells. These assays evaluated target engagement and cellular activity, not library-screening performance.

## Experimental Procedure

- Prepare ligand libraries with stereoisomer and tautomer enumeration, protonation-state prediction, 3D conformer generation, deduplication, quality checks, and calculation of 28 molecular properties.
- Partition compounds into an 18-dimensional property matrix and select 1–10 representative molecules per occupied tranche.
- Perform an ATG prescreen against the target; rank tranches by docking score and optionally apply property filters.
- Fully screen selected tranches in an ATG primary screen; optionally train a Morgan-fingerprint classifier on prescreen scores and use it to prioritize compounds.
- Benchmark ATG-VS against random ULVS using top-50 docking scores, screening depth, multiple docking engines, and ten protein targets.
- Evaluate scalability and deployment on heterogeneous local/cloud infrastructure, including AWS CPU instances, ARM CPUs, GPUs, Slurm, and spot instances.
- Screen FSP1 at its coenzyme-Q site using a prepared FSP1–FAD–NAD+ receptor; filter top candidates with physicochemical and predicted-toxicity criteria, synthesize selected compounds, and measure thermal shift, NADH depletion, kinetic Ki, surface-plasmon-resonance Kd, cellular target engagement, ferroptosis-related activity, and co-crystal structures.
- Screen PARP1 with an ATG prescreen followed by a 100-million-compound primary screen; synthesize 160 candidates and perform two-concentration enzymatic HTS, dose-response characterization, NMR binding analysis, X-ray crystallography, and clonogenic cellular assays.

## Key Biology Insights

- FSP1 can bind NAD(P)+ and coenzyme Q simultaneously in catalytically competent orientations. The structures support a ternary-complex mechanism and show that NAD+ binding shifts the flavin ring by approximately 2 Å.
- The validated FSP1 inhibitors occupy the coenzyme-Q site adjacent to FAD, displace coenzyme Q, and reproduce key interactions with the flavin and residues including Y290, F354, F15, and L323.
- Several FSP1 inhibitors preferentially reduce coenzyme-Q-reduction activity while retaining more NADH-oxidase activity. The authors propose that this separation could be pharmacologically useful, but state that the pro-ferroptotic mechanism requires further validation.
- The PARP1 results show that an unbiased virtual screen can yield both known-scaffold-related compounds and scaffold variations; iParp1 reached potency comparable to olaparib in the reported biochemical assay.
- Cellular activity was not equivalent to biochemical potency in all cases: reduced iParp1 activity was attributed to poor membrane permeability associated with hydrolysis.

## Implications

AdaptiveFlow provides a practical infrastructure for exploring chemical space at tens-of-billions scale without exhaustive docking of every molecule. Its tranche-based prioritization can reduce computation while preserving high-scoring candidates, and its modular design supports future docking algorithms, generative models, active-learning loops, and difficult target classes. The FSP1 and PARP1 demonstrations show that the approach can produce experimentally validated chemical starting points, although docking scores, biochemical potency, cellular exposure, and therapeutic efficacy remain distinct validation steps. The paper makes the platform code available under GPL-2.0 and provides REAL Space access, structural data, and related code/data resources through the project and public repositories.

