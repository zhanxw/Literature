# An agentic system for rare disease diagnosis with traceable reasoning

**Authors:** Chen et al.  
**Published:** Nature (2025)  
**DOI:** [s41586-025-10097-9](https://www.nature.com/articles/s41586-025-10097-9)

---

## Main Idea

This paper presents **DeepRare**, an agentic LLM-based system designed for rare disease differential diagnosis. Rare diseases affect over 300 million people worldwide, yet diagnosis is notoriously difficult due to clinical heterogeneity and low individual prevalence—patients often face a "diagnostic odyssey" averaging more than 5 years.

DeepRare addresses this challenge by leveraging multi-agent LLM architecture to process heterogeneous patient inputs (free-text clinical descriptions, structured HPO terms, and genomic testing results) and generate ranked candidate diagnoses with **transparent, traceable reasoning chains** that reference verifiable medical evidence.

---

## Key Innovation

The system introduces a **three-tier MCP-inspired architecture**:

1. **Central Host** (LLM-powered with memory): Orchestrates the diagnostic workflow and synthesizes evidence
2. **Specialized Agent Servers**: Handle phenotype/genotype analysis, normalization, and knowledge retrieval
3. **Web-Scale Medical Resources**: Integrate curated databases and real-time medical literature

A key innovation is the **self-reflective loop** that iteratively reassesses hypotheses to reduce over-diagnosis and mitigate LLM hallucinations.

---

## Evaluation Datasets

The study uses **6,401 clinical cases** from **9 datasets** across diverse populations (Asia, North America, Europe):

| Category | Datasets | Cases |
|----------|----------|-------|
| Research Papers | RareBench-MME, LIRICAL, DDD | 2,693 |
| Case Reports | RareBench-RAMEDIS, MyGene2 | 770 |
| Real Clinical Centres | RareBench-HMS, MIMIC-IV-Rare, Xinhua Hospital, Hunan Hospital | 2,938 |

These cover **2,919 rare diseases** spanning **14 medical specialties**. Two in-house datasets (Xinhua & Hunan) include whole-exome sequencing (WES) data for multi-modal evaluation.

---

## Experimental Procedure

### Methods Compared:
- **Traditional tools**: PhenoBrain, PubCaseFinder
- **General LLMs**: GPT-4o, DeepSeek-V3, Gemini-2.0-flash, Claude-3.7-Sonnet
- **Reasoning LLMs**: o3mini, DeepSeek-R1, Gemini-2.0-FT, Claude-3.7-Sonnet-thinking
- **Medical LLMs**: Baichuan-14B, MMedS-Llama 3
- **Agentic systems**: MDAgents, DS-R1-search

### Metrics:
- **Recall@K**: Whether correct diagnosis appears in top-K predictions
- Clinical expert verification of reasoning chains (10 physicians, 180 cases)

### Results:
| Metric | DeepRare | Second Best (Reasoning LLM) | Margin |
|--------|----------|----------------------------|--------|
| **Recall@1** | 57.18% | 33.39% | +23.79% |
| **Recall@3** | 65.25% | 46.60% | +18.65% |
| **Multi-modal Recall@1** | 69.1% | Exomiser: 55.9% | +13.2% |

DeepRare also achieved **95.4% agreement** with clinical experts on evidence factuality, confirming its reasoning steps are medically valid and traceable.

---

## Key Findings

1. **LLM-based approaches outperform traditional tools** – demonstrating superior flexibility in handling diverse clinical presentations
2. **Reasoning-enhanced LLMs beat general LLMs** – transparent reasoning traces improve diagnostic accuracy
3. **General LLMs surpass medical-tuned models** – likely due to parameter scale and training diversity
4. **Multi-agent orchestration is superior** – coordinated specialist agents significantly outpace single-model approaches

---

## Clinical Impact

DeepRare has been deployed as a **web-based diagnostic copilot** for rare disease physicians. The system addresses four critical challenges in AI-driven rare disease diagnosis:
1. Multi-disciplinary knowledge integration
2. Limited training data (few-shot/zero-shot capabilities)
3. Dynamic knowledge updates (~260 new rare diseases discovered annually)
4. Transparency and traceability for clinical trust

---

*Generated: 2025*
