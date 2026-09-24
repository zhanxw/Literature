# Paper Summary

**Title:** Antifungal therapy improves microbiome dynamics in inflammatory bowel disease

### Authors
Xiangyu Pan, Aidan Conroy, Tsering S. Ngima, Marissa Mesko, Olga Morzhanaeva, Aurelia Li, Jamie Marino, Lars F. Westblade, Alexander Grier, Petra Bacher, Randy S. Longman, Ellen J. Scherl, and Iliyan D. Iliev.

### Journal
Nature Medicine, volume 32, pages 3385-3395 (2026).

### Publication Date
Published online September 1, 2026; September 2026 issue.

### DOI
[10.1038/s41591-026-04616-y](https://doi.org/10.1038/s41591-026-04616-y)

## Keywords
Inflammatory bowel disease; Candida albicans; mycobiome; fluconazole; nystatin; cross-kingdom interactions; short-chain fatty acids; longitudinal multi-omics.

## Main Idea
In patients with mild-to-moderate inflammatory bowel disease (IBD) and oral thrush, a two-week course of fluconazole was associated with reduced intestinal Candida, changes in bacterial communities and stool metabolites, and improved clinical activity scores during eight weeks of observation. Swish-and-spit nystatin resolved oral thrush but did not produce comparable intestinal fungal changes. The prospective IVAN study supports testing mycobiome-guided antifungal cotherapy, but its nonrandomized design does not establish clinical efficacy (Figs. 1-5; Discussion).

## Evidence Supporting the Main Idea
- **An oral-gut fungal link:** Whole-genome analyses of 30 C. albicans isolates from paired oral and fecal samples of six patients showed closely related within-patient strains, including concordant SNP and loss-of-heterozygosity patterns. This supports shared colonization and a possible dissemination route, without proving its direction (Fig. 1a,b; Extended Data Fig. 1).
- **Intestinal fungal suppression:** Both treatments resolved oral thrush, but viable fecal Candida became nearly undetectable in most evaluated fluconazole recipients after treatment. Colonies reappeared in roughly half by week 4. ITS profiling showed reduced C. albicans, C. parapsilosis, opportunistic-fungal abundance, and fungal richness in the fluconazole group; swish-and-spit nystatin had little intestinal effect (Fig. 2; Extended Data Fig. 2).
- **Bacterial community changes:** Fluconazole-associated fungal suppression coincided with increased bacterial richness and expansion of taxa including Faecalibacterium prausnitzii, Clostridium butyricum, Roseburia hominis, and Odoribacter splanchnicus. C. albicans abundance correlated inversely with bacterial diversity (Fig. 3; Extended Data Fig. 3).
- **Metabolic changes:** Longitudinal clustering identified four modules containing 6,001 metabolomic features, with opposing patterns between treatments. Fluconazole was associated with increased butyric acid, changes in bile-acid-related pathways, and lower metabolite-based dysbiosis scores. Associations between bacterial abundance and metabolites support coordinated ecological changes, rather than directly demonstrating which organisms produced each compound (Fig. 4; Extended Data Fig. 4; Methods).
- **Exploratory clinical outcomes:** Among 49 longitudinally evaluable participants, numerical disease activity index (DAI) improvement at week 2 occurred in 27/33 fluconazole recipients (81.8%) and 8/16 nystatin recipients (50.0%). By weeks 4-8, the corresponding proportions were 31/33 (94.0%) and 9/16 (56.3%). More stringent clinical response at week 2 occurred in 15/33 (45.5%) versus 4/16 (25.0%); numerical improvement must not be equated with clinical response or remission (Fig. 5b,f).
- **Score-defined progression:** Estimated eight-week progression probabilities were 3.0% versus 37.5% for fluconazole and nystatin (log-rank P = 0.0017). Progression meant the first increase in a disease activity score above baseline, not an endoscopically confirmed relapse or a prespecified efficacy endpoint (Fig. 5e; Methods).

## Main Novelty
The study combines a clinically observable fungal manifestation, strain-resolved oral-gut Candida comparisons, and longitudinal fungal, bacterial, metabolomic, and clinical measurements. Its central contribution is a patient-selection framework and evidence of broad ecological changes associated with intestinal fungal targeting, rather than a definitive therapeutic trial (Fig. 1; Discussion).

## Datasets Used for Evaluation
All patient datasets below derive from the same IVAN observational cohort; they are not independent validation cohorts.

| Dataset | Contents and sample size | Role |
|---|---|---|
| IVAN clinical cohort | 53 patients: 30 ulcerative colitis (UC), 23 Crohn's disease (CD). Nystatin/ORNT: 18 patients, including 11 UC and 7 CD. Fluconazole/GIFT: 35 patients, including 19 UC and 16 CD. | Compare microbiome trajectories during physician-selected standard care; ongoing IBD medications were continued. |
| Oral-fecal isolate genomes | 30 C. albicans isolates from six patients. | Establish within-patient strain relatedness between sites (Fig. 1a,b). |
| Viable fungal cultures | 30 fecal samples from 19 patients with verified collection timing; paired longitudinal plots use seven ORNT and six GIFT participants. | Assess viable intestinal fungal burden (Fig. 2a,b). |
| Fungal ITS sequencing | 182 initial fecal libraries; 180 retained after quality filtering: 59 ORNT and 121 GIFT, including 108 UC and 72 CD samples. | Track fungal composition and diversity (Fig. 1e; Methods). |
| Shotgun metagenomics | 181 retained fecal profiles: 60 ORNT and 121 GIFT. | Profile bacterial diversity and taxa (Fig. 3; Extended Data Fig. 3). |
| Untargeted stool metabolomics | 155 samples: 51 ORNT and 104 GIFT; flow-injection mass spectrometry in negative-ion mode. | Identify metabolite modules, pathway patterns, and microbial associations (Fig. 4; Methods). |
| Longitudinal clinical/integrated analysis | 49 participants: 16 ORNT and 33 GIFT; four enrolled participants lacked sufficient longitudinal sampling for integrated analysis. | Analyze symptom trajectories, response, and exploratory progression (Fig. 5; Methods). |

Sample counts represent participant-time-point observations unless explicitly labeled as participants. Raw ITS and metagenomic reads are deposited under **PRJNA1449485**. The paper identifies Supplementary Tables 2, 3, 8, and 10 as sources for clinical/medication information, sample metadata, metabolomics, and bacterial abundance, respectively. The C. albicans SC5314 reference genome is **GCA_000182965.3**. Analysis code is reported at [pangxueyu233/MMC](https://github.com/pangxueyu233/MMC) (Data and Code availability).

## Experimental Procedure
- Enroll patients with IBD and mild oral thrush in prospective observational follow-up. Physicians independently chose antifungal treatment; investigators did not randomize, assign, or recommend treatment (Methods).
- Compare 14 days of swish-and-spit nystatin, 5 ml four times daily, with fluconazole, 200 mg on day 1 followed by 100 mg daily on days 2-14. These are the studied regimens, not treatment recommendations (Fig. 1c).
- Collect longitudinal samples around baseline and weeks 1, 2, 4, and 8; characterize paired oral-fecal isolates by whole-genome sequencing and fecal fungi by culture and ITS sequencing (Figs. 1-2).
- Profile bacteria by shotgun metagenomics and stool metabolites by untargeted mass spectrometry. Compare diversity, composition, taxa, temporal metabolite clusters, pathways, and microbial-metabolite associations (Figs. 3-4).
- Assess UC with partial Mayo scores and CD with the Harvey-Bradshaw Index. Evaluate baseline-adjusted changes, clinical response thresholds, and time to the first score increase; explore covariate adjustment using Cox regression (Fig. 5; Methods).
- Interpret these analyses as exploratory: no formal a priori sample-size calculation was performed, and many figure-level comparisons were not adjusted for multiple testing (Methods; figure legends).

## Key Biology Insights
- Fungal suppression can accompany broad bacterial and metabolic changes, supporting a cross-kingdom view of intestinal dysbiosis (Figs. 2-4).
- Reduced fungal richness and increased bacterial richness occurred together; diversity changes have different biological interpretations across kingdoms and cannot uniformly be called beneficial or harmful (Figs. 2-3).
- Some ecological changes persisted despite partial fungal rebound, suggesting that transient reduction of dominant opportunistic fungi may alter community organization beyond the treatment interval (Discussion).
- C. tropicalis and C. sake showed slight increases while other Candida species declined, consistent with species-specific susceptibility and possible selection. This study did not establish newly acquired resistance as the cause (Fig. 2i; Extended Data Fig. 2g).

## Implications
The findings motivate randomized, placebo-controlled studies in patients selected for relevant fungal manifestations, with objective inflammatory and endoscopic outcomes. Generalization to IBD without oral thrush, long-term efficacy, optimal treatment duration, and resistance consequences remain unresolved. Physician-selected treatment, small and unequal groups, residual confounding, eight-week follow-up, limited strain sampling, and absence of repeated endoscopic assessment constrain causal interpretation (Discussion; Methods).

**Source scope:** Summary based on the supplied article PDF, including its embedded extended data and methods. Separate supplementary-table files were not supplied; their contents are described only as reported in the article.
