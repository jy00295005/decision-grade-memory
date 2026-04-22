# Citation Audit for `short_paper_conference.md`

## Scope

- Audited [manuscript/sections/short_paper_conference.md](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/manuscript/sections/short_paper_conference.md) paragraph by paragraph.
- Combined two standards:
  - `dgm-citation-audit`: keep only claims that are directly supported, clearly marked as synthesis, or explicitly framed as this paper's own methodological argument.
  - `citation-management`: verify author, title, journal, DOI, and publication-year metadata conservatively before updating [references/library.bib](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/references/library.bib).
- Focused on the short-paper draft, not the older Day 1-4 modular drafts.

## 1. Paragraph-by-Paragraph Audit

### Abstract

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Abstract paragraph 1 | Acceptable as paper framing | This paragraph states the paper's proposed method rather than an external literature claim. No extra citation is required if kept clearly as the paper's own contribution framing. | Kept unchanged |
| Abstract paragraph 2 | Clearly supported | The claims about `6/1/2` pairwise outcomes, mixed regression, and prototype-level boundary are supported by the local experiment artifacts and chapter drafts. | Kept unchanged |

### Introduction

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Paragraph 1, sentence 1 | Originally too strong | `SME decision support rarely fails because...` was rhetorically strong and not directly sourced. | Softened to `A recurring difficulty...` |
| Paragraph 1, citation cluster | Strong enough to keep | `Smith et al. (1988)`, `Salles (2006)`, `Wong et al. (2018)`, and `Cowden et al. (2022)` jointly support uncertainty, weak structure, and owner-centered decision conditions. They do **not** support every possible SME constraint claim, so the wording should stay bounded. | Kept with tightened wording |
| Paragraph 2, AI-for-SME review claim | Strong enough to keep after wording control | `Hansen and Bøgh (2021)`, `Oldemeyer et al.`, and `Schwaeke et al.` support the claim that the review literature is stronger on adoption/readiness and bounded functional use than on decision-grade context reconstruction. This is a comparative literature synthesis, not a direct benchmark finding. | Kept; marked explicitly as `review literature` |
| Paragraphs 3-5 | Acceptable as paper contribution framing | These paragraphs describe the paper's own problem statement and contribution. They do not need external citation unless later expanded into stronger novelty claims. | Kept unchanged |

### Problem Positioning

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Paragraph 1 | Strong enough to keep | `Phillips-Wren et al. (2021)` and `Doumbouya et al. (2015)` are appropriate adjacent anchors for the distinction between data access and structured decision support with traceability. | Kept unchanged |
| Paragraph 2 | Partly supported, partly analytical inference | `Gibson (1992)`, `Salles (2006)`, and `Wong et al. (2018)` support irregular financial information use, hard-to-specify information requirements, and informal owner-centered decision processes. They do not directly prove `relation-rich retrieval contamination`; that remains this paper's analytical inference. | Kept, but changed to `In the setting studied here...` |
| Paragraphs 3-4 | Acceptable as paper argument | These are the paper's own organizational claim and scope boundary. No added citation required. | Kept unchanged |

### Method

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Section 3 throughout | Acceptable without further citation | The section is written as a method proposal, not as a literature review. Most claims define the architecture rather than attribute it to prior work. | Kept unchanged |
| Section 3.3, graph substrate rationale | Acceptable as internal method rationale | This is an explanation of why the graph layer matters in the present design. It does not need extra citation unless converted into a broader empirical claim about all SME memory systems. | Kept unchanged |

### Experimental Setup and Results

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Sections 4-5 throughout | Clearly supported by local evidence | These sections rely on the repository's own evaluation-design and experiments material, not on external literature claims. The main requirement here is internal consistency with the experiment artifacts, which is satisfied. | Kept unchanged |
| Results interpretation paragraphs | Strong enough to keep | Claims are appropriately bounded to the local prototype setting and do not overstate the evidence. | Kept unchanged |

### Discussion and Conclusion

| Location | Status | Audit note | Action |
| --- | --- | --- | --- |
| Discussion paragraph 1 | Supported as internal interpretation | This paragraph interprets the local result against the proposed method claim. It is not presented as a general external-literature finding. | Kept unchanged |
| Discussion paragraph 2-4 | Strong enough to keep | These paragraphs properly state corpus, audit, and generalization limits. They are consistent with the experiment artifacts and are conservatively worded. | Kept unchanged |
| Conclusion | Strong enough to keep | The conclusion remains bounded and does not exceed the supported scope. | Kept unchanged |

## 2. Claims Tightened or Softened

- The opening sentence of the Introduction was softened because the original formulation implied a broad causal generalization without direct support.
- The AI-for-SME literature sentence was tightened to say `the current review literature is stronger on...` rather than implying a universal state of the field.
- The contamination sentence in Problem Positioning was tightened so that the contamination risk is clearly presented as an inference in the present setting, not as a directly established property of all graph retrieval systems.

## 3. Sources Strong Enough to Keep

- `Smith et al. (1988)`: strong historical anchor for differences in decision behavior between smaller entrepreneurial and larger professionally managed firms.
- `Salles (2006)`: strong direct support for weakly structured SME decision situations and hard-to-specify information requirements.
- `Wong et al. (2018)`: strong support for owner-centered, case-shaped SME financial decision processes.
- `Cowden et al. (2022)`: strong support for uncertainty as a salient feature of small-firm decision making.
- `Gibson (1992)`: useful, older support for irregular financial-information use in small firms.
- `Hansen and Bøgh (2021)`: useful survey support for bounded AI/IoT application framing in SMEs.
- `Oldemeyer et al. (2025)`: strong systematic-review source for AI implementation and adoption barriers in SMEs.
- `Schwaeke et al. (2025)`: strong review source for AI adoption status in SMEs.
- `Phillips-Wren et al. (2021)`: strong conceptual DSS anchor for the distinction between data access and deeper decision support.
- `Doumbouya et al. (2015)`: acceptable adjacent source for reasoning traceability, as long as it remains clearly labeled non-SME-direct.

## 4. Sources or Moves That Still Need Caution

- `Gibson (1992)` is useful but old. It should support only bounded claims about irregular financial-information use, not modern digital-system generalizations.
- `Hansen and Bøgh (2021)`, `Oldemeyer et al. (2025)`, and `Schwaeke et al. (2025)` support adoption/readiness/application framing more strongly than they support claims about decision-grade context reconstruction. The manuscript now reflects that distinction.
- No external source in the current short paper directly proves `DecisionEpisode` as a category. That is acceptable because the manuscript presents it as the paper's own organizational proposal, not as an established term in the literature.

## 5. Bibliography Changes Made

Updated [references/library.bib](/Users/chen/Documents/学术/AIResearch/bridging growth-garap based ai for sme/references/library.bib) conservatively:

- `OldemeyerEtAl2024`: year updated from `2024` to `2025`
- `SchwaekeEtAl2024`: year updated from `2024` to `2025`

Reason:

- publisher-facing citation records now point to final issue publication in `2025`, even though DOI/online-first metadata can surface `2024` in some contexts.

Also normalized the short-paper reference list and in-text citations to the same year convention.

## 6. Uncertain Areas Intentionally Left Unresolved

- This audit did not add new adjacent citations for episodic memory, workflow memory, or case-based reasoning because the current short paper does not rely on them for any indispensable claim.
- This audit did not expand the bibliography beyond already verified and repository-tracked sources.
- Some older repository notes still contain outdated author-year shorthand for `Oldemeyer`, `Schwaeke`, and other sources. Those note-level inconsistencies were not globally rewritten here because this pass targeted the short-paper draft and the main bibliography.

## 7. Bottom Line

- The short-paper draft is now materially tighter at the citation level than before.
- The highest-risk unsupported formulations were softened rather than force-cited.
- The remaining external citations are now doing narrower, better-matched work.
- The manuscript is not fully citation-maximal, but it is substantially more citation-defensible and reviewer-safe.
