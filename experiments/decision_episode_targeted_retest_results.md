# DecisionEpisode Targeted Re-Test Results

## Status

The ProsperPath prototype now supports a targeted re-test that is materially stronger than the earlier “flat” comparison. The new result is useful for the paper because it no longer asks only whether `DecisionEpisode` exists; it asks whether `DecisionEpisode` is better at preserving bounded decision context on cases where contamination is likely.

## Main finding

On the stress-test set, `DecisionEpisode + strict projection` outperformed `combined_rrf`.

Stress-test averages:

| condition | completeness | traceability | usefulness | coherence |
| --- | ---: | ---: | ---: | ---: |
| `combined_rrf` | 4.02 | 3.64 | 2.74 | 3.83 |
| `DecisionEpisode + strict projection` | 4.27 | 4.50 | 3.93 | 5.00 |

Pairwise stress-test outcomes:

- `DecisionEpisode` wins: `6`
- `combined_rrf` wins: `1`
- ties: `2`

## What this result does support

This result supports a narrow and useful statement:

> In contamination-prone decision situations, an episode-bounded projection can preserve a cleaner and more decision-useful context package than richer graph retrieval alone.

That is the strongest defensible reading of the current result.

## Why `DecisionEpisode` won on the stress-test set

The pairwise summaries point to a consistent mechanism:

- distractor actions were dropped
- non-focal adjacent episode evidence was excluded
- the primary action-goal path was preserved more cleanly

This is important because the gain is not just “more evidence” or “more nodes.” The gain is boundedness.

## Where the result is still weak

The same retest also shows that the current `DecisionEpisode` lane is not yet universally stronger.

### Same-trigger-different-goal remains difficult

The hardest unresolved cases are those where:

- the same business trigger can legitimately support more than one decision goal
- the current evidence bundle does not sharply separate those goals

That is where the current pipeline still ties or loses.

### Full regression does not show universal superiority

The broader local regression set remains more mixed:

| condition | completeness | traceability | usefulness | coherence |
| --- | ---: | ---: | ---: | ---: |
| `text_rag` | 3.06 | 0.54 | 3.25 | 5.00 |
| `node_rrf` | 3.79 | 3.94 | 3.86 | 5.00 |
| `combined_rrf` | 4.46 | 4.57 | 3.93 | 5.00 |
| `DecisionEpisode + strict projection` | 4.24 | 4.46 | 3.86 | 5.00 |

This means the current paper should not claim that `DecisionEpisode` broadly dominates `combined_rrf`. The safer reading is:

- `DecisionEpisode` is especially valuable on hard, contamination-prone cases
- `combined_rrf` remains competitive on cleaner regression cases

## Extraction audit boundary

The extraction audit remains feasibility-level rather than strong validation.

What looks relatively stable:

- `actions`
- `trigger`
- some `goal` recovery

What remains clearly weak:

- `constraints`
- `uncertainties`
- fully reliable `focus` recovery

This matters because the experiment chapter should not silently turn “inspectable prototype extraction” into “robust episode extraction.”

## Working paper language

The current results are strong enough to support wording like:

> The prototype `DecisionEpisode` layer showed targeted superiority on local contamination-prone stress cases, where stricter episode-bounded projection improved coherence, traceability, and decision usefulness relative to richer graph retrieval alone.

But they are not strong enough to support wording like:

- `DecisionEpisode consistently outperformed combined_rrf across the evaluation set`
- `DecisionEpisode extraction is robust`
- `the system improves SME outcomes`

## What this means for the paper workflow

These results are now useful for two later writing moves:

1. an implementation-grounded instance-validation subsection
2. a narrow empirical subsection on targeted stress-test superiority

The results are not yet a substitute for a fully mature experiments chapter.
