---
result_type: "DiD"
status: EMERGING
source_papers:
  - lee_wu_bednar_orsc_18968 (Organization Science; DOI 10.1287/orsc.2024.18968)
  - hoffmann_cheong_phan_zurbruegg2024 (Journal of Marketing; DOI 10.1177/00222429241231236)
  - castellaneta_conti_kacperczyk_2017_smj (Strategic Management Journal; DOI 10.1002/smj.2533)
  - moon_2026_the_impact_of_legal_protection_of_trade_secrets_on (Journal of Marketing)
variants_count: 17
created: 2026-05-18
updated: 2026-08-23
---
# DiD — Results 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

槽位分布：

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| R2 | 4 | 3, 7, 11, 12 |
| R3 | 1 | 8 |
| R4 | 2 | 1, 4 |
| R7 | 9 | 5, 6, 9, 10, 13, 14, 15, 16, 17 |
| R8 | 1 | 2 |

### R2（4）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | DiD+Logit 分步入表 + 规格稳健 | DiD+Logit 稀有结果：无/有控制分步列表 + OR→相对概率经济显著性 + 低基准率诚实（副槽位 R3） | 把 table navigation 与 logit 经济显著性绑定，平行趋势/安慰剂留 Methods、用附录指针作 falling action | VERIFIED | Hoffmann et al. 2024 JM |
| 7 | 平均净效应开场 + 正负权变预告 | 对立机制/双向权变理论：先兑现平均净效应 climax，再括号预告"正负并存"引向交互段（副槽位 R3） | 区别于变体 3 标准主效应开场——平均净效应须来自交互规格均值处边际效应，非独立主假设 | EMERGING | Castellaneta et al. 2017 SMJ |
| 11 | 原始描述性证据开场（r2_did_raw_descriptive_preview） | 结果开篇先用裸数据报 control/treated 处理前后均值时序差异，再进入模型 | 区别于直接进模型（变体 3/7）——把处理前后趋势先立起来 | EMERGING | Moon et al. 2026 JM |
| 12 | 第一阶段选择回归内嵌（r2_did_selection_firststage_inline） | 结果段内嵌 disclosure/selection 第一阶段 probit（排他限制显著 + Wald 不弱工具），再进主效应 | 区别于压附录——第一阶段关键统计在正文给出 | EMERGING | Moon et al. 2026 JM |

### R3（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 8 | 交互假设完整四拍（1-SD 幅度，无交互图） | 主表分列交互、理论预测调节方向/幅度而非符号反转时：方向→交互显著→one-SD%→支持判断（副槽位 R4+R5） | 区别于变体 1（双端图+逐端核对）与变体 4（衰减%）——无图四拍；p=.062 须标 marginal | EMERGING | Castellaneta et al. 2017 SMJ |

### R4（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 交互项→幅度→双端条件效应→假设逐端核对 | 假设预测两端方向时必须逐端兑现：交互显著≠两端符号全兑现，意外端标 post hoc（副槽位 R5+R6） | 区别于变体 8 单侧四拍——含两端方向的假设必须逐端核对 | EMERGING | Lee, Wu & Bednar, OS |
| 4 | 双 moderator 衰减 + 90th 联合 switch-off | 三向交互：25th→75th 衰减百分比 + 双 90th 联合中和，须报 concurrent-cutoff 样本占比（副槽位 R5） | 区别于变体 1（双端符号核对）——强调 attenuation % 与文本式高百分位中和 | VERIFIED | Hoffmann et al. 2024 JM |

### R7（9）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | 替代解释两步排除（need vs willingness） | 排除替代机制：先控制 rival proxy，再交互检验，收束句强制 need vs willingness 语义区分 | 区别于泛化替代解释段——强制两步结构 + 语义区分收束 | VERIFIED | Hoffmann et al. 2024 JM |
| 6 | Top-firm 排除 + 联合调节边际不显著诚实 | 少数 firm 集中结果担忧 + 联合模型一边际显著时，用 qualified robustness 作标准 falling action | 区别于"all results hold"笼统收束——禁止笼统声明 | VERIFIED | Hoffmann et al. 2024 JM |
| 9 | 准实验识别威胁分节电池 | staggered policy/准自然实验正文分节识别电池：Matching→政治经济→供需→Placebo→Early/Late→替代测量，每节标题即威胁标签 | 区别于单威胁段落（placebo 单点等）——正文分节的完整识别电池，各节须对应真实威胁 | EMERGING | Castellaneta et al. 2017 SMJ |
| 10 | Null placebo（±k 期伪处理）识别确证 | ±k 期伪政策时点+预期 null：主效应与交互同时不显著，null 框定为识别确证而非假设检验 | 区别于注册表泛化 placebo 模板——固定 ±k 期 + 双 null + 识别确证定位 | EMERGING | Castellaneta et al. 2017 SMJ |
| 13 | 替代冲击复制（r7_did_alternative_shock_replication） | 用相关但不同的政策采纳作替代外生冲击，重估简单 DiD | 区别于换测量/换结局——换的是识别来源本身 | EMERGING | Moon et al. 2026 JM |
| 14 | Leave-one-out 处理单位排除（r7_did_leave_one_out_treated_unit） | 逐州/单位排除重估，排除结论被个别单位驱动 | 区别于 top-firm 排除（变体 6）——逐单位而非按规模 | EMERGING | Moon et al. 2026 JM |
| 15 | Stacked staggered DiD 稳健性（r7_did_stacked_staggered_robustness） | 交错处理下用 stacked cohort 设计作稳健主表 | 区别于 TWFE 诊断——现代化估计量进主表 | EMERGING | Moon et al. 2026 JM |
| 16 | 处理撤销反事实（r7_did_treatment_reversal_counterfactual） | 先采纳后撤销的州作反事实，预期反向效应 | 区别于 placebo（变体 10）——撤销是真实事件而非伪处理 | EMERGING | Moon et al. 2026 JM |
| 17 | 替代结局 placebo（r7_did_alternative_outcome_placebo） | 用无关替代 DV 排除"效应只是泛化成本上升"的替代解释 | 区别于 null placebo（变体 10）——换结局而非换时点 | EMERGING | Moon et al. 2026 JM |

### R8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 理论前提探测式补充证据链 | 机制补充分析逐项对应可观察理论前提（行为+沟通容量+中介关注），允许领域特定 null | 区别于罗列额外 DV——每个分析对应一个前提，domain-specific null 缩窄理论适用范围 | EMERGING | Lee, Wu & Bednar, OS |


## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `DiD` 专用变体）。

## 证据节奏摘要

- 条件化 DiD 不能停在交互项显著：需翻译幅度、画出条件效应两端，并逐端核对理论预测。
- **DiD+Logit 稀有结果**：OR→相对概率翻译后须诚实承认低基准率下的 modest absolute magnitude，再用 stakes 论证 practical importance（Hoffmann 2024）。
- **双 moderator 分步入模**：因 multicollinearity 先单独再联合；联合模型显著性衰减须如实报告。
- 补充分析可从“另一 DV”升级为“逐项探测理论前提”，但关联性结果只能提高机制可信度。
- 设计诊断按威胁组织；Web Appendix 指针式 robustness 可作为 falling action，但正文须保留核心 threat 句。
- 传统 TWFE 权重分解只作诊断，不作现代识别修复。
- **对立权变理论的平均净效应开场**（Castellaneta et al. 2017）：先报平均处理效应为正/负，再明示“正负权变并存但净效应仍为 X”，然后逐假设展开交互四拍。
- **无交互图的 1-SD 百分比四拍**（同文）：方向→交互显著→one-SD 幅度%→支持判断，适合主表分列交互而非 R4 图示。
- **识别威胁分节电池**（同文）：Matching / political economy / supply-demand / placebo / early-late / alt measures；null placebo 确证识别而非检验假设。

## 累积变体

<!-- distill-results-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: R?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

### 变体 1：交互项 → 幅度 → 双端条件效应 → 假设逐端核对（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**原始句锚点**: "In Model 2, we introduce the interaction between post local newspaper declines and national newspaper coverage, revealing a positive moderating effect (β = 0.38, p < 0.001). … When national newspaper coverage is higher, the decline of local newspapers appears to have a positive relationship with CSR engagement. In contrast, when national newspaper coverage is lower, the decline of local newspapers has a slightly negative relationship with CSR engagement."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R4 + R5 + R6

**骨架**:
> "The interaction between [treatment] and [moderator] is [direction] and statistically significant (β = [value], p [threshold]). Moving [moderator] from [low benchmark] to [high benchmark] changes the estimated treatment effect by [substantive magnitude]. Figure [x] shows that the treatment effect is [sign/direction] when [moderator] is high and [sign/direction] when it is low. The high-[moderator] pattern is consistent with the predicted [path A]. However, the low-[moderator] effect is [observed pattern], rather than the predicted [pattern]; therefore, the interaction supports the contingency but Hypothesis [x] receives only partial/no support as stated. [Clearly labeled post-hoc explanation, deferred or bounded]."

**与原骨架差异**: 把“交互项显著”与“完整支持符号反转假设”分开判定；假设若预测两端方向，必须逐端兑现。

**关键诚实规则**:
- significant interaction ≠ both simple effects have the predicted signs。
- 经济幅度要说明基准范围；不能只把 β 换算为百分比而不说相对谁。
- 意外一端的解释必须标为 post hoc，且不能回写成事前假设。

### 变体 2：理论前提探测式补充证据链（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**原始句锚点**: "To empirically assess this assumption, we regress national newspaper coverage, analyst coverage, and credit rating coverage on firms' CSR engagement … higher CSR engagement is indeed associated with increased national newspaper coverage and greater analyst attention, but not with higher credit rating coverage."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R8（Mechanism / Corroborative Evidence）

**骨架**:
> "We next probe the observable implications of the proposed mechanism. First, we examine [communication/trace outcome] to assess whether actors adjust not only [core behavior] but also its visibility. Second, we test whether [communication capacity] conditions the response as the theory implies. Third, we examine whether [behavior] is associated with subsequent attention from each proposed intermediary. The pattern for [intermediaries A/B] is consistent with the visibility premise, whereas the null result for [intermediary C] suggests that this actor may operate through [domain-specific alternative function]. These analyses corroborate selected premises but do not identify the causal mechanism."

**与原骨架差异**: 不是罗列额外 DV；每个分析对应一个明确可观察的理论前提，并允许不同中介出现领域特定 null。

**关键诚实规则**:
- 将行为回归到中介关注度的关联不能证明 `behavior → visibility → outcome` 因果链。
- domain-specific null 应缩窄理论适用范围，不应被“总体大致一致”吞掉。
- 补充结果若与主结果同源或同样受未观测混淆，只能称 corroborative / consistent with。

### 变体 3：DiD+Logit 分步入表 + 无控制/有控制规格稳健（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)

**原始句锚点**: The odds ratio for the UD_LAW × POST_ADOPTION coefficient in Column 2 is .4093, implying that firms in UD law states are, on average, 29.04% less likely to announce a product recall relative to firms headquartered in states that have not adopted UD laws.

**验证状态**: EMERGING（单篇；`section_variant`；2026-08-05 重蒸馏校准）

**槽位**: R2 + R3

**story_fidelity**: climax（H1 DiD 主效应）+ falling_action（Col 1–2 规格稳健）

**骨架**:
> "Table [x] reports DiD regression results for [outcome] (H1–H3). Columns 1 and 2 show models without and with control variables. Across specifications, [treatment × post] is consistently [direction] and significant, supporting H1. For economic interpretation, the odds ratio is [OR]; firms in treatment states are [X]% [less/more] likely to [outcome]. While sizeable in relative terms, the absolute probability change is modest given the low base rate ([Y]%). However, given the serious consequences of [behavior], we document an important effect."

**与原骨架差异**: 把 **table navigation（分步入模）** 与 **logit 经济显著性（OR→相对概率+低基准诚实）** 绑定；平行趋势/安慰剂留在 Methods，Results 用 appendix 指针作 falling action。

### 变体 4：双 moderator 25th→75th 处理效应衰减 + 90th 联合 switch-off（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)

**原始句锚点**: We calculate the difference in average predicted probabilities when changing the value of INST_OWNERSHIP from that representing the 25th percentile to that representing the 75th percentile. Moving from firms with lower to higher institutional ownership in this way reduces the impact of UD law adoption on product recall likelihood by 10.01%.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R4 + R5

**骨架**:
> "H[x] predicted that the [direction] association between [treatment] and [outcome] is weaker when [moderator] is [high]. The three-way interaction is [sign] and significant. Moving [moderator] from the 25th to the 75th percentile reduces the impact of [treatment] on [outcome] by [X]%. As a final sensitivity analysis, when both [moderator 1] and [moderator 2] exceed their 90th percentiles, the treatment effect is neutralized—but only [Z]% of observations meet both cutoffs; the effect extends to almost all firms."

**与原骨架差异**: Lee-Wu-Bednar 变体 1 要求双端条件核对；Hoffmann 变体强调 **attenuation %** 而非 simple-slope 符号，switch-off 为 **文本式高百分位中和 + 分布重叠 caveat**，非四场景图。

**诚实边界**: 90th 联合阈值下的 null 不能升级为“moderator 普遍消除效应”；必须报告 concurrent-cutoff 样本占比。

### 变体 5：替代解释两步排除（need vs willingness）（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)

**原始句锚点**: That is, it is unlikely that the documented effect of the reduced threat of managers being sued by shareholders on firms' likelihood to recall is an artefact of a lower *need* for recalls instead of reflecting a lower *willingness* of managers to recall.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R7

**骨架**:
> "A plausible alternative is that [rival mechanism: e.g., operational improvement → higher quality → lower need for recalls] rather than [theorized mechanism: lower willingness] drives the main effect. We rule this out in two steps. First, we CONTROL for [rival proxy]; [treatment × post] remains [direction] and significant with qualitatively similar magnitude. Second, we INTERACT [treatment × post] with [rival proxy]; the interaction is not significant, inconsistent with the rival account. Combined, it is unlikely that lower need rather than lower willingness explains the findings."

**与原骨架差异**: 收束句强制 **need vs willingness** 语义区分；follows Mayo et al. (2022) measure citation pattern。

### 变体 6：Top-firm 集中度排除 + 联合调节边际不显著诚实报告（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)

**原始句锚点**: When including both moderators simultaneously, the interaction effect of customer focus remains significant, while that of institutional ownership only just fails to reach significance at conventional levels (z-statistic = 1.62). In sum, we conclude that our results are generally robust.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R7

**骨架**:
> "One might be concerned that a few firms account for a substantial share of [outcomes]. Excluding the top [N] firms ([X]% of [outcomes]) and re-estimating, baseline and separate-moderator results hold. In the full model, [moderator A] remains significant while [moderator B] only just fails conventional significance (z = [value]). We conclude results are generally robust."

**与原骨架差异**: 把 **qualified robustness**（联合模型一边际显著）作为标准 falling action，禁止 "all results hold" 笼统收束。

### 变体 7：平均净效应开场 + 正负权变预告（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)

**原始句锚点**: This suggests that whereas a stronger trade-secrecy protection might produce both positive and negative effects (see results below), the positive effect is on average stronger than the negative one, generating a net increase in the firm market value.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R2 + R3

**story_fidelity**: climax setup（headline average answer）→ rising into contingency climax

**骨架**:
> "Table [x] presents the main [OLS / DiD-equivalent] results for [outcome]. The impact of [treatment] is, overall, [positive/negative]. Based on [column], [treatment] [increases/decreases] [outcome] of the average [unit] by about [X]% (keeping other covariates at their means). This suggests that whereas [treatment] might produce both positive and negative effects (see results below), the [positive/negative] effect is on average stronger than the opposing one, generating a net [increase/decrease] in [outcome]."

**与原骨架差异**: 标准 DiD R3（变体3 / baseline estimate）直接进入主效应或交互；本变体专为**对立机制/双向权变理论**——先兑现平均净效应 climax，再用括号预告“正负并存”，把读者导向后续 H1–H3 交互段落，而不是把平均效应当作独立主假设。

**诚实边界**:
- 平均净效应必须来自含交互的规格在均值处的边际效应，或明确标注为 unconditional average；不可在交互显著后仍把主效应项当作“独立平均效应”解释。
- “positive outweighs negative” 是叙事预告，不是第三个假设；不得升级为未经检验的元假设。

### 变体 8：交互假设完整四拍（1-SD 百分比幅度，无交互图）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)

**原始句锚点**: The positive coefficient of the interaction term implies that, as worker mobility increases by one standard deviation (equal in our sample to 0.061), the treatment augments the firm market value of the focal company by about 18 percent.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R3 + R4 + R5（幅度嵌入）

**story_fidelity**: climax（逐假设 headline answer）

**骨架**:
> "According to Hypothesis [x], [treatment] should [increase/decrease] [outcome] when [moderator] is [high/low]. Results in [column] of Table [x] provide support for Hypothesis [x]: the interaction between [treatment] and [moderator] is [positive/negative] ([p-value / p < threshold]). The [sign] coefficient of the interaction term implies that, as [moderator] [increases/decreases] by one standard deviation ([SD value]), the treatment [augments/reduces] [outcome] by about [Y]%. [Repeat for each contingency hypothesis, then close:] Overall, the results provide support for our hypotheses by documenting the heterogeneous effects of [treatment] on [outcome]."

**与原骨架差异**: Lee 变体1 要求双端条件图 + 逐端符号核对；Hoffmann 变体4 强调衰减%与高百分位中和。本变体是**无图、主表分列交互**的完整四拍（方向→交互显著→one-SD%→支持），适合理论预测的是“调节方向/幅度”而非符号反转两端。

**诚实边界**:
- 若 p 仅达 .10 惯例（如 p = .062），须标明 marginal / conventional .10，不得与 p < .05 的假设使用同等“provide support”强度而不加限定。
- one-SD 翻译必须报告样本 SD；百分比须明确是 outcome 的相对变化还是百分点。
- 显著交互 ≠ 已核对两端 simple effects；若假设含两端方向，改用变体1。

### 变体 9：准实验识别威胁分节电池（Matching→政治经济→供需→Placebo→Early/Late→替代测量）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)

**原始句锚点**: Our identification strategy assumes that the enactment of the UTSA laws is exogenous with respect to firm and state characteristics associated with firm market value. … In the following, we discuss potential identification concerns and describe how our specification helps address them.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R7

**story_fidelity**: falling_action / unravel（逐威胁测试 climax 答案）

**骨架**:
> "### Validity of the identification strategy
> Our identification strategy assumes that [treatment] is exogenous with respect to [unit/state] characteristics associated with [outcome]. We discuss potential identification concerns and perform additional analyses.
>
> ### Matching
> One concern is that treated and control [units] differ ex ante on characteristics that correlate with both treatment and [outcome]. We re-estimate baseline specifications after coarsened exact matching (CEM) on [ex-ante value proxy] and [risk proxy]. Results remain robust ([appendix table]).
>
> ### Political economy of [policy]
> Another concern is that state-level economic or political conditions drive both [policy enactment] and [outcome]. Qualitative search finds no evidence of [focal-actor lobbying]. Linear probability / hazard models of enactment on [GDP], [industry activity], and [governor party] show no significant predictors of treatment timing ([table]).
>
> ### [Market] supply and demand
> [Treatment] might change the supply or demand of [units], mechanically shifting [outcome]. Re-estimating models for [supply/demand proxies] shows [treatment] is not correlated with these quantities ([table columns]).
>
> ### Placebo tests
> To rule out chance significance, we create placebo treatments [k] periods before and after the true change. Neither the direct placebo impact nor interactions are significant ([appendix table]).
>
> ### Late versus early [policy] enactment
> Later adoptions might be anticipated. Splitting treatment into early vs late (e.g., at the median enactment year) yields same-signed, quantitatively similar estimates; a t-test does not reject equality of main or interaction effects.
>
> ### Robustness checks / Alternative measures
> Re-estimating with alternative [moderator], [DV censoring], and [treatment intensity index] leaves findings substantially unchanged ([appendix tables])."

**与原骨架差异**: 现有 DiD R7（placebo 单点、rival-mechanism 两步、top-firm 排除）是**单威胁段落**；本变体是**正文分节的识别电池**——每个小节标题即威胁标签，适合 staggered policy / 准自然实验且不以 event-study 图为唯一识别展示的论文。

**诚实边界**:
- 每个小节必须对应真实威胁；禁止为凑结构而堆砌无威胁的“再做一次”。
- 若设计本应报告 event-study / 平行趋势而仅用本电池替代，须在 Methods/局限中说明为何适用（例如非经典单位×时间面板），不得暗示已完成平行趋势检验。
- Appendix-only 结果须在正文保留一句结论，不能只写“see appendix”。


### 变体 10：Null placebo（±k 期伪处理）作为识别确证（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)

**原始句锚点**: We expect the fake treatment to have a weaker (or even null) effect on the dependent variable when compared with the actual treatment. Consistent with this idea, we find that neither the direct impact of our 'placebo treatment' nor any interaction is significant; results are shown in Table S3.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R7

**story_fidelity**: falling_action（unravel chance / spurious timing）

**骨架**:
> "To rule out the possibility that our treatment generates statistically significant results merely by chance, we create a placebo treatment by pretending that the change occurs [k] [years/periods] before and [k] after the real year of change. We expect the fake treatment to have a weaker or null effect relative to the actual treatment. Consistent with this idea, neither the direct impact of the placebo treatment nor any interaction is significant ([appendix table])."

**与原骨架差异**: 注册表既有 `r7_did_placebo_permutation` 为泛化安慰剂/置换模板；本变体固定为 **±k 期伪政策时点 + 预期 null + 主效应与交互同时不显著**，并把 null 明确框定为**识别确证**（chance/spurious timing），而非假设检验或理论支持。

**诚实边界**:
- Placebo null ≠ 假设得到支持；只能降低“结果纯属偶然/时点错置”的顾虑。
- 必须预先声明期望（weaker/null）；若 placebo 显著，不得沉默，应报告为 identification threat。


### 变体 11：r2_did_raw_descriptive_preview（moon2026）

**槽位**: R2

**模板/骨架**:
> "Before discussing the results of the DiD models, it is important to explore the descriptive evidence with raw data to assess the impact of [treatment] on [outcome] ([citation]). Accordingly, we first examine the average [outcome] of the control and treated [units] [k] years before and after [treatment]. Figure [x] shows that the average [outcome] of the control [units] remains largely unchanged before and after [treatment], but that of the treated [units] [increases/decreases] following [treatment] (see Figure [x])."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 12：r2_did_selection_firststage_inline（moon2026）

**槽位**: R2

**模板/骨架**:
> "To account for the potential selection bias arising from [disclosure/selection channel] by [units], we estimate a first-stage probit model where we find that both [exclusion restriction 1] (coef = [value], p = [threshold]) and [exclusion restriction 2] (coef = [value], p = [threshold]) are significant predictors of [selection outcome] (for details, see [appendix]). Importantly, the results of the Wald test for both instruments (chi2([df]) = [value], p = [threshold]) provide empirical support that weak instruments are unlikely to be a concern. To test the main effect hypothesis [H1], we examine the results of the main effect model in [Model x] of Table [y]."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 13：r7_did_alternative_shock_replication（moon2026）

**槽位**: R7

**模板/骨架**:
> "In addition, we also test if our conclusions are robust in an alternative empirical setting that uses [related but distinct policy adoption] as an alternative shock. To this end, we identify [N] observations of [n] [units] headquartered in [state] that adopted [alternative policy] in [year] as the treated group and [N] observations of [n] [units] headquartered in [states] as the control groups that never adopted [alternative policy]. We estimate the simple diff-in-diff models on these alternative treated and control groups and find consistent empirical support for our thesis (see [appendix table] for more details)."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 14：r7_did_leave_one_out_treated_unit（moon2026）

**槽位**: R7

**模板/骨架**:
> "The focal model examines the impact of [treatment] on [outcome] in [N] treated [states/units]. A potential critique is that our conclusions are driven by variations in a particular [state/unit]. Therefore, we construct alternative treated groups that exclude one treated [state/unit] at a time from our sample and re-estimate the models using [N] different samples ([citation]). Consistent with our expectations, we continue to find that [treatment] has a [positive] effect on [outcome] (see [appendix table])."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 15：r7_did_stacked_staggered_robustness（moon2026）

**槽位**: R7

**模板/骨架**:
> "Stacked diff-in-diff. In examining the impact of treatments that are staggered across time, a potential alternative estimation strategy would be to employ a stacked DiD model ([citation]). To this end, we construct an event specific sample with [units] in one [treatment state] as treated groups and those that never [receive treatment] as control groups, which forms a cohort, and stack all cohorts to construct the stacked dataset. The stacked DiD model incorporates the cohort-specific [unit] and [time] fixed effects and enables us to use relative time dummies, which allows for potentially cleaner comparison between the treated and control groups and alleviates the potential concern about the staggered treatment design ([citation]). As Model [x] in Table [y] shows, we consistently find support for the [positive/negative] effect of [treatment] on [outcome] in the stacked DiD models."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 16：r7_did_treatment_reversal_counterfactual（moon2026）

**槽位**: R7

**模板/骨架**:
> "Counterfactual analysis: treatment reversal. In the treated groups of our sample, [units in states/regions A and B] first [adopted/recognized] [treatment] in [year] and then rejected it later in [year]. These rulings that reject [treatment] offer a natural empirical setting for counterfactual analysis. If [treatment] increases [outcome] of [units], [treatment] rejection is expected to have the opposite effect on [outcome]. To test this expectation, we focus on [units] in the [states] that [adopted treatment] in the post-treatment period. Specifically, we use [units] in [reversal states] as the treated groups and those in [still-treated states] as the control groups and estimate [equation]. As shown in Model [x] in Table [y], we find that [treatment] rejection has a significant [negative/opposite-sign] effect on [outcome] (coef = [value], p = [threshold]), which is consistent with our expectations."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 17：r7_did_alternative_outcome_placebo（moon2026）

**槽位**: R7

**模板/骨架**:
> "Placebo tests with alternative dependent variables. A potential alternative explanation for the observed [positive] effect of [treatment] on [outcome] could be that it reflects a general increase in [overall operating costs / broader category] following [treatment]. ... Therefore, we conduct an additional analysis using alternative dependent variables that reflect [general business expenses]. Specifically, we use [alternative DV 1] and [alternative DV 2] as the alternative dependent variables. As shown in Model [x] of Table [y], we do not find empirical support for the alternative argument that [treatment] is likely to lead to a general increase in [broader outcome category] (i.e., the effect of [treatment] on [alt DV 1] = [value], p = [n.s.]; on [alt DV 2] = [value], p = [n.s.])."

来源：Moon et al. (2026, Journal of Marketing)。


## 反模式（zhang-idd-advertising-rejected 拒稿案例补充，2026-08-23）

来源：用户稿件 "Beyond Employee Retention..."（SMJ/JAMS 两轮拒稿）对照 Moon et al. (2026, JM) 的复盘；故事卡 `story-blueprints/v4/blueprints/zhang-idd-advertising-rejected.md`。

| 反模式 | 问题 | 应改为 |
|--------|------|--------|
| **全模型主效应符号反转不叙述** | 调节全模型中处理主效应由正转负（如 −0.101, p=.008），正文仍写 "results remain robust"；附录稳健性表（D1–D4）系统性复现负主效应仍无叙述 | 主效应变号必须在 Results 正文显式讨论：H1 是普遍效应还是条件效应；报告调节变量均值处的净效应及其显著性 |
| **正文与附录表述矛盾** | 附录表主效应为负且显著，正文/附录文字却写 "main effect remains positive and significant"——从漏叙述升级为误描述 | 投稿前逐表核对正文措辞与附录系数的符号和显著性；数量词（"三个稳健性检验"）与实际个数一致 |
| **post-treatment 交互当机制确证** | 用被处理影响过的变量（广告支出）与处理交互预测下游结果，宣称 "confirms the mechanism"——bad-controls，两轮评审当场抓获 | 交互结果降级为条件性证据（only-when 措辞）；机制主张必须由独立测度（文本、调查、一阶段）承接 |
