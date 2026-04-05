---
name: dgm-research-positioning
description: "Use for paper-first research positioning work in this repository: synthesize literature notes into a narrow problem framing, candidate research gap, strongest vs weakest thesis, contribution statements, and title options for decision-grade memory / SME decision support papers."
---

# DGM Research Positioning

Use this skill when the task is to turn existing literature review notes into a paper-facing positioning note.

## When to use

Trigger this skill when the user asks to:

- position the paper
- identify the research gap
- move from review notes to problem framing
- distinguish evidence-backed synthesis from conceptual framing
- generate candidate contribution statements or titles

Typical repository inputs:

- `references/notes/`
- `docs/rq.md`
- `docs/outline.md`
- existing review-analysis notes

Typical outputs:

- `docs/research_positioning.md`
- a positioning section inside a review note
- narrowed contribution statements

## Core rules

- Write like a careful research collaborator, not like a product strategist.
- Prefer the narrowest defensible framing over the broadest interesting framing.
- Separate evidence-backed synthesis from conceptual framing explicitly.
- If the literature does not support a strong claim, downgrade the claim.
- Do not invent citations, results, or stabilized terminology.
- Treat `scenario memory` as a working design term unless the literature clearly supports stronger wording.

## Workflow

1. Read the strongest available literature notes first.
   In this repo, start with the most synthetic notes before reading section drafts.
2. Extract only four things:
   - what the literature supports clearly
   - what the literature suggests but does not settle
   - what the paper can safely claim as a gap
   - what should remain a working hypothesis
3. Produce positioning with clear boundaries:
   - problem framing
   - why the problem is hard
   - why current approaches are insufficient
   - candidate research gap
   - strongest and weakest thesis versions
4. End with paper-useful outputs:
   - candidate contribution statements
   - candidate titles

## Preferred structure

When creating a positioning note, prefer this order:

- Problem framing
- Why the target decision problem is hard
- Why current AI support is insufficient
- Candidate research gap
- Competing framings of the gap
- Strongest version of the thesis
- Weakest / most defensible version of the thesis
- What would count as evidence
- What would count as non-evidence
- Candidate contribution statements
- Candidate titles

## Repository-specific guidance

- Keep terminology stable with the paper's method language:
  - `scenario memory`
  - `decision episode`
  - `decision-grade context`
  - `graph-based business memory`
- Align with the repo's academic writing discipline in `AGENTS.md`.
- If the positioning materially changes, add one concise follow-up item to `docs/todo.md`.
