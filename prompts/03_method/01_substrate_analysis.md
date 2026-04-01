# Prompt 01: Substrate Analysis

Use this prompt when you need to inspect an existing graph-based project and extract only the parts that matter for a paper-facing method design.

```text
Write like a careful research collaborator, not like a product marketer.
Prefer narrow, defensible conceptual framing over broad claims.
When uncertain, explicitly mark the boundary between existing implementation and proposed paper-layer design.

We are NOT redesigning or re-implementing the existing project right now.

Current goal:
Analyze the existing graph substrate as the basis for a paper-oriented Scenario Memory Layer.

Important constraints:
- Do NOT modify the codebase.
- Do NOT implement new schema classes or runtime logic.
- Do NOT propose a full system rewrite.
- This task is for paper writing, not engineering delivery.

Please inspect the existing schema and architecture and create:
- `manuscript/framework/scenario_memory_layer_analysis.md`

Structure:
- Overview
- What the current graph already provides
- What is still implicit rather than explicit
- Why this matters for the paper thesis
- Key design opportunity

Focus on:
- what the current graph already models well for SME decision support
- which entities and relations are already useful for scenario-oriented reasoning
- how the current ingestion/memory pipeline already supports structured memory
- what is still missing if full decision scenarios are to be represented explicitly

Requirements:
- optimize for paper writing, not system inventory
- do not invent implementation details
- clearly separate existing substrate from proposed paper-layer interpretation
```
