---
title: decision-grade-memory
---

# decision-grade-memory

Scenario-oriented memory for decision-grade AI support in SME contexts

## Project

This repository is an evolving academic research project around a working paper titled `Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`.

The project asks a narrow question:

How should AI systems support SME decision-making when decisions are weakly structured, constraint-heavy, and distributed across incomplete records, prior episodes, and changing business conditions?

## For readers coming from the next post

- This is not a one-shot AI writing demo.
- The paper is being built bottom-up, one chapter at a time.
- The current chapter sequence is:
  - Day 1: review-analysis on SME decision pain points and AI support limits
  - Day 2: Method chapter on scenario memory and decision episodes
  - Day 3: Evaluation design comparing fragment retrieval with scenario-oriented context construction
- The main idea is narrow: some SME decisions need decision-grade context, not just isolated fragments.

## Start here

- [Latest method PDF on GitHub](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdfs/section_3_method.pdf)
- [Latest review PDF on GitHub](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdf/sme_decision_support_review_export.pdf)
- [Outputs](outputs.md)
- [Research log](research_log.md)
- [Research positioning](research_positioning.md)
- [Series](series.md)
- [Prompt library](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts)
- [Skills usage](skills_usage.md)
- [Literature notes index](https://github.com/jy00295005/decision-grade-memory/blob/main/references/notes/README.md)

## Latest outputs

- [Evaluation PDF on GitHub](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdfs/04_evaluation_design.pdf)
- Day 3 result: evaluation design drafted as modular notes and exported as a paper-style chapter PDF.
- [Method PDF on GitHub](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdfs/section_3_method.pdf)
- Day 2 result: Method chapter drafted and exported as a paper-ready chapter PDF.
- Approximate effort: `2 hours`
- Approximate cost: `$1.00`
- [Review PDF on GitHub](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdf/sme_decision_support_review_export.pdf)
- Day 1 result: one review-analysis article completed from the initial note base.
- Approximate effort: `20 minutes`
- Approximate cost: `$0.50`

## Current research position

- The SME literature is strong on uncertainty, working-capital pressure, limited analytical capacity, and owner-manager-centered decisions.
- The AI literature is strong on retrieval, summarization, bounded prediction, and partial memory support.
- The current gap appears narrower than `AI for SMEs` in general.
- The most defensible framing so far is that some SME decisions may require more explicit episode-level context reconstruction and traceability than current support systems typically provide.
- For the next post, the main message is that the project has moved from literature review into chapter-by-chapter paper construction.

See the full positioning note here:

- [Research Positioning](research_positioning.md)

## What this repository contains

- [Paper Entry](https://github.com/jy00295005/decision-grade-memory/blob/main/manuscript/main.md)
- [Outline](outline.md)
- [Research Questions](rq.md)
- [Research Positioning](research_positioning.md)
- [Outputs](outputs.md)
- [Research Log](research_log.md)
- [Series](series.md)
- [Literature Review Round 1](https://github.com/jy00295005/decision-grade-memory/blob/main/references/notes/sme_ai_decision_review_round1.md)
- [SME Decision Pain Points](https://github.com/jy00295005/decision-grade-memory/blob/main/references/notes/sme_decision_pain_points.md)
- [AI Limits for SME Decision Support](https://github.com/jy00295005/decision-grade-memory/blob/main/references/notes/ai_limits_for_sme_decision_support.md)

## Prompt paths

- Setup prompts: [prompts/setup/](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts/setup)
- Literature review prompts: [prompts/literature_review/](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts/literature_review)
- Method prompts: [prompts/03_method/](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts/03_method)
- Figure prompts: [prompts/nanobanana/](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts/nanobanana)
- Drafting prompts: [prompts/writing/](https://github.com/jy00295005/decision-grade-memory/tree/main/prompts/writing)

## Custom skills

- Installed skill usage notes: [skills_usage.md](skills_usage.md)
- Project-local custom skill prefix: `dgm-`
- Current custom skills:
  - `dgm-research-positioning`
  - `dgm-citation-audit`
  - `dgm-method-design`
- Role:
  - these custom skills package the reusable parts of the paper workflow for research positioning, citation audit, and Method-section design

## Why GitHub Pages

This project is a continuous research repository rather than a static final paper. GitHub Pages is a suitable lightweight layer for:

- presenting the research question and current framing
- exposing selected literature notes and diagrams
- showing transparent progress through version history
- keeping the public project site close to the actual research files

## Current stage

Literature review, problem framing, research positioning, Method drafting, and evaluation design.

## Principles

- Keep claims narrower than the evidence base.
- Separate evidence-backed findings from working hypotheses.
- Prefer research transparency over polished hype.
- Treat the repository as a living research archive.

## Next likely milestones

1. Write the data-and-graph design section so it aligns with the scenario-memory method claim.
2. Turn the modular evaluation notes into a tighter Section 4 manuscript chapter if the next case round is strong enough.
3. Tighten Section 2 -> Section 3 -> Section 4 transitions so the paper reads as one argument rather than separate artifacts.
4. Keep the public story focused on the paper workflow rather than on isolated outputs.

## Research progress tracker

| Step | Owner | Time | Cost | PDF |
| --- | --- | --- | --- | --- |
| 1. Problem framing refinement | Human |  |  |  |
| 2. Related work consolidation | Codex | 30 mins | $0.50 | [Review PDF](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdf/sme_decision_support_review_export.pdf) |
| 3. Method framing draft | Codex | 2 hours | $1.00 | [Method PDF](https://github.com/jy00295005/decision-grade-memory/blob/main/output/pdfs/section_3_method.pdf) |
| 4. Data and graph design draft | Codex |  |  |  |
| 5. Evaluation design draft | Codex |  |  |  |
| 6. Full manuscript integration | Codex |  |  |  |
