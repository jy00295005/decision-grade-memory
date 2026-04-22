# DecisionEpisode Artifact Index

This file records the ProsperPath artifacts that currently back the experiment notes in this repository.

## ProsperPath paper-facing summaries

- [README.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/README.md)
- [episode_audit_summary.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/episode_audit_summary.md)
- [projection_examples.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/projection_examples.md)
- [decision_context_comparison_stress_summary.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/decision_context_comparison_stress_summary.md)
- [decision_context_comparison_full_summary.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/decision_context_comparison_full_summary.md)
- [decision_context_pairwise_summary.md](/Users/chen/Documents/code/finley/prosperpath/docs/paper_results/decision_episode_prototype_validation/decision_context_pairwise_summary.md)

## ProsperPath raw outputs

### Audit

- [episode_audit_gold.json](/Users/chen/Documents/code/finley/prosperpath/output/episode_audit/episode_audit_gold.json)
- [episode_audit_results.json](/Users/chen/Documents/code/finley/prosperpath/output/episode_audit/episode_audit_results.json)
- [episode_audit_report.md](/Users/chen/Documents/code/finley/prosperpath/output/episode_audit/episode_audit_report.md)

### Projection

- [projection_examples.json](/Users/chen/Documents/code/finley/prosperpath/output/decision_subgraph_projection/projection_examples.json)
- [projection_examples.md](/Users/chen/Documents/code/finley/prosperpath/output/decision_subgraph_projection/projection_examples.md)

### Comparison

- [decision_context_comparison_stress_results.json](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_stress_results.json)
- [decision_context_comparison_stress_results.csv](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_stress_results.csv)
- [decision_context_comparison_stress_summary.md](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_stress_summary.md)
- [decision_context_comparison_full_results.json](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_full_results.json)
- [decision_context_comparison_full_results.csv](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_full_results.csv)
- [decision_context_comparison_full_summary.md](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_comparison_full_summary.md)
- [decision_context_pairwise_summary.md](/Users/chen/Documents/code/finley/prosperpath/output/experiments/decision_context_pairwise_summary.md)

## How to use these artifacts in the paper repo

Use the Markdown summaries in this repository as the default drafting surface.

Use the ProsperPath raw files only when you need:

- case-level evidence
- exact tables or counts
- appendix-ready traceability material
- a check against overclaiming

## Current boundary

These artifacts support:

- prototype validation
- bounded stress-test comparison
- instance-level explanation of `DecisionEpisode`

They do not yet support:

- claims of robust extraction accuracy
- claims of broad benchmark superiority
- claims of downstream SME business impact
