# Section 4 Round 1: Evaluation Objective and Claims

## Why Section 4 exists

Section 4 is meant to test the empirical plausibility of the paper's narrow method claim.

It is not meant to establish broad business value, production readiness, or general superiority of graph-based systems.

## Evaluation objective

The evaluation objective is to test whether scenario-oriented context construction can yield better decision-grade context than fragment-oriented retrieval on SME-style decision tasks, using the same underlying graph memory.

The emphasis is on context quality, not on final answer quality in the abstract.

## Narrow paper claim

The paper's narrow method claim is:

`We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.`

The evaluation-facing version of that claim should stay narrower:

`Scenario-oriented context construction may produce more decision-grade context than fragment-oriented retrieval on SME-style decision tasks.`

## Non-claims

Section 4 is not trying to claim:

- universal business value across SMEs
- production performance of ProsperPath
- superior recommendation quality in general
- causal business impact
- that the current pilot is sufficient as final empirical validation
- that the current graph already implements a full scenario-memory layer

## Primary research questions

Primary question:

- Can a scenario-oriented context construction strategy produce better decision-grade context than fragment-oriented retrieval when both use the same underlying business graph?

Secondary questions:

- Does scenario-oriented context improve context completeness?
- Does it improve evidence traceability?
- Does it make unresolved unknowns more visible?
- Does it produce a more decision-useful context package for bounded SME decision tasks?

## Working hypotheses

`H1`

- For short-horizon SME decision tasks, scenario-oriented context construction will outperform fragment-oriented retrieval on context completeness and evidence traceability.

`H2`

- Scenario-oriented context construction will more often surface explicit challenge-action-goal-outcome structure.

`H3`

- Any observed gains will be stronger on operational or tactical tasks than on broad strategic prompts.

## Connection to Section 2

Section 2 argued that:

- SME decision-making is often constrained by incomplete information, fragmented systems, limited analytical capacity, and dynamic operating conditions.
- Current AI support systems often retrieve fragments well but may fail to reconstruct decision-grade business context.

Section 4 should therefore evaluate whether a different context construction strategy helps with exactly that problem.

## Connection to Section 3

Section 3 proposed:

- graph-based business memory as a useful long-term substrate
- scenario memory as an organizing abstraction
- decision episodes as the minimum representational unit
- decision subgraphs as the task-bounded context passed to the reasoning layer

Section 4 should not try to validate the whole conceptual framework at once.

It should test the most defensible empirical slice:

- whether a more scenario-oriented context package is better than a more fragment-oriented context package on comparable SME-style tasks

## Practical framing for Round 1

For now, Section 4 should be treated as:

- an evaluation design section with a pilot-backed starting point
- not yet a finalized experiments section
- not yet a polished narrative
