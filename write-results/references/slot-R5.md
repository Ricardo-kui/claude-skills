<!-- write-results 槽位骨架 R5：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

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

**调节变量经济显著性：25th→75th 处理效应衰减变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1 篇范文；2026-08-05 重蒸馏校准）⚠️ 保守替代：通用 R5 段落
```text
For an economic interpretation of this result, we examine the effect size of [moderator] by generating average predicted probabilities across the sample distribution of [moderator]. We calculate the difference in average predicted probabilities when changing the value of [moderator] from that representing the 25th percentile to that representing the 75th percentile. Moving from [low-moderator label] to [high-moderator label] in this way reduces the impact of [treatment] on [outcome] likelihood by [X]%.
```

**调节 25th→75th 处理效应衰减 QC**（hoffmann2024 校准）:
- 度量对象是 **treatment 效应被 moderator 衰减的百分比**（impact attenuation），不是 treatment=1 下预测概率的百分点变化
- 必须写明 P25→P75 的操作化；通过 **average predicted probabilities** 跨样本分布计算，不能只用交互项系数
- 每个 moderator 单独报告衰减 %（如 10.56% / 10.01%）；可与 R3 交互显著性段紧邻
- 禁止误用为 "treatment=0 vs treatment=1 下概率差"——那是不同范式（见下方通用 R5 段落）

**调节变量经济显著性：25th→75th 预测概率对比变体**（通用；非 hoffmann 主范式）： 🔬 EXPERIMENTAL ⚠️ 保守替代：通用 R5 段落
```text
To assess the economic significance of the moderating effect, we calculate predicted probabilities of [outcome] at different combinations of [moderator] and [treatment]. Holding other variables at their means, moving from the 25th to the 75th percentile of [moderator] changes the predicted probability of [outcome] by [X] percentage points when [treatment condition] holds — an economically meaningful shift given that the unconditional probability in our sample is only [Y]%. In contrast, when [treatment condition] does not hold, the same change in [moderator] is associated with a [smaller / negligible] shift of only [Z] percentage points. This asymmetry confirms that [moderator] primarily operates through the [treatment → outcome] channel, as our theory predicts.
```

**调节预测概率对比 QC**:
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

**计数结果 cost-per-event 经济显著性专用**（把系数/幅度翻译为"每改变一个事件需要多少投入"）： ✓ STANDARD
```text
To translate the coefficient into a more interpretable cost metric, we divide the estimated effect by the unit cost of [predictor]. The results imply that an additional [monetary unit] of [predictor] is associated with approximately [1/N] fewer [outcome events]. Equivalently, approximately [monetary amount] more in [predictor] is associated with one fewer [outcome event]. Given that the average [outcome event] involves [scale: e.g., units affected / duration / scope] and an estimated per-event cost of [cost], this magnitude is economically meaningful.
```

> **cost-per-event QC**:
> - 必须明确 "one unit of outcome" 对应的实际含义
> - 投入与产出单位必须匹配（如美元投入 → 事件数变化）
> - 必须提供一个保守或文献锚定的 per-event cost 作为基准
> - 仅适用于计数或近似计数的结果（recalls, patents, lawsuits, product launches, failures）

**事件研究小效应经济显著性辩护变体（相对比例 + 绝对金额双翻译）**（li_narayanan_2026_jscm 型）： ✓ STANDARD candidate — 专门防御 event study 中第三方/溢出效应"统计显著但绝对值小"的审稿质疑
```text
Regarding the effect size, the results indicate that [recipients / third parties] experienced [−X% CAR / small coefficient] during [window / condition]. This corresponds to approximately [Y]% of the effect size of [focal actor]'s direct impact (i.e., [−Z% CAR / coefficient] during [same window]). Although [−X%] may appear small, in [market-value / dollar] terms, it translates into economically meaningful [losses / gains]. Given that the average [market value / revenue / scale] for the [recipient] sample was [$M] in [year], this effect implies an additional [loss / gain] of roughly [$K] for [recipients]. Thus, the results support H[X].

Prior studies have reported [abnormal returns / coefficients] of a similar magnitude. For [phenomenon], [Author Year] reported [−A%] for [focal actor] on [event day / window], and [Author Year] found [−B%] over [window]. Within [field] studies, [Author Year] found that [recipient] experienced [−C%] ... [additional benchmark]. [Optional: This pattern places our effect within the normal range of published event studies on [topic].]
```
**关键特征**:
- **双翻译防御小效应**: (a) 相对比例——把第三方/溢出效应表达为焦点方直接效应的一个可观分数（如本文约 40% = −0.222%/−0.552%），论证"虽小但相对直接效应并非微不足道"；(b) 绝对金额——把小 % 乘以样本平均市值换算成美元（如 $57.45M），论证"小 % = 大美元"。注意：正文用 −0.552% 作 OEM 基准，Table 3 Panel A 同窗口为 −0.516%——属原文表文不一致，引用时以正文叙述为准并注明
- **直接回应"你的 CAR/系数太小"的审稿质疑**: event study 中第三方/溢出/间接效应天然远小于焦点方直接效应，本变体是把"小"转化为"实质显著"的标准辩护
- **紧跟文献基准量级段**: 用一系列已发表 event-study 的可比量级（如 Javadinia −0.20%、Liu −0.69%、Jacobs VW 供应商 −2.69%/−0.35%/−0.17%）把本文效应置于正常区间，削弱"异常地小"的质疑

**适用**: event study / 股票市场反应研究中，效应（尤其第三方/溢出/间接效应）统计显著但绝对值小的情况；任何需要把小系数翻译为实质显著的研究

**禁忌**:
- 相对比例的"基准效应"（focal actor direct effect）必须用**同一窗口、同一模型**估计，否则分数（如 40%）不可比
- 绝对金额换算必须用样本的**平均**市值/规模并报告年份——不可用个别大公司市值夸大
- 不要只做一种翻译——相对比例（说服"不小"）与绝对金额（说服"很值钱"）**双重**才构成完整辩护
- 文献基准量级必须来自**已发表** event-study，不可用工作论文或媒体数字
- 若相对比例极低（如 <10% of direct effect）或绝对金额不具经济意义，应诚实表述为 modest（见"当效应较小时"变体），而非强行辩护


**WTP / coefficient-ratio 经济显著性专用变体**（Kim & Lee 2026 SMJ 型）： 🔬 EXPERIMENTAL（1 篇范文）— 把非货币属性翻译为"愿放弃的工资/价格百分比"+ 双 benchmark
```text
To quantify the trade-off between [non-pecuniary attribute] and compensation, we estimate the marginal willingness to pay (WTP) for [attribute] as the negative ratio of the coefficient on [attribute] to the coefficient on [log wage / price], following [Maestas et al. 2023 / Reshef & Knott 2025]. This ratio represents the implied percentage of [compensation / price] that [decision-maker] is willing to forgo to obtain [attribute]. Across [N] specifications ([LPM / conditional logit / mixed logit]), the implied WTP ranges from [low]% to [high]%, implying that [decision-makers] are willing to forgo approximately [low-high]% of [compensation] for [attribute]. Our implied WTP of [low-high]% is within the range reported in prior [experimental / survey] studies ([prior range with citations]); our estimate is on the [lower/upper] end, which may reflect [contextual explanation: e.g., higher stakes of full-time vs gig/hypothetical settings]. Nonetheless, our estimated WTP for [attribute] is [higher than / comparable to] benchmarks for other major [job / product attributes], including [benchmark_1 ([B1]%)] ([citation]) and [benchmark_2 ([B2]%)] ([citation]).
```
**关键特征**:
- **系数比翻译**: WTP = -beta_[attribute] / beta_ln[price] 把二元/离散选择结果翻译为经济意义百分比（hedonic wage / equalizing differences, Rosen 1986）
- **双 benchmark 防御**: (a) vs prior estimates 定位"lower end"（防御"太小"+归因于更高赌注）；(b) vs other job/product attributes 论证"higher than"（论证实质显著）——同时防御"太小"与论证"实质显著"
- **三估计器收敛**: LPM/conditional logit/mixed logit 量级区间收敛本身是稳健性证据
**适用**: 涉及 actor 在货币与非货币属性间权衡的研究（使命、远程办公、自治、ESG、低物理强度）；任何"愿放弃多少工资/价格换 attribute X"问题。配套 write-methods 见 非线性模型.md 变体10（WTP 三估计器估计设计）。
**禁忌**:
- 系数比依赖 beta_price 精确识别——price 测量误差会传染 WTP
- 双 benchmark 的"prior estimates"与"other attributes"必须来自已发表研究，不可用工作论文
- 若三估计器量级差异巨大，不可只报最 favor 的；须预告主估计选择依据
