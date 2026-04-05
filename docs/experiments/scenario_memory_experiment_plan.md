# Scenario Memory Experiment Plan

## Exact files and modules likely to use

Primary ProsperPath components:

- `pp_query/service.py`
  - main graph search entrypoint
- `pp_query/schemas.py`
  - search strategy definitions
- `pp_query/query_client.py`
  - config-driven query client used for the pilot
- `decision_feat/graph_signals.py`
  - graph evidence and signal extraction logic
- `scripts/query_memories.py`
  - useful pattern for direct Neo4j access
- `schema/kg_schema.py`
  - schema reference for interpreting retrieved entities

Existing data assets:

- `mock_data/chat.json`
- `mock_data/ratio.json`
- `mock_data/user_memories.json`
- `mock_data/loca_trends.json`
- `1001_output.json`
- `1001_recommendations.json`

## Neo4j queries needed

Read-only Cypher inspections:

- count `Episodic` nodes for the target group
- count entities by label
- count relationships by type
- count `Action`, `Decision`, `Recommendation`, `Challenge`, and `FinancialPeriod`
- count edges where `r.episodes IS NOT NULL`
- sample action-to-goal, action-to-challenge, and recommendation-linked relationships

These queries are sufficient for:

- feasibility checking
- selecting usable cases
- confirming whether episode-linked context is present in the current graph

## Expected intermediate outputs

From the pilot pipeline:

- raw search results for each case and each condition
- compact baseline context package
- compact scenario-style context package
- a scored comparison table
- a short interpretation note describing what improved and what remained weak

Current pilot artifacts:

- `output/experiments/scenario_memory_pilot_results.json`
- `output/experiments/scenario_memory_pilot_results.csv`
- `output/experiments/scenario_memory_examples.md`
- `output/experiments/scenario_memory_pilot_summary.md`

## Evaluation tables to generate

At minimum:

- case-by-case comparison table with:
  - strategy
  - node count
  - edge count
  - context completeness
  - evidence traceability
  - missing-information awareness
  - decision usefulness

For the paper later:

- a compact task table describing each decision situation
- a results table aggregating rubric scores across fragment vs scenario conditions

## Whether human judgment is needed

Yes.

For the current assets, human judgment is necessary for the main pilot scoring because:

- the target construct is decision-grade context quality
- automatic scores would overfit to surface structure such as edge count
- the graph contains noise, so simple proxies would be misleading

Automatic proxy evaluation is realistic only as a secondary signal, for example:

- whether an output contains explicit problem-action-outcome linkage
- whether edge-backed evidence is present
- whether multiple contextual dimensions appear in one bundle

## Error and failure modes

- search retrieval may surface cross-domain or weakly related facts
- episode-aware retrieval may still fail to isolate one coherent business scenario
- some tasks may have recommendations but weak outcome traces
- some tasks may have goals and outcomes but weak challenge linkage
- graph relation labels may be semantically weak, for example many `RELATES_TO` edges

These failure modes do not invalidate the pilot, but they must be reported explicitly.

## What success would look like for a first paper-quality experiment

Minimum success:

- at least one or two cases where the scenario-style package is clearly better than the fragment package on completeness and traceability
- the improvement is inspectable in retrieved nodes and relation facts
- the limitations are transparent and do not require invented evidence

Stronger success:

- the same pattern repeats across several cases
- the scenario-style package consistently surfaces goal-challenge-action-outcome structure more clearly than the baseline
- the results support a narrow empirical statement in the paper

The current run should therefore be treated as a first inspectable pilot, not as the final paper experiment.
