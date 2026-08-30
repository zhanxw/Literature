# Paper Summary

**Paper:** Higher-order epistasis drives evolutionary unpredictability toward novel antibiotic resistance  
**Source:** [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2025.07.08.663783v1)  
**Peer-review status:** Preprint; not certified by peer review

### Authors

Ilona Kamila Gaszek; Muhammed Sadik Yildiz; Devin Meng; Jose Alberto de la Paz; Sophia Maria Alvarez; Faruck Morcos; Milo Lin; Erdal Toprak

### Journal

bioRxiv (preprint)

### Publication Date

July 11, 2025 (version 1)

### DOI

[10.1101/2025.07.08.663783](https://doi.org/10.1101/2025.07.08.663783)

## Keywords

- TEM-1 β-lactamase
- Extended-spectrum β-lactamase (ESBL)
- Antibiotic resistance
- Aztreonam
- Ampicillin
- Higher-order epistasis
- Fitness landscape
- Combinatorial mutagenesis
- DNA barcoding
- LightGBM and SHAP
- Direct coupling analysis (DCA)
- Latent generative landscape (LGL)

## Main Idea

The effect of mutations on antibiotic resistance depends strongly on whether TEM-1 β-lactamase is adapting to a familiar substrate or acquiring activity against a novel one. The authors exhaustively measured every combination of 18 clinically observed substitutions at 13 TEM-1 residues. Under ampicillin, a native substrate for which wild-type TEM-1 is already highly effective, the fitness landscape was comparatively smooth, mutation-averse, and predictable. Under aztreonam, a novel monobactam substrate, resistance depended on context-specific interactions extending well beyond mutation pairs, producing a rugged landscape with many possible evolutionary outcomes.

The central conclusion is that higher-order epistasis is a major source of evolutionary unpredictability during acquisition of a new resistance function. Nevertheless, high-performing variants remain constrained by coevolutionary patterns present in natural β-lactamase sequences, suggesting that adaptation requires both new substrate-recognition combinations and preservation of compatible protein-wide interactions.

## Evidence Supporting the Main Idea

### Direct experimental observations

- **Combinatorially complete landscape:** The TEM-1 combinatorial mutant library contained all **55,296** possible genotypes formed by 18 substitutions at 13 residues, with approximately **300 DNA barcodes per genotype** (Figure 1C).
- **Large, time-resolved fitness dataset:** The authors assayed the library in biological triplicate across six analyzed ampicillin concentrations and eight analyzed aztreonam concentrations, with sampling every 3 hours for 12 hours. This produced approximately **eight million individual fitness measurements** (Figure 1D–F; Methods).
- **Native versus novel substrate:** Few mutants exceeded wild-type TEM-1 under ampicillin, whereas hundreds to thousands outperformed wild type under aztreonam. At the highest analyzed aztreonam concentration, the surviving population was dominated by roughly **200 highly resistant variants** (Figure 1E–F and Figure S3).
- **Broad resistance potential:** The pooled library showed increased resistance to several cephalosporins and aztreonam. Ceftazidime and aztreonam minimum inhibitory concentrations increased by approximately **1,000-fold** relative to the relevant low-resistance controls, while no improved resistance was detected for the three tested carbapenem regimens (Figure S2).
- **Different landscape topology:** Graph-based coarse-graining yielded few dominant peaks under ampicillin but hundreds of combined peak nodes under aztreonam. Aztreonam topology also changed non-monotonically with drug concentration, indicating that evolutionary fate depends on both starting genotype and selection strength (Figure 2 and Figure S4).
- **Distinct mutation-load pattern:** Median ampicillin fitness declined monotonically as substitutions accumulated. Aztreonam fitness was much more dispersed, with the number and fitness of resistant variants peaking at approximately **four to seven mutations** (Figure 3C–D).
- **Context-dependent resistance determinants:** E104K, R164H/S/N, and E240K were enriched among the most aztreonam-resistant variants, while preservation of wild-type A237, G238, and R244 was often favored. This simple signature did not fully identify resistant genotypes, demonstrating that additional genetic context matters (Figure 3B).
- **Direct epistasis evidence:** Most single mutations were neutral or mildly deleterious under ampicillin, and pairwise interactions were generally small. Under aztreonam, combinations involving E104K, R164H/S/N, and E240K frequently showed strong positive or negative epistasis (Figure 4).
- **Higher-order trajectory effects:** R164S made E104K and E240K strongly beneficial under aztreonam, but A237T or G238S could reverse the effects of the same combinations. These sign changes across genetic backgrounds directly demonstrate higher-order, context-dependent epistasis (Figure S5).
- **Low-order models were insufficient:** Additive and pairwise terms explained just over half of ampicillin fitness variance (reported R² approximately 0.52), but aztreonam models did not reach R² = 0.5 until fifth-order interactions were included (Figure 5).
- **Machine-learning predictability differed:** LightGBM predictions converged rapidly for ampicillin. Aztreonam required substantially more training data and retained greater error, consistent with a more rugged landscape (Figures 6–7). The Results text reports RMSD **0.288** with 10% training data, whereas the Figure 7 caption reports **0.426**; this numerical discrepancy is unresolved in the preprint.
- **Evolutionary constraints remained visible:** High-fitness variants under both drugs were enriched for favorable, more-negative DCA Hamiltonian scores and localized near favorable regions surrounding wild-type TEM-1 in the latent generative landscape (Figure 8 and Figure S6).

### Authors' interpretation

- TEM-1 is already close to an optimum for ampicillin hydrolysis, leaving relatively little opportunity for tested clinical substitutions to improve performance.
- Novel aztreonam activity requires coordinated changes whose effects cannot be inferred reliably from isolated mutations or mutation pairs.
- Multiple aztreonam-resistance routes are possible, but successful variants must preserve family-level epistatic compatibility needed for β-lactamase folding or function.
- Combining complete experimental landscapes, graph analysis, interpretable machine learning, and evolutionary sequence statistics may help identify evolutionary roadblocks that reduce access to resistance.

## Main Novelty

- The study constructs what the authors describe as the **largest experimentally determined antibiotic-resistance fitness landscape to date**, exhaustively covering all 55,296 combinations of 18 clinically observed mutations rather than sampling only nearby or random mutants.
- It compares the same complete genotype set under a native substrate and a novel substrate across multiple selection strengths, directly linking functional novelty to increased higher-order epistasis, landscape ruggedness, and history dependence.
- It integrates four complementary levels of analysis:
  - time-resolved experimental fitness measurements;
  - graph-theoretic mapping of accessible evolutionary trajectories;
  - explicit epistatic reconstruction plus LightGBM/SHAP interpretation;
  - DCA and VAE-based latent generative landscapes derived from natural β-lactamase sequences.
- The work shows that a novel resistance phenotype can emerge without an obligatory loss of native-substrate resistance: many aztreonam-resistant variants also retained high ampicillin fitness.

## Datasets Used for Evaluation

### 1. TEM-1 combinatorial mutant library (TEM-1CML)

- **Content:** Every possible genotype formed from 18 clinically prevalent substitutions distributed across 13 TEM-1 residues; variants carried zero to 13 mutated positions.
- **Size:** **55,296 genotypes**.
- **Barcoding:** Random 52-bp barcode region with 15 variable nucleotide positions; approximately **300 mapped barcodes per genotype** on average.
- **Host and vector:** Low-copy pBR322 constructs in antibiotic-sensitive *Escherichia coli* NEB10-beta.
- **Controls:** Barcoded wild-type TEM-1 and a catalytically inactive S70A/E166A double mutant.
- **Data availability:** A public accession or repository for the complete measured landscape is **not specified in the paper**.

### 2. Antibiotic-selection fitness dataset

- **Content:** Barcode-derived genotype frequencies, total OD600, normalized genotype growth curves, and log10 area-under-the-curve fitness (AUC-Fitness).
- **Scale:** Approximately **eight million fitness measurements**.
- **Replication:** Three biological replicates.
- **Time points:** 0, 3, 6, 9, and 12 hours.
- **Analyzed concentration series:** Six ampicillin concentrations spanning 0–781 µg/mL and eight aztreonam concentrations spanning 0–324 µg/mL are reported in Figure 1. The Methods additionally list higher challenge doses used in the assay setup (up to 50,000 µg/mL ampicillin and 3,000 µg/mL aztreonam), indicating that some extreme-dose conditions were not retained in the main quantitative landscape.
- **Primary comparison conditions:** 781 µg/mL ampicillin and 36 µg/mL aztreonam; 36 µg/mL was chosen as slightly above the stated clinical resistance cutoff of 32 µg/mL.

### 3. β-lactam antibiotic MIC screen

- **Content:** Pooled-library and control susceptibility to ampicillin, ceftazidime, cefotaxime, ceftriaxone, aztreonam, cefepime, ertapenem, imipenem/cilastatin, and meropenem.
- **Design:** Threefold serial dilutions in 96-well plates; MIC assessed at 20 hours; three biological replicates.
- **Sample size:** Three strain/construct conditions are described: plasmid-free NEB10-beta, pBR322-TEM-1, and pBR322-TEM-1CML.

### 4. Natural β-lactamase family sequence dataset

- **Content:** UniProt Swiss-Prot and TrEMBL sequences matching the PF13354 β-lactamase profile-HMM seed.
- **Initial size:** **104,744 sequences**.
- **Filtered size:** **27,242 sequences** after removing sequences with at least 5% contiguous gaps.
- **Use:** Direct coupling analysis, conditional effective-alphabet estimates, sequence Hamiltonians, and VAE-based latent generative landscapes.
- **Coverage limitation:** Hamiltonian scoring used the TEM-1/PF13354 overlap at residues 48–261; mutated positions 21, 39, 275, and 276 were excluded from this analysis.

## Experimental Procedure

- **Select clinically relevant mutations:** Choose 18 substitutions across 13 TEM-1 positions based on their prevalence in clinical variants. One substitution, L21P, arose from an intended L21F construction but was retained for analysis.
- **Build the exhaustive library:** Synthesize all 55,296 combinations on low-copy pBR322, attach randomized DNA barcodes, transform into *E. coli* NEB10-beta, and pool nine transformations that each exceeded 10⁸ transformants.
- **Map barcodes to genotypes:** Use long-read PacBio sequencing to create the barcode–variant matchbook, yielding approximately 300 barcodes per genotype.
- **Add reference strains:** Spike pooled cultures with 5% barcoded wild-type TEM-1 cells and 1% barcoded catalytically inactive S70A/E166A cells.
- **Screen antibiotic breadth:** Measure pooled-library MICs across nine β-lactam antibiotic conditions to identify native and novel substrates with large dynamic ranges. This screen motivated detailed study of ampicillin and aztreonam.
- **Perform pooled selections:** Grow three replicate libraries across drug concentration series, track OD600 every 3 hours for 12 hours, harvest cells at each time point, isolate plasmids, amplify the barcode region, and sequence with paired-end Illumina/NovaSeq reads.
- **Calculate variant fitness:** Combine total culture density with barcode frequency to estimate each genotype's normalized cell density over time. Define AUC-Fitness as log10 of the area under that normalized growth curve, integrating lag time, growth rate, and final density.
- **Construct evolutionary graphs:** Connect genotypes differing by one substitution; orient edges toward equal or higher fitness; infer a no-drug neutrality cutoff covering 99% of adjacent-genotype fitness differences; iteratively merge neutral nodes; and classify coarse-grained nodes and edges as peaks, connections, or committed paths.
- **Quantify epistasis:** Compare single- and double-mutant effects, calculate pairwise epistasis, inspect selected higher-order trajectories, and fit linear models with interaction terms through as high as 13th order.
- **Model genotype-to-fitness relationships:** Train LightGBM regressors on varying fractions of genotypes, evaluate held-out RMSD, and use SHAP values to identify both global mutation importance and genotype-dependent effects.
- **Infer family-level evolutionary constraints:** Build a PF13354 multiple-sequence alignment, fit a DCA Potts model, calculate conditional effective alphabets and sequence Hamiltonians, and test whether experimental fitness aligns with natural β-lactamase sequence constraints.
- **Map functional sequence space:** Train a two-dimensional VAE on the family alignment, decode a grid of latent sequences, assign Hamiltonian scores, and locate TEM-1CML variants and high-fitness variants within the resulting latent generative landscape.

## Key Biology Insights

- **Functional novelty exposes hidden epistasis.** Mutations that appear neutral or deleterious alone can become strongly beneficial when combined in the correct background, especially for a substrate the wild-type enzyme poorly hydrolyzes.
- **Resistance mutations are not independent parts.** E104K, substitutions at R164, and E240K are major contributors to aztreonam resistance, but their effects depend on one another and on residues such as A237, G238, and R244.
- **R244 appears central to maintaining activity.** R244C/S generally reduced fitness under both antibiotics, and retaining wild-type R244 was the strongest SHAP-associated positive feature.
- **Native function can coexist with expanded specificity.** Many variants with high aztreonam fitness retained high ampicillin fitness, so acquisition of extended-spectrum activity does not necessarily impose a trade-off for this antibiotic pair.
- **Evolution remains constrained despite many possible paths.** Highly resistant genotypes preferentially preserve sequence couplings seen across natural β-lactamases, implying that broad substrate activity must be acquired within a restricted biophysical background.
- **Drug concentration changes evolutionary accessibility.** The number and prominence of fitness peaks under aztreonam changed non-monotonically with dose, suggesting that treatment intensity can alter which resistance routes are accessible rather than merely scaling selection strength.

## Implications

- Predicting resistance to a new antibiotic from single mutations or pairwise scans alone may fail because clinically relevant phenotypes can depend on fifth-order or higher interactions.
- Experimental designs should combine low-order mutants with strategically chosen combinatorial variants, potentially prioritized by evolutionary sequence models, instead of attempting exhaustive stepwise reconstruction in larger proteins.
- Drug-development risk assessment could compare a candidate β-lactam against combinatorial resistance landscapes to estimate the number, accessibility, and robustness of evolutionary escape routes.
- Graph-informed treatment or drug-design strategies might seek mutations or chemical constraints that block committed paths to high-fitness peaks, although this proposal remains a future application rather than a demonstrated clinical intervention.
- The pooled assay can be influenced by β-lactamase-producing cells protecting less-active “cheater” variants. The AUC-based metric reduces but does not eliminate this concern, and the library was restricted to preselected clinical substitutions; therefore, the results do not represent the complete mutational landscape of TEM-1.
- The work is a preprint, the full landscape has no public data accession specified, and the reported 10%-training aztreonam RMSD differs between the Results and Figure 7 caption. These issues should be resolved before relying on exact quantitative forecasts.
