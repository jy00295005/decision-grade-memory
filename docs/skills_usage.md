# Skills Usage

This file explains how the installed Codex skills are used in this repository.

## Why these skills

- The project is literature-heavy and Markdown-first.
- The current stage emphasizes review synthesis, citation hygiene, structured prompting, and early conceptual design.
- The skill set is intentionally small and focused on research throughput rather than automation breadth.

The repository currently uses two layers of skills:

- installed general-purpose research skills copied into the project from external skill packs
- project-local custom `dgm-` skills for reusable paper workflow actions

## Practical usage

| Skill | Role in this repo | Typical use |
| --- | --- | --- |
| `literature-review` | first-pass synthesis | run structured reconnaissance and theme extraction across a topic cluster |
| `bgpt-paper-search` | paper discovery | find additional papers when the remote MCP path is configured |
| `citation-management` | reference hygiene | verify metadata, correct author-year drift, and update `references/library.bib` |
| `markitdown` | document conversion | turn supported source files into Markdown-friendly text when needed |
| `markdown-mermaid-writing` | Markdown-native writing | draft notes, diagrams, and lightweight visual explanations |
| `hypothesis-generation` | conceptual framing | compare gap framings, competing explanations, and narrower thesis variants |
| `exploratory-data-analysis` | future empirical support | inspect pilot data or experiment artifacts when the project becomes empirical |
| `networkx` | graph-modeling support | sketch graph schemas and relationship structures for later method work |
| `dgm-research-positioning` | paper positioning workflow | turn literature notes into a narrow problem framing, candidate gap, thesis variants, and contribution statements |
| `dgm-citation-audit` | manuscript trust and reference hygiene | identify unsupported claims, separate strong vs weak sources, and conservatively update `references/library.bib` |
| `dgm-method-design` | paper-first method workflow | convert substrate analysis plus literature findings into a narrow, conceptual Method section without drifting into system-writeup language |

## High-frequency skills

- `literature-review`
- `citation-management`
- `hypothesis-generation`
- `dgm-research-positioning`
- `dgm-citation-audit`
- `dgm-method-design`

## Lower-frequency or future-stage skills

- `markitdown`
- `exploratory-data-analysis`
- `networkx`

## Caveat

- `bgpt-paper-search` is part of the intended workflow, but it still depends on external MCP configuration before it becomes fully usable in Codex.
- The three `dgm-` skills are project-local custom skills. They currently live in local `.codex/skills/` and are usable in Codex on this machine, but they are not tracked in the repository by default because `.codex/` is ignored.
