# AI Limits for SME Decision Support

## What current systems do well

- Current AI systems appear strongest at information-access and synthesis tasks rather than full decision reconstruction.
- In the SME literature, AI is most often presented as useful for:
  - forecasting demand or sales
  - customer analysis
  - credit or risk assessment
  - document or information retrieval
  - business-function optimization
- The SME review literature therefore supports a modest claim:
  - AI can improve access to information, predictions, and functional analytics in SMEs.
  - It does not yet strongly support the claim that current systems reliably reconstruct decision-grade business context end to end.
- Adjacent DSS and BI literature also supports the idea that data and analytics systems can convert more data into more insight.
  - Phillips-Wren and Dalla Bona (2021) explicitly frame BI and analytics as a descendant of DSS oriented toward improving decision making through data and analysis.
- In LLM and enterprise-assistant adjacent literature, current systems do reasonably well at:
  - retrieval over document collections
  - question answering over supplied context
  - short-horizon conversational support
  - long-term conversation support when explicit memory mechanisms are added
  - workflow guidance when prior routines can be induced and reused

## What they do not reconstruct well

- The literature reviewed here suggests that many current systems do not robustly reconstruct the full decision episode needed for business reasoning, especially across time and heterogeneous evidence sources.
- The missing elements often include:
  - the user's operative goal
  - the constraints active at the time
  - the triggering challenge or event
  - the action taken
  - the observed outcome
  - the evidence chain supporting the conclusion
- In other words, many systems can retrieve pieces of context but not necessarily rebuild the situation in which a business decision was made.
- This gap is clearest in adjacent literature rather than in SME-specific evaluations.
- The process-intelligence literature partly addresses this through event logs, decision mining, and explainable predictive process analytics.
  - However, these approaches typically depend on structured traces and do not automatically cover the broader mix of documents, tacit manager knowledge, ad hoc constraints, and informal decisions that characterize many SMEs.

## Evidence for fragment-retrieval limitation

1. Retrieval support is not the same as sufficient context.
   - `Sufficient Context: A New Lens on Retrieval Augmented Generation Systems` argues that relevant retrieved material may still be insufficient for answering correctly.
   - This is directly relevant because business decisions often require enough context to abstain, compare alternatives, or state uncertainty, not merely enough text to sound plausible.

2. RAG-oriented systems can remain weak on traceable and structured decision support.
   - `Retrieval Augmented Decision-Making` explicitly argues that standard RAG methods provide context-related suggestions but lack quantitative weighting and traceable reasoning paths for structured decision support.
   - This is one of the clearest sources in this pass linking retrieval limits to decision-support limits.

3. Long-term memory in LLMs remains fragile.
   - `Evaluating the Long-Term Memory of Large Language Models` shows that models can retain historical information to a degree, but that memory decays over time and varies by information category.
   - `Evaluating Very Long-Term Conversational Memory of LLM Agents` argues that even with long-context models and RAG, efficacy in very long-term dialogue remained underexplored enough to require a new benchmark grounded in temporal event graphs.

4. Conversational continuity is not equivalent to business scenario reconstruction.
   - `Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models` improves long-horizon conversation by generating explicit memory summaries.
   - This helps with continuity, but it does not by itself prove that a system can represent constraints, decisions, alternatives, and outcomes in a business-audit-ready way.

5. Workflow guidance is helpful but narrower than scenario reconstruction.
   - `Agent Workflow Memory` shows that agents can benefit from induced reusable routines.
   - This is strong evidence for procedural or workflow memory, but the benchmarked benefit is on long-horizon action trajectories rather than on reconstructing business decision episodes with evidence and outcomes.

## Related concepts from adjacent literature

### Closest established terms

- `document memory`
  - Closest manifestation: retrieval over documents, external knowledge stores, or RAG pipelines.
  - What it supports well: locating and surfacing relevant source material.
  - Main limitation: does not guarantee sufficient context, weighting, chronology, or rationale.

- `conversational memory`
  - Closest manifestation: short- and long-term dialogue memory across sessions.
  - What it supports well: continuity, personalization, and consistency in interaction.
  - Main limitation: preserving prior dialogue is not the same as preserving an operational decision state.

- `long-term user memory`
  - Closest manifestation: persistent user facts, preferences, and history across interactions.
  - What it supports well: personalization and repeated interaction quality.
  - Main limitation: knowing the user is not the same as reconstructing a specific business scenario.
  - Note: this term appears more in agent-memory and personalized-assistant literature than in SME DSS literature.

- `workflow memory`
  - Closest manifestation: reusable routines learned from prior action trajectories.
  - What it supports well: procedural guidance for repeated tasks.
  - Main limitation: a workflow can tell a system how to act without fully representing why a specific decision was appropriate in a particular case.

- `episodic memory`
  - Closest manifestation: memory for unique past experiences or event sequences.
  - What it supports well: event-based retrieval and temporally grounded recall.
  - Main limitation: current episodic-memory work is promising but still mostly benchmarked in general LLM settings, not SME decision support specifically.

- `decision traceability`
  - Closest manifestation: explicit record of what evidence, rules, and reasoning led to a recommendation or decision.
  - What it supports well: transparency, auditability, and justification.
  - Main limitation: traceability can explain a decision path without necessarily reconstructing the full scenario that made the decision meaningful.

- `decision mining` or `process memory`
  - Closest manifestation: event-log-based discovery or prediction of decisions in processes.
  - What it supports well: structured operational decisions in process-aware environments.
  - Main limitation: assumes event logs and structured traces that many SMEs may not possess comprehensively.

### Working Hypothesis

- `scenario memory` does not appear to be a standard dominant term in the literature reviewed here.
- The closest established terms are:
  - episodic memory
  - workflow memory
  - case-based reasoning
  - decision traceability
  - decision mining
  - long-term conversational memory
- Working Hypothesis:
  - the proposed idea of `scenario memory` may be best understood as a composite requirement spanning episodic recall, process or workflow context, and decision traceability.

## Candidate gap statement

- Candidate gap statement:
  - Current AI systems for SME support appear better at retrieving fragments, summarizing documents, and maintaining partial conversational or user memory than at reconstructing decision-grade business scenarios that integrate goals, constraints, triggering events, actions, outcomes, and evidentiary support.
- More conservative version:
  - The literature reviewed so far suggests a mismatch between what many AI support systems optimize for and what SME decision support often requires.
  - Existing systems are more mature on information retrieval, prediction, personalization, and workflow assistance than on explicit reconstruction of business decision episodes.
- Strongest defensible formulation from this pass:
  - There is likely a gap at the intersection of SME decision support, LLM memory design, and process traceability.
  - This gap is suggested by adjacent literatures, but not yet firmly established by a dedicated SME-specific body of evidence.

## Risks of overstating the gap

- Risk 1:
  - The problem may be less about memory architecture and more about poor data availability, weak system integration, and lack of organizational readiness in SMEs.

- Risk 2:
  - Process mining, decision mining, and explainable predictive process analytics may already solve part of the problem in structured operational settings.
  - If so, the true gap is narrower: informal and cross-source business scenario reconstruction, not decision support in general.

- Risk 3:
  - Some enterprise copilots may already implement combinations of document retrieval, persistent memory, workflow context, and tool use.
  - The academic literature on such systems may simply still be thin, meaning the gap could be empirical-publication lag rather than technical absence.

- Risk 4:
  - `Scenario memory` may be a useful design label but not a distinct theoretical contribution unless it is differentiated clearly from episodic memory, case-based reasoning, and traceability.

- Risk 5:
  - Decision-grade support may require more than memory.
  - It may also require explicit representation of alternatives, preferences, constraints, uncertainty, and accountability.

## TODO: terms to validate further

- TODO: validate whether `business process memory` is an established term with enough relevant literature or whether `process intelligence` and `decision mining` are the better anchors.
- TODO: validate whether `case-based reasoning` is the strongest historical precedent for scenario-level decision support.
- TODO: validate whether `episodic memory` in LLM literature can be translated credibly into business decision settings without becoming only a metaphor.
- TODO: find stronger literature on enterprise assistants or business copilots evaluated in real decision workflows rather than productivity tasks alone.
- TODO: find SME-specific studies, if any, on AI systems that persist user context, organizational memory, or decision rationale across multiple business episodes.
- TODO: verify whether `document memory`, `long-term user memory`, and `conversational memory` are standard formal terms or mostly engineering shorthand.

## Source notes

- `bgpt-paper-search` was not used in this pass because the BGPT remote MCP server is not configured in this Codex environment.
- The strongest evidence in this note comes from adjacent literatures:
  - SME AI reviews
  - DSS and BI research
  - RAG limitation papers
  - long-term memory papers
  - workflow and process-intelligence papers

## Sources used in this pass

- Le Dinh, T., Vu, M.-C., & Tran, G. T. C. (2025). `Artificial Intelligence in SMEs: Enhancing Business Functions Through Technologies and Applications`. Information, 16(5), 415. https://doi.org/10.3390/info16050415
- Phillips-Wren, G., & Dalla Bona, M. (2021). `Reconciling business intelligence, analytics and decision support systems: More data, deeper insight`. Decision Support Systems, 146, 113560. https://doi.org/10.1016/j.dss.2021.113560
- Joren, H., Zhang, J., Ferng, C.-S., Juan, D.-C., Taly, A., & Rashtchian, C. (2025). `Sufficient Context: A New Lens on Retrieval Augmented Generation Systems`. ICLR 2025 / arXiv:2411.06037. https://doi.org/10.48550/arXiv.2411.06037
- Wu, H., Zhang, H., Chen, W., & Xia, J. (2025). `Retrieval Augmented Decision-Making: A Requirements-Driven, Multi-Criteria Framework for Structured Decision Support`. arXiv:2505.18483. https://doi.org/10.48550/arXiv.2505.18483
- Jia, Z., Liu, Q., Li, H., Chen, Y., & Liu, J. (2025). `Evaluating the Long-Term Memory of Large Language Models`. Findings of ACL 2025, 19759-19777. https://doi.org/10.18653/v1/2025.findings-acl.1014
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). `Evaluating Very Long-Term Conversational Memory of LLM Agents`. ACL 2024. https://doi.org/10.48550/arXiv.2402.17753
- Xie, T., Zhao, C., Song, Y., Wu, C., Bian, J., & Rudzicz, F. (2025). `Recursively summarizing enables long-term dialogue memory in large language models`. Neurocomputing, 639, 130193. https://doi.org/10.1016/j.neucom.2025.130193
- Wang, Z. Z., Mao, J., Fried, D., & Neubig, G. (2024). `Agent Workflow Memory`. arXiv:2409.07429. https://doi.org/10.48550/arXiv.2409.07429
- Fountas, Z., Benfeghoul, M. A., Oomerjee, A., Christopoulou, F., Lampouras, G., Bou-Ammar, H., & Wang, J. (2025). `Human-inspired Episodic Memory for Infinite Context LLMs`. ICLR 2025 / arXiv:2407.09450. https://doi.org/10.48550/arXiv.2407.09450
- Ben-Youssef, O., Fahland, D., Park, G., Wynn, M. T., & van der Aalst, W. M. P. (2024). `Explainable predictive process monitoring`. Process Science, 1, 3. TODO: verify final citation details before reuse.
- Park, G., Küsters, A., Tews, M., Pitsch, C., Schneider, J., & van der Aalst, W. M. P. (2022). `Explainable Predictive Decision Mining for Operational Support`. arXiv:2210.16786. https://doi.org/10.48550/arXiv.2210.16786
