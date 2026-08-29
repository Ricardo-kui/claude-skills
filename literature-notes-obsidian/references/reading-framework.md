# Reading Framework

Use this reference to read a paper before writing the Obsidian note.

## Core Idea From the Source PDF

Read the paper as if the author is defending a case in front of a skeptical audience.

That means every strong note should recover:

- what the author is trying to prove
- what evidence the author uses
- how the argument is assembled
- where an imagined reviewer might attack the design, measurement, interpretation, or contribution

The reference PDF also frames good researchers as their own "imagined opponent." Use that mindset while reading. Ask not only "what does the paper say?" but also "where would a sharp reviewer push back?"

## Reading Modes

### Researcher mode

This is the default. Read with the AMJ Canvas questions (puzzle, conversation, WHAT/HOW/WHY, earned contribution), then write a single evidence card (天堂模版: Quick View + §0–§9). The question bank is [amj-canvas-questions.md](references/amj-canvas-questions.md). Do not emit a second AMJ seven-module note.

### Writer mode

Use [nelson-reading-guide.md](references/nelson-reading-guide.md) and [note-style-guide.md](references/note-style-guide.md) when the user wants to learn how the paper is written, structured, and narrated.

## Reading Depth Ladder

### 1. Triage

Use when the user only needs a quick keep-or-skip judgment.

Read in this order:

1. title
2. abstract
3. introduction opening and research question
4. tables, figures, or main results
5. conclusion

Output:

- one-sentence punchline
- whether the paper deserves deep reading
- likely relevance to the user's project

### 2. Purposeful Reading

This should be the default mode.

Recover the paper's backbone:

- research motivation
- exact research gap
- research question
- theory or conceptual move
- hypothesis logic
- variable measurement
- data and setting
- method or identification logic
- main result
- claimed contribution
- stated limitation

Always answer these three questions:

1. `如果只用一句话，这篇文章到底想告诉我什么？`
2. `这篇文章好在哪里？如果没有它会少什么？`
3. `这篇文章对我将来的 research 有什么帮助？`

For management and social-science papers, also answer these gap questions in prose:

1. `为什么这个研究问题值得关心？`
2. `这篇文章进入的是哪场文献讨论？`
3. `已有文献没有回答什么？`
4. `为什么这些未回答的问题重要？`
5. `作者如何借助现有文献把研究问题和独特贡献推出来？`

### 3. Constructive Reading

Use when the user wants deep project value, comparison, or theory positioning.

Go beyond the single paper and ask:

- Which literature stream does this paper belong to?
- What earlier or later papers does it resemble or challenge?
- Is the front-end motivation stronger than the actual gap?
- Which step in the hypothesis logic is doing the real work?
- Which variable measures are elegant, weak, or contestable?
- Does the identification strategy truly support a causal reading?
- What can be borrowed for the user's own project:
  - concept definition
  - mechanism logic
  - variable construction
  - identification strategy
  - robustness pattern
  - paper structure or paragraph move

Constructive reading blends input and output: read while already thinking about how the paper changes the user's own map of the literature.

## Memory Check

Before creating a new note file, check `memory/notes_log.md` for duplicate coverage and related notes worth linking.

## Extraction Checklist

Every full note should capture the paper's core content and land it on the evidence card:

- bibliographic metadata (`template: evidence-card` plus required frontmatter)
- **Quick View**: puzzle 一句, named framework, main-effect coefficient + direction + significance, project relevance
- **§0**: paper type, reading stance, keep / do not copy / must add
- **§1**: RQ, constructs in RQ, genuine vs manufactured puzzle, why-care practical/theoretical, intuition, gap type, literature move
- **§2**: conversation, prior consensus, unresolved type, 2–4 strands
- **§3**: lens + work test; constructs (origin) + relationship form; hypothesis logic (≥3-step chains); claims table
- **§4**: why-setting, design, sample, comparison, DV/IV, FE/cluster, assumptions, slippage; empirical Endogeneity (threat, Addressed?, strategy, residual threat; IV/CF must name the instrument/excluded variable)
- **§5**: main results, statistical vs substantive, interpretive weight, validity
- **§6**: earned vs claimed contribution, absence test, project critique
- **§7**: replication/Stata layer or `N/A`
- **§8**: project handoff and mis-use warnings
- **§9**: citation key, source path, Zotero, verification method

## What To Avoid

- Do not summarize paragraph by paragraph unless the user explicitly asks.
- Do not confuse correlation with causal identification in the note.
- Do not write "important" or "interesting" without saying why.
- Do not copy the paper's prose when a clean analytical sentence would do.
- Do not write a note that lacks a clear reuse judgment.

## Research Canvas Lens

Use Dorobantu et al. (2024) AMJ Canvas as the judgment lens, already mapped onto the evidence card:

1. Puzzle and why-care → §1
2. Audience / conversation → §2
3. Research question and literature move → §1
4. Constructs (WHAT) and relationship form (HOW) → §3b
5. Mechanism and lens (WHY) → §3a / §3c
6. Setting, measures, identification, slippage → §4
7. Findings and interpretive weight → §5
8. Earned contribution, absence test, boundaries → §6
9. Project reuse → §8

This lens prevents the note from collapsing into a loose summary. It forces a paper-shaped explanation *inside one template*.

## Management / Social-Science Reading Bias

When the paper is from management, strategy, organization theory, IB, sociology, political science, or adjacent empirical social science, pay special attention to:

- `Motivation and gap` (Introduction)
  - Big phenomenon does not automatically imply a real research gap.
  - Capture what prior work knows, what it misses, and why that matters (so what).
  - Note how the authors earn the gap through prior literature, not merely announce it.

- `Theory and hypotheses`
  - Identify the core theoretical perspective and its main propositions.
  - Trace the author's logic from theory to hypotheses: what is the central mechanism or reasoning?
  - Note the specific hypotheses and their directional predictions.
  - Flag any hypotheses that seem under-theorized or rely heavily on citation rather than argument.

- `Measurement`
  - Distinguish the theoretical construct from its operational measure.
  - Ask whether proxies, codings, scales, and archival measures are plausible and whether important mismatch remains.

- `Causal identification`
  - Explicitly state what source of variation or comparison the paper relies on.
  - Separate:
    - descriptive pattern
    - correlational regression
    - stronger identification strategy
  - Note the key identifying assumptions and the most serious threats.
  - For empirical papers, record whether endogeneity was addressed and how. If IV or control function: name the instrument / excluded variable, why it was chosen, relevance, and exclusion. Do not treat FE + controls as equivalent to IV.

## Evidence-Card Note Writing

Write the final note in the 天堂模版 skeleton, with AMJ judgment slots filled in §1–§6. Use the template's lists for scoped sections. Use compact prose for Quick View, §3a, and each §3c causal chain.

Do not emit a separate AMJ seven-module body or an 「概述 / 1. 引言 / 2. 理论与假设」body as the `literature/` formal note.
