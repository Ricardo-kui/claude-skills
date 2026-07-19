---
category: funnel-rhythm
description: 样本漏斗节奏——数字叙事的句法序列，让读者可以复现样本选择。
function: 可审计性——起始 N → 每步排除（理由+数字）→ 最终 N 的完整链条
slots: M2
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 样本漏斗节奏（Funnel Rhythm）

## 核心原则

样本漏斗不是列表，而是**叙事**。审稿人通过这个数字故事来判断：
1. 样本选择是否合理？
2. 数据损失是否过大？
3. 每一步是否有正当理由？

## 标准四步节奏

```
起始总体 → 匹配/合并 → 逐步排除 → 最终样本
```

## 微模板：起始总体

| 句式 | 风险 | 适用情境 |
|------|------|---------|
| `We began with [starting population] from [source] over [period].` | 安全 | 通用 |
| `Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [activity].` | 安全 | 自然实验/DiD |
| `The intersection of these datasets resulted in a sample of [N] [phenomenon] across [N] firms from [year_start] to [year_end].` | 需注意 | 多源匹配（缺少起始 N） |
| `No authoritative database exists for [object], so we constructed the dataset from [trace/source].` | 安全 | 实证对象构建 |

## 微模板：匹配/合并

| 句式 | 风险 | 适用情境 |
|------|------|---------|
| `We matched these observations to [additional sources] to obtain [variables].` | 安全 | 通用 |
| `We then linked [actor C characteristics] from [source C].` | 安全 | 多行为者设计 |
| `After propensity-score matching (described below), we estimate...` | 安全 | PSM |

## 微模板：逐步排除

| 句式 | 风险 | 适用情境 |
|------|------|---------|
| `We excluded [cases] because [reason].` | 安全 | 通用 |
| `We also excluded firms with fewer than [N] years of consecutive data to ensure sufficient within-firm variation.` | 安全 | 面板数据 |
| `Because testing [moderation] requires [additional source], the sample for H[x] is restricted to [available period/units].` | 安全 | 子样本 |
| `We dropped observations with missing [variable] because [reason].` | 安全 | 缺失值处理 |
| `To reduce selection bias, we first estimate propensity scores using [model] with [covariates]...` | 安全 | 匹配前筛选 |

**关键数字审计链格式**：
```
Of the [N] initial [units], [N] were excluded due to [reason_1],
[N] due to [reason_2], and [N] due to [reason_3],
resulting in a final sample of [N] [unit-years / observations].
```

## 微模板：最终样本

| 句式 | 风险 | 适用情境 |
|------|------|---------|
| `The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.` | 安全 | 通用 |
| `The matched sample consists of [N] [unit-years / dyads / firms].` | 安全 | 匹配后 |
| `The final analytic sample consists of [N] [dyads / triads / observations] in which [inclusion condition].` | 安全 | 多行为者设计 |

---

## 完整漏斗叙事示例（面板数据-OLS）

```text
We began with all publicly traded manufacturing firms from Compustat
North America over 2010–2020. We matched these observations to
Harte-Hanks CI Technology Database to obtain IT expenditure data
and to NBER Patent Database to obtain patent filings.

Of the 12,450 initial firm-year observations,
  1,230 were excluded because they are financial firms (SIC 6000–6999)
    or utilities (SIC 4900–4999),
  890 were excluded due to missing R&D expenditure data,
  and 450 were excluded because they have fewer than three consecutive
    years of data needed for fixed-effects estimation.

The final sample consists of 9,880 firm-year observations
from 1,247 unique firms.
```

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We excluded missing values.` | 无数字、无理由 | `We dropped 890 observations with missing R&D expenditure because [reason].` |
| `The final sample is large.` | 无起始 N，无法审计 | 提供完整的起始→最终 N 链条 |
| `Data come from multiple sources.` | 无匹配逻辑 | `We matched [source A] to [source B] using [key], yielding [N].` |
| 只有最终 N，无中间步骤 | 无法判断数据损失是否合理 | 至少报告主要排除步骤的数字 |
