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

**Staggered DiD + 二元结果 变体**（hoffmann_cheong_phan_zurbruegg2024 型，替换首句）： 🔬 EXPERIMENTAL（1 篇范文，2026-08-05 重蒸馏）⚠️ 保守替代：自然实验/DiD 变体 + M7 非线性模型变体
```text
We examine [phenomenon] by exploiting the staggered adoption of [policy/law] across [jurisdictions] between [first adoption year] and [last adoption year]. Staggered timing yields identifying variation from (1) within-[jurisdiction] before-after comparisons and (2) cross-[jurisdiction] comparisons among not-yet-adopted versus already-adopted units at each point in time. Exposure is determined by [assignment rule: e.g., state of incorporation], and the focal treatment term is [TreatGroup] × [Post], where [Post] switches on once a [unit]'s [jurisdiction] has adopted [law]. Because [outcome] is binary, we estimate a conditional logit panel model with year and industry fixed effects. We verify the quasi-experiment using model-free evidence, pretreatment trend tests, and a [jurisdiction]-reassignment placebo exercise before interpreting the regression estimates.
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
