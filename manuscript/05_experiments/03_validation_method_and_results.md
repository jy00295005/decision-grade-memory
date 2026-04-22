# 5.3 Validation Method and Results

## 5.3.1 Why the earlier evaluation-design notes are no longer sufficient as-is

The earlier evaluation-design notes were useful for defining the original pilot logic, the initial baselines, and the first-round scoring ideas. However, they were written before the current targeted re-test was completed. As a result, they no longer fully describe the actual validation path used in the most informative comparison round.

The current section therefore serves a different purpose. It does not replace the earlier notes, but it rewrites the validation method in light of the experiment that has now actually been run. In particular, it reflects three changes in the empirical setup: the move from a simple pilot to a targeted stress-test, the introduction of a stricter episode-bounded projection step, and the shift from general contextual richness toward explicit measurement of boundedness, coherence, and contamination.

## 5.3.2 Validation unit and audit support

The primary validation unit in the current experiment remains the `decision situation`, not a final mature `DecisionEpisode` object. This choice reflects the current state of the implementation and the current evidential boundary. While the system now contains an explicit `DecisionEpisode` layer, the evaluation still operates over curated decision situations because these provide the cleanest unit for controlled comparison across conditions.

To support scoring, the current experiment also uses a small feasibility-level extraction audit. The role of this audit is limited but important. It does not function as a full extraction benchmark. Instead, it provides enough structured reference information to evaluate whether a context package recovers the relevant decision slots and whether it remains inside the intended decision boundary. The audit therefore supports later scoring of both slot recovery and contamination-related errors.

## 5.3.3 Validation pipeline

The current validation pipeline compares context-construction conditions over the same underlying local graph substrate and the same focal decision situation. For each case, a context package is first built under the relevant baseline condition. In the method-facing condition, a `DecisionEpisode` object is then constructed from the same evidence bundle, with constrained LLM-based slot normalization preferred and rules-based recovery used as fallback when necessary. That episode is subsequently projected into a strict, query-time bounded reasoning view.

The key point is that the method-facing condition is not given a different underlying information source. What changes is the organization logic applied to that source. This is why the result can be interpreted as evidence about context construction rather than about information access.

## 5.3.4 Conditions used in the validation

The broader comparison framework retains four conditions: `text_rag`, `node_rrf`, `combined_rrf`, and `DecisionEpisode + strict projection`. However, the targeted empirical claim in this section rests primarily on the comparison between `combined_rrf` and `DecisionEpisode + strict projection`.

`combined_rrf` is the appropriate main comparator because it is the strongest non-episode graph baseline in the current setup. It already exposes richer relational structure than node-only retrieval, which makes it a demanding baseline. If `DecisionEpisode` can outperform it on hard cases, that result is substantially more meaningful than merely outperforming fragmented retrieval.

`DecisionEpisode + strict projection` is the method-facing condition because it introduces two linked operations: explicit episode organization and strict bounded projection. The projection stage is essential. Without it, the episode condition would risk collapsing back into a richer but weakly bounded package. The current validation therefore tests not only whether `DecisionEpisode` can be constructed, but also whether strict episode-bounded projection yields a cleaner reasoning view.

## 5.3.5 Scoring design

The current scorer uses four primary dimensions: `slot_completeness`, `slot_traceability`, `situation_coherence`, and `decision_usefulness`. These dimensions are narrower and more structurally aligned with the method than the earlier, broader pilot rubric.

`slot_completeness` evaluates whether the package recovers the core components of the decision situation, especially `trigger`, `goal`, `constraints`, `actions`, and `outcome`. `slot_traceability` evaluates whether recovered material remains visibly grounded in evidence references rather than appearing as unsupported synthesis. `situation_coherence` evaluates whether the package remains within a single decision situation rather than mixing adjacent but non-focal content. `decision_usefulness` evaluates whether the package supports a plausible decision discussion by jointly recovering the decision goal, operative constraints, and an aligned action path.

The shift toward coherence and contamination matters because the paper's empirical question is not simply whether richer packages retrieve more relevant information. It is whether they preserve a bounded decision structure.

## 5.3.6 Stress-test results

The targeted stress-test set provides the most informative current result. On this set, `DecisionEpisode + strict projection` outperformed `combined_rrf`.

| condition | completeness | traceability | usefulness | coherence |
| --- | ---: | ---: | ---: | ---: |
| `combined_rrf` | 4.02 | 3.64 | 2.74 | 3.83 |
| `DecisionEpisode + strict projection` | 4.27 | 4.50 | 3.93 | 5.00 |

The pairwise outcomes on the stress-test set were:

- `DecisionEpisode` wins: `6`
- `combined_rrf` wins: `1`
- ties: `2`

This pattern supports a narrow but meaningful interpretation. On contamination-prone local cases, the episode-oriented condition produced cleaner, more bounded context packages than richer retrieval alone. The main mechanism visible in the case-level summaries is not that the episode condition simply retrieved more material. Rather, it dropped distractor actions, excluded adjacent episode evidence, and preserved the primary action-goal path more cleanly.

## 5.3.7 Why the method wins on the hardest cases

The case-level results suggest that the advantage of `DecisionEpisode + strict projection` lies in boundedness rather than in retrieval breadth. On `cross_episode_contamination` cases, the episode condition benefited from explicitly removing semantically related but non-focal material. On `multi_action_confusion` cases, it more clearly preserved the action path aligned with the focal decision goal. These are exactly the circumstances under which a dedicated episode layer should be useful according to the method argument in Section 3.

![Figure 7: Comparison of context-construction outputs for the same SME decision situation](../figures/fig7_episode_projection_comparison.png)

*Figure 7. Comparison of context-construction outputs for the same decision situation. The `combined_rrf` panel preserves relevant but weakly bounded peripheral context, whereas `DecisionEpisode + strict projection` preserves a narrower challenge-action-goal-outcome path by removing distractor material. The figure is intended to visualize the mechanism behind the stress-test gains, not to function as a benchmark result on its own.*

This matters for the paper because it connects the empirical result back to the conceptual claim. The argument was never that richer retrieval is always inferior. The argument was that retrieval without bounded organizational structure can remain decision-incomplete even when it is relevant. The stress-test superiority result is the first local evidence supporting that claim.

## 5.3.8 Full regression results and why they do not support universal superiority

The broader full curated regression set yields a more mixed result:

| condition | completeness | traceability | usefulness | coherence |
| --- | ---: | ---: | ---: | ---: |
| `text_rag` | 3.06 | 0.54 | 3.25 | 5.00 |
| `node_rrf` | 3.79 | 3.94 | 3.86 | 5.00 |
| `combined_rrf` | 4.46 | 4.57 | 3.93 | 5.00 |
| `DecisionEpisode + strict projection` | 4.24 | 4.46 | 3.86 | 5.00 |

This table should be interpreted carefully. It does not show universal superiority of the episode condition. On the broader curated set, `combined_rrf` remains competitive and in some dimensions slightly stronger. This is not fatal to the paper's claim, because the method is not primarily motivated by already-clean cases. It is motivated by ambiguity, contamination, and action-goal confusion. The broader regression result therefore functions as a safety check, not as the primary source of the paper's strongest conclusion.

## 5.3.9 Extraction audit limits

The extraction audit remains feasibility-level. It shows that some elements of the current `DecisionEpisode` pipeline are relatively stable, especially `actions`, `trigger`, and parts of `goal` recovery. It also shows clear weaknesses: `constraints` remain uneven, `uncertainties` remain poorly recovered, and fully reliable `focus` recovery has not yet been achieved.

These limits must remain visible in the write-up. The current experiment validates an inspectable prototype extraction-and-projection pipeline. It does not validate robust episode extraction in the strong sense. Any wording that blurs this distinction would overstate the evidence.

## 5.3.10 What the results support and what they do not support

The current results support a narrow statement:

> The prototype `DecisionEpisode` layer showed targeted superiority on local contamination-prone stress cases, where strict episode-bounded projection improved coherence, traceability, and decision usefulness relative to richer graph retrieval alone.

The current results do not support stronger statements such as:

- `DecisionEpisode` consistently outperformed `combined_rrf` across the evaluation set
- `DecisionEpisode` extraction is robust
- the system has been validated at production scale
- the method improves SME business outcomes

This boundary is important for the integrity of the paper. The current validation is already strong enough to support an implementation-grounded instance-validation subsection and a narrow empirical subsection on targeted stress-test superiority. It is not yet strong enough to anchor a broad results chapter without qualification.
