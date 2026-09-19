<!-- write-results 槽位骨架 R7：由 SKILL.md「槽位骨架加载」按路由决策加载。 -->

### R7. 稳健性 / 效度 / 敏感性检验

**问题—检验契约（强制）**：每个独立分析单元必须交代六项功能：

1. 具体问题路径：什么数据生成、样本进入、变量测量、时序或识别过程会产生何种偏差；
2. 受影响的推断：该问题威胁哪一假设、系数、样本或解释；
3. 若问题成立，数据中应出现什么诊断性表现；
4. 所用检验为什么能够区分该问题；
5. 结果及其幅度/不确定性；
6. 判决与仍未解决的边界。

这六项是逻辑功能，不要求六句。像 “A first concern is selection” 或 “firm-years enter the record” 但不说明进入机制、偏差方向和受影响推断的表述不合格。Selection 与 endogeneity 默认分节；不同内生性来源也应分别使用问题导向的小标题。

**通用填空段落（按威胁组织，每威胁一段）**：

**测量威胁**： ✓ STANDARD
```text
One concern is that our findings depend on the specific operationalization of [construct]. To address this concern, we re-estimate our models using [alternative measure] instead of [main measure]. The results are substantively unchanged, reducing concerns that [measurement choice] drives the findings.
```

**模型威胁**：
```text
To ensure that our results are not sensitive to model choice, we re-estimate our models using [alternative model, e.g., Tobit / Poisson / negative binomial / Cox]. The pattern of coefficients is [consistent/qualified], suggesting that [model choice] is unlikely to account for the main pattern.
```

**样本威胁 — 排除敏感性**： ✓ STANDARD（覆盖率口径见 corpus/_evidence_registry.yaml）
```text
Our results may be sensitive to sample composition. We exclude [specific subsample, e.g., high-tech firms / financial crisis years / outliers] and re-estimate our models. The results [remain consistent/are qualified], suggesting that [sample restriction] does not drive the findings.
```
> 注：该变体对应 exclusion-based 样本稳健性。理论驱动的子样本异质性检验见 `r7-experimental-variants.md` §样本威胁（🔬 EXPERIMENTAL，源自 Yuan et al. 2026 JOM）。

**时点威胁**： ✓ STANDARD
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

**稳健性的 alternative-strategy 组织变体**（当多种识别/估计策略相互验证时）： ✓ STANDARD
```text
To assess whether our findings are robust to alternative empirical strategies, we conduct four supplemental analyses. First, to address [temporal carryover / dynamic effects], we re-estimate the model using [lagged predictor / stock measure / Koyck model]; the coefficient on [focal predictor] remains [direction/status]. Second, to address [system dependence / correlated error structure], we estimate [simultaneous equation system / 3SLS / GMM] that allows [outcome processes] to be jointly determined; the results are [status]. Third, to exploit [exogenous variation / external shock] outside our main design, we compare [affected units] with [unaffected units] before and after [event] using [DiD/event-study] and find [status]. Fourth, to ensure that the [count/ordinal/censored] nature of [outcome] does not drive the results, we re-estimate using [Poisson / negative binomial / ordered probit / Tobit] and find that [status].
```

> **组织方式选择**：若稳健性检验回应的是同一识别策略下的不同**威胁**（测量/样本/时点/内生性），用 threat-based 段落；若稳健性检验对应的是不同**识别或估计策略**（长短期、联立方程、外生事件、非线性），用 alternative-strategy 段落。两者可混合，但每段只采用一种逻辑。

**受众类型 falsification 专用**（Pontikes 2012 模式，排除一类受众中的子类型混淆）： ✓ STANDARD

```text
One might argue that the results for [audience B] are driven not by [theorized mechanism] but by [confounded subtype within audience B: e.g., corporate VCs pursuing strategic goals rather than financial returns]. To rule out this alternative, we [empirical strategy: e.g., partition audience B into subtypes and re-estimate]. If [confounded subtype] were driving the effect, the coefficient for [focal predictor] should be concentrated in [subtype X] and absent in [subtype Y]. Instead, we find [consistency across subtypes / opposite pattern]. The coefficient for [focal predictor] is [result for subtype A] and [result for subtype B], both [direction/significance]. This pattern indicates that [theorized mechanism]—not [confounded subtype]—drives the main [audience B] result.
```

> **受众 falsification QC**: 仅当理论中区分了多类受众且某一类受众内部存在可观察的异质性时使用

**DiD 平行趋势专用**：
```text
To assess parallel trends, we estimate an event-study model with leads and lags around [event]. The pre-treatment coefficients are [not distinguishable from zero / stable], suggesting no detectable pre-treatment divergence. The post-treatment coefficients [emerge / increase / persist] after [event], which is consistent with [causal / timing claim]. The lack of pre-treatment movement reduces concern that [outcome trend] anticipated or caused [treatment].
```


**Top-firm 集中度 QC**:
- 必须报告被排除 firm 数量、合计占 [outcome] 比例、是否点名典型 firm
- **联合调节显著性衰减**须诚实报告（如 z=1.62 边际不显著），禁止只写 "results hold"
- 定位：样本组成威胁的 falling action，非新主效应


**替代解释两步排除 QC**（hoffmann2024 校准）:
- CONTROL 步必须使用与 main specification 相同的模型规格（仅增加替代机制变量）
- INTERACT 步的交互项方向必须有明确的理论预测（如果 rival 为真，交互应为正/负）
- 两步必须都通过才算排除——仅 CONTROL 步通过（系数不变）但 INTERACT 步显著 → rival 部分成立
- 替代机制变量不能与核心自变量高度相关（r > .7），否则 CONTROL 步的 "系数不变" 是多重共线性造成的假象
- 应引用 **prior paper 的 measure construction**（如 Mayo et al. 2022 dictionary）并说明 rival 的 **need vs willingness** 逻辑
- 收束句须区分 **lower need for [outcome]** vs **lower willingness**——排除 rival 后强化 theorized mechanism
- 联合调节在 CONTROL/INTERACT 后 **可分别报告**（单独模型显著性更高），与主表 Col 3–4 vs 5 节奏一致


**实验排除标准专用**： ✓ STANDARD（5-6 篇实验范文复现）
```text
Results were [unchanged/qualified] when [alternative exclusion/coding rule] was applied, suggesting that the findings are not driven by [exclusion choice].
```

**IV 有效性专用**：
```text
To assess whether [instrument] satisfies the exclusion restriction, we conduct [overidentification test / placebo test / sensitivity analysis]. The [Sargan / Hansen J] test yields [value] (p = [value]), [failing to reject / rejecting] the null that all instruments are exogenous. We also estimate the model using [alternative instrument / limited information maximum likelihood] and find that the [predictor] effect remains [status], reducing concern that [instrument validity] drives the results.
```


**稳健性检验汇总表变体（Aim / Tests / Results / Details 四列）**（Li et al. 2025 JSCM 型）： ✓ STANDARD candidate — 当稳健性/内生性检验 ≥4 项、跨多种威胁类型时，用一张表总览，正文再逐条展开
```text
Additional analyses (summarized in Table [N]) tested the robustness of the results and addressed endogeneity concerns.

| Aim | Summary of tests | Results | Details |
|-----|------------------|---------|---------|
| [threat 1: e.g., event-window choice] | [what was re-estimated and how] | [consistent / qualified pattern] | [Table / Appendix ref] |
| [threat 2: alternative measures of IVs] | [alternative operationalizations] | [identical / consistent] | [Table ref] |
| [threat 3: selection / endogeneity] | [Heckman two-stage / IV / matching] | [identical after correction] | [Tables ref] |
| [threat 4: alternative data source] | [re-estimate with public/alternative DB] | [similar; often larger] | [Table ref] |
| [threat 5: long-term / alternative DV] | [predict downstream performance] | [consistent direction] | [Table ref] |

[正文随后逐条展开关键检验的设计与结果细节，表格作为导航与总览。]
```
**关键特征**:
- 一张表把所有稳健性/内生性检验的"**目的—做法—结果—出处**"结构化呈现，读者与审稿人可一行一检验地核验覆盖面
- Aim 列按**威胁类型**组织（测量/样本/时点/内生性/替代数据/长期影响），与 R7 threat-based 逻辑一致
- Details 列引用具体表/附录，把分散在多张附录表的检验**可追溯地索引**
- 表格做总览，正文仍逐条展开关键检验的**细节与解释**——表格不替代文字论证

**实证证据与假设支持矩阵（Table 4 式）**：当论文有至少两个假设且补充分析不少于四项，或任何关键结果出现 mixed/qualified evidence 时，增加一张跨分析总表。它回答“哪项分析对哪条假设提供何种证据”，不能以稳健性检验数量投票。

```text
| Analysis | Problem addressed | H1 evidence | H2 evidence | Interpretation | Location |
|---|---|---|---|---|---|
| Baseline specification | Designated hypothesis test | supported / partially supported / not supported / n.a. | supported / partially supported / not supported / n.a. | Baseline verdict only | Table [x] |
| [Selection check] | [Exact entry/composition path] | stable / qualified / mixed / unresolved / n.a. | [...] | [What changed and residual boundary] | Table [y] |
| [Endogeneity check] | [Specific omitted-variable/reverse-causality path] | [...] | [...] | [...] | Table [z] |
```

矩阵中的 baseline 行使用 hypothesis verdict；后续行使用 evidence status。若替代测量翻号、IPW 改变方向或某项检验只适用于 H1，必须分别写为 mixed/qualified/n.a.，不得合并成 “all hypotheses supported”。

**适用**: 稳健性检验 ≥4 项、跨多种威胁类型的研究（event study + 内生性 + 替代数据 + 长期效应的组合尤为典型）；正文篇幅紧张、需要紧凑呈现多重检验时

**禁忌**:
- 表格不能替代正文对关键检验（尤其内生性/识别策略）的**细节论证**——审稿人仍需读到检验设计与系数
- Results 列不可只写 "consistent"——必须点明**在哪个维度**一致（符号/显著性/量级），并对部分一致的检验诚实标注 "qualified"（如某调节只在长窗口一致）
- 若某检验结果与主分析不一致，必须在表格和正文**同时披露**，不可只在正文脚注里提

**Specification-Curve / Epistemic Map 变体（可视化规格稳健性）**（Lee & Wang 2026 型, following King, Goldfarb & Simcoe 2021）： ✓ STANDARD 候选 — 当稳健性维度是"分析者规格选择"（clustering level × sample restriction × control set）而非具体识别威胁时，用一张图展示系数跨全部规格组合的稳定性。图设计纪律（CI 显示、纵轴起点、伦理四规则）见 `visual-evidence.md` §5。

```text
To further assess the robustness of our findings to analyst degrees-of-freedom in specification choice, we develop an epistemic map of the coefficient on [predictor] ([Citation: King, Goldfarb, & Simcoe, 2021]). Specifically, we plot the coefficient and its [95% confidence interval] across all combinations of [specification dimensions: e.g., four clustering levels × two sample restrictions × two control-set choices], yielding [N_total_models] specifications. [Figure X] shows that all [N_total_models] coefficients are [of the predicted sign / greater than zero], and [N_significant] of them are statistically significant at the [threshold] level. The coefficients cluster tightly around the main estimate (β ≈ [value]), indicating that the magnitude of the effect is not sensitive to how the analyst chooses among these reasonable specifications. These robustness checks collectively demonstrate that our findings are not driven by model specification or sample composition.
```

**关键特征**:
- **可视化而非表格**: 与 threat-based 表格（Aim / Tests / Results / Details）按威胁汇总不同，specification curve 把系数 + CI 跨全部规格组合绘制在一张视觉画布上，读者一眼看到系数分布与显著性边界
- **规格选择，非识别威胁**: threat-based 稳健性回应具体识别担忧（omitted variables, reverse causality）；specification curve 系统性地变化"合理的分析者选择"（聚类层级、样本限制、控制变量纳入）来展示结果不依赖任何单一选择
- **基数显式**: "16 models (4×2×2)" 让读者看到规格空间的精确枚举，防止选择性报告的印象
- **Mass sign test**: "All 16 coefficients > 0" 是简单但有力的汇总，与视觉互补——符号在全部规格空间稳定

**适用**: 观察性研究中分析者自由度较大（多种聚类层级、样本限制、控制变量规则都合理）的设计；尤其适用于面板 / FE 设计（facility / firm / industry / state 多种聚类层级并存时）

**禁忌**:
- 规格维度必须与识别威胁正交——specification curve **补充而非替代** threat-based 稳健性；若 reverse causality 是担忧，specification curve 单独不能回应
- 必须**全部 [N_total_models] 规格**都报告；不可选择性省略不显著的规格
- 图必须显示 CI，不能只画点估计——读者需同时判断符号稳定性与显著性稳定性


> **R7 段落级体裁 QC**（审计体裁）:
> - **Problem-path first**：开头必须命名具体因果/数据路径和受影响的推断，而不只是套用 "One concern is..."。禁止 table-first-without-problem，也禁止只有 selection/endogeneity/measurement 这类工具标签
> - **Diagnostic fit**：在结果前说明若问题成立会观察到什么，以及该检验为何能诊断它；检验名称本身不是论证
> - **可导航标题**：每一项实质不同的 selection、endogeneity、mechanism、heterogeneity 或 robustness 分析应有短小、问题导向的小标题
> - **单段单威胁**：一段内出现 ≥3 个异质检验（如替代测量 + 安慰剂 + 子样本挤在一段）→ 按威胁拆段；与 §0.2 长度上限联动
> - **残余边界**：不得用 “addresses endogeneity” 或 “results are robust” 收尾；说明结果降低了哪一担忧、仍不能排除什么
> - **预期行为说明（非误报）**：本 threat-first 标准高于多数已发表论文的稳健性写作——Yuan et al. (2026) 指出大多数研究的稳健性报告不足（多为 "We performed three robustness checks. First... Second... Finally..." 式 laundry-list / procedure-first 开篇）。因此对既有范文（如 Malshe and Agarwal 2015, JM 的 R7 段）触发 flag 属预期行为，目的是把 laundry-list 写法推向 threat-framed，而非描述当前常态

> 本 QC 同样约束 `r7-experimental-variants.md` 中实验变体段落的写作。
