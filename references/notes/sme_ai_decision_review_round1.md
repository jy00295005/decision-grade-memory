# SME AI Decision Review Round 1

## Research question

Working placeholder: What decision-making pain points do SME owners and managers face in the AI era, what limitations characterize current AI support systems for SME decision support, and is there a defensible research gap around scenario-oriented memory or context reconstruction?

## Search strategy

- This was a reconnaissance pass, not a full systematic review.
- Source priority: peer-reviewed reviews and surveys on SMEs and AI first; adjacent AI-memory and decision-support papers second.
- Search channels used:
  - `literature-review` workflow logic for scoping, keyword clustering, and inclusion/exclusion structure.
  - `citation-management` workflow logic for source verification and source-type filtering.
  - web search across Springer, ScienceDirect, Taylor & Francis, PubMed, arXiv, and Google Research pages.
  - `hypothesis-generation` workflow logic for competing explanations and gap framing.
- `bgpt-paper-search` was not used in this pass because the BGPT remote MCP server is not configured in this Codex environment.
- `markitdown` was not needed because the selected sources were readable as HTML or snippets.
- Search emphasis:
  - SME decision-making under uncertainty
  - AI adoption and implementation barriers in SMEs
  - AI decision support limitations: explainability, traceability, structured reasoning
  - adjacent memory concepts: episodic memory, workflow memory, case-based reasoning, decision traceability, decision mining

## Keyword clusters

- `SME` + `decision making` + `uncertainty`
- `SME` + `AI adoption` + `implementation challenges`
- `SME` + `decision support` + `AI`
- `retrieval augmented generation` + `sufficient context`
- `LLM agent` + `workflow memory`
- `episodic memory` + `LLM`
- `case-based reasoning` + `decision support`
- `decision traceability` + `operational support`
- `business process` + `decision mining`

## Inclusion criteria

- Peer-reviewed review, survey, or empirical paper directly addressing SMEs, small firms, or small business decision conditions.
- Credible academic sources addressing AI support limitations relevant to decision support, even if not SME-specific.
- Adjacent AI-memory papers included only when they helped interpret the scenario-memory hypothesis.
- English-language sources with enough bibliographic information to identify the paper.

## Exclusion criteria

- Non-academic commentary, vendor marketing, or unsupported blog claims.
- General AI hype pieces without a clear research contribution.
- SME papers focused only on broad digitalization with no AI or decision relevance.
- Memory papers with no plausible link to decision support or long-horizon context.

## Preliminary findings

### Evidence-backed findings

1. The strongest SME-side evidence in this pass concerns adoption and implementation barriers, not decision-grade memory architecture.
   - Oldemeyer, Jede, and Teuteberg's systematic review identifies 27 AI adoption challenges for industrial SMEs and highlights knowledge, costs, and IT infrastructure or digital maturity as the most frequent barriers.
   - The same review also notes that management conviction, ROI evaluation difficulty, and data-related constraints recur across studies.

2. The SME literature consistently frames small-firm decision-making as highly exposed to uncertainty, resource limits, and manager-centric judgment.
   - `Uncertainty and decision making in small firms` directly centers uncertainty as a core condition of small-firm decision-making.
   - Related SME and entrepreneurship literature in this pass points more generally to concentrated managerial judgment and limited formal decision-support capacity under uncertainty rather than abundant formal decision infrastructure.

3. Current SME AI adoption reviews emphasize compatibility, infrastructure, knowledge, resources, culture, regulation, and ecosystem conditions.
   - `The new normal: The status quo of AI adoption in SMEs` organizes 100+ reviewed articles into clusters such as compatibility, infrastructure, knowledge, resources, culture, competition, regulation, and ecosystem.
   - This literature is more mature on adoption readiness than on how AI should reconstruct business context for decision support.

4. There is adjacent evidence that retrieval-style context provision is often insufficient for higher-quality reasoning.
   - `Sufficient Context: A New Lens on Retrieval Augmented Generation Systems` explicitly distinguishes between cases where retrieved context is sufficient and cases where it is not, and shows that strong models often answer incorrectly rather than abstain when context is insufficient.
   - `Retrieval Augmented Decision-Making` argues that ordinary RAG-style approaches provide context-related suggestions but lack quantitative weighting and traceable reasoning paths for structured decision support.

5. There is adjacent evidence that memory mechanisms beyond simple retrieval are being developed under other names.
   - `Agent Workflow Memory` focuses on reusable workflows learned from prior action trajectories.
   - `Human-inspired Episodic Memory for Infinite Context LLMs` organizes long inputs into events and retrieves them through episodic mechanisms.
   - Case-based reasoning literature treats stored prior cases as a reusable decision-support memory.
   - Process and operational support literature uses terms such as decision mining and reasoning traceability rather than scenario memory.

### Working hypotheses

- Working hypothesis A: For SME decision support, the bottleneck may be less "knowledge retrieval" and more "reconstructing the right business situation across time, actors, constraints, and alternatives."
- Working hypothesis B: In high-business-logic domains, decision support may require a composite memory stack:
  - document memory for source material
  - long-term memory for persistent facts
  - scenario or episodic or workflow memory for reconstructing prior situations, decisions, and consequences
- Working hypothesis C: The research gap may sit at the boundary between SME decision support, process traceability, and LLM memory design rather than within any one of those literatures alone.

## Themes from the literature

## Theme 1. SME decision-making remains manager-centric and uncertainty-heavy

- Small firms face uncertainty with fewer buffers, thinner specialist support functions, and more concentrated decision authority.
- This makes decision quality highly sensitive to missing context, incomplete evidence, and heuristic shortcuts.
- Evidence in this pass is stronger for uncertainty and capability constraints than for AI-specific decision architectures.

## Theme 2. SME AI research is still dominated by adoption and implementation concerns

- The SME AI literature concentrates on whether and how SMEs can adopt AI at all.
- Repeated barriers include knowledge gaps, costs, infrastructure limits, data issues, and weak ROI assessment.
- This means the literature says much less about what "good AI decision support" should look like once basic adoption barriers are crossed.

## Theme 3. Fragment retrieval is a weak proxy for decision support

- Retrieval helps surface relevant fragments, but the adjacent LLM literature shows that retrieved context may still be insufficient, weakly structured, or hard to use reliably.
- For decision support, the missing pieces are often weighting, rationale, chronology, and reconstruction of the decision situation rather than access to isolated text passages.
- Evidence for this theme is indirect but meaningful; it comes from RAG and structured decision-support work rather than SME-specific studies.

## Theme 4. Relevant adjacent concepts already exist under other names

- `episodic memory`: event-based retrieval of prior context
- `workflow memory`: reusable procedural patterns extracted from prior action traces
- `case-based reasoning`: reuse of similar prior cases to support current decisions
- `decision traceability`: explicit record of how a recommendation or decision was formed
- `decision mining` or `process memory`: reconstructing or predicting decision paths from process traces

## Theme 5. The literature gap is partly terminological

- SME researchers often discuss readiness, capability, and managerial barriers.
- AI-memory researchers discuss episodic, workflow, or contextual memory.
- Process researchers discuss traceability, event logs, and decision mining.
- These communities appear weakly integrated around the specific problem of decision-grade business context reconstruction for SMEs.

## Competing explanations

1. `Organizational-readiness explanation`
   - AI support for SMEs is weak mainly because SMEs lack data, skills, budgets, and infrastructure.
   - On this view, memory architecture is secondary until readiness problems are solved.

2. `Traceability-and-governance explanation`
   - The core issue is not memory scarcity but weak explanation, documentation, and auditability.
   - On this view, structured reasoning and decision traceability matter more than richer memory.

3. `Task-design explanation`
   - Many current AI tools for SMEs are optimized for retrieval, summarization, and drafting rather than decision support.
   - The gap may therefore reflect product design and evaluation targets more than a fundamental memory limitation.

4. `Scenario-memory explanation`
   - For business decisions spanning multiple documents, past events, alternatives, and constraints, current AI tools lack a representation of the situation itself.
   - On this view, fragment retrieval and generic long-term memory are insufficient because they do not reconstruct the decision episode in a reusable way.

## Research gap candidates

1. Direct SME literature says relatively little about how AI systems should represent and reconstruct business scenarios for owner-manager decisions.

2. The current SME AI literature is strong on adoption barriers and weak on the architecture of decision support once adoption begins.

3. Retrieval-oriented AI support appears under-specified for decisions that require:
   - multi-step business logic
   - cross-document synthesis
   - temporal reconstruction
   - rationale tracking
   - comparison of alternative courses of action

4. Adjacent literatures offer pieces of the answer under different names, but there is no clear synthesis yet around `scenario-oriented memory for SME decision support`.

5. A plausible gap candidate is:
   - how to build AI support systems for SMEs that move from fragment retrieval to reconstructable, traceable, scenario-level decision context.

## Open questions

- Which SME decision classes should anchor the problem: financing, hiring, inventory, pricing, compliance, vendor choice, or growth planning?
- Is the target deficiency best described as scenario memory, episodic business memory, workflow memory, case memory, or decision traceability?
- How much of the observed limitation comes from retrieval failure versus weak process modeling versus missing evaluation criteria?
- Are there mature enterprise systems or BPM literatures that already solve part of this problem outside the LLM framing?
- What would count as evidence that scenario reconstruction improves decision quality rather than only user experience?

## TODO: evidence still needed

- TODO: collect stronger peer-reviewed evidence on concrete decision pain points reported by SME owners and managers outside the AI-adoption literature.
- TODO: verify whether there are SME-specific studies on AI copilots, agent systems, or business advisory tools rather than general AI adoption.
- TODO: find stronger business-process or enterprise-memory literature using terms such as `process memory`, `event memory`, or `business context reconstruction`.
- TODO: check whether case-based reasoning has been used in SME advisory, SME finance, or SME operations specifically.
- TODO: verify whether there are existing evaluations that compare document retrieval against richer contextual or episodic memory in business decision tasks.

## Sources used in this pass

- Oldemeyer, L., Jede, A., & Teuteberg, F. (2025). `Investigation of artificial intelligence in SMEs: a systematic review of the state of the art and the main implementation challenges`. Management Review Quarterly, 75, 1185-1227. https://doi.org/10.1007/s11301-024-00405-4
- Schwaeke, J., Peters, A., Kanbach, D. K., Kraus, S., & Jones, P. (2025). `The new normal: The status quo of AI adoption in SMEs`. Journal of Small Business Management, 63(3), 1297-1331. https://doi.org/10.1080/00472778.2024.2379999
- Hansen, E. B., & Bøgh, S. (2021). `Artificial intelligence and internet of things in small and medium-sized enterprises: A survey`. Journal of Manufacturing Systems, 58, 362-372. https://doi.org/10.1016/j.jmsy.2020.08.009
- Adomako, S. (2022). `Uncertainty and decision making in small firms`. Journal of the International Council for Small Business, 3(4). https://doi.org/10.1080/26437015.2022.2098081
- Brereton, T. A., Malik, M. M., Lifson, M., Greenwood, J. D., Peterson, K. J., & Overgaard, S. M. (2023). `The Role of Artificial Intelligence Model Documentation in Translational Science: Scoping Review`. Interactive Journal of Medical Research, 12, e45903. https://doi.org/10.2196/45903
- Joren, H., Zhang, J., Ferng, C.-S., Juan, D.-C., Taly, A., & Rashtchian, C. (2025). `Sufficient Context: A New Lens on Retrieval Augmented Generation Systems`. ICLR 2025 / arXiv:2411.06037. https://doi.org/10.48550/arXiv.2411.06037
- Wang, Z. Z., Mao, J., Fried, D., & Neubig, G. (2024). `Agent Workflow Memory`. arXiv:2409.07429. https://doi.org/10.48550/arXiv.2409.07429
- Fountas, Z., Benfeghoul, M. A., Oomerjee, A., Christopoulou, F., Lampouras, G., Bou-Ammar, H., & Wang, J. (2025). `Human-inspired Episodic Memory for Infinite Context LLMs`. ICLR 2025 / arXiv:2407.09450. https://doi.org/10.48550/arXiv.2407.09450
- Wu, H., Zhang, H., Chen, W., & Xia, J. (2025). `Retrieval Augmented Decision-Making: A Requirements-Driven, Multi-Criteria Framework for Structured Decision Support`. arXiv:2505.18483. https://doi.org/10.48550/arXiv.2505.18483
- Park, G., Küsters, A., Tews, M., Pitsch, C., Schneider, J., & van der Aalst, W. M. P. (2022). `Explainable Predictive Decision Mining for Operational Support`. arXiv:2210.16786
- Bouslama, F., de Cesare, S., Fiaidhi, J., & Masclet, C. (2015). `A framework for decision making on teleexpertise with traceability of the reasoning`. IRBM, 36(1), 40-51. https://doi.org/10.1016/j.irbm.2014.09.002
- Hansen, J. V., Meservy, R. D., & Zwick, D. (1995). `Case-Based Reasoning: Application Techniques for Decision Support`. Proceedings of the Twenty-Eighth Hawaii International Conference on System Sciences.
