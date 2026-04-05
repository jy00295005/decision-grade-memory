---
name: dgm-md-to-pdf-chapter-polisher
description: "Use when ChatGPT/Codex needs to transform multiple Markdown working files for a single research paper chapter into a polished, journal-style chapter draft, create export-ready Markdown/HTML variants, and generate a single-chapter PDF."
---

# DGM Markdown-to-PDF Chapter Polisher

Use this skill when the task is to turn several Markdown working files for one paper chapter into a coherent, publication-oriented chapter draft and export it as a single-chapter PDF.

This is a chapter-level skill, not a full-paper skill.

It is designed for Markdown-first academic workflows where a chapter starts as modular research files such as:

- `01_xxx.md`
- `02_xxx.md`
- `03_xxx.md`
- optional figures
- optional figure notes or captions
- optional reference or audit notes

## When to use

Trigger this skill when the user asks to:

- merge several Markdown working files into one chapter
- polish a chapter into journal-style academic prose
- turn modular notes into a paper-facing chapter draft
- create a chapter export version
- generate a single-chapter PDF
- tighten overlap and repetition across several chapter source files

Typical chapter types:

- review / related work
- method
- evaluation design
- results
- discussion

Typical outputs:

- `manuscript/sections/<chapter_name>.md`
- `manuscript/sections/<chapter_name>_export.md`
- `manuscript/sections/<chapter_name>_export.html` when useful
- `output/pdfs/<chapter_name>.pdf`

## What this skill is especially for

This skill is not a generic summarizer.

It should behave like a careful academic chapter polisher that:

- preserves the chapter's intellectual structure
- removes obvious overlap and repetition
- rewrites note-like text into coherent academic prose
- keeps claims no stronger than the source material supports
- produces a PDF-ready chapter without requiring the full paper to be finished

## Core rules

- Work chapter by chapter, not full-paper by default.
- Read all chapter source files before merging.
- Identify overlap before rewriting.
- Preserve unique content even when compressing repeated ideas.
- Keep the chapter moderately polished, not overcompressed.
- Maintain stable terminology across the merged chapter.
- Do not hallucinate citations.
- Do not invent missing results, experiments, or findings.
- Preserve subsection numbering if it already exists and is useful.
- Use figure placeholders or figure references conservatively and only where structurally justified.
- Keep a clear distinction between:
  - working notes
  - merged working draft
  - polished export

## Standard workflow

1. Inspect the source set.
   - Identify the chapter folder or the explicit file list.
   - Separate primary source files from support files such as captions, figures, notes, and audits.
2. Map the structure.
   - Determine the intended section logic and subsection hierarchy.
   - Note repeated claims, repeated transitions, and conflicting terminology.
3. Merge into a working chapter draft.
   - Combine the source files into a single coherent Markdown chapter.
   - Keep the structure explicit.
   - Remove obvious duplication.
4. Rewrite into paper-style prose.
   - Convert note language into academic prose.
   - Improve transitions across subsections.
   - Keep paragraph length and density balanced.
5. Add figure handling.
   - Insert figure placeholders or direct figure references where they improve chapter flow.
   - Keep captions separate if the repo workflow prefers separate caption files.
6. Create export-ready chapter files.
   - Prepare a polished export Markdown file.
   - Create HTML only if it improves PDF conversion reliability.
7. Generate the single-chapter PDF.
   - Write the final PDF to `output/pdfs/`.
   - Validate heading hierarchy, spacing, margins, and figure placement.

## Preferred chapter assembly logic

When merging modular source files:

- start from the strongest existing outline
- preserve the chapter's intended order
- merge repeated motivation paragraphs
- compress repeated definitions
- avoid repeating the same claim in slightly different language
- keep one best version of each transition
- keep caveats and non-claims explicit

When the source material is uneven:

- prefer a structurally clean draft over maximal source retention
- keep unresolved points visible with `TODO:` rather than smoothing over real gaps

## Style target

Target style:

- journal-style academic writing
- cohesive and readable
- moderately polished
- not too compressed
- not too verbose
- stable terminology
- strong paragraph transitions
- no product language
- no casual working-note voice in the final export

## Figure handling

Support both patterns:

- placeholder style: `[Figure X about here]`
- direct Markdown image references when the chapter export already uses local figure paths

If figures already exist:

- place them where they carry structural load
- do not over-explain what the figure already shows
- keep captions concise and academically worded

## PDF guidance

This skill should coordinate with [$pdf](/Users/chen/.codex/skills/pdf/SKILL.md) when final rendering and layout matter.

PDF expectations:

- single chapter only
- clean heading hierarchy
- readable margins and line width
- consistent spacing
- figures and captions aligned with chapter flow
- suitable for sharing as a chapter draft

## Output discipline

Preferred outputs:

- merged working draft in `manuscript/sections/`
- polished export draft in `manuscript/sections/`
- optional HTML export in `manuscript/sections/`
- final PDF in `output/pdfs/`

If the source set is not ready for polishing:

- still produce a merged working draft
- state what blocked a stronger export
- do not fake completeness

## Repository-specific guidance

This skill is designed for the `decision-grade-memory` workflow:

- modular chapter inputs first
- chapter-level assembly and polish second
- PDF export third
- full paper assembly later

Use it when chapter cohesion and export readiness matter more than raw ideation.

## Supporting files

Use the companion templates in this skill when useful:

- `templates/chapter_workflow.md`
- `templates/export_checklist.md`
- `templates/chapter_output_map.md`
