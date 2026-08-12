---
design_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): natural-disaster instrument + 3-reason exclusion restriction (external-event-as-IV template)"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): Durbin-Wu-Hausman test + Gaussian copula endogeneity narrative"
  - "zhou_gao_zhao_2017 (Administrative Science Quarterly): geography-based IV (distance to seaports for institutional development, Frankel-Romer)"
  - "moon_tuli_mukherjee_2023_jm (Journal of Marketing): peer-IV proximity gradient balancing relevance and exclusion validity"
  - "Zorn_Shropshire_Martin_Combs_Ketchen_2017_SMJ (Strategic Management Journal): industry leave-out mean IV for endogenous lone-insider board adoption + dual estimator for continuous vs rare-binary DVs"
variants_count: 13
created: 2026-05-18
updated: 2026-08-05
---
# IV-2SLS — Methods 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M8 | 8 | 4、5、6、7、9、10、11、12 |
| M7 | 4 | 1、2、8、13 |
| M4 | 1 | 3 |

### M8（8）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | 外部自然事件作工具变量 + 三因排除限制论证 | IV 通过"制度/资源缝隙"推动非正式关系（政治关联、银企关系） | 区别于变体 1（Lewbel 内部生成）：外部事件 IV，"nature's fury" 外生性 + 三层排除论证 | 通过（单篇） | Qiao, Hiatt & Sine 2026 (SMJ) |
| 5 | DWH 检验 + Gaussian Copula 内生性叙事 | 面板 OLS 中核心 IV 潜在内生但无强外部 IV | 区别于变体 4：同行均值 IV + DWH 裁决 + copula 三角验证 | 通过（单篇） | Chung, Low & Rust 2022 (JAMS) |
| 6 | 早年传记性暴露作 IV + 第二组织级工具变量 | 焦点 IV 为个人稳定特质（意识形态/人格/风险偏好） | 区别于变体 4：外生性来自时间距离与层级隔离（imprinting 类 IV） | 通过（单篇） | Abdurakhmonov et al. 2026 (JOM) |
| 7 | Shift-Share / Bartik 工具变量（push × pull 交互） | [unit] 层 inflow/salience 构念（移民/贸易/资本流动） | 区别于变体 6：IV = push×pull 两组件交互，双独立排除限制 | 通过（单篇） | Lee & Wang 2026 (JOM) |
| 9 | simultaneity 先证伪后 IV（abundance of caution） | 主要内生性威胁为 simultaneity 且可在理论上 + 行为数据上证伪 | 区别于变体 5/1：先证伪威胁（文献+概念区分+行为证据）再防御性引入 IV | 通过（单篇） | Wowak 2025 (MS) |
| 10 | 地理外生性工具变量（Frankel-Romer 型） | 区域性、与经济互为因果的制度/发展变量（新兴市场跨地区） | 区别于变体 4/6/7：外生性来自地理前定性，持续型距离 | 通过（单篇） | Zhou et al. 2017 (ASQ) |
| 11 | 同行 IV 距离梯度组合（显式管理 relevance–validity 权衡） | 可构造行业/部门/审计师/地理/网络多层同行池 | 区别于变体 5（同行均值）：组织成距离梯度 + 逐类剔除敏感性 | 待交叉 | Moon, Tuli & Mukherjee 2023 (JM) |
| 12 | 行业 leave-out 均值 IV（内生二元结构） | 可能被 CEO/内部人推动采纳的内生二元治理变量 | 区别于变体 5/11：内生回归元为二元结构，威胁锚定"行动者推动采纳" | 通过（单篇） | Zorn et al. 2017 (SMJ) |

### M7（4）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | Lewbel 异方差识别工具三步法 | 无外部 IV 可用、需内部生成工具变量 | 区别于外部 IV 家族（变体 4–12）：从异方差残差内部生成 | 通过（单篇） | Wowak 2025 (MS) |
| 2 | IV 有效性诊断链完整报告 | 任何 IV 研究的必写诊断段落（副槽位 M8） | 与变体 1 配套：Lewbel 两假设 + 传统 relevance/exogeneity 五步诊断 | 通过（单篇） | Wowak 2025 (MS) |
| 8 | 双估计器双层级两阶段 IV（同 IV 双 DV） | 同一 IV 同时影响计数 DV 与连续/时长 DV | 区别于变体 1：估计器按 DV 性质匹配（NB FE vs 2SLS FE） | 通过（单篇） | Wowak 2025 (MS) |
| 13 | 连续 DV 用 2SLS + 双向 FE；稀有二元 DV 聚类 Logit | 同一理论 IV 预测连续与稀有二元结果的治理/战略面板 | 区别于变体 8（分布族匹配）：解决稀有二元与 FE 样本损失冲突 | 通过（单篇） | Zorn et al. 2017 (SMJ) |

### M4（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | 政治意识形态操作化（四步四指标聚合流程） | FEC/Open Secrets 政治捐赠数据研究（TMT 意识形态等） | 区别于识别型变体：测量操作化（四指标聚合 + 非捐赠者处理） | 可选 | Wowak 2025 (MS) |


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
**原始句锚点**: "To address this challenge, we use an IV approach that has emerged from the econometrics literature called the heteroskedastic identified instrument technique. This procedure allows us to generate valid instruments via three steps (Lewbel 2012, 2018; Bun and Harrison 2019)."
**验证状态**: 通过 (1/5 产品召回，但方法泛用性极高)
**写入日期**: 2026-05-20
**槽位**: M7
**骨架**:
> To address this challenge [of finding valid external instruments], we use an IV approach that has emerged from the econometrics literature called the heteroskedastic identified instrument technique. This technique, which has recently been adopted in [domain] research ([citations]), is designed to accommodate a setting "when no external instruments or other such information are available" ([citation], [page]). This procedure allows us to generate valid instruments via three steps ([citations]). First, we use the potentially endogenous independent variable ([IV]) as the dependent variable in a first-stage equation that features all our controls as regressors. Just as [citation] theorized and [citation] emphasize, we include all of our control variables as the regressors in this first-stage equation because doing so is the preferred specification, unless including a subset of the controls better upholds the assumptions of the model. In the second step, the technique calculates the residuals associated with each of those control variable regressors and transforms the heteroskedasticity into potentially valid IVs, but only when the assumptions of the model that we detail next are exhibited ([citations]). Finally, we incorporate the valid generated instruments into the two-stage IV fixed effects estimators.
**与原骨架差异**: 传统 IV-2SLS 要求研究者找到外部工具变量(如政策冲击、自然实验)，而 Lewbel 方法从第一阶段的**异方差残差**中内部生成有效IV。三步法核心：(1) 所有控制变量回归内生变量；(2) 残差异方差→有效IV；(3) 生成的IV纳入第二阶段。诚实边界：Lewbel 方法依赖于两个关键假设(见变体2)，若不满足则生成的IV无效。适用于"无外部IV可用"的情境。

### 变体 2: IV 有效性诊断链完整报告 (Lewbel + 传统诊断)
**来源论文**: Wowak2025 MS
**原始句锚点**: "It is worth underscoring that our generated instruments also conform to the traditional diagnostic tests pertaining to relevance and exogeneity for any type of IV."
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
**原始句锚点**: "Following research precedence, we averaged the indicators to calculate each TMT member's political ideology (Briscoe and Joshi 2017, Chin and Semadeni 2017, Gupta and Wowak 2017). In line with this literature, we assign a score of 0.5 to individuals with no political donations, indicating that they are politically moderate (Chin et al. 2013, Gupta and Wowak 2017, Gupta et al. 2018)."
**验证状态**: 可选变体 (1/5，政治意识形态研究特有)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> [IV] is calculated as the [aggregation_method] [annual] [construct] across members of a firm's [group] ([citations]). To compute this measure, we carefully followed the procedure documented in [domain] research ([citations]). We first used [source] to identify the [group_members] in each organization ([citations]). Next, we identified each [member]'s [construct] by accessing [data_source] from [database]. Using the [data], we then calculated [N] indicators that have been shown to collectively reflect [construct] ([citations]): (1) [indicator_1]; (2) [indicator_2]; (3) [indicator_3]; and (4) [indicator_4]. Each indicator ranges from [min] to [max]; [max] represents [pure_form], [min] represents [opposite_form]. Following research precedence, we [aggregation] the indicators ([citations]), as they demonstrate high reliability and internal consistency (α=[value]). In line with this literature, we assign a score of [neutral_value] to individuals with no [data], indicating that they are [neutral_label] ([citations]). That said, in robustness checks we remove [missing_data_group] from our sample and demonstrate that assigning a value of [neutral_value] to them does not meaningfully influence our results.
**与原骨架差异**: 政治意识形态的**标准操作化流程**——从 Chin et al. (2013) 确立的四个政治捐赠指标到均值聚合。关键要素：(1) 四指标全覆盖（捐赠数量比/金额比/候选人比/年份比）；(2) 高内部一致性引用 (α=0.95)；(3) 非捐赠者处理策略 (赋中性值0.5 + 排除稳健性检验)；(4) 每句都有方法论引用链。该骨架可迁移至任何使用 FEC/Open Secrets 政治捐赠数据的研究（CSR、公司创业、高管薪酬等）。

### 变体 4: 外部自然事件作工具变量 + 三因排除限制论证 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**原始句锚点**: "We focused on natural disasters in the airline's home country as an instrumental variable. First, natural disasters are exogenous, reflecting "nature's fury" (Ballesteros et al., 2017; Dutta, 2017: 443), and are not affected by airlines' international expansion."
**验证状态**: 通过 (单篇高价值，"外部自然事件→非正式关系"工具变量论证的稀缺范式)
**写入日期**: 2026-06-16
**槽位**: M8
**骨架**:
> An important consideration is that [actors] might self-select whether they [form the focal tie / take the treatment], creating an endogeneity issue. Furthermore, comparing the reduced-form [DV] model with the [mediator-included] model, Shaver ([2005]) suggested the reduced form may be mis-specified due to an omitted [mediator/endogenous regressor], and recommended an instrumental variable analysis. We focused on [an exogenous external / natural event — e.g., natural disasters in the actor's home market] as an instrumental variable. First, [the event] is exogenous, reflecting "nature's fury" ([citations]), and is not affected by [the outcome]. Second, [the event] might expose limitations of formal institutions (e.g., written rules and regulations) for acquiring strategic resources from the state, requiring [actors] to seek informal means—such as [forming the focal tie] ([citations]). Third, the existing [outcome] literature suggests that [actors] typically base [the outcome] on [alternative determinants: e.g., distance, host-market institutions, demand, own capabilities]; [the event], hence, may predict [the treatment] but have a limited effect on [the outcome] directly ([citation]). So, the instrument may satisfy exclusion-restriction conditions. We obtained data on [the event] from [source] and used it as an instrument.
**与原骨架差异**: 与变体 1–3（Lewbel 内部生成 IV）的根本区别——本变体用**外部自然/准自然事件**作 IV，且排除限制通过**三层论证**建立：(1) 事件外生性（"nature's fury"，不受结果影响）；(2) 事件→处理的渠道（制度缝隙逻辑：正式制度失效→寻求非正式关系）；(3) 事件→结果的直接渠道**缺失**（由结果文献的已知决定因素反推）。第（2）层是核心理论增量——IV 通过"挤压正式资源获取"间接推动处理。诚实边界：第（3）层"无直接渠道"是排除限制的关键假设，本质不可检验，必须用结果领域文献的既有发现支撑，不可断言。适用于 IV 通过"制度/资源缝隙"推动企业形成非正式关系（政治关联、军方关联、银企关系）的研究。配合 control-function 报告见 `../write-results/econometric-models/IV-2SLS.md` 变体 4。

### 变体 5: M8 Durbin-Wu-Hausman (DWH) Test + Gaussian Copula 内生性叙事 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: "Therefore, to further address endogeneity concerns, we conduct the Durbin-Wu-Hausman (DWH) test (Malshe & Agarwal, 2015; Whitler et al., 2018). To further substantiate the case of no endogeneity, we also use the instrument-free Gaussian copula joint estimation method (Park & Gupta, 2012) and reach similar conclusions."
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
**原始句锚点**: "The political environment during a CEO's adolescence is likely to shape their long-term ideological orientation but is less likely to directly influence the firm's CPT (Jennings & Niemi, 2014; Malmendier & Nagel, 2011). Specifically, for each CEO, we calculated the average Democratic political exposure between the ages of 15 and 25—a period widely recognized as critical for the formation of durable political beliefs."
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
**原始句锚点**: "Following the shift–share approach in economics (Burchardi, Chaney, & Hassan, 2019; Card, 2001; Tabellini, 2019), we construct a state–year instrumental variable that predicts the salience of migration issues by interacting a time-varying "push" factor with a state-specific historical "pull" factor. However, it is unlikely that either ancestry patterns fixed over four decades ago or armed conflicts occurring outside the United States plausibly affect facility-level toxic emissions except through their impact on migration and its salience, supporting the exclusion restriction."
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
**原始句锚点**: "We examine the influence of TMT political ideology on each of our dependent variables using similar forms of two-stage instrumental variable (IV) fixed effects regression. The level of analysis for the recall count model is the firm-year, and the level of analysis for the time-to-recall model is the individual recall."
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
**原始句锚点**: "However, out of an abundance of caution, and to further ameliorate concerns related to endogeneity bias that may be caused by this type of simultaneity, or other sources of endogeneity, we use IV estimation."
**验证状态**: 通过（单篇高价值；corpus 此前无"先证伪最可能威胁再以防御性 IV 收尾"的 M8 修辞变体）
**写入日期**: 2026-07-25
**槽位**: M8
**骨架**:
> [Adopt firm + year FE to absorb time-invariant and common-shock unobserved heterogeneity.] It is also possible that our estimates could exhibit bias from simultaneity if [actors] [the strategic behavior that would create reverse causality—e.g., donate to curry favoritism]. Such simultaneity is unlikely in our setting for [N] key reasons. First, prior research shows that [the focal behavior represents an actual underlying disposition, not a strategic move] ([citations]). [Relatedly, it is important to note that the literature on the confounding behavior focuses on a different object—e.g., firm lobbying dollars, not personal donations from individuals] ([citation]). Second, studies have consistently shown that [the underlying construct is highly stable over time and not apt to fluctuate strategically] ([citations]). We observe this characteristic as well; [N]% of [actors] in our sample do not [exhibit the strategic / switching behavior] during our sampling period. However, out of an abundance of caution, and to further ameliorate concerns related to endogeneity bias that may be caused by this type of simultaneity, or other sources of endogeneity, we use IV estimation.
**与原骨架差异**: 与变体 5（Chung DWH：FE → DWH 检验）和变体 1（直接引入 Lewbel IV）的根本修辞差异——本变体的 M8 结构是**先证伪最可能的内生性威胁（simultaneity），再以防御性 IV 收尾**。三步说服动作：(1) 命名具体 simultaneity 威胁（[actors] 为 [purpose] 而 [strategic behavior]）；(2) 双理由证伪——文献理由（该行为反映真实 disposition 而非策略）+ **概念区分**理由（focal 行为 ≠ 易混淆行为，如个人政治捐赠 ≠ 企业游说支出）+ **setting 特有行为证据**（[N]% 不切换政党 → 实证支撑稳定性）；(3) 才以 "out of an abundance of caution" 引入 IV。这个"先证伪后防御"顺序比"直接上 IV"更有说服力——展示研究者理解自己的 setting、不滥用 IV，且 IV 仅作为 residual threat 的保险。诚实边界："abundance of caution" **不能替代** IV 诊断（仍须报告变体 2 的完整诊断链）；行为证据（如 92% 不切换）必须是 setting 特有可观测事实，不能泛化；概念区分（个人捐赠 vs 游说）必须引用两类文献分别支撑。
**适用**: IV 的主要内生性威胁是 simultaneity / reverse-causality 且可在理论上 + 行为数据上证伪的研究；个人捐赠、个人稳定特质、长期偏好、价值观的研究（政治意识形态、人格、风险偏好）。
**禁忌**: 不要用 "abundance of caution" 掩盖 IV 诊断的缺失；行为证据百分比必须来自本文样本而非外推；证伪理由若引用文献则必须是与本文 setting 同类的文献。
**跨 skill 对齐**: 与变体 1（Lewbel 三步法）、变体 2（诊断链）配套——本变体是 IV 论证的**前置叙事**，变体 1–2 是 IV 的**技术与诊断**。三者共同构成完整 M8 IV 段落。

### 变体 10: M8 地理外生性工具变量（geography-based IV，Frankel-Romer 型）(2026-07-30)
**来源论文**: Zhou, Gao & Zhao (2017, Administrative Science Quarterly)
**原始句锚点**: "Because regions' geographic location is exogenous and predetermined by nature (Frankel and Romer, 1999), we used the distance of each province to major seaports as the instrument for the index of institutional development (Wei and Wu, 2001). We calculated the shortest physical distance from the capital city of each province to one of the two major seaports—Hong Kong and Shanghai—using the Great Circle formula with the latitudes and longitudes of cities."
**验证状态**: 通过（单篇，待第二篇交叉验证）
**槽位**: M8
**骨架**:
> "Because [the institutional/moderator variable] is endogenous to [regional economic development], we need to find an instrument that affects [the DV] indirectly through [the institutional variable]. Because [regions' geographic location] is exogenous and predetermined by nature ([Frankel and Romer, 1999]), we used [the distance of each province to major seaports] as the instrument for [the institutional variable] ([Wei and Wu, 2001]). We calculated the shortest physical distance from the capital city of each province to one of the [N] major [seaports/economic centers]—[city 1] and [city 2]—using the Great Circle formula with the latitudes and longitudes of cities. The instrumental variable estimate of [the institutional variable] was substituted into the models. The instrumental variable [exhibited a strong first-stage relationship] (first-stage *F* = [value], *p* < [.001])."
**与原骨架差异**: **geography-based IV**（Frankel-Romer 地理外生性传统）——用纯地理距离（到大港口/经济中心的物理距离，Great Circle 公式）为"区域性、随经济内生"的制度/发展变量（市场化程度、制度发展、贸易开放度）外生化。区别变体 4（自然灾害事件 IV）、变体 6（传记性暴露）、变体 7（Bartik shift-share）：本变体的外生性来自**地理前定性**（地区位置由自然决定，不随当代经济行为变化），且为**持续型地理距离**而非事件。配套报告第一阶段 *F* 确认工具强度（不可只说"valid"）。诚实点：引用 Frankel-Romer 地理外生性论证 + 替代性 geography 文献（Wei-Wu）双重背书。
**适用**: 制度发展、市场化指数、贸易开放度、基础设施可达性等"区域性、与经济发展互为因果"的变量作自变量/调节变量时；新兴市场跨地区研究（中国省际、印度/巴西邦际）。
**禁忌**: 地理距离的外生性须论证（不可默认）——若该距离通过非制度渠道影响 DV（如距离→运输成本→贸易→创新），则排除限制受损，须讨论；第一阶段 *F* 必须报告，弱工具（F<10）不可用；地理距离时不变，无法识别 within-region 时间效应，须配 FE 设计说明。

### 变体 11: M8 同行 IV 的距离梯度组合——显式管理 relevance–validity trade-off

**来源论文**: Moon, Tuli & Mukherjee (2023, *Journal of Marketing*)
**原始句锚点**: "Therefore, there is a natural trade-off between the strength and validity of peer-based instruments (see Papies, Ebbes, and Van Heerde 2017). Accordingly, to strengthen our identification strategy, we use three types of peers (i.e., industry, sector, and auditor peers) that represent different degrees of competitive proximity to the focal firm."
**验证状态**: 单篇高价值 reference-level 变体，待跨论文验证
**写入日期**: 2026-08-03
**槽位**: M8
**骨架**:
> Peer-based instruments create a natural trade-off between relevance and exclusion validity: peers closer to the focal unit are likely to predict [endogenous choice] strongly, but may also share competitive or demand shocks that affect [outcome]. We therefore construct an instrument portfolio ordered by proximity. [Close peers] provide strong behavioral relevance; [broader sector peers] reduce direct product-market overlap; and [institutional peers outside the focal market] capture shared [reporting/governance] practice while limiting competitive channels. We define each instrument as the [weighted proportion/mean] among peers, exclude the focal unit, lag the instrument, and assess sensitivity by removing each peer family in turn.

**与原骨架差异**: 现有变体主要为单一外部事件、内部生成 IV、Bartik IV 或多层级估计器。本变体的核心不是新的 IV 名称，而是把多个 peer instruments 组织成**距离梯度**：近邻提高 relevance，远邻/制度同伴改善 exclusion plausibility。作者先公开承认二者的结构性权衡，再用工具组合与逐类剔除敏感性分析管理该权衡。

**诚实边界**: 工具变量数量增加不会自动修复共同的排除限制；每一类 peers 都必须单独识别潜在直接渠道。逐类剔除只能显示结论不依赖某一工具族，不能证明剩余工具外生。必须报告第一阶段强度，并在可能时提供过度识别或替代识别检验。

**适用**: 行为扩散、披露、治理实践、同伴效应等可构造行业/部门/审计师/地理/网络多层同行池的研究。

### 变体 12: M8 行业 leave-out 均值 IV — 应对「行动者推动采纳」的内生二元结构 (EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: "To find suitable instruments for 2SLS, we follow recent research in top finance journals that uses the industry average of the focal independent variable, excluding the focal firm, to instrument for the focal predictor (Liu, Miletkov, Wei, & Yang, 2015; Yang & Zhao, 2014). Industry averages correlate with the focal firm given that firms in the same industry often have similar businesses and investment opportunities, but an industry average that excludes the focal firm is not endogenous with focal firm outcomes."
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-05
**槽位**: M8
**骨架**:
> Endogeneity concerns can arise when [binary governance / structural choice] is correlated with the error term—particularly recursive relationships between [governance] and [outcomes] and omitted determinants of adoption ([citations]). Of special concern is that [powerful actors: e.g., CEOs] may lobby for [the focal structure], making adoption endogenous to anticipated [pay / misconduct / performance] outcomes. To isolate variation in [endogenous binary structure] that is not correlated with the error term, we estimate two-stage least squares with [unit] and [time] fixed effects. Following research that instruments firm-level governance with industry averages excluding the focal firm ([citations]), our primary instrument is the [industry]-average incidence of [focal structure], computed leaving out the focal [unit]. Industry averages correlate with focal adoption because firms in the same industry share similar [business / investment / institutional] conditions, but an industry mean that excludes the focal firm is not endogenous to focal outcomes. We supplement this instrument with [N] additional instruments that correlate with [structure] but show only weak relationships with the dependent variables—[instrument_2: e.g., sum of directors' ages] and/or [instrument_3: e.g., sum of directors' tenures], selecting the secondary instrument set by dependent variable as needed ([citation]). We assess relevance with the first-stage F-test and exogeneity with Hansen's J statistic; both support instrument validity and are reported with the second-stage results.

**与原骨架差异**: 区别变体 5（Chung：同行均值作 DWH 工具、常用于连续 IV）、变体 11（Moon：多层 peers 距离梯度）——本变体的内生回归元是**二元治理/结构采纳**，威胁叙事显式锚定「[actor] 推动采纳」的 recursive governance–outcome 关系；工具组合是 **industry leave-out mean（主）+ 弱相关董事会构成汇总统计（辅）**，并按 DV 切换辅工具。诚实边界：leave-out industry mean 的排除限制依赖「行业冲击不通过非结构渠道影响焦点结果」——若行业共同冲击直接驱动 DV，排除限制受损；须报告 first-stage F 与 Hansen J，不可只声明 “valid instruments”；辅工具（董事年龄/任期之和）的相关性与外生性须分 DV 诊断，弱第一阶段不可硬用。

**适用**: 董事会结构、领导结构、委员会设置、所有权安排等可能由 CEO/内部人推动采纳的内生二元治理变量；S&P / Compustat 类大样本面板。

**跨 skill 对齐**: Results 见 `../write-results/econometric-models/IV-2SLS.md` 变体 8–10；构念「kind vs degree」辩护见 `面板数据-OLS.md` 变体 32。

### 变体 13: M7 连续 DV 用 2SLS+双向 FE；稀有二元 DV 放弃 FE 改用聚类 Logit（+ IV-Probit 稳健性预告）(EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: "To model financial misconduct, which is a binary dependent variable, we use logistic regression with year dummies and robust standard errors clustered by firm (Burns & Kedia, 2006). Given the low base rate occurrence of financial restatement (i.e., many firms never restate), fixed effects models drop a significant number of observations due to lack of variance in the dependent variable."
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-05
**槽位**: M7
**骨架**:
> Our sample is an unbalanced panel; annual observations are not independent. For continuous outcomes ([DV_list_continuous]), we estimate two-stage least squares with two-way fixed effects for [unit] and [time], which identifies effects from within-[unit] changes in [endogenous structure]. For the binary outcome ([rare_DV]), we use [logistic / probit] regression with [time] dummies and robust standard errors clustered by [unit] ([citation]). Given the low base-rate of [rare_DV]—many [units] never experience the event—fixed-effects models drop a substantial number of observations that lack within-[unit] variance in the dependent variable. We therefore absorb firm-level dependence via clustered standard errors rather than conditional fixed effects ([citation]). Because no exact logistic analogue of 2SLS exists, we confirm the binary-outcome results in robustness checks using an instrumental-variable [bivariate probit / IV-probit] specification with [time] dummies and [unit]-clustered robust standard errors.

**与原骨架差异**: 变体 8（Wowak：同 IV 下 NB FE vs 2SLS，因 DV 为计数 vs 连续）解决的是**分布族匹配**；本变体解决的是**稀有二元结果与 FE 的样本损失冲突**：主分析对连续 DV 保留 2SLS+FE（准实验强度），对稀有二元 DV 显式放弃 FE 并说明原因，用聚类 Logit 保样本，再以 IV-Probit 把识别强度拉回稳健性。诚实边界：主分析中稀有二元结果的因果语言须弱于 instrumented 连续结果（“associated with / more likely”），不可把聚类 Logit 写成与 2SLS 同等识别强度；IV-Probit 必须实际出现在 Results/Robustness，不可只预告。

**适用**: 同一理论 IV 同时预测连续结果（薪酬、绩效）与稀有二元结果（重述、违规、诉讼）的治理/战略面板。

**跨 skill 对齐**: 首次填充 `稀有结果.md` 变体 1；Results 多 DV 平行报告见 write-results IV-2SLS 变体 8。

---

## 反模式（IV 排除限制论证）

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **工具化平方项/交互项时 exclusion 未逐一论证** | 内生回归元含平方项或交互项（倒 U、曲线 IV、boundary-condition 交互），只对线性项给工具与排除理由；平方项/交互项工具的第一阶段相关性与排除限制未单独论证 | 对每个被工具化项（线性项、平方项、交互项）分别给工具、报第一阶段 F/偏 R²、独立论证排除限制；Hansen J 未拒绝不是排除限制成立的充分证明（联合过度识别检验只验证工具整体相关性，不验证每项的 exclusion）。Fini et al. 2017 (AMJ) 工具化三内生变量（peer eval / industry eval / industry eval²）即未对平方项独立论证——见 非线性模型 变体16 边界 |
