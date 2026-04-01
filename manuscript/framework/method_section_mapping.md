# Method Section Mapping

This document maps the scenario-memory design into a paper-facing Section 3 for `Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`.

## Core methodological claim

We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.

This is the central claim that Section 3 should keep repeating in different forms. If a paragraph does not support this claim, it is probably not essential to the method section.

## What is not claimed

- that the paper is about ProsperPath as a product or system write-up
- that a full scenario-memory implementation is already complete
- that the method has already demonstrated empirical performance gains
- that scenario memory is an established standard term in the literature
- that the proposed design is sufficient for every SME decision domain

## Method assumptions

- SME decisions often require more than retrieval of isolated facts or documents.
- Relevant business context can be represented as bounded decision episodes.
- Decision episodes can be assembled from heterogeneous business data and external signals represented in graph form.
- Decision support benefits from making goal, constraint, action, outcome, evidence, and time explicit.
- The LLM is better treated as a reasoning layer over structured memory than as the sole memory substrate.

## Section 3 thesis paragraph

Section 3 should argue that decision support for SMEs is fundamentally a context-organization problem rather than a retrieval-only problem. The method therefore introduces a scenario memory layer that organizes graph-based business context into explicit decision episodes, allowing data, signals, actions, outcomes, and evidence to be assembled into a bounded decision context for reasoning. The section should remain conceptual and design-oriented while making clear that the proposal is grounded in already feasible graph capabilities rather than in a purely speculative abstraction.

## Clean Section 3 / Method outline

### 3.1 Method objective and problem formulation

Purpose:
- define the methodological problem as moving from fragment retrieval to decision-grade context construction

What this subsection should say:

- current AI support often retrieves useful fragments but leaves decision situations under-organized
- SME decisions are often weakly structured, constraint-sensitive, and cross-source
- the method objective is therefore to organize relevant context into bounded decision episodes

Literature linkage:

- connect directly to the review findings on SME uncertainty, limited analytical capacity, fragmented context, and the limits of fragment-oriented AI support

### 3.2 Scenario memory as the organizing abstraction

Purpose:
- introduce scenario memory as the paper's central design abstraction

What this subsection should say:

- define scenario memory as an organization layer for decision episodes
- clarify that it is not equivalent to document memory, long-term user memory, or conversational memory
- explain that the design focus is episode structure rather than generic persistence

Literature linkage:

- connect to the review discussion of fragment-retrieval limits, episodic or workflow-adjacent concepts, and decision traceability

### 3.3 Structure of a decision episode

Purpose:
- define the minimum representational unit of the method

What this subsection should say:

- introduce the decision episode as a bounded unit linking actor, goal, constraint, trigger, action, outcome, evidence, and time
- explain why each element is necessary for decision-grade context
- keep the definition compact and paper-like rather than ontology-heavy

Literature linkage:

- connect constraints and outcomes back to the SME pain-point literature and evidence needs back to the AI support literature

### 3.4 Core conceptual components

Purpose:
- specify the minimal design components of the framework

What this subsection should say:

- present `DecisionEpisode`, `Constraint`, `Outcome`, and `EvidenceBundle` as the core components
- mention `ScenarioTag` or analogical linkage only as optional extensions if needed
- make clear that the first paper version is deliberately minimal

Literature linkage:

- show how these components respond to themes from the review:
  - weakly structured decisions
  - pressure and uncertainty
  - traceability needs
  - insufficiency of fragment-only support

### 3.5 Layered framework for decision-grade context

Purpose:
- explain how the components fit into the broader method architecture

What this subsection should say:

- introduce the layered view:
  - graph memory
  - scenario memory layer
  - decision subgraph
  - LLM reasoning
- explain that the contribution is not "graph instead of LLM" but "scenario organization over graph memory for LLM use"

Literature linkage:

- connect to the review's use of knowledge-graph thinking as contextual, temporal, and provenance-aware infrastructure

### 3.6 Decision subgraph construction view

Purpose:
- explain how scenario organization supports bounded query-time context

What this subsection should say:

- the system should not reason over the full graph indiscriminately
- it should construct a decision-relevant subgraph organized around the active episode
- the point is context construction, not raw recall

Literature linkage:

- connect to the review's argument that retrieval and summarization alone are often insufficient for decision support

### 3.7 Role of the LLM

Purpose:
- define the LLM's place in the framework

What this subsection should say:

- the LLM functions as a reasoning and interaction layer
- it should not be framed as the primary long-term memory store
- its role is to interpret prepared decision context, compare scenarios, and support explanation

Literature linkage:

- connect to the review's distinction between stored memory and decision-grade reasoning support

### 3.8 Scope boundaries and status of the design

Purpose:
- limit claims and prevent overstatement

What this subsection should say:

- the section presents a conceptual method design
- it is grounded in already feasible graph capabilities but is not itself an empirical validation claim
- the paper does not need to prove a brand-new memory category
- evaluation and implementation expansion remain separate future steps

Literature linkage:

- align this boundary statement with the review's caution that scenario memory is, at present, a working framing rather than a stabilized literature term

## One-sentence purpose for each subsection

| Subsection | One-sentence purpose |
| --- | --- |
| 3.1 | Formulate SME decision support as a context-organization problem rather than a retrieval-only problem. |
| 3.2 | Introduce scenario memory as the organizing abstraction of the method. |
| 3.3 | Define the decision episode as the minimum unit of decision-grade context. |
| 3.4 | Present the minimal core components of the framework. |
| 3.5 | Explain the layered relation among graph memory, scenario memory, bounded context construction, and LLM reasoning. |
| 3.6 | Show how scenario-aware organization supports query-time decision context assembly. |
| 3.7 | Position the LLM as a reasoning interface over structured memory. |
| 3.8 | State the limits of the method claim and prevent implementation overreach. |

## What should remain in the background rather than foregrounded

- internal implementation details
- product-like terminology
- codebase-specific module names
- detailed relation taxonomies beyond what the paper needs
- optional extensions unless they materially support the central claim

These can still inform the design, but they should not dominate Section 3.

## Safe claims to make

- SME decision support often requires organization of heterogeneous business context rather than retrieval of isolated fragments alone.
- Graph-based memory is useful because it can represent entities, relations, temporal context, and evidence traces in a structured way.
- A scenario memory layer can be proposed as a means of organizing distributed context into explicit decision episodes.
- Decision-grade context benefits from making goals, constraints, actions, outcomes, evidence, and time explicit.
- The LLM is more appropriately positioned as a reasoning layer over structured memory than as the sole memory substrate.

## Claims that should remain hypotheses or future directions

- that the proposed design improves decision quality in practice
- that scenario memory outperforms simpler memory forms across tasks
- that analogical scenario linkage materially improves support quality
- that the proposed component set is universally sufficient
- that the design already exists as a complete implemented layer

## Concise method summary paragraph

This paper proposes a scenario memory framework for decision-grade SME support. The framework treats decision support as a problem of organizing distributed business context rather than retrieving fragments alone. It represents decision situations as bounded episodes linking actors, goals, constraints, triggers, actions, outcomes, evidence, and temporal context, and places that episode structure between graph-based business memory and LLM-based reasoning. The contribution is conceptual and design-oriented: it clarifies how heterogeneous data and signals may be organized into decision-grade context without claiming a fully validated implementation.

## Concise system overview paragraph

At a high level, the framework consists of four layers: graph-based business memory, a scenario memory layer that organizes that memory into decision episodes, a decision subgraph that assembles bounded context for a specific query, and an LLM reasoning layer that interprets the resulting context for explanation and support. In this design, the graph provides structured long-term memory, the scenario layer provides episode-level organization, and the LLM operates as an interface for reasoning rather than as the sole repository of business knowledge.
