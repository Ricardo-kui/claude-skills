---
type: canonical_stakes
canonical_id: "09-myopic-management-long-term-loss"
status: 🟡 EMERGING
gap_type: Incompleteness / Inadequacy
cross_paper: EMERGING (1p)
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - chung_low_rust_2022_jams (JAMS, 2022): "Myopic marketing management trades long-term value for short-term earnings; 0.22% or $22 million market value decline from interquartile CEO confidence increase"
created: 2026-07-08
updated: 2026-07-08
source: Distilled from Chung, Low & Rust (2022, JAMS)
---

# 09-myopic-management-long-term-loss — 短视管理侵蚀长期价值 Stakes

## 功能描述

在 Gap 建立之后，论证"短视管理行为"（myopic management）如何通过削减长期投资来美化短期财务指标，进而侵蚀企业长期价值。强调这种行为的双面性：短期看似"改善"业绩，实则损害未来增长能力。

## 适用场景

- 研究 DV 涉及短视管理行为（如削减营销、R&D、维护、培训支出以操纵盈余）
- 需要建立"短期收益 vs 长期损失"的 stakes
- 目标期刊重视经济显著性和实践相关性
- 常与 upper echelons、公司治理、盈余管理、营销战略研究相关

## 验证状态

### 跨论文复现
- **EMERGING (1p)**: chung_low_rust_2022_jams (JAMS)
- 待第二篇 exemplar 提升为 VERIFIED

### 生成力
- **ADAPTABLE**: "By [myopic action], firms trade [long-term asset] for [short-term metric]." 模板可迁移

### 排他性
- **MEDIUM**: 专用于短视管理/长期投资削减类研究

---

## 句法模板

### 变体 A：短期收益 vs 长期损失对比型

**模板**:
> "[Actors] often face pressure to meet short-term performance expectations. A common response is to [myopic action], which improves [short-term metric] in the current period but at the expense of [long-term asset] ([citations]). Such actions are considered 'myopic' because they trade off long-term performance for short-term gains, leading to declines in [long-term outcome] in the long run ([citations])."

**来源**: chung_low_rust_2022_jams (JAMS), P1

**原文锚定**:
> "CEOs who are under pressure for short-term performance often adjust their marketing budgets to manage their earnings numbers and meet performance expectations. Such actions are considered 'myopic' because they trade off long-term performance for short-term gains, leading to declines in market-based assets in the long run."

**关键特征**:
- 先说明短期压力和行为
- 用 "but at the expense of" 揭示 trade-off
- 用 "such actions are considered 'myopic'" 给出学术定义

---

### 变体 B：量化长期损失型

**模板**:
> "A back-of-the-envelope calculation suggests that an interquartile increase in [IV] leads to an expected decline of [percentage] or [$amount] in [long-term value measure] over [time horizon] through its effect on [DV]. This magnitude underscores that [myopic action] is not merely an accounting artifact but a substantive source of long-term value destruction."

**来源**: chung_low_rust_2022_jams (JAMS), Discussion section

**原文锚定**:
> "A back-of-the-envelope calculation shows that an interquartile increase in CEO confidence leads to an expected decline of 0.22% or $22 million in firm market value over the next few years through the increased likelihood of myopic marketing management."

**关键特征**:
- 用具体数字建立 stakes 的紧迫感
- 强调 DV 不是会计 artifact 而是价值破坏
- 适合在 Discussion 或 Introduction 末尾使用

---

### 变体 C：利益相关者连锁反应型

**模板**:
> "The consequences of [myopic action] extend beyond the firm itself. [Stakeholder group 1] suffer from [consequence 1] because [mechanism], while [stakeholder group 2] face [consequence 2] ([citations]). Understanding when and why [actors] engage in [myopic action] is therefore critical for both firm value and broader stakeholder welfare."

**关键特征**:
- 从企业价值扩展到利益相关者
- 适合有 CSR/ESG 或 stakeholder theory 元素的研究

---

## 组装规则

### 必须配对
- **与 `24-positive-trait-dark-side` (Hook) 配对**: 当 Hook 揭示正向特质的阴暗面时
- **与 `20-opposite-predictions-positive-trait` (Tension) 配对**: 当文献对正向特质预测矛盾时
- **与 `08-cost-vs-benefit` (Tension) 配对**: 当研究核心是成本-收益权衡时

### 互斥
- **不能与 `02-quantified-economic-loss` 同用**: 两者都量化经济损失，重复使用造成 stakes 冗余；若必须使用，选择其一并强调 long-term 维度
- **不能与 `08-goal-conflict` 同用**: 短视管理 stakes 是单向价值侵蚀，goal conflict 是双向目标冲突

### 反模式提醒
- **不要只描述行为而不量化后果**: 必须说明"长期损失"具体是什么
- **不要把 stakes 写成贡献**: stakes 是"不解决会损失什么"，贡献是"解决了能学到什么"
- **避免过度道德化**: 用 "trade-off" / "value erosion" 等分析性语言，而非 "unethical"

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 营销研究中 myopic management 是经典议题 |
| SMJ | ⭐⭐⭐⭐ | 战略研究中 short-termism 与公司价值关联紧密 |
| MS/POM | ⭐⭐⭐⭐ | 运营/供应链中也可使用（如维护削减、库存操纵） |
| AMJ | ⭐⭐⭐ | 需与理论重要性并行 |
| ASQ/OS | ⭐⭐ | 更偏好制度/理论后果而非纯经济后果 |

---

## 相关语料

- 配合 `hooks/24-positive-trait-dark-side.md` 使用
- 配合 `tensions/20-opposite-predictions-positive-trait.md` 使用
- 配合 `transitions/13-multi-actor-upper-echelons-funnel.md` 使用
