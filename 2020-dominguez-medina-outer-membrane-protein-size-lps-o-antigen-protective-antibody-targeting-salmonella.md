# Paper Summary

### Authors

C. Coral Domínguez-Medina, Marisol Pérez-Toledo, Anna E. Schager, Jennifer L. Marshall, Charlotte N. Cook, Saeeda Bobat, Hyea Hwang, Byeong Jae Chun, Erin Logan, Jack A. Bryant, Will M. Channell, Faye C. Morris, Sian E. Jossi, Areej Alshayea, Amanda E. Rossiter, Paul A. Barrow, William G. Horsnell, Calman A. MacLennan, Ian R. Henderson, Jeremy H. Lakey, James C. Gumbart, Constantino López-Macías, Vassiliy N. Bavro, and Adam F. Cunningham.

### Journal

Nature Communications, 11, article 851.

### Publication Date

2020-02-12.

### DOI

[10.1038/s41467-020-14655-9](https://doi.org/10.1038/s41467-020-14655-9)

## Keywords

Salmonella; invasive nontyphoidal salmonellosis; OmpD; OmpA; lipopolysaccharide; O-antigen; antibody accessibility; serum bactericidal activity; molecular dynamics; vaccine design.

## Main Idea

Protective antibody recognition of a Gram-negative bacterial surface protein is determined by the interaction between the protein and its surrounding LPS O-antigen. Immunization with the trimeric porin OmpD from *Salmonella enterica* serovar Typhimurium (STm) protected mice against STm, but provided only minimal protection against the closely related *S. Enteritidis* (SEn). The authors attribute this to two coupled features: the OmpD trimer creates an O-antigen tunnel large enough for one IgG Fab, while the chemical and physical structure of the native O-antigen controls which OmpD epitopes are exposed.

## Evidence Supporting the Main Idea

- Two doses of 20 micrograms purified STmOmpD reduced median STm burdens by at least 100-fold in liver and spleen and nearly 10,000-fold in blood after challenge with invasive African isolate D23580 (Fig. 1b). Comparable protection was observed against laboratory strain SL1344.
- Anti-STmOmpD serum promoted opsonization-dependent reduction of bacterial numbers and complement-dependent killing in serum bactericidal assays (Fig. 1c,d). Similar protection with OmpD purified from a strain lacking OmpF, OmpC, and O-antigen argued against residual O-antigen as the main explanation.
- STmOmpD and SEnOmpD differ at only one residue, A263S, and anti-STmOmpD serum bound purified porins from both serovars. Nevertheless, STmOmpD immunization reduced STm burdens by about 100-fold but reduced SEn burdens by less than fivefold (Fig. 2b,c).
- Removing O-antigen with a *wbaP* mutation made SEn bacteria bind anti-STmOmpD antibody more strongly and become susceptible to antibody-mediated killing and protection (Fig. 3). This indicates that O-antigen masks conserved epitopes on OmpD.
- Molecular dynamics simulations showed that the OmpD trimer is approximately 70 Å across, compared with approximately 50 Å for the shortest dimension of a Fab. The resulting O-antigen channel can accommodate one Fab at a time; an IgG steered-MD simulation supported access to OmpD loops but not simultaneous access for two Fabs (Fig. 4).
- Swapping the O-antigens between STm (O:4) and SEn (O:9) reduced antibody binding, bactericidal activity, and protection. Reciprocal OmpD mutants similarly showed that optimal protection requires matching OmpD and native O-antigen (Fig. 5 and Supplementary Fig. 5).
- OmpA, a similarly sized but monomeric outer-membrane protein, generated a footprint too small for ready Fab access through the LPS layer. Although infection and OmpA immunization induced anti-OmpA responses, anti-OmpA antibody bound intact bacteria weakly and did not protect mice (Fig. 6).

## Main Novelty

The study links protective antibody function to the three-dimensional footprint of an outer-membrane antigen within the native LPS layer. It shows that a nearly identical protein antigen can have different vaccine value because a single protein substitution and a different O-antigen jointly alter epitope presentation. This provides a structural explanation for antigenic diversity and suggests that protein-antigen selection for vaccines should account for the antigen's oligomeric geometry and serovar-specific LPS environment.

## Datasets Used for Evaluation

- **STm D23580:** invasive African *S. Typhimurium* isolate; used for mouse challenge, whole-cell ELISA, and serum bactericidal assays. Challenge doses included 1 × 10^5 or 5 × 10^5 CFU, depending on the experiment.
- **STm SL1344 / SL3261:** laboratory *S. Typhimurium* strains, including an attenuated *aroA* mutant; used for antibody binding, challenge, opsonization, and bactericidal assays.
- **SEn D24954 / P12510:** invasive or attenuated *S. Enteritidis* strains; used to measure cross-protection and antibody activity.
- **O-antigen-deficient (*wbaP−*) STm and SEn mutants:** rough derivatives lacking O-antigen; used to test whether O-antigen shielding limits OmpD accessibility.
- **O-antigen chimera strains:** STm expressing O:9 and SEn expressing O:4; used to separate the effects of O-antigen chemistry from the OmpD sequence.
- **OmpD reciprocal mutants:** STm OmpD A263S and SEn OmpD S263A; used to test whether the A263S polymorphism and O-antigen must be matched.
- **Structural and simulation systems:** homology models of OmpD and OmpA in explicit STm and SEn outer membranes; four atomistic membrane systems were simulated for 2 microseconds each, plus a 70-nanosecond steered simulation with full murine IgG1.

Exact per-group mouse sample sizes are not consistently stated in the figure legends; plotted points represent individual mice where indicated. Source data for the reported figures and supplementary figures were provided by the authors.

## Experimental Procedure

- Purified STmOmpD, with or without O-antigen-deficient purification controls, and purified OmpA; immunized wild-type mice with 20 micrograms, generally in two doses, and collected immune sera.
- Measured serum IgG binding to intact bacteria and purified porins by ELISA.
- Challenged immunized and control mice intraperitoneally with STm, SEn, mutants, or O-antigen chimeras; enumerated bacterial burdens in liver, spleen, and blood.
- Tested antibody-mediated opsonization and complement-dependent killing using mouse serum plus antibody-depleted human serum as a complement source.
- Compared wild-type, O-antigen-deficient, reciprocal OmpD, and O-antigen-swapped strains to identify the contributions of protein sequence and LPS structure.
- Aligned OmpD sequences, mapped residue 263 onto an OmpD trimer model, and compared the dimensions of OmpD, OmpA, Fab, and IgG.
- Simulated OmpD-containing outer membranes with explicit LPS using NAMD/AMBER and the CHARMM36 force field; analyzed O-antigen motion, protein-LPS contacts, channel accessibility, and IgG approach.
- Used nonparametric Mann–Whitney U tests for group comparisons and serum bactericidal differences.

## Key Biology Insights

- O-antigen is not merely a general steric shield: its sugar composition and dynamics can alter how neighboring protein epitopes are presented.
- OmpD trimerization creates a sufficiently wide local opening for antibody access, whereas the smaller footprint of monomeric OmpA is largely occluded.
- O-antigen shielding concentrates immune pressure on a limited subset of exposed OmpD epitopes, including the region around residue 263.
- The chemical pairing of OmpD and O-antigen can preserve serovar-specific immune recognition even when the protein itself is highly conserved.
- A single Fab binding through an O-antigen channel can nevertheless support complement-dependent bacterial killing.

## Implications

For Gram-negative vaccine design, conserved protein sequence alone is an inadequate predictor of cross-serovar protection. Candidate antigens should be evaluated in their native oligomeric and LPS context, including the size of the access footprint and compatibility between the antigen and the target serovar's O-antigen. The authors propose that O-antigen shielding can increase combinatorial antigenic diversity while reducing the need for bacteria to accumulate protein mutations that may carry fitness costs. The conclusions are constrained by the limited time and sampling of molecular simulations and by the difficulty of reproducing the full bacterial surface environment in silico; the paper also notes that a minor contribution from co-purifying core LPS antibodies cannot be absolutely excluded.

Source: [Nature Communications article](https://www.nature.com/articles/s41467-020-14655-9).
