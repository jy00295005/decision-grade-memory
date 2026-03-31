# AGENTS.md

## Repo mission

Maintain a minimal, professional repository for drafting an academic paper on graph-based AI for SME decision-making. The repository should support section-by-section writing, literature synthesis, and careful claim development without premature tooling or fabricated content.

## Current phase

Early-stage literature review, outline refinement, research question definition, and section skeleton drafting.

## What "done" means for edits in this repo

- The edit moves the paper or repository structure forward in a concrete way.
- The change is traceable, local, and consistent with the current outline.
- Any unsupported statement is marked with `TODO:` rather than presented as established fact.
- Relevant follow-up work is added to `docs/todo.md` when appropriate.

## Writing rules

- Maintain academic tone.
- Keep prose precise, restrained, and non-marketing.
- Distinguish clearly between placeholders, hypotheses, and evidence-backed statements.
- Keep terminology consistent across files.
- Prefer concise paragraphs over inflated exposition.
- Use explicit scope language when a claim is provisional or bounded.

## Editing rules

- Make the smallest useful change that moves the draft forward.
- Prefer editing files under `manuscript/sections/` rather than writing everything into `manuscript/main.md`.
- Preserve filenames and directory structure unless explicitly instructed otherwise.
- Before major writing edits, read `README.md`, `docs/outline.md`, `docs/rq.md`, and relevant section files.
- When finishing a meaningful update, append a short actionable item to `docs/todo.md` if appropriate.
- Do not introduce tooling, scripts, automation, or workflow complexity unless explicitly requested.

## Citation rules

- Never invent citations.
- Never use placeholder citations such as `[1]` or `[2]`.
- Add source notes only when a real paper, report, or document exists.
- Keep bibliographic work in `references/library.bib` and paper-specific notes in `references/notes/`.

## Claim-evidence discipline

- Never fabricate empirical claims.
- Never imply validation, performance, or novelty without evidence.
- If a section lacks evidence, insert `TODO:` markers.
- Separate working hypotheses from evidence-backed claims in plain language.
- If a sentence depends on a missing source, either remove it or mark the gap explicitly.

## File discipline

- `manuscript/main.md` is the paper entry file, not the full drafting surface.
- Draft prose belongs in `manuscript/sections/`.
- Planning and framing belong in `docs/`.
- References belong in `references/`.
- Future empirical artifacts belong in `data/`, `experiments/`, and `results/` only when real materials exist.

## Preferred workflow

1. Read `README.md`, `docs/outline.md`, and `docs/rq.md`.
2. Inspect the target section file in `manuscript/sections/`.
3. Make a focused edit to one section or one planning document.
4. Mark unsupported content with `TODO:`.
5. Update `docs/todo.md` if the edit creates an obvious next action.

## What not to do

- Do not rewrite the whole paper in one pass.
- Do not collapse section files into a single manuscript draft.
- Do not add fake experiments, results, figures, tables, or datasets.
- Do not introduce claims of effectiveness, impact, or novelty without support.
- Do not rename core files or folders unless explicitly instructed.
- Do not turn placeholders into polished assertions before the evidence base exists.

## Working terminology

These terms are working placeholders and may be refined later.

- `SME`: small and medium-sized enterprises in the project context.
- `data`: structured or semi-structured information relevant to SME operations or environments.
- `signals`: interpretable indicators derived from data that may inform decisions.
- `growth`: business development outcomes, opportunities, constraints, or trajectories under study.
- `graph-based AI`: methods that represent entities and relations in graph form for reasoning or analysis.
- `decision-making`: the processes through which SMEs evaluate options and choose actions.
