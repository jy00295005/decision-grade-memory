# Scenario Memory Layer Design

## Design objective

This document defines a paper-level scenario memory design for `Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`. The goal is not to describe an existing product architecture in prose. The goal is to articulate a narrow method design that is:

- informed by already implemented graph capabilities
- consistent with the literature review
- minimal enough to support one paper cleanly
- cautious about what is proposed versus what is already realized

The central design intuition is that decision support for SMEs often requires more than retrieval over documents, facts, or prior chat turns. It requires organization of relevant business context into explicit decision episodes.

## Conceptual assumptions

- SME decisions are often weakly structured, constraint-sensitive, and temporally situated.
- Relevant decision context is typically distributed across business records, user interactions, financial signals, and external signals.
- Existing graph representations can capture many ingredients of decision context but do not automatically expose the episode structure of a decision.
- Decision support benefits from structured context construction, not only from fragment retrieval.
- The LLM should be treated as a reasoning interface over structured memory rather than as the sole memory substrate.

These assumptions are consistent with the earlier literature review and are narrower than a claim of validated performance improvement.

## Scenario memory unit

In this paper, a `scenario` or `decision episode` is defined as a bounded business situation in which an SME actor or firm pursues a goal under identifiable constraints, encounters a trigger or challenge, takes or considers an action, and interprets outcomes with respect to supporting evidence and temporal context.

### Compact definition

A decision episode can be represented conceptually as:

`E = (A, G, C, T, X, O, V, tau)`

where:

- `A` = actor or business context
- `G` = focal goal
- `C` = operative constraints
- `T` = triggering challenge, event, or signal
- `X` = candidate or executed action or decision
- `O` = observed or expected outcome
- `V` = evidence bundle
- `tau` = temporal placement

This is not presented as a final formal ontology. It is a compact representation of what the method needs to organize for decision-grade context construction.

## Core scenario components

The paper design should keep the core component set small.

### 1. `DecisionEpisode`

Role:
- the central organizing unit

Why include it:
- the literature review suggests that retrieval alone often leaves business context fragmented
- a decision episode provides the bounded unit that ties goal, pressure, action, and evidence together

Relation to implemented graph capabilities:
- grounded in already represented business actors, goals, problems, actions, events, signals, and recommendation traces
- should be framed as a conceptual paper-layer abstraction rather than an already implemented runtime class

### 2. `Constraint`

Role:
- represents the conditions, pressures, and limits under which a decision is made

Why include it:
- the SME literature repeatedly highlights uncertainty, liquidity pressure, capability constraints, and dynamic operating conditions
- these are too central to leave implicit if the method is meant to support decision-grade context

Relation to implemented graph capabilities:
- can be grounded in existing challenge, crisis, risk, financial, regulatory, and market structures
- should be treated as a unifying analytical role, not necessarily as a separate implemented schema object

### 3. `Outcome`

Role:
- represents what followed, what is expected to follow, or what remains unresolved after an action or decision

Why include it:
- decision support is incomplete if it only reconstructs the problem state and not the consequence structure
- the literature on traceability and process-aware reasoning suggests that consequences matter for reuse and explanation

Relation to implemented graph capabilities:
- can be grounded in existing events, follow-on actions, financial changes, and recommendation lifecycle signals
- should be framed conservatively because outcome assembly is still only partial in the implemented substrate

### 4. `EvidenceBundle`

Role:
- represents the supporting basis for interpreting a decision episode

Why include it:
- one of the review's clearest implications is that decision support needs more than relevance; it needs justifiable context
- evidence linkage helps distinguish decision support from unsupported summarization

Relation to implemented graph capabilities:
- can be grounded in provenance-aware episodes, relation-level evidence, signal chains, and recommendation rationale
- should be described as a scenario-level abstraction over already available evidentiary traces

## Optional supporting abstractions

These may be useful, but they should not be treated as equally central in the first paper version.

### `ScenarioTag`

Possible role:
- lightweight grouping or indexing label for recurring business situations such as cash-flow pressure, demand shock, or hiring bottleneck

Why optional:
- useful for navigation and retrieval across cases
- not required for the core methodological claim

### Analogical linkage

Possible role:
- connecting one decision episode to prior similar episodes

Why optional:
- conceptually attractive and consistent with case-based or episodic reasoning
- not necessary for the smallest defensible contribution
- better treated as an extension or future direction unless the paper later develops it more fully

## Comparison of core scenario roles

| Component | Semantic role | Temporal role | Typical grounding in graph structure |
| --- | --- | --- | --- |
| `Constraint` | Operating condition or pressure | Before and during action | challenge, crisis, risk, financial pressure, regulation, market signals |
| `Outcome` | Consequence or resulting state | During and after action | event sequence, action consequence, financial change, response trajectory |
| `EvidenceBundle` | Justification for interpretation | May span the full episode | provenance links, evidence chains, source signals, rationale traces |

This distinction is useful because these three components should not be conflated. One describes the conditions of action, one describes consequence, and one describes the support for interpretation.

## Proposed conceptual relations

The paper does not need to introduce an extensive new relation taxonomy. It only needs the relations necessary to explain how a decision episode is organized. A minimal conceptual set is:

- `INVOLVES_ACTOR`
- `FOCUSED_ON_GOAL`
- `OPERATES_UNDER`
- `TRIGGERED_BY`
- `INCLUDES_ACTION`
- `RESULTS_IN`
- `SUPPORTED_BY`
- `OCCURS_DURING`

These should be understood as paper-level organizational relations. Some map closely onto already implemented graph semantics. Others serve mainly to clarify the scenario-memory design.

## Relation to existing graph memory

The design should be described as a layer over graph memory rather than as a replacement for it.

The intended flow is:

1. business graph memory
   - stores actors, goals, challenges, actions, events, internal signals, external signals, and evidence traces
2. scenario memory layer
   - organizes relevant graph material into explicit decision episodes
3. decision subgraph
   - constructs a bounded context for the current query or decision task
4. LLM reasoning layer
   - interprets and compares the prepared scenario-aware context

This framing keeps the method aligned with the literature review. It treats graph memory as foundational infrastructure, but not as sufficient on its own for decision-grade context assembly.

## Why this improves on fragment retrieval

The design is not intended to replace retrieval. It is intended to change what retrieval is organized around.

Compared with fragment-oriented retrieval, a scenario memory layer is meant to make more explicit:

- which goal is being pursued
- which constraints are currently operative
- which trigger or challenge made the situation decision-relevant
- which action or decision is at issue
- which outcome is known, expected, or unresolved
- which evidence supports that interpretation

This is the most defensible way to connect the method design to the literature review. It does not require claiming a wholly new memory category. It only requires showing that existing memory forms often leave episode structure implicit.

## Role of the LLM in the framework

The LLM should be framed as:

- an interface for explanation, comparison, and reasoning
- a consumer of structured scenario-aware context
- not the primary substrate for long-term business memory

This keeps the design aligned with the graph-based orientation of the paper title. The graph carries the durable, structured memory role; the scenario layer organizes that memory for decision use; the LLM reasons over the resulting context.

## What is conceptual versus what is already realized

### Already realized in the implemented basis

- graph-based representation of SME actors, goals, challenges, actions, events, and business signals
- semantically richer relations than generic document linkage
- provenance-aware and temporal graph traces
- decision-oriented filtering and context compression

### Proposed for the paper layer

- explicit organization of distributed graph context into `DecisionEpisode`
- unified treatment of `Constraint`
- scenario-level treatment of `Outcome`
- `EvidenceBundle` as a scenario-level justification unit
- optional cross-scenario indexing or analogical linkage

This distinction should remain explicit in all later paper drafting.

## Minimal defensible contribution

The minimal contribution of the method section should be stated narrowly:

- the paper does not claim that a full scenario-memory implementation is already complete
- the paper does not claim proven empirical gains
- the paper does not claim to solve all forms of SME decision support

Instead, the paper proposes a scenario memory design that organizes distributed graph context into explicit decision episodes for decision-grade context construction. That is the smallest, clearest, and most defensible methodological claim.
