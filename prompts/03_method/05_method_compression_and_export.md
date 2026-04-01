# Prompt 05: Method Compression and Export

Use this prompt when a full method draft already exists and needs to be compressed into a sharper conference-paper version and synchronized with export outputs.

```text
Revise Section 3 / Method with a ruthless conference-paper compression mindset: preserve the claim, remove redundancy, and make every paragraph earn its place.

Current files to use:
- `manuscript/sections/03_method.md`
- `manuscript/sections/03_method_compact.md`
- `manuscript/framework/method_section_mapping.md`
- `manuscript/framework/scenario_memory_layer_analysis.md`
- `manuscript/framework/scenario_memory_layer_design.md`

Main revision objective:
Keep the core methodological claim exactly the same, but compress the section into a sharper, denser, more reviewer-friendly Method section.

Core methodological claim to preserve:
We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.

Preferred target structure:
- 3.1 Method objective and organizing abstraction
- 3.2 Decision episode representation
- 3.3 Layered framework for decision-grade context
- 3.4 Decision subgraph construction and role of the LLM
- 3.5 Scope boundaries

What to improve:
1. reduce repetition across subsections
2. increase method density
3. make the section feel more like a top-tier paper
4. let figures carry more of the motivational and structural load
5. compress overlapping subsections where possible

Outputs:
- revise `manuscript/sections/03_method.md`
- create `manuscript/sections/03_method_tight.md`
- create `manuscript/framework/section3_revision_notes.md`

If export artifacts are needed:
- update `manuscript/sections/03_method_export.md`
- regenerate `manuscript/sections/03_method_export.html`
- regenerate `output/pdfs/section_3_method.pdf`

Requirements:
- no product language
- no implementation-heavy language
- no inflated novelty claims
- no unnecessary hedging loops
- keep the section narrow, defensible, and reviewer-friendly
```
