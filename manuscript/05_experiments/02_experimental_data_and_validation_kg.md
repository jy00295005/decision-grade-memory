# 5.2 Experimental Data, Corpus Construction, and Validation KG

## 5.2.1 Source assets and provenance

The current experiment does not rely on open real-world firm data or on a production-scale enterprise graph. Instead, it uses the current ProsperPath prototype assets as a local, curated, paper-facing validation substrate. These assets include mock conversational traces, derived recommendation outputs, graph-linked decision traces, and supporting local artifacts that together make it possible to construct bounded SME decision situations for inspection.

This provenance matters for the scope of the paper's empirical claims. Because the materials are local and curated, the resulting evidence can support prototype validation, method illustration, and narrow comparative testing. It cannot support broad claims about external validity, general SME coverage, or production readiness. The experiment should therefore be read as a structured validation exercise over a local corpus rather than as a field benchmark.

## 5.2.2 Decision situations and task families

The corpus is organized around `decision situations` rather than around broad company histories. A decision situation is a bounded evaluation case consisting of a focal decision query, a recognizable business problem, a graph-backed context bundle, and one or more candidate actions that can be related to constraints, goals, and outcomes. This unit is appropriate for the current stage of the work because the implementation does not yet expose a stable ground-truth `DecisionEpisode` object that can function directly as the evaluation unit.

The current corpus focuses on three recurring task families that are both SME-relevant and sufficiently represented in the available materials:

- supplier MOQ pressure under cash-flow constraints
- weekend staffing or rota conflict under service constraints
- sales decline recovery under attribution uncertainty

These families were chosen because they involve practical short-horizon decisions rather than generic descriptive questions. Each requires more than isolated facts. A usable context package should expose some combination of triggering problem, operative constraint, candidate response, target state, and partial consequence.

## 5.2.3 Representative source asset types

Although the current paper does not reproduce the full ProsperPath repository structure in the main text, the local validation corpus is built from a small number of recurring asset types. In practical terms, four source types are especially important.

First, chat-like traces provide the initial problem framing. These materials contain owner-facing business concerns, operational pressures, and natural-language descriptions of what needs attention. They supply much of the raw wording for the focal decision query and for the trigger side of the later graph representation.

Second, recommendation outputs provide candidate actions and action rationales. These artifacts are important because they turn business pressure into inspectable response options rather than leaving the corpus at the level of problem description alone.

Third, derived graph traces provide typed relations among challenges, actions, goals, and partial outcomes. These relations make it possible to distinguish between a merely relevant fragment and a decision-aligned path through the local graph.

Fourth, local evidence references provide the grounding layer later used for validation. They make it possible to trace a recovered slot back to a supporting node, edge, or derived trace rather than treating the experiment as ungrounded summarization.

Taken together, these source types make the current corpus richer than a plain text collection while still remaining local and prototype-facing.

## 5.2.4 Representative decision-situation examples

The current corpus can be understood more concretely through three compact examples, each corresponding to one of the recurring task families.

### Supplier MOQ under cash pressure

A representative supplier case asks what bounded supplier response should be taken when minimum-order-quantity pressure collides with holiday cash strain. In this type of case, the trigger comes from supplier pressure, the constraint comes from short-horizon cash protection, the action trace centers on split shipment or smaller opening-order responses, and the partial goal is to preserve replenishment flexibility without worsening liquidity pressure.

### Weekend staffing under service constraints

A representative staffing case asks what bounded staffing response should address weekend rota conflict without drifting into unrelated sales-recovery tactics. In this type of case, the trigger is a rota or shift-coverage problem, the constraint is service continuity, the action trace centers on standby shift or swap workflows, and the evaluative question is whether the package stays inside the staffing episode rather than mixing in adjacent commercial interventions.

### Sales decline recovery under attribution uncertainty

A representative sales case asks what bounded conversion-recovery response should follow an October decline when attribution remains unclear. In this type of case, the trigger is declining revenue or conversion, the constraint is attribution uncertainty and short-term decision pressure, the action trace centers on bundle or channel-adjustment interventions, and the key issue is whether the package preserves the conversion-recovery path rather than importing supplier or cash-protection tactics.

These examples are intentionally small. Their function is not to present full case records, but to show the reader what a usable decision situation looks like in the current validation corpus.

## 5.2.5 Curated case construction

Within these task families, the evaluation corpus is not assembled as an arbitrary set of queries. Cases are curated to represent bounded decision situations with enough inspectable structure for comparison. A usable case must contain at least three kinds of material: a problem trace, an action or recommendation trace, and a goal, benefit, or outcome fragment that makes the decision situation interpretable as more than a disconnected retrieval bundle.

The targeted re-test further refines this curation by adding specific stress patterns. The stress-test set contains cases that instantiate one of three designed difficulties:

- `cross_episode_contamination`
- `multi_action_confusion`
- `same_trigger_different_goal`

These stress types are important because they create situations in which relation-rich retrieval may remain relevant but insufficiently bounded. In other words, the experiment corpus is not only a set of business examples. It is also a controlled way of exposing where bounded episode organization should matter.

## 5.2.6 What counts as a usable decision situation

The current validation corpus uses conservative inclusion logic. A case is usable when it is clearly decision-oriented, SME-relevant, and supported by enough graph-linked material to compare competing context-construction strategies. In practice, this means the case should expose at least one challenge, crisis, or business-pressure trace; at least one recommendation or action path; and at least one goal, benefit statement, or partial outcome indication.

Cases dominated by generic owner metadata, weakly connected retrieval noise, or missing action pathways should be excluded. Likewise, a case that retrieves many semantically adjacent fragments but cannot be interpreted as a bounded decision situation is not appropriate for this evaluation. This conservative filtering is important because the experiment aims to compare context organization quality, not retrieval breadth in the abstract.

## 5.2.7 From local corpus to validation KG

The validation KG used in this experiment is not a separate graph built exclusively for the paper. It is the graph substrate implied by the current ProsperPath local assets and their derived traces. The corpus contributes the textual and semi-structured materials, while the derived outputs contribute typed relations, recommendation/action associations, and local evidence references that make bounded comparison possible.

Operationally, the corpus-to-graph transformation preserves the paper's methodological distinction between raw source material and decision-support structure. Source texts, local outputs, and recommendation traces do not function directly as the evaluation object. Instead, they are mapped into graph-backed entities, relations, and support traces that can be assembled into graph retrieval packages and, later, into `DecisionEpisode` objects.

## 5.2.8 Validation KG composition example

A representative local graph fragment for the current experiment can be described as a compact challenge-action-goal-outcome structure anchored by evidence references. In a supplier MOQ case, for example, the graph may contain a challenge node representing supplier minimum-order-quantity pressure, an action or recommendation node representing split shipment or smaller opening-order tactics, a goal node representing cash preservation or replenishment flexibility, and a partial outcome node indicating whether the pressure was mitigated. These nodes are then connected by typed edges such as `ADDRESSES`, `SUPPORTS`, or other relation-backed traces that preserve the local decision structure.

![Figure 6: Local validation KG fragment for a bounded SME decision situation](../figures/fig6_validation_kg_fragment.png)

*Figure 6. A local validation KG fragment for a bounded supplier MOQ decision situation. The graph is intentionally small and decision-centered. It preserves the challenge-action-goal-outcome structure needed for later episode construction, while keeping evidence references visible enough to support traceability during validation.*

This is important for the paper because the validation KG is not merely a storage substrate. It is the layer that makes episode-oriented comparison possible. The later `DecisionEpisode` object does not arise from raw text alone. It arises from a graph-backed local structure in which challenge, action, goal, and evidence can already be related to one another in inspectable form.

Figure 6 illustrates this point more effectively than a full graph screenshot would. For the present paper, the most informative visualization is a small decision-centered subgraph showing the challenge-action-goal-outcome pattern and the evidence-linked traces that support later projection. A full graph screenshot would be far less useful because the experiment depends on bounded local structure rather than on total graph scale.

## 5.2.9 What the validation KG contains

The current validation KG contains enough representational structure to support prototype-level comparison. It includes business entities and business-state references associated with the selected decision situations. It also includes relation-backed traces linking problem statements, actions, recommendations, and partial outcomes. These traces make it possible to distinguish between a package that merely surfaces relevant fragments and one that organizes them into a more interpretable decision context.

At a practical level, the current validation KG contains the following kinds of material:

- entities tied to focal business actors, operational conditions, and business objects
- relations connecting business problems, actions, goals, and partial outcomes
- recommendation or action traces that can be linked back to specific decision contexts
- goal and outcome fragments that make success criteria or consequences partially visible
- evidence references that allow slot-level grounding in later validation

This is sufficient for the current empirical purpose because the experiment is not trying to validate end-to-end world modeling. It is trying to test whether bounded organization over a graph-backed substrate improves decision-context construction.

## 5.2.10 What the validation KG does not yet contain

The current validation KG remains limited in several important ways. It does not yet provide a robust uncertainty layer, so explicit missing-information modeling is still weak. It also does not contain stable ground-truth `DecisionEpisode` objects that could serve as authoritative supervision targets for large-scale extraction evaluation. In addition, its coverage is local and curated rather than production-scale, which limits what can be claimed about generalization.

These limits matter for the framing of the experiment. The validation KG is strong enough to support a prototype comparison between bounded and less-bounded context construction strategies. It is not strong enough to support robust claims about extraction accuracy in the large, broad enterprise applicability, or downstream business impact.

## 5.2.11 Why this data substrate is still useful for the paper

Despite these limits, the current data and validation KG are appropriate for the paper's present stage. They provide exactly what is needed for a narrow empirical test: repeated SME-like decision situations, inspectable action and goal traces, relation-backed local evidence, and sufficient variation to create contamination-prone cases. This makes it possible to test the paper's central methodological intuition under controlled conditions, while remaining explicit that the evidence base is still prototype-level and curated.
