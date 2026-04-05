# ProsperPath Experiment Feasibility

## Available assets

ProsperPath already contains enough material to support a narrow, initial evaluation of context construction strategies for SME-style decision support.

- Raw business-like inputs exist in `mock_data/`, including:
  - `chat.json` with multi-session owner-agent discussions covering sales decline, staffing gaps, inventory sync, supplier MOQ pressure, and other operational issues.
  - `ratio.json` with period-level financial metrics.
  - `user_memories.json` with owner context, preferences, and business constraints.
  - `loca_trends.json` with market trends, competitor actions, and regulatory/grant signals.
- Derived artifacts already exist in ProsperPath:
  - `1001_output.json` with decision factors, trace scores, and factor summaries.
  - `1001_recommendations.json` with recommendation traces, signal summaries, and action suggestions.
- Existing schema coverage is broad enough for a pilot:
  - `schema/kg_schema.py` and `schema/README.md` show support for `Owner`, `OwnerCompany`, `Goal`, `Challenge`, `Crisis`, `Decision`, `Action`, `FinancialPeriod`, `CompetitorAction`, `MarketTrend`, `RiskEvent`, and `Recommendation`.
- Existing query and evidence paths are usable:
  - `pp_query/service.py` exposes search strategies through `search(...)`.
  - `pp_query/schemas.py` defines `node_rrf`, `edge_episode`, and `combined_rrf`.
  - `decision_feat/graph_signals.py` exposes graph-based evidence signals such as mention count, relationship strength, and action connectivity.

Read-only Neo4j inspection for `group_id = user_1001` confirmed non-trivial graph coverage.

- `75` `Episodic` nodes
- `682` total `Entity` nodes
- `59` `Recommendation` nodes
- `16` `Action` nodes
- `3` `Decision` nodes
- `14` `Challenge` nodes
- `327` edges with non-null `episodes` metadata

## Likely usable evaluation units

The cleanest unit for a first experiment is not a fully formalized decision episode, because the graph does not currently store explicit `DecisionEpisode` nodes. The most usable unit is a `decision situation` defined by:

- a user query about a concrete SME problem
- a small set of retrieved graph nodes and edges
- one short-horizon business context where the graph contains at least a challenge, a suggested action, and some outcome or goal trace

Three task types already appear realistic with current assets.

- Supplier MOQ pressure under cash-flow constraints
- Weekend staffing or rota conflicts under service constraints
- Sales decline recovery under attribution uncertainty

These are suitable because they already have:

- owner-facing problem statements in chat sessions
- graph entities and recommendations linked to those problems
- at least partial outcome or goal traces in the graph

## Major blockers

The assets are usable, but only for a narrow and explicitly provisional experiment.

- No explicit `DecisionEpisode` layer currently exists in the graph.
  - The pilot therefore approximates scenario-style context construction through richer relational retrieval and episode-linked context assembly.
- Explicit evidence modeling is thin.
  - `SUPPORTS` edges exist, but `EVIDENCED_BY` is effectively absent in the inspected sample.
- Some retrieval noise is already visible.
  - `combined_rrf` is usable, but still surfaces unrelated or weakly related facts.
  - `edge_episode` is more episode-aware, but noisier than `combined_rrf` in the tested cases.
- Outcomes are uneven.
  - Some cases include achieved goals or benefit statements.
  - Others only contain partial follow-through, not clean before/after business outcomes.
- The dataset is synthetic or semi-simulated.
  - That does not invalidate a feasibility pilot, but it limits external claims.

## Confidence level on experiment feasibility

Medium.

The repository already supports a credible pilot for the narrow paper claim:

`scenario-oriented context construction may produce more decision-grade context than fragment retrieval alone on SME-like decision tasks.`

Confidence is not high because the graph still mixes clean local context with noisy retrieval artifacts, and because explicit outcome/evidence schema support is incomplete.

## Recommendation

Proceed narrowly.

What is feasible now:

- a small, inspectable comparison between `node_rrf` fragment-oriented retrieval and `combined_rrf` scenario-style context assembly
- a rubric-based comparison of context quality on a few SME-like decision tasks

What is not yet feasible as a strong main experiment:

- robust claims about business effectiveness
- broad claims across SME domains
- fully automated scoring of decision quality
- a clean test of a true implemented scenario-memory layer

The current assets are strong enough for a first paper-facing pilot, but not strong enough for a definitive empirical validation.
