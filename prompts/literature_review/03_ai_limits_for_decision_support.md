# Literature Review Prompt 03

## Purpose

Investigate the limitations of current AI systems for SME decision support.

## Prompt

```md
Now investigate the limitations of current AI systems for SME decision support.

Working angle:
Many AI systems can retrieve information, summarize documents, answer questions, or store long-term memory, but may still fail to reconstruct a full decision scenario:
- what the user’s goal was
- what constraints existed
- what challenge emerged
- what action was taken
- what outcome followed
- what evidence supports the conclusion

Tasks:
1. Review literature on AI support for SME decision-making, business copilots, enterprise assistants, agent memory, decision support systems, and business process intelligence.
2. Identify what kinds of memory/context support current systems usually provide.
3. Identify what is still missing for decision-grade business reasoning.
4. Compare at least these context types if literature allows:
   - document memory
   - long-term user memory
   - conversational memory
   - workflow/process memory
   - episodic/scenario memory
5. Create:
   `references/notes/ai_limits_for_sme_decision_support.md`

Use this structure:
- What current systems do well
- What they do not reconstruct well
- Evidence for fragment-retrieval limitation
- Related concepts from adjacent literature
- Candidate gap statement
- Risks of overstating the gap
- TODO: terms to validate further

Requirements:
- Be skeptical and precise.
- Do not force the conclusion.
- If “scenario memory” is not a standard term, identify the closest established terms used in the literature.
- Mark speculative synthesis clearly as Working Hypothesis.
```

## Notes

- Use after clarifying SME decision pain points.
- This prompt isolates the system/architecture side of the paper.
