# Prompt 02: Scenario Layer Design

Use this prompt when the substrate analysis is complete and you need a paper-level design for the Scenario Memory Layer.

```text
Write like a careful research collaborator, not like a product marketer.
Prefer narrow, defensible conceptual framing over broad claims.

Current goal:
Design a paper-level Scenario Memory Layer that sits on top of the existing graph substrate.

Important constraints:
- treat this as a conceptual design layer over the existing graph
- preserve compatibility with the current graph worldview
- avoid unnecessary complexity
- do not propose implementation work
- do not imply empirical validation

Paper thesis direction:
Current AI systems often retrieve fragments, but struggle to reconstruct decision-grade business context.
We want to frame a Scenario Memory Layer that represents:
- decision goals
- constraints
- challenges or triggers
- actions
- outcomes
- evidence
- temporal context
- optional links to analogous prior scenarios

Create:
- `manuscript/framework/scenario_memory_layer_design.md`

Required structure:
- Design objective
- Conceptual assumptions
- Scenario memory unit
- Core scenario components
- Optional supporting abstractions
- Proposed conceptual relations
- Relation to existing graph memory
- Why this improves on fragment retrieval
- Role of the LLM in the framework
- What is conceptual versus what is already realized
- Minimal defensible contribution

Requirements:
- define the decision episode compactly
- keep the core component set small
- make the design academically defensible
- avoid ontology-catalog language unless necessary
- clearly distinguish what already exists from what is only proposed
```
