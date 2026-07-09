---
design_type: "面板数据-OLS"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership"
  - "darby2025_activist_investors_supply_chain_failures"
  - "eilert2017_recall_timing_stock_market"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
  - "mannor_wowak_bartkus_gomez-mejia_2016_heavy_lies_crown_smj (Strategic Management Journal): multi-channel elites recruitment, nested cross-section clustered SE, retrospective bias triangulation"
  - "desai_2011_mass_media_massive_failures_amj (Academy of Management Journal): institutional break sample defense, conditional FE negative binomial zero-panel audit"
  - "pfarrer_pollock_rindova_2010_tale_of_two_assets_amj (Academy of Management Journal): matched sample hierarchical fallback + matching balance conservative test"
  - "li_chiu_kong_cropanzano_ho_2026_jom (Journal of Management): RE triple defense (theory+Hausman+ICC), full-spectrum 19 controls each with because clause, RavenPack event controls, CEO Big 5 controls"
  - "cui_yang_vertinsky_smj_attacking_partners (Strategic Management Journal): dyad FE + dyad clustered SE, multi-source alliance database cross-validation, factor-score multidimensional DV, single-industry setting dual-phenomenon defense"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): executive confidence option moneyness operationalization, model-free evidence preview, three-way interaction setup with mean-centering"
variants_count: 21
created: 2026-05-18
updated: 2026-07-08
---

# 面板数据-OLS — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 填空段落骨架 → `面板数据-OLS`。

## 设计特征摘要

- **because密度标杆**: MVP30顶刊中位数~35%，优秀>=60%，Darby2026达~85%
- **控制变量层级**: recall-level → executive-level → firm-level → board-level → ownership concentration
- **because逻辑**: 每个控制变量需回答"为什么影响DV"和"为什么与IV相关"
- **跨论文复现率**: 分层控制变量结构在 4/4 产品召回顶刊论文中完全复现

## 累积变体

### 变体 1: 控制变量分层 because 结构 (4/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Eilert2017 JM / Darby2023 MSOM
**验证状态**: 通过
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M6
**骨架**:
> We included a broad set of control variables that influence [DV] directly and those that help address alternative explanations ([methodology_citation]); in our case, variables correlated with [IV] that may also influence [DV]. We first included [level_1]_level factors that may influence how [DV] is handled. To address alternative explanations stemming from [concern_1], we included [control_1], measured as [definition] ([citation]), and [control_2], measured as [definition] ([citation]). [IV]_related_rationale: [actor] may be sensitive to [outcome] ([citation]), so it is important to control for [related_factor] as well as the scale and scope of a particular [phenomenon].
>
> We also controlled for [level_2]_level characteristics that have been shown to influence [DV] using data from [source]. In doing so, we aimed to address alternative explanations related to [concern_3] and [concern_4], which are important [theory] considerations for [actor] ([citation]). [control_4] was measured as [definition] ([citation]).
>
> [Actor_type] can influence both [IV] and [DV], so [number] [actor_type] characteristics were controlled for. [Control_7] was measured as [definition] ([citation]). [Control_8] was measured as [definition] ([citation]).
>
> Lastly, we included firm and year fixed effects to account for [time_varying_concerns] as well as [time_invariant_concerns] ([citation]).
**与原骨架差异**: 这是面板数据控制变量的**黄金标准结构**。关键要素：(1) 总起句锚定方法论引用(如Shang & Rönkkö 2022)；(2) 按分析层级递进呈现；(3) 每个变量有显式because逻辑；(4) 过渡句衔接各层级("We also...", "Beyond...", "Lastly...")。because密度目标：>=60%为优秀。4/4复现确认此为产品召回研究**必写模块**。

### 变体 2: 样本交集漏斗 (3/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Darby2023 MSOM
**验证状态**: 通过
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M2
**骨架**:
> The intersection of these datasets resulted in a sample of [N] [phenomenon] across [N] firms from [year_start] to [year_end].
**与原骨架差异**: 产品召回论文的**常见缺陷**——缺少起始N到最终N的逐层排除audit trail。理想写法应补充："Of the [N] initial observations, [N] were excluded due to [reason_1], [N] due to [reason_2], resulting in a final sample of [N]."
**诚实边界**: 若数据为FOIA请求获得的一手数据，起始N可能无法精确确定，需在Limitations中说明。

### 变体 3: IV 选择三层 because 论证链
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，但生成力极高)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> We used [IV] as our primary measure because it is a broad, comprehensive measure that reflects the [number] related, but distinct, mechanisms we theorized about in [Hypothesis]—[mechanism_1], [mechanism_2], and [mechanism_3]. First, [theoretical_rationale_1] ([citation]), and research indicates that [IV] is one of the most effective tools to do so ([citation]). Second, research suggests that [IV_property_2] ([citation]). Third, [IV_property_3] ([citation]). Overall, prior studies conclude that [IV] is key to understanding [theoretical_consequence] ([citation]), which is why we use it as our primary measure, although we examine alternative measures in [location].
**与原骨架差异**: 一般论文在M4中简单报告"We measure X as Y"，而此骨架构建了从构念→操作化→多机制映射的完整论证链。适用于任何**单一操作化同时代理多个理论机制**的情境。关键策略：(1) 理论机制枚举（"three related, but distinct, mechanisms"）；(2) 每个机制有独立文献链；(3) 末句预告替代变量检验（"although we examine alternative measures"），建立M4→M5的叙事桥梁。

### 变体 4: Mixed-effects within/between 机制分解
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，机制检验设计特有)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> We used mixed-effects models to explore the within-[unit] and between-[unit] effects of [IV], and the results are reported in [Table_reference]. Model ([ref]) indicates that the within-component of [IV] has a [direction] and [significance] relationship with [DV] (β = [value], p < [threshold]), whereas the between-component is [not statistically significant / opposite direction]. The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not the difference in [IV] between [units], but, rather, a relative increase in [IV] for a given [unit] within the same [cluster] that explains [DV].
**与原骨架差异**: 这是将统计结果翻译为机制语言的核心句式。关键策略：(1) 报告within/between系数对比；(2) "it is not... but, rather..."句式将统计输出转化为理论叙事；(3) 明确指出是"个体内部变化"还是"个体间差异"驱动效应。适用于任何面板数据中需要区分个体内变化vs个体间差异的机制检验。

### 变体 5: 替代变量机制对齐矩阵
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，需配合 Figure 1 机制对齐图使用)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> Following extant research ([citation]), we used [Primary_IV] as our primary measure because it broadly reflects [number] mechanisms: [mechanism_list]. To probe these mechanisms at a more granular level, we replicated our analyses using two alternative measures of [construct]—[Alternative_1] and [Alternative_2]. We measured [Alternative_1] as [definition]. We measured [Alternative_2] as [definition]. [Figure_reference] details each measure and its alignment with our theorized mechanisms. Both our primary measure and the alternative measures inherently reflect [shared_mechanism]. [Alternative_1] also proxies for [mechanism_A] because [rationale] ([citation]), whereas [Alternative_2] also proxies for [mechanism_B] because [rationale] ([citation]). Thus, although our primary measure is comprehensive and reflects all [number] mechanisms, the alternative measures help us examine whether, indeed, all [number] mechanisms contribute to [DV].
**与原骨架差异**: 这是**三角验证**策略在 variable construction 层面的应用。关键要素：(1) 主变量+替代变量矩阵；(2) Figure 1 机制对齐图（每个变量→哪些机制→理论基础）；(3) 部分重叠的机制映射（变量A覆盖机制1+2，变量B覆盖机制1+3，变量C覆盖机制2+3）；(4) "虽然主变量全面，但替代变量帮我们检验是否所有机制都起作用"的诚实表述。适用于任何"一个构念→多个可分离机制"的构念效度设计。

### 变体 6: M2 多通道精英/关键行为人招募 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We recruited [actors] through [N] channels to maximize sample diversity and reduce selection bias. First, we partnered with [organization_type_A: e.g., board advocacy group] which provided access to [actor_pool_A]. Second, we worked with [organization_type_B: e.g., consulting firm] to identify [actor_pool_B]. Third, we contacted [organization_type_C: e.g., alumni office] for [actor_pool_C]. Finally, we used snowball sampling through [references] to reach additional participants. This multi-channel approach yielded [N_final] [actors] representing [N_firms/units] across [N_industries] industries.
**与原骨架差异**: 针对难以接触的研究对象（高管、董事会成员、精英决策者），单一招募渠道会导致样本集中于某一类型——多通道招募通过制度多样性（advocacy groups vs consulting partners vs alumni networks）增加样本覆盖。关键要素：每个通道说明其提供哪类参与者，最终汇总样本的行业分布。

### 变体 7: M7 嵌套横截面数据的聚类稳健标准误 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> Because our data involve [lower_unit] nested within [higher_unit] (e.g., decisions nested within executives), observations are not independent. We therefore estimated [models] with [SE_type] robust standard errors clustered by [cluster_level] to account for within-[cluster] correlation of the error terms ([citation]). This approach treats each [cluster] as an independent sampling unit while allowing [lower_units] within the same [cluster] to share unobserved characteristics.
**与原骨架差异**: 当数据具有嵌套结构（如多个决策嵌套在同一高管/公司内）但不足以运行多层模型（样本量/top-level 单元数不足）时，聚类稳健SE是最小负担的解决方案。关键：明确说明嵌套层级和聚类层级，解释为什么这样聚类（共享不可观测特征）。

### 变体 8: M8 回顾性偏差三角检验 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M8
**骨架**:
> A potential concern with [retrospective/interview-based] data is that [actors]'s recollections may be colored by [outcome knowledge/hindsight]. We addressed this concern through a triangulation approach: First, we controlled for [affective/outcome variables: e.g., satisfaction with decision outcome] to partial out post-hoc rationalization. Second, we compared [qualitative/text patterns] with [quantitative/archival patterns] to check consistency. Third, we replicated our findings using [alternative measure/sample] that is less susceptible to retrospective bias. Results were consistent across all approaches.
**与原骨架差异**: 适用于任何依赖事后自我报告的研究（访谈、问卷、回忆数据）。三管齐下：(1) 控制情感/结果变量（partial out halo）；(2) 定性-定量一致性检查；(3) 替代测量复制。

### 变体 9: M2 制度断点样本辩护 — 行业收缩+时间边界双重正当性 (1篇高价值)
**来源论文**: Desai 2011 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> The sample period begins in [year_start] because [institutional_event: e.g., regulatory change / industry deregulation] fundamentally altered [key_process] in [industry]. Before [year_start], [condition_A]; after [year_start], [condition_B], making the post-[year_start] period uniquely suited to testing our theory. The sample ends in [year_end], the last year for which [data_source] was available. We focus on a single industry—[industry_name]—to hold constant [confounds: e.g., regulatory environment, technological trajectory, product characteristics] that vary across industries. This single-industry design maximizes internal validity at the expense of generalizability, a trade-off appropriate for theory testing.
**与原骨架差异**: 单行业面板的样本辩护需要完成三重正当性：(1) 制度/法规事件作为起始边界（不早不晚）；(2) 数据可得性作为终止边界；(3) 单行业选择的理论理由（holding confounds constant → internal validity > generalizability）。与多行业面板的"we used all firms in Compustat"形成对比。

### 变体 10: M7 Hausman 检验 — FE vs RE 选择 (1篇高价值)
**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used a [Hausman test] to determine whether [fixed effects] or [random effects] was more appropriate for our panel structure. The test strongly rejected the null hypothesis that the [unit]-specific effects are uncorrelated with the regressors (χ² = [value], p < [threshold]), indicating that [fixed effects] is the preferred specification. We therefore estimated [FE_estimator] with [SE_type] clustered by [cluster_level].
**与原骨架差异**: 标准 FE/RE 选择段落。关键三步：(1) Hausman 检验结果（χ² + p-value）；(2) 解释拒绝意味着什么（"unit-specific effects correlated with regressors"）；(3) 据此选择估计器 + 标准误声明。

### 变体 11: M2 匹配样本层次回退 + 匹配平衡保守检验 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We used a matched sample design to construct a comparison group of [units] that did not experience [treatment] but were otherwise similar on [key dimensions]. Specifically, we matched each [treated_unit] to [N] [control_units] in the same [industry/sector] and [time_period] based on [matching_criteria: e.g., size, age, performance]. When a close match was unavailable at [strict_criteria], we relaxed the criteria to find the closest available match—a hierarchical fallback approach that prioritizes match quality while preserving sample size. To ensure that the matched groups are balanced, we compared [treated] and [control] groups on [N] characteristics using [t-tests / standardized differences]. No significant differences were found across any of the [N] dimensions (all p > [threshold]), suggesting that the matching procedure achieved adequate balance.
**与原骨架差异**: 标准匹配样本段落仅报告"we matched on X"——Pfarrer 增加了两个关键要素：(1) **层次回退**——先在严格维度匹配，无匹配时放宽标准，透明化匹配的灵活边界；(2) **匹配平衡保守检验**——使用保守的 t-test（而非仅标准差异）验证处理组和对照组在所有匹配维度上的可比性。适用于匹配样本设计中匹配质量与样本量之间存在 trade-off 的场景。

### 变体 12: M2 单行业面板 + SIC 边界意识 + 限制样本稳健性 (1篇高价值)
**来源论文**: Darby, Wowak, Ketchen, Connelly & Skowronski 2026 (Journal of Operations Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> As might be expected, the majority of [units] in our sample operate primarily in [primary_industry] ([SIC_code]). However, the sample was not limited to this industry because [units] may be formally classified in other industries ([example_codes]) but still [engage in phenomenon]. To ensure that the sample is not unduly influencing our results, we conducted an additional analysis that limited the sample to only [primary_industry] [units]. The results are consistent with our primary results.
**与原骨架差异**: 单行业研究的标准担忧是"样本是否受少数非核心行业企业驱动"。本骨架通过两步消除此担忧：(1) 先承认行业分类的模糊性——SIC code 不完全等于业务实质；(2) 报告限制样本的稳健性检验。两句话完成，不需要独立附录表。

### 变体 13: M7 随机效应选择三重辩护 — 理论+Hausman+ICC (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used panel regressions with random-effects estimations, because theoretically, we were more interested in the differential effects across [unit] rather than changes within [unit]. The Hausman test (p = [value]) confirmed that using the random-effects (vs. fixed-effects) method was more appropriate. Also, [key_predictor] is likely to be an enduring [attribute_type] that remains stable over a short timeframe. We examined [its/their] internal consistency (ICC) using hierarchical linear modeling (HLM) to further test this premise. We used [predictor] as the outcome variable and treated [level_1_unit] as Level 1 and [level_2_unit] as Level 2 in the analyses. The ICC value ([value]) indicated that [predictor] tends to be stable within the individual but shows systematic variation across [level_2_unit]. We used robust standard errors to minimize heteroscedasticity and autocorrelation in our analyses ([citation]).
**与原骨架差异**: 本骨架与变体10（标准 Hausman→FE 选择）互补——当**理论指向 RE**时（关注跨单元差异>单元内变化），需要比单一 Hausman 更系统的辩护。Li et al. 提供了三层递进：(1) 理论理由——"more interested in differential effects across CEOs rather than changes within CEOs"；(2) Hausman 统计证据（p>.05 → RE 合适）；(3) ICC 辅助证据——用 HLM 估计关键预测变量的跨层变异比例，证明该变量确实在 Level 2 单元间存在系统性变异。注意：若理论关注单元内变化（如 within-firm dynamics），即使 Hausman 不显著也应使用 FE 并报告两者比较——本骨架仅适用于 theory→RE 的路径。
**诚实边界**: RE 选择的最低要求：(1) 理论理由（跨单元差异>单元内变化），(2) Hausman 检验结果，(3) 关键预测变量的 ICC 作为辅助证据。仅凭 "Hausman test was not significant (p > .05)" 不足以说服审稿人——需解释**为什么理论预期 RE 比 FE 更合适**。

### 变体 14: M6 全谱系控制变量 — 高 because 密度 + RavenPack事件控制 + CEO人格特质 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M6
**骨架**:
> We controlled for several variables to account for their unique influence on [DV]. The control variable data were derived from [time_period] before the focal [event] unless otherwise indicated. First, we controlled for [control_1] ([operationalization]), as [because_reason]. We controlled for [control_2], calculated as [formula]. We accounted for [control_3] from [source] ([scale_description]). We used [aggregation_method] by [source_type] based on [selection_criterion] before the [event] ([citation]). We controlled for [control_4], measured in [unit], since [because_reason]. We controlled for [control_5] ([operationalization]), measured as [calculation_detail] ([citation]). We accounted for the confounding effects of [event_type_1] and [event_type_2] on [DV] ([citation_1]; [citation_2]). All pertinent news was sourced from the "[category_1]" and "[category_2]" categories from the [database]. We included only news articles with a relevance score of [threshold], indicating [rationale]. Furthermore, we kept only the first occurrence of each [event_type] that appeared in any news outlet within a [time_window].
>
> In addition, we controlled for [actor] [demographic_1], [demographic_2], and [demographic_3] ([citation]). We controlled for [actor] displayed [psychological_state_1] and [psychological_state_2], generated using [text_tool] [version] default dictionary, because [rationale] ([citation]). We controlled for [actor] use of [linguistic_feature] ([citation]) because, similar to [key_predictor], [linguistic_feature] might [threat_rationale]. [Actor] personality traits ([trait_list]) were controlled because they may impact [outcome]; they were measured based on [citation]. We controlled for [complementary_DV_dimension] to account for the [opposite_dimension] in [data_source], measured with [dictionary/method]. Finally, we included [fixed_effect_1] and [fixed_effect_2] in each model.
**与原骨架差异**: 在变体1（分层 because 结构）基础上的三个升级：(1) **RavenPack 事件控制**——新产品公告和M&A新闻的 confounding effects 需明确控制，且需报告 relevance score 阈值和去重策略（"first occurrence within a one-day window"）；(2) **CEO 人格特质控制**（Big 5）——在 CEO 沟通研究中，人格特质可能同时影响语言使用和投资者感知，但极少论文控制此维度；(3) **互补 DV 维度控制**——如主DV为负向情绪时，控制正向情绪维度。本骨架的 because 密度目标为 ~100%——每个控制变量（共19个）都附带 because 理由。适用于任何理论预测多种混淆来源的研究（特别是文本构念+市场反应的交叉领域）。
**诚实边界**: 19个控制变量可能引发 overfitting 担忧——应在稳健性中报告仅含核心控制的简化模型。若某控制变量的 because 无法给出，应质疑是否真的需要控制。

### 变体 15: M1 单行业设置 — 双重现象共存辩护 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M1
**骨架**:
> We chose [industry/setting] as an appropriate setting for examining our hypotheses because it features both [phenomenon A] and [phenomenon B] ([citation_1]; [citation_2]).
**与原骨架差异**: 单行业研究常用一句话完成情境正当化。关键：不罗列行业统计数字，而是点明两个与理论直接相关的现象在该情境中同时存在。Cui et al. 用 "extensive alliance activities" + "competition for new products" 同时激活 alliance 与 competition 两个理论前提。

### 变体 16: M2 多源 alliance 数据库合并与交叉验证 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M2
**骨架**:
> We first collected data on [alliances/relationships] within [industry] from [year_start] to [year_end], using [N] data sources—[source A], [source B], and [source C]—which (a) have very similar standards for reporting information, including [key fields], and (b) each normally reports only a fraction of all [activity] ([citation]). Although databases that track [activity] in [industry] are normally reliable ([citation]), we found that [source A] covers more [historical data], while [source B] and [source C] include more [recent information]. We constructed a more comprehensive [database] by combining these [N] data sources. For due diligence, we followed [citation], searching for [announcements/status reports] from [source D], [source E], and [source F]. Most [announcements] were cross-validated by at least two additional sources. By relying on multiple sources, we minimized the possibility of double-counting [alliances] and of counting [alliances] that were announced but not realized.
**与原骨架差异**: 在现有变体2（样本交集漏斗）基础上扩展为完整段落。关键要素：(1) 多数据库互补性说明；(2) 人工 due diligence（LexisNexis / 公司网站 / SEC filings）；(3) 交叉验证的两个明确目标：防重复计数、防 announced-but-not-realized。适用 alliance / network / contract 等多源合并场景。
**诚实边界**: 仍需报告关键中间匹配 N（如初始 alliance 条目、合并后条目、匹配 Compustat/FDA 后最终 dyad-year），否则仍落入"多数据库无漏斗"反模式。

### 变体 17: M3 多维行为指标 → factor score → 平均值 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M3
**骨架**:
> [DV construct] describes both [dimension 1] and [dimension 2] of [actor]'s [behavior] ([citation]). This variable contains [N] items: [item 1], [item 2], and [item 3]. [Item 2] measures [definition]; [item 3] measures [definition]. [Item 3] is a more aggressive form of [behavior] than [item 2] because [theoretical rationale] ([citation]). We ran a factor analysis of these [N] items and found that all [N] loaded high (>[threshold]) on one latent factor, while the value of Cronbach's alpha is [value], which suggests that it is a reliable construct. We used the [average score] for these [N] items to measure the dependent variable.
**与原骨架差异**: 适用于多维行为 DV（如竞争攻击性 = 行动数量 + 宽度 + 深度）。关键：(1) 每个子维度的理论含义；(2) 子维度间的理论排序（如某维度更激进）；(3) factor loading + Cronbach's alpha；(4) 合成方式（平均值或 factor score）。与文本构念测量变体5（复合文本指标）互补——本骨架用于行为计数+定性深度组合。

### 变体 18: M7 dyad fixed effects + dyad 聚类标准误 + 具体混淆源举例 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We tested our hypotheses using fixed-effects models. The unit of analysis is [actor]-[partner]-[time], and we allowed a [N]-year lag between our predictor variables and the dependent variable. A fixed-effects estimator has superior controls for time-invariant variables ([citation]) and is an effective way to account for possible endogeneity problems. For example, if unobserved heterogeneities, such as [example 1] and [example 2], are constant within [dyad], then there might be an endogeneity concern. A fixed-effects estimator can rule out such a possibility by eliminating time-invariant heterogeneities. Fixed-effects models also allow us to account for intra-cluster correlations caused by multiple observations of the same [dyad] over time. We therefore employed [dyad] fixed-effects and clustered standard errors on [dyad] in our models.
**与原骨架差异**: 与变体7（嵌套横截面聚类 SE）互补。本骨架增加 dyad FE + 具体时不变混淆源举例（如 "attractiveness of partners to one another and their tendencies to compete"），让 FE 的识别价值从抽象变为可感知。关键：混淆源举例必须真实存在于研究情境中，而非泛泛而谈。
**诚实边界**: dyad FE 只能消除时不变遗漏变量；若存在时变混淆（如共同市场冲击），FE 无法识别因果。网络变量研究还需额外讨论反射性问题。

### 变体 19: M4 高管信心期权 moneyness 操作化 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M4
**骨架**:
> We follow the finance and accounting literature and infer [actor] confidence from [actor]s' decisions about when to exercise company stock options ([citation]). The options-based measure uses archival data and is easily calculated from Execucomp, allowing us to examine executive confidence for a broad cross-section of firms over a long period ([citation]). [Actor] confidence is measured as the average moneyness of the exercisable options held by the [actor] in [year t]. The average moneyness is defined as the ratio of the average value per option to the average strike price ([citations]). The constructs are measured with a lag relative to the dependent variable to create temporal distance and maintain causal priority.
**与原骨架差异**: 高管信心的经典期权 moneyness 操作化。关键要素：(1) 理论直觉（自信高管延迟行使深度实值期权）；(2) 公式（average value/strike price of exercisable options）；(3) 滞后处理（避免薪酬同期受 DV 污染）。与 `micro-templates/executive-confidence-operationalization.md` 配套使用。
**诚实边界**: 必须说明该指标测量的是"基于财富的信念"而非心理学过度自信；必须报告滞后结构；样本中无 exercisable options 的高管需说明缺失值处理。

### 变体 20: M2.5 Model-Free Evidence 预览 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M2.5
**骨架**:
> Before presenting the model-based evidence, we provide model-free evidence on the relationship between [IV] and [DV]. We divide the sample into quartiles based on [IV] and calculate the mean and median [DV] for firms in each quartile. If [theory] holds, we should observe a monotonic [increase/decrease] in [DV] from the lowest to the highest [IV] quartile.
**与原骨架差异**: 在正式回归前用 quartile means/medians 展示无条件关系。关键：明确分位数基于 [IV]、报告 mean + median、说明预期模式（单调递增/递减）。适用于连续 IV 与连续 DV 的初步关系展示，增强读者对主效应方向的直观信心。
**诚实边界**: Model-free evidence 不能替代模型控制；必须在 Methods 中预告其探索性质，并在 Results 中明确与模型结果的对比。

### 变体 21: M7 三向交互模型设定 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We estimate the following model: [DV] = β₀ + β₁[IV] + β₂[IV]×[W1] + β₃[IV]×[W1]×[W2] + β₄[IV]×[W2] + β₅[W1]×[W2] + β₆[W1] + β₇[W2] + Controls + ε. For ease of interpretation of the interaction coefficients, we mean-center [IV], [W1], and [W2] before including them in the regressions ([citation]). We include all two-way interactions and the constituent terms to avoid omitted-variable bias in the three-way interaction coefficient ([citation]). We cluster the standard errors at the [firm] level to account for heteroskedasticity and within-[firm] correlation ([citation]).
**与原骨架差异**: 三向交互的标准 Methods 写法。关键要素：(1) 完整模型方程（含所有 lower-order terms）；(2) mean-centering 声明；(3) 聚类 SE 层级。适用于 X × W1 × W2 设计。
**诚实边界**: 必须包含所有 lower-order terms；mean-centering 不影响系数解释但影响常数项；若 W1/W2 偏态，±1 SD 切割需改用实际分位数。
**跨 skill 对齐**: `write-theory/corpus/variants/E_moderation.md` E6（序列嵌套调节理论推导）；`write-results/三向交互.md` 变体2（连续调节变量三向交互边际效应表）。

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **多数据库无漏斗** | 多数据库合并（Compustat + Execucomp + CRSP + ...）后仅报告最终 N，未说明各数据库交集前后的 N 损失 | 如无法构建完整逐层漏斗（因多源合并非逐步筛选），至少报告："Of the [N_initial] firm-quarters in [primary_source], [N_matched] could be matched to [secondary_source], yielding [N_intersection]." |
| **多源合并后中间 N 缺失** | 合并多个数据库后仅报告最终 N，未报告 alliance/relationship 条目、样本匹配前后损失 | 报告关键中间匹配 N，如 "Of the [N_initial] [alliances] from [source A], [N_matched] could be matched to [source B], yielding [N_final] [dyad-years]." |
| **调节效应论文 Methods 未报告交互项构造** | 论文核心贡献是调节效应，但 Methods 未说明交互项、去心化或二次项 | 在 M5/M7 明确说明交互项形式、是否 mean-centered、是否包含二次项及其构造方式 |
| **仅凭 Hausman 选择 RE** | 仅报告 "Hausman test not significant (p > .05), so we use RE"，无理论理由 | 参见变体13——RE 选择需理论理由（跨单元差异>单元内变化）+ Hausman + ICC 三重辩护 |
| **控制变量无 because** | 罗列变量名和操作化但不解释"为什么控制这个变量" | 每个控制变量必须回答：(1) 为什么影响 DV，(2) 为什么可能与 IV 相关 |

## 诚实边界

- **RE vs FE 选择**：必须基于理论（跨单元差异 vs 单元内变化）而非仅凭 Hausman。若理论关注单元内变化但 Hausman 不显著 → 仍应使用 FE 并报告两者比较。ICC 可用于辅助论证但非决定性。
- **多数据库合并**：报告交集前后的 N 差异。若某一数据库匹配率极低（<50%），应解释原因并讨论选择偏误风险。
- **控制变量数量**：19+ 控制变量需提供理论或方法论引用支撑（如 "following [citation], we include a comprehensive set of controls"），且在稳健性中报告简化模型。
- **网络变量与 FE 的交互**：当模型同时包含 dyad FE 和网络变量时，网络变量的 within-dyad 变异可能很小，导致系数估计不稳健，需在 M8 讨论。
