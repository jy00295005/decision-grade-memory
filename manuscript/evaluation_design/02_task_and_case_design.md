# Section 4 Round 1: Task and Case Design

## Target SME-style decision tasks

Current task family for the pilot and next experiment round:

- supplier MOQ pressure under cash-flow constraints
- weekend staffing or rota conflict decisions under service constraints
- sales decline recovery under attribution uncertainty
- inventory sync / overselling prevention under operational constraints
- return-cost or bracketing mitigation under margin pressure

These tasks are intentionally short-horizon and decision-specific.

## Why these tasks are suitable

These tasks are suitable because they are:

- close to actual SME operating conditions
- weakly structured rather than purely factual
- dependent on combining multiple context elements
- narrow enough to inspect manually

They also fit the paper's logic well because they require more than isolated facts. A useful context package needs some combination of:

- business goal
- operational or financial constraint
- triggering challenge or crisis
- candidate action
- observed or expected outcome
- evidence or supporting basis

## What counts as a case

For the current experiment, the cleanest evaluation unit is a `decision situation`, not a formally implemented decision episode.

A case should include:

- one decision-oriented user query
- one focal business problem
- one shared underlying information source
- two context construction conditions

In practical terms, a case is acceptable when the graph contains at least:

- a challenge, crisis, or problem trace
- an action or recommendation trace
- a goal, benefit statement, or outcome trace

## Case vs episode vs query

Working distinction for Round 1:

- `query`: the natural-language prompt used to retrieve context
- `case`: the evaluation unit built around one query and one focal decision situation
- `episode`: a conceptual ideal from Section 3; not yet a clean implemented graph unit in the current system

This distinction matters because the current graph does not yet expose a stable explicit `DecisionEpisode` object for evaluation.

## Pilot vs full experiment

Pilot:

- `3-5` cases
- manual inspection is realistic
- useful for testing whether the experimental comparison is viable
- useful for detecting retrieval noise and case-selection problems

Next real experiment:

- `15-30` cases
- should include repeated task patterns, not just one-off examples
- should use a more stable scoring process
- should be strong enough to support a modest empirical claim

## Case selection criteria

Include cases where:

- the task is clearly SME-relevant
- the query is decision-oriented rather than purely descriptive
- the graph returns enough material to compare two context packages
- the case is not dominated by unrelated retrieval

Prefer cases where:

- the graph contains at least one explicit challenge or crisis
- the graph contains at least one action or recommendation
- the graph contains a goal or partial outcome
- the case involves meaningful constraints, such as cash, staffing, timing, or channel uncertainty

Exclude cases where:

- retrieval is dominated by cross-domain noise
- the graph only returns generic owner/company context
- there is no visible action path
- there is no inspectable consequence or target state

## Minimum scale for the next round

Recommended minimum for the next experiment round:

- `15-30` cases total
- at least `4-6` cases per recurring task family if possible

This would make it easier to say something modest but more defensible about pattern stability.

## Current design choice

For now, Section 4 should treat:

- the current 3-case run as a pilot
- the `15-30` case setup as the next experiment target

That keeps the empirical framing narrow and honest.
