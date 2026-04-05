# Prompt Library

This directory stores reusable project-specific prompts for Codex work in this repository.

## Recommended order

1. `setup/project_setup_mvp.md`
2. `literature_review/01_round1_reconnaissance.md`
3. `literature_review/02_sme_decision_pain_points.md`
4. `literature_review/03_ai_limits_for_decision_support.md`
5. `literature_review/04_research_positioning.md`
6. `03_method/01_substrate_analysis.md`
7. `03_method/02_scenario_layer_design.md`
8. `03_method/03_method_mapping.md`
9. `03_method/04_method_drafting.md`
10. `03_method/05_method_compression_and_export.md`
11. `evaluation_design/01_section4_round1_design.md`
12. `evaluation_design/02_section4_chapter_export.md`
13. `writing/section_drafting.md`

## Categories

- `setup/`: repository setup and project scaffolding prompts
- `literature_review/`: literature reconnaissance, synthesis, and positioning prompts
- `03_method/`: method-design prompts for Section 3 drafting and export
- `evaluation_design/`: prompts for Section 4 modular design and chapter export
- `nanobanana/`: academic figure-generation prompts
- `writing/`: manuscript drafting and revision prompts

## When to use which

- Use `setup/` before substantial drafting when repository structure or workflow still needs to be established.
- Use `literature_review/` for topic scoping, synthesis, gap identification, and research positioning.
- Use `03_method/` when the paper claim is stable enough to turn design notes into a Method chapter.
- Use `evaluation_design/` when the experiment logic is ready to be formalized but should still remain narrow and conservative.
- Use `writing/` after the literature and positioning materials are stable enough to support section drafting.

## Codex workflow fit

- These prompts are written for Codex-centered work in this repository.
- They assume section-by-section writing, conservative claims, and traceable edits.
- They work best alongside `literature-review`, `citation-management`, the project-local `dgm-*` skills, and chapter-export workflows.

## Scope rule

- Keep only research-project prompts that are reusable inside this repository.
- Do not store generic GitHub operations prompts here.
