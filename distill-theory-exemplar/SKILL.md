---
name: distill-theory-exemplar
description: "蒸馏顶刊论文 Theory & Hypotheses 范文——识别理论构建类型、拆解功能模块与 why-chain 模式（提炼 HOW they explain why），并反馈 write-theory 语料缺口。当用户要求学习/蒸馏某篇论文理论与假设部分的写法时使用。"
whenToUse: "当用户要求蒸馏、提炼、学习某篇（或批量）论文 Theory 或 Hypotheses 部分的论证手法时使用。触发词：蒸馏 theory、提炼理论部分、学习这篇理论写法、分析假设怎么推的、theory 范文蒸馏、批量蒸馏理论与假设"
---

# Distill Theory Exemplar

Distill the architecture and reasoning of a published Theory section into reusable patterns without copying its substantive claims.

## Workflow

先确认请求性质：范文蒸馏走本 skill；草稿审查 → `theory-review`；用户只说"分析/蒸馏这篇论文"未指定 section 时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。

1. Read `references/intake-and-classification.md`; identify theory-building type, hypothesis structure, evidence boundaries, and story-fidelity classification. For Incommensurability, also read `../write-theory/references/incommensurability-resolution-routes.md` and produce its L0–L3 full-text profile before extracting hypothesis skeletons.
2. Load only the phase required:
   - module mapping, special institutional-shock lenses, and coverage: `references/phase-1-module-map.md`
   - persuasive actions, expression skeletons, and why-chains: `references/phase-2-extraction.md`
   - DNA/profile reporting and DNA→validator reflux (Phase 3.5): `references/phase-3-dna-report.md`
   - cross-paper validation and corpus writeback: `references/phase-4-validation-writeback.md`
   - final QC, honesty boundaries, and downstream interface: `references/phase-5-qc-and-boundaries.md`
3. Load supporting protocols only as needed: `protocols/corpus_taxonomy.md`, `protocols/phase2_extraction_frameworks.md`, `protocols/profile_template.md`, `protocols/phase5_qc.md`, `protocols/connector_patterns.md`, `protocols/pollock_annotations.md`, and `protocols/writeback_reminders.md`.
4. Compare against the sibling `write-theory/corpus/` only after the paper-first extraction is complete.
5. Treat single-paper patterns as candidates, not stable corpus rules. For Incommensurability, use R1–R4 to compare reasoning, not to impose model form: L2 architectures remain optional and L3 model signatures never enter core routing. Reference-level variants may be written automatically; core candidates first enter the design registry and only bounded, eligible low/medium-risk corrections may auto-apply.
6. In Phase 4, load `references/design-feedback-loop.md`, compare observed practice with current write-theory rules, and always emit `skill_design_feedback`（无缺陷时 `observations: []`）. Persist candidates with `_update_design_feedback.py`.
7. Auto-write eligible reference variants. Apply bounded core corrections only when the evidence, authorization, risk, and dual-regression gates pass; schema/stage-gate/high-risk changes always require explicit review.

**完成判据**：①请求性质已确认（蒸馏 vs 审查；section 已消歧）；②理论构建类型 + 假设结构 + story-fidelity 分类已输出（Incommensurability 时含 L0–L3 profile、route confidence 与 distinguishing prediction）；③所用 phase 输出件按请求深度齐全（module map / why-chains / DNA / QC）；④每个写入变体/句式附带原文锚点字段；⑤`skill_design_feedback` 必发（无缺陷时 `observations: []`）并已持久化；⑥自动写回仅限 reference 级变体与有界低风险 core 修正。

## 选材 Gate（轻量版：读 routing 表与验证状态）

蒸馏选材时，读 `write-theory/corpus/meta/routing_table.md`（Gap × 贡献杠杆 → 首选变体）与目标变体文件的验证状态做三带判定：

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap** | routing 表/语料中无对应理论构建变体 | **HIGH**：ADD 候选，优先深读 |
| **薄弱** | 目标变体单篇来源/EMERGING/「待第二篇交叉验证」 | **HIGH**：EXTEND/REPLACE 候选 |
| **quiet** | 目标变体多篇验证 | MEDIUM：正常蒸馏（除非论文带来明确新维度） |

批量模式按带排序优先处理 HIGH 档。单篇论文（用户明确指定）不拒绝，但输出带判定。

## 原文锚点提取规则（语料锚点层）

每个待写入变体/句式模板必须附带 `**原文锚点**` 字段——来源论文 1-2 句 verbatim 原句（15-50 tokens），风格参照用：

- **选句标准**：最能代表该变体论证手法的句子（如构念辨析的定义区分句、机制链的推导句、调节的交互预期句、辩证对立的整合 resolution 句）
- **提取来源**：优先本次蒸馏论文原文；缺失时按知识库检索（mvp30 / Clippings / 论文导入 / 写作指导 四源，见 `corpus/variants/` 既有锚点格式）
- **检索不到原文**：锚点标"待补"，不阻塞写入
- **边界**：锚点是风格参照不是复制源——不得保留专有名词/数字；citation 链接还原为纯文本；OCR 污染句优先选无污染句

**完成判据**：①请求性质已确认（蒸馏 vs 审查；section 已消歧）；②理论构建类型 + 假设结构 + story-fidelity 分类已输出（Incommensurability 时含 L0–L3 profile、route confidence 与 distinguishing prediction）；③所用 phase 输出件按请求深度齐全（module map / why-chains / DNA / QC）；④每个写入变体/句式附带原文锚点字段；⑤`skill_design_feedback` 必发（无缺陷时 `observations: []`）并已持久化；⑥自动写回仅限 reference 级变体与有界低风险 core 修正。

## 选材 Gate（轻量版：读 routing 表与验证状态）

蒸馏选材时，读 `write-theory/corpus/meta/routing_table.md`（Gap × 贡献杠杆 → 首选变体）与目标变体文件的验证状态做三带判定：

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap** | routing 表/语料中无对应理论构建变体 | **HIGH**：ADD 候选，优先深读 |
| **薄弱** | 目标变体单篇来源/EMERGING/「待第二篇交叉验证」 | **HIGH**：EXTEND/REPLACE 候选 |
| **quiet** | 目标变体多篇验证 | MEDIUM：正常蒸馏（除非论文带来明确新维度） |

批量模式按带排序优先处理 HIGH 档。单篇论文（用户明确指定）不拒绝，但输出带判定。

## 原文锚点提取规则（语料锚点层）

每个待写入变体/句式模板必须附带 `**原文锚点**` 字段——来源论文 1-2 句 verbatim 原句（15-50 tokens），风格参照用：

- **选句标准**：最能代表该变体论证手法的句子（如构念辨析的定义区分句、机制链的推导句、调节的交互预期句、辩证对立的整合 resolution 句）
- **提取来源**：优先本次蒸馏论文原文；缺失时按知识库检索（mvp30 / Clippings / 论文导入 / 写作指导 四源，见 `corpus/variants/` 既有锚点格式）
- **检索不到原文**：锚点标"待补"，不阻塞写入
- **边界**：锚点是风格参照不是复制源——不得保留专有名词/数字；citation 链接还原为纯文本；OCR 污染句优先选无污染句

## Output contract

Return the theory-building classification, functional module map, why-chain, construct relationships, hypothesis organization, transferable skeletons, non-transferable boundaries, evidence anchors, QC findings, and `skill_design_feedback`. For Incommensurability, include L0–L3, route confidence, closest alternative, unclassified residual, architecture necessity, and the distinguishing prediction. Separate corpus enrichment from core-design defects, label inference explicitly, and never copy source sentences as templates.

## Context discipline

Do not preload the full write-theory corpus. Finish paper-first extraction, then inspect only the exact rule targets and corpus files needed for comparison, persistence, or writeback.
