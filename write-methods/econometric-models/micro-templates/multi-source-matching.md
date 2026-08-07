---
category: multi-source-matching
description: 多数据源匹配叙述句法——描述如何将多个独立数据源交叉合并以构建分析样本。
function: 可审计性——让读者理解样本如何从多个原始痕迹中一步步构建出来
slots: M2
extracted_from: malik2025_jom / mayo2023_poms / singh2023_jmr / li_bapuji_talluri_singh_venkataraman_2026_pom / li_bapuji_talluri_singh_narayanan_2026_jscm
updated: 2026-08-06
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
| `In addition to [primary portal], we collected data from [N] other sources. First, ... Second, ... Third, ...` | 安全 | M2（li_venkataraman_2026_pom 型多源枚举） |
| `We transformed [addresses] into geocode data using [API A for region 1] and [API B for region 2].` | 安全 | M2（跨境 geocoding） |
| `We combined data from these different sources by [matching keys]. After removing observations with missing values ([N_removed] of [N_raw]), the final sample is [N_final].` | 安全 | M2 |

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

---

## 类型 6：七库合并 + 事件样本删样规则（li_narayanan_2026_jscm 型）

**功能**：多数据库枚举、显著事件阈值、以及 event-study 样本的逐条删样理由。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The panel data included merged data from [N] databases: (1) [source A] for [variables]; (2) [source B] for [variables]; ... (7) [source G] for [variables]. [Figure_reference] lists detailed steps for matching different datasets (with observations dropped in each step).` | 安全 | M2 |
| `Similar to previous studies ([citations]), this study included only significant [events] when [volume metric] is higher than a threshold ([X]% of [base]) because small-scale [events] are common in the [industry] and thus are not regarded as crises.` | 安全 | M2 |
| `It specifically focused on media-reported [events], matching each [regulatory record] with [news database] reports ([citation for news coverage]).` | 安全 | M2 |
| `For methodological considerations, observations were deleted when: (1) [confound rule 1]; (2) [confound rule 2 — e.g., confounding events in event window]; (3) [actor-type exclusion]; (4) [missing values on key variables].` | 安全 | M2 |
| `The period of study was from [year_start] to [year_end], to exclude the impacts of [macro shock A] and [macro shock B] on the [industry]. The final panel dataset contained [N_obs] observations based on [N_dyads] [dyad type] ([N focal actors] and [N partners]) of [N_events] media-reported major [events].` | 安全 | M2 |

**关键特征**:
- **七库编号枚举**：每库一行用途，与 Online Appendix 匹配流程图交叉引用
- **2% 阈值 + 媒体报告**：把"小召回不算危机"操作化为可复现规则，并说明 RavenPack 区分 media-reported vs 未报道
- **四条删样规则**：同日多 buyer 召回、事件窗混淆事件、金融/OEM 供应商、缺失值——每条对应一种识别威胁

**适用**: 事件研究 + dyad 面板；召回/危机溢出；多库 secondary data；JSCM/JOM/MSOM

**禁忌**:
- 删样规则须在 Methods 预告、Appendix 给逐步 N——不能只报最终 N
- 阈值须引用先例（Gao et al.; Javadinia et al.）或论证行业特异性
- 不要把 media-reported 筛选说成 exogenous——须在 Limitations 承认报道选择
