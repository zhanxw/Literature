# Paper Summary: Evaluating explainability for graph neural networks

### Authors
Chirag Agarwal, Owen Queen, Himabindu Lakkaraju, and Marinka Zitnik

### Journal
Scientific Data

### Publication Date
2023

### DOI
10.1038/s41597-023-01974-x

## Keywords
- graph neural networks
- explainability
- GraphXAI
- ShapeGGen
- synthetic benchmarks
- fairness
- ground-truth explanations

## Main Idea
The paper introduces `ShapeGGen`, a flexible synthetic graph generator with ground-truth explanations, and packages it together with real-world datasets, explainers, utilities, and evaluation metrics in `GraphXAI`. The goal is to make benchmarking of graph neural network (GNN) explanation methods more reliable, standardized, and stress-testable across graph properties such as homophily, explanation size, feature informativeness, and fairness.

## Evidence Supporting the Main Idea
- The resource directly addresses a core benchmark gap: most existing graph datasets either lack ground-truth explanations or contain explanations that are redundant, trivial, or misaligned with the rationale used by the trained model.
- `GraphXAI` includes eight explanation methods for benchmarking: Grad, GradCAM, GuidedBP, Integrated Gradients, GNNExplainer, PGExplainer, SubgraphX, and PGMExplainer, plus random baselines.
- The evaluation framework measures multiple explanation properties rather than accuracy alone, including graph explanation accuracy, faithfulness, stability, and fairness.
- On ShapeGGen node-classification datasets, the paper reports that `SubgraphX` produced `145.95%` more accurate and `64.80%` more faithful explanations on average than random baselines.
- The resource exposes systematic weaknesses in current explainers:
  - explanations were `55.98%` more unfaithful on heterophilic than homophilic graphs;
  - many explainers degraded on larger ground-truth explanations;
  - fairness analyses showed that state-of-the-art explainers often fail to preserve counterfactual fairness.
- The library also supports real-world graph tasks, letting the same evaluation machinery be applied beyond synthetic motifs.

## Main Novelty
- Introduces a synthetic graph generator designed specifically for explanation benchmarking with controllable, non-trivial, ground-truth explanations.
- Combines datasets, explainers, metrics, visualizers, and loaders into a single graph-explainability benchmarking ecosystem.
- Expands explanation evaluation to fairness and stability, not just overlap with a nominal ground truth.

## Datasets Used for Evaluation
- Synthetic datasets:
  - `ShapeGGen` family of generated graphs with controllable properties such as graph size, degree distribution, homophily versus heterophily, fairness, and node-feature informativeness.
  - Default split for ShapeGGen datasets: `70/5/25` train/validation/test.
- Real-world graph-classification datasets with ground-truth explanations:
  - `MUTAG`: `1,768` graphs, mutagenicity classification.
  - `Benzene`: `12,000` graphs from ZINC, benzene-ring detection.
  - `Fluoride Carbonyl`: `8,671` graphs, fluoride-plus-carbonyl motif detection.
  - `Alkane Carbonyl`: `4,326` graphs, alkane-plus-carbonyl motif detection.
- Real-world node-classification graphs without ground-truth explanations:
  - `German credit`: `1,000` nodes.
  - `Recidivism`: `18,876` nodes.
  - `Credit defaulter`: `30,000` nodes.
- Data release:
  - GraphXAI datasets hosted on Harvard Dataverse at `10.7910/DVN/KULOS8`.

## Experimental Procedure
- Generate synthetic graphs with built-in node, edge, and node-feature explanations using ShapeGGen.
- Train GNN predictors, including three-layer `GIN` and `GCN` architectures, on synthetic and real-world tasks.
- Run multiple post hoc explainers on the trained GNNs and convert their outputs into comparable explanation objects.
- Evaluate explanations with metrics covering overlap with ground truth, faithfulness to the model, stability under perturbation, and fairness under counterfactual changes.
- Benchmark explainer performance across graph regimes such as homophilic versus heterophilic graphs, small versus large ground-truth explanations, and weakly versus strongly unfair settings.
- Use `70/10/20` train/validation/test splits for the molecular real-world datasets.

## Key Biology Insights
- In molecular-graph settings, the resource treats chemically meaningful motifs such as benzene rings, nitro groups, fluoride atoms, and carbonyl groups as explicit ground-truth rationales, providing a more realistic basis for evaluating scientific graph explanations.
- The results show that explanation reliability is highly dependent on graph structure and task regime, which is important for biological or chemical applications where graph topology and motif size vary substantially.
- Poor explanation faithfulness on larger or more complex motifs suggests that apparently plausible molecular explanations can still be unreliable when used to justify model decisions.

## Implications
- The paper provides a practical benchmark foundation for comparing GNN explainers under controlled conditions instead of ad hoc one-off case studies.
- It suggests that current explanation methods remain insufficient for high-stakes use cases unless they are tested for faithfulness and fairness, not just visual plausibility.
- `GraphXAI` lowers the barrier for future work on explanation robustness, particularly in scientific domains such as chemistry and biology where motif-level reasoning matters.
