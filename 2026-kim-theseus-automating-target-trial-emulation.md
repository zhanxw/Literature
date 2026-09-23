# Paper Summary

**Title:** From study design to executable code: automating target trial emulation with large language models

### Authors
Hanjae Kim, Minseong Kim, Seonji Kim, and Seng Chan You. Hanjae Kim and Minseong Kim contributed equally.

### Journal
JAMIA Open, volume 9, issue 4, article ooag131. Peer-reviewed Research and Applications article.

### Publication Date
July 9, 2026 (online publication, publisher metadata); August 2026 issue. The attached PDF records receipt on May 10, revision on June 12, and acceptance on June 18, 2026.

### DOI
[10.1093/jamiaopen/ooag131](https://doi.org/10.1093/jamiaopen/ooag131)

Source: user-supplied publisher PDF, `ooag131.pdf`, 9 pages. [Publisher article](https://academic.oup.com/jamiaopen/article/9/4/ooag131/8729191). Page, table, and figure locators below refer to that PDF. Separate supplementary files were not independently inspected.

## Keywords
Target trial emulation; large language models; OHDSI; OMOP common data model; Strategus; human-in-the-loop AI; structured specifications; reproducibility; THESEUS.

## Main Idea
THESEUS (Text-guided Health-study Estimation and Specification Engine Using Strategus) separates natural-language interpretation from code construction. An LLM converts study descriptions into structured JSON specifications; users review the settings, and deterministic rules translate them into Strategus R scripts. The implemented scope comprises study period, time-at-risk (TAR), propensity-score (PS) adjustment, and outcome model settings within OHDSI's Cohort Method workflow (Figures 1-2; pp. 2-4).

The evaluated task is specification extraction and standardization. The paper does not demonstrate autonomous identification of a valid causal question, complete cohort construction, or recovery of unbiased treatment effects.

## Evidence Supporting the Main Idea
- **Primary-analysis extraction:** Across 15 OHDSI studies, mean accuracy across the four specification sections was 0.93-0.97. Across 15 non-OHDSI studies, it was 0.82-0.95. Gemini-3.1-Pro led the OHDSI evaluation at 0.97; GPT-5.5 and Gemini-3.1-Pro tied at 0.95 for non-OHDSI studies (Table 1, p. 5). Overall accuracy is not the proportion of complete protocols extracted without error.
- **Timing is harder:** TAR accuracy ranged from 0.73 to 0.93 for OHDSI studies and 0.53 to 0.93 for non-OHDSI studies. All models achieved 1.00 for OHDSI study period and outcome model extraction, so aggregate accuracy can conceal timing errors (Table 1).
- **Primary plus sensitivity analyses:** On 99 OHDSI gold-standard specification items, precision was 0.87-0.99, sensitivity 0.83-0.97, and false positives 0.07-0.80 per study. On 83 non-OHDSI items, corresponding ranges were 0.78-0.90, 0.77-0.89, and 0.53-1.20 (Table 2, p. 5).
- **Best full-analysis result:** GPT-5.5 achieved precision/sensitivity of 0.99/0.97 for OHDSI and 0.90/0.89 for non-OHDSI descriptions, with 0.07 and 0.53 false positives per study, respectively (Table 2).
- **Modified descriptions:** Thirty augmented OHDSI descriptions tested extraction after changing design parameters. GPT-5.5 achieved 1.00 across all four sections (Results; Figure 3, pp. 5-6). The Results prose gives an across-model range of 0.82-1.00, but the lowest augmented bar in Figure 3 appears near 0.90; exact lower-end reconciliation requires Supplementary Material 7.
- **Available implementation:** The paper describes a review GUI, command-line tooling, MCP tools/slash commands for coding agents, and incorporation into OHDSI Study Agent (p. 4). Availability is not equivalent to an end-to-end effectiveness evaluation.

## Main Novelty
The contribution is a constrained architecture combining LLM extraction, a standardized analytic schema, human review, and deterministic workflow generation. OMOP standardizes the data layer, while Strategus standardizes analysis specifications; this reduces open-ended code generation to a structured mapping problem. An accompanying `renv` environment records R dependencies (pp. 2-3, 6).

## Datasets Used for Evaluation
- **OHDSI publication benchmark:** 15 published studies using OMOP CDM and HADES or Strategus. Author-extracted methods passages provide primary-analysis and full-analysis inputs; author-created specifications serve as the gold standard. The full-analysis benchmark contains 99 items: 18 study-period, 35 TAR, 31 PS-adjustment, and 15 outcome-model items (pp. 3-5; references 17-31).
- **Non-OHDSI publication benchmark:** 15 studies with explicit follow-up, PS-adjustment, and outcome-model descriptions. Full-analysis evaluation contains 83 items: 22 study-period, 20 TAR, 22 PS-adjustment, and 19 outcome-model items. Unsupported methods were excluded, including outcome models outside Cox, Poisson, or logistic regression and doubly robust estimation (pp. 3, 5, 7; references 32-46).
- **Augmented OHDSI benchmark:** Two modified primary-analysis descriptions per OHDSI study, totaling 30 descriptions. Wording was largely preserved while study settings were recombined; this probes sensitivity to changed parameters rather than simply reproducing published settings (pp. 4-5).
- **Patient-level evaluation dataset:** Not specified in paper. The reported benchmark units are study descriptions and specification fields, not patients or newly estimated clinical outcomes.

## Experimental Procedure
- Manually extract relevant methods passages and construct reference specifications from the 30 publications.
- Provide each model with the same study description, JSON schema, and field-level guidance; request structured settings and interpretation explanations.
- Compare eight models: GPT-5.5, GPT-5.4-mini, Gemini-3.1-Pro, Gemini-3.1-Flash-Lite, Claude-opus-4.8, Claude-haiku-4.5, DeepSeek-V4-Pro, and DeepSeek-V4-Flash.
- Run API queries in June 2026, without fine-tuning, using temperature 0, one attempt per input, no retries, and no vendor-specific prompt modifications (p. 4).
- Score primary-analysis accuracy by specification section; score full-analysis fields using precision, sensitivity, and false positives per study; repeat primary extraction on modified OHDSI descriptions.
- In the implemented workflow, display proposed changes for human acceptance or rejection, then generate Strategus R scripts through deterministic rules (Figures 1-2). The quantitative evaluation focuses on the extraction stage.

## Key Biology Insights
Not specified in paper. This is a research-informatics methods study, not a new biological or comparative-treatment-effect investigation. Clinical studies provide language inputs; their treatment findings are not independently re-estimated or validated here.

## Implications
- **Authors' interpretation:** Standardized data and analysis frameworks enable accessible, reproducible generation of observational research workflows. Integration with separate cohort-definition systems could extend coverage to a fuller TTE workflow (Discussion, p. 6).
- **Authors' limitations:** Only four specification components and supported Cohort Method settings were evaluated. The publication sample is small, possible pretraining exposure cannot be excluded, researcher usability was not tested, and sites need OMOP-converted data (p. 7).
- **Assessment:** High extraction accuracy does not demonstrate that the source design is causally valid, that an entire protocol is correct, or that treatment-effect estimates are unbiased. Timing errors deserve separate review because they can have disproportionate consequences.
- **Assessment:** Non-OHDSI validation tests translation of selected supported study descriptions into OHDSI settings; it does not establish execution on arbitrary non-OMOP databases.
- **Assessment:** Deterministic code construction can improve consistency but does not by itself prove defect-free implementation. The study supplies no direct user time-saving, cognitive-load, or end-to-end clinical-effect validation results.
- Public resources: [application code](https://github.com/dr-you-group/theseus-app), [coding-agent tooling](https://github.com/dr-you-group/theseus-plugin), [evaluation data and code](https://github.com/dr-you-group/theseus-evaluation), and [Dryad archive](https://doi.org/10.5061/dryad.qnk98sfzs).
