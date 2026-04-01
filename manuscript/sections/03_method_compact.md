# 3. Method: A Scenario Memory Framework for Decision-Grade SME Context

## 3.1 Method objective and problem formulation

This section addresses a methodological problem rather than an implementation problem: how to move from fragment retrieval to decision-grade context construction in SME decision support. Earlier sections argued that SME decisions are often made under uncertainty, resource constraints, uneven information quality, and changing operating conditions. In such settings, useful support requires more than retrieval of relevant passages, summaries, or remembered facts. It requires a representation of the business situation in which goals, constraints, triggers, actions, outcomes, and evidence are made explicit enough to support reasoning.

The core claim of this section is therefore narrow. We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction. This framing does not reject retrieval. Rather, it argues that retrieval alone often leaves the structure of the decision situation implicit. The methodological task is thus to organize heterogeneous business data and signals into bounded contexts that can support explanation and judgment.

![Figure 1. Fragment retrieval, scenario memory, and evidence-backed reasoning.](../figures/fig1_fragment_vs_scenario.png)

*Figure 1. Fragment retrieval, scenario memory, and evidence-backed reasoning. The figure contrasts fragment-oriented support with scenario-oriented context construction and highlights the role of explicit evidence in decision-grade reasoning.*

## 3.2 Scenario memory as the organizing abstraction

In this paper, *scenario memory* is used as a design term for organizing business context around bounded decision situations. It is not presented as a settled standard category in the literature. The term is introduced because existing memory forms often organize information around documents, chat turns, or persistent user facts, whereas decision support requires an organization centered on the episode itself.

Scenario memory therefore denotes a layer that reconstructs a decision-relevant situation rather than simply returning associated fragments. Its purpose is to make explicit how a focal goal, current constraints, triggering conditions, candidate actions, and evidence relate within one business episode.

## 3.3 Structure of a decision episode

The minimum representational unit of the framework is the *decision episode*. A decision episode is defined here as a bounded business situation in which an SME actor or firm pursues a goal under identifiable constraints, encounters a trigger or challenge, takes or considers an action, and interprets outcomes with respect to evidence and temporal context.

Conceptually, the episode may be written as:

`E = (A, G, C, T, X, O, V, tau)`

where `A` denotes actor or business context, `G` the focal goal, `C` operative constraints, `T` a trigger or challenge, `X` an action or decision, `O` an observed or expected outcome, `V` an evidence bundle, and `tau` the temporal placement of the episode. The value of this structure is that it defines what must be assembled if the system is to provide decision-grade context rather than a loose collection of relevant fragments.

![Figure 3. Structure of a decision episode.](../figures/fig3_decision_episode_structure.png)

*Figure 3. Structure of a decision episode. A decision episode is represented as a bounded unit linking actor or business context, goal, constraint, trigger, action, outcome, evidence, and temporal placement.*

## 3.4 Core conceptual components

The design relies on four core conceptual components. `DecisionEpisode` is the central organizing unit. `Constraint` makes pressures and operating limits explicit, reflecting the literature on SME uncertainty, liquidity pressure, and capability limits. `Outcome` captures what followed, what is expected to follow, or what remains unresolved after an action. `EvidenceBundle` provides the basis for representing the episode in a justified rather than purely associative way.

These components should be treated as a minimal design set. Optional extensions such as scenario tags or analogical links across episodes may later be useful, but they are not required for the core methodological claim.

## 3.5 Layered framework for decision-grade context

The framework is organized into four layers. First, graph-based business memory stores heterogeneous business data and signals in a structured form that preserves entities, relations, temporal traces, and evidence links. Second, the scenario memory layer organizes relevant graph context into explicit decision episodes. Third, a decision subgraph assembles a bounded context for the active query or decision task. Fourth, the LLM reasoning layer interprets that prepared context for explanation and support. This layering gives the method a clear division of labor between storage, organization, bounded assembly, and reasoning.

This layered structure captures the paper's central methodological point. Graph-based memory is useful because it preserves distributed business context in an explicit relational form. However, graph memory is not sufficient on its own if the user still has to reconstruct the decision situation from scattered elements. The scenario layer is introduced precisely to organize graph memory into decision episodes that can support bounded context assembly.

![Figure 2. Overall framework for decision-grade SME context construction.](../figures/fig2_framework_overview.png)

*Figure 2. Overall framework for decision-grade SME context construction. Heterogeneous business inputs are organized through graph-based business memory, a scenario memory layer, a decision subgraph, and an LLM reasoning layer.*

## 3.6 Decision subgraph construction view

The decision subgraph is the query-time context view used for a specific decision task. Its role is not simply to return relevant items, but to assemble a bounded representation of the active decision episode. In this sense, the decision subgraph is a context-construction mechanism rather than a raw retrieval result.

This distinction matters because a relevant passage or recalled fact may still leave key issues unresolved: which goal is at stake, which constraints matter most, what triggered the episode, what action is under consideration, and what evidence supports the interpretation. A scenario-oriented subgraph is intended to make those relations sufficiently explicit for reasoning.

## 3.7 Role of the LLM

The LLM is positioned as a reasoning and interaction layer over structured memory, not as the sole repository of business context. Its role is to interpret prepared scenario-aware context, compare alternatives, summarize the logic of the episode, and support explanation. This positioning is consistent with the broader claim of the section: decision support depends on context organization, not on fluent generation alone.

## 3.8 Scope boundaries and status of the design

The framework presented here is a conceptual method design. It is not an empirical validation claim, and it does not assume that scenario memory is already a stabilized term in the literature. Nor does it claim that the proposed design is sufficient for all SME decision domains or that it has already demonstrated superior performance.

The narrower and more defensible claim is that graph-based business memory provides a useful substrate for SME decision support, but that distributed graph context still benefits from explicit organization into decision episodes. The proposed scenario memory layer is intended to provide that organization and thereby support a shift from fragment retrieval to decision-grade context construction.
