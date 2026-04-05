# Paper Skills Pack

This directory contains the research-writing skill pack for this repository in a tracked, shareable form.

It exists because the active skills used in Codex can live under local `.codex/` or global Codex directories, which are not automatically shareable through the repository.

## What is included

### Custom `dgm-` skills included directly in this repo

- `dgm-research-positioning`
- `dgm-citation-audit`
- `dgm-method-design`
- `dgm-md-to-pdf-chapter-polisher`

These are copied into:

- `codex/paper_skills/custom/`

and also packaged in:

- `codex/skill_packages/dgm-paper-workflow-pack.zip`

### External paper-workflow skills used in this project

These are listed in:

- `codex/paper_skills/manifests/external_skills_manifest.md`

They are part of the working paper workflow, but their original source lives outside this repository.

## Why this directory matters

- makes the paper workflow more portable
- makes the custom `dgm-` skills downloadable by collaborators
- separates project-specific research skills from machine-local Codex installation state

## Recommended use

- use `custom/` when you want the tracked source of the `dgm-*` skills
- use `codex/skill_packages/` when you want zip packages for transfer or reuse
- use the manifest when reproducing the broader installed skill set on another machine
