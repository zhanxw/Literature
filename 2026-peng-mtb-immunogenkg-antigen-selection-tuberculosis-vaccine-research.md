# Paper Summary: MTB-ImmunogenKG: An LLM-assisted knowledge graph for antigen selection in tuberculosis vaccine research

### Authors
Jielong Peng, Xinhao Zhuang, Yingying Chen, Haitong Xu, Yunjie Du, Bingdong Zhu, Guoping Zhao, Ying Wang, Yunchao Ling, Guoqing Zhang

### Journal
Biosafety and Health

### Publication Date
2026 (accepted February 3, 2026; corrected proof)

### DOI
10.1016/j.bsheal.2026.02.001

## Keywords
- Mycobacterium tuberculosis (MTB)
- Vaccine development
- Antigen prioritization
- Knowledge graph
- Large language model (LLM)
- Literature mining

## Main Idea
The paper introduces `MTB-ImmunogenKG`, a provenance-linked, antigen-centric knowledge graph for tuberculosis vaccine research. It combines large-scale literature mining, named entity recognition, entity normalization, Neo4j-based graph construction, and LLM-assisted summarization to support contradiction-aware antigen profiling and improve prediction of antigen protective efficacy.

## Evidence Supporting the Main Idea
- The resource was built from more than 77,000 PubMed MTB records as of July 2024 and consolidated `1,476,300` sentence-level evidence instances spanning four vaccine-relevant knowledge patterns: antigen, host immune response, antigen synergy, and adjuvant.
- The graph contains `3,154` unique MTB proteins, which the authors state is about `77%` of the `4,083` annotated proteins in the organism.
- The extraction pipeline processed `51,037` full-text PDFs plus abstracts for the remaining records, converted text to plain text, and segmented the corpus into `9,310,502` short sentences before knowledge filtering.
- Figure 1 summarizes the full pipeline: corpus acquisition and preprocessing, Cavistill-based knowledge extraction, entity standardization, and Neo4j/web-portal deployment.
- The authors report that the graph supports contradiction-aware antigen summaries. Their Rv1813c example surfaces conflicting immune-response evidence from different studies rather than collapsing them into one conclusion.
- In the independent efficacy-prediction experiment, the KG-augmented GPT-4o setup achieved the best reported Matthews correlation coefficient (`0.40`), improving MCC by `0.19` over the best sequence-based tool (`Vaxijen3`) and by `0.45` over an LLM given only antigen names.
- Figure 3 further shows `14` KG-fix cases versus `6` KG-break cases, for a net gain of `8` correct classifications after adding knowledge-graph evidence.
- Error analysis identified biologically plausible false positives: four of the ten most confident false positives were antigens known to induce strong T-cell responses despite limited protective efficacy, which supports the authors' claim that the task is biologically nontrivial rather than a simple extraction artifact.

## Main Novelty
- Builds a tuberculosis-focused, antigen-centric knowledge graph that links literature evidence directly to vaccine decision criteria.
- Uses sentence-level provenance so each summary can be traced back to specific supporting papers and statements.
- Explicitly surfaces contradictions in the literature instead of forcing a single synthesized answer.
- Demonstrates that structured literature evidence can improve downstream protective-efficacy prediction beyond sequence-only tools and name-only LLM prompting.

## Datasets Used for Evaluation
- `PubMed MTB literature corpus`
  - Content: PubMed records retrieved with an unrestricted search for `"Mycobacterium tuberculosis"` as of July 2024.
  - Size: `77,704` records total.
  - Full text: `51,037` PDFs retrieved; remaining records represented by abstracts via Entrez E-utilities.
- `Sentence corpus after preprocessing`
  - Content: Plain-text sentences extracted from full text and abstracts.
  - Size: `9,310,502` sentences, median `29` tokens.
- `Knowledge graph evidence set`
  - Content: Sentences retained after pattern classification and entity extraction.
  - Size: `1,476,300` evidence instances across four knowledge patterns.
- `Independent antigen efficacy evaluation set`
  - Content: `42` MTB antigens from an in vivo study using `CB6F1` mice challenged with `H37Rv`.
  - Labeling rule: antigens with greater than `1.5-fold` reduction in lung colony-forming units were labeled positive for high protection; `1.5-fold` or less were labeled negative.

## Experimental Procedure
- Retrieve MTB-related PubMed records and collect full-text PDFs when available; collect abstracts otherwise.
- Convert PDFs to plain text with `GROBID` and split all text into sentences using Spark NLP `SentenceDetectorDLModel`.
- Define four knowledge patterns relevant to TB antigen selection: antigen, host immune response, antigen synergy, and adjuvant.
- Use the `Cavistill` distillation framework with `GPT-4o` as teacher and `phi-3.5-mini-instruct` as student to train:
  - a knowledge-pattern classifier
  - a named entity recognition model over 14 entity types
- Normalize extracted entities using reference databases where possible and LLM-assisted categorization where no authoritative database exists.
- Load `Paper`, `Sentence`, and `Entity` nodes into `Neo4j` and preserve sentence-to-paper provenance links.
- For antigen profiling, retrieve evidence by knowledge pattern, summarize large evidence sets with a sliding-window approach, and generate a final contradiction-aware knowledge summary.
- For efficacy prediction, compare three approaches on the 42-antigen test set:
  - KG-augmented `GPT-4o` using graph-derived summaries
  - name-only `GPT-4o`
  - sequence-based tools `Vaxign-ML`, `Vaxijen2`, and `Vaxijen3`
- Evaluate with Matthews correlation coefficient, precision, recall, and F1 score, then inspect per-antigen fixes/breaks and the most confident false positives.

## Key Biology Insights
- TB antigen selection is not just a sequence-ranking problem; it depends on linking antigen identity to immune context, combinatorial antigen usage, and adjuvant effects.
- Host immune-response evidence dominates the literature, while antigen-synergy and adjuvant evidence are comparatively sparse, indicating a narrower evidence base for some vaccine-design decisions.
- Strong immunogenicity does not guarantee protection. The false-positive analysis highlights antigens that trigger robust T-cell responses yet still show limited protective efficacy in vivo.
- Contradictory literature exists even for specific candidates such as `Rv1813c`, reinforcing the need for traceable, context-aware evidence review instead of simple aggregate scoring.

## Implications
- The resource can shorten the manual literature-synthesis step in TB vaccine antigen prioritization by turning dispersed narrative evidence into searchable, auditable summaries.
- Its design offers a practical bridge from literature retrieval to experimental planning, especially when building antigen panels or pairing antigens with adjuvants.
- The framework is portable: the authors argue the same pattern-based knowledge-graph approach could be rebuilt for other bacterial vaccine programs.
