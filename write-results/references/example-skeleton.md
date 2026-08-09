# Example Skeleton — OLS/FE + 交互效应 示例（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成 OLS/FE + 交互效应骨架时**对照参考**（直接复制替换方括号）。其余结果类型见 `econometric-models/[结果类型].md`。

**输入**：`/write-results OLS/FE --hypotheses="H1: DT -> Routine updating (+); H2: Routine updating -> Innovation (+); H3: DT × AC -> Innovation" --has-interactions`

```text
Table [1] presents descriptive statistics and correlations for the variables used in our analyses. The correlations are generally consistent with our expectations and do not indicate [multicollinearity concerns]. VIF values were below [2.5], reducing concern about [collinearity among predictors].

Table [2] reports fixed-effects panel regression models predicting [firm innovation performance]. Model [1] includes [firm and year fixed effects and controls]. Model [2] adds [digital transformation intensity]. Model [3] adds [organizational routine updating]. Model [4] adds the interaction between [digital transformation] and [absorptive capacity]. We use Model [4] as the preferred specification because it tests the full theoretical model.

Hypothesis [1] predicted that [digital transformation] would be [positive] associated with [organizational routine updating]. As shown in Model [2] of Table [2], the coefficient for [digital transformation] is [positive] and statistically significant (β = [0.32], p < [0.01]). Substantively, a [one-standard-deviation] increase in [digital transformation intensity] is associated with a [X%] increase in [organizational routine updating]. Thus, Hypothesis [1] is supported.

Hypothesis [2] predicted that [organizational routine updating] would be [positive] associated with [firm innovation performance]. Model [3] of Table [2] shows that the coefficient for [organizational routine updating] is [positive] and statistically significant (β = [0.28], p < [0.01]). Thus, Hypothesis [2] is supported.

Hypothesis [3] predicted that [absorptive capacity] would moderate the relationship between [digital transformation] and [firm innovation performance]. Model [4] adds the interaction between [digital transformation] and [absorptive capacity]. The interaction term is [positive] and statistically significant (β = [0.15], p < [0.05]). Because the interaction term is significant, the main effects of [digital transformation] and [absorptive capacity] cannot be interpreted independently. To interpret this effect, Figure [1] plots the marginal effect of [digital transformation] on [innovation performance] at low (mean – 1 SD) and high (mean + 1 SD) levels of [absorptive capacity]. At low [absorptive capacity], the slope is flat and insignificant (β = [0.08], p = [0.31]). At high [absorptive capacity], the slope is steep and significant (β = [0.42], p < [0.01]). Thus, Hypothesis [3] is supported.

To address the concern that [our results are driven by reverse causality], we re-estimate our models using [two-stage least squares] with [instrument] as an instrument for [digital transformation]. The [digital transformation] effect remains [positive and significant], suggesting that [reverse causality] is unlikely to account for the main pattern.

To ensure that our results are not sensitive to model choice, we re-estimate our models using [random effects] and [Tobit]. The pattern of coefficients is [consistent], suggesting that [model choice] does not drive the findings.

Taken together, the results indicate that [headline answer supported by the reported estimates]. The supplemental analyses [strengthen / qualify / fail to resolve] concerns about [specific threat]. The evidence leaves [remaining unresolved question] open.
```
