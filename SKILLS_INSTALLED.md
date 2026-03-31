# Skills Installed

Project-local Codex skills installed in `.codex/skills/`.

## Installed skills

- `literature-review`: structured workflow for systematic literature review and research synthesis.
- `bgpt-paper-search`: paper discovery via a remote BGPT MCP server with structured full-text-derived fields.
- `citation-management`: citation lookup, metadata extraction, and BibTeX-oriented reference handling.
- `markitdown`: document and file conversion into Markdown-friendly text.
- `markdown-mermaid-writing`: Markdown-first writing patterns plus Mermaid diagram drafting.
- `hypothesis-generation`: structured hypothesis framing, competing explanations, and testable prediction design.
- `exploratory-data-analysis`: broad exploratory analysis guidance for scientific and general data files.
- `networkx`: graph construction, analysis, and visualization support for relationship data.

## Dependency notes

- No Python packages, npm packages, or system tools were installed as part of this setup.
- `bgpt-paper-search` requires external MCP configuration using `npx` and the BGPT remote server before it becomes usable in the app.
- `literature-review` documents optional use of `requests`, `pandoc`, and a LaTeX toolchain for PDF generation.
- `citation-management` documents optional use of `requests`, `bibtexparser`, `biopython`, and optionally `scholarly` or `selenium`.
- `markitdown` documents optional package installs depending on the file types you want to convert.
- `hypothesis-generation` documents a LaTeX-based output workflow that expects XeLaTeX or LuaLaTeX.
- `networkx` expects the `networkx` Python package when you want to run graph code.
- `exploratory-data-analysis` may require additional libraries depending on the file formats analyzed.

## Caveats

- This setup is intentionally minimal and reversible: only skill folders were copied into the project.
- `bgpt-paper-search` is the main non-local dependency in the set; a safer local substitute from the same repository would be `paper-lookup` if you want to avoid remote MCP setup.
- `hypothesis-generation` is useful for reasoning, but its documented output path is less aligned with this repository's Markdown-first workflow; a cleaner substitute would be `scientific-brainstorming` if needed later.
- Several skills mention diagram or PDF workflows, but those optional paths were not configured or enabled here.
