# Paper Summary

**Title:** AERO: An AI Agent for Adaptive Eligibility Refinement and Optimization of Clinical Trial Criteria in Real-World Trial Emulation

### Authors
Xiaodi Li, Jose James, Patricia Pellikka, and Nansu Zong.

### Journal
medRxiv preprint, version 1; not peer reviewed in the version summarized.

### Publication Date
May 1, 2026 (version 1 posting date).

### DOI
[10.64898/2026.04.30.26352142](https://doi.org/10.64898/2026.04.30.26352142)

Source: [version 1 PDF](https://www.medrxiv.org/content/10.64898/2026.04.30.26352142v1.full.pdf), 10 pages. Figure and table numbering below follows the supplied PDF, including its numbering gaps.

## Keywords
Target trial emulation; eligibility criteria; agentic AI; electronic health records; WARCEF; warfarin; aspirin; heart failure; AERO.

## Main Idea
AERO uses knowledge-augmented LLM reasoning to classify trial eligibility criteria as strict inclusion, strict exclusion, confounder, or operational criteria to drop. It aims to make randomized-trial protocols usable in EHR data while explicitly recording how eligibility is adapted. Evaluation is a single WARCEF-inspired warfarin-versus-aspirin emulation using Mayo Clinic Platform data (Figure 1; Methods, pp. 2-4).

## Evidence Supporting the Main Idea
- **Operational classification:** Table 2 retains heart failure and reduced ventricular function as inclusion criteria, reclassifies several risk-related criteria as adjustment variables, and drops requirements such as outpatient-protocol compliance (p. 5).
- **Population change:** Figure 2 shows that the adaptive cohort is older and has a different sex distribution, while aspirin remains the predominant treatment. Thus adaptation changes the population, not merely the code (pp. 4-6).
- **Treatment result:** The adjusted Cox estimate is HR 1.561, p = 0.0605; the matched-cohort log-rank test gives p = 0.045. The paper contrasts this with the original trial's HR 1.01, p = 0.91 and calls the adjusted conclusions consistent (Figure 3, p. 7).
- **Eligibility ablation:** Treating ongoing low-molecular-weight heparin (LMWH) as a strict exclusion instead of an adjustment variable changes the treatment estimate to approximately HR 1.86, adjusted p = 0.0347 (Figure 5, p. 8).
- **Assessment:** These results establish sensitivity to eligibility decisions. Matching the category 'not statistically significant' does not establish equivalence of HR 1.561 and HR 1.01, nor validate causal accuracy.

## Main Novelty
The proposed agent acts upstream of estimation: it formalizes eligibility adaptation using protocol context, clinical knowledge, and operational feasibility. Its four-category taxonomy makes adaptation decisions inspectable. The paper does not introduce a new causal estimator or demonstrate broad superiority over expert-designed cohorts (Methods; Discussion).

## Datasets Used for Evaluation
- **Mayo Clinic Platform (MCP):** Multi-institutional EHR data containing treatment exposure, demographic and clinical variables, and survival outcomes. Used to construct original/adaptive eligibility cohorts and the LMWH ablation cohort. The stated restriction is before July 2014, although the text also says 'prior to 2014.' Total database size, analytic cohort counts, arm sizes, and event counts: Not specified in paper.
- **WARCEF protocol and published results:** Eligibility wording from ClinicalTrials.gov and published warfarin-versus-aspirin findings in heart failure with reduced ejection fraction and sinus rhythm. Used as the protocol source and comparison benchmark. Trial participant sample size: Not specified in paper.
- **Knowledge inputs:** UpToDate, Claude-generated contextual interpretation, and ToolUniverse drug information support GPT-5 reasoning. Numbers of retrieved documents, retrieval dates, and independently adjudicated criterion labels: Not specified in paper (pp. 2-3).

## Experimental Procedure
- Copy original WARCEF eligibility criteria from ClinicalTrials.gov.
- Retrieve disease, treatment, safety, and pharmacological context from external knowledge sources.
- Use GPT-5 to classify each criterion into inclusion, exclusion, confounder, or drop/operational.
- Construct EHR treatment cohorts using retained filters and retain reclassified variables for adjustment.
- Compare cohort characteristics; estimate survival using Kaplan-Meier/log-rank and a Cox model adjusted for propensity score and additional covariates.
- Repeat analysis with ongoing LMWH treated as a strict exclusion rather than a confounder; compare effect estimates and significance (Figures 1-3 and 5; Table 2).

## Key Biology Insights
The study provides no new biological mechanism or definitive evidence favoring aspirin or warfarin. It illustrates how cohort composition and treatment selection affect estimated survival associations in heart failure. The stronger mortality association for age over 65 (HR approximately 2.53 in Figure 3) is a model association, not mechanistic evidence.

## Implications
- **Authors' interpretation:** Systematic, knowledge-informed eligibility adaptation may improve feasibility and reproducibility of trial emulation; acknowledged limitations include one trial, prompt/retrieval sensitivity, residual confounding, and possible selection bias (p. 9).
- **Assessment:** Relaxing population-defining or safety criteria can change the target population and estimand. Adjusting for an excluded characteristic does not automatically reproduce the original trial.
- **Reporting inconsistency:** Table 2 labels LMWH, intravenous heparin, and several contraindications as strict exclusions, but the ablation section states that the main analysis treated them as confounders to preserve sample size (pp. 5, 7). This weakens protocol-to-analysis traceability.
- **Reporting limitation:** The paper does not provide a sufficiently detailed time-zero definition, complete cohort counts, quantitative balance diagnostics, or a numeric treatment-effect confidence interval in the prose. Confidence intervals are drawn in the forest plot but should not be reverse-engineered into exact numbers.
- **Assessment:** The description of the 2014 cutoff as avoiding dissemination-related changes is questionable on the paper's own chronology: its reference to the original WARCEF findings is a 2012 publication. This requires clarification, rather than silently treating the cutoff as pre-publication.
