# Scenario Memory Layer Analysis

## Overview

This note clarifies how the paper's method design can be grounded in implemented graph capabilities without turning Section 3 into a system description. The paper title, `Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`, requires a method framing that links three things coherently:

- SME decision contexts are shaped by heterogeneous business data and external signals.
- Current AI support often remains fragment-oriented.
- Decision support may therefore require a more explicit organization of business context into bounded decision situations.

The practical design reference for this work is ProsperPath. However, the paper should not be written as "a paper about ProsperPath." Instead, ProsperPath is best treated as the implemented basis that shows which parts of a scenario-oriented design are already plausible and which parts remain only conceptual.

## What ProsperPath already provides

### Representational coverage

The existing graph substrate already covers a substantial portion of the business context needed for SME decision support. In practical terms, it models:

- business actors and firm context:
  - `Owner`
  - `OwnerCompany`
- intention and problem state:
  - `Goal`
  - `Challenge`
  - `Crisis`
  - `RiskEvent`
- intervention and event structure:
  - `Decision`
  - `Action`
  - `Event`
- business and environmental signals:
  - `FinancialPeriod`
  - `Benchmark`
  - `MarketTrend`
  - `CompetitorAction`
  - `Regulation`
- decision-support outputs:
  - `Recommendation`

For the paper, the important point is not the inventory itself. The important point is that the design does not begin from unstructured documents alone. It begins from a graph representation that already spans internal business state, external pressures, and possible response pathways.

### Relational expressiveness

The existing design also captures more than loose co-occurrence. It already uses semantically richer relations that are relevant to decision support, including:

- ownership and pursuit:
  - `BELONGS_TO`
  - `HAS`
  - `PURSUES`
- business pressure and dependency:
  - `FACES`
  - `SUFFERS_FROM`
  - `BLOCKS`
  - `REQUIRES`
  - `DEPENDS_ON`
- action and decision structure:
  - `ADDRESSES`
  - `MITIGATES`
  - `RESOLVES`
  - `ACHIEVES`
  - `SUPPORTS`
  - `TRIGGERED_BY`
  - `RESULTS_IN`
- evidentiary and recommendation linkage:
  - `EVIDENCED_BY`
  - `BASED_ON`
  - `RECOMMENDED_TO`
  - `SUPERSEDES`

This matters because the literature review does not suggest that SME decision support fails only because data are absent. A recurring theme is that decisions are weakly structured, constraint-heavy, and cross-source. That kind of setting requires at least partial access to goal structure, pressure structure, intervention structure, and evidence lineage. The existing graph already provides much of that material.

### Provenance-aware and temporal organization

The graph is also not purely static. Through episode-based ingestion and graph-level temporal metadata, it already supports a limited but important form of structured memory:

- information enters as bounded episodes rather than only as isolated facts
- edge metadata preserves episode linkage and therefore supports provenance tracking
- temporal structure allows business context to be situated over time
- distinct sources such as chat, financial data, onboarding, and research can remain connected without being collapsed into a single undifferentiated memory store

This is especially relevant given the literature review. One of the safer conclusions from the review is that fragment retrieval is often insufficient when the user needs to reconstruct how a business situation developed, what constraints mattered, and which evidence supports an interpretation. A provenance-aware graph already moves in that direction, even if it does not yet fully solve the problem.

### Decision-focused filtering

The existing decision-subgraph logic is also important as a methodological clue. It already assumes that:

- not all stored business context is equally useful for a decision query
- context needs to be filtered, prioritized, and made explainable
- evidence chains and confidence distinctions matter for decision support

This aligns closely with the literature review, which suggested that retrieval, summarization, and memory persistence are not enough by themselves for decision-grade reasoning. The filtering layer indicates that the implemented substrate already recognizes a context-construction problem, not merely a retrieval problem.

## What is still implicit rather than explicit

### Decision episodes remain distributed

The strongest limitation, from the paper's point of view, is that the relevant ingredients of a decision situation remain distributed across graph entities, edges, episodes, and filtered factors. The graph can represent goals, challenges, actions, financial changes, and recommendations, but it does not yet make the full decision episode explicit as a primary analytical unit.

Put differently, the substrate already contains many of the ingredients of decision context, but not yet a single representation that directly answers:

- what goal was at stake
- what constraints were operative
- what event or challenge triggered the episode
- what action or decision was taken or considered
- what outcome followed or was expected
- what evidence supports the interpretation

### Constraints are present, but not unified

The literature review repeatedly highlighted the importance of cash pressure, uncertainty, limited staffing, dynamic conditions, and weak analytical capacity in SMEs. The implemented graph already captures several of these indirectly through `Challenge`, `Crisis`, `RiskEvent`, `FinancialPeriod`, `Regulation`, and external market signals. However, these do not yet appear as a unified scenario-level account of "operating constraints."

For the paper, this means `constraint` is a justifiable design concept, but it should be framed as a proposed analytical layer rather than an implemented object.

### Outcomes are only partially assembled

The current graph contains multiple traces of outcome:

- action or event consequences
- changes across financial periods
- recommendation lifecycle and response signals
- downstream event sequences

However, those traces are not yet assembled into a stable scenario-level representation of what followed from a decision and how confidently that outcome should be interpreted. The review literature supports the importance of traceability and evidence, but it does not support the stronger claim that existing SME AI systems already reconstruct outcome-aware decision episodes well.

### Analogical linkage remains a future possibility

The graph structure makes it plausible to compare similar business situations across time, but explicit scenario-to-scenario linkage does not yet appear to be a central implemented design unit. This is relevant because the working thesis mentions links to prior analogous scenarios. That idea remains plausible, but it should not be treated as a core implemented capability or as a central claim in the first paper version.

## Why this matters for the paper thesis

The central methodological opportunity is narrow. The paper does not need to argue that existing systems lack all memory. The literature review does not support that broader claim, and the implemented graph substrate itself argues against it. A more defensible thesis is:

- graph-based business memory can already capture many ingredients of SME decision context;
- however, those ingredients often remain distributed and therefore may still be consumed as fragments;
- a scenario-oriented design can therefore be proposed to organize distributed graph context into explicit decision episodes for decision-grade context construction.

That claim is both literature-linked and implementation-grounded. It connects directly to the review findings on SME pain points, fragment-retrieval limits, traceability, and adjacent concepts such as episodic or workflow memory, without overstating what has already been built.

## Key design opportunity

The most useful design opportunity for the paper is not a full new ontology or a system rewrite. It is a minimal paper-layer abstraction that sits between the business graph and query-time decision reasoning.

Its role would be to organize distributed graph context into bounded decision episodes that make explicit:

- the focal actor or business context
- the focal goal
- the operative constraints
- the triggering event, challenge, or signal
- the action or decision path
- the observed or expected outcome
- the supporting evidence
- the relevant temporal placement

This is the smallest design move that directly answers the literature review and supports the paper's core framing: from fragment retrieval to decision-grade context.
