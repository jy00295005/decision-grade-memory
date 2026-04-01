# Section 3 Prompt Pack

This directory records the main prompts used to develop Section 3 / Method for the paper:

`Bridging Data, Signals, and Growth: A Graph-Based AI for SME Decision-Making`

The goal of this prompt pack is reproducibility. These prompts are not raw chat logs. They are distilled working prompts that another Codex session can reuse to reproduce the method-design workflow with minimal re-deciding.

## Recommended order

1. `01_substrate_analysis.md`
2. `02_scenario_layer_design.md`
3. `03_method_mapping.md`
4. `04_method_drafting.md`
5. `05_method_compression_and_export.md`

## What each prompt does

- `01_substrate_analysis.md`
  - analyzes the existing graph substrate and identifies what it already supports versus what remains implicit
- `02_scenario_layer_design.md`
  - proposes the conceptual Scenario Memory Layer on top of the existing graph worldview
- `03_method_mapping.md`
  - converts the design into a paper-facing Section 3 outline and claim structure
- `04_method_drafting.md`
  - drafts the actual Method section in paper prose
- `05_method_compression_and_export.md`
  - compresses the section for conference-paper density and prepares export-oriented outputs

## Use guidance

- These prompts are paper-first, not product-first.
- They assume the method is inspired by an implemented graph substrate, but the paper should not be written as a system write-up.
- They are optimized for:
  - reviewer trust
  - conceptual clarity
  - minimal defensible claims
  - PDF-ready academic writing

## Stable framing to preserve

- Core method claim:
  - `We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.`
- Keep terminology stable:
  - `scenario memory`
  - `decision episode`
  - `decision-grade context`
  - `graph-based business memory`
  - `decision subgraph`
  - `LLM reasoning layer`
