# Citation Audit for `sme_decision_support_review.md`

## Scope

- Audited [manuscript/reviews/sme_decision_support_review.md](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/manuscript/reviews/sme_decision_support_review.md) against the current note set under `references/notes/`.
- Standard used here: keep claims only when they are directly supported by the current source base, clearly presented as synthesis, or explicitly marked as `Working Hypothesis`.
- Bibliography update rule: add only verified entries with stable bibliographic metadata to [references/library.bib](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/references/library.bib).

## 1. Claims That Need Citations

| Location in review | Claim or move | Audit note | Suggested action |
| --- | --- | --- | --- |
| Introduction, lines 5-6 | SMEs operate with less managerial specialization, less analytical slack, lower financial buffers, and more concentrated authority | Plausible synthesis, but currently bundled into one uncited opening claim | Split or cite with a cluster such as Smith et al. (1988), Nicolas (2021), Salles (2006), and Wong et al. (2018) |
| Review Scope, lines 13-15 | The source base is asymmetric, with stronger business-problem evidence than architecture evidence | Accurate as a review-level characterization, but still a claim about the literature set | Cite the relevant note clusters or mark explicitly as `review-scope synthesis` |
| Section 3, line 30 | SMEs have less capacity to convert imperfect information into defensible decisions under pressure | Strong synthesis, but not directly cited | Support with Salles (2006), Gibson (1992), Wong et al. (2018), and Nicolas (2021) |
| Section 3, line 61 | SME decision support is inherently a context problem | This is the article's own analytical inference, not a direct finding | Keep, but label as synthesis and cite the main pain-point sources |
| Section 4, lines 67-75 | Current systems are strongest at retrieval, summarization, bounded QA, prediction, conversational continuity, and workflow support | Too broad to stand uncited, especially because it blends SME-specific and adjacent AI evidence | Add source clusters by support type or narrow the wording to `in the current notes` |
| Section 4, lines 76-77 | The literature does not strongly demonstrate full decision-episode reconstruction in SME-specific settings | Negative evidence claim; should be anchored more carefully | Phrase as `the current review set does not provide strong SME-specific evidence` and cite Oldemeyer et al. (2024), Schwaeke et al. (2024), Hansen and Bøgh (2021) |
| Section 4, line 89 | Accurate summaries may still be insufficient for decisions involving timing, trade-offs, and evidentiary uncertainty | Supported conceptually, but not directly as an SME-tested finding | Cite adjacent RAG and DSS work, or mark as `analytical implication` |
| Section 6, lines 112-123 | Related concepts are distributed across literatures rather than gathered under a stable term | Reasonable, but still a literature claim | Cite the actual anchor literatures if retained |
| Section 8, lines 165-171 | There is a mismatch between SME decision demands and current AI maturity; publication lag and organizational readiness are competing explanations | First half is defensible synthesis; second half is interpretive and partly speculative | Keep, but distinguish clearly between evidence-backed synthesis and competing explanations |
| Conclusion, lines 182-184 | Three-part conclusion about SME difficulty, current AI limits, and scenario-oriented framing | Directionally consistent with the article, but the conclusion inherits the citation gaps above | Safe once earlier sections are properly cited and attribution errors are corrected |

## 2. Unsupported or Weakly Supported Claims

| Location in review | Issue | Current support strength | Conservative handling |
| --- | --- | --- | --- |
| Introduction, lines 5-6 | The full bundle of SME constraints is stated as if equally established | Mixed; financial pressure and owner-centrality are stronger than `managerial specialization` and `analytical slack` | Unbundle and weaken the softer items |
| Table 2, line 46 | Staffing constraints are treated as a direct decision-quality problem | Moderate only; the current notes already flag this as an evidence gap | Keep as `moderate` and preserve `TODO:` follow-up |
| Table 2, lines 45 and 47 | Fragmented or weakly integrated systems are implied to be a primary decision pain point | Moderate at best; stronger as an adoption/data-readiness issue than as a direct decision-study finding | Downgrade to `data and integration difficulty appear recurrent` unless stronger direct evidence is added |
| Table 3, line 57 | SMEs are said to have more fragmented or manually maintained information infrastructure | Plausible, but mostly supported by review literature, not by direct comparative decision studies | Keep as a comparative interpretation, not a settled empirical generalization |
| Section 4, lines 67-75 | The overview of current AI support types implies a stable typology | Mixed; retrieval, summarization, and bounded QA are well supported, but `workflow-like procedural support` and `long-term user memory` rely more on adjacent or engineering-oriented literature | Cite selectively and avoid implying a mature unified taxonomy |
| Section 5, lines 95-108 | Fragment retrieval is not enough for decision support | Strong as adjacent synthesis; weak as a direct SME-specific finding | Keep, but state explicitly that this is inferred from adjacent decision-support and RAG literature |
| Section 8, line 171 | Publication lag may explain the apparent gap | Speculative | Keep only as a competing explanation, not as an evidence-backed observation |

## 3. Citation Attribution Corrections Needed

These should be treated as high-priority cleanup items before reusing the article in a more formal manuscript.

| Current shorthand in notes/review | Verified citation form | Audit note |
| --- | --- | --- |
| `Adomako (2022)` | `Cowden et al. (2022)` | DOI metadata shows Adomako is a coauthor, not sole author |
| `Cieślik et al. (2021)` | `Nicolas (2021)` | The DOI used in the notes resolves to a single-author paper by Théo Nicolas; the current shorthand is inconsistent with the verified metadata |
| `Mitchell (1988)` | `Smith et al. (1988)` | The cited paper is multi-author; Mitchell is not the lead author |
| `Phillips-Wren and Dalla Bona (2021)` | `Phillips-Wren, Daly, and Burstein (2021)` | Current note-level attribution is incorrect |
| `Bouslama et al. (2015)` | `Doumbouya et al. (2015)` | The DOI in the notes resolves to Doumbouya and coauthors, not Bouslama and coauthors |
| `Oldemeyer et al. (2025)` | `Oldemeyer et al. (2024)` | Verified DOI metadata currently points to 2024 |
| `Schwaeke et al. (2025)` | `Schwaeke et al. (2024)` | Verified DOI metadata currently points to 2024 |

## 4. Sources Strong Enough to Keep

| Source | Role in the review | Strength | Keep? |
| --- | --- | --- | --- |
| Cowden et al. (2022) | SME uncertainty and decision difficulty | Strong, direct SME problem-framing source | Yes |
| Nicolas (2021) | Working-capital constraints and investment trade-offs | Strong, direct SME finance constraint source | Yes |
| Salles (2006) | Weakly structured decisions and information requirements | Strong and highly relevant to decision-support framing | Yes |
| Smith et al. (1988) | Smaller vs larger firm decision behavior | Strong historical comparative anchor | Yes |
| Wong et al. (2018) | Owner-centered and case-shaped SME financial decisions | Strong for owner-manager centrality and informal decision logic | Yes |
| Gibson (1992) | Irregular financial information use in small firms | Useful supporting source, though older | Yes |
| Oldemeyer et al. (2024) | AI in SMEs systematic review and implementation barriers | Strong for AI adoption and implementation context | Yes |
| Schwaeke et al. (2024) | AI adoption status in SMEs | Strong for adoption/readiness context | Yes |
| Hansen and Bøgh (2021) | AI/IoT survey in SMEs | Strong for bounded operational AI support context | Yes |
| Phillips-Wren et al. (2021) | What counts as decision support beyond data access | Strong conceptual anchor for DSS framing | Yes |
| Doumbouya et al. (2015) | Traceability analogue from adjacent domain | Useful adjacent support, not SME-direct | Yes, but keep clearly labeled as adjacent |
| Brereton et al. (2023) | Documentation and traceability in decision-support-like settings | Useful analogue, not SME-direct | Yes, with domain-boundary caution |
| Molina-Abril et al. (2025) | Strategic decision-making review in SMEs | Useful supporting review, but not the primary anchor | Yes |
| Kgakatsi et al. (2024) | Data and capability barriers around big data in SMEs | Useful supporting review, but secondary to direct decision studies | Yes |

## 5. Where More Formal References Are Needed

- Direct SME studies on business copilots, enterprise assistants, or AI advisory systems evaluated on real decision tasks.
- Formal comparisons between plain retrieval and richer contextual reconstruction in business decision environments.
- Stronger literature connecting fragmented systems and staffing shortages to decision quality, not only to adoption difficulty or execution limits.
- More explicit sources on workflow memory, decision mining, and process intelligence that connect operational traces to managerial decision support.
- Better-grounded references for terms such as `document memory`, `long-term user memory`, and `conversational memory`, which currently risk reading as engineering shorthand.
- Modern business or SME uses of case-based reasoning, if the article wants to present it as more than a historical analogue.

## 6. Conservative Bibliography Update

Updated [references/library.bib](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/references/library.bib) with verified formal entries only.

Added:

- Brereton et al. (2023)
- Cowden et al. (2022)
- Doumbouya et al. (2015)
- Gibson (1992)
- Hansen and Bøgh (2021)
- Jia et al. (2025)
- Kgakatsi et al. (2024)
- Molina-Abril et al. (2025)
- Nicolas (2021)
- Oldemeyer et al. (2024)
- Phillips-Wren et al. (2021)
- Salles (2006)
- Schwaeke et al. (2024)
- Smith et al. (1988)
- Wong et al. (2018)

Intentionally not added at this stage:

- `Sufficient Context` and `Retrieval Augmented Decision-Making`, because the current note set cites them through arXiv-style records rather than a clearly stabilized final bibliographic form.
- `Agent Workflow Memory` and `Human-inspired Episodic Memory for Infinite Context LLMs`, for the same reason.
- `Explainable predictive process monitoring`, because the notes already mark the citation details as needing verification.

## 7. Bottom Line

- The review article is directionally sound, but it still needs citation cleanup before it should be treated as a stable review essay.
- The highest-risk issue is not only missing citations, but incorrect author-year shorthand that could propagate into later drafts.
- The safest next step is to normalize the article's in-text citations to the verified entries now in [references/library.bib](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/references/library.bib), then downgrade or mark the weaker claims identified above.
