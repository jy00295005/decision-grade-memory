# Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making

Scenario-oriented memory for decision-grade AI support in SME contexts

This repository is a minimal Markdown-first workspace for developing an early-stage academic paper on graph-based AI for SME decision-making. It is structured for iterative drafting, literature synthesis, section-level writing, and later migration to TeX if the project matures.

This repository is intended to function both as a working research archive and as a public-facing project page on GitHub and GitHub Pages. The public presentation should emphasize research framing, evolving notes, and transparent progress rather than polished product claims.

## Start here

- [GitHub Pages](https://jy00295005.github.io/decision-grade-memory/)
- [Latest experiments PDF](output/pdfs/05_experiments.pdf)
- [Latest evaluation PDF](output/pdfs/04_evaluation_design.pdf)
- [Latest method PDF](output/pdfs/section_3_method.pdf)
- [Latest review PDF](output/pdf/sme_decision_support_review_export.pdf)
- [Research positioning](docs/research_positioning.md)
- [Outputs](docs/outputs.md)
- [Research log](docs/research_log.md)
- [Prompt library](prompts/README.md)
- [Skills usage](docs/skills_usage.md)

## Latest artifacts

- Day 4 experiments output: [Section 5 Experiments PDF](output/pdfs/05_experiments.pdf)
- Day 4 chapter assets: `manuscript/05_experiments/` now contains modular experiment drafts plus figure-backed section assembly
- Day 3 evaluation output: [Section 4 Evaluation Design PDF](output/pdfs/04_evaluation_design.pdf)
- Day 3 workflow update: tracked paper-skill pack and evaluation-design prompt pack added to the repository
- Day 2 method output: [Section 3 Method PDF](output/pdfs/section_3_method.pdf)
- Method framing draft: approximately `2 hours` total effort, approximately `$1.00` total usage cost
- Day 1 review output: [SME decision support review PDF](output/pdf/sme_decision_support_review_export.pdf)
- First-day synthesis run: approximately `$0.50` total usage cost, completed in about `20 minutes`

## Research progress tracker

| Step | Owner | Time | Cost | PDF |
| --- | --- | --- | --- | --- |
| 1. Problem framing refinement | Human |  |  |  |
| 2. Related work consolidation | Codex | 30 mins | $0.50 | [Review PDF](output/pdf/sme_decision_support_review_export.pdf) |
| 3. Method framing draft | Codex | 2 hours | $1.00 | [Method PDF](output/pdfs/section_3_method.pdf) |
| 4. Data and graph design draft | Codex |  |  |  |
| 5. Evaluation design draft | Codex |  |  | [Evaluation PDF](output/pdfs/04_evaluation_design.pdf) |
| 6. Full manuscript integration | Codex |  |  |  |

## Project Identity

- Repository name: `decision-grade-memory`
- Working paper title: `Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`
- Project tagline: `Scenario-oriented memory for decision-grade AI support in SME contexts`

## Public presentation

- GitHub repository: the canonical home for version history, notes, manuscript structure, and research updates.
- GitHub Pages: a lightweight landing page for the project overview, positioning, current status, and key research notes.
  - URL: `https://jy00295005.github.io/decision-grade-memory/`
- Presentation style: research-first, transparent, and evolving; not startup-style marketing.

## Why this repo exists

- Keep the paper draft organized from the start.
- Separate research framing, section drafting, references, and future evidence artifacts.
- Make Codex collaboration predictable, incremental, and easy to resume across sessions.

## Intended contributions

- TODO: define the problem framing contribution.
- TODO: define the methodological contribution.
- TODO: define the practical or decision-support contribution.

## Current stage

Review-analysis complete, Method drafted, Section 4 evaluation design exported, and Section 5 experiments drafted and exported as a single chapter PDF

## Public story so far

If a new reader arrives from the next post, the short version is:

- Day 1: literature review and problem framing, focused on SME decision pain points and current AI support limits.
- Day 2: Method chapter drafted around a scenario memory framework for decision-grade context.
- Day 3: Evaluation design drafted to compare fragment-oriented retrieval with scenario-oriented context construction.
- Day 4: Experiments chapter drafted around targeted retest design, validation KG, and bounded `DecisionEpisode` results.
- Current direction: keep the paper modular, chapter-by-chapter, and exportable as PDF instead of trying to write the whole paper at once.

This is the main narrative the next post should carry forward.

## Main manuscript entry

`manuscript/main.md`

## Research positioning entry

`docs/research_positioning.md`

## Repository map

- `docs/`: working planning documents for outline, research questions, style, and actionable tasks.
- `manuscript/`: paper entry file plus section-by-section draft files.
- `references/`: bibliography file, source PDFs, and reading notes.
- `data/`: placeholders for raw and processed data when the project becomes empirical.
- `experiments/`: future home for experiment setup notes or artifacts, if needed later.
- `results/`: future home for result summaries, figures, or tables once evidence exists.
- `prompts/`: reusable prompt templates for structured Codex writing sessions.
- `codex/`: session handoff notes and Codex-specific collaboration context.

## Suggested GitHub Pages structure

- `docs/index.md`: public landing page for project framing and navigation.
- `docs/series.md`: public series view for the evolving research storyline.
- `docs/outputs.md`: public index of PDFs and shareable outputs.
- `docs/research_log.md`: dated research progress log.
- `docs/research_positioning.md`: research gap and positioning note.
- `references/notes/`: working literature notes that can be linked selectively from the landing page.


## Prompt library

- `prompts/setup/`: project setup and repository initialization prompts.
- `prompts/literature_review/`: staged prompts for literature reconnaissance, pain-point review, AI-limit review, and research positioning.
- `prompts/03_method/`: distilled prompts for substrate analysis, scenario-layer design, method mapping, method drafting, and compression/export.
- `prompts/evaluation_design/`: prompts for modular Section 4 design and chapter-level export.
- `prompts/nanobanana/`: reusable image-generation prompts for Method figures.
- `prompts/writing/`: section drafting and revision prompts for manuscript work.
- [Prompt index](prompts/README.md): recommended order and usage notes.

## Custom Codex skills

- Installed research workflow skills: see [docs/skills_usage.md](docs/skills_usage.md)
- Project-local custom skill prefix: `dgm-`
- Current custom skills:
  - `dgm-research-positioning`
  - `dgm-citation-audit`
  - `dgm-method-design`
  - `dgm-md-to-pdf-chapter-polisher`
- Important:
  - active installations still live under local `.codex/skills/`
  - tracked shareable copies now live under `codex/paper_skills/custom/`
  - zip packages now live under `codex/skill_packages/`
  - they support research positioning, citation audit, Method-section design, and chapter-level Markdown-to-PDF export

## Today in the repo

- Added a tracked paper-skill pack under `codex/paper_skills/` so collaborators can download the `dgm-*` workflow skills from the repository.
- Added zip packages for the custom paper workflow skills under `codex/skill_packages/`.
- Added a new Section 4 prompt pack under `prompts/evaluation_design/`.
- Expanded prompt index coverage so setup, literature review, method, evaluation design, figures, and writing each have clearer entry points.
- Exported a paper-style Section 4 chapter PDF to `output/pdfs/04_evaluation_design.pdf`.

## How Codex should work in this repo

- Work section by section.
- Prefer small, traceable edits.
- Read `README.md` and `docs/outline.md` before major edits.
- Use `TODO:` markers instead of unsupported claims.
- Keep content academic, precise, and non-marketing.
- Do not collapse the whole paper into one file.

## Working principles

- Treat all framing as provisional until backed by sources or evidence.
- Preserve a clear distinction between outline material, draft prose, and confirmed evidence.
- Keep terminology stable across files unless there is a deliberate reason to revise it.
- Add the smallest useful change that improves the draft or repository clarity.
- Record follow-up work in `docs/todo.md` when a meaningful edit reveals the next concrete step.

## Next 5 tasks

1. Tighten the transition from related work into the compressed Section 3 method framing.
2. Draft the data and graph design section so it aligns with the scenario-memory method claim.
3. Add formal citation anchors directly into the method and evaluation chapters where reviewer expectations are highest.
4. Refine the introduction so the review, method, and evaluation chapter artifacts connect as one paper narrative.
5. Prepare the next export-ready chapter artifact after the data/graph design section is stable.

## Not in scope for MVP

- TeX, journal formatting, or submission packaging
- invented citations, results, or empirical claims
- scripts, CI, Docker, tests, or automation
- fabricated figures or unsupported tables before there is real source material
