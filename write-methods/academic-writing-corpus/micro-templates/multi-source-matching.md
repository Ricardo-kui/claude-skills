---
category: multi-source-matching
description: 多数据源匹配叙述句法——描述如何将多个独立数据源交叉合并以构建分析样本。
function: 可审计性——让读者理解样本如何从多个原始痕迹中一步步构建出来
slots: M2
extracted_from: malik2025_jom / mayo2023_poms / singh2023_jmr
created: 2026-05-22
updated: 2026-05-22
---

# 多源数据匹配（Multi-Source Matching）

## 设计原则

当论文使用多个独立数据源（如 FDA + Compustat + Execucomp + BoardEx + Factiva）时，M2 的核心任务不是"排除步骤审计"，而是**数据源交叉逻辑**。需要清晰说明：每个数据源提供了什么变量、如何匹配、匹配键是什么、匹配后的样本量。

---

## 类型 1：多源获取总起句

**功能**：概括说明使用了多少个数据源及其各自用途。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We obtained [data type A] from [source A], [data type B] from [source B], and [data type C] from [source C].` | 安全 | M2 |
| `Our data come from [N] sources: [source A] for [variable set], [source B] for [variable set], and [source C] for [variable set].` | 安全 | M2 |
| `We matched these [observations] to [additional sources] to obtain [variables].` | 安全 | M2（已有主骨架） |

---

## 类型 2：逐源说明句

**功能**：逐个数据源说明其内容和用途。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Source A] data include [variable list: e.g., recall date, firm name, recall description text].` | 安全 | M2 |
| `[Source B] data include [variable list: e.g., firm name, CEO name, gender, start date].` | 安全 | M2 |
| `To examine [construct], we use the [database] database, which tracks [scope].` | 安全 | M2 |
| `Finally, to examine [additional construct], we sourced data directly from [agency] through [FOIA / data request].` | 安全 | M2 |

---

## 类型 3：匹配逻辑句

**功能**：说明如何将多个数据源匹配到一起。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The intersection of these data sources leads to a sample of [N] [units] that experienced [phenomenon] across [period].` | 安全 | M2 |
| `We matched [dataset A] to [dataset B] using [matching key: firm name / ticker / CUSIP] and [matching procedure].` | 安全 | M2 |
| `Because there is no common firm-level identifier between [source A] and [source B], we manually matched [entities] belonging to corresponding [units].` | 安全 | M2 |
| `We then matched these [observations] to [source C] containing [variables] to obtain [additional measures].` | 安全 | M2 |

---

## 类型 4：匹配后样本描述句

**功能**：报告匹配后的最终样本结构。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The intersection of these data sources leads to a sample of [N] [units] from [N] [higher-level units] across [period].` | 安全 | M2 |
| `Our final sample included [N] [observations] by [N] [units] led by [N] [actors] between [year_start] and [year_end].` | 安全 | M2 |
| `The matched sample consists of [N] [unit-years] with complete data for all variables of interest.` | 安全 | M2 |

---

## 类型 5：特殊数据获取句（FOIA/一手数据）

**功能**：说明非公开数据的获取方式。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We sought data directly from [agency] through the Freedom of Information Act regarding [variable].` | 安全 | M2 |
| `For companies present in [source A] but absent in [source B], we manually collected [data] from [source] filed with [agency].` | 安全 | M2 |
| `We downloaded all [documents] from [source] for the sample period and [processing step].` | 安全 | M2 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We used multiple data sources.` | 过于笼统，无法复现 | `We obtained recall data from CPSC, board data from BoardEx, CEO data from Execucomp, and firm financial data from Compustat.` |
| `The data were merged.` | 未说明匹配键和逻辑 | `We matched CPSC recall data to Compustat using firm name and year; the intersection resulted in 125 firms.` |
