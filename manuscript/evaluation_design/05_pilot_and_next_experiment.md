# Section 4 Round 1: Pilot and Next Experiment

## What the pilot already did

The current pilot compared two context construction conditions on three SME-style decision tasks:

- supplier MOQ pressure under cash-flow constraints
- weekend staffing conflict under service constraints
- sales decline recovery under attribution uncertainty

Conditions used:

- fragment-oriented baseline: `node_rrf`
- scenario-oriented proxy condition: `combined_rrf`

Pilot artifacts already exist in:

- `output/experiments/scenario_memory_pilot_summary.md`
- `output/experiments/scenario_memory_examples.md`
- `output/experiments/scenario_memory_pilot_results.csv`
- `output/experiments/scenario_memory_pilot_results.json`

## What the pilot can support

The pilot can support a narrow statement such as:

- in a small set of SME-like tasks, a scenario-oriented context package appeared more complete and more traceable than a fragment-oriented baseline

It can also support:

- the feasibility of running a larger comparison on the current graph
- the claim that the comparison target should be context construction quality rather than broad answer quality

## What the pilot cannot support

The pilot cannot support:

- a strong empirical claim about business effectiveness
- a broad claim across SMEs or domains
- a stable quantitative performance claim
- a claim that a full scenario-memory layer has already been implemented and validated

## Current caveats

Main caveats from the current run:

- small sample size
- synthetic or semi-simulated data
- noisy graph retrieval
- weak relation semantics in some places, especially many `RELATES_TO` facts
- no blinded or multi-reviewer scoring
- scenario-oriented condition is still a proxy rather than a clean episode-level mechanism

## What a 15-30 case experiment would look like

Recommended next round:

- `15-30` decision situations
- repeated task families rather than only one-off examples
- fixed query templates
- fixed retrieval settings
- stable scoring rubric
- second-reviewer scoring on at least a meaningful subset

Useful task families:

- cash and inventory pressure
- staffing and scheduling
- sales decline and channel decisions
- supplier response and ordering strategy
- return-cost or margin-protection decisions

## What should be improved in the next round

- cleaner case selection
- less noisy scenario-oriented retrieval
- clearer episode boundary logic
- stronger outcome traces where available
- explicit logging of missing information
- stronger scorer discipline

## What evidence would count as promising

Promising evidence would include:

- repeated case-level improvement in completeness and traceability under the scenario-oriented condition
- visible challenge-action-goal-outcome structure in the richer context package
- gains that remain interpretable rather than being driven only by larger output volume
- similar pattern across multiple task families

## What evidence would count as still inconclusive

Still inconclusive evidence would include:

- mixed case-level patterns with no stable direction
- improvements that disappear once noisy cases are removed
- context packages that are larger but not more decision-useful
- scenario-oriented condition retrieving more facts without improving structure
- scorer disagreement that remains unresolved

## Round 1 stance

For now, the pilot should be treated as:

- preliminary evidence
- enough to justify the next experiment round
- not enough to anchor the final paper's evaluation claims by itself
