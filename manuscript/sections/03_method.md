# 3. Method: A Scenario Memory Framework for Decision-Grade SME Context

## 3.1 Method objective and organizing abstraction

This section addresses a representation problem in SME decision support: how to move from fragment retrieval to decision-grade context construction. Prior sections argued that SME decisions are often made under uncertainty, resource constraints, uneven information quality, and dynamic operating conditions. In such settings, relevant information is rarely contained in a single source. Instead, it is distributed across business records, external signals, prior interactions, and evolving operating conditions. Retrieval can surface useful fragments from that distributed context, but fragment access is not equivalent to decision support. Decision support requires a bounded representation of the business situation in which goals, constraints, triggers, actions, outcomes, and evidence are organized in a form suitable for reasoning.

We therefore propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction. The point is not to replace retrieval, but to make retrieval subordinate to a more suitable unit of organization. In this framing, graph-based business memory remains important because it can preserve entities, relations, temporal structure, and evidence traces across heterogeneous inputs. Yet graph memory alone is not sufficient if the decision situation remains implicit and must still be reconstructed by the user or by the reasoning layer on demand.

The term *scenario memory* is used here as a design term rather than as a standardized category in the literature. It denotes an organizing abstraction centered on bounded decision situations. This distinguishes it from document memory, which is organized around source texts; from conversational memory, which is organized around turns or threads; and from persistent user memory, which is organized around relatively stable facts or preferences. The narrower claim of this section is that these memory forms often leave episode structure under-specified when the task is decision support rather than general assistance.

[Figure 1 about here]

## 3.2 Decision episode representation

The minimum representational unit of the framework is the *decision episode*. We define a decision episode as a bounded business situation in which an SME actor or firm pursues a goal under identifiable constraints, encounters a trigger or challenge, takes or considers an action, and interprets outcomes with respect to supporting evidence and temporal context. This definition is intentionally compact: it is not a full ontology of business activity, but the smallest representation that can support decision-grade context construction.

Conceptually, a decision episode may be expressed as `E = (A, G, C, T, X, O, V, tau)`, where `A` denotes actor or business context, `G` the focal goal, `C` operative constraints, `T` a trigger or challenge, `X` an action or decision, `O` an observed or expected outcome, `V` an evidence bundle, and `tau` temporal placement. The purpose of this formulation is not formalism for its own sake. Its purpose is to specify what must be assembled if the system is to move beyond loosely related fragments toward an interpretable decision context.

The framework relies on four core conceptual components. `DecisionEpisode` is the organizing unit that binds the situation into a coherent context for reasoning. `Constraint` makes explicit the operating limits and pressures that shape feasible action, which is especially important in SMEs given the literature on liquidity pressure, staffing limits, uncertainty, and weakly structured decision conditions. `Outcome` captures what followed, what is expected to follow, or what remains unresolved after an action or decision; without it, the framework would reconstruct problem state but not consequence structure. `EvidenceBundle` captures the supporting basis for representing an episode in a particular way and thereby distinguishes evidence-backed context construction from unsupported summarization.

These components play different roles and should not be conflated. Constraints describe conditions of action, outcomes describe consequences, and evidence supports interpretation. Optional extensions such as scenario tags or analogical links across episodes may later be useful, but they are not required for the core methodological claim advanced here.

[Figure 3 about here]

## 3.3 Layered framework for decision-grade context

The proposed framework consists of four layers: graph-based business memory, the scenario memory layer, a decision subgraph, and an LLM reasoning layer. This organization separates durable structured memory from episode-level organization, bounded context assembly, and final reasoning.

Graph-based business memory serves as the long-term substrate. It stores heterogeneous business data and signals in a form that preserves entities, relations, temporal traces, and evidentiary links. This layer matters because SME decision contexts frequently span internal business state, external market conditions, and prior actions rather than a single document or interaction history.

The scenario memory layer is the central methodological contribution of the section. It organizes relevant graph material into explicit decision episodes. The key idea is not that graph memory is unnecessary, but that graph memory is often too distributed to function directly as decision-grade context. Scenario memory therefore provides an episode-centered organization over graph-based memory rather than a replacement for it.

The decision subgraph is the bounded query-time view used for a specific decision task. Not all stored context is equally relevant to every question, and the method does not assume that the full graph should be exposed indiscriminately to the reasoning layer. Instead, it constructs a decision-relevant subgraph organized around the active or queried decision episode. The LLM reasoning layer then operates over that prepared context for explanation, comparison, and decision support.

This layered view clarifies the paper's claim. The contribution is not “graph instead of LLM,” nor “memory instead of retrieval.” It is a scenario-oriented organization of graph-based business memory that makes explicit decision episodes available for bounded context construction.

[Figure 2 about here]

## 3.4 Decision subgraph construction and role of the LLM

The decision subgraph translates broad business memory into a bounded representation suitable for a specific decision query. This is where the difference between relevance and decision utility becomes operational. A retrieved passage, recalled fact, or summarized interaction may be relevant without clarifying which goal is at stake, which constraints matter most, what triggered the episode, what action is under consideration, or what evidence supports the interpretation. A scenario-oriented subgraph is intended to make those relations explicit enough for reasoning.

In this view, retrieval is one component of context construction rather than the endpoint of the method. The decision subgraph is not a loose collection of relevant items; it is a task-bounded representation of the episode most relevant to the current decision problem. Its purpose is to provide a structured context in which the focal goal, salient constraints, trigger conditions, candidate actions, outcomes, and evidence can be interpreted together.

The LLM is therefore positioned as a reasoning layer over structured memory rather than as the sole repository of business context. Its role is to operate on prepared scenario-aware context: explaining the episode, comparing alternatives, summarizing the relation among goals, constraints, actions, and outcomes, and supporting judgment. This positioning is methodologically important because it keeps the section focused on context organization rather than on generation alone. The framework does not assume that language models are incapable of useful memory behavior; it argues more narrowly that decision support benefits when the reasoning layer receives context already organized around explicit decision episodes.

## 3.5 Scope boundaries

The method presented here is a conceptual design for scenario-oriented context organization. It is not an empirical validation claim, and it does not assume that scenario memory is already a stabilized term in the literature. Nor does it claim that the proposed design is sufficient for all SME decision domains or that it has already demonstrated superior decision performance.

The narrower and more defensible claim is that graph-based business memory is useful but not sufficient on its own when the relevant decision situation remains distributed across heterogeneous data and signals. The proposed scenario memory layer addresses that gap by organizing distributed context into explicit decision episodes, which in turn support bounded context assembly through a decision subgraph. In that sense, the contribution of this section is methodological: it specifies a minimal framework for moving from fragment retrieval to decision-grade context construction.
