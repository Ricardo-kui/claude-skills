# Evidence Card Template（天堂模版）

Authoritative copy lives in the vault:

`D:\Onedrive\Obsidian Vault\00 工作台\evidence-card-template.md`

This file is the skill's operational copy. If they diverge, **the vault file wins**.

`literature/` formal notes use this structure only. Heading order stays Quick View + §0–§9. AMJ Canvas (Dorobantu et al. 2024) is **folded into those sections**, not a second note body.

| AMJ module | Lands in |
|------------|----------|
| M1 Puzzle | §1 Core puzzle, Why care, genuine vs manufactured |
| M2 Audience | §2 Conversation, prior consensus, unresolved type, strands |
| M3 Research Question | §1 RQ, constructs in RQ, intuition, literature move |
| M4 WHAT / HOW / WHY | §3a lens + work test; §3b constructs + relationship form; §3c chains |
| M5 Setting and Design | §4 why-setting, comparison, assumptions, slippage, **endogeneity / IV-CF instruments** |
| M6 Findings | §5 coefficients + statistical vs substantive + interpretive weight |
| M7 Contribution | §6 earned vs claimed, absence test, boundary |

天堂-only sections: §0 scope, §3c numbering, §7 replication, §8 project handoff, §9 metadata.

Writer-mode notes use `assets/note_template_writer.md` and are not `literature/` formal notes.

Existing cards (pre-2026-08-29) do not need a rewrite. New ingest and upgrades fill the added slots.

## Frontmatter Schema

Required: `note_type`, `title`, `citekey`, `authors`, `year`, `journal`, `paper_kind`, `reading_stage`, `evidence_grade`, `status`, `created`, `updated`, `tags`, `template: evidence-card`.

Fill after verification: `confidence`, `verified`, `doi`, `projects`, `project_relevance`, `related`. Keep Zotero extras when resolved.

## 段落结构

### Quick View

150–250 词。Puzzle 一句；核心发现；框架/机制名；主效应系数+方向+显著性；异质性或机制；项目 relevance 一句。不要复述摘要。

### §0. Reading Scope and Paper Type

Paper type; reading stance; Keep / Do not copy / Must add.

### §1. Research Question, Purpose, and Gap

One-sentence RQ; constructs in the RQ; purpose type; core puzzle (genuine vs manufactured); why care practical + theoretical; intuitive answer and why not enough; gap type (`mechanism|boundary|comparison|measurement|identification`); gap 1–2 sentences; literature move (not another setting).

### §2. Prior Research on This Question

Conversation (scholars, assumptions, theories); prior consensus; unresolved type; then 2–4 strands: 前人做了什么 → 缺了什么 → 本文如何填补.

### §3. Theory, Constructs, and Claims

- **3a** lens + why it fits + work test (real causal/behavioral work vs labels/citations)
- **3b** each construct: definition, origin (`inherited|sharpened|new`), operationalization, role; plus relationship form (`linear|moderated|mediated|sequential|recursive|comparative`)
- **3c** each H: 理论前提 / ≥3-step 因果机制 with logic types / 实证预测 / rival / 边界
- **3d** claims table with 逻辑链关键词

### §4. Research Design, Data, Measures, and Ethics

Why this setting; design; sample; comparison structure; DVs; IVs; controls; FE/cluster; identifying assumptions; slippage; extra ID features.

Empirical papers must fill **Endogeneity**: threat; Addressed? (`yes|partial|no|not claimed`); strategy; residual threat. IV requires instrument name, construction, relevance, exclusion, diagnostics. Control function requires the excluded variable / CF source (name + construction), first-stage/CF construction, and diagnostics. Do not write only “used IV/CF”. Interpretive weight in §5 cannot exceed this verdict. Conceptual papers: `N/A（非实证）`.

### §5. Findings, Validity, and Interpretation

Main effects; hetero/channels; robustness; statistical vs substantive; interpretive weight (association / conditional association / causal); internal/external validity.

### §6. Contribution, Critique, and Reuse

Theoretical; empirical/method; earned vs claimed; absence test; boundary; project critique; key citations to retain.

### §7. Codex-Required Sections

`N/A（<原因>）` unless a Stata/replication layer is needed.

### §8. Project Handoff and Evidence Check

Motivation/gap use; theory/hypothesis use; measures; reviewer defense; related papers; mis-use warning; concept/argument-card follow-ups. At least two project-specific uses or warnings when a project is in scope.

### §9. Metadata Notes

Citekey, DOI, canonical source, full-text path, Zotero, reading status, confidence, stub corrections.

## 质量检查清单

见 vault 模版。最低限度：`template: evidence-card`；§1 puzzle/gap type；§3c 三层链；实证 §4 内生性（IV/CF 记录工具变量）；§6 absence test；§8 项目手递；没有另写 AMJ 七模块正文。
