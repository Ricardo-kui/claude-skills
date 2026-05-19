---
design_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
variants_count: 3
created: 2026-05-18
updated: 2026-05-20
---

# IV-2SLS — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 填空段落骨架 → `IV-2SLS`。

## 设计特征摘要

- **核心估计器**: Two-stage instrumental variable (IV) regression: 2SLS for continuous DV, IV-Probit/IV-Tobit/IV-Poisson for limited DV
- **识别策略**: 工具变量必须满足 relevance (与内生变量相关) 和 exogeneity/exclusion (仅通过内生变量影响DV) 两个条件
- **工具变量来源**: 外部IV (自然实验/政策冲击) 或 内部IV (Lewbel 2012 heteroskedastic identified instrument)
- **诊断检验链**: Partial F-statistic (relevance), Sargan/Hansen J-test (overidentification), Andrews identification test, Pagan-Hall/Breusch-Pagan (Lewbel-specific)
- **适用场景**: 内生性威胁严重(omitted variable / simultaneity / measurement error)且可找到有效IV的研究
- **跨论文复现率**: 1/5 产品召回论文 (Wowak2025)；传统IV在 Eilert2017 Control Function 中有间接应用

## 累积变体

### 变体 1: Lewbel (2012) Heteroskedastic Identified Instrument 三步法
**来源论文**: Wowak2025 MS
**验证状态**: 通过 (1/5 产品召回，但方法泛用性极高)
**写入日期**: 2026-05-20
**槽位**: M7
**骨架**:
> To address this challenge [of finding valid external instruments], we use an IV approach that has emerged from the econometrics literature called the heteroskedastic identified instrument technique. This technique, which has recently been adopted in [domain] research ([citations]), is designed to accommodate a setting "when no external instruments or other such information are available" ([citation], [page]). This procedure allows us to generate valid instruments via three steps ([citations]). First, we use the potentially endogenous independent variable ([IV]) as the dependent variable in a first-stage equation that features all our controls as regressors. Just as [citation] theorized and [citation] emphasize, we include all of our control variables as the regressors in this first-stage equation because doing so is the preferred specification, unless including a subset of the controls better upholds the assumptions of the model. In the second step, the technique calculates the residuals associated with each of those control variable regressors and transforms the heteroskedasticity into potentially valid IVs, but only when the assumptions of the model that we detail next are exhibited ([citations]). Finally, we incorporate the valid generated instruments into the two-stage IV fixed effects estimators.
**与原骨架差异**: 传统 IV-2SLS 要求研究者找到外部工具变量(如政策冲击、自然实验)，而 Lewbel 方法从第一阶段的**异方差残差**中内部生成有效IV。三步法核心：(1) 所有控制变量回归内生变量；(2) 残差异方差→有效IV；(3) 生成的IV纳入第二阶段。诚实边界：Lewbel 方法依赖于两个关键假设(见变体2)，若不满足则生成的IV无效。适用于"无外部IV可用"的情境。

### 变体 2: IV 有效性诊断链完整报告 (Lewbel + 传统诊断)
**来源论文**: Wowak2025 MS
**验证状态**: 通过 (1/5 产品召回，IV研究的必写段落)
**写入日期**: 2026-05-20
**槽位**: M7/M8
**骨架**:
> Scholars indicate that the heteroskedastic identified instrument procedure can generate valid instruments under two assumptions ([citations]). First, [citation] note that the instruments generated from the heteroskedastic identified technique must not be correlated with the covariance in the error terms from the first and second stage equations. Just as [citation] prescribe, [citation, p. X] emphasize that this assumption is upheld by "failing to reject homoskedasticity with respect to [the first-stage regressors]" via the [test_name] test. For our data, the [test_name] diagnostic [test_result] ([test_stat]=[value]; p=[threshold]), thereby adhering to this first assumption. Second, [citation] state that the generated instruments must be meaningfully correlated with the endogenous independent variable. In line with [citation], [citation, p. X] argue that this assumption can be supported when scholars "reject homoskedasticity with respect to the selected [regressors]" via the [test_name] test. Our variables uphold this condition by [test_result] ([test_stat]=[value]; p < [threshold]), thus adhering to this second assumption.
>
> It is worth underscoring that our generated instruments also conform to the traditional diagnostic tests pertaining to relevance and exogeneity for any type of IV. Indeed, the partial F-statistic exceeds the thresholds that scholars suggest represent relevance (partial F-stat = [value]; p < [threshold]), and the [identification_test] from [citation] does not contain zero [[lower], [upper]], reflecting relevant instruments ([citation]). Similarly, diagnostic tests for exogeneity suggest our instruments are unrelated to the structural error terms pertaining to [DV_1] (Sargan χ² = [value]; p = [threshold]) and [DV_2] (Sargan χ² = [value]; p = [threshold]), indicating that our instruments are not endogenous ([citation]). Taken together, our instruments appear to be properly identified and valid.
**与原骨架差异**: 这是 IV-2SLS 的**完整诊断报告模板**。关键要素：(1) Lewbel 假设1: Pagan-Hall 不拒绝 homoskedasticity → 生成的IV与误差协方差无关；(2) Lewbel 假设2: Breusch-Pagan 拒绝 homoskedasticity → 生成的IV与内生变量相关；(3) 传统 relevance: partial F > 10；(4) 传统 identification: Andrews 区间不含0；(5) 传统 exogeneity: Sargan 不拒绝 → IV外生。适用于任何IV研究——传统IV替换前两个测试为 Wu-Hausman / Cragg-Donald。**诚实边界**: 若任何测试未通过，相应的IV无效，需重新选择工具变量。

### 变体 3: 政治意识形态操作化 — 四步四指标聚合流程
**来源论文**: Wowak2025 MS
**验证状态**: 可选变体 (1/5，政治意识形态研究特有)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> [IV] is calculated as the [aggregation_method] [annual] [construct] across members of a firm's [group] ([citations]). To compute this measure, we carefully followed the procedure documented in [domain] research ([citations]). We first used [source] to identify the [group_members] in each organization ([citations]). Next, we identified each [member]'s [construct] by accessing [data_source] from [database]. Using the [data], we then calculated [N] indicators that have been shown to collectively reflect [construct] ([citations]): (1) [indicator_1]; (2) [indicator_2]; (3) [indicator_3]; and (4) [indicator_4]. Each indicator ranges from [min] to [max]; [max] represents [pure_form], [min] represents [opposite_form]. Following research precedence, we [aggregation] the indicators ([citations]), as they demonstrate high reliability and internal consistency (α=[value]). In line with this literature, we assign a score of [neutral_value] to individuals with no [data], indicating that they are [neutral_label] ([citations]). That said, in robustness checks we remove [missing_data_group] from our sample and demonstrate that assigning a value of [neutral_value] to them does not meaningfully influence our results.
**与原骨架差异**: 政治意识形态的**标准操作化流程**——从 Chin et al. (2013) 确立的四个政治捐赠指标到均值聚合。关键要素：(1) 四指标全覆盖（捐赠数量比/金额比/候选人比/年份比）；(2) 高内部一致性引用 (α=0.95)；(3) 非捐赠者处理策略 (赋中性值0.5 + 排除稳健性检验)；(4) 每句都有方法论引用链。该骨架可迁移至任何使用 FEC/Open Secrets 政治捐赠数据的研究（CSR、公司创业、高管薪酬等）。
