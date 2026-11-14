# Paper Summary

### Authors
John A. Bachman, Benjamin M. Gyori, and Peter K. Sorger

### Journal
Molecular Systems Biology, 19: e11325

### Publication Date
20 March 2023

### DOI
[10.15252/msb.202211325](https://doi.org/10.15252/msb.202211325)

## Keywords
INDRA; knowledge assembly; text mining; biocuration; mechanistic models; causal networks; protein interactions; Cancer Dependency Map

## Main Idea
The authors present an expanded Integrated Network and Dynamical Reasoning Assembler (INDRA) workflow for assembling reliable, non-redundant molecular mechanisms from heterogeneous sources at literature scale. INDRA converts machine-read and curated information into standardized Statements, corrects entity grounding, removes unsupported or poorly formed assertions, detects duplicate and refinement relationships, and estimates Statement reliability with belief models or machine-learning classifiers. The resulting corpus can support biocuration and mechanistic interpretation of functional-genomics data.

## Evidence Supporting the Main Idea
- Six reading systems processed 567,507 articles and produced approximately 5.9 million raw Statements. Structured sources contributed approximately 730,000 additional Statements, for approximately 6.7 million raw Statements overall.
- Filtering and normalization produced approximately 2.9 million Statements; duplicate assembly yielded approximately 900,000 unique Statements representing human protein mechanisms, with an average of about three supporting mentions per Statement.
- Figure 2 shows that assembly links curated database interactions to specific text-mined evidence. For example, the curated RCHY1–TP73 ubiquitination mechanism was supported by seven text-mined mentions from four readers and two publications.
- Refinement relationships were common: 38% of Statements refined at least one less-specific Statement, and some refinement graphs extended through nine levels of specificity (Fig. 3).
- In a manually curated set of 1,800 Statements and 6,022 mentions, the INDRA Belief Model and beta-binomial model outperformed a simple binomial model. A Random Forest using Statement, reader, refinement, and curated-database features reached the highest reported precision–recall performance (AUPRC 0.942).
- Reader overlap was limited: 19% of assembled Statements had support from at least two readers, while 81.3% had support from one reader. Despite this, overlap and mention counts were informative about correctness.
- Compared with BioGRID, the corpus contained approximately 101,000 PPI Statements absent from BioGRID. The authors estimated a lower bound of approximately 28,600 correct but uncurated PPIs, a 6% increase over the approximately 480,000 unique human PPIs in BioGRID.
- For DepMap codependencies, the full INDRA network explained 22% of strong correlations (|z| > 6), compared with 11% for the database-only network. Using the INDRA network as a prior identified 4,007 Benjamini–Yekutieli-significant codependencies that were not recovered when all pairwise hypotheses were tested without that prior.

## Main Novelty
The work combines multiple machine readers and curated pathway resources in a single intermediate representation and adds explicit hierarchical refinement, evidence aggregation, and calibrated reliability estimation. This turns fragmented, differently specific, and error-prone extractions into an auditable mechanistic knowledge assembly that can be filtered by confidence and reused for multiple downstream models.

## Datasets Used for Evaluation
- **Literature corpus:** 567,507 articles relevant to human protein function. It contained 384,628 PubMed abstracts (67.8%), 81,567 Elsevier articles (14.4%), 74,654 PMC open-access articles (13.2%), 25,950 PMC author manuscripts (4.6%), and 707 records with missing content (0.1%). Role: large-scale event extraction and Benchmark Corpus construction.
- **Structured knowledge sources:** approximately 730,000 Statements derived from Pathway Commons, BEL Large Corpus, SIGNOR, and other structured sources. Role: integration with text-mined mechanisms and evidence comparison.
- **Reader-curation corpus:** 1,800 sampled Statements with 6,022 mentions, curated by two biomedical scientists; the authors sampled 1–10-mention Statements from five readers (Reach, Sparser, MedScan, RLIMS-P, and TRIPS). Role: training and evaluating belief/reliability models.
- **BioGRID:** approximately 480,000 unique human PPIs used as a curated comparison resource. Role: validation of belief scores and estimation of candidate uncurated PPIs.
- **Cancer Dependency Map (DepMap):** more than 700 cancer cell lines with RNAi and CRISPR-Cas9 gene-inactivation viability/growth measurements. Role: testing whether INDRA networks can constrain and mechanistically explain gene codependencies.
- **MitoCarta:** mitochondrial gene reference used to exclude strong mitochondrial codependencies considered assay-related rather than informative of specific functional relationships.

## Experimental Procedure
- Run six text-reading systems—Reach, Sparser, MedScan, TRIPS/DRUM, RLIMS-P, and ISI/AMR—over the article corpus; normalize outputs into INDRA Statements with provenance.
- Add Statements extracted from curated pathway and signaling resources.
- Remove hypothesis-like assertions, repair entity grounding and identifier mappings, restrict the benchmark to human-gene/family/complex mechanisms, and remove invalid sequence positions.
- Merge equivalent Statements and attach all supporting mentions; infer refinement relationships using protein-family, activity, modification, compartment, and contextual hierarchies.
- Build a manually curated Statement/mention dataset; fit binomial, beta-binomial, INDRA Belief, and machine-learning reliability models.
- Compare assembled PPI Statements and evidence against BioGRID, and estimate the expected yield of reviewing uncurated high-belief candidates.
- Build a directed gene network from assembled causal Statements; use it as a hypothesis-space prior and as a source of direct, family/complex, and parent-link explanations for DepMap correlations.

## Key Biology Insights
- Combining literature and databases can add mechanistic detail—direction, regulatory type, molecular state, and modification site—to otherwise coarse or incompletely curated interactions.
- Text mining contributed useful information beyond curated databases: the full INDRA network explained roughly twice as many strong DepMap codependencies as the database-only network.
- Family- and complex-level Statements are biologically useful for explaining gene relationships that are reported generically in the literature. For example, ROCK2–MPRIP codependency was explained through ROCK-family binding in a complex containing PPP1R12A.
- Context-dependent mechanisms can be retained: INDRA distinguished different BRAF states when relating BRAF to MITF, supporting distinct regulatory effects in oncogenic and wild-type contexts.

## Implications
INDRA provides a practical framework for human-in-the-loop biocuration: reviewers can prioritize high-belief candidates, while retaining provenance back to reader outputs, sentences, publications, and databases. The assembled corpus can improve pathway modeling, PPI resource expansion, and interpretation of functional-genomics screens. Important limitations remain: the benchmark covers only part of PubMed, the network is incomplete, machine-reading errors can be systematic, and the current representation focuses mainly on molecular interactions and post-translational regulation rather than genetic interactions, disease relationships, biomarkers, or general statistical associations.

Source: https://doi.org/10.15252/msb.202211325
