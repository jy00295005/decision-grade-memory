# Scenario Memory Experiment Design

## Research question(s)

Primary question:

Can scenario-oriented context construction produce more decision-grade context than fragment-oriented retrieval on SME-like decision support tasks, using the same underlying graph memory?

Secondary questions:

- Does scenario-style context improve context completeness?
- Does it improve evidence traceability?
- Does it make missing information more visible rather than hiding it?
- Does it produce a more decision-useful context package for short-horizon SME decisions?

## Hypotheses

`H1`:
For SME-style operational or tactical decisions, scenario-style context construction will outperform fragment-oriented retrieval on context completeness and evidence traceability.

`H2`:
Scenario-style context construction will more often surface explicit links between challenge, action, goal, and observed outcome.

`H3`:
Any observed gains will be strongest on short-horizon, operationally grounded tasks rather than on broad strategic questions.

## Task definition

This experiment does not compare final business answers. It compares context packages.

Each test item is a `decision situation` consisting of:

- a realistic owner query
- the same underlying ProsperPath graph as the information source
- two context construction strategies

Candidate task types for the first run:

- supplier MOQ pressure under cash-flow constraints
- weekend staffing and rota conflict decisions
- October sales decline and conversion recovery

These tasks were selected because the current assets include problem traces, suggested actions, and at least partial goal or outcome evidence.

## Baseline definition

Condition A: fragment-oriented retrieval

- Retrieval strategy: `node_rrf`
- Interpretation: top matching nodes are treated as the context package
- Strength: simple and realistic baseline
- Weakness: does not explicitly recover relational business logic

Condition B: scenario-style context construction

- Retrieval strategy: `combined_rrf`
- Interpretation: top nodes plus episode-linked relational facts are assembled into a bounded context package
- Strength: more likely to expose challenge, goal, action, and outcome links in one bundle
- Weakness: still an approximation, not a fully implemented scenario-memory layer

`edge_episode` was tested during feasibility checking, but it was noisier than `combined_rrf` in the inspected cases. It is therefore better treated as supporting feasibility evidence rather than the main pilot condition.

## Evaluation metrics

Preferred pilot metrics:

- Context completeness
  - Does the context package expose the main problem, relevant constraint, plausible action, and outcome or target state?
- Evidence traceability
  - Can the reader trace why the recommendation or action is being surfaced?
- Missing-information awareness
  - Does the context package make important unknowns visible rather than implying false completeness?
- Decision usefulness
  - Would a reviewer plausibly regard the package as a better basis for a business decision discussion?

Optional metric:

- Action justification quality
  - Useful later, but not necessary for the first pilot

For this first run, these metrics are best scored by explicit human judgment using a small rubric. Automatic proxy metrics alone would be too weak.

## Data selection criteria

Include only cases where:

- the query corresponds to a concrete SME-style decision problem
- the graph contains at least one relevant challenge or crisis trace
- the graph contains at least one action or recommendation trace
- the graph contains at least one goal, benefit statement, or partial outcome trace

Exclude cases where:

- retrieval returns mostly unrelated domains
- there is no visible action or recommendation trace
- there is no inspectable contextual grounding beyond generic owner/company information

## Minimum dataset size needed for a meaningful first run

For a pilot:

- `3-5` decision situations is sufficient to test the pipeline and reveal whether the comparison is promising

For a stronger initial experiment:

- `15-30` decision situations would be a more defensible minimum, ideally spanning several repeated problem types

## Risks to validity

- The current graph is not a clean implementation of a scenario-memory layer.
- `combined_rrf` is only a proxy for scenario-oriented context construction.
- The dataset is synthetic or semi-simulated.
- Outcome traces are inconsistent across cases.
- Retrieval noise can inflate or distort apparent scenario gains.
- Human scoring in the pilot is subjective and unblinded.

Because of these risks, the pilot should be framed as an initial empirical check on feasibility, not as definitive validation.
