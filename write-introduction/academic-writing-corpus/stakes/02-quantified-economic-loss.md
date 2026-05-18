---
type: canonical_stakes
canonical_id: "02-quantified-economic-loss"
status: ✓ STANDARD
gap_type: Incompleteness / Inadequacy
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - ceo_regulatory_focus_ijrm (IJRM, 2021): "$79bn foregone earnings; Warren Buffett call for action"
  - malshe2015 (JM, 2015): "economically significant: $26 million loss per 1-SD leverage increase"
  - darby2024 (MSOM, 2024): "stock market penalties for recall delays"
created: 2026-05-18
source: Extracted from MVP30 narrative_analysis files
---

# 02-quantified-economic-loss — 量化经济损失 Stakes

## 功能描述

在 Gap 建立之后，用具体的数字量化"如果不解决这个研究问题会造成的经济损失"。这是管理学期刊中最常用、最有效的 Stakes 类型——它直接回答"so what"的经济版本。与 `07-reputation-legitimacy-crisis` 的区别：本模块聚焦于可量化的财务/市场后果，而非声誉/制度层面的后果。

## 适用场景

- 研究含市场/财务结果（ROA、托宾Q、股价反应、现金流）
- 研究含可量化的管理成本（广告支出浪费、召回成本、客户流失成本）
- 目标期刊偏好经济显著性（JM, JMR, IJRM, MSOM；SMJ/AMJ 次之）
- 需要说服读者这个问题有"真金白银"的后果

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): ceo_regulatory_focus_ijrm (IJRM), malshe2015 (JM), darby2024 (MSOM)

### 生成力
- **ADAPTABLE**: 量化逻辑高度可迁移，但具体数字需要真实数据支撑

### 排他性
- **MEDIUM**: 跨 Gap 类型可用，在管理/营销/运营期刊中更常见

---

## 句法模板

### 变体 A：成本量化+权威呼吁型（ceo_regulatory_focus_ijrm 型）

**模板**:
> "Such [behavior/phenomenon] has led to an estimated $[cost] in [foregone outcome] over [time period] and has prompted [prominent figure] to call for [action]."

**来源**: ceo_regulatory_focus_ijrm (IJRM), P2

**原文锚定**:
> "Such short-term decision-making has led to an estimated $79bn in foregone annual earnings over the period 1996 to 2018 at S&P 500 firms and has prompted prominent business leaders such as Warren Buffett to call for a greater focus on long-term sustainable value creation."

**关键特征**:
- 具体金额（$79bn）+ 时间段（1996-2018）+ 受影响群体（S&P 500）
- 权威人物（Warren Buffett）增加号召力
- 从成本量化自然过渡到"需要行动"

---

### 变体 B：经济显著性锚定型（malshe2015 型）

**模板**:
> "The impact is economically significant: [quantification of effect size in dollar terms]. This is especially meaningful when [baseline comparison]. Without understanding [mechanism], [actors] are likely to [overestimate/underestimate] [outcome], especially in firms with [condition]."

**来源**: malshe2015 (JM), P3

**原文锚定**:
> "The impact of leverage on satisfaction is economically significant: a one-standard-deviation increase in leverage from the average level results in a .47 point decrease in customer satisfaction, which is equivalent to an estimated loss of $26 million in net operating cash flows."

**关键特征**:
- 用 "one-standard-deviation increase" 建立 effect size 的直观感受
- 将统计效应转化为具体金额
- "This is especially meaningful when..." 将量化锚定到实际管理决策

---

### 变体 C：市场惩罚型（darby2024 型）

**模板**:
> "We find that [behavior] significantly magnifies the [market penalty], with [quantified consequence]. The consequences extend beyond [immediate outcome] to [broader outcome], affecting [stakeholders]. Moreover, no studies of which we are aware have examined [specific financial consequence]."

**来源**: darby2024 (MSOM), P6

**原文锚定**:
> "We find that delaying the initiation of a recall significantly magnifies the stock market penalty... Moreover, no studies of which we are aware have examined the stock market implications of time-to-recall."

**关键特征**:
- "significantly magnifies" → 不只说"有影响"，说"放大惩罚"
- 区分直接后果（recall costs）和市场后果（stock penalty）
- "no studies of which we are aware have examined" → 谨慎但明确的缺口确认

---

## 组装规则

### 必须配对
- **必须在 Gap 之后出现**: Stakes 是缺口重要性的论证，不能前置
- **与具体数字的真实性绑定**: 不能编造数字；必须来自可引用的来源（CSO survey, McKinsey report, prior research data）

### 互斥
- **不能与 `03-data-shock` (Hook) 同用**: 功能冗余——两者都用数字建立震撼力；数字疲劳会削弱两者效果
- **不能与 `07-reputation-legitimacy-crisis` (Stakes) 同用**: 经济损失是效率逻辑，声誉危机是制度逻辑，重复使用造成 stakes 冗余

### 反模式提醒
- **不要编造或模糊化数字**: 如果没有精确数据，用范围（"estimated $X–$Y billion"）或引用已有研究的数据，而不是"billions of dollars"
- **不要把 stakes 写成贡献**: Stakes 是"不解决会损失什么"，贡献是"解决了能学到什么"
- **经济显著性应与统计显著性分离**: "economically significant" ≠ "statistically significant"

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐ 极高 | 经济显著性在 Intro 中报告是 JM/JMR 的标准预期 |
| IJRM | ⭐⭐⭐ 极高 | 偏好成本量化+权威呼吁组合 |
| MSOM/POM | ⭐⭐⭐ 高 | 偏好市场惩罚/运营成本量化 |
| SMJ | ⭐⭐ 中 | 可接受但不过度强调；偏好战略后果而非纯财务数字 |
| AMJ | ⭐⭐ 中 | 需与理论重要性并行，不能只有经济数字 |
| ASQ | ⭐ 低 | 纯经济 stakes 与 ASQ 理论导向不匹配 |
