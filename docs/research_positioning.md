# Research Positioning

## Problem framing

### Evidence-backed synthesis

- SME decision-making is shaped by uncertainty, resource constraints, concentrated owner-manager judgment, weakly structured choices, and uneven information quality.
- The literature reviewed so far suggests that SME decision problems are not just about missing data in the abstract; they are often about making time-sensitive choices with incomplete information, limited analytical capacity, and limited organizational slack.
- The SME AI literature is stronger on adoption barriers and functional applications than on the architecture of decision support systems for owner-manager decisions.

### Conceptual framing

- A narrow way to frame the problem is:
  - SME decision support requires more than retrieval, prediction, or generic memory because many real decisions depend on reconstructing the relevant business situation across goals, constraints, triggers, actions, outcomes, and evidence.
- This framing should remain provisional until supported by stronger task-level evidence.

## Why SME decision support is hard

### Evidence-backed synthesis

- SME decisions are often made under uncertainty rather than under stable planning assumptions.
- SMEs face stronger short-term liquidity pressure and lower human-resource slack than larger firms.
- Decision authority is frequently concentrated in owners or small management teams.
- Tactical and strategic decisions are often weakly structured, which makes information requirements harder to specify in advance.
- Information use may be irregular, incomplete, or only partly formalized.

### Conceptual framing

- Together, these conditions make SME decision support hard because the relevant decision state is distributed across:
  - partial records
  - current constraints
  - tacit manager knowledge
  - prior episodes
  - shifting external conditions

## Why current AI support is insufficient

### Evidence-backed synthesis

- Current AI systems appear strongest at:
  - document retrieval
  - summarization
  - question answering
  - prediction in bounded tasks
  - limited conversational continuity
  - workflow guidance in repeated tasks
- Adjacent literature shows that fragment retrieval is not the same as sufficient context.
- Structured decision-support work suggests that ordinary RAG is weak when decisions require weighting, traceable reasoning, or explicit comparison of alternatives.
- Workflow-memory and episodic-memory papers suggest useful directions, but they are not SME-specific evidence that business decision reconstruction is already solved.

### Conceptual framing

- A conservative interpretation is that current systems are often optimized for helpfulness over fragments, not for explicit reconstruction of decision episodes.
- The likely insufficiency is not that AI lacks all memory, but that the available memory forms may be misaligned with what decision-grade SME reasoning requires.

## Candidate research gap

### Evidence-backed synthesis

- There is no strong SME-specific literature base yet showing that current AI systems adequately reconstruct decision-grade business context for owner-manager decisions.
- There is adjacent evidence that:
  - retrieval can be insufficient
  - conversational memory is limited
  - workflow memory helps with procedure
  - process-intelligence literature supports traceability and event-aware reasoning in structured settings

### Conceptual framing

- Candidate gap:
  - a missing integration between SME decision-support needs, memory or context design for AI systems, and traceable reconstruction of business decision situations.
- More narrowly:
  - the gap may be not "AI for SMEs" in general, but `AI support for weakly structured SME decisions that require cross-source, time-aware, traceable context reconstruction`.

## Competing framings of the gap

1. `Readiness framing`
   - The real gap is SME capability, not AI architecture.
   - On this view, data quality, budgets, infrastructure, and skills are the primary bottlenecks.

2. `Traceability framing`
   - The real gap is not memory but explanation and auditability.
   - On this view, decision traceability and structured rationale matter more than richer memory representations.

3. `Task-design framing`
   - Current systems seem insufficient because they are built for retrieval, drafting, and productivity, not for decision support.
   - On this view, the key problem is evaluation target mismatch.

4. `Process-intelligence framing`
   - The relevant precedent is process mining or decision mining rather than LLM memory.
   - On this view, the solution space may already exist for structured workflows and only needs adaptation.

5. `Scenario-memory framing`
   - Current systems lack a sufficiently rich representation of the business decision episode itself.
   - On this view, fragment retrieval, user memory, and conversation history do not yet reconstruct the situation well enough for decision-grade reasoning.

## Strongest version of the scenario-memory thesis

### Working Hypothesis

- Many SME decisions are weakly structured, cross-document, time-dependent, and constraint-heavy.
- Current AI systems appear better at surfacing relevant fragments than at reconstructing the full decision situation in a traceable and reusable form.
- Therefore, a useful next step may be an AI architecture for SMEs that combines:
  - document memory
  - persistent factual memory
  - event or episode-level memory
  - workflow or process context
  - decision traceability
- Under this formulation, `scenario memory` is not a standalone memory primitive already established in the literature, but a design shorthand for combining these capabilities around a business decision episode.

## Weakest / most defensible version of the thesis

### Working Hypothesis

- The current literature suggests a mismatch between common AI support mechanisms and the context requirements of some SME decisions.
- In particular, retrieval and summarization alone may be insufficient when decisions require explicit handling of:
  - constraints
  - chronology
  - alternatives
  - outcomes
  - evidentiary support
- A defensible paper does not need to prove a brand-new memory category.
- It may be enough to argue that SME decision support needs a more explicit treatment of episode-level context and traceability than current systems typically provide.

## What would count as evidence

- Empirical studies showing that SME decision tasks fail when systems only retrieve documents or summarize fragments.
- Comparative evaluations where richer contextual reconstruction outperforms plain retrieval or plain conversational memory on SME-like decision tasks.
- Evidence that owners or managers rely on cross-episode context such as prior decisions, constraints, outcomes, and rationales when making repeat or comparable decisions.
- Studies showing that process-aware or event-aware context improves decision quality, explanation quality, or user trust in business settings.
- Evidence that decision-support users need explicit representation of assumptions, constraints, and evidence provenance to act confidently.

## What would count as non-evidence

- Generic claims that AI is useful for business productivity.
- Evidence that AI improves forecasting, search, drafting, or general analytics without testing decision reconstruction.
- Memory benchmark gains on unrelated tasks without a credible bridge to SME decision support.
- Adoption-barrier studies alone.
- Claims based only on product marketing or anecdotal enterprise-copilot usage.

## 3 candidate paper contribution statements

1. This paper synthesizes SME decision-making literature and adjacent AI-memory literature to argue that current support systems are under-specified for weakly structured SME decisions that require cross-source and time-aware context reconstruction.

2. This paper proposes a conceptual framework for SME decision support that distinguishes document retrieval, persistent factual memory, workflow context, and episode-level decision context, and clarifies where current systems remain limited.

3. This paper reframes the AI-for-SME research gap from general adoption or functional automation toward traceable reconstruction of decision situations, identifying a narrower and more defensible target for future system design and evaluation.

## 3 candidate paper titles

1. `From Fragment Retrieval to Decision Context: Positioning a Research Gap in AI Support for SMEs`

2. `Toward Decision-Grade AI for SMEs: Context Reconstruction, Traceability, and the Limits of Current Support Systems`

3. `AI Support for Weakly Structured SME Decisions: A Research Positioning Note on Context, Memory, and Traceability`
