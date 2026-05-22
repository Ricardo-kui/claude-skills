---
design_type: IV-2SLS
status: VERIFIED
source_papers:
- wowak2025_tmt_political_ideology_ms
- singh_grewal2023_lobbying_recalls_jmr
variants_count: 6
created: 2026-05-18
updated: '2026-05-22'
---

# IV-2SLS — Methods 骨架

## 设计特征摘要

<!-- 由 distill-methods-exemplar 首次蒸馏后填充 -->

## M1. 研究情境 / 实证背景

### 主骨架（通用）
： ⭐ PREMIUM（28/28 篇范文使用，跨所有模型类型复现）

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

---

## M2. 数据来源与样本漏斗

### 主骨架（通用）
：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

---

## M3. 因变量

### 主骨架（通用）
：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

---

## M4. 自变量 / 核心预测变量

### 主骨架（通用）
：

```text
Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].
```

### 变体 1: 工具变量三级论证（Relevance → Exclusion → Empirical Validity）
： ✓ STANDARD（IV 设计必写模块）

```text
Our focal independent variable, [predictor name], may be endogenous because [endogeneity concern: e.g., time-varying omitted variables / simultaneity / reverse causality]. We therefore instrument [predictor] with [instrument name]. We argue that [instrument] is a valid instrument through three layers of justification.

First, [instrument] is conceptually relevant to [predictor] because [theoretical mechanism linking instrument to endogenous variable]. [Empirical pattern or institutional feature] ensures that variation in [instrument] is associated with variation in [predictor].

Second, [instrument] satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor]. [Instrument] is unlikely to be correlated with omitted variables that determine [outcome] because [reason: e.g., individual-level decisions vary substantially across units / institutional design ensures no direct effect / efficient market hypothesis argues past information is already incorporated in prices].

Third, [instrument] meets statistical validity requirements. The first-stage F-statistic is [value], exceeding the Stock-Yogo threshold. The [Wu-Hausman / Sargan-Hansen] test [result], confirming that [endogeneity exists / instruments are exogenous]. We report these diagnostics in [Table X].
```

**设计变体**：
- **地理/制度IV模式**（如 JMR 2023 Singh）：县级政治捐款→企业游说；相关性来自地理足迹替代政治需求；排他性来自个体捐款动机与企业质量无关。
- **政策冲击IV模式**：政策实施时点→企业行为；相关性来自政策强制力；排他性来自政策只影响目标领域。
- **Lewbel异方差生成IV模式**（Wowak2025 MS）：无外生IV时，从第一阶段残差异方差中生成IV；需额外报告Pagan-Hall和Breusch-Pagan检验。
- **诚实边界**：三级论证不是可有可无的装饰。审稿人对IV的攻击通常从"为什么这个IV是外生的"开始，若M4/M7中缺乏概念层面的排他性论证，仅报告统计检验，审稿人会质疑排他性是否成立。

---

## M5. 调节/中介/机制变量

### 主骨架（通用）
：

```text
To capture [boundary/mechanism], we measure [moderator/mediator] as [operation]. We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition]. To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.
```

---

## M6. 控制变量与竞争性解释

### 主骨架（通用）
：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

---

## M7. 模型规格与估计方法

### 主骨架（通用）
：

```text
Because [dependent variable] is [continuous/binary/ordinal/count/censored/time-to-event], we estimate [model]. The specification includes [fixed effects] to absorb [unobserved heterogeneity/common shocks]. Standard errors are clustered at [level] to account for [within-unit dependence]. We use [estimator] for [hypotheses] because [outcome/design logic]. We also considered [alternative estimator]; results using this approach are reported as [robustness/supplement].
```

### 主骨架（通用）
（按需添加）： ✓ STANDARD（15+/28 篇范文使用）

```text
We employ [unit] fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01), indicating that unobserved [unit]-specific factors are correlated with our independent variables. [Year] fixed effects control for temporal trends such as [macroeconomic shocks/industry-wide shifts].
```

### 主骨架（通用）
：

```text
We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10, indicating that multicollinearity is not a concern. Second, the [Wooldridge/modified Wald] test indicates [presence/absence] of [autocorrelation/heteroskedasticity], and we report [robust/clustered] standard errors accordingly.
```

### 主骨架（通用）
：
当模型同时涉及非线性 DV 和工具变量时（如 Zhou 2017 ASQ），建议按以下顺序拼接：
1. 先报告 estimator-DV 匹配逻辑（Tobit 处理 censored / Poisson 处理 count）；
2. 再报告 IV 必要性与工具变量合理性；
3. 最后说明 second-stage 的解释策略（marginal effects / turning points / count effects）。
first-stage 统计量可置于 M7 正文、表格脚注或 R1 诊断段，取决于识别策略在论文中的核心程度。若 first-stage 仅作为诊断而非展示重点（如 ASQ 常见做法），建议在 M7 中仅简要提及"first-stage F 超过 Stock-Yogo 阈值"，将具体数值放入表格脚注。

**混合效应（within-between 分解）变体**：

```text
To disentangle the within-[unit] and between-[unit] effects of [predictor], we estimate mixed-effects models that decompose [predictor] into two components: [predictor]_{within}, which captures deviations from each [unit]'s mean over time, and [predictor]_{between}, which captures each [unit]'s time-invariant average. The within-effect answers whether [predictor] changes within the same [unit] are associated with [outcome] changes. The between-effect answers whether [units] with higher average [predictor] exhibit systematically different [outcome]. We include [random effects] to account for [unit]-level unobserved heterogeneity and [fixed effects] to absorb [time/common shocks].
```

### 变体 1: IV/2SLS 变体
： ✓ STANDARD（3-4 篇 IV 范文复现）

```text
Although [baseline estimator] can exploit [within/between] variation, it may still be biased if [predictor] is endogenous due to [omitted variable / reverse causality / measurement error]. We therefore use two-stage least squares (2SLS) with [instrument] as an instrument for [endogenous predictor]. [Instrument] satisfies the relevance condition because [first-stage F-statistic / theoretical reason for correlation with endogenous predictor]. It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor]. In the first stage, [endogenous predictor] is regressed on [instrument], [exogenous controls], and [fixed effects]. The first-stage F-statistic is [value], exceeding the Stock-Yogo threshold, indicating that [instrument] is not weak. In the second stage, [outcome] is regressed on the predicted [endogenous predictor] and the same controls. Standard errors are [robust / clustered] to account for [error structure].
```

### 变体 2: 线性概率模型（LPM）+ 2SLS 变体
（二元 DV 且需固定效应时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：IV/2SLS 变体

```text
Because the dependent variable is binary, one might consider Logit or Probit. However, when using 2SLS with fixed effects, the linear probability model (LPM) is often preferred because coefficients are directly interpretable as probability changes and computational tractability is preserved. We therefore estimate LPM with 2SLS for the main analyses and report Probit/Logit IV only as robustness. The specification includes [fixed effects] to absorb [unobserved heterogeneity]. Standard errors are clustered at the [level] to account for [dependence structure].
```

### 变体 3: 分层 IV 论证（JMR/MS 子标题风格）
： 🔬 EXPERIMENTAL（2/28 篇：Singh & Grewal 2023 JMR, Wowak2025 MS）⚠️ 保守替代：IV/2SLS 变体 1（扁平化单段）

```text
#### [Why IV: 内生性来源]
[Predictor] is a strategic decision for [units], which invest because they anticipate potential benefits. An omitted variable bias might arise if a time-varying omitted variable influences both [predictor] and [outcome], such as [unobserved strategic philosophy]. The prominence and dynamism of [institutional environment] creates a situation in which [contextual risk] constitutes a primary risk for [industry]. Thus, a link likely exists between [unit]'s [unobserved strategy] and [predictor]. For example, in anticipation of future [outcome], [units] might invest proactively in [predictor] to influence key stakeholders. Such a strategy, flowing from an organizational mindset embedded throughout the [unit] and based in managerial experience, is difficult to quantify. The absence of a measure of [unobserved construct], which correlates with both [outcome] and [predictor], creates an omitted variable bias that raises endogeneity concerns ([methodology_citation]). With 2SLS, we aim to identify an IV that meets the relevance and exclusion restrictions to address this concern.

#### [What IV: 工具变量构建]
The [geographical/temporal/institutional] [aggregate measure] of [exogenous source] provides a potential IV. In [country/institution], [contributors] may [action] to any [target]; the [database] maintains a database of all [records]. For example, [unit] has a presence in [N] [locations]. We [aggregate] the [records] from these [locations]. With the prediction that [unit] with a larger [geographical footprint] is more likely to be active in [predictor] at both its headquarters and [other locations], we gather [location information] for each [unit] from various sources. Then we search [databases] to find [location codes] and corresponding [identifiers] for each [location]. We enter these [identifiers] into the [database] to identify [individual-level data] over the [study period].

#### [Instrument Relevance]
To satisfy the relevance criterion, the IV should correlate with the endogenous regressor, which is [predictor]. We anticipate that they correlate [direction]: if [contributors] who live in [locations] where [unit] has its [presence] increase (decrease) their [contributions], [units]' [predictor] should decrease (increase). In general, [contributors] might make [contributions] to signal [motivation] or share views on issues related to [local concerns]; those issues might also be relevant to [units] with a presence in those local [locations]. When [contributions] increase, [units] may be motivated to dedicate less money to [predictor] activities, because they know their interests already are being represented. [Contributions] also fund the political ambitions of elected officials, so those officials likely account for the signaled interests of [contributors] in their legislative decisions. As [citation] determine, if more politicians already represent the interests of the citizens of a [region] in which [unit] is present, the [unit]'s need to [predictor] decreases. If, instead, [contributions] decrease, [units] may be motivated to allocate more money to [predictor] to ensure adequate representation of their interests. Conceptually, this instrument appears to meet the instrument relevance criterion.

#### [Exclusion Restriction]
The proposed instrument should not correlate with the omitted variable absorbed by the error term ([methodology_citation]). [Individual-level source] seems unlikely to exhibit any association with omitted variables (e.g., [unobserved quality]) that determine the [outcome]; rather, reasons to [contribute] likely vary substantially across individual [contributors] ([citation]). Citizens usually make [contributions] to express a personal political orientation or ideology ([citation]) or out of a sense of civic duty; an [example contributor] might contribute to a committee that is raising support for [specific issue]. Others might donate to align with the norms of their networks. In all these cases, individual [contributions] are unlikely to be directly associated with omitted variables that determine [outcome], so conceptually, it also meets the exclusion restriction criterion.

#### [Empirical Validity]
We assess the empirical validity of the IV by examining its strength and exogeneity, using different tests. Before doing so, we remove [contributions] from individuals associated with any [industry] [unit], according to [employer information]. We consider many variations of [units]' names to identify employees. Significant heterogeneity appears in [contributions] across [unit locations].

In [Table reference], we report the first-stage results of the two-stage estimator, which show that our IVs are significant predictors of [predictor]. For both set of equations, the IV coefficients are significant and empirically support the proposed relationship with the endogenous variable. A [sign] sign indicates that a greater (lower) degree of [IV] lowers (increases) [units]' need to [predictor]. For [outcome_1], the F-test rejects the null hypothesis of weak instruments (statistic = [value] (d.f. = [df]), p < [threshold]). The first-stage equation also controls for other exogenous variables, such as [fixed effects]. A Wu–Hausman test suggests the presence of endogeneity in the system, in that it rejects the null hypothesis (statistic = [value] (d.f. = [df]), p < [threshold]). Furthermore, a Sargan–Hansen test ensures the validity of the instruments; it does not reject the null hypothesis that the instruments are exogenous and thus valid (statistic = [value] (d.f. = [df]), n.s.). We find similar statistics for [outcome_2]. An F-test rejects the null hypothesis of weak instruments (statistic = [value] (d.f. = [df]), p < [threshold]); the Wu–Hausman test suggests the presence of endogeneity (statistic = [value] (d.f. = [df]) p < [threshold]); and a Sargan–Hansen test does not reject the null hypothesis that the instruments are exogenous (statistic = [value] (d.f. = [df]), n.s.).
```
**与原骨架差异**：这是 JMR/MS 风格的**分层子标题化 IV 论证**，将原本扁平化的单段 IV 说明拆分为五个功能子节。关键差异：(1) "Why IV"独立成节，详细论证内生性来源（time-varying omitted variable + 具体产业情境）；(2) "What IV"独立成节，详细描述 IV 的构建过程（地理足迹→数据匹配→聚合）；(3) "Relevance"和"Exclusion"各自独立成节，每节约 2-3 句理论论证；(4) "Empirical Validity"独立成节，完整报告 first-stage F、Wu-Hausman、Sargan-Hansen 三层诊断。与扁平化变体 1 的区别：变体 1 将所有内容压缩为一段，适用于 AMJ/SMJ 等偏好简洁 Methods 的期刊；分层变体适用于 JMR/MS 等偏好详细展开论证的期刊。诚实边界：目前仅观察到 2/28 篇范文使用此结构（Singh & Grewal 2023 JMR, Wowak2025 MS），暂未达到 STANDARD（15+/28）门槛，应标记为 EXPERIMENTAL。

### 变体 4: Model-Free Evidence 前置（强识别设计）
： ✓ STANDARD（当识别策略需要直观证据铺垫时）

```text
Before estimating the formal model, we present model-free evidence for the relationship between [predictor] and [outcome]. We split the sample into [low-intensity] and [high-intensity] groups based on [threshold: e.g., the mean / median value of predictor] and compare [outcome] across groups. A [t-test] (M_high = [value], M_low = [value], p < [threshold]) suggests that [pattern: e.g., the number of standardized recalls is lower in the high-intensity group than the low-intensity group], representing model-free evidence of [relationship]. The pattern in [Figure X] further supports this [direction] relationship. This evidence is purely descriptive and does not control for [confounds], but it provides a useful benchmark against which to assess the regression estimates.
```

**设计变体**：
- **均值/中位数分组模式**（如 JMR 2023 Singh）：按 lobbying 均值分组→比较 standardized recalls→t-test→图6展示。
- **处理/对照简单对比模式**（如 DiD 设计）：比较处理组和对照组的 raw means，展示处理前差异和处理后变化。
- **事件窗口简单计数模式**：事件发生前后，计数或均值简单对比。
- **诚实边界**：Model-Free Evidence 必须在正式模型之前呈现，且明确标注为"descriptive"和"does not control for"，避免审稿人误将其视为因果证据。其功能是"提供直观基准"，而非替代正式识别策略。

---

## M8. 识别策略 / 效度 / 诊断检验

### 主骨架（通用）
：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

### 变体 1: IV 排他性约束/过度识别检验变体
：

```text
A threat to our IV strategy is that [instrument] may affect [outcome] through channels other than [endogenous predictor]. We address this concern in three ways. First, we argue theoretically that [instrument] influences [outcome] only through [predictor] because [theoretical mechanism / institutional feature]. Second, we include [control for alternative channel] in the second stage to absorb [potential violation path]. Third, [IF overidentified: we report the Sargan / Hansen J overidentification test ([value], p = [value]), which does not reject the null that all instruments are valid, strengthening confidence in the exclusion restriction. IF just-identified: because the model is just-identified (one instrument for one endogenous variable), overidentification tests are infeasible. We therefore rely on theoretical arguments for the exclusion restriction and conduct placebo tests / sensitivity analyses to assess robustness.]
```

---

## M10. Methods 到 Results 的过渡

### 主骨架（通用）
：

```text
The Results section first reports [main tests] and then examines [validity/robustness checks]. Because [measure/design] raises [concern], we address this issue in supplemental analyses using [test]. The model requires interpreting [marginal effects/predicted values], which we report after the coefficient estimates. We assess the plausibility of [identification assumption] through [event-study/placebo/diagnostic] tests.
```

---

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