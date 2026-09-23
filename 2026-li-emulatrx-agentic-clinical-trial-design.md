# Paper Summary

**Title:** Empowering clinical trial design with agentic intelligence and real-world data

### Authors
Haoyang Li, Weishen Pan, Suraj Rajendran, Chengxi Zang, and Fei Wang. Li, Pan, and Rajendran contributed equally.

### Journal
Nature Communications, volume 17, article 5501. Peer-reviewed research article.

### Publication Date
July 7, 2026. Received June 24, 2025; accepted June 8, 2026.

### DOI
[10.1038/s41467-026-74501-2](https://doi.org/10.1038/s41467-026-74501-2)

Source: [publisher PDF](https://www.nature.com/articles/s41467-026-74501-2.pdf). Locators below refer to this 19-page article; separate supplementary files were not independently inspected.

## Keywords
Target trial emulation; multi-agent systems; large language models; clinical trial design; electronic health records; OMOP; causal inference; EmulatRx.

## Main Idea
EmulatRx organizes five LLM agents (Supervisor, Trialist, Informatician, Clinician, and Statistician) into a tool-using workflow that retrieves trials, specifies protocols, constructs EHR cohorts, runs statistical analyses, and iteratively generates trial-design reports. The primary contribution is workflow automation with clinical knowledge retrieval and feedback, rather than a new causal estimator (Figure 1; pp. 2-3).

## Evidence Supporting the Main Idea
- **Retrieval:** Across three hydrocortisone/septic-shock queries, the trial knowledge graph retrieved all 34, 10, and 1 relevant trials, respectively, with 100% precision and recall. This is a narrow three-query evaluation (Table 1, p. 4).
- **Protocol parsing:** On 266 annotated concepts from 20 trials, GPT-4o attained 98.9% recall and 96.7% precision. These are concept-extraction metrics, not end-to-end causal validity (Figure 2a; p. 4).
- **Cohort SQL:** Error counts increased with eligibility complexity (Spearman rho = 0.45, p = 0.043). The best model still made errors; Table 2 lists trial-specific counts (pp. 5-6).
- **Synthetic estimation:** For true HRs of 0.5, 1, 2, and 3, estimates were 0.6345, 1.0383, 1.7524, and 2.8074. Identical outputs across LLMs arose because they selected the same deterministic statistical tools (Table 3, p. 7). The 95% interval for the true-HR-0.5 scenario, 0.5448-0.7389, excludes 0.5; therefore these examples do not establish unbiased estimation or nominal coverage.
- **Expert ratings:** Three clinical experts rated generated responses. GPT-4o's average was 4.88/5 versus 4.78, 4.71, and 4.40 for Phi-4, DeepSeek-R1, and Gemma 3 (Table 5, p. 8).
- **Runtime:** The main text reports GPT-4o runtime of 5.75 +/- 1.52 minutes and refers to Supplementary Figure 3. The days-to-weeks manual comparison is contextual, not a randomized head-to-head time study (p. 10).

## Main Novelty
A coordinated agent architecture connects protocol interpretation to executable cohort queries, causal-analysis tools, clinical interpretation, and iterative design refinement. Additional modules include eligibility-criterion Shapley analysis, subgroup exploration, and prospective sample-size planning (Figures 1 and 5; Methods, pp. 12-15).

## Datasets Used for Evaluation
- **ClinicalTrials.gov retrieval corpus:** 1,363 trials in septic shock, acute kidney injury, acute heart failure, and acute pulmonary edema; supports the knowledge graph and three retrieval queries (p. 4).
- **Expert-annotated benchmark:** 20 trials, including 10 acute-condition trials evaluated with MIMIC-IV and 10 chronic-condition trials with INSIGHT; 266 annotated concepts for parsing, plus SQL evaluations (pp. 2, 4; Table 2).
- **MIMIC-IV:** The paper describes over 299,000 patients from Beth Israel Deaconess Medical Center, 2008-2019. Used for acute-care cohort construction and demonstrations. Reported case cohorts contain 13,942 patients for nesiritide, 11,124 for renal replacement therapy, and 2,306 for hydrocortisone (pp. 10-11). A separate sample-size demonstration uses 6,971 patients; these are distinct reported analyses (p. 7).
- **INSIGHT:** 5,532,428 patients from five New York City health systems, January 2007-December 2023; supports chronic-disease examples and longitudinal eligibility evaluation (p. 11).
- **Synthetic survival data:** 1,000 subjects and 10 covariates for four treatment-effect scenarios; another 1,000-subject dataset with SOFA and age evaluates effect modification. Figure 2 states each estimate derives from one simulated dataset, without biological or technical replicates (pp. 5-8).
- **Synthetic eligibility-importance data:** 2-20 criteria, known contributions, and Gaussian noise; evaluates Monte Carlo Shapley estimation. Patient sample size: Not specified in paper for this experiment (p. 7).

## Experimental Procedure
- Retrieve trial protocols, extract clinical concepts and temporal constraints, and construct a standardized knowledge graph.
- Generate and execute SQL against EHR data; compare outputs and errors with expert expectations.
- Select covariates and statistical tools, evaluate balance, and estimate survival effects. Methods describe clone-censor-weight handling of treatment timing, propensity-score methods, and outcome models; implementation fidelity requires separate verification.
- Compare four LLM backends using retrieval, parsing, SQL, simulation, and expert-rating evaluations.
- Demonstrate three acute-care emulations; explore subgroups, eligibility changes, and sample-size planning; produce structured reports (Figures 1-3; Tables 1-5).

## Key Biology Insights
No new molecular mechanism is established. Reported clinical associations include nesiritide HR 0.5913 (95% CI 0.46-0.76), renal replacement therapy HR 0.6443 (p = 0.0008), and hydrocortisone HR 1.2983 (95% CI 1.07-1.58) in the respective observational cohorts (p. 10). These illustrate generated analyses and should not be interpreted as independently validated treatment recommendations.

## Implications
- **Authors' interpretation:** Agent collaboration can accelerate EHR-based trial design and evidence generation; broader external validation and standardized end-to-end benchmarks remain necessary (Discussion, p. 11).
- **Assessment:** Strong component performance does not establish causal identification. Outcome-driven subgroup and eligibility refinement requires prespecification or independent validation to avoid selective inference (Methods, pp. 14-15).
- **Assessment:** The nesiritide example drops an imbalanced covariate after agent consultation. Better reported balance after dropping a variable is not evidence that confounding by that variable disappeared (p. 10).
- **Reporting caveat:** The Discussion reports a Trialist F1 of 95.4%, whereas Results gives precision 96.7% and recall 98.9%. These reported quantities are not numerically consistent if they describe the same aggregation; the summary preserves the Results metrics without silently reconciling them.
- [Code](https://github.com/TrialLab/EmulatRx) is available; patient data require the respective access agreements.
