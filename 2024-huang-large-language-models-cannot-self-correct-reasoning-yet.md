# Paper Summary

### Authors
Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou

### Journal
ICLR 2024 conference paper

### Publication Date
March 14, 2024 (arXiv v2; published at ICLR 2024)

### DOI
Not specified in paper

## Keywords
Large language models; intrinsic self-correction; reasoning; self-consistency; multi-agent debate; external feedback; verifier.

## Main Idea
LLMs generally cannot reliably correct their own reasoning using only intrinsic feedback. When the model must decide whether its answer is wrong and when to stop, self-correction often changes correct answers into incorrect ones and lowers accuracy. Apparent gains in earlier work largely depend on oracle labels, unequal inference budgets, or incomplete initial prompts.

## Evidence Supporting the Main Idea
- On GSM8K, CommonSenseQA, and HotpotQA, oracle-label self-correction improves GPT-3.5 from 75.9/75.8/26.0 to 84.3/89.7/29.0 and GPT-4 from 95.5/82.0/49.0 to 97.5/85.5/59.0. The oracle tells the process when the answer is correct, so it is not available in ordinary problem solving.
- Without oracle labels, GPT-3.5 falls after two rounds from 75.9 to 74.7 on GSM8K, 75.8 to 41.8 on CommonSenseQA, and 26.0 to 25.0 on HotpotQA. GPT-4 falls from 95.5 to 89.0 on GSM8K and from 49.0 to 43.0 on HotpotQA.
- For GSM8K, GPT-3.5 retains its initial answer 74.7% of the time after two rounds; among changed answers, it is more likely to turn a correct answer into an incorrect one than to repair an incorrect answer.
- With equal numbers of responses on GSM8K, multi-agent debate does not beat self-consistency: with six responses, debate scores 83.2 while self-consistency scores 85.3; with nine, debate scores 83.0 while self-consistency scores 88.2.
- On constrained generation, adding the full requirement to the initial prompt produces 81.8, while applying the self-correction prompt afterward produces 75.1, illustrating the confounding effect of prompt design.

## Main Novelty
The paper isolates **intrinsic** self-correction from correction guided by ground-truth labels, tools, humans, or other external signals, then evaluates it under matched inference cost and stronger initial prompts. It turns the stopping decision itself into the central difficulty rather than treating it as a free oracle operation.

## Datasets Used for Evaluation
- **GSM8K:** 1,319 linguistically diverse grade-school math word problems in the test set; used for mathematical reasoning and multi-agent/self-consistency comparisons.
- **CommonSenseQA:** 1,221 development-set multiple-choice commonsense questions; used for answer-correction evaluation.
- **HotpotQA:** 100 closed-book open-domain multi-hop questions in the matched evaluation set; exact match used.
- **CommonGen-Hard:** constrained-generation benchmark used for the prompt-design experiment; the paper reports scores but does not specify the benchmark size in the cited section.

## Experimental Procedure
- Evaluate GPT-3.5-Turbo and GPT-4 with oracle labels, then GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, and Llama-2-70B-chat without external correctness labels.
- Generate an initial answer, ask the model to critique it, and ask it to answer again; allow up to two correction rounds and report both accuracy and model-call count.
- Vary feedback prompts to test whether a prompt alone can rescue intrinsic correction.
- Compare multi-agent debate with self-consistency at equal response counts on GSM8K.
- Replicate a constrained-generation setting with a complete initial instruction to separate genuine correction from information introduced only in the feedback prompt.

## Key Biology Insights
Not specified in paper. The benchmarks concern language, mathematics, commonsense, and multi-hop question answering.

## Implications
A model should not be trusted to stop or revise solely because it declares its own reasoning wrong. Reliable stopping needs an independent signal: executable tests, calculators/search/tools, a trained verifier, human feedback, or another validated external evaluator. Evaluations should compare equal inference budgets, include self-consistency baselines, and put the full task specification in the initial prompt. In the terms of the paper, “thinking longer” without a better correctness signal can make the answer worse.
