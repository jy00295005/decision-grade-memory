# Draft Reviewer Response

## Paper

**Title:** *Scenario Memory for LLM-Based SME Decision Support: DecisionEpisode as the Core Unit of Bounded Context Construction*

## Overall response

We thank the reviewer for the careful and constructive reading of the paper. We appreciate the positive assessment of the paper's problem framing, conceptual contribution, stress-test design, and the paper's restrained treatment of its current evidential scope. The comments were especially helpful in identifying where the manuscript needed to be more explicit about the mechanics of strict projection, the interpretation of the scoring rubric, and the risks associated with over-bounded episode construction.

In response, we revised the manuscript in four main ways. First, we clarified the relationship between `scenario memory` and `DecisionEpisode`, making explicit that `scenario memory` is the framework-level proposal and `DecisionEpisode` its core operational unit. Second, we expanded the description of `strict projection` into a more explicit rule-based procedure and made its explainability role more explicit by framing it as a provenance-preserving filtering step rather than a black-box classifier. Third, we strengthened the evaluation section by clarifying the comparison conditions and by making the scoring rubric more interpretable through explicit score anchors. Fourth, we expanded the discussion of limitations to address over-filtering, false-negative risks, and the method's dependency on a minimally structured graph substrate, and we now describe a layered-context expansion mechanism as a future robustness direction.

Below we respond point by point.

---

## Response to strengths summary

We thank the reviewer for recognizing what we hoped would be the central contribution of the short paper: not a broad claim of production-ready SME AI, but a narrow argument that LLM-based decision support needs a more bounded organizational layer than fragment retrieval alone. We are particularly encouraged that the reviewer found the pressure-test logic and the paper's restrained claim discipline appropriate for the short-paper format.

---

## Response to major weaknesses and suggested improvements

### A. Evaluation scale and subjectivity

**Reviewer comment:** The stress-test is small (`9` cases), and the scoring uses a non-blinded human `1-5` rating scheme. The reviewer suggests adding inter-rater reliability and, if possible, automated LLM-based scoring.

**Response:** We agree that this is a real limitation and we have made the paper more explicit about it. In the revised manuscript, the scoring subsection now clarifies that the current study should be read as a disciplined prototype comparison under inspectable local conditions rather than as a benchmark-grade evaluation. We also added clearer `1/3/5` score anchors so that the rubric is more transparent about what constitutes fragmentary, partially usable, and well-bounded context packages.

At the same time, we did not add inter-rater reliability statistics or LLM-as-judge comparisons in the current revision because those analyses are not yet available in a form we would consider methodologically stable enough to report. Rather than imply a stronger validation regime than we currently have, we chose to state the limitation more directly: the scoring is non-blinded, the dataset is small, and the current evidence remains prototype-level. We believe this is the most defensible treatment within the scope of the present short paper.

### B. Implementation details of strict projection

**Reviewer comment:** The paper presents `strict projection` as central to the gains over `combined_rrf`, but its implementation logic was not concrete enough.

**Response:** We agree, and this was one of the most useful comments. We revised the method section to make `strict projection` more explicit as a rule-based filtering step. The revised text now explains that the projection:

1. starts from the candidate evidence bundle attached to the focal decision situation rather than from the entire retrieved neighborhood,
2. retains only material linked to at least one focal episode slot,
3. preserves paths that maintain challenge-action-goal-outcome consistency, and
4. discards nodes that are semantically related but not episode-aligned, such as adjacent actions, peripheral benefits, or traces attached to a different goal path.

We also made explicit that, in the current prototype, this step is primarily graph- and rule-driven rather than delegated to a separate learned classifier. Our goal in this revision was not to overstate the sophistication of the current implementation, but to make the operational logic inspectable enough for the reader to understand why the episode condition differs from a richer retrieval baseline.

In the revised manuscript, we also made a second point more explicit: this rule-based design improves explainability. Because inclusion and exclusion decisions are made through explicit slot-linking and graph-visible path constraints, the system provides a natural provenance chain for human review. A reader can inspect why a specific constraint or action trace was retained and why a nearby distractor was filtered out. We believe this is especially important for SME-oriented decision support, where the practical value of a bounded context package depends not only on its compactness but also on whether its evidence chain remains auditable.

### C. Extraction robustness and constraint recovery

**Reviewer comment:** The paper acknowledges weaker recovery of constraints and uncertainties, and the reviewer rightly notes that this can be especially serious in SME settings.

**Response:** We strongly agree. In the revised discussion, we now state more directly that the risk is not only contamination from overly broad retrieval. There is also a complementary false-negative risk: if a latent cash, staffing, or supply constraint is not recovered into the episode, `strict projection` can produce a cleaner but misleading decision package by excluding a constraint that should still shape the recommendation. We felt this point should be stated plainly because, in SME settings, a single omitted operational constraint can materially alter the action path.

We also expanded the discussion of method assumptions by clarifying that the current framework depends on a minimally structured graph substrate that can distinguish, at least imperfectly, between challenge, action, goal, outcome, and evidence relations. In addition, we now describe a layered-context fallback as the most plausible future mechanism for mitigating this risk. Under that design, the initial `DecisionEpisode` remains the primary bounded context, but the system can request a controlled expansion into adjacent episodes or peripheral context when the current episode appears insufficient for decision support. This is intended as a future robustness direction rather than as a capability already validated by the present prototype.

---

## Response to questions for authors

### 1. On cases where `combined_rrf` performs slightly better

**Reviewer question:** In the cleaner cases where `combined_rrf` performs slightly better, is the likely reason over-filtering?

**Response:** Yes, we think that is a plausible interpretation for at least part of the mixed broader regression. We revised the results section to say this more directly. On lower-ambiguity cases, the benefit of strict episode enforcement can shrink because the baseline is already operating with relatively little contamination. In such settings, a broader relation-rich package may remain sufficient and may sometimes preserve weakly useful peripheral context that a stricter episode boundary removes. We do not treat this as a contradiction to the main claim; rather, it helps define the intended operating region of the method more clearly.

### 2. On automation versus manual assistance in episode construction

**Reviewer question:** Is the mapping from the knowledge graph to `DecisionEpisode` automatic, or does it require manual slot annotation?

**Response:** The current paper evaluates an inspectable prototype pipeline over curated local decision situations rather than a fully validated large-scale automatic extraction system. In the revised manuscript, we emphasize that the evaluation unit is the bounded decision situation, not a benchmark of fully stabilized, automatically extracted episode objects. The current implementation is therefore better understood as prototype episode construction over graph-backed cases than as evidence of robust autonomous slot extraction at scale.

### 3. On dependency on the underlying graph schema

**Reviewer question:** How dependent is the framework on the graph substrate and its schema? What happens when SME records are much more weakly structured?

**Response:** We now address this more explicitly in the discussion. The present method assumes a minimally structured graph substrate capable of preserving challenge, action, goal, outcome, and evidence distinctions. If the source environment does not support those distinctions, or only supports them very weakly and inconsistently, then both episode construction and strict projection are expected to degrade. We view this as an important scope condition of the current paper rather than as a hidden limitation.

---

## Closing statement

We thank the reviewer again for the constructive assessment. The review helped us sharpen the paper in the direction we think best suits a conference short paper: not by expanding the empirical claim, but by making the method more inspectable, the evaluation rubric more interpretable, and the limitations more explicit. We believe the revised manuscript now presents a clearer and more defensible argument for `scenario memory` and `DecisionEpisode` as bounded context-construction mechanisms for LLM-based SME decision support.
