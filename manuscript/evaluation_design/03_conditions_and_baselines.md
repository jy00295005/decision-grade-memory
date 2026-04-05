# Section 4 Round 1: Conditions and Baselines

## What is being compared

The experiment compares two context construction strategies over the same underlying business graph.

This is not a model-vs-model benchmark.

It is a context-assembly comparison.

![Figure 4: Experimental comparison of fragment-oriented and scenario-oriented context construction](../figures/fig4.png)

*Figure 4. Evaluation framing for the current experiment. The same SME decision case and the same underlying information source are held constant, while the context construction strategy differs. This is the core comparison logic for Section 4: fragment-oriented retrieval versus scenario-oriented context assembly.*

## Condition A: fragment-oriented baseline

Working definition:

- retrieval strategy: `node_rrf`
- output form: top matching nodes returned as the context package

Interpretation:

- this approximates fragment-oriented retrieval where the system retrieves relevant pieces but does not strongly organize them into a bounded decision structure

Why it is a reasonable baseline:

- simple
- realistic
- already supported by the current retrieval stack

Expected weakness:

- often returns relevant fragments without clearly exposing challenge-action-goal-outcome relations

## Condition B: scenario-oriented condition

Working definition:

- retrieval strategy: `combined_rrf`
- output form: top nodes plus episode-linked relational facts assembled into a bounded context package

Interpretation:

- this is a proxy for scenario-oriented context construction, not a full implemented scenario-memory layer

Why it is usable now:

- it can expose relational evidence instead of only isolated nodes
- it is available in the current system
- it is closer to the paper's logic of bounded decision-grade context construction

Expected weakness:

- still noisy
- not yet a clean episode-level representation

## Rejected or noisier condition

`edge_episode` was inspected during feasibility work.

Reason to not use it as the main scenario condition in the current round:

- it was often noisier than `combined_rrf`
- it surfaced some relevant facts, but also more weakly related or distracting relational material

It can still be mentioned in Section 4 as:

- a useful exploratory condition
- not yet stable enough to serve as the primary comparison

## Same-information-source comparison logic

The comparison should hold the information source constant.

That means:

- same graph
- same case
- same query intent
- different context construction strategy

This is important because the paper's empirical question is not whether one system has more information.

It is whether one organization strategy makes the same information more decision-useful.

## What must be held constant

Across conditions, keep constant:

- target group or user context
- case definition
- query wording or equivalent query intent
- retrieval limit unless there is a stated reason to change it
- same underlying graph snapshot

## What differs across conditions

The main difference should be:

- how the context package is assembled

In the current round this means:

- fragment baseline emphasizes matched nodes
- scenario-oriented condition includes more explicit relational and episode-linked context

The scoring should therefore evaluate:

- context quality difference under controlled information-source conditions

not:

- absolute answer quality in a broad product sense

## Practical note for later paper writing

Section 4 should describe Condition B carefully.

Safer wording:

- `scenario-oriented context construction proxy`
- `scenario-style context assembly`

Less safe wording at this stage:

- `fully implemented scenario memory system`
