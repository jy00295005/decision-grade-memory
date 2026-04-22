# Research Log

## 2026-04-22

### Done

- Reworked the experiments material into a dedicated manuscript workspace under `manuscript/05_experiments/`.
- Drafted three paper-facing experiment files:
  - experiment design
  - experimental data / validation KG
  - validation method and results
- Added two figure assets for the experiments chapter:
  - a local validation KG fragment
  - a `combined_rrf` versus `DecisionEpisode + strict projection` comparison figure
- Merged the three experiment drafts into a full chapter draft at `manuscript/sections/05_experiments.md`.
- Generated export-ready Markdown and HTML variants and produced a single-chapter PDF at `output/pdfs/05_experiments.pdf`.

### Key insight

- The experiments chapter is now materially stronger than the earlier evaluation-design stage because it is aligned with the actual targeted re-test rather than with the pre-experiment pilot framing alone.
- The strongest current empirical signal is no longer broad scenario-oriented retrieval versus fragment retrieval. It is targeted superiority of `DecisionEpisode + strict projection` on contamination-prone local stress cases.
- The experiments material can now support chapter drafting at three levels:
  - experimental design
  - validation data / graph substrate
  - validation method plus bounded results

### Open questions

- Should the full regression table remain in the main chapter or move to an appendix-style note, given that it does not show universal `DecisionEpisode` superiority?
- Does the experiments chapter need one more compression pass before it is merged into a full manuscript export?
- Should the next visual addition be a cleaner appendix-ready local KG screenshot or a table-based case summary for the stress-test set?

### Next step

- Decide how `manuscript/05_experiments/01-03` should be compressed into the final chapter narrative.
- Keep the strongest claim narrow: targeted stress-test superiority rather than universal superiority.
- Use the new chapter PDF as the current shareable experiments artifact while keeping the modular experiment drafts editable.

## 2026-04-11

### Done

- Read the current Method and evaluation-design chapters alongside the ProsperPath feasibility note and pilot outputs.
- Checked the current graph-backed pilot artifacts against the paper's Day 4 goal: data analysis and experimental validation.

### Key insight

- The current ProsperPath assets are sufficient for a narrow feasibility pilot, but not yet for a strong empirical chapter.
- The strongest readable signal is a comparison of fragment-oriented retrieval versus scenario-oriented context assembly on a small number of inspectable decision situations.
- The main limitation is that scenario-oriented retrieval is still only a proxy for a true episode-level layer, and the graph remains noisy, synthetic or semi-simulated, and uneven in outcome/evidence coverage.

### Open questions

- Which existing cases can support a defensible 15-30 item comparison set without forcing weak or unrelated retrieval?
- What exact inclusion and exclusion rules should govern the next dataset slice?
- Can the current scoring rubric be tightened enough to reduce reviewer overlap before a second reviewer is added?
- What graph or retrieval changes would be required before the method can be described as more than a proxy implementation?

### Next step

- Build a narrow case-selection and scoring protocol for the next experiment round.
- Separate immediate feasibility analysis from any claims of empirical validation.
- Keep the next paper move focused on data coverage, retrieval quality, and rubric stability rather than product benchmarking.

## 2026-04-01

### Done

- Structured the repository as a Markdown-first academic writing workspace.
- Installed a project-local Codex skill set for literature review, citation work, writing, and graph support.
- Completed four rounds of literature review and one research-positioning synthesis pass.
- Drafted and exported the first review-analysis PDF.
- Designed, compressed, and exported a full Section 3 / Method chapter as a paper-ready PDF.
- Distilled the main Method workflow into a reusable prompt pack and added reusable figure prompts.

### Key insight

- Fragment retrieval appears useful but insufficient for decision-grade support when SME decisions depend on constraints, chronology, and evidence traceability.
- The method contribution becomes much clearer when it is framed as explicit episode organization over graph-based business memory rather than as a larger system narrative.

### Open questions

- Is `scenario-oriented memory` a genuinely useful framing, or mainly a relabeling of adjacent concepts such as episodic memory, workflow memory, case-based reasoning, or decision traceability?
- Which SME decision classes most clearly depend on episode-level context rather than document-level retrieval?
- Where does the main bottleneck sit: retrieval quality, missing process structure, weak traceability, or lack of direct SME-specific evaluations?
- How much direct citation support should remain in Section 3 itself versus being carried by Section 2 and the review article?

### Next step

- Tighten the transition from related work to the compressed Method chapter.
- Draft the data and graph design section so it directly follows the scenario-memory method claim.
- Decide which method claims need explicit in-section citation anchors for reviewer trust.
