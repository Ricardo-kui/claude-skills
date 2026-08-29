---
name: literature-notes-obsidian
description: "Read a paper (PDF/DOI/URL/title/abstract) into an Obsidian evidence-card note (天堂模版, with AMJ Canvas judgment slots); resolves Zotero metadata and logs into the vault."
when_to_use: "读文献做笔记、升级已有笔记、或对比 2-5 篇论文并落库 Obsidian 时使用。"
whenToUse: Use when reading a paper PDF, DOI, URL, or abstract into an Obsidian literature note, upgrading an existing note, or comparing a small paper set. Trigger words: 做文献笔记, 读论文, 阅读笔记, literature note, 笔记这篇, 写笔记, evidence card, 天堂模版
---

# Literature Notes for Obsidian

Use this skill to turn papers into reusable Obsidian notes. The note should help the user decide what the paper says, why it matters, where it is weak, and how it can be reused in the user's own project.

**Default note format is the vault evidence card (天堂模版).** `literature/` formal notes use Quick View + §0–§9 and `template: evidence-card`. AMJ Canvas (Dorobantu et al. 2024) is folded into §1–§6 as judgment slots (puzzle, conversation, WHAT/HOW/WHY, earned contribution). Do not write a second AMJ seven-module note. There is no simplified literature template.

This skill still supports two *reading* modes. They change what you judge, not the note skeleton:

- `researcher` mode (default): AMJ-style judgment inside the evidence card, plus project reuse
- `writer` mode: structure, narrative moves, paragraph logic, transferable writing patterns — write a separate writer note; do not replace the evidence card

## Scope

- Use for one paper, a small batch, an existing rough note, or a request such as "read this paper into my Obsidian vault."
- Use for `upgrade-note`, `compare-papers`, and `abstract-only` as well as fresh note creation.
- Use for writing deconstruction when the user wants to learn how a paper is written.
- Do not use for ongoing paper recommendation, discovery loops, or long-term reading-feed maintenance; use `articlefeed` for that.

## Default Paths and Runtime State

Read `config.json` for machine-specific defaults. Current defaults are:

- `vault_root`: `D:\Onedrive\Obsidian Vault`
- `default_notes_dir`: `literature`
- `evidence_card_template`: `D:\Onedrive\Obsidian Vault\00 工作台\evidence-card-template.md`
- `zotero_db`: `D:\同步文件\文献库\zotero.sqlite`
- `zotero_storage`: `D:\同步文件\文献库\storage`
- `memory_log`: `memory/notes_log.md`

Keep `config.json` and the scripts in sync. Do not hardcode stale machine-specific paths into new updates.

If `config.json` and the vault template disagree on note structure, **the vault file wins**.

## Source Authority

Use the strongest available full text for substantive reading and verification, in this order:

1. User-provided or vault full-text Markdown (including `文献笔记库/01 导入/论文导入/`, `00 工作台/项目/`, and `Clippings/`)
2. A local PDF only when no authoritative full-text Markdown exists, or when a page-image/layout check is specifically necessary
3. Abstract, DOI, URL, title, or other partial metadata

Treat a supplied complete Markdown file as the paper's authoritative reading source. Read it directly; do not reopen a Zotero PDF merely to read or verify the paper. Zotero is a metadata service: use it only to resolve citation key, DOI, bibliographic fields, and optional attachment links. Record the actual full-text Markdown path and the verification method in frontmatter `verified` and in §9.

## Router

Resolve the task in this order:

1. `read-one`
2. `upgrade-note`
3. `compare-papers`
4. `abstract-only`

Then apply mode and overlays:

- `researcher mode` overlay (AMJ questions already mapped onto the card)
- `writer mode` overlay
- `writing-deconstruction overlay`
- `skill-harvest overlay`

### `read-one`

Trigger when the user gives one paper and wants an Obsidian note.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)
- [amj-canvas-questions.md](references/amj-canvas-questions.md)
- the vault file `00 工作台/evidence-card-template.md`

Write a complete evidence card into `literature/`. Fill AMJ slots inside §1–§6. Do not leave required sections blank; if a section cannot be filled, write `N/A（<原因>）`.

### `upgrade-note`

Trigger when the user already has a rough note, highlights, or extracted/full-text Markdown and wants a better literature note. A complete Markdown is a full-text source, not an inferior proxy.

Load the same files as `read-one`.

Keep bibliographic identifiers (`citekey`, Zotero keys, wiki links) when they are correct. Convert old AMJ-canvas / 「概述 / 1. 引言」notes onto the evidence-card skeleton: map Puzzle/Audience/RQ/WHAT-HOW-WHY/Design/Findings/Contribution into §1–§6, then fill §0, §3c, §8, §9. Update `template: evidence-card` and `verified`.

### `compare-papers`

Trigger when the user wants one synthesis note comparing 2-5 papers on the same puzzle, method, mechanism, or concept.

Each *paper* note in `literature/` remains an evidence card. The synthesis note links those cards; it is not a second literature-note template.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)

### `abstract-only`

Trigger when only an abstract, title, citation, DOI, or partial metadata is available.

Still use the evidence-card skeleton. Set `status: triage`, `reading_stage: browsed` or `to-read`, `evidence_grade: low`, `confidence: seed`. Mark Quick View and §9 as abstract-based. Do not pretend to have read the full paper. Unfilled empirical slots get `N/A（仅摘要）`.

### `researcher mode`

This is the default. It does **not** change the note format.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)
- [note-style-guide.md](references/note-style-guide.md)
- [amj-canvas-questions.md](references/amj-canvas-questions.md)

Use this mode when the user wants to evaluate design credibility, contribution, causal leverage, or reuse value. AMJ questions are the judgment layer; the evidence card is the only note body.

### `writer mode`

Trigger when the user asks how the paper is written, asks for a writing exemplar analysis, asks for "写作模式" / "as a writer", or mainly wants structural craft rather than a literature evidence card.

Load:

- [reading-framework.md](references/reading-framework.md)
- [nelson-reading-guide.md](references/nelson-reading-guide.md)
- [note-style-guide.md](references/note-style-guide.md)
- `assets/note_template_writer.md`

Writer output is a *separate* writing-craft note. If the user also needs a literature formal note, still produce (or upgrade) the evidence card.

### `writing-deconstruction overlay`

Trigger when the user explicitly wants the paper mapped onto `write-introduction`, `write-theory`, `write-methods`, or `write-results`.

Load:

- [writing-deconstruction.md](references/writing-deconstruction.md)

Keep the literature note as an evidence card. Put transferable writing observations in §7 if they are brief; otherwise write a companion writer note.

### `skill-harvest overlay`

Trigger when the paper contains a strong and teachable writing pattern that might deserve promotion into one of the named writing skills.

Load [writing-deconstruction.md](references/writing-deconstruction.md).

Default behavior: record the candidate pattern inside the writer note or §7; state the target skill; state the exact rule or example. Only patch skill files when the user explicitly asks.

## Workflow

### 1. Check note memory first

Before creating a new note file, read `memory/notes_log.md`.

Use it to:

- avoid duplicate coverage
- surface likely related notes
- detect whether the task is a fresh note or an upgrade

### 2. Choose the authoritative reading source first

For a supplied or vault full-text Markdown, read that file directly. It is the default authoritative source for content, evidence, tables transcribed into Markdown, hypotheses, and methods. Do not extract it again and do not switch to Zotero PDF for substantive reading.

When a local PDF must be converted and no full-text Markdown exists, default to local OvisOCR2 (workspace PDF rule):

```powershell
D:\OvisOCR2\start-ovisocr2-server.cmd
# wait until http://127.0.0.1:8001/health returns 200
D:\OvisOCR2\run-pdf-ocr-wsl.cmd "<absolute-pdf-path>"
```

Use the bundled wrapper only if the user asks for another parser or OvisOCR2 cannot process the file:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\read_pdf.py" "paper.pdf"
```

If only a DOI, URL, title, or abstract is available, gather the best available metadata first and label the evidence level honestly.

### 3. Resolve metadata (optional Zotero lookup)

When the user gives a title-like query and wants a quick Zotero match, use:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\query_zotero.py" "title keyword"
```

For full note scaffolding, the main scaffold script may resolve DOI, citation key, and optional attachment/title links against Zotero. This lookup never changes the selected reading source.

### 4. Read with the right depth

Follow [reading-framework.md](references/reading-framework.md):

- default to `purposeful`
- escalate to `constructive` when the user wants project relevance, comparison, theory positioning, or reusable methods
- use `triage` when the user only wants keep-or-skip judgment

Map reading depth onto evidence-card frontmatter:

- triage → `reading_stage: to-read` or `browsed`; `status: triage`
- purposeful / constructive → `reading_stage: close-read`; `status: developing` or `citation_ready`

Treat the paper as a case to be defended:

- what is the author trying to prove
- what evidence does the author use
- how is the argument assembled
- where would a sharp reviewer push back

### 5. Force the core note questions

At minimum, answer these every time (they land in Quick View, §1, §6, §8):

1. `如果只用一句话，这篇文章到底想告诉我什么？`
2. `这篇文章好在哪里？如果没有它会少什么？`
3. `这篇文章对我将来的 research 有什么帮助？`

For management and social-science papers, also force these AMJ-backed checks (they land in §1–§6):

1. `这是 genuine puzzle 还是 manufactured gap？practical 和 theoretical 各为什么值得关心？`
2. `文章进入哪场 conversation？没解决的是机制、边界、比较、测量，还是识别？`
3. `常识答案是什么、为什么不够？回答这个问题是推进对话，还是再加一个 setting？`
4. `构念是继承、锐化还是新造？关系形态是 HOW 的哪一种？WHY 是真机制还是标签+引用？`
5. `假设链有没有跳步？`（写入 §3c，每条 H 至少 3 步）
6. `理想检验和实际设计之间的 slippage 在哪里？内生性是否被处理、如何处理？IV/CF 的工具变量或排除变量是什么？发现支撑到关联还是因果？`
7. `若没有这篇，文献会少什么？哪些贡献是 earned，哪些只是 claimed？`

### 6. Scaffold before filling

Use the bundled scaffold when the user wants a new note file created:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\scaffold_obsidian_literature_note.py" `
  --title "Paper Title" `
  --authors "Author One; Author Two" `
  --year 2024 `
  --journal "Journal Name" `
  --doi "10.0000/example" `
  --markdown-path "D:\papers\paper-fulltext.md" `
  --source-type markdown `
  --reading-mode researcher `
  --paper-kind empirical `
  --reading-stage close-read `
  --status developing `
  --vault-root "D:\Onedrive\Obsidian Vault"
```

The scaffold writes an evidence-card skeleton (`template: evidence-card`) unless `--reading-mode writer`. It also supports Zotero-aware extra fields, citation-key resolution, and `--markdown-path` / `--source-type markdown`.

Prefer filling the vault template directly when the paper is already fully read; the scaffold is a file-creation aid, not a license to leave prompts in the finished note.

### 7. Write the note as a decision tool

The visible top of the note is **Quick View**. After verification it must contain:

- the puzzle in one sentence
- the paper's core finding
- named theoretical framework / mechanism
- main-effect coefficient + direction + significance
- key heterogeneity or mechanism
- one sentence of project relevance

Then complete §0–§9, including the AMJ slots in §1–§6. Separate:

- facts from the paper
- your inference about what the paper is doing
- your critique or reuse judgment (§6, §8)

Do not turn the note into a paraphrase dump. Do not emit a separate AMJ seven-module body or an 「概述 / 1. 引言 / 2. 理论与假设」body.

### 8. Save and log the note

When the user wants the note written into the vault and logged, pipe the final markdown into:

```powershell
Get-Content -Raw ".\note.md" | python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\save_note.py" "paper-note.md"
```

`save_note.py` writes the file into the configured Obsidian notes directory, backs up any overwritten file, and appends a structured record to `memory/notes_log.md`.

After saving, add wiki links from the paper note to the full-text source (path-style if the file is outside `literature/`) and from any already-linked maps / import indexes back to the new note.

## Operating Rules

- Formal `literature/` notes must use 天堂模版: `template: evidence-card`, Quick View + §0–§9. AMJ Canvas is the judgment layer inside §1–§6, not a second template.
- Required frontmatter: `note_type`, `title`, `citekey`, `authors`, `year`, `journal`, `paper_kind`, `reading_stage`, `evidence_grade`, `status`, `created`, `updated`, `tags`, `template`. Keep Zotero extra fields when resolved.
- Preserve original constructs and terminology even if the analysis is written in Chinese.
- State the actual full-text source in `verified` and §9. For complete Markdown, label it `verified-from-fulltext-markdown`.
- Prefer a Zotero or Better BibTeX citation key when one is available.
- If only part of the paper was read, say so in Quick View, §0, and §9.
- §3c is mandatory for empirical papers with hypotheses: `H_main` / `H_xxx` / `H_channel_xxx` / `H_med`; each causal chain at least 3 steps with logic types.
- Empirical papers must fill §4 Endogeneity: threat, whether addressed, how. IV or control function notes must record the instrument / excluded variable (name, construction, relevance, exclusion), not only the method name.
- §7 is omit-able (`N/A`) unless a Stata/replication translation layer is needed. Writer-craft harvest may live here if short.
- §8 must contain project-specific handoff, including at least two usable hypothesis or mis-use warnings when a project is in scope.
- Conceptual papers: keep the skeleton; replace measures/identification with argument architecture.
- Do not promote a writing pattern into named writing skills unless it is stable, teachable, and generalizable.

## Bundled Resources

- `config.json`
  - machine-specific defaults for vault, Zotero, note logging, extraction routing, and the evidence-card template path

- `memory/notes_log.md`
  - local note memory for duplicate detection and related-note linkage

- `scripts/read_pdf.py`
  - fallback wrapper around ODL, hybrid ODL, and markitdown (OvisOCR2 is preferred)

- `scripts/query_zotero.py`
  - cached Zotero metadata lookup by title keyword

- `scripts/save_note.py`
  - save note into Obsidian and append note log

- `scripts/scaffold_obsidian_literature_note.py`
  - create a new evidence-card note file with frontmatter and §0–§9 skeleton
  - writer-mode body only when `--reading-mode writer`

- `references/reading-framework.md`
  - reading-depth ladder and default logic for note-making

- `references/note-template.md`
  - operational copy of the evidence-card structure (vault file is authoritative)

- `references/note-style-guide.md`
  - how to fill Quick View and §0–§9

- `references/amj-canvas-questions.md`
  - AMJ question bank already mapped onto §1–§6 of the evidence card

- `references/nelson-reading-guide.md`
  - writer-mode analysis prompts

- `references/writing-deconstruction.md`
  - deeper mapping from paper craft into the named writing skills

- `assets/note_template_researcher.md`
  - fillable evidence-card skeleton

- `assets/note_template_writer.md`
  - writer-mode template (not a `literature/` formal-note format)

## Validation

After edits to this skill, run:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.claude\skills\.system\skill-creator\scripts\quick_validate.py" `
  "$env:USERPROFILE\.claude\skills\literature-notes-obsidian"
```
