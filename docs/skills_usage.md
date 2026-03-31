# Skills Usage

This file explains how the installed Codex skills are used in this repository.

## Why these skills

- The project is literature-heavy and Markdown-first.
- The current stage emphasizes review synthesis, citation hygiene, structured prompting, and early conceptual design.
- The skill set is intentionally small and focused on research throughput rather than automation breadth.

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

## High-frequency skills

- `literature-review`
- `citation-management`
- `hypothesis-generation`

## Lower-frequency or future-stage skills

- `markitdown`
- `exploratory-data-analysis`
- `networkx`

## Caveat

- `bgpt-paper-search` is part of the intended workflow, but it still depends on external MCP configuration before it becomes fully usable in Codex.
