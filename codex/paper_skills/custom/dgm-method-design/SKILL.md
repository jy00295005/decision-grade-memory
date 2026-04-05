---
name: dgm-method-design
description: "Use for paper-first method design work in this repository: translate an implemented or existing graph substrate plus literature findings into a narrow, conceptual Method section centered on scenario memory, decision episodes, and decision-grade context without turning the paper into a system write-up."
---

# DGM Method Design

Use this skill when the task is to design or rewrite the paper's Method section from a paper-first perspective.

## When to use

Trigger this skill when the user asks to:

- design the method section
- turn an implemented substrate into a paper-facing conceptual framework
- define scenario memory or decision episodes
- map method design into Section 3 prose
- compress a method draft into conference-paper form

Typical inputs:

- existing project/schema/architecture context
- literature review findings
- current method notes or drafts

Typical outputs:

- `manuscript/framework/scenario_memory_layer_analysis.md`
- `manuscript/framework/scenario_memory_layer_design.md`
- `manuscript/framework/method_section_mapping.md`
- `manuscript/sections/03_method*.md`

## Core rules

- The paper is not a product write-up.
- Do not foreground the implementation project unless the user explicitly wants that.
- Do not imply full implementation or empirical validation.
- Prefer a narrow methodological claim over a broad framework claim.
- Treat the existing implementation as a design basis and reality check, not as the subject of the paper.
- Keep terminology stable:
  - `scenario memory`
  - `decision episode`
  - `decision-grade context`
  - `graph-based business memory`
  - `decision subgraph`
  - `LLM reasoning layer`

## Workflow

1. Start from the literature-backed problem.
   - What kind of decision support problem is being addressed?
   - Why is fragment retrieval insufficient?
2. Read the substrate only to determine:
   - what is already feasible
   - what remains implicit
   - what should be proposed at paper level
3. Define the smallest defensible method claim.
4. Specify the decision episode compactly.
5. Keep the component set minimal.
6. Map the design into a paper structure before drafting prose.
7. If needed, compress the draft aggressively for conference-paper density.

## Preferred outputs

### Analysis note

- Overview
- What the substrate already provides
- What remains implicit
- Why this matters for the thesis
- Key design opportunity

### Design note

- Design objective
- Conceptual assumptions
- Scenario memory unit
- Core scenario components
- Optional supporting abstractions
- Layered framework
- Role of the LLM
- Minimal defensible contribution

### Method section

Prefer this compact five-part structure unless the user asks otherwise:

- Method objective and organizing abstraction
- Decision episode representation
- Layered framework for decision-grade context
- Decision subgraph construction and role of the LLM
- Scope boundaries

## Compression rules

When revising a method draft:

- remove repeated motivation
- let figures carry structure where possible
- merge overlapping subsections
- keep only the paragraphs that perform methodological work
- concentrate non-claims into one short boundary subsection

## Repository-specific guidance

- Align Section 3 with the existing literature review and research positioning files.
- If figures already exist, reference them with placeholders in the section draft and use separate export files for figure-embedded versions.
- Keep `03_method.md` as the manuscript-facing draft and use export variants for PDF-ready output.
