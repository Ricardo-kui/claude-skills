---
design_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): natural-disaster instrument + 3-reason exclusion restriction (external-event-as-IV template)"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): Durbin-Wu-Hausman test + Gaussian copula endogeneity narrative"
variants_count: 5
created: 2026-05-18
updated: 2026-07-08
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

### 变体 4: 外部自然事件作工具变量 + 三因排除限制论证 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**验证状态**: 通过 (单篇高价值，"外部自然事件→非正式关系"工具变量论证的稀缺范式)
**写入日期**: 2026-06-16
**槽位**: M8
**骨架**:
> An important consideration is that [actors] might self-select whether they [form the focal tie / take the treatment], creating an endogeneity issue. Furthermore, comparing the reduced-form [DV] model with the [mediator-included] model, Shaver ([2005]) suggested the reduced form may be mis-specified due to an omitted [mediator/endogenous regressor], and recommended an instrumental variable analysis. We focused on [an exogenous external / natural event — e.g., natural disasters in the actor's home market] as an instrumental variable. First, [the event] is exogenous, reflecting "nature's fury" ([citations]), and is not affected by [the outcome]. Second, [the event] might expose limitations of formal institutions (e.g., written rules and regulations) for acquiring strategic resources from the state, requiring [actors] to seek informal means—such as [forming the focal tie] ([citations]). Third, the existing [outcome] literature suggests that [actors] typically base [the outcome] on [alternative determinants: e.g., distance, host-market institutions, demand, own capabilities]; [the event], hence, may predict [the treatment] but have a limited effect on [the outcome] directly ([citation]). So, the instrument may satisfy exclusion-restriction conditions. We obtained data on [the event] from [source] and used it as an instrument.
**与原骨架差异**: 与变体 1–3（Lewbel 内部生成 IV）的根本区别——本变体用**外部自然/准自然事件**作 IV，且排除限制通过**三层论证**建立：(1) 事件外生性（"nature's fury"，不受结果影响）；(2) 事件→处理的渠道（制度缝隙逻辑：正式制度失效→寻求非正式关系）；(3) 事件→结果的直接渠道**缺失**（由结果文献的已知决定因素反推）。第（2）层是核心理论增量——IV 通过"挤压正式资源获取"间接推动处理。诚实边界：第（3）层"无直接渠道"是排除限制的关键假设，本质不可检验，必须用结果领域文献的既有发现支撑，不可断言。适用于 IV 通过"制度/资源缝隙"推动企业形成非正式关系（政治关联、军方关联、银企关系）的研究。配合 control-function 报告见 `write-results/IV-2SLS.md` 变体 4。

### 变体 5: M8 Durbin-Wu-Hausman (DWH) Test + Gaussian Copula 内生性叙事 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M8
**骨架**:
> Our hypothesis builds on the premise that [IV] is exogenous to [DV]. However, endogeneity such as that arising from omitted variables and reverse causality may bias our estimates. To address omitted variables issues, we have controlled for many possible variables that might affect [DV]. Nevertheless, it is possible that unobservable omitted variables, such as [example], may affect both [IV] and [DV]. We examine the effects of unobservable [unit]-specific omitted variables in a model that incorporates [unit] fixed effects. The [unit] fixed effects control for any time-invariant omitted variable that might affect [DV] and [IV], and thus control for heterogeneity across [units] that are time-invariant ([citation]). However, [unit] fixed effects cannot address issues relating to reverse causality and time-varying omitted variables. Therefore, to further address endogeneity concerns, we conduct the Durbin-Wu-Hausman (DWH) test ([citations]). Similar to our exclusion restriction, we use the average [IV] of peer firms operating in the same industries as the focal firm as an instrument for [IV]. For the results of the DWH test to be useful, the instrument needs to be relevant and strong ([citation]). Peer [IV] significantly predicts focal [IV] with [t-statistic] and p-value [p]. The partial R-squared of excluded instruments is [value] with an F-statistic of [F], which is above the rule-of-thumb cutoff of 10 for weak instruments ([citation]) and also above all of the Stock and Yogo ([citation]) critical values. The Chi-sq test statistic for the DWH test is [value] (p-value = [p]), indicating [no/some] evidence of endogeneity. To further substantiate the case of [no] endogeneity, we also use the instrument-free Gaussian copula joint estimation method ([citation]) and reach similar conclusions.
**与原骨架差异**: 完整的"DWH 检验 + Gaussian copula"内生性叙事。关键要素：(1) 遗漏变量与反向因果的双重威胁；(2) [unit] FE 处理时不变遗漏变量；(3) 同行 [IV] 作为工具变量及其相关性诊断（F-statistic、Stock-Yogo）；(4) DWH 结果解释（能否拒绝内生性原假设）；(5) Gaussian copula 作为无工具变量替代方法提供三角验证。适用于面板 OLS 研究中核心 IV 潜在内生性但又不存在强外部 IV 的情境。
**诚实边界**: DWH 检验的功效依赖于 IV 强度；若 IV 弱或 DWH 不显著，不能断言无内生性。Gaussian copula 对分布假设敏感，应在稳健性中报告敏感性分析。
**跨 skill 对齐**: `write-results/OLS-FE.md` 变体26（R7 内生性稳健性表叙事 — threat-by-threat Table 7 汇总）。
