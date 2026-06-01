# Obsidian Note Template

Use this as the default `researcher`-mode note structure. It keeps the note decision-oriented, paragraph-first, and reusable inside Obsidian.

When the user wants:

- a stricter AMJ canvas note, also read [amj-canvas-questions.md](references/amj-canvas-questions.md) and optionally consult `assets/note_template_researcher.md`
- a writing-only note, use `assets/note_template_writer.md` together with [nelson-reading-guide.md](references/nelson-reading-guide.md)
- explicit writing transfer into the three named writing skills, layer on [writing-deconstruction.md](references/writing-deconstruction.md)

## Preferred Structure

```markdown
---
title: "{{title}}"
aliases:
  - "{{citekey}}"
authors:
  - "{{author_1}}"
year: "{{year}}"
journal: "{{journal}}"
doi: "{{doi}}"
url: "{{url}}"
citekey: "{{citekey}}"
citation_key: "{{citation_key}}"
citation_key_source: "{{citation_key_source}}"
pandoc_cite: "{{pandoc_cite}}"
zotero_item_key: "{{zotero_item_key}}"
zotero_attachment_key: "{{zotero_attachment_key}}"
zotero_select_uri: "{{zotero_select_uri}}"
zotero_pdf_uri: "{{zotero_pdf_uri}}"
note_type: "literature-note"
reading_mode: "researcher"
source_type: "pdf"
reading_stage: "purposeful"
status: "reading"
created: "YYYY-MM-DD"
tags:
  - "literature-note"
  - "paper"
---

# {{title}}

## Quick View

用一个短段落回答四件事：这篇文章到底在说什么，值不值得深读，证据强度如何，它对我有什么直接用处。

## 1. Research Purpose and Research Gap

写成 2-4 段。

第一段：现象、问题或谜题是什么，为什么值得关心。

第二段：文章进入的是哪场 literatures / 对话 / 争论。

第三段：已有文献究竟遗漏了什么。不要只写“研究较少”，而要写清楚遗漏的是机制、边界条件、比较关系、测量、还是因果判断。

第四段：为什么这些遗漏重要，以及作者如何借助已有文献把研究问题和独特贡献推出来。

## 2. Theory, Argument, and Hypothesis Logic

写成 2-4 段。解释核心构念、理论视角、机制链条、以及假设如何被一步一步“挣出来”。

如果论文在正式假设前先整合多条理论传统，可加一个小节 `理论前提与框架整合`，说明作者如何让这些理论互补，而不是平行堆放。

如果论文按理论块组织假设，可在本节下使用分组小标题。每个假设或核心主张都尽量区分：

- `HOW`：假设本身，即变量、方向、效应类型
- `WHY`：支撑这个关系的机制。若机制可枚举，可以用短 bullet 说明多个渠道，最后点出其共同依托的上位理论

最后补一段整体评估：

- 理论逻辑最强的地方在哪里
- 哪一步有跳跃或偷换
- 多组假设是否共享一个连贯的上位逻辑，还是有“拼接感”
- 作者如何从文献综述切入自己的解释

## 3. Variables, Measures, and Empirical Strategy

如果论文是实证研究，写成 2-4 段：

第一段：setting、sample、data source、research design。

第二段：核心变量如何操作化，理论构念与实际 proxy 是否贴切。

第三段：文章依赖的识别或比较逻辑是什么。variation 从哪里来，关键识别假设是什么，最主要的威胁是什么。

第四段：主要结果是什么，作者如何解释这些结果，这种解释是否超出设计所能支持的强度。

如果论文是理论或概念性文章，没有实证部分，则明确写一句：
`本文为理论/概念性文章，无正式变量测量和因果识别设计；应重点评估其概念界定、论证链条与理论贡献。`

## 4. Contribution, Limits, and My Judgment

写成 2-3 段：

第一段：理论贡献、经验贡献或方法贡献到底是什么。

第二段：局限、边界条件、最容易被攻击的地方。

第三段：我自己的总体判断。这篇文章好在哪里，如果没有它会少什么，它对我将来的 research 有什么帮助。

## 5. Writing Deconstruction

### 5.1 Introduction Craft

用一个短段落说明它的前端是怎么写的：hook 怎么开，文献讨论怎么转，gap 句子如何落地，paper move 如何显出来。

然后写一句：
`Transferable rule for $write-social-science-introduction: ...`

### 5.2 Theory and Hypotheses Craft

用一个短段落说明它如何引入构念、铺机制、把文献支持变成 why 逻辑，以及如何让假设显得是“被挣出来的”。

然后写一句：
`Transferable rule for $write-theory-and-hypotheses: ...`

### 5.3 Methods and Results Craft

用一个短段落说明它如何写 sample、measure、identification、results、interaction、robustness，尤其是如何避免念表和过度因果语言。

然后写一句：
`Transferable rule for $write-methods-and-results: ...`

## 6. Writing Transfer Candidate

只有在模式真的可泛化时才填写。简短写明：

- target skill
- source passage or paragraph
- why it works
- generalized rule
- confidence

## 7. Metadata Notes
- Citation key:
- Citation key source:
- Pandoc cite token:
- Source file or link:
- Zotero item key:
- Zotero attachment key:
- Zotero item link: `[Open Zotero Item](zotero://select/library/items/...)`
- Zotero PDF link: `[Open Zotero PDF](zotero://open-pdf/library/items/...)`
- Reading date:
- Related notes:
```

## Writing Rules

- Make `Quick View` a short paragraph, not a checklist.
- Keep `Research Purpose and Research Gap` paragraph-heavy. This is the note's center of gravity.
- Use `Theory, Argument, and Hypothesis Logic` to reconstruct the mechanism chain, not to paraphrase the theory section.
- Distinguish theory labels from actual explanation.
- Distinguish constructs from proxies and associations from causal leverage.
- If the note is abstract-based, say so explicitly in `Quick View` and `Metadata Notes`.
- If the paper is weak, say exactly where it is weak.
- If the paper is useful, say exactly what is reusable.
