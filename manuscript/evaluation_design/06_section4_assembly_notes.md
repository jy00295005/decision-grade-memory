# Section 4 Round 1: Assembly Notes

## Goal of these files

These files are meant to support later compression into a paper-style Section 4.

They are deliberately modular so that:

- evaluation logic can be inspected directly
- weak assumptions can be revised locally
- the final paper section can be assembled without rewriting from scratch

## Likely mapping into a later paper section

Possible Section 4 structure later:

- `4.1 Evaluation objective and scope`
  - draw mainly from `01_eval_objective_and_claims.md`
- `4.2 Tasks, cases, and experimental conditions`
  - merge material from `02_task_and_case_design.md` and `03_conditions_and_baselines.md`
- `4.3 Metrics and scoring`
  - compress `04_metrics_and_rubric.md`
- `4.4 Pilot setup and preliminary observations`
  - draw from `05_pilot_and_next_experiment.md`

## What can be merged later

Likely merge candidates:

- task design + conditions
- pilot description + caveats
- claims + non-claims into one scope paragraph

## What should probably stay out of the main section

Better for appendix or supplement:

- detailed case selection rules
- full scoring rubric wording
- raw pilot examples
- long discussion of rejected conditions such as `edge_episode`
- operational notes about file locations and intermediate artifacts

## What should stay in the main section

Main-paper essentials:

- narrow evaluation objective
- same-information-source comparison logic
- baseline vs scenario-oriented condition
- core metrics
- pilot status and limits
- what the next real experiment would need

## Compression warning

When these files are compressed into a paper section, do not let:

- ProsperPath implementation detail
- pilot artifact management
- retrieval debugging detail

take over the narrative.

The paper-facing center should remain:

- what is being compared
- why that comparison matches the paper claim
- what the pilot suggests
- what remains unvalidated
