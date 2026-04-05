# Section 4 Round 1 Design Prompt

## Purpose

Create modular Markdown design files for Section 4 / evaluation design before writing the final paper section.

## Prompt

```md
Work like a careful research collaborator preparing an evaluation section, not like a paper-polishing assistant.

We are now moving to Section 4, but in Round 1 I do NOT want a polished paper section yet.

Goal for Round 1:
Create Section 4 as a set of modular Markdown design documents that define the evaluation logic clearly and practically.
Do not make it overly paper-like yet.
Do not optimize for elegant prose.
Optimize for:
- clarity
- defensibility
- experimental structure
- traceability to the paper claim
- ease of later conversion into a paper section

Context:
We already have:
- Section 2 review-analysis
- Section 3 method

The paper’s narrow method claim is:
We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.

The experimental objective should stay narrow:
We are NOT trying to prove universal business value.
We are trying to test whether scenario-oriented context construction can yield better decision-grade context than fragment-oriented retrieval on SME-style decision tasks.

Please create modular Markdown files under:
`manuscript/evaluation_design/`

Required files:
1. `01_eval_objective_and_claims.md`
2. `02_task_and_case_design.md`
3. `03_conditions_and_baselines.md`
4. `04_metrics_and_rubric.md`
5. `05_pilot_and_next_experiment.md`
Optional:
6. `06_section4_assembly_notes.md`

Rules:
- keep the experimental logic aligned with the paper claim
- separate pilot evidence from full experiment design
- be explicit about limitations
- do not fabricate any findings
- do not write future results as if already known
- keep the focus on context construction strategies, not product features
```

## Notes

- This is the correct prompt when Section 4 still needs to be designed as modular notes.
- Use this before chapter polishing or PDF export.
