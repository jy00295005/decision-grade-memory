# 5.1 Experiment Design

## 5.1.1 Evaluation objective and bounded empirical claim

This experiment section evaluates a narrow empirical question derived from the paper's method claim. Section 3 argued that a graph substrate alone is not sufficient for decision-grade support in SME contexts. The proposed contribution is an intermediate `DecisionEpisode` layer that organizes distributed business traces into bounded decision situations before query-time reasoning. The empirical objective is therefore not to establish broad product performance, firm-level business impact, or universal superiority of graph-based AI systems. It is to test whether an explicit episode-oriented organization layer can improve decision-context construction under controlled comparison conditions.

The bounded empirical claim is correspondingly narrow. The experiment asks whether, when the underlying business graph and query intent are held constant, `DecisionEpisode`-oriented context construction can produce a more bounded and decision-useful context package than fragment-oriented or relation-rich retrieval alone. The most defensible version of this claim is local and conditional: if gains appear, they should be interpreted as evidence that episode-bounded organization helps in contamination-prone SME decision situations, not as evidence that the overall system has been comprehensively validated.

## 5.1.2 Why the earlier pilot design was no longer sufficient

The earlier evaluation design and preliminary pilot established a useful starting point. They compared fragment-oriented retrieval with a scenario-oriented proxy over the same graph and showed that richer relational context could improve completeness and traceability on a small number of cases. However, that earlier design was not sufficient for the current paper objective for three reasons.

First, the original pilot cases were relatively clean. They were adequate for showing feasibility, but they did not create enough pressure on the comparison to reveal whether `DecisionEpisode` actually improves bounded reasoning under ambiguity. Second, the previous scenario-oriented condition was still close to a richer retrieval bundle. It improved relational exposure, but it did not yet sharply separate focal decision context from adjacent but non-focal material. Third, the earlier scoring logic emphasized contextual richness more than situation-level boundedness. This made it difficult to distinguish a package that was simply richer from a package that was more decision-grade in the sense intended by the method.

For these reasons, the current experiment should be understood as a targeted re-test rather than a simple extension of the first pilot. Its purpose is to probe the specific failure mode that motivates the paper: the retrieval of semantically related but insufficiently bounded context.

## 5.1.3 Revised experiment logic

The revised experiment is organized around two complementary evaluation sets. The first is a targeted stress-test set designed to expose cases in which richer retrieval is likely to blur episode boundaries. The second is a broader curated regression set designed to check that the stricter episode-oriented condition does not collapse outside those hardest cases.

The stress-test set is the main proof-oriented comparison. It contains local curated decision situations from three recurring task families: supplier minimum-order-quantity pressure under cash constraints, weekend staffing or rota conflict under service constraints, and sales decline recovery under attribution uncertainty. Within these task families, the stress cases are constructed to represent three recurrent difficulties: `cross_episode_contamination`, `multi_action_confusion`, and `same_trigger_different_goal`. These are precisely the kinds of situations in which the paper expects a bounded episode layer to matter most.

The full curated regression set plays a different role. It is not the main source of the paper's strongest empirical statement. Instead, it functions as a stability check. If `DecisionEpisode` only wins on stress cases but catastrophically degrades outside them, the argument for bounded organization would remain weak. The regression set therefore tests whether the stricter condition remains broadly competitive even when the case is cleaner and richer retrieval is already strong.

## 5.1.4 Experimental conditions

The current design uses four context-construction conditions, although only two are central to the main targeted claim.

`text_rag` is a plain fragmented text retrieval baseline over local textual materials. It acts as an external baseline and helps clarify that the paper is not only comparing graph variants against each other. It also provides a lower-bound comparison for what can be recovered from fragmented text chunks without stronger structural organization.

`node_rrf` is the graph-fragment baseline. It retrieves node-level graph material without stronger bounded organization into a single decision situation. This condition remains useful because it approximates a common graph retrieval pattern: the system returns relevant fragments, but leaves the user to reconstruct the decision situation.

`combined_rrf` is the strongest non-episode graph baseline and the main comparator for `DecisionEpisode`. It provides a richer graph package than `node_rrf` by exposing additional relational material. It is therefore a more demanding baseline than fragment-only retrieval. In the current experiment, `combined_rrf` should be interpreted as relation-rich retrieval, not as an explicit episode layer.

`DecisionEpisode + strict projection` is the method-facing condition. It first constructs an explicit `DecisionEpisode` object from the same local evidence bundle, preferring constrained LLM-based slot normalization with rules-based fallback. It then projects that episode into a strict, query-time bounded view. This condition is intended to test not whether more information can be retrieved, but whether bounded episode organization can produce a cleaner reasoning package from the same information source.

## 5.1.5 Same-source comparison logic

The comparison logic is intentionally same-source. Across conditions, the underlying information source remains fixed: the graph substrate, the case definition, the local decision query, and the general retrieval budget are held constant unless a stated methodological reason requires otherwise. What changes is the way the context package is assembled and bounded.

This same-source design is critical for the paper's logic. The experiment is not asking whether one system has access to more information than another. It is asking whether one organizational strategy makes the same information more useful for bounded SME decision support. This is why the experiment should be described as a decision-context construction comparison rather than as a system benchmark.

## 5.1.6 Main proof set versus safety-check set

The primary claim in the paper should rest on the stress-test set rather than on the full regression set. The stress-test set is where the method has the clearest theoretical reason to help: when semantically related evidence is available, but the decision boundary is easy to blur. If `DecisionEpisode + strict projection` performs better there, that result is informative because it aligns with the method's intended function.

The full curated regression set should be used more cautiously. It is valuable because it shows whether the stricter condition remains broadly serviceable, but it is not the right basis for claiming strong average superiority. A mixed regression pattern is compatible with the paper's argument, so long as the stress-test superiority remains clear and the limits of the broader result are explicitly stated.

## 5.1.7 Non-claims and evidential boundary

This experiment does not validate business effectiveness, production readiness, or a mature end-to-end scenario memory system. It does not show that `DecisionEpisode` extraction is robust in the large-scale sense, nor does it establish a live benchmark over production-scale enterprise graphs. The current evidence is prototype-level, local, and curated.

Accordingly, the strongest legitimate interpretation of the experiment is narrow. If the targeted stress-test favors `DecisionEpisode + strict projection`, the result supports the claim that bounded episode organization can improve coherence, traceability, and decision usefulness in contamination-prone decision situations. It does not support the stronger claim that `DecisionEpisode` universally dominates richer graph retrieval across all settings or that the system improves SME outcomes in practice.
