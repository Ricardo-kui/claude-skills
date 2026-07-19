<!-- write-results 槽位骨架 R1：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R1. 描述性统计 / 诊断导向

**通用填空段落**： ✓ STANDARD（15+/28 篇范文使用）

```text
Table [x] presents descriptive statistics and correlations for the variables used in our analyses. The correlations are generally consistent with our expectations and do not indicate [concern]. [Diagnostic] values were below [threshold], reducing concern about [routine issue]. The descriptive statistics also show [contextual pattern] that helps interpret the results below.
```

> **非 OLS 模型注**：对于 GLM、生存分析、计数模型等非 OLS 估计量，多重共线性诊断（VIF）较少在 R1 中报告；如有需要，可替换为 "we verified that [diagnostic] is not a concern"。
```

**Model-Free Evidence 结果报告变体**（复杂识别设计前，描述性分组对比）： ✓ STANDARD
```text
We begin with model-free evidence for the relationship between [predictor] and [outcome]. We split the sample into [high/low] groups based on [criterion] and compare [standardized outcome] across groups. The mean standardized [outcome] is [value] for the [high] group and [value] for the [low] group; a [t-test/Wilcoxon rank-sum test] indicates that the difference is statistically [significant/not significant] ([statistic] = [value], p [relation] [threshold]). This raw pattern is consistent with [theory], but it does not address [identification threat]; the formal estimates below speak to that concern.
```

**多研究变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R2 段落
```text
Table [x] presents descriptive statistics and correlations for Study [n]. [Diagnostic] values indicate that [multicollinearity/diagnostic issue] is [not a concern / addressed by additional checks].
```
