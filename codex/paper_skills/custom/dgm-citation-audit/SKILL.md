---
name: dgm-citation-audit
description: "Use for citation-quality audits in this repository: identify claims needing citations, flag unsupported or weakly supported claims, keep only strong sources, and conservatively update references/library.bib with verified entries for paper drafts and review-analysis chapters."
---

# DGM Citation Audit

Use this skill when the task is to audit citation quality in a draft, review note, or manuscript section.

## When to use

Trigger this skill when the user asks to:

- audit citations
- find unsupported claims
- identify weakly supported claims
- decide which sources are strong enough to keep
- update `references/library.bib` conservatively

Typical repository inputs:

- `manuscript/`
- `references/library.bib`
- `references/notes/`

Typical outputs:

- a citation audit note in `references/notes/`
- conservative `.bib` updates

## Core rules

- No invented references.
- No fake numeric placeholders.
- Prefer formal academic sources over product pages or generic web summaries.
- If source attribution is uncertain, mark it uncertain instead of guessing.
- Do not make the bibliography look fuller by adding unverified entries.
- Separate these categories clearly:
  - claim needs citation
  - claim is weakly supported
  - source is strong enough to retain
  - source needs replacement or verification

## Workflow

1. Read the target draft first.
2. Mark claims in four buckets:
   - clearly supported
   - citation needed
   - weakly supported
   - should be softened or removed
3. Cross-check cited author/year forms against actual verified records.
4. Update `references/library.bib` only when metadata are verified.
5. Produce an audit note that tells the next writer exactly what to fix.

## Preferred audit structure

- Claims that need citations
- Unsupported or weakly supported claims
- Sources strong enough to keep
- Places where more formal references are needed
- Bibliography changes made
- Uncertain areas that were intentionally left unresolved

## Repository-specific guidance

- Default output path:
  - `references/notes/<draft_name>_citation_audit.md`
- When a claim is conceptually useful but weakly supported, prefer softening the wording instead of forcing a citation.
- In this repo, review-analysis writing should preserve reviewer trust over rhetorical sharpness.
