# SME Decision-Making Pain Points, AI Support Limits, and the Case for a Scenario-Oriented Analytical Lens

## 1. Introduction

Small and medium-sized enterprises (SMEs) occupy a difficult decision environment. Compared with larger firms, they often operate with less managerial specialization, less analytical slack, lower financial buffers, and more concentrated decision authority. These constraints are not incidental. They shape how decisions are framed, what evidence is available, how quickly alternatives must be assessed, and how much of the decision process can realistically be formalized. In this setting, AI support systems are often introduced with the promise of better information access, faster analysis, and more timely business insight. Yet the current literature reviewed in this repository suggests a more uneven picture.

Evidence-backed findings indicate that SME research is strongest on decision difficulty under uncertainty, working-capital pressure, uneven data conditions, and owner-manager-centered judgment (Adomako, 2022; Cieślik et al., 2021; Salles, 2006; Wong et al., 2018). By contrast, the AI-for-SME literature is stronger on adoption barriers, digital readiness, and functional applications than on decision-grade context reconstruction (Oldemeyer et al., 2025; Schwaeke et al., 2025; Hansen and Bøgh, 2021). Adjacent literatures on retrieval-augmented generation (RAG), conversational memory, workflow memory, episodic memory, and process intelligence suggest that current systems may be capable of retrieving fragments, summarizing documents, or preserving limited continuity, while still falling short of reconstructing a complete decision situation.

This review-analysis article synthesizes those strands. It does not present a validated framework, a methods contribution, or an empirical system evaluation. Instead, it asks a narrower analytical question: what does the literature currently support about SME decision pain points, what kinds of support current AI systems appear able to provide, and whether a scenario-oriented framing offers a useful, but still provisional, way to interpret the remaining gap.

## 2. Review Scope and Analytical Lens

This article is based on prior literature reconnaissance notes in this repository rather than on a new systematic search. The source base combines four types of material: SME decision-making studies, SME AI adoption reviews, adjacent AI memory and RAG studies, and process-intelligence or decision-traceability work. The scope is deliberately asymmetric. SME-specific evidence is stronger on the business problem side than on the memory-architecture side. The architecture side relies more heavily on adjacent literatures.

Two distinctions structure the analysis. First, evidence-backed observations are treated separately from working hypotheses. Second, the article distinguishes between what current systems can do at the level of information assistance and what they may still fail to do at the level of decision reconstruction. This distinction matters because "useful AI" for search, summarization, or workflow aid does not automatically imply "decision-grade AI" for weakly structured business decisions.

Table 1 summarizes the analytical scope used in this review.

| Analytical dimension | What was included | What was not treated as sufficient on its own | Why it matters |
| --- | --- | --- | --- |
| SME decision conditions | Uncertainty, cash-flow pressure, staffing limits, information problems, informal decision routines | Generic claims that SMEs are "challenging" environments | Grounds the problem in concrete managerial conditions |
| SME AI literature | Adoption reviews, functional application surveys, readiness barriers | Productivity claims without decision-task specificity | Shows what the SME AI literature currently emphasizes |
| Adjacent AI memory literature | RAG sufficiency, long-term memory, workflow memory, episodic memory | Benchmark gains without a plausible bridge to business decisions | Clarifies where the context-reconstruction argument is coming from |
| Process intelligence literature | Decision mining, traceability, explainable process monitoring | General BPM claims without decision relevance | Provides non-LLM precedents for structured decision context |

The resulting lens is not "AI for SMEs" in the broadest sense. It is closer to the narrower question of how AI systems might support weakly structured SME decisions that depend on incomplete, cross-source, temporally distributed context.

## 3. SME Decision-Making Pain Points

The reviewed literature suggests that SME decision difficulty does not arise from a single bottleneck. It emerges from the interaction of data problems, operational pressures, strategic uncertainty, and organizational or cognitive limits. The recurring theme is not simply that SMEs have less data or less technology. Rather, they often have less capacity to convert imperfect information into defensible decisions under time and resource pressure.

### Evidence-backed findings

- SME decisions are often made under uncertainty rather than under stable planning assumptions (Adomako, 2022).
- Short-term working-capital constraints can materially crowd out longer-term investment choices (Cieślik et al., 2021).
- Tactical and strategic decisions in SMEs are frequently weakly structured, which makes it hard to define information requirements in advance (Salles, 2006).
- Smaller entrepreneurial firms often rely on less comprehensive decision routines than larger professionally managed firms (Mitchell, 1988).
- Owner goals, life events, and personal perspectives can directly shape business and financial decisions in SMEs (Wong et al., 2018).
- Recent review literature also points to limited skills, poor data conditions, and integration difficulty as recurring constraints on data-driven decision making (Oldemeyer et al., 2025; Schwaeke et al., 2025; Kgakatsi et al., 2024).

Table 2 organizes the recurring pain points into four categories.

| Pain point category | Typical manifestation in SMEs | Why it disrupts decision quality | Evidence status in current notes | Consequence for AI support |
| --- | --- | --- | --- | --- |
| Data problems | Partial, lagged, or weakly integrated records; irregular use of financial information; difficulty specifying information needs for weakly structured decisions | Obscures current state, hides missing variables, and makes comparison across alternatives fragile | Moderate to strong; supported by Salles (2006), Gibson (1992), Oldemeyer et al. (2025), Kgakatsi et al. (2024) | Systems must surface missing information, provenance, and uncertainty rather than assume a complete data view |
| Operational problems | Working-capital pressure, staffing constraints, and low organizational slack | Forces short-horizon choices, compresses analysis time, and elevates immediate constraints over abstract optimization | Strong on liquidity; moderate on staffing/slack; supported by Cieślik et al. (2021) and Wong et al. (2018) | Support must treat liquidity, labor, and execution constraints as first-class decision variables |
| Strategic problems | Dynamic market conditions, weakly structured choices, and multi-objective trade-offs | Makes it difficult to stabilize goals, rank criteria, and know which information is decision-relevant | Moderate to strong; supported by Adomako (2022), Salles (2006), Molina-Abril et al. (2025) | Support must help structure the problem itself, not only retrieve evidence after the problem is defined |
| Organizational/cognitive problems | Owner-manager centrality, informal routines, and satisficing under pressure | Concentrates judgment in a small group and leaves more of the decision state implicit or tacit | Strong; supported by Mitchell (1988), Wong et al. (2018), Adomako (2022) | Support must fit informal decision practice and make assumptions explicit without requiring enterprise-style formalization |

What appears specific to SMEs, relative to larger firms, is not only scale but decision architecture. Larger firms can often distribute decision work across finance, analytics, operations, and strategy functions. SMEs more often compress those roles into a small owner-manager group. This makes decision quality more dependent on a combination of partial records, tacit knowledge, and rapidly changing operational constraints.

Table 3 highlights the differences that matter most for the present review.

| Dimension | Typical SME condition | Typical larger-firm condition | Consequence for decision support |
| --- | --- | --- | --- |
| Decision authority | Concentrated in owners or a small leadership group | Distributed across specialized roles | Support must fit owner-manager judgment rather than idealized formal process |
| Information infrastructure | More uneven, fragmented, or manually maintained | More formalized and integrated | Systems cannot assume clean enterprise data architecture |
| Resource slack | Lower financial and staffing buffers | Greater functional redundancy and analytical capacity | Decisions are more time-sensitive and constraint-dominated |
| Decision formalization | More informal or simplified | More formalized and process-governed | Support should surface assumptions and gaps rather than assume complete specifications |

The practical implication is that SME decision support is inherently a context problem. A recommendation is only as useful as its ability to account for the constraints, history, and evidentiary limits surrounding a decision episode.

## 4. What Current AI Support Systems Can and Cannot Do

The current literature does support a meaningful but bounded view of what AI can do for SMEs and related business contexts. In the SME-focused literature, AI is mostly associated with functional assistance: prediction, risk assessment, customer analysis, process optimization, and information retrieval. These are valuable capabilities, but they are not equivalent to reconstructing the full business situation in which a decision is made.

Evidence-backed synthesis from the review notes suggests that current systems are strongest at:

- retrieving relevant documents or fragments
- summarizing material for faster inspection
- answering bounded questions over provided context
- offering predictive support in specific business functions
- maintaining limited conversational continuity
- guiding repeated tasks through workflow-like procedural support

What the current literature does not strongly demonstrate, at least in SME-specific settings, is that these systems can reconstruct the full decision episode: the operative goal, active constraints, triggering event, action path, observed outcome, and evidentiary basis for a conclusion.

Table 4 compares the main context-support types discussed in the literature reviewed here.

| Current AI support type | Typical context basis | What it supports well | What remains under-specified for decision-grade reasoning | Evidence basis |
| --- | --- | --- | --- | --- |
| Document retrieval / RAG | Retrieved passages, files, reports, and knowledge stores | Locating relevant source material and grounding answers in accessible documents | Sufficiency of context, chronology, weighting of alternatives, and explicit rationale | Strong adjacent evidence from Joren et al. (2025) and Wu et al. (2025) |
| Summarization / question answering | Local document context or conversation window | Faster inspection of large volumes of text and bounded answering over supplied context | The user's operative goal, omitted constraints, and whether the available evidence is enough to decide | Moderate; supported indirectly by RAG sufficiency literature and by the absence of stronger SME-specific evidence |
| Functional predictive support | Task-specific business data such as sales, risk, or customer signals | Forecasting, classification, and narrow decision aids inside bounded functions | Cross-functional trade-offs, explanation of actionability, and integration with broader business context | Strong for bounded tasks in SME AI reviews; weak for full decision reconstruction |
| Conversational assistants with persistence | Dialogue history plus limited persistent user facts | Continuity, personalization, and repeated interaction quality | Business episode boundaries, changing constraints, and explicit links between past advice and later outcomes | Moderate adjacent evidence from long-term conversational memory work |
| Workflow or process-aware assistance | Reusable routines, event logs, or action traces | Repeated task execution, procedural guidance, and structured operational support | Case-specific deviations, tacit business judgment, and informal decisions outside logged workflows | Moderate to strong in adjacent workflow-memory and process-intelligence literature |
| Long-term user memory | Persistent preferences, facts, and user history | Stable personalization across sessions | Knowing the actor is not the same as reconstructing the decision situation facing that actor | Moderate adjacent evidence; concept clearer in agent literature than in SME DSS literature |

This distinction matters because systems can look competent in interaction while still underrepresenting the decision context that matters most. A summary of a contract, a prior conversation, or a market report may be accurate and still not be enough for a decision that depends on timing, trade-offs, organizational constraints, and evidentiary uncertainty.

## 5. Why Fragment Retrieval Is Not Decision Support

The strongest direct support for this article's central concern does not come from SME-specific evaluations. It comes from adjacent work on RAG and structured decision support. The key point is not that retrieval is useless. It is that retrieval is a partial support layer, not a complete decision layer.

`Sufficient Context: A New Lens on Retrieval Augmented Generation Systems` is especially relevant because it shows that retrieved material can be relevant while still being insufficient for correct reasoning. This matters in business settings because decisions frequently require abstention, explicit uncertainty, or comparison of alternatives rather than merely a plausible answer. `Retrieval Augmented Decision-Making` reinforces the same point in a more decision-oriented register by arguing that standard RAG provides context-related suggestions but remains weak on weighting, reasoning transparency, and structured support.

This distinction can be made more explicit by separating fragment retrieval from decision support requirements.

| Dimension | Fragment retrieval | Decision-grade context |
| --- | --- | --- |
| Primary unit of support | Passage, snippet, file, or isolated fact | Decision episode linking goal, constraints, trigger, action, outcome, and evidence |
| Typical success criterion | Relevant material is found and surfaced | A user can compare alternatives, understand trade-offs, and justify action under uncertainty |
| Time structure | Often weakly temporal or document-local | Explicitly chronological and sensitive to what changed over time |
| Treatment of constraints | Constraints may be mentioned if present in retrieved text | Constraints are modeled as active filters on what actions are feasible |
| Treatment of evidence gaps | Missing information can remain implicit | Missing information must be surfaced as a decision-relevant gap |
| User burden after system output | User still integrates fragments into a coherent situation model | System reduces synthesis burden by organizing the situation model itself |

The literature reviewed so far therefore supports a narrow conclusion: fragment retrieval is helpful, but it should not be treated as equivalent to decision support when the decision depends on more than document access. This is especially important in SME settings where decisions are often weakly structured and information is only partly formalized.

## 6. Related Concepts in the Literature

One difficulty in evaluating the present argument is terminological. The phrase `scenario memory` does not appear, in the current notes, to be a dominant established term. The nearest precedents are distributed across several literatures rather than gathered under one shared concept. This is both an opportunity and a risk: it suggests a cross-disciplinary gap, but it also means that the argument must avoid relabeling known ideas without adding clarity.

The closest adjacent concepts are as follows:

- `episodic memory`: memory of distinct past events or event sequences
- `workflow memory`: reusable routines extracted from prior action traces
- `case-based reasoning`: reuse of prior cases to support current decisions
- `decision traceability`: explicit record of how evidence and reasoning produced a recommendation
- `decision mining` or `process memory`: discovery or prediction of decisions from event logs and process traces

These concepts do not solve the same problem in the same way. Episodic memory emphasizes event-grounded recall. Workflow memory emphasizes reusable procedure. Case-based reasoning emphasizes analogical reuse. Decision traceability emphasizes justification. Process intelligence emphasizes structured traces. A scenario-oriented framing is analytically useful only if it clarifies how these partial mechanisms relate to one another in business decision settings.

Table 5 summarizes the comparison.

| Concept | Primary unit of context or memory | Main analytical strength | Why it is insufficient on its own | Relation to a scenario-oriented lens |
| --- | --- | --- | --- | --- |
| Episodic memory | Distinct past events or event sequences | Preserves temporally grounded recall and event continuity | Does not by itself specify decision criteria, evidence standards, or business constraints | Likely one component of scenario-oriented support |
| Workflow memory | Reusable action trajectories or routines | Captures procedure and repeatable task structure | May preserve how tasks were executed without capturing why a particular choice was justified in context | Likely useful where decisions are embedded in recurring workflows |
| Case-based reasoning | Prior cases linking problem, response, and outcome | Provides a strong decision-support precedent for analogical reuse | Older literature and not designed for modern multi-source LLM settings | Closest historical analogue to scenario-level reuse |
| Decision traceability | Evidence and reasoning path behind a recommendation | Supports auditability, explanation, and trust | Can explain a reasoning path without reconstructing the full surrounding situation | Likely a necessary property, not the whole memory model |
| Decision mining / process intelligence | Event-log traces and decision points in processes | Works well for structured operational decisions and explicit process states | Depends on logs and process structure that many SMEs may not possess comprehensively | Important adjacent literature for structured subsets of the problem |
| Scenario-oriented memory | Working Hypothesis: business decision episode as the unit of support | Integrates goals, constraints, triggers, actions, outcomes, and evidence in one analytical frame | Not an established standard term; currently a synthesis label rather than a validated category | Proposed umbrella lens for combining the partial strengths above |

The closest conservative interpretation is that the literature does not yet justify a claim that `scenario memory` is an established category. It does justify treating it as a provisional analytical lens for thinking about how these existing concepts might need to be combined.

## 7. A Scenario-Oriented View of Decision Memory

### Working Hypothesis

A scenario-oriented view of decision memory can be understood as the idea that decision support should preserve not just information fragments, but the decision episode as such. In this sense, the relevant unit is not a document, a conversation turn, or a user preference alone. It is a structured business situation that includes:

- the operative goal
- the active constraints
- the triggering challenge or event
- the alternatives considered
- the action taken
- the observed or expected outcome
- the evidence supporting the reasoning

This view should remain tentative. The current literature reviewed in this repository does not validate scenario-oriented memory as an established framework. What it does suggest is that the combination of SME decision conditions and AI support limits makes such a lens analytically useful.

The strongest version of the thesis would be that some SME decisions require an architecture combining document memory, persistent factual memory, event or episode-level memory, workflow context, and decision traceability. The weaker and more defensible version is narrower: some SME decisions appear to require more explicit treatment of episode-level context and traceability than current support systems typically provide.

Table 6 makes that distinction explicit.

| Version of the thesis | Claim strength | What the current literature supports |
| --- | --- | --- |
| Strong version | Decision-grade SME AI requires a combined scenario-memory architecture | Only partial indirect support from adjacent literature |
| Weak version | Some SME decisions require more explicit episode-level context and traceability than current systems usually provide | Plausible and more defensible given current notes |
| Overstated version to avoid | Scenario memory is already an established validated category for SME AI | Not supported by current evidence base |

## 8. Discussion and Research Opportunities

The central analytical result of this review is not that current AI systems are ineffective, nor that a new memory architecture has already been justified. It is that the literature points to a mismatch: SME decisions often depend on weakly structured, cross-source, constraint-heavy context, while current AI systems are more mature on retrieval, summarization, prediction, personalization, and procedural assistance.

This mismatch suggests several research opportunities.

First, the field needs task-level evidence rather than only conceptual appeal. It is not enough to say that richer memory would help. A stronger evidence base would compare fragment retrieval against richer contextual reconstruction on SME-like decision tasks. Second, the process-intelligence literature should be integrated more seriously into the AI-for-SME conversation. Event-log-based and traceability-oriented work may already solve part of the problem for structured operational decisions. Third, the literature needs better empirical work on how SMEs actually use prior episodes, partial records, and tacit knowledge when making repeat or comparable decisions.

Several cautions follow from the same review. The apparent gap may partly reflect publication lag rather than total absence of capable systems. The core bottleneck may be organizational readiness rather than memory architecture in some settings. Some terms currently in use, such as `document memory` or `long-term user memory`, may be more engineering shorthand than stable scholarly categories. And some of the strongest adjacent work still lacks direct SME validation.

The most productive near-term research program would therefore avoid grand claims. It would ask narrower questions such as:

- Which SME decisions are most dependent on episode-level context?
- When does retrieval fail because context is insufficient rather than because retrieval itself is poor?
- Which combination of traceability, case memory, workflow context, and event recall matters most for business users?
- What evidence would show real improvement in decision quality rather than only in user satisfaction?

## 9. Conclusion

The literature reviewed in this repository supports three conclusions. First, SME decision-making is difficult for reasons that are concrete and recurring: uncertainty, short-term financial pressure, limited analytical capacity, weakly structured choices, and owner-manager-centered judgment. Second, current AI systems appear better at retrieving, summarizing, predicting, and guiding bounded tasks than at reconstructing full business decision situations. Third, a scenario-oriented framing is analytically useful because it draws attention to what may be missing between fragment-level support and decision-grade reasoning.

At the same time, the review does not justify presenting scenario-oriented memory as a validated framework or mature category. The more defensible claim is narrower: for at least some SME decisions, explicit episode-level context and traceability may matter more than current support systems typically capture. If that claim holds under stronger empirical study, it would provide a more grounded basis for future design work on decision-grade AI support in SME contexts.
