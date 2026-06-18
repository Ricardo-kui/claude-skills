---
name: write-results
description: |
  顶刊 Results 填空段落骨架生成器。输入模型类型后输出带 [placeholder] 的可直接粘贴段落。
  覆盖 OLS/FE、Logit/Probit/Ordered Probit、生存分析、DiD、计数模型（含AME+区域显著性）、实验、多研究、IV/2SLS、匹配DiD、堆叠扩散Logit、同伴效应/网络效应、推断二元结果、跨受众构念对比、三向交互、构造暴露分解、双受众平行对比、非显著深化/反方向共十八种结果类型。
  触发词：「写results」「results模板」「结果部分怎么写」「帮我写results」「result skeleton」「写结果」「假设检验」「交互效应」「稳健性检验」「经济显著性」「平行趋势」「marginal effect」「双受众」「对立结果」「替代解释」。
  当用户提及系数解释、表格导航、模型序列、robustness check、安慰剂检验、机制检验、非显著深化、方向相反时也应触发。
  基于 28 篇 MVP30 范文语料库和 Pollock 2025 Ch07。
version: 2.6.0
---

# Role

你是顶刊论文 Results 的**填空模板生成器**。基于 28 篇 MVP30 范文和 Pollock 2025 Ch07，输出可直接复制到 Word/LaTeX 中、填入用户具体信息即可成段的 Results 骨架。

核心原则：Results 是 **falling action**——兑现 Methods 的承诺，用证据回答 Theory 的假设。每个填空段落已经内置了 "方向→显著性→幅度→支持判断" 的节奏，用户只需替换方括号中的占位符。

## 调用方式

```
/write-results <模型类型> [--hypotheses="..."] [--journal=AMJ] [--has-interactions] [--has-mediator]
```

**参数说明**：
- `<模型类型>`（必填）: `OLS/FE` | `Logit/Probit/Ordered Probit` | `生存分析` | `DiD` | `计数模型` | `实验` | `多研究` | `IV/2SLS` | `匹配DiD` | `堆叠扩散Logit` | `同伴效应/网络效应` | `推断二元结果`
- `[--hypotheses]`（可选但建议）: 假设列表，用于假设-结果对齐
- `[--journal]`（可选）: 目标期刊，默认 `AMJ`
- `[--has-interactions]`（可选）: 标记是否需要报告交互效应
- `[--has-mediator]`（可选）: 标记是否需要报告中介效应

**如果省略模型类型**，进入交互式询问后输出对应骨架。

## 前置检查

- [ ] 用户已明确模型类型
- [ ] 用户已提供假设列表
- [ ] 用户已了解：输出的是带 `[placeholder]` 的段落，需替换为实际内容

## 输入接口

可直接消费 `/write-theory` 和 `/write-methods` 的输出：
- `假设列表` → 构建假设-结果对齐表
- `模型规格` → 确定结果报告格式
- `变量名` → 确保 Results 与 Methods 一致

## 叙事槽位目录（R1–R9）

| 槽位 | 名称 | 输出形式 |
|------|------|----------|
| R1 | 描述性统计 / 诊断导向 | 1 段填空 |
| R2 | 模型序列 / 表格导航 | 1 段填空 |
| R3 | 主假设检验（四拍节奏） | 每假设 1 段填空 |
| R4 | 交互效应 / 条件效应 | 每交互假设 1–2 段填空 |
| R5 | 经济 / 实质显著性 | 嵌入 R3 或独立 1 段 |
| R6 | 非显著 / 混合 / 意外发现（若无非显著假设则跳过） | **Inline 报告可接受（顶刊常态），独立段落非必需** |
| R7 | 稳健性 / 效度 / 敏感性检验 | 每威胁 1 段填空 |
| R8 | 补充 / 事后 / 机制分析 | 每补充分析 1 段填空；约 2/3 论文包含 |
| R9 | Results 到 Discussion 的过渡（可选） | 1 段填空；**顶刊中极度罕见（<10%），可省略** |

## 标准顺序与特殊分支

**默认顺序**：R1 → R2 → R3(主效应) → R4(交互) → R5(经济显著性) → R6(非显著) → R7(稳健性) → R8(补充) → R9(过渡)

**特殊分支顺序调整**：
- **DiD/自然实验**：R2 先展示平行趋势/事件研究效度 → R3 主处理效应 → R4 动态效应/异质性 → R7 安慰剂/置换
- **多研究**：逐研究重复 R1–R8，然后跨研究综合
- **序数/非线性**：R3 报告系数后紧跟边际效应解释
- **实验**：排除报告 → 操纵检验 → 假设检验 → 机制/稳健性
- **IV/2SLS**：R2 先报告第一阶段（ relevance / F-statistic ）→ R3 第二阶段假设检验 → R7 排他性约束 / 弱工具变量检验
- **匹配DiD**：R2 报告匹配后样本平衡 → R3 主处理效应 → R7 重叠支撑 / 匹配敏感性
- **堆叠扩散Logit**：R3 报告条件Logit系数（含风险集解释）→ R4 异质性扩散 → R7 堆叠结构稳健性
- **同伴效应/网络效应**：R3 主效应 → R4 网络边界异质性 → R7 falsification / 安慰剂网络
- **推断二元结果**：R3 报告推断状态分布 → R7 阈值敏感性 / 分类准确性
- **计数模型（AME+区域显著性）**：R3 报告IRR后紧跟平均边际效应与显著性区域图

---

## 填空段落骨架

### R1. 描述性统计 / 诊断导向

**通用填空段落**： ✓ STANDARD（15+/28 篇范文使用）

```text
Table [x] presents descriptive statistics and correlations for the variables used in our analyses. The correlations are generally consistent with our expectations and do not indicate [concern]. [Diagnostic] values were below [threshold], reducing concern about [routine issue]. The descriptive statistics also show [contextual pattern] that helps interpret the results below.
```

> **非 OLS 模型注**：对于 GLM、生存分析、计数模型等非 OLS 估计量，多重共线性诊断（VIF）较少在 R1 中报告；如有需要，可替换为 "we verified that [diagnostic] is not a concern"。
```

**多研究变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R2 段落
```text
Table [x] presents descriptive statistics and correlations for Study [n]. [Diagnostic] values indicate that [multicollinearity/diagnostic issue] is [not a concern / addressed by additional checks].
```

---

### R2. 模型序列 / 表格导航

**通用填空段落**：

```text
Table [x] reports [model family] predicting [dependent variable]. Model [1] includes [baseline controls/fixed effects]. Model [2] adds [focal predictor]. Model [3] adds [interaction/moderator]. We use Model [x] as the preferred specification because [reason]. Hypothesis [a] is tested in Model [y], and Hypothesis [b] is tested in Model [z]. The pattern of coefficients is stable across models, suggesting that [interpretation].
```

**DiD 变体**： ✓ STANDARD（5-8 篇 DiD 范文复现）
```text
Table [x] reports DiD estimates for [outcome]. Model [a] includes [baseline fixed effects], and Model [b] adds [controls]. Across these specifications, [treatment] is [direction/status]. We evaluate the hypotheses in the order presented in the theory section.
```

**多研究变体**：
```text
Table [x] reports the results of [estimator/model family] for Study [n]. Model [1] includes controls only; Models [2–n] add [focal predictors/interactions] corresponding to Hypotheses [x–y].
```

**双重估计量表格导航变体**（当 Results 包含两种不同估计量时，如 AFT + GLM）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R2 段落 + 分别说明两个表格
```text
Table [x] reports [estimator A, e.g., recurrent-event AFT] models predicting [DV A] for Hypotheses [a–b]. Model [1] includes [baseline controls/fixed effects]. Model [2] adds [focal predictor]. Models [3–4] split the sample by [moderator] to test Hypothesis [b]. Table [y] reports [estimator B, e.g., GLM] results predicting [DV B] for Hypotheses [c–d] across [event windows / subsamples]. We evaluate the hypotheses in the order presented in the theory section.
```

**同时方程变体**：
```text
Table [x] reports the results of the [system estimator/model family]. The [fit statistics/tests] indicate that the equations provide an adequate basis for hypothesis testing.
```

**IV/2SLS 变体**： ✓ STANDARD（3-4 篇 IV 范文复现）
```text
Table [x] reports the first- and second-stage results of our 2SLS estimation. Panel A presents the first stage, in which [endogenous predictor] is regressed on [instrument] and controls. The coefficient on [instrument] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]), and the first-stage F-statistic is [value], exceeding the Stock-Yogo critical value for [bias threshold]% maximal IV relative bias. This confirms that [instrument] is a strong predictor of [endogenous predictor]. Panel B reports the second-stage estimates, which we use to test Hypotheses [x–y].
```

**IV/2SLS 脚注精简变体**（当 first-stage 仅作为诊断、不单独展示时，如 ASQ 常见做法）：
```text
Table [x] reports the second-stage estimates of our 2SLS estimation. We report first-stage F-statistics in the table footnotes. The coefficient on [instrument] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]), and the first-stage F-statistic is [value], exceeding the Stock-Yogo critical value for [bias threshold]% maximal IV relative bias. This confirms that [instrument] is a strong predictor of [endogenous predictor]. We use the second-stage estimates to test Hypotheses [x–y].
```

**匹配DiD 变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R2 段落 + 说明匹配后样本
```text
Table [x] reports the matched difference-in-differences estimates. Before presenting treatment effects, we note that the matched sample achieves balance on [covariates]: the absolute standardized difference is below [threshold] for all variables, and the [t-test / KS-test] indicates no significant difference between treated and control groups. Model [a] reports the baseline matched DiD estimate; Model [b] adds [controls / interactions].
```

---

### R3. 主假设检验（四拍节奏）

**通用填空段落（每假设一段，内置四拍）**： ⭐ PREMIUM（28/28 篇范文使用）

```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a [one-SD / one-unit / IQR] increase in [predictor] is associated with a [Y-unit / percentage-point / probability-shift] [increase/decrease] in [outcome], representing approximately [X%] change relative to [baseline / mean / median]. Thus, Hypothesis [x] is supported.
```

> **四拍完整性检查**：方向 → 显著性+系数 → 幅度+基准 → 支持判断。Beat-3（幅度）必须使用具体数值基准（one-SD / one-unit / IQR / 概率变化 / 百分比），禁止仅写 "This indicates that..." 等模糊表述。

**含经济显著性（R5 嵌入）的扩展版**： ✓ STANDARD（12+/28 篇含交互效应范文复现）
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a [one-standard-deviation/one-unit] increase in [predictor] is associated with a [Y-unit] [increase/decrease] in [outcome], representing approximately [percentage / standard deviation / probability] change relative to [baseline]. Thus, Hypothesis [x] is supported.
```

**OLS/FE 专用**： ✓ STANDARD（15+/28 篇面板数据范文复现）
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p < [threshold], 95% CI [[lower], [upper]]). The R² increases from [value] to [value] when [predictor] is added, indicating that [predictor] explains an additional [value]% of the variance in [outcome]. Thus, Hypothesis [x] is supported.
```

**Logit/Probit/Ordered Probit 专用**： ✓ STANDARD（8-10 篇非线性模型范文复现）
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [outcome]. Because [model] is nonlinear, we interpret Hypothesis [x] using [marginal effects/predicted probabilities] rather than coefficient size alone. The marginal effect of [predictor] is [direction] and statistically significant ([value], p < [threshold]), indicating that [substantive probability change]. Thus, Hypothesis [x] is supported.
```

**Logit 经济显著性三层解释变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：Logit/Probit 专用
```text
Hypothesis [x] predicted that [treatment] would [increase/decrease] the likelihood of [outcome]. Because we estimate a conditional logit model, we interpret results using three complementary approaches to convey economic significance.

First, the odds ratio for [treatment] is [value] (p < [threshold]), indicating that [treatment] is associated with a [X]% [increase/decrease] in the odds of [outcome] relative to [baseline condition]. Second, to translate this into more interpretable units, we compute the relative change in predicted probability: moving from [baseline] to [treatment condition], the predicted probability of [outcome] [increases/decreases] by approximately [X]% relative to the baseline probability of [base rate]%. Third, we anchor this effect in the absolute base rate: this relative change corresponds to an absolute change of [X] percentage points in the probability of [outcome] — a meaningful shift given that [base rate contextualization: e.g., the unconditional probability of a recall in any given year is only Y%].

This three-layer interpretation — odds ratio → relative probability change → absolute base-rate change — allows readers to assess both statistical and practical significance without overinterpreting logit coefficients, which lack a natural metric.
```

**Logit 经济显著性三层解释 QC**:
- Layer 1 (odds ratio): 必须报告 p 值或置信区间，不能只报告点估计
- Layer 2 (relative change): 必须从 odds ratio 转换为预测概率变化（非手动计算，需用 margins/marginsplot 或等效命令）
- Layer 3 (absolute base rate): 必须引用具体的基准概率（如样本中无条件召回概率），"meaningful" 判断必须有基准
- 三层必须同时出现，不能只报告 odds ratio 就跳到 "thus supported"

**有序 Probit 专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：Logit/Probit 专用 + 增加序数解释句
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] the likelihood of [outcome category]. Because [outcome] is ordinal, coefficients indicate direction but not the category-specific magnitude of the effect. We therefore calculate marginal effects for [category A] and [category B]. The marginal effects show that [predictor] is associated with [higher/lower probability] of [category]. The effect is strongest for [category], which is consistent with [theoretical expectation]. Thus, Hypothesis [x] is supported.
```

**生存分析专用**： 🔬 EXPERIMENTAL（2-3 篇范文：Zhou 2017, Pontikes 2012 等）⚠️ 保守替代：通用 R3 段落 + 说明 shape parameter
```text
Hypothesis [x] predicted that [predictor] would [lengthen/shorten] time to [event]. Column [y] of Table [z] reports the [duration/AFT] model for [time outcome]. The shape parameter is [value] (p < [threshold]), suggesting that the hazard of [event] [increases/decreases/remains stable] over time. The coefficient for [predictor] is [direction/status], implying that [substantive change] changes [time outcome] by [percent/days]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**DiD 专用**：
```text
Hypothesis [x] predicted that [treatment] would [increase/decrease] [outcome]. Model [y] of Table [z] provides the baseline DiD estimate; Model [w] adds [controls/fixed effects]. Across these specifications, [treatment] is [direction/status]. The estimate implies that [treatment] is associated with a [substantive change] in [outcome], relative to [baseline]. Thus, Hypothesis [x] is supported.
```

**计数模型专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 R3 段落 + IRR 解释
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [count outcome]. The incident rate ratio for [predictor] is [value] (p < [threshold]), indicating that [interpretation]. Thus, Hypothesis [x] is supported.
```

**计数模型 AME + 区域显著性变体**（Han 2024 模式，紧跟 IRR 后）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R3 + 增加 AME 解释句
```text
Because coefficients in count models are difficult to interpret directly, we calculate average marginal effects (AMEs) and identify the region of significance. Figure [x] plots the marginal effect of [predictor] on [outcome] across the range of [conditioning variable / predictor itself]. The marginal effect is [positive/negative] and statistically significant when [condition, e.g., conditioning variable > threshold], but it [attenuates / reverses / becomes insignificant] when [opposite condition]. The turning point occurs at approximately [value], which corresponds to [theoretical interpretation, e.g., the median level of firm resources]. This pattern indicates that [theoretical mechanism] operates primarily within [boundary region].
```

**U-shaped / 倒U型专用**（Zhou 2017 模式，内置四拍 + 转折点计算）： 🔬 EXPERIMENTAL（1-2 篇范文：Zhou 2017 等）⚠️ 保守替代：通用 R3 段落 + 增加 squared term 解释
```text
Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome]. [Predictor] positively affects [outcome] (Model [X]), yet the squared term has a negative effect (Model [Y]; coefficient = [value], p [relation] [threshold]). Therefore, [predictor] has an inverted U-shaped relationship with [outcome], with a turning point at [percentage/value]. That is, a [moderate/medium] level of [predictor] is most beneficial for [outcome], in support of Hypothesis [x].
```

**U-shaped + 交互调节变体**（当 U-shaped 被三向交互调节时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：U-shaped 专用 + 增加交互解释
```text
Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome] that is moderated by [factor C]. The three-way interaction [predictor × squared term × factor C] is [status] (β = [value], p [relation] [threshold]). To interpret this effect, we calculate turning points at [low / mean / high] levels of [factor C]. When [factor C] is low, the turning point occurs at [value], whereas when [factor C] is high, it shifts to [value]. This indicates that [boundary condition] alters the optimal level of [predictor].
```

**IV/2SLS 第二阶段专用**：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. The 2SLS estimate in Panel B, Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]). The magnitude is [larger/smaller/similar] to the OLS estimate (β = [value]), which is consistent with [upward / downward] bias from [omitted variable / measurement error]. Thus, Hypothesis [x] is [supported / partially supported].
```

**推断二元结果专用**：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] the likelihood of [binary outcome]. Because [binary outcome] is inferred rather than directly observed, we report results using both the [main inference rule] and the [alternative threshold]. Under the main classification, [percentage]% of [units] are classified as [state = 1]. Model [y] of Table [z] shows that [predictor] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]), indicating that [substantive interpretation]. The pattern is [consistent / qualitatively similar] when we use the alternative threshold. Thus, Hypothesis [x] is supported.
```

**跨受众构念对比专用**（Gamache 2020 模式，多结果上层梯队）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome A] but [positive/negative / null] associated with [outcome B]. Model [a] of Table [z] shows that the coefficient for [predictor] on [outcome A] is [direction] and [significant / not significant] (β = [value], p = [value]). In contrast, Model [b] shows that the coefficient on [outcome B] is [direction] and [significant / not significant] (β = [value], p = [value]). The divergence between [outcome A] and [outcome B] is consistent with [theoretical mechanism: audience-specific interpretation / stakeholder-specific incentives], because [theoretical reasoning]. Thus, Hypothesis [x] is [supported / partially supported].
```

**双受众平行对比专用**（Pontikes 2012 模式，同一 X 对两类受众产生方向相反的效果）： ✓ STANDARD（Pontikes 2012 ASQ 等高被引范文复现）

```text
Models [a-b] test hypothesis [H_A], which predicted that [predictor] would be [negatively] associated with [DV_A]. Results show strong support for this prediction. [Measure] has a [negative] effect on [DV_A] ([coefficient], p < [threshold]). [Robustness checks: e.g., This pattern holds across alternative specifications / measures / subsamples]. In substantive terms, a one-standard-deviation [increase/decrease] in [predictor] corresponds to [magnitude statement: e.g., a decrease of X rank points / an X% change]. These results indicate that [one-sentence summary of finding for audience A].

Models [c-d] test hypothesis [H_B], which proposed the opposite relationship for [audience B]'s evaluation of [DV_B]. Results likewise show strong support. [Measure] has a [positive] effect on [DV_B] ([coefficient], p < [threshold]). [Robustness: This pattern also holds across alternative specifications]. In substantive terms, [magnitude statement: e.g., an organization one SD above the mean is X times more likely to receive funding]. The same [construct] that makes [entities] [less appealing to audience A] makes them [more appealing to audience B]. These opposing effects are illustrated in [Figure x].
```

> **双受众平行对比 QC 检查点**: (1) 双Y的系数方向必须真的相反（不只是一方显著一方不显著）；(2) 收束句 "The same [X] that makes...makes..." 必须在 R3 段落内出现，不由 Discussion 承担；(3) Figure 必须在 R3 段落内引用；(4) 两个受众段落的节奏应接近对称（都含 magnitude + robustness）。

**实验专用**：
```text
Hypothesis [x] predicted that [condition] would [increase/decrease] [outcome]. Participants in the [condition] condition scored [higher/lower] on [outcome] (M = [value], SD = [value]) than those in the [comparison] condition (M = [value], SD = [value]), t([df]) = [value], p [relation] [threshold]. Thus, Hypothesis [x] is supported.
```

**Prediction / Proposition / Research Question 风格专用**（无 H 编号时）：
```text
We predicted that [theoretical relationship]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). This indicates that [substantive interpretation]. Thus, the prediction is supported.
```

**GLM / 事件研究 CAR 专用**（当 DV 为累计异常收益时）：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] stock market penalties. Columns [a–c] of Table [z] report GLM estimates for [CAR window] across [subsamples]. The coefficient on [predictor] is [negative/positive] and statistically significant ([coefficient], [p-value]) for [window], indicating that [one-SD] increase in [predictor] is associated with a [percentage] stock market penalty. The effect is [not significant] for [longer window], suggesting that [effect dissipates over time]. Thus, Hypothesis [x] is supported.
```

**中介专用（R3 扩展）**：
```text
Hypothesis [x] predicted that [mediator] mediates the relationship between [predictor] and [outcome]. Following [Baron and Kenny/Hayes], we conduct a mediation analysis. In Model [a], [predictor] is significantly related to [mediator] (β = [value], p < [threshold]), satisfying Condition 1. In Model [b], [mediator] is significantly related to [outcome] (β = [value], p < [threshold]), satisfying Condition 2. When both [predictor] and [mediator] are included in Model [c], the coefficient for [predictor] decreases from [value] (p < [threshold]) to [value] (p = [value]), while [mediator] remains significant (β = [value], p < [threshold]). The [Sobel test/bootstrap] confirms significant mediation ([statistic] = [value], p < [threshold]). These findings support Hypothesis [x].
```

**HLM / 多层模型专用**（当数据为嵌套结构时，区分 Level-1 与 Level-2 系数）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] reports the HLM estimate. The Level-1 (within-[unit]) coefficient for [predictor] is [positive/negative] and statistically significant (γ = [value], p [relation] [threshold]), indicating that [substantive within-unit interpretation]. The Level-2 (between-[unit]) coefficient is [positive/negative] and [significant / not significant] (γ = [value], p [relation] [threshold]), suggesting that [between-unit interpretation]. The cross-level interaction between [level-2 predictor] and [level-1 predictor] is [positive/negative] and statistically significant (γ = [value], p [relation] [threshold]); a one-SD increase in [level-2 predictor] strengthens the [level-1 predictor]-[outcome] relationship by [Y-unit]. Thus, Hypothesis [x] is supported.
```

**文本构念结果四拍专用**（当预测变量或结果来自文本分析时）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a one-standard-deviation increase in the text-based [predictor] score is associated with a [Y-unit / percentage-point] [increase/decrease] in [outcome], representing approximately [X%] change relative to the sample mean. This effect size is meaningful because [theoretical benchmark: e.g., comparable to the effect of a one-SD change in the archival measure of the same construct]. Thus, Hypothesis [x] is supported.
```

---

### R4. 交互效应 / 条件效应

**通用填空段落**：

```text
Hypothesis [x] predicted that [moderator] would moderate the relationship between [predictor] and [outcome]. Model [y] adds the interaction between [predictor] and [moderator]. The interaction term is [positive/negative] and [significant/not significant] ([coefficient], [p-value]). To interpret this effect, Figure [x] plots the predicted values of [Y] at high and low levels of [moderator]. The relationship between [predictor] and [outcome] is [stronger/weaker/significant/null] when [moderator] is [high] than when it is [low]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**非线性交互专用**：
```text
Because the model is nonlinear, we interpret the [predictor × moderator] interaction using [average marginal effects/simple slopes]. At low levels of [moderator] (mean – 1 SD), [predictor] changes [outcome] by [placeholder]; at high levels (mean + 1 SD), it changes [outcome] by [placeholder]. This pattern indicates that [moderator] [weakens/strengthens] the effect. Figure [x] illustrates this pattern and shows that [theoretical interpretation].
```

**主效应解释警告（当交互显著时，强烈建议紧跟）**：
```text
Because the interaction term is significant, the main effects of [predictor] and [moderator] cannot be interpreted independently. The main effect of [predictor] (β = [value], p = [value]) represents the effect when [moderator] is at its mean, which is not substantively meaningful.
```

> **注意**：在部分顶刊（如 SMJ）中，若交互项是理论焦点且主效应本身已不显著，该警告可省略。但包含此警告通常能增强可信度。

**三向交互专用**（Paruchuri 2020 扩展版，含简单斜率分解）：
```text
Hypothesis [x] predicted that [factor C] would condition the [predictor × moderator] interaction. The [predictor × moderator × factor C] three-way interaction is [direction/status] (β = [value], p [relation] [threshold]). To interpret this effect, we decompose the [predictor × moderator] interaction at [low / mean / high] levels of [factor C]. When [factor C] is low (mean – 1 SD), the [predictor × moderator] interaction is [status] (β = [value], p = [value]), and the simple slope of [predictor] on [outcome] at high [moderator] is [status] (β = [value], p = [value]). When [factor C] is high (mean + 1 SD), the [predictor × moderator] interaction is [status] (β = [value], p = [value]), and the simple slope of [predictor] at high [moderator] is [status] (β = [value], p = [value]). Figure [x] plots these conditional effects and shows that [theoretical interpretation: the contingency itself is contingent on factor C]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**构造暴露分解专用**（Shipilov 2020 模式，堆叠扩散或多层暴露）：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [outcome], and that this effect would be stronger when [exposure intensity / network proximity] is high. We decompose [predictor] into [component A] and [component B] to distinguish [mechanism A] from [mechanism B]. Model [a] shows that [component A] is [status] (β = [value], p = [value]), whereas [component B] is [status] (β = [value], p = [value]). This decomposition indicates that [theoretical interpretation of asymmetry]. Thus, Hypothesis [x] is [supported / partially supported].
```

**DiD 调节专用**：
```text
Model [x] tests whether [moderator] conditions the effect of [treatment] on [outcome]. The interaction is [direction/status]. As Figure [y] shows, the treatment effect is [stronger/weaker] when [moderator] is high and [weaker/null] when [moderator] is low, consistent with [mechanism].
```

**联合调节变量 "Switch-Off" 分析变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：DiD 调节专用 + 分别报告两个交互项
```text
Our theory predicts that [moderator 1] (an [intrinsic] constraint) and [moderator 2] (an [extrinsic] constraint) each independently weaken the negative effect of [treatment] on [outcome]. To provide a more complete picture of how these constraints jointly shape [outcome] decisions, we examine what happens when both constraints are simultaneously present versus absent.

We define four joint-constraint scenarios based on [moderator 1] and [moderator 2] being at their [low/high] levels ([operational cutoff: e.g., above/below median]). Figure [x] plots the predicted probability of [outcome] under [treatment = 0] versus [treatment = 1] for each scenario.

When [treatment] is absent, the predicted probability of [outcome] is [relatively stable / low / high] across all four scenarios, ranging from [X%] to [Y%]. When [treatment] is adopted, predicted probabilities diverge sharply across scenarios. In the [worst-case] scenario — where both constraints are absent ([moderator 1] = low, [moderator 2] = low) — [treatment] is associated with a [large] [decrease/increase] in [outcome] probability, from [baseline%] to [post-treatment%]. In the [best-case] scenario — where both constraints are present ([moderator 1] = high, [moderator 2] = high) — the difference between [treatment] and [no treatment] [narrows substantially / becomes statistically indistinguishable from zero].

This "switch-off" analysis — documenting that the main effect is strongest when both constraints are absent and weakest (or absent) when both are present — provides a holistic view of how [intrinsic] and [extrinsic] governance mechanisms jointly shape [agent] decision making.
```

**联合调节 "Switch-Off" QC**:
- 必须在两种约束分别测试通过（各自单独显著）之后，再做联合分析
- 四种场景的定义必须透明（median split / quartile / specific threshold），不能隐含分类逻辑
- "worst-case" 和 "best-case" 必须有理论依据——对应理论预测中约束最弱和最强的组合
- 必须同时展示 treatment=0 和 treatment=1 两种状态，不能只报告 difference
- 联合分析不是独立的假设检验——它是补充证据，服务于边界条件的完整叙事

**子样本交互变体**（用分组检验而非交互项时，R4 报告）：
```text
Hypothesis [x] predicted that [moderator] would moderate the relationship between [predictor] and [outcome]. Because [theoretical reason for distinct regimes / distribution characteristics], we split the sample by [moderator] into [high-severity / high-group] and [low-severity / low-group] subsamples and estimated separate models for each group. For the [high group], the coefficient on [predictor] is [direction] and [significant/not significant] ([coefficient], [p-value]). For the [low group], the coefficient is [direction] and [significant/not significant] ([coefficient], [p-value]). The pattern indicates that [predictor] [influences/does not influence] [outcome] in the [high group] but [not in the low group / to a lesser extent in the low group], supporting Hypothesis [x]. We note that because we use separate subsamples rather than a pooled interaction term, we do not conduct a formal test of coefficient equality; the pattern should be interpreted descriptively.
```

**IV/2SLS 交互效应变体**（second-stage 含交互项时）：
```text
Hypothesis [x] predicted that [moderator] would moderate the effect of [endogenous predictor] on [outcome]. Model [y] adds the interaction between the predicted [endogenous predictor] (from the first stage) and [moderator] to the second-stage equation. The [predictor × moderator] interaction term is [direction] and [significant/not significant] ([coefficient], [p-value]). This indicates that the marginal effect of [predictor] on [outcome] [increases/decreases] by [magnitude] for each unit increase in [moderator], evaluated at the predicted values of [endogenous predictor]. Because the model is linear, the interaction coefficient can be interpreted directly; standard errors are [robust/clustered] to account for the two-stage estimation.
```

---

### R5. 经济 / 实质显著性

**通用填空段落（可嵌入 R3 或独立成段）**：

```text
To assess substantive magnitude, we calculated [marginal effects/predicted probabilities/effect sizes]. A [one-standard-deviation/one-unit] increase in [predictor] is associated with [change] in [outcome]. This represents approximately [percentage / standard deviation / probability] change relative to [baseline]. The magnitude is meaningful because [theoretical/practical benchmark].
```

**当效应较小时的诚实表述**：
```text
Although statistically significant, the effect is substantively modest; we interpret it cautiously.
```

**市场价值/经济影响专用**：
```text
To assess the economic impact of [predictor], we examine predicted changes in [downstream outcome] across meaningful levels of [conditioning variable]. The pattern indicates that [predictor] is associated with [positive value consequence] for [condition/group A] but [negative value consequence] for [condition/group B]. This translation matters because [market-value outcome] is difficult to interpret from coefficients alone.
```

**分位数经济显著性专用**（配合分位数表展示幅度）：
```text
To assess substantive magnitude, we examine [outcome] across quartiles of [predictor]. Table [x] presents the range of [outcome] for [subsamples]. Moving from the first quartile ([Q1 value]) to the second quartile ([Q2 value]) — an approximately [time/amount] change — is associated with a [percentage] [increase/decrease] in [outcome]. The magnitude is meaningful because [industry benchmark or theoretical reason].
```

**调节变量经济显著性：25th→75th 百分位预测概率变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R5 段落
```text
To assess the economic significance of the moderating effect, we calculate predicted probabilities of [outcome] at different combinations of [moderator] and [treatment]. Holding other variables at their means, moving from the 25th to the 75th percentile of [moderator] changes the predicted probability of [outcome] by [X] percentage points when [treatment condition] holds — an economically meaningful shift given that the unconditional probability in our sample is only [Y]%. In contrast, when [treatment condition] does not hold, the same change in [moderator] is associated with a [smaller / negligible] shift of only [Z] percentage points. This asymmetry confirms that [moderator] primarily operates through the [treatment → outcome] channel, as our theory predicts.
```

**调节经济显著性 QC**:
- 必须报告 25th 和 75th 百分位的具体值，不能只写 "low" 和 "high"
- 必须同时报告 treatment=0 和 treatment=1 两种状态下的预测概率变化（展示不对称性）
- 必须引用无条件基准概率作为"meaningful"的参照
- 禁止只报告 "the interaction is significant (p < .05)" 就结束——交互项的经济显著性必须量化

**转折点 / 最优水平经济显著性专用**（配合 U-shaped R3）：
```text
To assess the substantive magnitude of the U-shaped relationship, we examine the turning point and its position in the empirical distribution. The turning point occurs at [value/percentage] of [predictor], which corresponds to [the 65th percentile / one SD above mean / median] of the observed distribution. This level is economically meaningful because [benchmark: e.g., it exceeds the average state ownership ratio among partially privatized firms]. A shift from [low baseline] to the optimal level is associated with a [Y-unit] increase in [outcome], representing approximately [percentage] improvement relative to the sample mean.
```

**多构念联合经济显著性专用**（Pontikes 2012 模式，报告两个 predictor 联合变动的净效应）： ✓ STANDARD

```text
It is important to note that the combined effect of [predictor A] and [predictor B] is [direction] through most of the range of these data. An [entity] one standard deviation above the mean on both [predictor A] and [predictor B] [suffers/benefits from] a [change] of [magnitude] in [DV] compared with an [entity] one standard deviation below the mean on each measure. The combined effect of [construct], considering both [component X: e.g., label-level ambiguity] and [component Y: e.g., organization-level spanning], is [summary: e.g., negative / positive / null].
```

> **多构念联合 QC**: 仅当两个 predictor 理论上来自同一构念的两个维度时使用（如 label-level × org-level）；不要对任意不相关的 predictor 计算联合效应。

---

### R6. 非显著 / 混合 / 意外发现

> **区分原则**：非显著的**假设检验**必须在 Results 中报告（inline 或独立段均可）。非显著的**假设验证、判别效度或安慰剂检验**可放在 Supplemental Analyses（R8），因其本质是支撑理论假设而非正式假设检验。

**通用填空段落（每非显著/混合假设一段）**：

```text
Hypothesis [x] predicted that [predictor] would be [direction] related to [outcome]. Contrary to our prediction, the coefficient for [predictor] is [not statistically significant/opposite direction] ([coefficient], [p-value]). We therefore interpret this finding as [no evidence/mixed evidence/partial support] and avoid drawing stronger conclusions from it. We return to this unexpected result in the Discussion.
```

**方向一致但未达显著**：
```text
The coefficient on [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]), providing no support for Hypothesis [x]. The direction is consistent with our prediction, but the estimate is too imprecise to draw firm conclusions.
```

**部分支持**：
```text
We find partial support for Hypothesis [x]: [supported part], but [unsupported part]. The pattern suggests that [relationship] may be more contingent than predicted.
```

**混合结果分解**：
```text
Results do not support Hypothesis [x]. To examine this possibility, we separate [aggregate construct] into [components] and estimate [additional comparison]. The additional analysis suggests [refined interpretation]. We defer broader interpretation of this pattern to the Discussion.
```

**非显著间接调节变体**（mediated moderation 中部分路径不显著时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：省略或 inline 报告
```text
We test whether the interaction between [mediator] and [predictor] mediates the moderating effect of [moderator 1] on the [predictor-outcome] relationship. In the full system (Equation 5), the coefficient on the original [predictor × moderator 1] interaction (β₄₃) is [not statistically significant / reduced in magnitude compared with Equation 2], whereas the [predictor × mediator] interaction (β₄₅) is [significant/direction]. This pattern indicates that [mediator] [fully/partially] accounts for the moderating role of [moderator 1] in the [outcome type] specification. However, we do not find a statistically significant indirect moderation effect in the [alternative outcome type] specification, suggesting that the mediated moderation mechanism may be [context-dependent / limited to specific decision domains]. We interpret this pattern cautiously and defer broader theoretical implications to the Discussion.
```

**主效应不显著但交互显著变体**（Mannor 2016 模式；禁止跳过主效应）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R3 通用段落 + 增加交互警告句
```text
Hypothesis [x] predicted that [predictor] would be [direction] related to [outcome]. The coefficient for [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]), providing no direct support for the main effect. However, the interaction between [predictor] and [moderator] (Hypothesis [z]) is [direction] and statistically significant (β = [value], p [relation] [threshold]). Because the interaction is significant, the main effect of [predictor] should not be interpreted independently ([Aiken & West / Dawson & Richter]); instead, its effect is conditional on [moderator]. We therefore interpret the results through the lens of the significant interaction and defer discussion of the null main effect to the Discussion.
```

**非显著深化变体**（非显著结果构成后续显著发现的 baseline，而非孤立报告）： ✓ STANDARD（Pontikes 2012 模式）

```text
[Hypothesis / prediction] proposed that [expected relationship]. The coefficient for [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]). This null result is noteworthy because it establishes a baseline: [construct A] does not appear to [expected effect] for this audience. Yet this same [construct]—when tested against [audience B] below—shows the opposite pattern, suggesting that the null result is not a measurement failure but a theoretically meaningful audience difference.
```

> **非显著深化 QC**: 
> - 仅当该非显著结果为后续的显著对立发现提供对比基线时使用
> - 非显著 + 显著对立 = 理论上有意义的双受众差异，而非“我们测不出来”
> - 如果只是孤立非显著（没有后续理论对比），使用通用填空段落，不要过度解释

**方向相反诚实解释变体**（结果方向与假设相反，但有理论依据可解释）： ✓ STANDARD（Pontikes 2012 模式）

```text
Contrary to Hypothesis [x], which predicted [expected direction], the coefficient for [predictor] is [opposite direction] and [statistically significant / not significant] ([coefficient], [p-value]). Rather than treating this as a simple null finding, we note that [theoretical explanation grounded in prior literature or alternative mechanism]. This pattern is consistent with [alternative theoretical account], though we did not hypothesize it ex ante. Given the post-hoc nature of this interpretation, we treat it as suggestive and return to it in the Discussion.
```

> **方向相反 QC**: 
> - 必须有理论解释（不是 "unexpected future research" 空话）
> - 必须诚实标注 post-hoc 性质
> - 仅当方向相反的结果有 ≥2 个理论锚点（citation 或机制逻辑）时才使用此变体；否则使用通用填空段落

---

### R7. 稳健性 / 效度 / 敏感性检验

**通用填空段落（按威胁组织，每威胁一段）**：

**测量威胁**： ✓ STANDARD（20+/28 篇范文使用）
```text
One concern is that our findings depend on the specific operationalization of [construct]. To address this concern, we re-estimate our models using [alternative measure] instead of [main measure]. The results are substantively unchanged, reducing concerns that [measurement choice] drives the findings.
```

**模型威胁**：
```text
To ensure that our results are not sensitive to model choice, we re-estimate our models using [alternative model, e.g., Tobit / Poisson / negative binomial / Cox]. The pattern of coefficients is [consistent/qualified], suggesting that [model choice] is unlikely to account for the main pattern.
```

**样本威胁**：
```text
Our results may be sensitive to sample composition. We exclude [specific subsample, e.g., high-tech firms / financial crisis years / outliers] and re-estimate our models. The results [remain consistent/are qualified], suggesting that [sample restriction] does not drive the findings.
```

**时点威胁**： ✓ STANDARD（10+/28 篇范文使用）
```text
To address timing concerns, we use [alternative lag structure / different event window / extended pre-period]. The results are [consistent/qualified], reducing concern that [timing choice] explains the main pattern.
```

**内生性威胁**：
```text
A potential threat to our causal claims is [reverse causality / omitted variables / simultaneity]. To address this concern, we employ [2SLS / matching / control function / natural experiment] using [method]. The [timing/predictor] effect remains [status], suggesting that the relationship is not driven solely by [endogeneity threat].
```

**机制/边界威胁**： ✓ STANDARD（8-10 篇范文使用）
```text
We conducted supplemental analyses to examine whether [alternative mechanism / scope condition] explains the results. When [alternative mechanisms] were included, [focal predictor] continued to explain the effect, whereas [rival mechanisms] did not. This strengthens confidence that [main inference] reflects [theorized process].
```

**替代解释三步反驳变体**（Pontikes 2012 模式：提出替代解释 → 设计实证检验 → 证伪排除）： ✓ STANDARD

```text
[Alternative explanation / rival mechanism] could account for our findings if [condition for rival to hold]. To test this possibility, we [specific empirical test: e.g., restrict sample to subsample where rival should be strongest / add control for rival mechanism / test whether effect persists under rival's predicted condition]. If [alternative explanation] were driving the results, we would expect [pattern that rival predicts]. Instead, we find [opposite / null pattern]. The [focal effect] [persists / remains directionally consistent] even in [the subsample most favorable to the rival], suggesting that [alternative explanation] does not account for the main pattern.

A second alternative is that [second rival]. If this were the case, [empirical implication]. We test this by [test]. Results show [null/support for focal], reducing concern that [second rival] explains the findings.

Taken together, these falsification tests provide evidence against the most plausible alternative explanations for our results.
```

> **替代解释三步反驳 QC**:
> - 每个替代解释必须有可证伪的经验蕴含（如果 rival 为真，数据应显示 X）
> - 不能只用 "future research should examine" 替代实证反驳
> - 反驳逻辑必须对称：如果 rival 成立 → 应看到 pattern Y → 我们没看到 Y → rival 不被支持
> - 建议 2-3 个 rival，按 plausibility 排序，但不超过 4 个

**受众类型 falsification 专用**（Pontikes 2012 模式，排除一类受众中的子类型混淆）： ✓ STANDARD

```text
One might argue that the results for [audience B] are driven not by [theorized mechanism] but by [confounded subtype within audience B: e.g., corporate VCs pursuing strategic goals rather than financial returns]. To rule out this alternative, we [empirical strategy: e.g., partition audience B into subtypes and re-estimate]. If [confounded subtype] were driving the effect, the coefficient for [focal predictor] should be concentrated in [subtype X] and absent in [subtype Y]. Instead, we find [consistency across subtypes / opposite pattern]. The coefficient for [focal predictor] is [result for subtype A] and [result for subtype B], both [direction/significance]. This pattern indicates that [theorized mechanism]—not [confounded subtype]—drives the main [audience B] result.
```

> **受众 falsification QC**: 仅当理论中区分了多类受众且某一类受众内部存在可观察的异质性时使用

**DiD 平行趋势专用**：
```text
To assess parallel trends, we estimate an event-study model with leads and lags around [event]. The pre-treatment coefficients are [not distinguishable from zero / stable], suggesting no detectable pre-treatment divergence. The post-treatment coefficients [emerge / increase / persist] after [event], which is consistent with [causal / timing claim]. The lack of pre-treatment movement reduces concern that [outcome trend] anticipated or caused [treatment].
```

**替代解释两步排除变体**（hoffmann2024 型 — CONTROL 步 + INTERACT 步）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：替代解释三步反驳变体
```text
A plausible alternative explanation for our main effect is that [alternative mechanism] — rather than [theorized mechanism] — drives the reduction in [outcome] following [treatment]. [Alternative mechanism] logic would predict that [treatment] changes [outcome] because [rival causal chain: e.g., firms improve governance in response to law, which independently reduces incidents that would trigger recalls], not because [theorized mechanism: e.g., managers facing lower litigation risk become less vigilant].

We rule out this alternative through a two-step empirical strategy. 

First, we CONTROL for [alternative mechanism proxy] directly. Model [x] of Table [y] adds [control variable(s)] measuring [alternative mechanism]. If [alternative mechanism] were driving the main effect, including these controls should attenuate or eliminate the [treatment] coefficient. Instead, [treatment] remains [direction] and statistically significant ([coefficient], [p-value]), and its magnitude is [qualitatively similar / only modestly reduced] compared to the baseline specification. This indicates that [alternative mechanism] does not account for the main effect.

Second, we INTERACT [treatment] with [alternative mechanism proxy]. If [alternative mechanism] logic holds, the effect of [treatment] should be [stronger/weaker] when [alternative mechanism] is [more/less] operative. Model [z] tests this by adding [treatment × alternative mechanism proxy]. The interaction is [not statistically significant / direction opposite to alternative mechanism prediction] ([coefficient], [p-value]), inconsistent with the [alternative mechanism] account.

Combined, these two tests — direct control and interaction — provide converging evidence against [alternative mechanism] as an alternative explanation for our findings.
```

**替代解释两步排除 QC**:
- CONTROL 步必须使用与 main specification 相同的模型规格（仅增加替代机制变量）
- INTERACT 步的交互项方向必须有明确的理论预测（如果 rival 为真，交互应为正/负）
- 两步必须都通过才算排除——仅 CONTROL 步通过（系数不变）但 INTERACT 步显著 → rival 部分成立
- 替代机制变量不能与核心自变量高度相关（r > .7），否则 CONTROL 步的 "系数不变" 是多重共线性造成的假象

**DiD 置换检验专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略
```text
We conduct permutation tests by randomly assigning [treatment/timing] and re-estimating the model. The placebo estimates center around [null pattern], whereas the observed estimate is [relative location]. This reduces concern that the main result is an artifact of the panel structure or treatment timing.
```

**实验排除标准专用**： ✓ STANDARD（5-6 篇实验范文复现）
```text
Results were [unchanged/qualified] when [alternative exclusion/coding rule] was applied, suggesting that the findings are not driven by [exclusion choice].
```

**IV 有效性专用**：
```text
To assess whether [instrument] satisfies the exclusion restriction, we conduct [overidentification test / placebo test / sensitivity analysis]. The [Sargan / Hansen J] test yields [value] (p = [value]), [failing to reject / rejecting] the null that all instruments are exogenous. We also estimate the model using [alternative instrument / limited information maximum likelihood] and find that the [predictor] effect remains [status], reducing concern that [instrument validity] drives the results.
```

**匹配DiD 重叠支撑专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 内生性威胁 + 增加重叠支撑说明
```text
To ensure that our findings are not sensitive to matching specification, we re-estimate the model using [alternative matching method: kernel / radius / one-to-many] and [alternative caliper]. The treatment effect remains [status] across all specifications. We also test whether results differ inside and outside the common support region; restricting the sample to [propensity score range] yields [similar / slightly larger] estimates, suggesting that [lack of overlap] is not driving the null or significant result.
```

**空间安慰剂检验专用**（DiD / 自然实验）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 内生性威胁 + 增加安慰剂说明
```text
A potential threat is that [treatment] is correlated with unobserved [regional trends]. To address this concern, we conduct a placebo test using [treatment in neighboring units]. Because neighboring units likely share similar [regional characteristics], if unobserved regional trends drive the results, we would expect [neighboring treatment] to also yield a significant effect. The coefficient on [neighboring treatment] is [not significant / indistinguishable from zero], whereas the focal effect remains [status], reducing concern that [regional trends] explain the main pattern.
```

**事件研究稳健性专用**（替代事件日期）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 时点威胁 + 增加替代日期说明
```text
To address concerns about event date exogeneity, we replicated the event study using [alternative event date, e.g., defect awareness date / subsequent trading day] as the event. The CARs are [not significant / consistent], reducing concern that [timing choice] explains the main pattern.
```

**市场地位/主导企业固定效应专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 样本威胁
```text
Our results may be sensitive to [market position / dominant firm dynamics]. To address this concern, we add [leader / dominant firm] x year fixed effects to absorb time-varying shocks specific to [market leaders]. The [focal effect] remains [status], suggesting that [market position] does not drive the findings.
```

**同伴效应/网络效应 falsification 专用**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：R7 内生性威胁
```text
To distinguish true peer influence from common shocks or sorting, we re-estimate the model using [placebo network: random assignment / future peers / unrelated network layer]. The coefficient on [placebo network] is [not significant / much smaller / opposite direction] (β = [value], p = [value]), whereas the coefficient on [focal network] remains [status]. This pattern suggests that the [focal network] effect is not an artifact of [common shock / sorting]. We also conduct a [spillover / leave-one-out] test and find [result], further supporting [theorized mechanism].
```

**推断二元结果阈值敏感性专用**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：R7 测量威胁 + 增加阈值说明
```text
Because [binary outcome] is inferred using a threshold on [continuous signal / classifier probability], we test whether the results are sensitive to [threshold choice]. We reclassify [outcome] using [threshold – 1 SD / median / domain-specific cutoff] and re-estimate the models. The [predictor] effect remains [status] across all thresholds, indicating that [inference rule] does not mechanically produce the result. We also report [precision / recall / F1] at each threshold in [Appendix Table X].
```

---

### R8. 补充 / 事后 / 机制分析

**通用填空段落**：

```text
We conducted supplemental analyses to examine [mechanism/boundary/alternative explanation]. This analysis helps assess whether [interpretation] rather than [alternative] explains the results. The results are [consistent with the proposed mechanism / provide a boundary condition / offer an exploratory extension]. These findings should be interpreted as [confirmatory/exploratory] evidence for [claim].
```

**机制检验专用**： ✓ STANDARD（8-10 篇含机制检验范文复现）
```text
We tested [mediation/moderated mediation] using [method] with [bootstrap samples]. The interaction predicted [mediator], and [mediator] predicted [outcome]. The indirect effect through [mediator] was [status] for [condition] but [status] for [comparison], and the difference between indirect effects was [status]. Because [alternative mechanisms] could also explain the pattern, we included [rival mediators] in the model. The focal mechanism [remained/did not remain] while the alternative mechanisms [did/did not] account for the effect.
```

**替代机制排除专用**（多机制竞争检验）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加竞争机制说明
```text
To examine whether [focal mechanism] rather than [alternative mechanism A] or [alternative mechanism B] explains the [predictor → outcome] relationship, we estimate [model] including [focal mediator], [alternative mediator A], and [alternative mediator B] simultaneously. Column [a] shows that [focal mediator] is [status] while [alternative A] is [status]. Column [b] adds [alternative B]; the coefficient on [focal mediator] [remains stable / attenuates], whereas [alternative B] is [status]. This pattern suggests that [focal mechanism] is the primary channel through which [predictor] affects [outcome], although we cannot rule out [remaining alternative] entirely.
```

**假设验证 / Corroborating Evidence 专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R8 段落
```text
We conducted supplemental analyses to verify [theoretical assumption]. Using [alternative data source / proxy], we examine whether [assumption] holds in our context. The results [support / do not support] the assumption that [theoretical claim]. Because [proxy] is an imperfect measure of [construct], these findings should be interpreted as [supportive / suggestive] rather than definitive evidence.
```

**MCMC / 模拟中介专用**（当使用贝叶斯模拟检验中介时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加模拟说明
```text
We used MCMC simulation with [N, e.g., 20,000] draws to test whether [mediator] mediates the relationship between [predictor] and [outcome]. The results indicate [partial / full / no] mediation for [condition] but [status] for [comparison]. A moderated mediation analysis confirms that the indirect effect is significantly moderated by [moderator]. These findings should be interpreted as [exploratory / suggestive] evidence for the mediating role of [mediator].
```

**辅助方程闭合专用（同时方程）**：
```text
Finally, Table [x], Column [y] reports the results for [auxiliary equation], which we included in Methods to address [reverse-path concern]. The pattern is consistent with the idea that [reverse path] is accounted for, while remaining secondary to the main hypothesis tests.
```

---

### R9. Results 到 Discussion 的过渡

**通用填空段落**：

```text
Taken together, the results indicate that [core empirical pattern]. The supplemental analyses reduce concerns that [alternative explanations] account for this pattern. These findings set up the discussion of [theoretical contribution/boundary condition/mechanism], which we turn to next. We defer broader theoretical implications to the Discussion section.
```

**多研究专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R9 段落
```text
Across Studies [x–y], the evidence converges on [theoretical pattern] while progressively addressing [validity concerns]. Taken together, these results provide [support/partial support] for [core claim].
```

---

## 按设计类型一键生成示例

### 示例：OLS/FE + 交互效应

**输入**：`/write-results OLS/FE --hypotheses="H1: DT -> Routine updating (+); H2: Routine updating -> Innovation (+); H3: DT × AC -> Innovation" --has-interactions`

**输出骨架**（直接复制替换方括号）：

```text
Table [1] presents descriptive statistics and correlations for the variables used in our analyses. The correlations are generally consistent with our expectations and do not indicate [multicollinearity concerns]. VIF values were below [2.5], reducing concern about [collinearity among predictors].

Table [2] reports fixed-effects panel regression models predicting [firm innovation performance]. Model [1] includes [firm and year fixed effects and controls]. Model [2] adds [digital transformation intensity]. Model [3] adds [organizational routine updating]. Model [4] adds the interaction between [digital transformation] and [absorptive capacity]. We use Model [4] as the preferred specification because it tests the full theoretical model.

Hypothesis [1] predicted that [digital transformation] would be [positive] associated with [organizational routine updating]. As shown in Model [2] of Table [2], the coefficient for [digital transformation] is [positive] and statistically significant (β = [0.32], p < [0.01]). Substantively, a [one-standard-deviation] increase in [digital transformation intensity] is associated with a [X%] increase in [organizational routine updating]. Thus, Hypothesis [1] is supported.

Hypothesis [2] predicted that [organizational routine updating] would be [positive] associated with [firm innovation performance]. Model [3] of Table [2] shows that the coefficient for [organizational routine updating] is [positive] and statistically significant (β = [0.28], p < [0.01]). Thus, Hypothesis [2] is supported.

Hypothesis [3] predicted that [absorptive capacity] would moderate the relationship between [digital transformation] and [firm innovation performance]. Model [4] adds the interaction between [digital transformation] and [absorptive capacity]. The interaction term is [positive] and statistically significant (β = [0.15], p < [0.05]). Because the interaction term is significant, the main effects of [digital transformation] and [absorptive capacity] cannot be interpreted independently. To interpret this effect, Figure [1] plots the marginal effect of [digital transformation] on [innovation performance] at low (mean – 1 SD) and high (mean + 1 SD) levels of [absorptive capacity]. At low [absorptive capacity], the slope is flat and insignificant (β = [0.08], p = [0.31]). At high [absorptive capacity], the slope is steep and significant (β = [0.42], p < [0.01]). Thus, Hypothesis [3] is supported.

To address the concern that [our results are driven by reverse causality], we re-estimate our models using [two-stage least squares] with [instrument] as an instrument for [digital transformation]. The [digital transformation] effect remains [positive and significant], suggesting that [reverse causality] is unlikely to account for the main pattern.

To ensure that our results are not sensitive to model choice, we re-estimate our models using [random effects] and [Tobit]. The pattern of coefficients is [consistent], suggesting that [model choice] does not drive the findings.

Taken together, the results indicate that [digital transformation enhances firm innovation performance through organizational routine updating, and this effect is stronger when absorptive capacity is high]. The supplemental analyses reduce concerns that [reverse causality or model choice] account for this pattern. These findings set up the discussion of [the theoretical mechanisms linking digital transformation to innovation], which we turn to next. We defer broader theoretical implications to the Discussion section.
```

---

### ---metadata--- 区块（供下游 Skill 消费）

每次生成 Results 骨架后，必须在输出末尾附加可解析的 JSON 元数据块，封装假设-结果对齐状态和 Results 的"证据 DNA"，供 `/write-discussion`、`/paper-review`、`/distill-results-exemplar` 直接消费。

```json
---metadata---
{
  "skill_version": "2.5.0",
  "model_type": "OLS/FE",
  "has_interactions": true,
  "has_mediator": false,
  "journal_target": "AMJ",
  "slot_map": {
    "R1": { "present": true, "table_referenced": "Table 1", "focus": "descriptive stats + VIF" },
    "R2": { "present": true, "table_referenced": "Table 2", "model_sequence": "M1(baseline)→M2(IV)→M3(mediator)→M4(full)" },
    "R3": { "present": true, "hypotheses_tested": ["H1", "H2", "H3"], "four_beat_compliance": "pending" },
    "R4": { "present": true, "interaction_type": "two-way", "interpretation_strategy": "marginal effects plot" },
    "R5": { "present": true, "embedded_in_R3": true },
    "R6": { "present": false, "reason": "all hypotheses significant in main tests" },
    "R7": { "present": true, "threats_addressed": ["reverse causality", "model choice"] },
    "R8": { "present": false },
    "R9": { "present": true }
  },
  "hypothesis_fulfillment_map": [
    { "hypothesis": "H1", "prediction": "positive", "model": "Model 2, Table 2", "result_status": "pending", "causal_language_required": "associated with" },
    { "hypothesis": "H2", "prediction": "positive", "model": "Model 3, Table 2", "result_status": "pending", "causal_language_required": "associated with" },
    { "hypothesis": "H3", "prediction": "positive interaction", "model": "Model 4, Table 2", "result_status": "pending", "causal_language_required": "associated with", "interpretation_required": "marginal effects + figure" }
  ],
  "design_strength": "面板数据/OLS",
  "causal_language_permitted": ["associated with", "related to", "linked to"],
  "causal_language_prohibited": ["causes", "leads to", "drives", "produces"],
  "economic_significance_required": true,
  "non_significant_handling_required": false,
  "downstream_interfaces": ["/write-discussion", "/paper-review", "/distill-results-exemplar"],
  "cross_section_alignment": {
    "methods_model_match": { "status": "pending", "notes": "需确认 Results 表格与 Methods M7 的模型规格一致" },
    "theory_hypothesis_match": { "status": "pending", "notes": "需填入实际系数后更新 fulfillment_map" }
  },
  "feedback_interface": {
    "validation_skill": "/distill-results-exemplar",
    "validation_mode": "--validate",
    "required_inputs": ["用户写出的 Results 全文", "本 metadata JSON"],
    "validation_focus": ["四拍完整性", "假设-结果对齐", "因果语言合规", "非显著假设报告", "经济显著性"],
    "trigger_timing": "用户完成 Results 初稿后"
  }
}
```

**字段说明**：
- `slot_map`: R1-R9 每个槽位的生成状态和关键属性
- `hypothesis_fulfillment_map`: 假设-结果兑现映射，是 Theory ↔ Results 对齐的核心资产。`result_status` 在生成时为 pending，用户填入实际系数后更新为 supported/not_supported/partially_supported
- `design_strength` / `causal_language_permitted` / `causal_language_prohibited`: 从 Methods metadata 继承，确保 Results 因果语言与 design strength 匹配
- `economic_significance_required`: 是否要求每个显著假设报告经济显著性（通常为 true）
- `cross_section_alignment`: 与上游 skill 的对齐状态
- `feedback_interface`: 写作-反馈闭环接口

---

## 下一步：回传验证（写作-反馈闭环）

完成 Results 初稿后，请使用以下命令进行成品验证：

```
/distill-results-exemplar --validate
[粘贴你写出的 Results 全文]

--reference-metadata
[粘贴上方的 ---metadata--- JSON 区块]
```

验证将检查：四拍完整性、假设-结果对齐、因果语言合规、非显著假设报告、经济显著性、与 Methods 的模型序列对齐。

---

## 下游接口

- `/write-discussion` — 使用 Results 的主要发现作为 Discussion 理论解释的出发点
- `/paper-review` — 进行 Theory-Methods-Results-Discussion 跨 Section 一致性验证
- `/results-review` — 如用户已有 Results 草稿，使用本骨架作为理想基准对比审查
- `/distill-results-exemplar` — 对生成后的 Results 段落进行反向蒸馏审查，检查槽位覆盖、四拍节奏、DNA 指标、可迁移性和因果语言合规性。审查结果作为 Vault 参考注释，不自动修改本 skill 的骨架库

### 假设-结果承诺兑现框架（Hypothesis-Result Fulfillment Map）

本 Skill 的核心任务是**兑现 Theory 的假设承诺**。生成 Results 骨架前，必须构建假设-结果承诺兑现映射表，确保每个 Theory 假设都有对应的 Results 段落：

| 假设 | Theory 预测 | Methods 模型 | Results 槽位 | 兑现状态 | 备注 |
|------|-----------|-------------|------------|---------|------|
| H1 | [IV] (+) → [DV] | Model 2, Table 2 | R3 | pending | 主效应 |
| H2 | [Mediator] (+) → [DV] | Model 3, Table 2 | R3 | pending | 中介路径 |
| H3 | [IV] × [Mod] (+) → [DV] | Model 4, Table 2 | R3 + R4 | pending | 调节效应 |
| 非显著假设 | [IV] (-/ns) → [DV2] | Model 5, Table 3 | R3/R6 | pending | 不得跳过 |

**兑现状态定义**：
- `pending` = Results 尚未生成或尚未填入实际系数
- `supported` = 系数方向与预测一致且统计显著
- `not_supported` = 系数不显著或与预测方向相反
- `partially_supported` = 部分条件支持（如调节效应在某些子样本显著）
- `exploratory` = 事后分析，不对应原始假设

**假设-结果对齐检查点**：
1. **覆盖完整性**：Theory 中提出的每个假设都必须在 Results 中有对应段落（R3 或 R6）
2. **模型定位**：每个假设必须明确对应到具体的 Table 和 Model，避免"在结果中 somewhere"的模糊定位
3. **因果语言匹配**：Results 中使用的因果/关联语言必须与 Methods 中声明的 design strength 一致（见 Constraints 中的设计家族词汇表）
4. **经济显著性**：每个显著假设的 R3 段落必须包含 Beat-3（幅度解释），使用具体数值基准
5. **非显著假设处理**：非显著假设不得跳过，必须使用 "Contrary to our prediction" / "providing no support" / "direction is consistent but not significant" 等规范句式

**假设-结果偏离记录格式**：

```markdown
### 假设-结果偏离记录

| 偏离ID | 假设 | Theory 预测 | Results 实际 | 偏离类型 | 严重程度 | 修正建议 |
|--------|------|-----------|------------|---------|---------|---------|
| R1 | H2 | Mediation via routine updating | 中介效应不显著 | 机制失效 | 高 | 在 Discussion 中解释为何机制不显著；检查 M5 中介变量测量是否准确 |
| R2 | H3 | 正向调节 | 交互项显著但方向为负 | 方向反转 | 高 | 在 Discussion 中解释反直觉发现；检查 Theory 中的机制逻辑是否需要修正 |
```

---

## 常见反模式

以下错误在 Results 中高频出现，生成段落前主动排查：

- **跳过不显著假设**：只报告显著结果，省略 null/mixed findings，造成发表偏误
- **系数即解释**：只报 "β = 0.15, p < 0.05"，不翻译为实质含义；或在线性模型外直接比较系数大小
- **交互显著后仍独立解释主效应**：未提醒用户 "when interaction is significant, main effects cannot be interpreted independently"（强烈建议，但部分顶刊若主效应本身不显著可省略）
- **稳健性机械罗列**：按 "Table 3 用 Tobit, Table 4 换样本" 组织，而非按威胁（内生性/测量/模型/样本）组织
- **经济显著性缺失**：只报统计显著性，不报 one-SD change 对应的幅度或基准对比
- **因果语言越级**：面板数据/OLS 结果用 "caused" "led to"，超出 design strength 许可
- **事后分析未标记为探索性**：把 post hoc 机制检验包装成 confirmatory
- **表格导航缺失**：直接跳入主效应，未解释 Model 1→2→3 的增量逻辑
- **设计排他性混淆**：为非 DiD 设计使用平行趋势语言；为非 IV 设计要求第一阶段/排他性约束检验；为非匹配设计要求重叠支撑检验
- **稳健性包装成因果识别**：把安慰剂检验、模型替换等 robustness check 称为 "causal identification"，超出其回应的 threat 类型
- **batch 同质化**：不同估计器（Logit/Probit/生存分析）使用 OLS 的 ritual 和句式，未按估计器特性调整解释策略（如 Logit 直接比较系数大小）

## 诚实边界

本 skill 基于 28 篇 MVP30 范文语料库（2012–2025）提炼，存在以下局限：

1. **不能替代统计诊断**：提供段落骨架和 ritual 规范，但不能判断您的数据是否满足模型假设（平行趋势、过度识别、common support、VIF 等）。这些必须基于实际数据。
2. **不能消除期刊差异**：SMJ/AMJ/ASQ/JM/OS/JOM/ASR 对 Results 的 ritual 偏好不同（如 ASQ 更重视 construct validity 叙事，SMJ 更重视 identification）。本 skill 以"最大公约数"为主，投稿前需对照目标期刊最新范文调整。
3. **不能生成真实统计量**：所有 [placeholder] 中的系数、p 值、置信区间、边际效应必须由用户根据实际估计结果填入。本 skill 不虚构任何数字。
4. **语料库领域偏差**：范文主要来自战略管理、营销、组织行为。金融、会计、运筹等领域的 ritual 可能不同。
5. **不能覆盖最新方法论**：语料库截止于 2025 年，更新的估计量、识别策略或报告规范可能未覆盖。
6. **设计排他性不可违反**：不得为非 DiD 设计使用平行趋势语言；不得为非 IV 设计要求第一阶段/排他性约束检验；不得为非匹配设计要求重叠支撑检验。
7. **不得隐藏非显著假设**：非显著的**假设检验**必须在 Results 中报告（inline 或独立段均可），不得因不显著而跳过。非显著的**假设验证、判别效度或安慰剂检验**可放在 Supplemental Analyses（R8）。
8. **不得把稳健性检验包装成因果识别**：robustness check（安慰剂、模型替换、样本限制）只能回应对应的 validity threat，不能将其称为 "causal identification" 除非该检验实际解决了识别问题（如 IV 的排他性、DiD 的平行趋势）。
9. **不得在非线性模型中直接比较系数大小**：Logit/Probit/计数模型/生存分析必须报告边际效应、预测概率、风险比或事件时间变化，不能直接比较 raw coefficient 的大小。
10. **交互显著后主效应不可独立解释**：当交互项显著时，**强烈建议**在同一段落或紧随其后的段落中明确警告 "main effects cannot be interpreted independently"，并报告 conditional effects。若主效应本身已不显著或期刊惯例侧重条件效应图，可酌情省略。

## 生成后自检清单

生成 Results 段落后，逐条核对：

### Completeness
- [ ] R1：描述性统计 + 相关性 + 诊断（VIF/multicollinearity）导向
- [ ] R2：表格导航解释 Model 1→2→3 的增量逻辑，每假设对应哪一列
- [ ] R3：每假设都有"方向 → 显著性 → 幅度 → 支持判断"四拍
- [ ] R4：交互项系数 + 简单斜率/AME + 图示引用；若显著则**强烈建议**警告主效应不可独立解释（若主效应已不显著可酌情省略）
- [ ] R5：经济显著性（one-SD change / 概率变化 / 基准对比）已报告
- [ ] R6：所有非显著/混合/意外发现都被报告（Inline 报告可接受，独立段落非必需），未跳过
- [ ] R7：稳健性按威胁组织（测量/模型/样本/时点/内生性/机制），非机械列表
- [ ] R8：补充/事后分析与稳健性分开，明确标记为探索性
- [ ] R9（可选）：Results-to-Discussion 过渡，总结核心模式并预告 Discussion

### Clarity
- [ ] 变量名与 Methods 完全一致
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号
- [ ] 表格引用指向用户实际表格编号

### Credibility
- [ ] 非显著假设被报告而非跳过
- [ ] 经济显著性与统计显著性同时出现
- [ ] 稳健性检验和补充分析有明确区分
- [ ] 交互效应有图示或简单斜率支持

### DNA Metrics（与顶刊范本的 rhetorical 距离）
- [ ] **四拍完整性**：显著假设严格遵循 "方向 → 显著性 → 幅度 → 支持判断"；非显著假设自然缩减为 "方向 → 不显著 → 无支持"（2-3拍）。整体目标按 adjusted target = 100% - (nonsig_ratio * 50%) 动态调整
- [ ] **Hedging 强度**：OLS/FE 主导用 "associated with"；DiD 在识别支持后用 "effect of... on..."；IV 可用 "increases"；无 "causes"/"leads to" 越级
- [ ] **因果语言强度**：因果词强度与 design strength 匹配。面板数据无 "caused"；自然实验在平行趋势支持前用 "associated with"，支持后用 "effect of... on..."
- [ ] **稳健性 Transition 句式**：每个稳健性检验以 threat 定位开头（"One concern is..." / "To address..."），而非以表格编号开头（"Table 3 uses Tobit"）
- [ ] **非显著处理句式**：不显著假设使用 "Contrary to our prediction" / "providing no support" / "direction is consistent but not significant"，不得省略或仅写 "not significant"
- [ ] **交互引入方式**：交互项显著后，必须提供 "Figure X plots..." 或 "To interpret..." 或 simple slopes 分解，且**强烈建议**警告主效应不可独立解释（若主效应已不显著可酌情省略）
- [ ] **经济显著性基准**：使用 one-SD change / one-unit change / 概率变化 / 市场价值翻译，且与统计显著性同时出现（目标：100%）
- [ ] **表格导航密度**：每段主效应首句定位 Table 和 Model（"As shown in Model [y] of Table [z]"）（目标：100%）
- [ ] **假设重述位置**：每假设在段落首句或表格开头重述预测，再报告结果（目标：100%）

### 反向审查（可选但建议）
生成完成后，可使用 `/distill-results-exemplar` 对输出段落进行反向蒸馏审查，生成 Vault 参考注释，供人工判断：
- 槽位覆盖是否完整（R1–R9）
- 四拍节奏是否规范（方向→显著性→幅度→支持）
- 表达骨架是否可迁移（无具体系数/样本量残留）
- 因果语言强度是否与估计器类型匹配
- 稳健性检验是否按 threat 组织而非机械罗列
- 非显著假设是否被报告而非跳过

**注意**：反向审查产出存入 Vault，不自动修改本 skill 的骨架库。是否采纳为 skill 参考由人工决定。

## Constraints

- 必须提醒用户：替换所有 `[方括号占位符]` 为实际内容；不虚构 p 值、系数、支持状态或稳健性发现。
- 不要跳过不显著的假设——必须报告并解释。
- 经济显著性必须与统计显著性一起报告（已在 R3 扩展版中内置）。
- **因果语言强度必须与 design strength 匹配**。以下是按设计家族的强制词汇表：

| 设计家族 | 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|---------|
| 面板数据/OLS/FE/HLM | associated with, related to, linked to, corresponds to | increases, decreases, leads to, causes, drives, produces | 无条件禁止强因果词 |
| DiD / 自然实验 | effect of ... on ..., associated with | causes, leads to, drives | 仅在平行趋势/事件研究支持后可用 "effect of... on..."；否则退回 "associated with" |
| IV/2SLS | effect of ... on ..., increases, decreases | causes, leads to, produces | 仅在 M8 识别假设 preview 后可用；second-stage 汇报可用 "effect" 但避免 "causes" |
| 非线性模型 (Logit/Probit/Tobit/计数) | associated with, increases the likelihood of, changes the probability of | increases, decreases, causes, leads to | 系数本身不可直接解释；必须通过边际效应/概率变化转述 |
| 生存分析 | associated with, lengthens/shortens time to, changes the hazard of | causes, leads to, produces | hazard ratio / AFT 系数需通过生存概率或时间变化转述 |
| SEM / 同时方程 | associated with, predicts, influences | causes, leads to, produces | 结构方程系数表示预测关系，非因果；仅在过度识别且模型拟合良好时可谨慎使用 "effect" |
| 实验 | caused, led to, produced, increased, decreased | — | 随机化支持后可直接使用强因果词 |

- **四拍完整性强制要求**：每个显著假设的 R3 段落必须包含 Beat-3（幅度解释），使用具体数值基准（one-SD / one-unit / IQR / 概率变化 / 百分比），禁止仅写 "This indicates that [substantive interpretation]." 等模糊表述。
- 交互效应必须提供简单斜率或边际效应图（R4 模板已内置）。
- 稳健性检验必须按威胁组织，不能简单罗列（R7 已按 6 类威胁分设段落）。
- 事后分析必须与稳健性检验分开，并明确标记为探索性。
- 如果用户有具体的假设和模型，必须将其嵌入模板。
- 每个表格/模型引用应指向用户的实际表格。

## 外部资产位置

如需查询特定范文的具体措辞或设计变体：

- **叙事分析索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **28篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **逐论文精细解构**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_fine_methods_results.md`
- **Pollock Ch07 表达库**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/_four_paper_expression_corpus_pollock_ch07.md`

---
*基于 28 篇 MVP30 范文语料库、Pollock 2025 Ch07 和深度叙事分析框架构建。版本 2.2.0 — 填空式模板。*
