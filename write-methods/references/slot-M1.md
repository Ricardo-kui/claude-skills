<!-- write-methods 槽位骨架 M1：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M1. 研究情境 / 实证背景

**通用填空段落**： ⭐ PREMIUM（28/28 篇范文使用，跨所有模型类型复现）

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

**自然实验/DiD 变体**（替换首句）： ✓ STANDARD（5-8 篇 DiD/自然实验范文复现）
```text
We examine [phenomenon] using [policy/event/institutional change] that altered [exposure/risk/incentive] across [units] and time. [Empirical setting] is well suited because [process] is well documented and [context controls] reduce [confounding concern].
```

**Staggered DiD + 二元结果 变体**（hoffmann2024 型，替换首句）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：自然实验/DiD 变体 + M7 非线性模型变体
```text
We examine [phenomenon] in the context of staggered adoption of [policy/law] across [jurisdictions] over [period]. Because [law] adoption is staggered across [N] [jurisdictions/states] between [start year] and [end year] — affording us both temporal and cross-sectional identifying variation — we use a difference-in-differences design in which [outcome] is regressed on [treatment indicator], [controls], and [fixed effects]. Since [outcome] is binary, we estimate [conditional logit / linear probability model] to assess whether [law] adoption affects the likelihood of [outcome]. The identifying assumption is that [law] adoption in any given [jurisdiction] is orthogonal to changes in [outcome] in the same [jurisdiction], conditional on [controls] and [fixed effects].
```

**实验变体**： ✓ STANDARD（5-6 篇实验范文复现）
```text
We test [theoretical claim] using a [laboratory/field/online] experiment. This design is strongest for assessing [internal validity], although it requires caution in generalizing to [boundary condition].
```

**多研究变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：省略
```text
Across [N] studies, we use complementary designs to test [theory] and address [validity concerns]. Study 1 examines [field/archival evidence], Study 2 tests [replication/design upgrade], and Studies [x–y] examine [mechanism/intervention/behavior].
```

**同时方程/SEM 变体**（替换整个 M1）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用填空段落 + M7 同时方程变体
```text
Our conceptual framework links [driver], [mechanisms], [outcome], and [downstream outcome]. We therefore specify a system of [N] equations to capture [direct path], [mediating paths], [downstream path], and [reverse/auxiliary path]. [Empirical setting] provides the data needed to estimate these relationships jointly.
```

**质性→量化混合方法变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M1 段落
```text
[Empirical setting A] provides an appropriate context for developing theory because [extreme manifestation] makes [underlying mechanism] observable. [Empirical setting B] then provides a complementary context for testing the theory because [phenomenon] occurs with sufficient frequency to enable large-N analysis. Together, these contexts provide a more comprehensive, grounded, and generalized test of new theory than either case study or deductive empirical work alone.
```
