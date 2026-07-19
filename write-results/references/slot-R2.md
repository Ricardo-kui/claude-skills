<!-- write-results 槽位骨架 R2：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

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

**IV/2SLS 多结果表格导航变体**（同 IV，多个 second-stage 结果）： ✓ STANDARD
```text
Table [x] reports the 2SLS results for [outcome A] (Panel A) and [outcome B] (Panel B). Each panel separates the first stage and the second stage. The first-stage estimates, in which [endogenous predictor] is regressed on [instrument] and controls, are reported in the left columns of each panel; the coefficient on [instrument] is [positive/negative] and statistically significant in both panels (β = [value], p [relation] [threshold] for [outcome A]; β = [value], p [relation] [threshold] for [outcome B]), and the first-stage F-statistics exceed the Stock-Yogo threshold. The right columns of each panel report the second-stage estimates, which we use to test Hypotheses [x–y] for [outcome A] and Hypotheses [z–w] for [outcome B].
```

**匹配DiD 变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R2 段落 + 说明匹配后样本
```text
Table [x] reports the matched difference-in-differences estimates. Before presenting treatment effects, we note that the matched sample achieves balance on [covariates]: the absolute standardized difference is below [threshold] for all variables, and the [t-test / KS-test] indicates no significant difference between treated and control groups. Model [a] reports the baseline matched DiD estimate; Model [b] adds [controls / interactions].
```
