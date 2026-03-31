# Literature Review Prompt 01

## Purpose

Run a first-pass reconnaissance review on the overall research direction.

## Prompt

```md
Work like a careful research assistant supporting a senior researcher.
Do not optimize for fluency alone.
Optimize for:
- search quality
- concept disambiguation
- gap identification
- defensible synthesis
- clean Markdown notes
If the literature does not support a strong claim, downgrade the claim rather than stretching it.

Use the installed skills to run a first-pass literature review for this research direction:

Topic:
Decision-making pain points for small business owners in the AI era, and limitations of current AI support systems for SME decision support.

Working hypothesis:
Current AI systems for SMEs are often good at retrieving fragments of information, documents, and long-term memories, but weak at reconstructing decision-grade business context across scenarios.
In high-business-logic vertical domains, LLM agents may need scenario-oriented memory in addition to long-term memory and document memory.

Investigate:
1. Major decision-making pain points for SME owners/managers.
2. Main limitations of current AI systems designed to support SME decision-making.
3. Whether fragment retrieval is not enough for decision support.
4. Related concepts under different names, such as episodic memory, case-based reasoning, workflow memory, event memory, decision traceability, business process memory, or scenario reconstruction.
5. The likely research gap.

Deliverables:
1. `references/notes/sme_ai_decision_review_round1.md`
2. `references/notes/sme_ai_decision_review_matrix.md`
3. Update `docs/todo.md` with only the most useful next actions.
```

## Notes

- Use this before narrowing the research framing.
- This is the broad reconnaissance pass.
