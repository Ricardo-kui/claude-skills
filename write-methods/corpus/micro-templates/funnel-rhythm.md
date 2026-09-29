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


**补充句式（westphal_bednar2005 型）：样本框三理由枚举辩护**
> We chose this sample frame for three reasons: (1) to exploit [a large database of unit-level information] provided by [source], which covers [population feature]; (2) to improve [the response rate], which would likely be lower for [alternative population]; and (3) to enhance our knowledge of [phenomenon] among an understudied population of [units].
- 三理由的标准组合：数据可得性 / 数据收集可行性（响应率）/ 研究缺口（understudied population 的贡献声明）——第三点把抽样决策升格为对外部效度的正面论证
- "for three reasons: (1)...(2)...(3)..." 枚举结构可直接迁移到任何一手数据设计的样本框辩护段

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


## 微模板：响应率工程链（carpenterwestphal2001 型）

| 步骤 | 句式 | 抗辩点 |
|------|------|--------|
| 反差定位 | `Although surveys have been used frequently to measure [behavioral processes] at [lower levels], surveys of [elite respondents] have often suffered from low response rates (less than [25] percent).` | 用先例反差预设威胁（基层常用 vs 精英低响应） |
| 承诺句 | `To ensure the highest possible response in this case, we took the following steps ([methodology citations]):` | 承诺 + 方法论文献背书 |
| 编号步骤 | `(1) [an in-depth pretest was used to streamline the survey, making it easier and more appealing to complete]; (2) [requests for participation linked the current study with an ongoing series of surveys ... to which hundreds of these respondents' peers had responded]; and (3) [about N days after the initial mailing, nonrespondents were sent a second letter with a new questionnaire]` | 每步自带 because：减负 / 机构背书借同行先例 / 催复附新问卷 |
| 对标收口 | `These response rates are high in comparison to those of other [elite] surveys (cf. [citation]).` | 报数字 + 与同类调查对标，闭合链条 |
- 适用：top-management / 精英样本问卷；普通消费者样本不需要此链
- 收口后必须衔接漏斗下一步（数据缺失排除 → 最终 N），使响应率工程成为漏斗叙事的一部分而非孤立抗辩

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:m2_response_rate_engineering_chain -->


## 微模板：抽样框威胁三理由反驳（dewan_jensen2020 型）

> "A potential limitation of this approach is that [frame threat], a threat particularly relevant for [focal subgroup] because of [incentive] ([citations]). We are less concerned with [the threat] in our context for three reasons. First, [institutional change] has significantly reduced [the threat's prevalence] ([citations]). Second, the distribution of [focal variable] among [units] follows [the expected shape] typical of [the population structure] (e.g., [citations]). Similarly, the distribution of [focal variable] follows [the expected shape] both for [units whose frame membership might signal the threat] and for [units where it does not]. It indicates that [the threat] is not primarily determined by [focal variable]. Third, we take the possibility of [the threat] into account by controlling for several [threat-relevant characteristics] in our analysis. And we conduct several robustness checks such as [dropping the suspect subsets] (see Table [X]). The results do not change, which suggest that our results are unlikely to be biased by [the threat against the focal subgroup]."

- 与「样本框三理由枚举辩护」（westphal_bednar2005）互为镜像：那边枚举**选框的好处**（合法性论证），这边反驳**框的威胁**（抗辩性）。三理由的标准组合：制度层（规则/环境变化压缩威胁空间）→ 分布层（威胁的特征签名在数据中不存在：威胁若由 [focal variable] 驱动，其分布应在 [suspect subset] 中变形，实际对称）→ 分析层（controls + robustness 实际处理）。
- "It indicates that [the threat] is not primarily determined by [focal variable]" 是分布检验的解释句——把一个描述性分布观察转成"威胁不成立"的推断，衔接第二理由到第三理由。
- 位置纪律：此反驳紧跟抽样框定义段（frame 声明后立刻预判最可能的攻击），不要推迟到 limitations；robustness 结果可用 "The results do not change" 一句预收口 + 表格指针。

<!-- wb:dewan_2020_catching_the_big_fish_the_role_of_scandals_in_mak:m2_sampling_frame_threat_rebuttal_triad -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


## 微模板：流失 t 检验诚实报告链（dewan_jensen2020 型）

> "We performed [t-tests] (on the available data) to compare the [dropped units] with the [units] used in the analysis. The main reason for missing data are the [variable families], and there are statistically significant differences between the two samples on all variables of interest besides [exception variable]. To mitigate the concern of missing data, we performed several robustness checks that are reported following the main results."

- 反直觉的诚实点：**报告显著差异而非隐藏**——"statistically significant differences ... on all variables of interest besides [exception]" 直接承认流失非随机，随即给出缺失主因归因（[variable families]）与处置承诺（robustness checks + 位置指针）。
- 三步链：比较检验 → 缺失机制归因 → 稳健性预告。比 "dropped due to missing data" 式静默排除多出可审计性与威胁处置两层；"(on the available data)" 括号声明连比较本身的数据边界都交代了。
- 适用：档案多库合并中因数据可得性排除 10%+ 观测、且排除组与保留组可观测特征有差异的场景；与 robustness-foreshadowing（样本选择类）配合使用。

<!-- wb:dewan_2020_catching_the_big_fish_the_role_of_scandals_in_mak:m2_attrition_ttest_honest_reporting_chain -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


## 微模板：最终样本可比性对标收口（javadinia_2024 型）

**功能**：漏斗走完后的最终样本，用同行研究样本量对标收口，把"样本小"的质疑前截。

**骨架**：
[Our final sample used to test the hypotheses consists of [N] [events] and is comparable to those used in previous studies. For example, [Study A] had a sample of [N_A] [events], [Study B] [N_B] [events], and [Study C] [N_C] [events].]

**关键句法**：① 收口句一拍完成——最终 N + "comparable to previous studies"；② 3–4 个同行研究的样本量枚举背书（每项带引用）。

**适用/禁忌**：适用——小样本档案事件研究（漏斗尾部 N 偏小）；禁忌——样本量大或有明确代表性论证时多余。

**原文锚点**："Our final sample used to test the hypotheses consists of 148 automobile safety recalls and is comparable to those used in previous studies."

<!-- wb:javadinia_2024_recall_environment_and_post_recall_stock_mark:m2_final_n_comparability_closure -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
