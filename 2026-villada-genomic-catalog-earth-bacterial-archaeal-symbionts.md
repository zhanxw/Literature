# Paper Summary

### Authors

Juan C. Villada, Yumary M. Vasquez, Gitta Szabó, Ewan Whittaker-Walker, Miguel F. Romero, Sarina Qin, Neha Varghese, Emiley A. Eloe-Fadrosh, Nikos C. Kyrpides, SymGs data consortium, Axel Visel, Tanja Woyke and Frederik Schulz.

### Journal

Nature Biotechnology

### Publication Date

31 August 2026 (published online)

### DOI

[10.1038/s41587-026-03213-1](https://doi.org/10.1038/s41587-026-03213-1)

## Keywords

Microbial symbiosis; metagenome-assembled genomes; single amplified genomes; genome-resolved metagenomics; machine learning; symclatron; SymGs; host dependence; genome reduction; metabolic specialization.

## Main Idea

The authors developed symclatron, an interpretable machine-learning framework that predicts whether bacterial and archaeal genomes are free-living, host-associated or obligately intracellular from genomic gene-content signatures. Applying it to a dereplicated catalog of 107,067 genomes produced SymGs, a set of 14,070 high-confidence predicted symbiont genomes. The catalog suggests that symbiotic lifestyles are widespread and account for approximately 15–23% of sampled uncultivated microbial diversity, depending on the catalog and confidence definition.

The predictions are provisional: they indicate genomic evidence for a stable, close host association, not direct proof of a particular host or interaction. The paper excludes generic syntrophy or diffusible cross-feeding without evidence of a specific, persistent host association.

## Evidence Supporting the Main Idea

- The manually curated training set contained 6,751 genomes: 5,959 free-living, 409 host-associated and 383 obligately intracellular. The authors also assembled 792 curated symbiont proteomes into 20,063 orthogroup HMMs.
- Symclatron was evaluated with leave-one-clade-out validation across 11,025 clades and taxonomic ranks from species to phylum, testing generalization to lineages withheld from training.
- In the held-out benchmark, one-versus-all ROC AUC values were 0.99 for free-living, 0.98 for host-associated and 1.00 for obligately intracellular genomes (Fig. 1g). Overall accuracy was 96%; class-specific F1 values were 0.982, 0.699 and 0.908, respectively (Fig. 1h).
- The confidence threshold used for the SymGs catalog was 0.725. At this threshold, the reported false-positive rate was 1.5% among incorrect predictions. Confidence was highest for familiar lineages; in the most phylogenetically distant validation quintile, accuracy declined from 94.1% to 72.7%, with the largest loss for host-associated genomes (Extended Data Fig. 1).
- The final 14,070 SymGs represented 14% of the 107,067-genome catalog, had median completeness above 90% and typically less than 0.2% contamination (Fig. 2e).
- Symbiont predictions were distributed across nearly all major bacterial phyla and multiple archaeal lineages. Candidate Phyla Radiation/Patescibacterota and DPANN archaea were especially enriched for host-dependent organisms, whereas symbionts formed smaller subsets in large phyla such as Pseudomonadota and Actinomycetota (Figs. 3–5).
- Functional interpretation found loss or incompleteness of core biosynthetic pathways, especially amino-acid synthesis, alongside enrichment or retention of transport, membrane and host-exchange functions. In selected symbiont-exclusive clades, nitrogen and sulfur metabolism modules were retained or more complete than in free-living relatives (Fig. 6; Extended Data Figs. 3–5).

## Main Novelty

This work combines expert lifestyle curation, symbiont-derived protein HMMs, clade-held-out validation and a confidence-calibrated neural network to infer host dependence at global metagenomic scale. It provides both a reusable predictor (symclatron) and a genome resource (SymGs), extending symbiosis surveys beyond cultured organisms and previously characterized host associations.

## Datasets Used for Evaluation

- **Curated training/benchmark genomes:** 6,751 IMG/M genomes, sampled at one or two genomes per genus and manually labeled as 5,959 free-living, 409 host-associated or 383 obligately intracellular. Each genome was also artificially reduced to 50–90% completeness with 10, 30 or 50 kb fragmentation lengths to test incomplete assemblies.
- **Curated symbiont proteomes:** 792 proteomes spanning major bacterial and archaeal clades; 1,642,823 proteins were used to infer 20,063 orthogroups/HMMs for feature extraction.
- **NeLLi2023 environmental catalog:** Bins from 31,152 IMG/M environmental sequencing projects, including 5,635,662 initial bins. After quality filtering and dereplication, the genome catalog contained 107,067 bacterial and archaeal genomes/bins.
- **Reference genomes:** Approximately 116,000 IMG/M isolate/reference genomes and 85,205 GTDB representative genomes were incorporated before quality control and dereplication.
- **SymGs:** The high-confidence subset of 14,070 genomes from the 107,067-genome catalog; it was used for taxonomic, biome and metabolic analyses rather than as an independent ground-truth set.

## Experimental Procedure

- Define three lifestyle labels along a host-dependence continuum and manually curate the 6,751-genome reference set from primary literature and expert knowledge.
- Infer orthogroups from the 792 curated symbiont proteomes, align and trim them, and build 20,063 profile HMMs.
- Call genes uniformly, scan proteins against the HMM library, and represent each genome by a 20,063-dimensional bitscore vector.
- Train an XGBoost classifier (symcla) and regressor (symreg), retaining the 1,000 most relevant features for each model.
- Repeatedly withhold complete clades at species, genus, family, order, class and phylum levels; use the resulting out-of-fold class probabilities, continuous symbiosis score, distances to training data and genome completeness as seven inputs to a feedforward neural network.
- Calibrate the final symclatron confidence score and evaluate performance on a stratified 80:20 split of 482,250 out-of-fold proteome evaluations.
- Construct the NeLLi2023 catalog from metagenomic bins, IMG/M and GTDB genomes; apply CheckM/CheckM2 quality control, UNI56 marker checks, GTDB-Tk taxonomy and 95% ANI dereplication.
- Run symclatron on the 107,067-genome catalog and retain predictions with confidence ≥0.725 as SymGs.
- Analyze taxonomic and biome distributions, use SHAP with KEGG/COG/Pfam/GO annotations to interpret model features, and compare KEGG metabolic-module completeness between symbiont-exclusive clades and free-living sister clades using bootstrap confidence intervals.

## Key Biology Insights

- Host dependence is likely much more common across environmental microbial diversity than culture-based genome collections suggest.
- Symbiotic lifestyles recur across distant bacterial and archaeal lineages, implying repeated evolutionary transitions rather than confinement to a few canonical symbiont groups.
- Genome reduction is accompanied by metabolic complementarity: symbionts often lose amino-acid and other biosynthetic capacities while retaining functions likely to support exchange with hosts.
- The retained metabolic repertoire is lineage- and habitat-specific. For example, Thioglobaceae symbionts retain nitrogen and sulfur metabolism modules that could supplement host nutrition or support energy generation in anoxic, sulfur-rich environments.
- Symclatron recovered known cases, including intracellular Azoamicus, DPANN-associated archaeal symbionts and the deeply branching archaeal symbiont Candidatus Sukunaarchaeum mirabile, despite limited archaeal representation in the training set.

## Implications

SymGs offers a starting point for discovering uncultivated symbionts, prioritizing host-association experiments and investigating metabolic division of labor. Symclatron’s interpretable features and confidence scores may also guide synthetic-community design, minimal-genome engineering, enzyme discovery and biogeochemical studies.

The main limitations are important for reuse: predictions are not direct evidence of a host or interaction; training labels are biased toward characterized lineages and especially bacterial symbionts of eukaryotes; performance drops for the most distant lineages, particularly host-associated ones; and the obligately intracellular class was defined conservatively. The authors recommend treating low-confidence or phylogenetically distant predictions as hypotheses requiring ecological, genomic and experimental confirmation.

Source: [Villada et al., Nature Biotechnology](https://www.nature.com/articles/s41587-026-03213-1)
