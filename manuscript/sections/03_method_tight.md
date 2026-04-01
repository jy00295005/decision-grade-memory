# 3. Method: A Scenario Memory Framework for Decision-Grade SME Context

## 3.1 Method objective and organizing abstraction

We address a representation problem in SME decision support: how to move from fragment retrieval to decision-grade context construction. SME decisions are often made under uncertainty, resource constraints, uneven information quality, and dynamic operating conditions, so relevant context is typically distributed across business records, external signals, prior interactions, and evolving conditions. Retrieval can surface useful fragments from that distribution, but fragment access is not itself decision support. Decision support requires a bounded representation in which goals, constraints, triggers, actions, outcomes, and evidence are organized for reasoning.

We therefore propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction. The claim is narrow. We do not reject retrieval; we argue that retrieval should be organized around a more suitable unit of context. In this framing, graph-based business memory is useful because it preserves entities, relations, temporal structure, and evidence traces across heterogeneous inputs. However, graph memory alone is insufficient when the relevant decision situation remains implicit.

The term *scenario memory* is used here as a design term rather than as a standardized category in the literature. It denotes an organizing abstraction centered on bounded decision situations and is therefore distinct from document memory, conversational memory, or persistent user memory, each of which stores useful information but often leaves episode structure under-specified for decision support.

[Figure 1 about here]

## 3.2 Decision episode representation

The minimum representational unit of the framework is the *decision episode*. We define a decision episode as a bounded business situation in which an SME actor or firm pursues a goal under identifiable constraints, encounters a trigger or challenge, takes or considers an action, and interprets outcomes with respect to supporting evidence and temporal context. In compact form, a decision episode may be written as `E = (A, G, C, T, X, O, V, tau)`, where `A` denotes actor or business context, `G` the focal goal, `C` operative constraints, `T` a trigger or challenge, `X` an action or decision, `O` an observed or expected outcome, `V` an evidence bundle, and `tau` temporal placement.

This representation supports the core methodological claim because it specifies what must be assembled if a system is to move beyond loosely related fragments toward interpretable decision context. The framework uses four core conceptual components. `DecisionEpisode` is the organizing unit. `Constraint` makes explicit the pressures and limits under which action becomes feasible or risky. `Outcome` captures consequence structure rather than only problem state. `EvidenceBundle` provides the basis for representing the episode in a justified rather than purely associative way. Optional extensions such as scenario tags or analogical links may later be useful, but they are not necessary for the present claim.

[Figure 3 about here]

## 3.3 Layered framework for decision-grade context

The framework consists of four layers: graph-based business memory, scenario memory, a decision subgraph, and an LLM reasoning layer. Graph-based business memory serves as the long-term substrate, preserving heterogeneous business data and signals together with relational, temporal, and evidentiary structure. Scenario memory organizes relevant graph material into explicit decision episodes. The decision subgraph is the bounded query-time view assembled for a particular decision task. The LLM reasoning layer then operates over that prepared context for explanation and support.

The methodological point is not “graph instead of LLM,” nor “memory instead of retrieval.” It is a scenario-oriented organization of graph-based business memory that makes explicit decision episodes available for bounded context construction.

[Figure 2 about here]

## 3.4 Decision subgraph construction and role of the LLM

The decision subgraph translates broad business memory into a task-bounded context. This is where the distinction between relevance and decision utility becomes operational. A retrieved passage or recalled fact may be relevant without clarifying which goal is at stake, which constraints dominate, what triggered the episode, what action is under consideration, or what evidence supports the interpretation. A scenario-oriented subgraph is intended to make those relations explicit enough for reasoning.

Retrieval therefore functions as one mechanism within context construction rather than as the endpoint of the method. The decision subgraph is not a loose set of relevant items; it is a bounded representation of the episode most relevant to the current decision problem.

The LLM is positioned as a reasoning layer over structured memory rather than as the sole repository of business context. Its role is to operate on prepared scenario-aware context: explaining the episode, comparing alternatives, and supporting judgment. The claim here is modest but important: decision support benefits when the reasoning layer receives context already organized around explicit decision episodes.

## 3.5 Scope boundaries

This method section presents a conceptual design for scenario-oriented context organization. It is not an empirical validation claim, and it does not assume that scenario memory is already a stabilized literature term. Nor does it claim that the proposed design is sufficient for all SME decision domains or that it has already demonstrated superior decision performance.

The narrower claim is that graph-based business memory is useful but not sufficient on its own when the relevant decision situation remains distributed across heterogeneous data and signals. The proposed scenario memory layer addresses that gap by organizing distributed context into explicit decision episodes, which then support bounded context assembly through a decision subgraph.
