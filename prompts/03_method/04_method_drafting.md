# Prompt 04: Method Drafting

Use this prompt when the method mapping is stable and you want a full Section 3 draft in paper prose.

```text
Write Section 3 / Method as a conceptual and methodological design section, not as product documentation and not as a system write-up.

Important framing:
- Do NOT foreground the implementation project
- Do NOT describe the method as “built on our current implementation”
- Do NOT make implementation-heavy claims
- Do NOT imply empirical validation

Core methodological claim:
We propose a scenario memory layer that organizes distributed graph-based SME context into explicit decision episodes for decision-grade context construction.

Use as source of truth:
- `manuscript/framework/method_section_mapping.md`
- `manuscript/framework/scenario_memory_layer_analysis.md`
- `manuscript/framework/scenario_memory_layer_design.md`

Draft:
- `manuscript/sections/03_method.md`
- optionally a shorter version at `manuscript/sections/03_method_compact.md`

Target style:
- serious academic tone
- clear, compact, and readable
- conceptual but not vague
- design-oriented, not implementation-heavy
- avoid hype and product language

Recommended subsection structure:
- 3.1 Method objective and problem formulation
- 3.2 Scenario memory as the organizing abstraction
- 3.3 Structure of a decision episode
- 3.4 Core conceptual components
- 3.5 Layered framework for decision-grade context
- 3.6 Decision subgraph construction view
- 3.7 Role of the LLM
- 3.8 Scope boundaries and status of the design

Requirements:
- write complete prose, not outline bullets
- keep terminology stable
- distinguish fragment retrieval from decision-grade context construction
- define the decision episode clearly
- keep the method minimal and defensible
- do not drift into ontology catalog language
```
