# Section 4 Chapter Export Prompt

## Purpose

Turn the modular Section 4 evaluation-design files into a coherent chapter draft and export a single-chapter PDF.

## Prompt

```md
Use [$dgm-md-to-pdf-chapter-polisher](../.codex/skills/dgm-md-to-pdf-chapter-polisher/SKILL.md) to assemble and polish the Section 4 evaluation-design materials into a chapter-level export.

Source files:
- `manuscript/evaluation_design/01_eval_objective_and_claims.md`
- `manuscript/evaluation_design/02_task_and_case_design.md`
- `manuscript/evaluation_design/03_conditions_and_baselines.md`
- `manuscript/evaluation_design/04_metrics_and_rubric.md`
- `manuscript/evaluation_design/05_pilot_and_next_experiment.md`
- `manuscript/evaluation_design/06_section4_assembly_notes.md`

Optional figure inputs:
- `manuscript/figures/fig4.png`
- `manuscript/figures/fig5.png`

Please:
1. merge the modular files into a coherent Section 4 chapter draft
2. remove overlap and repeated ideas
3. rewrite into journal-style academic prose
4. keep the claims narrow and conservative
5. include figure placeholders or direct figure references where appropriate
6. create:
   - `manuscript/sections/04_evaluation_design.md`
   - `manuscript/sections/04_evaluation_design_export.md`
   - optional `manuscript/sections/04_evaluation_design_export.html`
   - `output/pdfs/04_evaluation_design.pdf`

Important:
- this is still a chapter-level artifact, not a full paper export
- do not invent results
- keep pilot evidence and final experiment design clearly separated
```

## Notes

- Use this after the modular Section 4 notes are stable.
- This prompt is for chapter polishing and export, not for initial evaluation design.
