---
note_type: literature-note
title: "{Paper Title}"
aliases:
  - "{CiteKey}"
citekey: "{CiteKey}"
authors:
  - "{Last, First}"
year: "{YYYY}"
journal: "{Journal}"
doi: "{DOI}"
url: "{URL}"
zotero_item_key: "{ZOTERO_ITEM_KEY}"
zotero_attachment_key: "{ZOTERO_ATTACHMENT_KEY}"
zotero_select_uri: "zotero://select/library/items/{ZOTERO_ITEM_KEY}"
zotero_pdf_uri: "zotero://open-pdf/library/items/{ZOTERO_ATTACHMENT_KEY}"
paper_kind: "{theoretical|empirical|review|methods|mixed}"
reading_stage: "{to-read|browsed|close-read}"
evidence_grade: "{low|medium|high}"
reuse_level: "{low|medium|high}"
project_relevance:
  - "{project-slug}"
archive_only: false
status: "{triage|developing|citation_ready}"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags:
  - source
  - literature-note
projects:
  - "{project-slug}"
related: []
confidence: "{seed|low|medium|high}"
verified: "{YYYY-MM-DD — 核验方式}"
template: evidence-card
---

# {Paper Title}

## Quick View

{150–250 词：puzzle 一句；核心发现；框架/机制名；主效应系数 + 方向 + 显著性；异质性或机制；项目 relevance 一句。不要复述摘要。}

原文：[[path-style-wikilink-to-fulltext|显示名]]。

---

## §0. Reading Scope and Paper Type

- Paper type:
- Reading stance: core / supporting / background
- Keep:
- Do not copy:
- Must add:

---

## §1. Research Question, Purpose, and Gap

- One-sentence RQ:
- Constructs in the RQ:
- Purpose type: explanatory / exploratory / descriptive
- Core puzzle: 真实现象或未解经验模式；若是 manufactured gap，在此点破
- Why care — practical:
- Why care — theoretical:
- Intuitive answer, and why it is not enough:
- Gap type: mechanism / boundary / comparison / measurement / identification
- Gap:
- Literature move: 如何推进这场对话，而不是再加一个 setting

---

## §2. Prior Research on This Question

- Conversation:
- Prior consensus:
- Unresolved: mechanism / boundary / comparison / measurement / identification
- **Strand 1 — [标签]**: 前人做了什么 → 缺了什么 → 本文如何填补
- **Strand 2 — [标签]**:

---

## §3. Theory, Constructs, and Claims

### 3a. Theoretical framework

{框架名称 + 核心逻辑 + 为什么适合这个 RQ。}

Work test: 机制是否做了真实的因果/行为工作，还是主要靠理论标签和引用？

### 3b. Core constructs

- **{Construct}**:
  - Definition:
  - Origin: inherited / sharpened / newly introduced
  - Operationalization:
  - Role: IV / DV / mediator / moderator
- Relationship form: linear / moderated / mediated / sequential / recursive / comparative

### 3c. Hypothesis Logic

**H_main (标签): 一句话预测**

- 理论前提:
- 因果机制: A → B → C → Y（每步标注逻辑类型）
- 实证预测:
- 竞争性解释排除:
- 边界:

### 3d. Key claims (summary table)

| H | 预测 | 系数 | 显著性 | 逻辑链关键词 |
|---|------|------|--------|------------|
| H_main |  |  |  |  |

---

## §4. Research Design, Data, Measures, and Ethics

- Why this setting:
- Design:
- Sample:
- Comparison structure:
- DVs:
- Key IVs:
- Controls:
- Fixed effects / SE clustering:
- Identifying assumptions:
- Slippage (ideal test vs actual design):
- Key identification features:

Endogeneity（实证必填；概念文 `N/A（非实证）`）

- Threat: simultaneity / omitted variable / measurement error / selection / reverse causality
- Addressed?: yes / partial / no / not claimed
- Strategy: OLS+controls / FE / matching / DiD / RDD / IV / control function / other
- Residual threat:

若 IV：

- Endogenous regressor:
- Instrument(s): 名称、构造、variation 层级
- Why this instrument:
- Relevance（一阶段 F / KP 等）:
- Exclusion（作者论证 + 笔记是否买账）:
- Diagnostics:

若 control function：

- Endogenous regressor:
- CF source / excluded variable: 名称 + 构造（不得只写“用了 CF”）
- First stage / CF construction:
- Why this source:
- Diagnostics:

---

## §5. Findings, Validity, and Interpretation

- 主效应:
- 异质性/调节:
- 渠道/中介:
- 稳健性:
- Statistical vs substantive:
- Interpretive weight: association / conditional association / causal（不得高于 §4 Endogeneity 的 Addressed?）
- 内部效度:
- 外部效度:

---

## §6. Contribution, Critique, and Reuse

- Theoretical contribution:
- Empirical / methodological contribution:
- Earned vs claimed:
- Absence test: 若没有这篇，文献会少什么
- Boundary:
- My critique for {project}:
- Key citations to retain:

---

## §7. Codex-Required Sections

N/A（无需 Stata/复制层）

---

## §8. Project Handoff and Evidence Check

- Motivation / gap use:
- Theory / hypothesis use:
- Variables / measures:
- Reviewer defense use:
- Related / similar / opposing papers:
- My critique:
- Should create or update concept page:
- Should create or update argument card:
- Atomic deep-evidence page needed: yes / no

---

## §9. Metadata Notes

- Citation key: {CiteKey}
- DOI: {DOI}
- Journal volume/issue/pages:
- Canonical source: [[{CiteKey}]]
- Source PDF / Markdown: {Source}
- Zotero item link: [Open Zotero Item](zotero://select/library/items/{ZOTERO_ITEM_KEY})
- Zotero PDF link: [Open Zotero PDF](zotero://open-pdf/library/items/{ZOTERO_ATTACHMENT_KEY})
- Reading status: verified-from-fulltext-markdown / verified-from-pdf / stub
- Confidence:
- Key corrections from stub:
