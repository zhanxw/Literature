# Paper Summary

**Title:** Antisense transcription reveals disease-associated adaptations in the human gut microbiome

### Authors
Marie-Madlen Pust, Ahmed M. T. Mohamed, Martin Stražar, Aranzazu Arias-Rojas, Edward Cunningham-Oakes, Eric M. Brown, Amanda Bumber, Gleb Pishchany, Chenhao Li, Ashwin N. Ananthakrishnan, Alistair C. Darby, Hera Vlamakis, Damian R. Plichta, and Ramnik J. Xavier.

### Journal
Nature Microbiology, volume 11, pages 2464-2477 (2026).

### Publication Date
Published online August 10, 2026; September 2026 issue.

### DOI
[10.1038/s41564-026-02442-z](https://doi.org/10.1038/s41564-026-02442-z)

## Keywords
Antisense RNA; metastrand; strand-aware metatranscriptomics; inflammatory bowel disease; insertion sequence elements; microbial adaptation; transposition; oxidative stress.

## Main Idea
The metastrand framework separates microbial sense and antisense transcription using paired metatranscriptomic and metagenomic data. Antisense programs converge during active inflammatory bowel disease (IBD), track inflammatory and metabolic states, and reveal transcriptional changes in mobile insertion sequence elements (ISEs) carrying adaptive functions. Human comparisons, experimental colitis, and bacterial stress experiments link shifts toward sense transcription to subsequent genomic repositioning; direct causality and the molecular mechanisms of antisense control remain unproven (Figs. 1-6; Discussion).

## Evidence Supporting the Main Idea
- **Ignoring strand loses biological information:** Antisense reads represented approximately 10% of mapped reads (SD 6%), yet at least one-third of differential-expression calls at FDR thresholds below 0.25 were antisense-driven. Across evaluated thresholds, 3,632-4,305 antisense-derived differentially expressed genes (DEGs) were detected, and 261-651 genes were misclassified as mRNA-derived by unstranded analysis. Relative to sense-derived calls, unstranded F1 remained below 0.5 at FDR <0.05; this comparison uses sense-derived calls as a reference, supplemented by simulations with known ground truth (Fig. 1; Extended Data Fig. 2).
- **Inflammatory activity explains antisense structure:** After controlling for cohort, subject identity, and species abundance, constrained ordination retained an association between disease activity and species-level antisense profiles (P = 0.017). Profiles converged in active IBD across diverse taxa; severity separation along the first constrained axis had P = 3.44 × 10^-10. In the broader variance partitioning, inflammatory activity explained about 2% of variation, so the association is not the sole driver of microbiome variability (Fig. 2; Results).
- **Metabolite-linked transcription:** Opposing sense/antisense shifts involved Bilophila wadsworthia ydfG, NAD+ kinase, serine/lactate metabolism, and citrate synthase. Fecal serine and lactate correlated positively with calprotectin (r = 0.66 and 0.46), whereas citrate correlated negatively (r = -0.44). These associations connect transcriptional programs to the inflammatory nutrient environment without establishing metabolite flux or production source (Fig. 3).
- **Mobile-element signatures:** Replication/recombination/repair functions were overrepresented among antisense DEGs, with many originating from ISEs. IS3, IS21, IS256, and IS200/IS605 shifted toward sense transcription in active IBD and carried comparatively diverse passenger functions, including resistance, stress response, nutrient utilization, and host-substrate degradation (Fig. 4).
- **Experimental colitis:** DSS-treated mice showed reduced antisense and increased sense transcription in several functionally diverse ISE families. IS21 and IS3 had greater changes in flanking genomic sequences than controls, consistent with repositioning; stable taxonomic distributions argued against species turnover, although strain turnover remained an alternative (Fig. 5; Results).
- **Within-strain temporal evidence:** In five H2O2-exposed E. coli K12 cultures, IS3 transcription shifted toward sense by about 20 minutes, preceding detected repositioning. Mobilization increased across time (Kruskal-Wallis P approximately 0.0003), reaching approximately 2.7-fold higher levels at 24 hours than at 60 minutes. Untreated cultures showed little movement. This supports temporal directionality, but no targeted antisense perturbation established a causal regulatory mechanism (Fig. 6; Discussion).
- **Context-dependent external replication:** INTEGRATE gastroenteritis data showed higher sense-to-antisense ratios for functionally diverse versus selfish ISE families in E. coli and viral infection groups; C. jejuni showed no significant difference. Healthy MLVS participants had comparatively stable ISE transcription, demonstrating that the pattern is not universal across infections or physiological states (Extended Data Fig. 10).

## Main Novelty
Metastrand brings gene-level antisense quantification, technical strand-leakage filtering, and DNA-abundance normalization into community metatranscriptomics. The biological advance is connecting inflammation-associated antisense programs with mobile elements carrying adaptive functions, supported by human multi-omics, comparative isolate genomics, a mouse model, and a controlled within-strain time course (Figs. 1, 4-6).

## Datasets Used for Evaluation
| Dataset | Contents and sample size | Role |
|---|---|---|
| IBD discovery cohorts (dataset 1a) | 295 paired stool metagenomic/metatranscriptomic profiles from 156 people: 82 CD, 29 UC, and 45 healthy controls. Samples: 125 active IBD, 80 remission, and 90 healthy. Cohort resources include RISK, STiNKi, PRISM, and PRISM-LSS. | Discover strand-specific inflammatory signatures and evaluate unstranded versus strand-aware analyses. |
| Matched metabolomics (dataset 1b) | 64 cross-sectional LC-MS profiles matched to dataset 1a; Extended Data Fig. 1 identifies 64 patients. | Relate enzyme transcription, metabolites, and calprotectin. |
| Longitudinal stability subset | 35 samples from six healthy participants; 47 from seven patients in sustained remission; 43 from six patients transitioning between activity and remission. | Test within-person stability and changes across disease states (Fig. 4a). |
| INTEGRATE (dataset 2a) | 970 paired stool metagenomic/metatranscriptomic datasets from UK gastroenteritis cases, spanning bacterial, viral, and protozoal infections. Unique participant count for the analyzed set: **Not specified in paper**. | Assess ISE transcription beyond IBD, including age/sex-matched pathogen comparisons. |
| Men's Lifestyle Validation Study, MLVS (dataset 2b) | 342 paired metagenomic/metatranscriptomic samples from 96 healthy men. | External healthy longitudinal comparison. |
| Clinical isolate genomes (dataset 3a) | 509 genomes from Bifidobacterium species, Eggerthella lenta, and Escherichia coli, newly sequenced or obtained from public resources, across health and disease contexts. | Compare ISE genomic positions at strain resolution. |
| DSS colitis model (dataset 3b) | Five untreated and five DSS-treated specific-pathogen-free mice; 2.5% DSS for seven days, with baseline, day-2, and post-treatment stool sampling and paired RNA/short-read DNA plus baseline/post-treatment long-read DNA profiling. | Relate inflammatory perturbation, strand changes, and genomic-neighborhood remodeling. |
| E. coli oxidative stress assay (dataset 3c) | Five independently H2O2-exposed cultures with DNA sampling through 24 hours and RNA sampling including 4 and 8 hours; three untreated cultures with baseline/24-hour DNA sequencing. | Resolve transcriptional changes and mobilization within one strain over time. |
| Synthetic benchmark | Negative-binomial simulated sense, antisense, and total-count matrices with known DEGs, varying antisense prevalence, expression balance, and technical noise. Total simulated dataset count: **Not specified in paper**. | Evaluate recovery against known truth (Extended Data Fig. 2; Methods). |

Dataset definitions and counts are reported in Extended Data Fig. 1, Fig. 4a, and Methods. Accessions: IBD metagenomes **PRJNA237362**, **PRJNA385949**, **PRJNA400072**; metabolomics **PR000639**; INTEGRATE **PRJEB62473**; MLVS **PRJNA354235**; newly generated colitis, oxidative-stress, and IBD RNA data **PRJEB79363**, **PRJEB114850**, and **PRJEB79362**, respectively (Data availability).

## Experimental Procedure
- Build a microbial gene catalogue by mixed assembly of stool metagenomes; the authors report roughly twice as many full-length coding sequences and up to approximately 20% higher mapping rates than other tested de novo assembly approaches (Results; Supplementary Table 1 as described in the article).
- Map paired DNA/RNA reads, count sense, antisense, and total transcription, filter low counts and antisense signals compatible with technical strand leakage, and normalize transcription against gene abundance using an RNA-to-DNA strategy (Fig. 1a; Methods).
- Fit zero-inflated negative-binomial differential-expression models controlling for gene copy number, cohort, and patient identity; apply Benjamini-Hochberg correction. Benchmark unstranded results and simulated datasets (Fig. 1; Extended Data Fig. 2).
- Partition antisense variation by clinical and microbial covariates; relate disease-associated enzyme signatures to matched metabolites and calprotectin; assess longitudinal stability and random-forest prediction across functional categories (Figs. 2-4).
- Annotate ISEs, terminal inverted repeats, and passenger genes. Compare ISE locations in isolate genomes and use 31-mer signatures of flanking regions to assess genomic-neighborhood change in mice (Figs. 4-5).
- Use long-read E. coli assemblies and strand-specific RNA time courses to establish the order of transcriptional changes and repositioning under oxidative stress; compare with untreated controls and external human cohorts (Fig. 6; Extended Data Figs. 9-10).

## Key Biology Insights
- Antisense transcription is a substantial component of disease-associated microbial regulation despite contributing a minority of RNA reads; treating total RNA as mRNA can obscure or reverse functional interpretation (Fig. 1).
- Active inflammation is associated with convergent microbial transcription across taxonomically diverse organisms. Nutrient utilization and stress-response programs may reflect shared environmental pressures (Figs. 2-4).
- Antisense changes in ISEs suggest a possible balance between genome stability and mobilization of adaptive functions. The proposed regulatory role requires direct mechanistic experiments (Figs. 4-6; Discussion).
- B. wadsworthia ydfG and methylglyoxal-related signals can persist in remission even as most species-associated transcriptional perturbations resolve, indicating that clinical states need not correspond to complete metabolic normalization (Fig. 3; Extended Data Fig. 3).

## Implications
Strand-aware RNA/DNA integration offers a way to study inflammatory activity and microbial adaptation that DNA abundance or unstranded RNA alone misses. The paper motivates biomarker validation and targeted experiments on antisense regulation; it does not establish a clinically validated diagnostic or demonstrate that manipulating antisense RNA prevents disease. Stool sampling lacks tissue-level spatial resolution, sequencing misses parts of the small noncoding-RNA repertoire, and the molecular causality of antisense-mediated transposition remains unresolved (Discussion).

The authors provide [metastrand](https://gitlab.com/mpust/metastrand) and [analysis workflows](https://gitlab.com/mpust/antisense-microbiome) (Code availability).

**Source scope:** Summary based on the supplied article PDF, including embedded methods and extended data. Separate supplementary-table files were not supplied; their contents are described only as reported in the article.
