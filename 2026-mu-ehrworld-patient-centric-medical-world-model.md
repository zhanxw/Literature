# Paper Summary

### Authors
Linjie Mu, Zhongzhen Huang, Yannian Gu, Shengqian Qin, Shaoting Zhang, and Xiaofan Zhang.

### Journal
Not specified in paper. arXiv preprint (arXiv:2602.03569v1; categories cs.AI and cs.LG).

### Publication Date
February 3, 2026.

### DOI
Not specified in paper.

## Keywords

Medical world models; electronic health records; longitudinal clinical trajectories; patient simulation; causal sequential modeling; long-horizon prediction; clinical interventions; large language models.

## Main Idea

The paper argues that medical knowledge alone does not make an LLM a reliable dynamic patient simulator. In sequential clinical simulation, naive LLMs can reproduce isolated observations but fail to maintain a consistent latent patient state after interventions, causing errors to accumulate over long rollouts. The authors introduce EHRWorld, a patient-centric medical world model trained on intervention-conditioned, temporally ordered clinical trajectories. EHRWorld explicitly maintains the patient history and uses different prediction behavior for inquiry events (which produce observable values) and intervention events (which alter future state without an immediate value).

## Evidence Supporting the Main Idea

- The evaluation uses full-trajectory prediction: models autoregressively generate a hospitalization trajectory from admission to discharge while conditioning on sequential clinical events and interventions.
- In Table 1, EHRWorld-4B/8B/14B obtain Avg Scores of 0.755/0.762/0.765, compared with 0.618 for GPT-5.2 and 0.574 for GEMINI-3.0-Pro-Preview. EHRWorld-14B also obtains S@25 = 0.716 and SMAPE error = 0.262.
- In Table 2, EHRWorld-14B has the highest overall retention rate, 92.6%, compared with 86.2% for GPT-5.2. Its retention rates are 88.8% for numerical S@25, 85.1% for Stat F1, and 98.4% for Label F1.
- On the high-sensitivity subset, where consecutive states change by more than 50%, EHRWorld-14B's S@25 falls only from 71.6% to 69.7% and its SMAPE rises from 0.262 to 0.292 (Figure 3). The paper reports larger degradation for the general-purpose baselines.
- In the qualitative case study (Figure 4), EHRWorld-14B keeps most predictions within the precise error range (at most 10%), while competing models show larger deviations for laboratory measurements such as calcium, creatining, hemoglobin, and hematocrit.
- The authors also report that scaling general-purpose models is not sufficient: Qwen3-235B-A22B-Instruct has Avg Score 0.506, whereas the 4B EHRWorld model reaches 0.755.

## Main Novelty

- EHRWorld-110K: a large longitudinal dataset built from complete hospitalization episodes, combining static patient context, diagnoses, and chronologically ordered inquiry and intervention events.
- A causal sequential training paradigm that treats clinical simulation as state evolution conditioned on sets of concurrent actions.
- A deterministic history update that feeds generated events back into the next patient state, supporting long-horizon consistency.
- A unified family of 4B, 8B, and 14B patient-centric world models and an evaluation focused on both local prediction and error accumulation during full rollouts.

## Datasets Used for Evaluation

- **EHRWorld-110K:** Derived from the MIMIC-IV electronic health record database. It contains 110,513 hospitalization episodes and approximately 17.5 million clinical events, including unstructured discharge-note information converted into demographics and hierarchical diagnoses, plus time-stamped laboratory/inquiry, medication, procedure, microbiology, and other clinical events. It is used for model training and held-out trajectory evaluation.
- **Held-out test split from EHRWorld-110K:** 579 hospitalization episodes, containing 84,010 inquiry events and 25,798 intervention events, with 1,043 unique primary and secondary diagnostic conditions. Splitting is patient-centric, so all admissions for a patient remain in one partition to reduce leakage. The paper does not report a separate external test dataset.

## Experimental Procedure

- Extract static demographics and admission-relevant hierarchical diagnoses from MIMIC-IV discharge summaries using Qwen3-235B-A22B-Instruct.
- Parse time-stamped EHR events and classify them as inquiry events (passive observations with values) or intervention events (active actions that modify the patient state).
- Combine the static context and ordered event sequence at the hospitalization-episode level; remove episodes with insufficient activity, incomplete records, extreme lengths/event counts, or no medication administrations.
- Fine-tune Qwen3-4B-Instruct, Qwen3-8B, and Qwen2.5-14B-Instruct for three epochs on eight NVIDIA H100 GPUs using DeepSpeed ZeRO-2, AdamW, learning rate 1e-6, cosine decay, 0.05 warm-up ratio, and causal masking.
- Compare EHRWorld with closed-source GPT-5.2 and Gemini-3.0-Pro-Preview; general-purpose open models from 4B to 671B parameters; and medical models MedGemma-4B/27B and Baichuan-M2-32B.
- Evaluate numerical outputs using S@10, S@15, S@25, SMAPE, and Stat F1; evaluate discrete outputs using precision, recall, and Label F1; report their mean as Avg Score.
- Compare next-step prediction with autoregressive full-trajectory prediction and define Retention Rate as Full / Next × 100 to measure resistance to error accumulation.
- Stress-test robustness on a high-sensitivity subset with more than 50% relative change between consecutive states and inspect a qualitative patient case.

## Key Biology Insights

- The central biological insight is methodological: a patient trajectory is not a collection of independent measurements. Clinical measurements and treatment responses must be modeled as evolving consequences of an underlying physiological state and prior interventions.
- Interventions such as medications and procedures may not yield an immediate observable value, but they alter the context for subsequent laboratory and clinical observations. Representing them explicitly improves temporal and causal consistency.
- The results suggest that longitudinal, intervention-conditioned supervision captures clinically relevant temporal dependencies more effectively than static medical knowledge or instruction tuning alone.
- The paper does not establish clinical treatment efficacy or biological causal effects in patients; its evidence is limited to retrospective EHR trajectory simulation.

## Implications

EHRWorld supports research into patient-state simulation, counterfactual treatment comparison, and clinician-in-the-loop evaluation, but it is not presented as an autonomous or real-time clinical decision system. The authors note residual autoregressive error, the absence of direct treatment-optimization or policy-learning evaluation, and possible bias from observational practice patterns. Any clinical deployment would require external validation, transparency, careful bias assessment, and human oversight.

