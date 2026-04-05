# Section 4 Round 1: Metrics and Rubric

## Core metrics

Primary metrics for the current experiment:

- context completeness
- evidence traceability
- missing-information awareness
- decision usefulness

Optional later metric:

- action justification quality

![Figure 5: Evaluation workflow and scoring dimensions](../figures/fig5.png)

*Figure 5. Evaluation workflow for the pilot and the next experiment round. Cases are converted into decision queries, compared under two context conditions, and then scored with a rubric focused on context quality rather than broad product performance. The pilot uses author judgment; a stronger next round should add a second reviewer and a more fixed scoring process.*

## Metric definitions

### Context completeness

Question:

- Does the context package expose enough of the decision situation to support bounded reasoning?

Look for:

- focal problem
- relevant goal or target state
- key constraint
- candidate action
- partial or observed outcome when available

### Evidence traceability

Question:

- Can the reader see why the context package supports the decision discussion?

Look for:

- explicit relation facts
- episode-linked traces
- visible linkage between recommendation/action and supporting business context

### Missing-information awareness

Question:

- Does the context package make important unknowns visible instead of pretending the context is complete?

Look for:

- unresolved attribution
- missing outcome evidence
- incomplete constraint visibility
- visible ambiguity rather than false closure

### Decision usefulness

Question:

- Would this package be a better basis for a business decision conversation than the alternative condition?

Look for:

- practical decision relevance
- reduced need for manual reconstruction
- clearer relation among problem, action, and consequence

### Optional: action justification quality

Question:

- If an action is surfaced, is the reason for that action understandable and tied to the context?

This is optional for now because it overlaps with traceability and usefulness in the current pilot.

## Suggested scoring rubric

Use a simple `1-5` scale for each metric.

Working rubric:

- `1`: very weak or largely absent
- `2`: partial but insufficient
- `3`: usable but limited
- `4`: strong for the task
- `5`: very strong and clearly superior for the task

## Who does the scoring

Current pilot:

- single-reviewer human judgment
- explicit rubric-based scoring

Stronger next round:

- one primary scorer plus at least one second reviewer on a subset or all cases
- disagreement logging and resolution notes

## Role of automatic scoring

Current recommendation:

- use automatic evaluation only as a secondary aid

Possible automatic proxies later:

- presence of challenge-action-goal-outcome linkage
- number of edge-backed facts in the context package
- presence of explicit uncertainty or unresolved missing information

Automatic scoring should not be the sole evaluation in the next round unless the outputs become much cleaner.

## Pilot scoring limitations

Current limitations:

- unblinded scoring
- single reviewer
- small case count
- noisy retrieval
- metric overlap, especially between traceability and usefulness

This means current scores should be interpreted as:

- structured pilot judgments

not:

- stable final measurements

## What a stronger next-round evaluation should change

- increase case count to `15-30`
- freeze query templates and retrieval settings
- define a stable scoring sheet
- add second-reviewer scoring
- separate pilot examples from scored final cases
- tighten the scenario-oriented condition so it is less proxy-like and more explicitly episode-centered
