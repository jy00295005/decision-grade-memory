# DecisionEpisode Targeted Re-Test Plan

## Purpose

This experiment lane is designed to test a narrower and more defensible claim than a broad system-performance benchmark:

> In contamination-prone SME decision situations, an explicit `DecisionEpisode` layer followed by strict projection can produce a more bounded and decision-useful context package than richer graph retrieval alone.

The purpose of the retest is not to show that `DecisionEpisode` always outperforms every baseline on every case. The purpose is to expose the specific failure mode that motivated the method: semantically related but poorly bounded context.

## Why the earlier comparison was not enough

The earlier four-condition local comparison was useful as a baseline, but it did not create enough separation between `combined_rrf` and `DecisionEpisode + projected subgraph`. Three limitations mattered:

1. The curated cases were too clean.
2. Projection behaved more like light trimming than strict decision bounding.
3. The scoring logic rewarded slot hit coverage more than situation-level coherence.

Because of that, the earlier comparison could show that `DecisionEpisode` was feasible, but not that it was clearly better than `combined_rrf` on the cases where bounded organization should matter most.

## Revised experiment logic

The retest uses two complementary sets:

### 1. Stress-test set

This is the main proof-oriented set.

- Size:
  - `9` local curated cases
- Families:
  - `supplier_moq_cash_pressure`
  - `weekend_staffing_rota_conflict`
  - `sales_decline_conversion_recovery`
- Stress types:
  - `cross_episode_contamination`
  - `multi_action_confusion`
  - `same_trigger_different_goal`

These cases are designed so that `combined_rrf` is likely to retrieve relevant but poorly bounded context, while `DecisionEpisode + strict projection` has a plausible path to a cleaner decision package.

### 2. Full curated regression set

This is the stability-oriented set.

- Purpose:
  - verify that the stricter episode condition does not collapse outside the hardest cases
- Conditions retained:
  - `text_rag`
  - `node_rrf`
  - `combined_rrf`
  - `DecisionEpisode + strict projection`

The regression set should be interpreted as a safety check, not the primary source of the paper’s strongest comparison claim.

## Experimental conditions

### `text_rag`

Plain fragmented text retrieval over local source texts.

Role:

- external baseline
- shows what plain text chunk retrieval can and cannot recover

### `node_rrf`

Node-focused graph retrieval baseline.

Role:

- graph-fragment baseline

### `combined_rrf`

Richer graph retrieval baseline using a broader relation package.

Role:

- strongest non-episode graph baseline
- the main comparator for `DecisionEpisode`

### `DecisionEpisode + strict projection`

The method-facing experimental condition.

Pipeline:

1. Build `DecisionEpisode` from the same local evidence bundle.
2. Prefer `llm_constrained` slot normalization with fallback to rules.
3. Project the episode into a strict, query-time bounded reasoning view.

Role:

- explicit test of whether episode organization improves bounded decision context

## What “strict projection” means

The projection step is intentionally selective.

It keeps:

- slot-linked evidence
- aligned `trigger -> action`
- aligned `action -> goal`
- aligned `action -> outcome`
- aligned `challenge -> constraint`

It drops:

- distractor actions
- adjacent episode evidence pulled in by semantic proximity
- background benefits unless they directly support the current outcome

This matters because the paper’s claim is not that more retrieval is always better. The claim is that decision support benefits from bounded scenario organization.

## Audit support

The current experiment design also relies on a small feasibility-level extraction audit. The audit is not a final accuracy benchmark, but it provides enough structure to score context packages against:

- gold slot text
- primary action refs
- primary goal refs
- allowed context refs
- distractor refs

This is what makes it possible to score not only recovery, but also boundedness and contamination.

## Main scoring dimensions

The current scorer uses four main dimensions:

### `slot_completeness`

Whether the package recovers the key decision slots:

- `trigger`
- `goal`
- `constraints`
- `actions`
- `outcome`

### `slot_traceability`

Whether recovered slots remain attached to evidence refs, rather than appearing as ungrounded summaries.

### `situation_coherence`

Whether the package remains inside one decision situation, rather than mixing neighboring but non-focal context.

### `decision_usefulness`

Whether the package actually supports a plausible decision discussion by jointly recovering:

- the decision goal
- the operative constraints
- a relevant action path

## Intended reading of the results

If the stress-test condition favors `DecisionEpisode + strict projection`, the correct interpretation is:

- bounded episode organization helps when retrieval is vulnerable to contamination or action-goal confusion

The correct interpretation is not:

- `DecisionEpisode` has been broadly validated
- graph retrieval is solved
- extraction quality is already robust

## Current evidential boundary

This experiment lane should support only a bounded empirical claim:

> `DecisionEpisode` shows prototype-level superiority on targeted contamination-prone local cases, while remaining roughly competitive on the broader curated regression set.

Anything stronger should be deferred until there is:

- a larger annotated set
- stronger uncertainty extraction
- richer projection diagnostics
- possibly human or judge-assisted evaluation
