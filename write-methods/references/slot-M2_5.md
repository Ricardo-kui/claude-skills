<!-- write-methods 槽位骨架 M2.5：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M2.5. Model-Free Evidence（可选 credibility-building 段落）

**通用填空段落**： ✓ STANDARD（IV/DiD/匹配/自然实验/复杂档案研究中常见）

```text
Before estimating the formal model, we present model-free evidence for the relationship between [predictor] and [outcome]. We split the sample into [high/low] groups based on [criterion: e.g., median / mean of predictor], yielding [N_high] and [N_low] observations. Because [confound] could mechanically produce a difference, we standardize [outcome] by [denominator] before comparing groups. The mean standardized [outcome] is [value] for the [high] group and [value] for the [low] group; a [t-test/Wilcoxon rank-sum test] indicates that the difference is statistically [significant/not significant] ([statistic] = [value], p [relation] [threshold]). This pattern is consistent with [theory], but it does not address [identification threat]; the formal estimates below speak to that concern.
```

> **使用条件**：Model-free evidence 仅作为**描述性可信度铺垫**，不能替代识别策略。若设计本身不涉及复杂识别（纯 OLS/FE 面板），此段落通常多余。

**IV/2SLS 变体**（替换首句和末句）：
```text
Before estimating the instrumental-variable model, we present model-free evidence to show that the raw data exhibit the pattern implied by our theory. We split the sample into [high/low] groups based on [predictor] and compare [standardized outcome] across groups. The descriptive pattern is consistent with [negative/positive association], but it does not establish causality; the IV estimates below address the endogeneity of [predictor].
```

**自然实验/DiD 变体**（替换末句）：
```text
Before estimating the difference-in-differences model, we plot [outcome] over time for [treated] and [control] groups. The raw trajectories appear [parallel] prior to [event], and [diverge/converge] afterward, consistent with [theory]. Formal event-study estimates in the Results section assess whether this visual pattern is statistically reliable.
```

**事件历史变体**（在通用段落中加入过程说明）： 🔬 EXPERIMENTAL（2-3 篇范文：Zhou 2017, Pontikes 2012 等）⚠️ 保守替代：通用 M2 + M3 生存分析变体
```text
[Authority/actor] opens [process] when [trigger]. The process ends when [event occurs] or [case closes/continues]. [Time outcome] is the elapsed time between [start date] and [event date]. Cases without [event] by [end of observation] are treated as [right-censored] because [logic].
```
