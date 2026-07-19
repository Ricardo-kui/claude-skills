<!-- write-methods 槽位骨架 M3：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M3. 因变量

**通用填空段落**：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

**稀有结果/序数变体**（替换末句）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落
```text
Given the skewed distribution of [construct], we treat it as ordered categories that distinguish [low/mid/high states]. Because [outcome] is ordinal, coefficients indicate direction but substantive interpretation requires [marginal effects/predicted probabilities].
```

**事件研究变体**： ✓ STANDARD（3-4 篇事件研究范文复现）
```text
We measure [market/stakeholder reaction] as [CAR/abnormal response] around [event], using [benchmark model] to estimate expected returns. Expected returns are estimated over [estimation window] using [factor model]; abnormal returns are observed returns minus expected returns. We aggregate abnormal returns over [event window] to allow for [information leakage/dissemination].
```

**指数/净指数变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M3 段落
```text
Because the theory concerns both [positive actions] and mitigation of [negative actions], we construct [net outcome] from [strengths] and [concerns]. For each [category-year], we divide the number of [items] by the maximum possible number in each [category-year] to account for changes in measurement coverage. The net index subtracts [negative index] from [positive index] and sums across [categories].
```

**行为编码变体（实验）**： 🔬 EXPERIMENTAL（3-4 篇实验范文）⚠️ 保守替代：通用 M3 段落 + 说明编码者间信度
```text
We capture [outcome] behaviorally by [task/coding procedure], reducing reliance on self-reported intentions. Blind coders rated [behavior] on [scale]. We averaged ratings because interrater reliability was [acceptable statistic].
```

**文本构念测量变体**（M3 或 M4 均可使用，三段式效度链）： 🔬 EXPERIMENTAL（3-4 篇范文：Zhao 2022, Gamache 2020 等）⚠️ 保守替代：通用 M3 + 增加效度检验句
```text
Our dependent variable, [text-derived construct], is measured from [text source: earnings calls / press releases / 10-K / media / survey open-ends] using [method: dictionary / LDA / supervised ML / word embeddings]. We first [preprocessing: remove stop words / stem / lemmatize / exclude boilerplate]. We then [measurement step: count semantic similarity / topic proportion / trained classifier probability / cosine distance to anchor]. The measure captures [construct] because [theoretical link between text feature and underlying construct]. To validate the measure, we correlate it with [external benchmark: human-coded sample / established scale / related archival measure]; the correlation is [value] (p [relation] [threshold]). We also inspect [example excerpts] to confirm face validity. Higher values indicate [interpretation direction].
```

**LIWC 心理语言学构念测量变体**（如 Mannor et al. SMJ，Pfarrer et al. AMJ）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落 + 增加字典说明
```text
We used a [method: e.g., psycholinguistic] approach aimed at measuring [construct] based on the language [participants/actors] used during [data collection context]. [Software] contains established dictionaries of words that have been validated by [citation] to reflect underlying [psychological phenomenon]. For example, [prior study] used [software] to measure [prior construct]. We followed a similar approach in constructing our measures for [construct components]. [Component 1] was captured by assessing [language feature: e.g., use of positive emotion language and words associated with achievement]. The [dictionary] included [N] words (such as [examples]) whose average coefficient alpha was [value]. [Component 2] was measured by assessing [language feature: e.g., use of negative affective language and words associated with inhibition]. This component was calculated as the [relative percentage / raw count] of words contained in the [dictionary]. Next, we standardized the [component scores]. We then used these standardized scores to create a [net / composite] [construct] score, which was calculated as [formula].
```

**人工内容分析 + 编码者间信度变体**（如 Desai AMJ，Pfarrer et al. AMJ）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落 + 编码者间信度说明
```text
To develop the [variable], we collected [document type] from [source]. Searches were conducted on [databases] for [keywords / search terms]. [Relevance criterion] yielded [N] unique [documents]. [Construct] falls into [N] categories: [category 1: definition and example], [category 2: definition and example], and [category 3: definition and example]. I read and coded all [documents], and a colleague used the same coding scheme on [percentage]% of them, selected randomly. The two raters agreed on [N] of the codings, a level of agreement resulting in a Cohen's kappa of [value], suggesting [interpretation: e.g., high intercoder reliability]. The [variable] equals [operationalization: e.g., a count of the documents meeting any of the above criteria].
```

**推断二元结果变体**：
```text
Our dependent variable is [binary outcome construct]. Because [direct observation is unavailable / the construct is latent], we infer [binary state] from [observable signal: text / count threshold / categorical mapping]. We classify a [unit] as [state = 1] when [rule: keyword presence / count exceeds threshold / human-coded indicator / classifier probability > cutoff]. We set the threshold at [value] because [justification: distribution elbow / domain convention / validation against human coding]. To assess classification accuracy, we [validation procedure: manual audit of random sample / compare to gold-standard subsample / report precision-recall]. The inferred [binary state] aligns with [external indicator] for [percentage] of cases.
```

**多行为者因变量变体**：
```text
We measure [outcome] at the [actor B] level because [theoretical reason: actor B is the decision maker / actor B bears the consequence]. The dependent variable is [operational definition] from [source B]. For robustness, we also construct an alternative measure from [source C] using [alternative rule]. The correlation between the two measures is [value], indicating [acceptable / strong] convergent validity.
```

**测量防御三段式变体**（Pontikes 2012 模式：承认局限 → 论证最优可用 → 保守检验逻辑）： ✓ STANDARD

```text
We acknowledge that our measure of [construct] has limitations. [Specific limitation 1: e.g., the measure relies on observable classification claims rather than direct perceptual data]. [Specific limitation 2 if applicable: e.g., the measure captures only one dimension of a multi-dimensional construct]. These limitations stem from [inherent data constraint: e.g., the lack of fine-grained perceptual surveys for the full population over the study period].

Despite these limitations, this measure is the best available operationalization for three reasons. First, [reason 1: construct coverage — the measure captures the core theoretical mechanism because...]. Second, [reason 2: empirical precedent — similar approaches have been used in...]. Third, [reason 3: scope — the measure is available for the full population, avoiding selection issues that would arise from survey-based alternatives].

Importantly, the limitations of this measure bias against finding the hypothesized results. [Conservative test logic: e.g., measurement error in the independent variable attenuates coefficients toward zero / if anything, our measure undercounts the phenomenon, making significant findings harder to obtain]. Finding [significant results / the predicted pattern] despite this conservative bias strengthens confidence in the underlying relationship.
```

> **测量防御 QC**:
> - 三段结构必须完整：承认局限 → 论证最优可用 → 保守检验逻辑
> - 局限必须诚实（不能只说 "future research should improve"），且必须解释为什么在此局限下测量仍有效
> - 保守检验逻辑必须有方向性：为什么局限让显著结果更难（而非更容易）获得？
> - 如果局限可能让结果更容易显著，不能使用此变体——应改用通用 M3 + 诚实标注局限

**替代测量效度三角变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M3 段落
```text
To measure [construct], we used [primary operationalization] because [theoretical justification]. [Specific mechanism]. As an alternative measure of [construct], we used [alternative operationalization] because [additional theoretical justification]. This alternative is instructive because [why it differs from primary measure and what it adds]. Because [alternative measure] relies on a different [data source / institutional process] than [primary measure], finding consistent results across the two measures increases confidence that our findings reflect [construct] rather than [idiosyncrasy of primary measure].
```
