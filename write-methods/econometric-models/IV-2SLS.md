---
design_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): natural-disaster instrument + 3-reason exclusion restriction (external-event-as-IV template)"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): Durbin-Wu-Hausman test + Gaussian copula endogeneity narrative"
variants_count: 9
created: 2026-05-18
updated: 2026-07-25
---

# IV-2SLS — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `IV-2SLS` 专用变体）。

## 设计特征摘要

- **核心估计器**: Two-stage instrumental variable (IV) regression: 2SLS for continuous DV, IV-Probit/IV-Tobit/IV-Poisson for limited DV
- **识别策略**: 工具变量必须满足 relevance (与内生变量相关) 和 exogeneity/exclusion (仅通过内生变量影响DV) 两个条件
- **工具变量来源**: 外部IV (自然实验/政策冲击) 或 内部IV (Lewbel 2012 heteroskedastic identified instrument)
- **诊断检验链**: Partial F-statistic (relevance), Sargan/Hansen J-test (overidentification), Andrews identification test, Pagan-Hall/Breusch-Pagan (Lewbel-specific)
- **适用场景**: 内生性威胁严重(omitted variable / simultaneity / measurement error)且可找到有效IV的研究
- **跨论文复现率**: 1/5 产品召回论文 (Wowak2025)；传统IV在 Eilert2017 Control Function 中有间接应用

## 累积变体

### 变体 1: Lewbel (2012) Heteroskedastic Identified Instrument 三步法
**来源论文**: Wowak2025 MS
**验证状态**: 通过 (1/5 产品召回，但方法泛用性极高)
**写入日期**: 2026-05-20
**槽位**: M7
**骨架**:
> To address this challenge [of finding valid external instruments], we use an IV approach that has emerged from the econometrics literature called the heteroskedastic identified instrument technique. This technique, which has recently been adopted in [domain] research ([citations]), is designed to accommodate a setting "when no external instruments or other such information are available" ([citation], [page]). This procedure allows us to generate valid instruments via three steps ([citations]). First, we use the potentially endogenous independent variable ([IV]) as the dependent variable in a first-stage equation that features all our controls as regressors. Just as [citation] theorized and [citation] emphasize, we include all of our control variables as the regressors in this first-stage equation because doing so is the preferred specification, unless including a subset of the controls better upholds the assumptions of the model. In the second step, the technique calculates the residuals associated with each of those control variable regressors and transforms the heteroskedasticity into potentially valid IVs, but only when the assumptions of the model that we detail next are exhibited ([citations]). Finally, we incorporate the valid generated instruments into the two-stage IV fixed effects estimators.
**与原骨架差异**: 传统 IV-2SLS 要求研究者找到外部工具变量(如政策冲击、自然实验)，而 Lewbel 方法从第一阶段的**异方差残差**中内部生成有效IV。三步法核心：(1) 所有控制变量回归内生变量；(2) 残差异方差→有效IV；(3) 生成的IV纳入第二阶段。诚实边界：Lewbel 方法依赖于两个关键假设(见变体2)，若不满足则生成的IV无效。适用于"无外部IV可用"的情境。

### 变体 2: IV 有效性诊断链完整报告 (Lewbel + 传统诊断)
**来源论文**: Wowak2025 MS
**验证状态**: 通过 (1/5 产品召回，IV研究的必写段落)
**写入日期**: 2026-05-20
**槽位**: M7/M8
**骨架**:
> Scholars indicate that the heteroskedastic identified instrument procedure can generate valid instruments under two assumptions ([citations]). First, [citation] note that the instruments generated from the heteroskedastic identified technique must not be correlated with the covariance in the error terms from the first and second stage equations. Just as [citation] prescribe, [citation, p. X] emphasize that this assumption is upheld by "failing to reject homoskedasticity with respect to [the first-stage regressors]" via the [test_name] test. For our data, the [test_name] diagnostic [test_result] ([test_stat]=[value]; p=[threshold]), thereby adhering to this first assumption. Second, [citation] state that the generated instruments must be meaningfully correlated with the endogenous independent variable. In line with [citation], [citation, p. X] argue that this assumption can be supported when scholars "reject homoskedasticity with respect to the selected [regressors]" via the [test_name] test. Our variables uphold this condition by [test_result] ([test_stat]=[value]; p < [threshold]), thus adhering to this second assumption.
>
> It is worth underscoring that our generated instruments also conform to the traditional diagnostic tests pertaining to relevance and exogeneity for any type of IV. Indeed, the partial F-statistic exceeds the thresholds that scholars suggest represent relevance (partial F-stat = [value]; p < [threshold]), and the [identification_test] from [citation] does not contain zero [[lower], [upper]], reflecting relevant instruments ([citation]). Similarly, diagnostic tests for exogeneity suggest our instruments are unrelated to the structural error terms pertaining to [DV_1] (Sargan χ² = [value]; p = [threshold]) and [DV_2] (Sargan χ² = [value]; p = [threshold]), indicating that our instruments are not endogenous ([citation]). Taken together, our instruments appear to be properly identified and valid.
**与原骨架差异**: 这是 IV-2SLS 的**完整诊断报告模板**。关键要素：(1) Lewbel 假设1: Pagan-Hall 不拒绝 homoskedasticity → 生成的IV与误差协方差无关；(2) Lewbel 假设2: Breusch-Pagan 拒绝 homoskedasticity → 生成的IV与内生变量相关；(3) 传统 relevance: partial F > 10；(4) 传统 identification: Andrews 区间不含0；(5) 传统 exogeneity: Sargan 不拒绝 → IV外生。适用于任何IV研究——传统IV替换前两个测试为 Wu-Hausman / Cragg-Donald。**诚实边界**: 若任何测试未通过，相应的IV无效，需重新选择工具变量。

### 变体 3: 政治意识形态操作化 — 四步四指标聚合流程
**来源论文**: Wowak2025 MS
**验证状态**: 可选变体 (1/5，政治意识形态研究特有)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> [IV] is calculated as the [aggregation_method] [annual] [construct] across members of a firm's [group] ([citations]). To compute this measure, we carefully followed the procedure documented in [domain] research ([citations]). We first used [source] to identify the [group_members] in each organization ([citations]). Next, we identified each [member]'s [construct] by accessing [data_source] from [database]. Using the [data], we then calculated [N] indicators that have been shown to collectively reflect [construct] ([citations]): (1) [indicator_1]; (2) [indicator_2]; (3) [indicator_3]; and (4) [indicator_4]. Each indicator ranges from [min] to [max]; [max] represents [pure_form], [min] represents [opposite_form]. Following research precedence, we [aggregation] the indicators ([citations]), as they demonstrate high reliability and internal consistency (α=[value]). In line with this literature, we assign a score of [neutral_value] to individuals with no [data], indicating that they are [neutral_label] ([citations]). That said, in robustness checks we remove [missing_data_group] from our sample and demonstrate that assigning a value of [neutral_value] to them does not meaningfully influence our results.
**与原骨架差异**: 政治意识形态的**标准操作化流程**——从 Chin et al. (2013) 确立的四个政治捐赠指标到均值聚合。关键要素：(1) 四指标全覆盖（捐赠数量比/金额比/候选人比/年份比）；(2) 高内部一致性引用 (α=0.95)；(3) 非捐赠者处理策略 (赋中性值0.5 + 排除稳健性检验)；(4) 每句都有方法论引用链。该骨架可迁移至任何使用 FEC/Open Secrets 政治捐赠数据的研究（CSR、公司创业、高管薪酬等）。

### 变体 4: 外部自然事件作工具变量 + 三因排除限制论证 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**验证状态**: 通过 (单篇高价值，"外部自然事件→非正式关系"工具变量论证的稀缺范式)
**写入日期**: 2026-06-16
**槽位**: M8
**骨架**:
> An important consideration is that [actors] might self-select whether they [form the focal tie / take the treatment], creating an endogeneity issue. Furthermore, comparing the reduced-form [DV] model with the [mediator-included] model, Shaver ([2005]) suggested the reduced form may be mis-specified due to an omitted [mediator/endogenous regressor], and recommended an instrumental variable analysis. We focused on [an exogenous external / natural event — e.g., natural disasters in the actor's home market] as an instrumental variable. First, [the event] is exogenous, reflecting "nature's fury" ([citations]), and is not affected by [the outcome]. Second, [the event] might expose limitations of formal institutions (e.g., written rules and regulations) for acquiring strategic resources from the state, requiring [actors] to seek informal means—such as [forming the focal tie] ([citations]). Third, the existing [outcome] literature suggests that [actors] typically base [the outcome] on [alternative determinants: e.g., distance, host-market institutions, demand, own capabilities]; [the event], hence, may predict [the treatment] but have a limited effect on [the outcome] directly ([citation]). So, the instrument may satisfy exclusion-restriction conditions. We obtained data on [the event] from [source] and used it as an instrument.
**与原骨架差异**: 与变体 1–3（Lewbel 内部生成 IV）的根本区别——本变体用**外部自然/准自然事件**作 IV，且排除限制通过**三层论证**建立：(1) 事件外生性（"nature's fury"，不受结果影响）；(2) 事件→处理的渠道（制度缝隙逻辑：正式制度失效→寻求非正式关系）；(3) 事件→结果的直接渠道**缺失**（由结果文献的已知决定因素反推）。第（2）层是核心理论增量——IV 通过"挤压正式资源获取"间接推动处理。诚实边界：第（3）层"无直接渠道"是排除限制的关键假设，本质不可检验，必须用结果领域文献的既有发现支撑，不可断言。适用于 IV 通过"制度/资源缝隙"推动企业形成非正式关系（政治关联、军方关联、银企关系）的研究。配合 control-function 报告见 `../write-results/econometric-models/IV-2SLS.md` 变体 4。

### 变体 5: M8 Durbin-Wu-Hausman (DWH) Test + Gaussian Copula 内生性叙事 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M8
**骨架**:
> Our hypothesis builds on the premise that [IV] is exogenous to [DV]. However, endogeneity such as that arising from omitted variables and reverse causality may bias our estimates. To address omitted variables issues, we have controlled for many possible variables that might affect [DV]. Nevertheless, it is possible that unobservable omitted variables, such as [example], may affect both [IV] and [DV]. We examine the effects of unobservable [unit]-specific omitted variables in a model that incorporates [unit] fixed effects. The [unit] fixed effects control for any time-invariant omitted variable that might affect [DV] and [IV], and thus control for heterogeneity across [units] that are time-invariant ([citation]). However, [unit] fixed effects cannot address issues relating to reverse causality and time-varying omitted variables. Therefore, to further address endogeneity concerns, we conduct the Durbin-Wu-Hausman (DWH) test ([citations]). Similar to our exclusion restriction, we use the average [IV] of peer firms operating in the same industries as the focal firm as an instrument for [IV]. For the results of the DWH test to be useful, the instrument needs to be relevant and strong ([citation]). Peer [IV] significantly predicts focal [IV] with [t-statistic] and p-value [p]. The partial R-squared of excluded instruments is [value] with an F-statistic of [F], which is above the rule-of-thumb cutoff of 10 for weak instruments ([citation]) and also above all of the Stock and Yogo ([citation]) critical values. The Chi-sq test statistic for the DWH test is [value] (p-value = [p]), indicating [no/some] evidence of endogeneity. To further substantiate the case of [no] endogeneity, we also use the instrument-free Gaussian copula joint estimation method ([citation]) and reach similar conclusions.
**与原骨架差异**: 完整的"DWH 检验 + Gaussian copula"内生性叙事。关键要素：(1) 遗漏变量与反向因果的双重威胁；(2) [unit] FE 处理时不变遗漏变量；(3) 同行 [IV] 作为工具变量及其相关性诊断（F-statistic、Stock-Yogo）；(4) DWH 结果解释（能否拒绝内生性原假设）；(5) Gaussian copula 作为无工具变量替代方法提供三角验证。适用于面板 OLS 研究中核心 IV 潜在内生性但又不存在强外部 IV 的情境。
**诚实边界**: DWH 检验的功效依赖于 IV 强度；若 IV 弱或 DWH 不显著，不能断言无内生性。Gaussian copula 对分布假设敏感，应在稳健性中报告敏感性分析。
**跨 skill 对齐**: `../write-results/econometric-models/OLS-FE.md` 变体26（R7 内生性稳健性表叙事 — threat-by-threat Table 7 汇总）。

### 变体 6: M8 早年传记性暴露作工具变量（政治社会化 / imprinting）+ 第二组织级工具变量 (1篇高价值)
**来源论文**: Abdurakhmonov, Ingram & Ridge (2026, JOM)
**验证状态**: 通过（单篇入库，待第二篇交叉验证；corpus 此前无 biographical / imprinting 类 IV 变体）
**写入日期**: 2026-07-22
**槽位**: M8
**骨架**:
> For instruments, we used (1) [early-life / biographical exposure to a stable trait] and (2) [organizational / group-level alignment with the trait]. The [political / social / cultural environment] during a [CEO / actor]'s [adolescence / formative years] is likely to shape their long-term [trait] orientation but is unlikely to directly influence [firm-level DV] ([biographical-imprinting citations]). To capture this exogenous variation, we construct an [adolescence / formative-period exposure index] based on the [environment] experienced during the [actor]'s developmental years, drawing on [political-socialization theory / imprinting theory] ([citations]). Specifically, for each [actor], we calculated the average [exposure to the focal orientation] between the ages of [age_start] and [age_end]—a period widely recognized as critical for the formation of durable [beliefs / values]. We computed the index as the mean of [N] components: the proportion of [indicator_1: e.g., congressional seats held by focal party] and the proportion of [time_period: e.g., years under focal administration] during this window. This yields a continuous measure of early-life exposure to [focal condition], with higher values indicating greater [orientation] influence during the [actor]'s formative years. [Organizational / group-level ideology] is also likely to influence the appointment of [actors] whose [trait] aligns with the organization's existing [orientation]; prior work shows [organizations] often seek [trait] alignment to maintain [stakeholder trust / internal legitimacy] ([citation]). Furthermore, [organizational ideology] is unlikely to directly influence [DV] once [actor-level IV] is accounted for, because [organizational-level ideology reflects historical behavior, whereas the focal decision is situated at the executive level and shaped by personal preferences / risk tolerance / values] ([citations]).
**与原骨架差异**: 与变体 1（Lewbel 内部异方差 IV）、变体 4（Qiao 2026 外部自然事件 IV）的根本区别——本变体的 IV 来自 **个人早年传记性暴露**（"imprinting" 类 IV）。relevance 来自发展心理学 / 政治社会化理论（早年是稳定信念形成的关键期），exclusion 来自"早年环境 → 数十年后决策"的 **时间距离** + **分析单位隔离**（个人特质 vs 公司结果）。与变体 4 的 "nature's fury" 外生性论证不同：变体 4 的外生性来自事件物理外生性，本变体的外生性来自时间距离与层级隔离。关键四要素：① 早年暴露的具体时段（如 15-25 岁，发展心理学关键期，须引 Jennings & Niemi 2014 / Malmendier & Nagel 2011）；② 多成分指数构造（每成分有独立理论含义）；③ 排他性三层论证（理论 + 机制 + 文献反推）；④ 第二工具变量（组织意识形态）及其独立的排他性论证。诊断报告 Cragg-Donald Wald F 与 Sargan p-value 按变体 2 标准报告。
**诚实边界**: 早年暴露时段的合理性必须引用发展心理学 / 政治社会化文献，不能任意选年龄段；多成分指数构造需说明每成分的理论含义；排他性论证本质不可检验，必须诚实标注为 "assumption" 而非 "test result"；若 [actor] 早年暴露地与当前 [unit] 所在地不一致，需报告并讨论潜在问题；单工具变量稳健性（从两 IV 减至早年暴露一 IV）应作为稳健性检验报告——会损失 first-stage 解释力与过度识别检验，但消除弱 IV 导致的过度识别偏误风险。
**适用**: 焦点 IV 为个人稳定特质（政治意识形态、人格、风险偏好、文化背景）的研究；任何可获取 [actor] 早年传记数据（出生地、教育地、早年工作地）的情境。
**跨 skill 对齐**: 与变体 3（政治意识形态操作化）配套——变体 3 测量 focal IV，本变量为其构造工具变量解决内生性。

### 变体 7: M8 Shift-Share / Bartik 工具变量（push × pull interaction）+ 双重独立排除限制 (1篇高价值)
**来源论文**: Lee & Wang (2026, Journal of Management)
**验证状态**: 通过（单篇入库，待第二篇交叉验证；corpus 此前无 shift-share / Bartik 类 IV 变体）
**写入日期**: 2026-07-22
**槽位**: M8
**骨架**:
> Following the shift–share approach in economics ([Burchardi, Chaney, & Hassan, 2019](#bibr15); [Card, 2001](#bibr16); [Tabellini, 2019](#bibr60)), we construct a [unit]–[time] instrumental variable that predicts [endogenous regressor: e.g., the salience of migration issues] by interacting a time-varying "push" factor with a [unit]-specific historical "pull" factor. The push component is [a plausibly exogenous time-varying shock: e.g., the annual number of armed conflicts worldwide from the Uppsala Conflict Data Program (UCDP)], which captures exogenous shocks that increase [global displacement pressures / the upstream driver of the endogenous regressor]; the pull component is [a predetermined [unit]-specific stock measure: e.g., the number of residents in 1980 who reported foreign-born ancestry in each state], capturing [network-driven attractiveness / the historical structural condition that amplifies the push]. This interaction is relevant because [push shocks] raise [expected inflows / endogenous regressor levels] disproportionately where [historical enclaves / pull factor] are larger, thus predicting [current migrant populations] and, in turn, [the salience of the focal issue]. However, it is unlikely that either [ancestry patterns / pull factor] fixed over [N] decades ago or [armed conflicts / push factor] occurring outside [the focal geographies] plausibly affect [facility-level DV] except through their impact on [migration and its salience / the endogenous regressor], supporting the exclusion restriction.
**与原骨架差异**: 与变体 1（Lewbel 内部异方差 IV）、变体 4（Qiao 外部自然事件 IV）、变体 5（Chung 同行均值 IV + Gaussian copula）、变体 6（Abdurakhmonov 早年传记 IV）的根本区别——本变体的 IV 是 **两个独立论证的组件的交互项**：(a) 时变 push（外生全球冲击）；(b) [unit]-特定 pull（历史预定结构特征）。这是劳动 / 迁移经济学（Card 2001, Burchardi Chaney Hassan 2019, Tabellini 2019）的经典设计。关键结构差异：① **relevance via disproportionate response**——push 在 pull 较大处放大效应，使交互项预测内生变量；② **exclusion via dual independence**——两组件各自的时间距离（数十年前）和空间距离（域外）共同排除直接渠道；③ **IV = interaction**，而非单一外部事件或单一内部生成残差。诊断报告 Cragg-Donald Wald F 与 Stock-Yogo 临界值按变体 2 标准报告（本文 F=7324.562 vs 16.38）。
**诚实边界**: push 因子的外生性论证必须基于"研究情境之外的外生冲击"（如域外武装冲突、全球商品价格、跨国政策变化），不能是 [unit] 内部决策可影响的变量；pull 因子的"预定性"必须有时间距离（通常 ≥ 20–30 年），并引用历史移民 / 网络文献支撑"历史 enclaves 决定后续 inflow 模式"；排除限制本质不可检验，必须诚实标注为 "assumption"——若 push 因子可能通过非 focal 渠道影响 DV（如全球冲突影响供应链进而影响污染），需在 Limitations 显式承认；应报告 first-stage F-stat 远超 Stock-Yogo 临界值，但不应过度依赖超大 F 值掩盖排除限制的可论证性。
**适用**: 焦点 IV 为 [unit] 层面的 inflow / salience / intensity 构念（移民、贸易、资本流动、技术扩散、人才流动）的研究；任何可构造"外生全球冲击 × 历史[unit]特定暴露"交互的研究。典型应用：移民 / 贸易 / 资本流入对[unit]（州 / 国家 / 地区 / 行业）结果的影响。
**跨 skill 对齐**: 与变体 4（Qiao 自然事件 IV）互补——变体 4 用单一外部事件作 IV，本变体用两组件交互；与变体 6（Abdurakhmonov biographical IV）互补——变体 6 的"距离"来自时间，本变体的"距离"来自时间 + 空间双维度。

### 变体 8: M7 双估计器双层级两阶段 IV（同一 IV 对两个不同性质/层级 DV）
**来源论文**: Wowak2025 MS
**验证状态**: 通过（补足变体 1 的估计器选择维度；corpus 此前无"同 IV 双 DV 双估计器双层级"显式变体）
**写入日期**: 2026-07-25
**槽位**: M7
**骨架**:
> We examine the influence of [IV] on each of our dependent variables using similar forms of two-stage instrumental variable (IV) fixed effects regression. Specifically, we use a two-stage [count estimator—e.g., negative binomial] fixed effects model for [DV_1: count outcome] and a two-stage least squares fixed effects model for [DV_2: continuous / timing outcome] ([citations]). The level of analysis for the [DV_1] model is the [unit-time—e.g., firm-year], and the level of analysis for the [DV_2] model is the [event—e.g., individual recall].
**与原骨架差异**: 变体 1 详述 Lewbel 工具变量的**生成**，本变体补充**估计器与层级的匹配逻辑**：同一 IV 同时作用于两个 DV，但因 DV 性质不同（计数 vs 连续/时长）而采用不同估计器（NB FE vs 2SLS FE），且分析层级按 DV 内涵匹配（unit-time vs event）。关键点：(1) 两模型共享同一 IV 操作化和同一 IV 诊断（生成的工具变量同时用于两模型）；(2) 估计器按 DV 性质选择——计数 DV 用负二项（避免对数变换的 down-side，见 Note 2），时长 DV 用 2SLS（已对数化的连续 DV）；(3) 两模型都含 firm + year FE。诚实边界：两 DV 在不同层级意味着样本量不同（如 firm-year N=992 vs recall N=4072），须在表注分别报告；负二项 FE 在面板中存在 incidental parameters 问题，应作为已知限制承认。
**适用**: 同一 IV 影响一个计数 DV 和一个连续/时长 DV 的研究（召回数量 + 召回时延、专利数量 + 研发时长、投诉数量 + 处理时长）；产品安全 / 质量管理 / 创新研究中"频率 + 速度"双 DV 设计。
**跨 skill 对齐**: 与变体 1（Lewbel 三步法）配套——变体 1 生成工具变量，本变体说明工具变量如何进入两个不同估计器。

### 变体 9: M8 simultaneity 先证伪后 IV 的 "abundance of caution" 叙事
**来源论文**: Wowak2025 MS
**验证状态**: 通过（单篇高价值；corpus 此前无"先证伪最可能威胁再以防御性 IV 收尾"的 M8 修辞变体）
**写入日期**: 2026-07-25
**槽位**: M8
**骨架**:
> [Adopt firm + year FE to absorb time-invariant and common-shock unobserved heterogeneity.] It is also possible that our estimates could exhibit bias from simultaneity if [actors] [the strategic behavior that would create reverse causality—e.g., donate to curry favoritism]. Such simultaneity is unlikely in our setting for [N] key reasons. First, prior research shows that [the focal behavior represents an actual underlying disposition, not a strategic move] ([citations]). [Relatedly, it is important to note that the literature on the confounding behavior focuses on a different object—e.g., firm lobbying dollars, not personal donations from individuals] ([citation]). Second, studies have consistently shown that [the underlying construct is highly stable over time and not apt to fluctuate strategically] ([citations]). We observe this characteristic as well; [N]% of [actors] in our sample do not [exhibit the strategic / switching behavior] during our sampling period. However, out of an abundance of caution, and to further ameliorate concerns related to endogeneity bias that may be caused by this type of simultaneity, or other sources of endogeneity, we use IV estimation.
**与原骨架差异**: 与变体 5（Chung DWH：FE → DWH 检验）和变体 1（直接引入 Lewbel IV）的根本修辞差异——本变体的 M8 结构是**先证伪最可能的内生性威胁（simultaneity），再以防御性 IV 收尾**。三步说服动作：(1) 命名具体 simultaneity 威胁（[actors] 为 [purpose] 而 [strategic behavior]）；(2) 双理由证伪——文献理由（该行为反映真实 disposition 而非策略）+ **概念区分**理由（focal 行为 ≠ 易混淆行为，如个人政治捐赠 ≠ 企业游说支出）+ **setting 特有行为证据**（[N]% 不切换政党 → 实证支撑稳定性）；(3) 才以 "out of an abundance of caution" 引入 IV。这个"先证伪后防御"顺序比"直接上 IV"更有说服力——展示研究者理解自己的 setting、不滥用 IV，且 IV 仅作为 residual threat 的保险。诚实边界："abundance of caution" **不能替代** IV 诊断（仍须报告变体 2 的完整诊断链）；行为证据（如 92% 不切换）必须是 setting 特有可观测事实，不能泛化；概念区分（个人捐赠 vs 游说）必须引用两类文献分别支撑。
**适用**: IV 的主要内生性威胁是 simultaneity / reverse-causality 且可在理论上 + 行为数据上证伪的研究；个人捐赠、个人稳定特质、长期偏好、价值观的研究（政治意识形态、人格、风险偏好）。
**禁忌**: 不要用 "abundance of caution" 掩盖 IV 诊断的缺失；行为证据百分比必须来自本文样本而非外推；证伪理由若引用文献则必须是与本文 setting 同类的文献。
**跨 skill 对齐**: 与变体 1（Lewbel 三步法）、变体 2（诊断链）配套——本变体是 IV 论证的**前置叙事**，变体 1–2 是 IV 的**技术与诊断**。三者共同构成完整 M8 IV 段落。
