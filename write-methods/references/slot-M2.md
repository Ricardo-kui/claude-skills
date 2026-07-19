<!-- write-methods 槽位骨架 M2：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M2. 数据来源与样本漏斗

**通用填空段落**：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

**稀有结果变体**（在通用段落前插入）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + 脚注说明抽样策略
```text
Because [outcome] is rare, a simple random sample would yield too few [cases] for meaningful analysis; we therefore used [sampling strategy]. The screening criterion increased the likelihood of observing [rare phenomenon], but it did not determine [final outcome measure]. Because [sampling design] affects [representation/effect sizes], we interpret signs and significance but avoid overinterpreting magnitude.
```

**实证对象构建变体**（替换或前置）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M2 段落
```text
No authoritative database exists for [empirical object], so we constructed the dataset from [trace/source]. We used [trace/source] because it records [actor claim/action/evaluation] over time. From [raw records], we identified [entities], [events/labels/claims], and [time points]. We then transformed [raw trace] into [analytic variable] by [coding/aggregation rule]. To make the construction auditable, we define each step from [raw input] to [final measure].
```

**自然实验/DiD 变体**： ✓ STANDARD（5-8 篇 DiD 范文复现）
```text
Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [construct-relevant activity]. The observation window begins in [year] because [source/construct availability] and ends in [year] to capture [post-treatment horizon]. Treatment is observed for [treated units] after [event], while [control units] provide the counterfactual comparison. Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].
```

**Staggered DiD 样本周期双重辩护变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：自然实验/DiD 变体
```text
Our primary sample consists of [units] observed from [start year] to [end year]. We choose [start year] for two reasons: first, [data availability / quality reason]; second, this year coincides with [institutional event / regime change] that marks [theoretical relevance]. We end in [end year] to capture a meaningful post-treatment window following the last [law/policy] adoption in [last adoption year], while avoiding contamination from [confounding event: e.g., COVID-19 pandemic].

We exclude [excluded observations] from our sample because they involve [exclusion rationale: e.g., known product defects that already caused injuries/deaths]. This exclusion is theoretically motivated: [theory-based justification — e.g., when harm has already materialized, managers face reputational and legal pressures that override the discretion mechanisms our theory examines]. The final sample consists of [N] [unit-years] across [K] [units].
```

**多研究变体**（逐研究）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + M9 多研究过渡段
```text
Study [x] used [sample source]. Participants/observations were included if [criterion], yielding [analytic sample]. For supplemental analyses, we also use [source] to measure [assumption/mechanism/alternative outcome].
```

**PSM匹配面板变体**（在通用段落中加入匹配步骤）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M2 + M8 匹配检验
```text
To reduce selection bias, we first estimate propensity scores using [logit/probit] with [covariates] as predictors of [treatment/status]. We match [treated units] to [control units] using [method: one-to-one nearest-neighbor / kernel / caliper] matching with [calipersize] caliper on [distance metric]. After matching, the standardized bias for all covariates is below [threshold], and the [t-test / KS-test] indicates no significant difference in [covariates] between groups. The matched sample consists of [N] [unit-years / dyads / firms].
```

**层级回退匹配变体**（如 Pfarrer et al. AMJ，1:3 SIC 匹配 + 层级回退）： 🔬 EXPERIMENTAL（2 篇范文：Pfarrer et al., Mayo et al.）⚠️ 保守替代：通用 M2 + PSM 变体
```text
To construct the sample, we first identified [N] [treatment group] firms that [criterion]. We then matched each [treatment group] firm with [ratio: e.g., three] firms from the same [primary matching criterion: e.g., four-digit SIC code] that were similar in [matching variables: e.g., assets, revenues, and ROA]. Where appropriate matches were not found at the [primary level], we looked at [secondary level] and [tertiary level] for similar firms. Through this process we identified [N] matching firms at the [primary level], [N] at the [secondary level], and [N] at the [tertiary level]. A t-test comparing differences in [variable] revealed no significant differences between the [treatment] and [control] companies; however, in keeping with the predictions of prior [construct] research, there were significant differences in [variables]. [Attrition description]. These characteristics suggested our sample provided a [conservative/liberal] test of our hypotheses since they result in some restriction of range to primarily [sample characteristic].
```

**多行为者设计变体**（替换通用段落）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + 说明多数据源匹配
```text
Our data link [actor A], [actor B], and [actor C] through [matching key / dyadic structure]. We began with [starting universe of actor A] from [source A] over [period] and matched these to [actor B observations] from [source B] using [matching rule]. We then linked [actor C characteristics] from [source C]. The final analytic sample consists of [N] [dyads / triads / observations] in which [inclusion condition]. Because [actor B] characteristics are measured at [level], we aggregate [construct] to the [analysis level] using [aggregation rule].
```

**多源嵌套调查变体**（如 Mannor et al. SMJ，多方法数据 + 聚类标准误）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 + M7 多层模型/聚类标准误
```text
We used a multisource, multimethod data collection approach to test our ideas. This involved gathering data from [N] sources: [source 1: e.g., in-person interviews], [source 2: e.g., online surveys to subordinates], [source 3: e.g., hard-copy surveys to friends/family], and [source 4: e.g., archival company data]. Testing our theory required gaining access to [phenomenon], and our methodology was designed with this goal in mind. We established [N] criteria to govern recruitment: [criterion 1], [criterion 2], and [criterion 3]. We tested our hypotheses using [estimator: e.g., hierarchical linear regression]. To account for the nonindependence in our data (i.e., [nesting structure]), we specified [SE type: e.g., Huber/White/sandwich standard errors] using the [software option]. [Observations] were clustered by [clustering variable].
```
