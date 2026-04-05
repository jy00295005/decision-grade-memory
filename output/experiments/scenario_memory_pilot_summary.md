# Scenario Memory Pilot Summary

## What was actually run

This pilot used the existing ProsperPath graph for `group_id = user_1001` and compared two retrieval-based context construction conditions on three SME-style decision tasks.

- Fragment-oriented baseline: `node_rrf`
- Scenario-style condition: `combined_rrf`

Tested tasks:

- supplier MOQ pressure under cash-flow constraints
- weekend staffing conflict under service constraints
- sales decline recovery under attribution uncertainty

The same underlying graph was queried in both conditions. The comparison focused on context package quality, not on final answer generation.

## What could not be run cleanly

- A true implemented `ScenarioMemoryLayer` was not available in ProsperPath.
- `edge_episode` retrieval was tested during feasibility work but was noisier than `combined_rrf`, so it was not used as the main pilot condition.
- No blinded human evaluation was run.
- No business outcome benchmark was attempted.

## Pilot reading

The pilot is promising, but only narrowly.

- In all three cases, the fragment baseline returned relevant nodes but little or no explicit relational evidence.
- The scenario-style condition consistently surfaced more decision-structured context, especially challenge-action-goal or challenge-action-outcome links.
- The gains were strongest in context completeness and evidence traceability.
- The pilot remains limited by noisy relations and synthetic or semi-simulated data.

Overall interpretation:

- promising for the narrow paper claim
- not sufficient for a strong standalone empirical claim

## What should be done next for a real paper experiment

- build a cleaner case set with `15-30` decision situations
- formalize a human scoring rubric and use at least one second reviewer
- reduce retrieval noise before treating scenario-style assembly as a serious experimental condition
- make scenario-oriented assembly more explicit than `combined_rrf`, ideally with a cleaner episode-level representation
