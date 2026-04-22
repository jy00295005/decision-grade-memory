# Experiments Workspace

This directory stores paper-facing experiment notes, design summaries, and result digests that can support later chapter drafting.

It is intentionally separate from:

- `docs/`
  - planning notes and research workflow documents
- `manuscript/sections/`
  - paper prose
- ProsperPath implementation outputs
  - local prototype artifacts that live in the ProsperPath repository

## Current contents

- `decision_episode_targeted_retest_plan.md`
  - the narrowed experiment design for testing whether `DecisionEpisode` improves bounded decision context over fragment-oriented graph retrieval
- `decision_episode_targeted_retest_results.md`
  - the current paper-facing summary of the targeted stress-test and full regression outputs
- `decision_episode_artifact_index.md`
  - the index of raw ProsperPath artifacts that back the summaries here

## Scope boundary

These files are for:

- preserving a traceable experimental narrative
- supporting later writing of the empirical chapter
- keeping claims conservative and evidence-bounded

These files are not:

- the final paper section
- a product benchmark report
- a claim of large-scale validation

## Working interpretation

At the current stage, the experiment lane supports a prototype-level, local, curated evaluation of `DecisionEpisode` as a bounded context-construction layer. It does not yet support strong claims about large-scale extraction accuracy, business impact, or robust superiority across all retrieval settings.
