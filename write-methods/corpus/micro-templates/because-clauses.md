---
category: because-clauses
description: because 从句架构——控制变量理由、样本排除逻辑、构念效度论证的核心句法单元。
function: 抗辩性/对齐性——每个 because 从句完成一个微型论证
slots: M2, M3, M4, M6, M7, M8
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# because 从句架构（Because Clauses）

## 设计原则

because 从句是 Methods 中**最密集的说服单元**。一个 because 从句的质量决定了审稿人是否会追问 "why this control?" 或 "why this measure?"。

## 六大 because 类型

### 1. 竞争性解释型（Rival Explanation）

**功能**：论证控制变量排除的是哪一个替代理论或遗漏变量威胁。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `...because [larger and older firms] may have more resources for both [IV] and [DV].` | 安全 | M6 |
| `...because [rival theory] predicts that [alternative mechanism] drives [outcome].` | 安全 | M6 |
| `...because [omitted variable] may confound the [IV-DV] relationship by [mechanism].` | 安全 | M6 |
| `...because [actor] may be sensitive to [outcome] ([citation]), so it is important to control for [related_factor].` | 安全 | M6 |
| `...because [time-varying shocks] may simultaneously affect [IV] and [DV].` | 安全 | M6 |

**关键区分**：
- 弱：`...because [variable] is important.`（没有说明威胁什么）
- 强：`...because [variable] may confound [IV-DV] by [mechanism].`（明确的 omitted variable 逻辑）

### 2. 构念效度型（Construct Validity）

**功能**：论证测量捕捉了理论构念。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `This measure captures [construct] because [construct-validity logic].` | 安全 | M3, M4 |
| `The measure captures [construct] because [theoretical link between text feature and underlying construct].` | 安全 | 文本构念 |
| `We chose this source because [theoretical reason for text reflecting construct].` | 安全 | 文本构念 |
| `This variable corresponds to Hypothesis [x] because it captures [mechanism].` | 安全 | M4 |
| `Following extant research ([citation]), we used [measure] as our primary measure because it broadly reflects [N] mechanisms: [mechanism_list].` | 安全 | M4 |

### 3. 样本排除型（Sample Exclusion）

**功能**：为每一步样本损失提供理由。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We excluded [cases] because [comparability/measurement/identification reason].` | 安全 | M2 |
| `We also excluded firms with fewer than [three] years of consecutive data to ensure sufficient within-firm variation for fixed-effects estimation.` | 安全 | M2 |
| `Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].` | 安全 | M2 |
| `Because [outcome] is rare, a simple random sample would yield too few [cases]; we therefore used [sampling strategy].` | 安全 | M2 |

### 4. 机制解释型（Mechanism Linkage）

**功能**：在变量操作化段落中，连接构念→测量→理论机制。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `...because it captures [mechanism], which links [IV] to [DV] through [process].` | 安全 | M4 |
| `...because [theoretical_rationale], and research indicates that [IV] is one of the most effective tools to do so ([citation]).` | 安全 | M4 |
| `...because [measure] proxies for [mechanism_A] through [rationale] ([citation]).` | 安全 | M4, M5 |
| `The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not..., but, rather, a relative increase...` | 安全 | M5 |

### 5. 估计器选择型（Estimator Justification）

**功能**：论证为什么选这个估计器而不是替代方案。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `Because [DV] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model].` | 安全 | M7 |
| `We employ [unit] fixed effects rather than random effects because the Hausman test rejects...` | 安全 | M7 |
| `Because [DV] is persistent and our panel is short, fixed-effects estimation may be biased (Nickell bias). We therefore estimate...` | 安全 | M7 |
| `Because the shape of [event timing] is not known ex ante, we compare [distributions] and select [distribution] based on [fit criterion].` | 安全 | M7 |
| `Coefficients indicate direction, but substantive interpretation requires [marginal effects/predicted probabilities/hazard ratios].` | 安全 | M7 |

### 6. 识别策略型（Identification Defense）

**功能**：在识别策略段落中，论证为什么威胁不严重或已被处理。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Shock/event] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason].` | 安全 | M8 |
| `It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor].` | 安全 | M8 |
| `Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].` | 安全 | M8 |
| `Because [network-based construct] may capture common shocks rather than true peer influence, we conduct falsification tests.` | 安全 | M8 |

---

## because 密度标杆（启发估计，非计算基准）

> **来源审计（2026-09-20）**：下表数字出自 2026-05 micro-templates 富集批次，早于句档基建（2026-08-29），无计算脚本、无 slot 级底层数据可复现（.sentences.md 仅 section 级标注，无 M6/M8 槽位）。定位为未经计算的启发式印象：不得作为字数配额、门禁或逐句目标使用。原理性目标（见下方）不受影响。待 claim-design mismatch 基线建立后以可复现口径替代。

| 密度等级 | M6 because 覆盖率 | MVP30 顶刊表现 |
|---------|-------------------|----------------|
| 优秀 | >= 60% | Darby2026 JOM (~85%) |
| 良好 | 40–59% | SMJ/JM/ASQ 多数 |
| 及格 | 30–39% | MVP30 中位数 (~35%) |
| 需关注 | < 30% | AMJ 约 30% 可低至 0% |

**目标**：每个控制变量、每个样本排除步骤、每个关键测量都应有 because 从句。

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We control for Size, Age, and ROA.` | 无 because 逻辑 | `We control for firm size because larger firms have more resources for both [IV] and [DV].` |
| `We excluded missing values.` | 无排除理由 | `We excluded observations with missing [variable] because [reason for missingness threatening validity].` |
| `This measure is good because it is reliable.` | 循环论证 | `This measure captures [construct] because [theoretical link], validated by [external benchmark].` |
| `Because the data say so.` | 无理论机制 | `Because [theory] predicts that [mechanism] links [IV] to [DV].` |


### 变体 A：理论驱动观察窗 because 从句（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "Data were collected for [years X to Y], and [focal events] are observed from [X'] to [Y'], inclusive, because the [model's] lag structure requires collecting data for the earlier and later time periods. We chose this time frame because [the theoretical process] has exerted increased [pressure] for [the focal outcome] during this period ([citation])."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Sample and Data Collection（P1 末）

**原文锚定**:
> "We chose this time frame because institutional investors have exerted increased pressure for greater management accountability to shareholders during this period (Davis and Thompson, 1994)."

**关键特征**:
- 观察窗选择自带理论 because：不是"数据可得"而是"该理论过程在此期间加剧"——窗口本身成为构念活跃期的证据，样本期即研究设计的一部分
- 双窗分离句式（数据收集窗 vs 事件观察窗）用 lag structure 因果从句衔接——技术性理由（滞后需要缓冲）与理论性理由（过程活跃期）各归其位
- 现在进行时 "have exerted" 把窗口论证锚定在过程的持续性而非一次性时点，暗示现象在窗内充分展开

**适用**: 事件观察窗短于数据收集窗的面板/事件史设计；观察期起点由理论过程（监管压力、制度变迁、技术浪潮）界定而非数据可得性决定的研究

**禁忌**: 理论 because 需有可引的过程性证据（文献综述或制度化事实），不能拿"我们认为这段重要"充数；窗口选择若同时受数据可得性约束，诚实做法是双理由并列

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


### 变体 B：测量窗对齐 because 从句 — 为交互项估计统一累积窗（anand_mukherjee_2024 型）
- **出处**: Anand & Mukherjee 2024 (Organization Science)，医疗设备/制药召回面板
- **槽位**: M4 自变量操作化
- **可迁移性**: 高（任何多个解释变量各带滞后/累积窗、又要两两进交互的设定）
- **区别于**: 变体 A（理论驱动观察窗）— 变体 A 的窗口由构念活跃期证据决定；本变体的窗口由估计设计决定：与另一解释变量的累积窗对齐，使交互项可估，且以 post hoc 换窗检验兜底
- **原始句锚点**（Anand & Mukherjee 2024 原文）: "By accumulating prior patent counts for 10 years, we also achieve congruence with our other count variables of accumulated recalls, which is helpful as we estimate interactions of pairs of independent variables."
- **验证状态**: VERIFIED (expert_audit_override, user 2026-08-29: 用户裁决产品召回主题全部蒸馏成果升 VERIFIED)
- **写入日期**: 2026-08-29
[骨架]:
[Accumulated IV] of a [unit] for a specific year t is the cumulative count of [events] issued by the [unit] until the prior year (t - 1). To achieve homogeneity and consistency of this measure, we accumulate [events] over an equal number of years, [k], for each year in the main models. We use time periods other than [k] years for [the measure] for a post hoc test. By accumulating [second measure] for [k] years, we also achieve congruence with our other count variables, which is helpful as we estimate interactions of pairs of independent variables for testing [Hypothesis].

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:m4_window_congruence_for_interactions -->


### 变体 C：M3 计数测量=逐次评价事件归因 because 链（fini_jourdan_perkmann_2017 型）

**来源论文**: Fini, Jourdan & Perkmann 2017 (*Academy of Management Journal*)
**原始句锚点**: "The number of grants is an appropriate measure of peer evaluation because each additional grant is based on an additional attribution of value to the researcher by a panel of peer reviewers."
**验证状态**: EMERGING（单篇；`section_variant`）
**槽位**: M3（因变量操作化 — 构念效度 because 型扩展）
**骨架**:
> The [count measure] is an appropriate measure of [social-evaluation construct] because each additional [count unit] is based on an additional [attribution of value] to the [candidate] by a [panel of evaluators].
**与原骨架差异**: 现有构念效度 because 微模板为通用单句（"This measure captures [construct] because [logic]"）；本变体专门处理"计数测量承载评价/认可类构念"的情形——把计数分解为**逐次评价事件**（each additional unit = one more attribution by an evaluator panel），使 count 与构念（audience valuation）之间的对应关系显式化。适用于 grant 数、得票数、奖项数、采纳数等"评审性行为计数"作 DV 的设计。
**诚实边界**: 只适用于计数单位本身构成一次独立评价行为的测量；纯产出类计数（专利数、发文量）不承载评价者归因，套用此链会构成构念跳跃。

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:m3_count_dv_repeated_evaluation_attribution_chain -->


### 变体 D：多维决定子分解 because 链——"captures A but not B" 转轴 + 混同构念分离 + 归纳类型学（dewan_jensen2020 型）

**模板**:
> "A key determinant of [outcome] is [the determinant] ([authority citation]). [The determinant] is multidimensional, however, thus suggesting that controls for different dimensions of [the determinant] are required. First, we control for [dimension-1 measure]. [Domain definition of dimension 1] ([citations]). Accordingly, the larger [dimension 1], the larger [the extent it captures]. Second, we control for [dimension-2 measure], i.e., [definition] ([citations]). While [dimension-1 and dimension-2 measures] capture [aspect A] of [the determinant], these variables do not necessarily capture [aspect B]. To capture [aspect B], we control for [dimension-3 measure]. This variable captures [what it records, including the boundary rule for zero values]. Finally, we control for [the type dimension]. Because there is no taken-for-granted typology of [the domain], we inductively developed a typology of [types] by coding all [source documents] in the sample. The result was [k] categories: [list]. ... Further, it is important to separate [unit-level construct]'s [measure] from [context-level construct]'s [measure]. We therefore control for [prior context measure] operationalized as [transformation of coverage one period prior to the focal event]."

**要点**:
- "multidimensional, however, thus suggesting that controls for different dimensions are required" 一句把一组名义控制变量升格为**维度分解架构**：每个控制各承接一维，维度间用 "While [A-measures] capture [aspect A], these variables do not necessarily capture [aspect B]" 的**否定转轴**连接——控制变量段的内部结构靠"测量了什么/没测量什么"的显式对照推进，而非平铺列举。
- 混同构念分离：当两个构念共享同一测量族（[unit] 的报道量 vs [context] 的报道量），用 "it is important to separate X's [measure] from Y's [measure]. We therefore control for ..." 显式切开，并给分离操作化（事件前一期 + 转换），防的是 [context 构念] 与 [unit 构念] 的机械相关污染。
- 归纳类型学三句式："no taken-for-granted typology exists → we inductively developed a typology by coding all [documents] → The result was [k] categories"——无既有分类时的合法化路径，"all ... in the sample" 全集编码声明承担可审计性。

**诚实边界**: 分解架构的前提是 [authority citation] 真的支持"多维"判断，否则是伪架构；归纳类型学应补编码者构成与一致性报告（本范文未报，勿模仿）；分离操作的时点选择（前一期）需一句 because 交代为何前置。

<!-- wb:dewan_2020_catching_the_big_fish_the_role_of_scandals_in_mak:m6_multidimensional_determinant_decomposition -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
