---
name: literature-notes-obsidian
description: Read one academic paper or a small paper set into Obsidian-ready literature notes, with a management and social-science bias. Use when Codex needs to read a local PDF, DOI, URL, title, or abstract; upgrade an existing literature note; compare 2-5 papers; or write a reusable Obsidian note that captures research motivation, exact gap, theory or hypothesis logic, variable measurement, empirical strategy, contribution, threats, and reuse value. Also use when the user wants a paper read in `researcher` mode or `writer` mode, wants Zotero metadata resolved into the note, wants the note saved into an Obsidian vault with note logging, or wants writing deconstruction mapped onto `write-social-science-introduction`, `write-theory-and-hypotheses`, and `write-methods-and-results`.
---

# Literature Notes for Obsidian

Use this skill to turn papers into sharp, reusable Obsidian notes. The note should help the user decide what the paper says, why it matters, where it is weak, and how it can be reused in the user's own project.

This skill now supports two reading modes:

- `researcher` mode: judge puzzle, gap, measurement, identification, and contribution
- `writer` mode: judge structure, narrative moves, paragraph logic, and what writing patterns are worth borrowing

Default note style: paragraph-first, not checklist-first. Use metadata for retrieval; use paragraphs for substantive explanation.

## Scope

- Use for one paper, a small batch, an existing rough note, or a request such as "read this paper into my Obsidian vault."
- Use for `upgrade-note`, `compare-papers`, and `abstract-only` tasks as well as fresh note creation.
- Use for writing deconstruction when the user wants to learn how a paper is written.
- Do not use for ongoing paper recommendation, discovery loops, or long-term reading-feed maintenance; use `articlefeed` for that.

## Default Paths and Runtime State

Read `config.json` for machine-specific defaults. Current defaults are:

- `vault_root`: `D:\Onedrive\Obsidian Vault`
- `default_notes_dir`: `literature`
- `zotero_db`: `D:\同步文件\文献库\zotero.sqlite`
- `zotero_storage`: `D:\同步文件\文献库\storage`
- `memory_log`: `memory/notes_log.md`

Keep `config.json` and the scripts in sync. Do not hardcode stale machine-specific paths into new updates.

## Router

Resolve the task in this order:

1. `read-one`
2. `upgrade-note`
3. `compare-papers`
4. `abstract-only`

Then apply mode and overlays:

- `researcher mode` overlay
- `writer mode` overlay
- `writing-deconstruction overlay`
- `skill-harvest overlay`

### `read-one`

Trigger when the user gives one paper and wants an Obsidian note.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)

### `upgrade-note`

Trigger when the user already has a rough note, highlights, or extracted Markdown and wants a better literature note.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)

Keep the original metadata and upgrade the reasoning, structure, and scan-ability.

### `compare-papers`

Trigger when the user wants one synthesis note comparing 2-5 papers on the same puzzle, method, mechanism, or concept.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)

Create one synthesis note plus explicit links to the underlying paper notes when available.

### `abstract-only`

Trigger when only an abstract, title, citation, DOI, or partial metadata is available.

Load:

- [reading-framework.md](references/reading-framework.md)
- [note-template.md](references/note-template.md)

Mark the note clearly as abstract-based. Do not pretend to have read the full paper.

### `researcher mode`

This is the default.

Load:

- [reading-framework.md](references/reading-framework.md)
- [amj-canvas-questions.md](references/amj-canvas-questions.md)
- [note-style-guide.md](references/note-style-guide.md)

Use this mode when the user wants to evaluate design credibility, contribution, causal leverage, or reuse value for their own research.

### `writer mode`

Trigger when the user asks how the paper is written, asks for a writing exemplar analysis, asks for "写作模式" / "as a writer", or mainly wants structural craft rather than substantive critique.

Load:

- [reading-framework.md](references/reading-framework.md)
- [nelson-reading-guide.md](references/nelson-reading-guide.md)
- [note-style-guide.md](references/note-style-guide.md)
- `assets/note_template_writer.md`

Use this mode to extract introduction strategy, literature-review moves, methods/results narration, and transferable writing patterns.

### `writing-deconstruction overlay`

Trigger when the user explicitly wants the paper mapped onto:

- `write-social-science-introduction`
- `write-theory-and-hypotheses`
- `write-methods-and-results`

Load:

- [writing-deconstruction.md](references/writing-deconstruction.md)
- [note-template.md](references/note-template.md)

### `skill-harvest overlay`

Trigger when the paper contains a strong and teachable writing pattern that might deserve promotion into one of the three named writing skills.

Load:

- [writing-deconstruction.md](references/writing-deconstruction.md)

Default behavior:

- record the candidate pattern inside the note
- state which target skill it belongs to
- state the exact rule or example worth absorbing

Only patch the target skill files when the user explicitly asks for that update or the task clearly includes skill maintenance.

## Workflow

### 1. Check note memory first

Before creating a new note file, read `memory/notes_log.md`.

Use it to:

- avoid duplicate coverage
- surface likely related notes
- detect whether the task is a fresh note or an upgrade

### 2. Choose extraction route first

For local PDFs, prefer the bundled wrapper:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\read_pdf.py" "paper.pdf"
```

The wrapper follows the current workspace routing:

- default to `opendataloader-pdf` for academic PDFs
- try hybrid ODL on harder layouts
- fall back to `markitdown`
- apply the Windows non-ASCII path fallback automatically

If the user needs a specific engine, use:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\read_pdf.py" "paper.pdf" --force-hybrid
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\read_pdf.py" "paper.pdf" --force-markitdown
```

If only a DOI, URL, title, or abstract is available, gather the best available metadata first and label the evidence level honestly.

### 3. Resolve Zotero metadata

When the user gives a title-like query and wants a quick Zotero match, use:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\query_zotero.py" "title keyword"
```

For full note scaffolding, the main scaffold script already tries DOI, attachment, and title matching against Zotero.

### 4. Read with the right depth

Follow [reading-framework.md](references/reading-framework.md):

- default to `purposeful`
- escalate to `constructive` when the user wants project relevance, comparison, theory positioning, or reusable methods
- use `triage` when the user only wants keep-or-skip judgment

Treat the paper as a case to be defended:

- what is the author trying to prove
- what evidence does the author use
- how is the argument assembled
- where would a sharp reviewer push back

### 5. Force the core note questions

At minimum, answer these every time:

1. `如果只用一句话，这篇文章到底想告诉我什么？`
2. `这篇文章好在哪里？如果没有它会少什么？`
3. `这篇文章对我将来的 research 有什么帮助？`

For management and social-science papers, also force these checks:

1. `作者为什么觉得这个问题值得研究？`
2. `文章到底补了哪一个 gap，而不是泛泛地说“文献很少研究”？`
3. `假设推导的理论链条有没有跳步？`
4. `变量测量和识别策略能不能支撑作者的因果或理论主张？`

### 6. Scaffold before filling

Use the bundled scaffold when the user wants a new note file created:

```powershell
python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\scaffold_obsidian_literature_note.py" `
  --title "Paper Title" `
  --authors "Author One; Author Two" `
  --year 2024 `
  --journal "Journal Name" `
  --doi "10.0000/example" `
  --pdf-path "D:\papers\paper.pdf" `
  --reading-mode researcher `
  --vault-root "D:\Onedrive\Obsidian Vault"
```

The scaffold script now supports:

- `--reading-mode researcher|writer`
- Zotero-aware frontmatter
- citation-key resolution
- writer-mode note bodies
- stronger theory-and-hypothesis prompts for grouped hypotheses and multi-mechanism `WHY`

### 7. Write the note as a decision tool

The visible top of the note should let the user answer:

- What is the paper's one-sentence punchline?
- Is it worth deeper reading or reuse?
- What is the main contribution?
- What is the most relevant takeaway for the user's own project?
- What research motivation and research gap justify the paper?
- What theory, measurement, and identification structure hold the paper together?
- What part of the writing is worth imitating?

Do not turn the note into a paraphrase dump. Separate:

- facts from the paper
- your inference about what the paper is doing
- your critique or reuse judgment

### 8. Save and log the note

When the user wants the note written into the vault and logged, pipe the final markdown into:

```powershell
Get-Content -Raw ".\note.md" | python "$env:USERPROFILE\.claude\skills\literature-notes-obsidian\scripts\save_note.py" "paper-note.md"
```

`save_note.py` writes the file into the configured Obsidian notes directory, backs up any overwritten file, and appends a structured record to `memory/notes_log.md`.

## Operating Rules

- Preserve traceable metadata: title, authors, year, source, DOI/URL when available.
- Preserve Zotero linkage when available: item key, attachment key, select link, and PDF link.
- Prefer a Zotero or Better BibTeX citation key when one is available; otherwise fall back to the generated citekey.
- Keep the paper's constructs and original terminology accurate even if the analysis is written in Chinese.
- If only part of the paper was read, say so directly.
- If extraction is messy, repair structure before interpreting content.
- For comparison notes, cite note titles or source filenames so the synthesis remains auditable.
- Prefer short, high-signal sentences. The note should be scannable inside Obsidian.
- Prefer paragraph exposition for research purpose, research gap, theory and hypothesis logic, contribution, and limitation.
- Use bullets mainly for metadata, compact comparisons, or enumerated mechanism channels.
- If the paper is conceptual rather than empirical, replace measures and identification with argument architecture and conceptual contribution.
- In writer mode, separate what is strong because of content from what is strong because of writing.
- Do not promote a pattern into the named writing skills unless it is stable, teachable, and generalizable.

## Bundled Resources

- `config.json`
  - machine-specific defaults for vault, Zotero, note logging, and extraction routing

- `memory/notes_log.md`
  - local note memory for duplicate detection and related-note linkage

- `scripts/read_pdf.py`
  - local wrapper around ODL, hybrid ODL, and markitdown

- `scripts/query_zotero.py`
  - cached Zotero metadata lookup by title keyword

- `scripts/save_note.py`
  - save note into Obsidian and append note log

- `scripts/scaffold_obsidian_literature_note.py`
  - create a new note file with frontmatter and section skeleton
  - resolve a default Obsidian literature-note directory
  - try to resolve a Zotero parent item and PDF attachment from the local Zotero database
  - support `researcher` and `writer` note bodies

- `references/reading-framework.md`
  - reading-depth ladder and default logic for note-making

- `references/amj-canvas-questions.md`
  - AMJ-style researcher prompts

- `references/nelson-reading-guide.md`
  - writer-mode analysis prompts

- `references/note-style-guide.md`
  - paragraph-first note style and bilingual guidance

- `references/note-template.md`
  - the default research-canvas note structure

- `references/writing-deconstruction.md`
  - deeper mapping from paper craft into the three named writing skills

- `assets/note_template_researcher.md`
  - an AMJ-canvas-style researcher template

- `assets/note_template_writer.md`
  - a writer-mode template

## Validation

After edits to this skill, run:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.claude\skills\.system\skill-creator\scripts\quick_validate.py" `
  "$env:USERPROFILE\.claude\skills\literature-notes-obsidian"
```
