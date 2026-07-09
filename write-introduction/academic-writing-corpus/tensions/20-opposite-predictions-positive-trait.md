---
type: canonical_tension
canonical_id: "20-opposite-predictions-positive-trait"
status: 🟡 EMERGING
gap_type: Inadequacy
cross_paper: EMERGING (1p)
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - chung_low_rust_2022_jams (JAMS, 2022): "CEO confidence → R&D investment (long-term) vs CEO confidence → accrual earnings management (short-term) lead to opposite predictions for myopic marketing management"
created: 2026-07-08
updated: 2026-07-08
source: Distilled from Chung, Low & Rust (2022, JAMS)
---

# 20-opposite-predictions-positive-trait — 同一正向特质的两文献流做出相反预测

## 功能描述

在 Gap 段呈现：**同一正向高管特质**在不同文献流中推导出**方向相反的组织结果预测**。这不是简单的"文献有矛盾"，而是指出矛盾源于两流文献研究的是**不同但相关的决策情境**——因此需要一个针对目标情境的专门检验。

## 适用场景

- 同一 IV（通常是正向心理/人格/激励特质）在文献中既有长期主义预测，也有短期主义/机会主义预测
- 两类预测分别来自不同的理论传统或实证语境
- 目标情境（DV）与已有文献既有联系又有区别，值得单独研究
- 常见于 upper echelons、CEO 特质、公司治理、创业研究

## 验证状态

### 跨论文复现
- **EMERGING (1p)**: chung_low_rust_2022_jams (JAMS)
- 待第二篇 exemplar 提升为 VERIFIED

### 生成力
- **GENERATIVE**: "On the one hand... On the other hand... However, the contexts they examine... are quite different from that of [target DV]." 模板高度可迁移

### 排他性
- **MEDIUM**: 专用于同一正向特质的相反预测情境

---

## 句法模板

### 变体 A：两文献流相反预测 + 情境差异解释

**模板**:
> "The most closely related literature to the current paper comprises studies showing that [positive trait] leads to [long-term outcome A] ([citations]) and studies showing that [positive trait] increases [short-term/opportunistic outcome B] ([citations]). However, these two streams lead to opposite predictions of how [positive trait] would impact [target DV]. [Stream A] argues that [actors] high in [positive trait] are more bullish about the future and thus more willing to [long-term behavior]. This second stream of literature leads to a prediction opposite to that of [Stream B] — [actors] high in [positive trait] are less likely to engage in [target DV]. At first glance, both streams have merits. However, the contexts they examine, though somewhat related, are quite different from that of [target DV]. As such, how [positive trait] affects [target DV] deserves a separate careful examination."

**来源**: chung_low_rust_2022_jams (JAMS), Theory section

**原文锚定**:
> "The most closely related literature to the current paper are papers that show that CEO confidence leads to increased R&D spending (Galasso & Simcoe, 2011; Hirshleifer et al., 2012) and a higher propensity for accrual-based earnings management (Schrand & Zechman, 2012). However, these two streams of literature lead to opposite predictions of how CEO confidence would impact myopic marketing management."

**关键特征**:
- 明确指出两个文献流及其代表结果
- 用 "However" 揭示方向冲突
- 解释冲突不是因为某一文献错误，而是因为情境不同
- 以 "deserves a separate careful examination" 自然引出本文任务

---

### 变体 B：理论机制对比型

**模板**:
> "Two theoretical lenses offer conflicting predictions about the effect of [positive trait] on [target DV]. From a [theory A] perspective, [positive trait] signals [belief/state], leading [actors] to [long-term behavior] ([citations]). From a [theory B] perspective, the same [positive trait] inflates [actors]' perceived ability to [recover/justify], making them more willing to [short-term behavior] ([citations]). Because [target DV] differs from both [outcome A] and [outcome B] in [dimension], it remains an open question which effect dominates."

**关键特征**:
- 用理论视角而非文献流组织对立
- 强调两个机制都合理，但目标情境不同

---

### 变体 C：简洁矛盾引入型

**模板**:
> "Although [positive trait] is generally associated with [positive outcome], it is unclear whether this relationship extends to [target DV]. On the one hand, [positive trait] may [prediction 1] because [mechanism A]. On the other hand, [positive trait] may [prediction 2] because [mechanism B]. Resolving this tension is important because [stake]."

**关键特征**:
- 更短，适合作为 Gap 段第一句
- 直接陈述两种预测并引出 stakes

---

## 组装规则

### 必须配对
- **与 `24-positive-trait-dark-side` (Hook) 配对**: 当 Hook 已经建立了正向特质的阴暗面张力
- **与 `E 调节效应型` (Theory Variant) 配对**: 通常用调节机制解释哪种情境下哪个预测成立
- **与 `08-cost-vs-benefit` (Tension) 配对**: 若两种预测可归结为成本-收益权衡的不同侧面

### 互斥
- **不能与 `01-despite-progress-unaddressed` 同用**: 后者强调"已有进展但遗漏"，而本 Tension 强调"已有研究但矛盾"
- **与 `14-debate-unresolved` 的区别**: 后者是任意文献辩论，本 Tension 特指**同一正向特质**的相反预测

### 反模式提醒
- **不要只列矛盾而不解释来源**: 必须说明为什么两流文献会做出不同预测
- **不要贬低已有文献**: 要说 "contexts are different" 而非 "prior research is wrong"
- **不要停留在 "mixed results"**: 必须指向一个理论框架来调和矛盾

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| SMJ | ⭐⭐⭐⭐ | 战略研究中特质矛盾常见，适合理论调和 |
| AMJ | ⭐⭐⭐⭐ | OB/领导力研究中常用 "competing predictions" 结构 |
| JM/JMR | ⭐⭐⭐⭐ | 营销战略研究适配 |
| OS | ⭐⭐⭐ | 需更强的理论机制支撑 |
| ASQ | ⭐⭐⭐ | 偏好用理论视角而非文献流组织对立 |

---

## 相关语料

- 配合 `hooks/24-positive-trait-dark-side.md` 使用
- 配合 `transitions/14-nested-moderation-preview.md` 使用：当用多层调节来调和相反预测时
- 配合 `write-theory/corpus/subprotocols/B2_dual_track.md` 使用：同一构念双路径机制
