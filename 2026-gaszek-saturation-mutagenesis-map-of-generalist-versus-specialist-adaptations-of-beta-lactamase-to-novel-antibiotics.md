# Paper Summary

**Paper:** Saturation mutagenesis map of generalist versus specialist adaptations of β-lactamase to novel antibiotics  
**Source:** [bioRxiv preprint, version 2](https://www.biorxiv.org/content/10.1101/2025.10.14.682469v2)  
**Peer-review status:** Preprint; not certified by peer review

### Authors

Ilona K. Gaszek; Muhammed S. Yildiz; Levent Sari; Ayesha Ahmed; Erdal Toprak; Milo M. Lin

### Journal

bioRxiv (preprint)

### Publication Date

February 28, 2026 (version 2)

### DOI

[10.1101/2025.10.14.682469](https://doi.org/10.1101/2025.10.14.682469)

## Keywords

- TEM-1 β-lactamase
- Antibiotic resistance
- Saturation mutagenesis
- Generalist and specialist mutations
- β-lactam antibiotics
- Ceftazidime
- Ampicillin
- Cephalosporins
- Monobactams
- Extended-spectrum β-lactamase (ESBL)
- Ω-loop
- E166P
- Molecular dynamics
- Alternative catalysis

## Main Idea

Single amino-acid substitutions in TEM-1 β-lactamase follow two contrasting adaptive patterns. **Generalist mutations**, which increase resistance to multiple β-lactam antibiotics, are structurally predictable and confined to three active-site-associated positions: R164, G238, and E240. **Specialist mutations**, which benefit only one tested antibiotic, occupy a much broader and less predictable set of positions.

Ceftazidime produced the widest range of specialist solutions. The most unexpected was E166P: replacing a highly conserved catalytic glutamate largely abolished native ampicillin resistance but increased ceftazidime resistance. Experiments show only partial removal of ceftazidime from culture, while simulations and follow-up mutagenesis implicate a reorganized K73–N132 interaction network. The data therefore support a ceftazidime-specific alternative or slow catalytic/sequestration mechanism, but they do not directly establish the chemical deacylation step.

## Evidence Supporting the Main Idea

### Direct experimental observations

- **Protein-wide single-mutant screen:** Every position in mature TEM-1, residues 26–290, was substituted with all possible amino acids on low-copy pBR322 and screened in *Escherichia coli* NEB10β. This design nominally spans approximately 5,035 nonsynonymous single-amino-acid substitutions (265 positions × 19 alternatives), although the paper does not report the exact number of variants successfully quantified.
- **Six-antibiotic selection panel:** Triplicate pooled libraries were challenged with ampicillin; the cephalosporins ceftazidime, cefotaxime, ceftriaxone, and cefepime; and the monobactam aztreonam. Carbapenems were screened initially, but the library did not show increased resistance to meropenem or imipenem (Supplementary Figure 1).
- **Stringent enrichment criterion:** Mutations were called beneficial when enrichment exceeded log₂ fold change 3 (approximately eightfold) with false-discovery-rate-adjusted significance below 0.05; a stricter adjusted p-value below 0.01 was also used in the Results discussion (Figure 1C).
- **Only three generalist positions:** All mutations benefiting at least two antibiotics localized to R164, G238, or E240. Figure 2C shows multiple effective substitutions at each site, including known clinical changes and less commonly observed alternatives such as R164N, G238C/A, and E240Q/H.
- **Generalist mechanism is structurally coherent:** R164 substitutions disrupt the R164–D179 salt bridge and increase Ω-loop flexibility; G238 and E240 lie at the active-site edge and influence accommodation of bulky β-lactam side chains (Figure 2A). These mechanisms are interpretations supported by prior structural work rather than directly measured in this study.
- **Specialists are structurally dispersed:** Specialist positions appeared in the active site, Ω-loop, protein periphery, and distant structural regions. Ampicillin yielded only three modest specialists (R120S, S258D, and T114G), consistent with TEM-1 already being optimized for penicillin hydrolysis (Figure 2B–C).
- **Ceftazidime had the greatest specialist diversity:** Numerous ceftazidime-only substitutions clustered in and around the Ω-loop, including multiple replacements at E166 and neighboring residues. Cefepime and one of the two other cephalosporin conditions yielded no specialist mutations meeting the threshold; the paper's CFX/CTX labels are inconsistent, so the exact cefotaxime-versus-ceftriaxone assignment should be checked against source data before reuse.
- **E166 substitutions create a strong trade-off:** Wild-type TEM-1 had an ampicillin MIC of approximately 30,000 µg/mL. E166D, E166G, E166H, and E166P reduced this to approximately 4.57–13.72 µg/mL, a three- to four-log loss. Against ceftazidime, wild type had MIC 1.33 µg/mL; E166D/G/H reached 4 µg/mL, and E166P reached 12 µg/mL (Figure 3A–B; Table 1).
- **E166P did not broadly improve resistance:** The tested E166 variants did not significantly improve aztreonam, cefepime, cefotaxime, or ceftriaxone resistance, supporting classification as ceftazidime specialists.
- **Indirect activity assay indicates incomplete drug removal:** After primary exposure, E166P increased apparent ceftazidime tolerance eightfold. Sensitive cells subsequently grown in filtered E166P-conditioned supernatant showed a fourfold MIC increase, but their growth remained restricted. R164N-conditioned supernatant supported robust growth across all tested concentrations (Figure 3C–D). Thus, E166P caused partial loss of free ceftazidime, consistent with slow hydrolysis or sequestration rather than robust degradation.
- **Simulations identify altered active-site organization:** In three 1-µs simulations per protein, water occurred within 3.5 Å of ceftazidime C6 in 63.6% of wild-type and 63.2% of E166P frames. K73-associated coordination fell from 55.8% to 47.9%, N132 remained near 9.8–9.9%, and N170-associated coordination rose from 18.2% to 42.5% (Figure 4A–C).
- **N132 and K73 are functionally required:** K73A strongly impaired both native and E166P backgrounds. N132A retained substantial ampicillin resistance but lost ceftazidime activity; the N132A/E166P double mutant lost E166P-mediated ceftazidime resistance (Figure 4D–E). E168A and N170A did not abolish E166P resistance when tested in the relevant combinations (Supplementary Figure 5).

### Authors' interpretation

- Broad resistance is accessible through a small, predictable set of active-site control points that improve accommodation of multiple bulky substrates.
- Specialist resistance has a larger and more idiosyncratic solution space because a mutation need only solve the structural problem posed by one antibiotic.
- In E166P, loss of the canonical E166 general base reorganizes K73 toward N132, potentially supporting ceftazidime positioning and a slower, noncanonical route to deacylation.
- Because the indirect assay cannot distinguish hydrolysis from stable acyl-enzyme sequestration, the proposed alternative catalytic chemistry remains a mechanistic hypothesis rather than a direct biochemical demonstration.

## Main Novelty

- The study systematically classifies protein-wide TEM-1 single substitutions as **generalists** or **specialists** across six chemically diverse β-lactam antibiotics rather than testing resistance under only one or two drugs.
- It shows a sharp structural asymmetry: generalist substitutions are confined to three positions, while specialist substitutions are distributed broadly and depend strongly on the selected antibiotic.
- It identifies numerous experimentally potent substitutions that are rare or absent clinically, illustrating how nucleotide accessibility and multi-mutation context narrow the evolutionary outcomes observed in patients.
- It provides a focused mechanistic analysis of E166P, a ceftazidime specialist at a residue normally considered indispensable for class A β-lactamase deacylation.
- It combines saturation mutagenesis, enrichment sequencing, MIC validation, an indirect antibiotic-removal assay, molecular dynamics, and targeted second-site mutations to connect evolutionary screening with a testable molecular mechanism.

## Datasets Used for Evaluation

### 1. TEM-1 saturation mutagenesis library

- **Content:** Single amino-acid substitutions across mature TEM-1 residues 26–290, divided into ten positional sublibraries.
- **Nominal size:** Approximately **5,035 nonsynonymous variants** based on 265 positions × 19 alternative residues; exact recovered coverage and per-variant read depth are **not specified in the paper**.
- **Vector and host:** Constitutive TEM-1 expression from low-copy pBR322 in *E. coli* NEB10β.
- **Replication:** Three independently pooled biological libraries; each sublibrary transformation exceeded 10⁶ CFU/mL.
- **Origin:** Library construction was previously described by Stiffler and colleagues.

### 2. Six-antibiotic deep-mutational selection dataset

- **Content:** Variant read counts and treated-versus-untreated enrichment for ampicillin, ceftazidime, cefotaxime, ceftriaxone, cefepime, and aztreonam.
- **Selected sequencing concentrations:** Ampicillin 4,096 µg/mL; ceftazidime 1 µg/mL; cefotaxime 0.25 µg/mL; ceftriaxone 0.25 µg/mL; cefepime 1 µg/mL; aztreonam 0.5 µg/mL; plus no-drug controls.
- **Replication:** Three biological replicates, with paired treated and untreated comparisons.
- **Read processing:** Paired-end 2 × 150-bp reads; reads with more than one amino-acid change were discarded; counts were collapsed by amino-acid substitution.
- **Public availability:** A data repository or accession for the enrichment matrices is **not specified in the paper**.

### 3. β-lactam MIC validation dataset

- **Content:** MICs for wild-type TEM-1, selected E166 variants, control strains, and targeted second-site combinations across multiple β-lactams.
- **Replication:** Biological replicates with three technical replicates each; MICs reported as medians with bootstrap 95% confidence intervals.
- **Key comparisons:** E166D/G/H/P; E166P with K73A, N132A, E168A, and N170A backgrounds; R164N positive control.

### 4. Indirect ceftazidime-removal dataset

- **Content:** Growth of four primary strains across 0–32 µg/mL ceftazidime for 9 hours, followed by growth of ceftazidime-sensitive *E. coli* for 16 hours in filtered conditioned supernatants at concentrations up to 8 µg/mL.
- **Strains:** Sensitive NEB10β, wild-type TEM-1, E166P, and R164N.
- **Replication:** Three replicates per condition.

### 5. Molecular-dynamics dataset

- **Content:** Acyl-enzyme models of ceftazidime-bound wild-type TEM-1 and E166P, constructed from PDB 1BTL and ceftazidime-bound KPC-2 PDB 6Z24.
- **Sampling:** Three independent **1-µs production simulations per protein**, following energy minimization and two 5-ns equilibration stages.
- **Analysis:** Protein RMSD/RMSF and frequency of water molecules simultaneously within 3.5 Å of ceftazidime C6 and active-site atoms from K73, N132, E166/P166, or N170.
- **Trajectory availability:** A public trajectory or code archive is **not specified in the paper**.

## Experimental Procedure

- **Prepare the library:** Transform ten TEM-1 positional saturation-mutagenesis sublibraries separately into *E. coli* NEB10β, pool them at equal OD600, and establish three biological replicate libraries.
- **Identify selectable antibiotics:** Compare pooled-library, wild-type TEM-1, and sensitive-host MIC profiles across penicillins, cephalosporins, monobactams, and carbapenems; exclude carbapenems because the library showed no increased resistance.
- **Run pooled selections:** Grow each library over concentration gradients for six antibiotics in 96-well plates for 18 hours, with wild-type TEM-1 and no-drug controls.
- **Choose bottleneck doses:** Select concentrations where wild type no longer protects cells but resistant library members still grow; expand surviving cells briefly without β-lactam to obtain sufficient plasmid DNA.
- **Sequence variants:** Amplify TEM-1, perform paired-end Illumina sequencing, align reads to the plasmid reference, discard reads with multiple amino-acid changes, and count each single substitution.
- **Calculate enrichment:** Normalize counts to within-sample frequencies, add a 0.1 pseudocount for zero values, compute treated-versus-untreated log enrichment, and compare each mutant with the median synonymous wild-type baseline using paired t-tests and Benjamini–Hochberg correction.
- **Classify adaptations:** Define significant beneficial substitutions as log₂ fold change above 3 with adjusted p below 0.05; call a mutation generalist if significant for at least two antibiotics and specialist if significant for exactly one.
- **Validate E166 variants:** Engineer selected E166 substitutions individually and measure MICs against the antibiotic panel after 20 hours.
- **Test ceftazidime removal:** Incubate wild type, E166P, R164N, and sensitive control cells with ceftazidime; filter supernatants; then use sensitive *E. coli* growth to estimate residual antibiotic activity.
- **Model the acyl-enzyme state:** Covalently place ceftazidime on S70 in wild-type and E166P TEM-1 models, solvate and equilibrate each system, and run triplicate 1-µs molecular-dynamics simulations.
- **Analyze catalytic-water geometry:** Quantify water bridging between ceftazidime C6 and K73, N132, E166, or N170 with a 3.5-Å cutoff.
- **Perturb the proposed network:** Introduce K73A, N132A, E168A, and N170A in wild-type or E166P backgrounds and use ampicillin and ceftazidime MICs to test which residues are required for the specialist phenotype.

## Key Biology Insights

- **Broad-spectrum adaptation has a narrow structural gateway.** Multiple amino-acid identities can work, but generalist resistance repeatedly uses R164, G238, or E240 because these sites control Ω-loop flexibility and substrate accommodation.
- **Observed clinical evolution is a subset of biochemical possibility.** R164N performs strongly in the laboratory but requires two nucleotide changes, whereas clinically common R164S is accessible through one; mutational accessibility therefore helps explain why equally effective amino-acid variants differ in prevalence.
- **Specialization can repurpose conserved catalytic architecture.** E166P sacrifices penicillin activity yet creates moderate ceftazidime resistance, showing that a residue essential to the ancestral mechanism can become an innovation point under a different substrate.
- **N132 is central to cephalosporin function.** Its removal abolishes ceftazidime resistance in both wild-type and E166P contexts, consistent with a role in substrate/transition-state positioning.
- **E166P is much weaker than canonical ESBL solutions.** The indirect assay shows residual antibiotic after E166P treatment, whereas R164N efficiently removes ceftazidime; the specialist phenotype may reflect slow turnover, sequestration, or both.
- **Single substitutions reveal entry points, not complete clinical ESBL phenotypes.** Clinical extended-spectrum enzymes commonly contain two to five mutations whose cooperative effects can overcome limitations of isolated changes.

## Implications

- Drug sequences or combinations that alternate structurally distinct β-lactams may penalize narrow specialists such as E166P, whereas prolonged dominance of one antibiotic could favor them. This is a testable evolutionary-treatment hypothesis, not a clinical recommendation established by this study.
- Surveillance limited to common clinical substitutions may miss rare but biochemically accessible resistance routes, especially at conserved residues thought to be immutable.
- Generalist hotspots offer compact targets for prospective resistance monitoring, while specialist prediction requires broader protein-wide screening.
- Designing antibiotics that force resistance through specialist mutations with severe trade-offs could reduce cross-resistance, but clinical benefit would depend on mutation supply, compensatory evolution, pharmacology, and pathogen context.
- Important limitations are the use of a single-mutant library, pooled enrichment rather than direct kinetics for most variants, an indirect assay that cannot separate hydrolysis from sequestration, no public data/code accession, and inconsistent CFX/CTX antibiotic labeling in the text and Figure 2 caption.
