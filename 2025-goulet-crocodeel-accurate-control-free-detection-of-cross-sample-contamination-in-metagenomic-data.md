# Paper Summary

## Keywords
metagenomics QC, cross-sample contamination, contamination detection, random forest, species abundance profiles

## Main Idea
CroCoDeEL detects and quantifies cross-sample contamination directly from species-abundance profiles without requiring negative controls or plate-position metadata.

## Evidence Supporting the Main Idea
The method is built on contamination-line patterns in log-scale species-abundance comparisons (Figure 1), then combines engineered features with a pretrained random-forest classifier. Benchmarks on three independent real cohorts show consistent classification performance (reported MCC around 0.7 and high precision/recall behavior in heavily imbalanced data). The authors also report very low false positives when evaluating large numbers of non-contaminated sample pairs and show substantial previously unreported contamination in public datasets.

## Main Novelty
A control-free, decision-support framework that jointly identifies contamination events, contamination direction, and contamination proportion from routine taxonomic profiles.

## Datasets Used for Evaluation
A human-curated semi-simulated training dataset and three independent public human fecal metagenomic test cohorts; additional re-analyses of published cohorts.

## Experimental Procedure
The workflow computes pairwise contamination features from species-abundance vectors, trains a supervised model on curated semi-simulated events, and applies it to all sample pairs in target cohorts. Performance is assessed against human-reported contamination events and by targeted robustness checks on simulated and real settings.
