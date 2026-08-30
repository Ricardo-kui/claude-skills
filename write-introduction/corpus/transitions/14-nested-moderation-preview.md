---
type: canonical_transition
canonical_id: "14-nested-moderation-preview"
status: EMERGING
function: "在 Introduction 末尾预览从 two-way 到 three-way 的嵌套调节结构"
cross_paper: EMERGING (1p)
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - chung_low_rust_2022_jams (JAMS, 2022): "CMO confidence moderates CEO confidence; CMO power amplifies CMO confidence; board independence exacerbates CEO confidence; CMO confidence tempers board effect"
created: 2026-07-08
updated: 2026-07-08
source: Distilled from Chung, Low & Rust (2022, JAMS)
---

# 14-nested-moderation-preview — 嵌套调节结构预览过渡

## 功能描述

在 Introduction 末尾或 Theory 引入段，用**一句话/一小段预览研究的嵌套调节结构**：先建立主效应，再说明第一层调节（two-way），最后引出第二层嵌套调节（three-way）。帮助读者在密集的理论展开前建立路线图。

## 适用场景

- 研究包含三向交互或序列嵌套调节
- 需要让读者提前知道调节结构的层次关系
- 适合 upper echelons、TMT、公司治理、营销战略中多层边界条件研究

## 验证状态

### 跨论文复现
- **EMERGING (1p)**: chung_low_rust_2022_jams (JAMS)
- 待第二篇 exemplar 提升为 VERIFIED

### 生成力
- **GENERATIVE**: "We expect [moderator 1] to [buffer/amplify] the [X]→[Y] relationship; moreover, this [buffering/amplifying] effect is itself [strengthened/weakened] by [moderator 2]." 模板可迁移

### 排他性
- **HIGH**: 专用于嵌套调节/三向交互研究

---

## 句法模板

### 变体 A：从主效应到三向交互的完整预览

**模板**:
> "We propose that [IV] [increases/decreases] [DV] because [short mechanism]. We then theorize that this relationship is [buffered/amplified] by [moderator 1], such that [prediction for two-way]. Furthermore, we argue that the [buffering/amplifying] effect of [moderator 1] is itself [strengthened/weakened] when [moderator 2] is [high/low], leading to a three-way interaction. Finally, we examine how [moderator 3] shapes these dynamics, and whether [lower-level actor characteristic] can counteract [moderator 3]'s [amplifying/buffering] effect."

**来源**: chung_low_rust_2022_jams (JAMS), P2-P3

**原文锚定**:
> "We expect this persuasive role to be most effective when the CMO displays high confidence in their judgment and ability to extract value improvement from their marketing recommendations. We further model how the board of directors, being the top decision-making body in a firm, affects the myopic marketing tendencies of the confident CEO through its intensive monitoring."

**关键特征**:
- 每一层都有明确的机制关键词
- 用 "Furthermore" / "Finally" 标示结构层次
- 不展开具体理论，只给路线图

---

### 变体 B：研究问题串型

**模板**:
> "Our study addresses four related questions. First, does [IV] affect [DV]? Second, does [moderator 1] moderate this relationship? Third, is the moderating effect of [moderator 1] contingent on [moderator 2]? Fourth, can [lower-level actor] offset the [amplifying/buffering] effect of [moderator 3]? By answering these questions, we provide a more nuanced understanding of [phenomenon]."

**关键特征**:
- 用编号问题清晰展示嵌套结构
- 适合在 Introduction 末尾作为过渡

---

### 变体 C：表格/图预览型

**模板**:
> "Figure [N] summarizes our conceptual model. The model begins with the direct effect of [IV] on [DV] (Path A). It then adds [moderator 1] as a first-layer boundary condition (Path B) and [moderator 2] as a second-layer nested boundary condition (Path C). The right-hand side of the model captures how [moderator 3] and [lower-level actor] jointly shape the [IV]→[DV] relationship (Path D). We develop each path below."

**关键特征**:
- 配合概念模型图使用
- 用 Path A/B/C/D 给读者清晰的视觉锚点

---

## 组装规则

### 必须配对
- **与 `13-multi-actor-upper-echelons-funnel` (Transition) 配对**: 当多层级与嵌套调节结合时
- **与 `write-theory/corpus/variants/E_moderation.md` 配对**: E3/E6 子协议用于三向交互理论展开
- **与 `write-results/corpus/三向交互.md` 配对**: 结果报告的三向交互变体

### 互斥
- **不要在没有三向交互的研究中使用**: 如果只是 two-way 调节，用普通的 moderation preview 即可
- **不要过度展开理论**: 这是预览，具体机制留给 Theory 部分

### 反模式提醒
- **不要堆砌调节器而无层次**: 每个调节器必须说明其层级功能
- **不要混淆调节方向**: 预览中必须明确 buffer vs amplify
- **不要忘记 lower-level actor 的劝说角色**: 在 upper echelons 情境中，三向交互常涉及权力/劝说不对称

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| SMJ | ⭐⭐⭐⭐⭐ | 复杂调节结构是战略研究常态 |
| AMJ | ⭐⭐⭐⭐ | TMT 互动中常用 |
| JM/JMR | ⭐⭐⭐⭐ | 营销战略研究适配 |
| OS | ⭐⭐⭐ | 需清晰的理论层次 |
| ASQ | ⭐⭐⭐ | 通常更简洁， previews 不宜过长 |

---

## 相关语料

- 配合 `transitions/13-multi-actor-upper-echelons-funnel.md` 使用
- 配合 `write-theory/corpus/subprotocols/hypothesis_derivation_patterns.md` 中的 sequential nested moderation 模式使用
