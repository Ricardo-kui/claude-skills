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
  - "pupovac_astvansh_carrillat_legoux_2026_pom (Production and Operations Management): automotive supplier setting defense, mandatory/voluntary disclosure threshold operationalization"
  - "du_tsolmon_2024_post_ma_retention_orsc (Organization Science): TMT retention rate DV 文献基准锚定（54.8% vs 前人 55%/59.4%）+ 三层异质数据库漏斗附录审计"
  - "malshe2015 (Journal of Marketing): cross-database manual matching (ACSI↔Compustat no common ID) + 5-source merge funnel"
  - "schumacher_keck_tang_2020_smj (Strategic Management Journal): nonoverlapping construct-formation/outcome windows + media/option dual-proxy convergence"
  - "liu_shankar2015 (Management Science): recall severity theory-based classification, media relevancy-score threshold, parent-brand vs nameplate advertising split, monthly recall aggregation"
  - "Zorn_Shropshire_Martin_Combs_Ketchen_2017_SMJ (Strategic Management Journal): categorical lone-insider board as change-in-kind vs continuous independence"
  - "desjardine_li_shi_2025_amj (Academy of Management Journal): single-intermediary setting defense (a/b/c + single-agency consistency), multi-source list + coverage-bound sample window, letter-grade DV boundary-distance operationalization, composite-construct stepwise construction + threshold defense + feasibility argument, rival mirror control convention, theory-estimator alignment + no-lag defense (Bellemare)"
  - "ridge_hill_ingram_kolomeitsev_worrell_2024_amj (Academy of Management Journal): one-sentence temporal-spacing declaration (DV t+1 / IV & controls t) as reverse-causality preemption; control variables dual-sided because (one reason for DV + one reason for covarying with the trait)"
variants_count: 40
created: 2026-05-18
updated: 2026-08-12
---

# 面板数据-OLS — Methods 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M1 | 3 | 15, 23, 33 |
| M2 | 10 | 2, 6, 9, 11, 12, 16, 26, 27, 31, 34 |
| M2.5 | 2 | 20, 39 |
| M3 | 3 | 17, 25, 35 |
| M4 | 7 | 3, 19, 24, 29, 30, 32, 36 |
| M5 | 3 | 4, 5, 28 |
| M6 | 4 | 1, 14, 37, 40 |
| M7 | 7 | 7, 10, 13, 18, 21, 22, 38 |
| M8 | 1 | 8 |

### M1（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 15 | 单行业设置 — 双重现象共存辩护 | 单行业样本一句式情境正当化：两个理论前提现象同时存在 | — | 通过（单篇） | Cui, Yang & Vertinsky SMJ |
| 23 | 行业统计 + 先例对齐的设置辩护 | 单行业事件研究：行业统计证互依 + "大事件"抽样标准 + 先例对齐 | 区别于变体9（制度断点）与变体15（双重现象）：行业统计+抽样阈值+先例对齐 | 通过（单篇） | Pupovac et al. 2026 POM |
| 33 | 单一中介机构设置辩护 | 以单个评级/平台/审核机构为情境：a/b/c 三理由+单一机构一致性 | 区别于变体15（双重现象）与变体23（行业统计）：中介机构选择+方法差异消解 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |

### M2（10）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 样本交集漏斗 | 多库合并后报告起始N到最终N的逐层排除审计 | — | 通过（3/4 复现） | Darby2026/2025/2023 |
| 6 | 多通道精英/关键行为人招募 | 难以接触的研究对象（高管/董事/精英决策者）多通道招募 | — | 待交叉 | Mannor et al. 2016 SMJ |
| 9 | 制度断点样本辩护 | 单行业面板：制度事件定起始、数据可得定终止、单行业理论理由 | 区别于变体15（M1 设置辩护）：M2 样本边界三重正当性 | 待交叉 | Desai 2011 AMJ |
| 11 | 匹配样本层次回退 + 匹配平衡保守检验 | 匹配质量与样本量存在 trade-off 的匹配样本设计 | — | 待交叉 | Pfarrer et al. 2010 AMJ |
| 12 | 单行业面板 + SIC 边界意识 + 限制样本稳健性 | 单行业样本受少数非核心行业企业驱动的担忧 | 区别于变体9（制度断点定边界）：行业分类模糊性+限制样本稳健性 | 待交叉 | Darby et al. 2026 JOM |
| 16 | 多源 alliance 数据库合并与交叉验证 | 多数据库互补合并，防重复计数、防 announced-but-not-realized | 在变体2（交集漏斗）基础上扩展为完整段落：多源互补+人工 due diligence | 通过（单篇） | Cui, Yang & Vertinsky SMJ |
| 26 | 跨库手工匹配（无共同标识符）+ 多源漏斗 | 两核心库无共同标识符（如 ACSI↔Compustat）须手工匹配 | 区别于变体16（自动交叉验证）与变体2（逐步交集）：手工匹配明示+五库漏斗 | 通过（单篇） | Malshe & Agarwal 2015 JM |
| 27 | 构念形成窗—结果观察窗分离 + 双代理收敛 | 稳定特质代理可能被同期结果反向污染（副槽位 M4、M8） | 区别于变体19（同期/滞后期权 moneyness）：完整形成期与观察期切开+双代理三角化 | 通过（单篇） | Schumacher, Keck & Tang 2020 SMJ |
| 31 | 异频数据时间对齐 — 事件聚合至结果频率 | event-day vs 月 vs 年三频数据对齐（副槽位 M4） | 区别于变体2/26（强调多库交集N）：解决频率对齐 | 待交叉 | Liu & Shankar 2015 MS |
| 34 | 多源清单 + 覆盖边界定样本窗 | 多库枚举后直接交集，数据库覆盖边界定起始/终止 | 区别于变体9（制度事件定起始）：数据覆盖驱动双边界 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |

### M2.5（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 20 | Model-Free Evidence 预览 | 正式回归前以 quartile 均值/中位数展示无条件关系 | — | 通过（单篇） | Chung, Low & Rust 2022 JAMS |
| 39 | 时间间隔声明（DV t+1 / IV & controls t） | 纵贯面板需在 Methods 层预先化解反向因果 | 区别于变体 20（model-free 预览）与变体 27（窗口分离）：单句 baseline 承诺，更通用 | EMERGING | Ridge et al. 2024 (AMJ) |

### M3（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 17 | 多维行为指标 → factor score → 平均值 | 多维行为 DV：子维度理论含义+信度+合成方式 | — | 通过（单篇） | Cui, Yang & Vertinsky SMJ |
| 25 | DV 文献基准锚定 — 均值与前人文献对比 | 新构建比率/计数 DV 的外部效度锚定 | 语料内首见 DV 外部效度锚定（现有变体无） | 通过（单篇） | Du & Tsolmon 2024 ORSC |
| 35 | 离散化等级 DV 边界距离操作化 | letter-grade DV：边界距离变量+边际影响预检验 | 区别于变体17（factor score）与变体25（文献锚定）：边界聚集+边际影响声明 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |

### M4（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | IV 选择三层 because 论证链 | 单一操作化同时代理多个理论机制的 IV 辩护 | — | 可选 | Darby2023 MSOM |
| 19 | 高管信心期权 moneyness 操作化 | 高管自信构念操作化（公式+滞后+因果优先） | — | 通过（单篇） | Chung, Low & Rust 2022 JAMS |
| 24 | 法律强制披露阈值 → 自愿披露操作化 | 法律-会计准则张力转化为构念变异空间 | — | 通过（单篇） | Pupovac et al. 2026 POM |
| 29 | 召回严重度理论分类 — 后果类型二元操作化 | 监管后果描述→心理学可辩护的二元 severity | — | 待交叉 | Liu & Shankar 2015 MS |
| 30 | 媒体覆盖 — 双索引相关度阈值 + 互补数据源 | 媒体计数需 face-validity 链：双索引阈值+双源互补 | 区别于 generic media count：强制双索引 relevancy 阈值+排除逻辑 | 待交叉 | Liu & Shankar 2015 MS |
| 32 | 结构二元特征操作化为「kind」而非「degree」 | 治理/组织极端结构二元化（lone-insider 董事会等） | 区别于现有 M4 变体（连续构念/阈值披露/双代理收敛）：kind≠degree 辩护+稳健性预告 | 通过（单篇） | Zorn et al. 2017 SMJ |
| 36 | 复合测量构念分步构建 | 乘积/交集型复合 IV：阈值辩护+可行性论证+分步计算 | 区别于变体3（三层 because 机制代理）与变体19（moneyness）：双持有侧乘积+可行性 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |

### M5（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | Mixed-effects within/between 机制分解 | 面板中区分个体内变化 vs 个体间差异的机制检验 | — | 可选 | Darby2023 MSOM |
| 5 | 替代变量机制对齐矩阵 | 一个构念→多个可分离机制的三角验证（配合机制对齐图） | 区别于变体4（within/between 分解）：主变量+替代变量×机制映射矩阵 | 可选 | Darby2023 MSOM |
| 28 | Binary-panel GEE + 全零单元保留 + 正式曲线识别链 | 二元面板大量全零单元 + U/倒U假设（副槽位 M7、M8） | 区别于变体22（时不变 IV 选 GEE）：保留全零单元为首要理由+曲线四事前约束 | 通过（单篇） | Bendig et al. 2024 ETP |

### M6（4）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 控制变量分层 because 结构 | 控制变量的黄金标准：按层级递进+每变量显式 because | — | 通过（4/4 复现） | Darby2026/2025/2023 + Eilert2017 |
| 14 | 全谱系控制变量 — 高 because 密度 + 事件控制 + CEO 人格 | 文本构念+市场反应交叉领域、多种混淆来源并存 | 在变体1（分层 because）基础上三升级：RavenPack 事件控制+Big5 人格+互补DV维度 | 待交叉 | Li et al. 2026 JOM |
| 37 | rival 镜像控制变量惯例 | 对手侧镜像控制：引用前例+命名规则+聚合方式一句完成 | 区别于变体1（分层 because）与变体14（全谱系）：跨主体镜像控制 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |
| 40 | 控制变量"双面 because" — 对 DV 一条理由 + 对 IV 共变一条理由 | CEO/个体特质 → 结果研究，控制为何与特质共变最易被质疑时 | 区别于变体14（强调 because 密度）：每个控制对 DV 与对 IV 各一条理由，平行论证结构 | EMERGING | Ridge et al. 2024 (AMJ) |

### M7（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 7 | 嵌套横截面数据的聚类稳健标准误 | 数据嵌套（决策嵌于高管）但不足以跑多层模型 | — | 待交叉 | Mannor et al. 2016 SMJ |
| 10 | Hausman 检验 — FE vs RE 选择 | 标准 FE/RE 选择三步段 | 与变体13 互补（其处理 theory→RE 路径） | 待交叉 | Bamberger et al. 2021 JM |
| 13 | 随机效应选择三重辩护 — 理论+Hausman+ICC | 理论指向 RE（关注跨单元差异）时的系统辩护 | 区别于变体10（标准 Hausman→FE）：理论理由+Hausman+ICC 三层递进 | 待交叉 | Li et al. 2026 JOM |
| 18 | dyad fixed effects + dyad 聚类标准误 | dyad 面板 + 需具体时不变混淆源举例 | 与变体7（嵌套横截面聚类）互补：dyad FE+混淆源实例化 | 通过（单篇） | Cui, Yang & Vertinsky SMJ |
| 21 | 三向交互模型设定 | X×W1×W2 设计：完整方程+mean-centering+聚类SE | — | 通过（单篇） | Chung, Low & Rust 2022 JAMS |
| 22 | GEE + AR(1) working correlation — 时不变焦点 IV | 焦点 IV 时不变（意识形态/人格/创始人身份等），firm FE 会吸收主效应 | 区别于变体10/13（Hausman/ICC 选 FE/RE）：按 IV 时不变性选 GEE | 通过（单篇） | Abdurakhmonov et al. 2026 JOM |
| 38 | 理论-估计量对齐 + 不滞后辩护 | between-unit 理论 → pooled OLS 显式对齐；当前期机制 → 不滞后（Bellemare） | 区别于变体10/13（Hausman/ICC）：理论对齐+不滞后反向论证 | 待交叉 | DesJardine, Li & Shi 2025 AMJ |

### M8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 8 | 回顾性偏差三角检验 | 依赖事后自我报告的数据：控制情感变量+定性定量一致性+替代测量复制 | — | 待交叉 | Mannor et al. 2016 SMJ |

## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `面板数据-OLS` 专用变体）。

## 设计特征摘要

- **because密度标杆**: MVP30顶刊中位数~35%，优秀>=60%，Darby2026达~85%
- **控制变量层级**: recall-level → executive-level → firm-level → board-level → ownership concentration
- **because逻辑**: 每个控制变量需回答"为什么影响DV"和"为什么与IV相关"
- **跨论文复现率**: 分层控制变量结构在 4/4 产品召回顶刊论文中完全复现

## 累积变体

### 变体 1: 控制变量分层 because 结构 (4/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Eilert2017 JM / Darby2023 MSOM
**原始句锚点**: We included a broad set of control variables that influence recalls directly and those that help address alternative explanations (Shang and Rönkkö 2022); in our case, variables correlated with ownership by large institutional investors that may also influence the time-to-recall.
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
**原始句锚点**: The intersection of these datasets resulted in a sample of 2982 high severity recalls across 69 publicly traded firms from 2002 to 2020.
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
**原始句锚点**: We used CEO Ownership as our primary measure because it is a broad, comprehensive measure that reflects the three related, but distinct, mechanisms we theorized about in Hypothesis 1—firm financial interests, CEO power, and CEO financial interests.
**验证状态**: 可选变体 (1/4，但生成力极高)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> We used [IV] as our primary measure because it is a broad, comprehensive measure that reflects the [number] related, but distinct, mechanisms we theorized about in [Hypothesis]—[mechanism_1], [mechanism_2], and [mechanism_3]. First, [theoretical_rationale_1] ([citation]), and research indicates that [IV] is one of the most effective tools to do so ([citation]). Second, research suggests that [IV_property_2] ([citation]). Third, [IV_property_3] ([citation]). Overall, prior studies conclude that [IV] is key to understanding [theoretical_consequence] ([citation]), which is why we use it as our primary measure, although we examine alternative measures in [location].
**与原骨架差异**: 一般论文在M4中简单报告"We measure X as Y"，而此骨架构建了从构念→操作化→多机制映射的完整论证链。适用于任何**单一操作化同时代理多个理论机制**的情境。关键策略：(1) 理论机制枚举（"three related, but distinct, mechanisms"）；(2) 每个机制有独立文献链；(3) 末句预告替代变量检验（"although we examine alternative measures"），建立M4→M5的叙事桥梁。

### 变体 4: Mixed-effects within/between 机制分解
**来源论文**: Darby2023 MSOM
**原始句锚点**: The results suggest that the effect of CEO stock ownership is driven by the within-component rather than the between-component. That is, it is not the difference in CEO stock ownership between firms, but, rather, a relative increase in stock ownership for a given CEO within the same firm that explains recall delays.
**验证状态**: 可选变体 (1/4，机制检验设计特有)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> We used mixed-effects models to explore the within-[unit] and between-[unit] effects of [IV], and the results are reported in [Table_reference]. Model ([ref]) indicates that the within-component of [IV] has a [direction] and [significance] relationship with [DV] (β = [value], p < [threshold]), whereas the between-component is [not statistically significant / opposite direction]. The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not the difference in [IV] between [units], but, rather, a relative increase in [IV] for a given [unit] within the same [cluster] that explains [DV].
**与原骨架差异**: 这是将统计结果翻译为机制语言的核心句式。关键策略：(1) 报告within/between系数对比；(2) "it is not... but, rather..."句式将统计输出转化为理论叙事；(3) 明确指出是"个体内部变化"还是"个体间差异"驱动效应。适用于任何面板数据中需要区分个体内变化vs个体间差异的机制检验。

### 变体 5: 替代变量机制对齐矩阵
**来源论文**: Darby2023 MSOM
**原始句锚点**: To probe these three mechanisms at a more granular level, we replicated our recurrent-event AFT analyses using two alternative measures of CEO stock ownership—specifically, CEO Equity-Based Compensation and CEO Ownership (Monetary).
**验证状态**: 可选变体 (1/4，需配合 Figure 1 机制对齐图使用)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> Following extant research ([citation]), we used [Primary_IV] as our primary measure because it broadly reflects [number] mechanisms: [mechanism_list]. To probe these mechanisms at a more granular level, we replicated our analyses using two alternative measures of [construct]—[Alternative_1] and [Alternative_2]. We measured [Alternative_1] as [definition]. We measured [Alternative_2] as [definition]. [Figure_reference] details each measure and its alignment with our theorized mechanisms. Both our primary measure and the alternative measures inherently reflect [shared_mechanism]. [Alternative_1] also proxies for [mechanism_A] because [rationale] ([citation]), whereas [Alternative_2] also proxies for [mechanism_B] because [rationale] ([citation]). Thus, although our primary measure is comprehensive and reflects all [number] mechanisms, the alternative measures help us examine whether, indeed, all [number] mechanisms contribute to [DV].
**与原骨架差异**: 这是**三角验证**策略在 variable construction 层面的应用。关键要素：(1) 主变量+替代变量矩阵；(2) Figure 1 机制对齐图（每个变量→哪些机制→理论基础）；(3) 部分重叠的机制映射（变量A覆盖机制1+2，变量B覆盖机制1+3，变量C覆盖机制2+3）；(4) "虽然主变量全面，但替代变量帮我们检验是否所有机制都起作用"的诚实表述。适用于任何"一个构念→多个可分离机制"的构念效度设计。

### 变体 6: M2 多通道精英/关键行为人招募 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: Recognizing the challenge of the last criterion in particular, we used four methods to recruit participants. First, several key advocates for our research served on the boards of Fortune 500 companies and agreed to contact as many of their director colleagues as possible on our behalf.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We recruited [actors] through [N] channels to maximize sample diversity and reduce selection bias. First, we partnered with [organization_type_A: e.g., board advocacy group] which provided access to [actor_pool_A]. Second, we worked with [organization_type_B: e.g., consulting firm] to identify [actor_pool_B]. Third, we contacted [organization_type_C: e.g., alumni office] for [actor_pool_C]. Finally, we used snowball sampling through [references] to reach additional participants. This multi-channel approach yielded [N_final] [actors] representing [N_firms/units] across [N_industries] industries.
**与原骨架差异**: 针对难以接触的研究对象（高管、董事会成员、精英决策者），单一招募渠道会导致样本集中于某一类型——多通道招募通过制度多样性（advocacy groups vs consulting partners vs alumni networks）增加样本覆盖。关键要素：每个通道说明其提供哪类参与者，最终汇总样本的行业分布。

### 变体 7: M7 嵌套横截面数据的聚类稳健标准误 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: To account for the nonindependence in our data (i.e., the multiple strategic decisions per executive), we specified Huber/White/sandwich standard errors using the “robust” option in Stata 12. Decisions were clustered by executive.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> Because our data involve [lower_unit] nested within [higher_unit] (e.g., decisions nested within executives), observations are not independent. We therefore estimated [models] with [SE_type] robust standard errors clustered by [cluster_level] to account for within-[cluster] correlation of the error terms ([citation]). This approach treats each [cluster] as an independent sampling unit while allowing [lower_units] within the same [cluster] to share unobserved characteristics.
**与原骨架差异**: 当数据具有嵌套结构（如多个决策嵌套在同一高管/公司内）但不足以运行多层模型（样本量/top-level 单元数不足）时，聚类稳健SE是最小负担的解决方案。关键：明确说明嵌套层级和聚类层级，解释为什么这样聚类（共享不可观测特征）。

### 变体 8: M8 回顾性偏差三角检验 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: We thus took steps to ensure that the lengthier time horizon for some of the decisions did not introduce retrospective bias into our study. First, and as we discuss later, we controlled for executives' self-ratings of decision quality and recent performance in all models.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M8
**骨架**:
> A potential concern with [retrospective/interview-based] data is that [actors]'s recollections may be colored by [outcome knowledge/hindsight]. We addressed this concern through a triangulation approach: First, we controlled for [affective/outcome variables: e.g., satisfaction with decision outcome] to partial out post-hoc rationalization. Second, we compared [qualitative/text patterns] with [quantitative/archival patterns] to check consistency. Third, we replicated our findings using [alternative measure/sample] that is less susceptible to retrospective bias. Results were consistent across all approaches.
**与原骨架差异**: 适用于任何依赖事后自我报告的研究（访谈、问卷、回忆数据）。三管齐下：(1) 控制情感/结果变量（partial out halo）；(2) 定性-定量一致性检查；(3) 替代测量复制。

### 变体 9: M2 制度断点样本辩护 — 行业收缩+时间边界双重正当性 (1篇高价值)
**来源论文**: Desai 2011 (Academy of Management Journal)
**原始句锚点**: I tested these hypotheses on a panel of all U.S. class I railroad firms operating between 1980 and 2003. The U.S. railroad industry was deregulated in 1980, making prior years incomparable with later ones (Smith & Grimm, 1987).
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> The sample period begins in [year_start] because [institutional_event: e.g., regulatory change / industry deregulation] fundamentally altered [key_process] in [industry]. Before [year_start], [condition_A]; after [year_start], [condition_B], making the post-[year_start] period uniquely suited to testing our theory. The sample ends in [year_end], the last year for which [data_source] was available. We focus on a single industry—[industry_name]—to hold constant [confounds: e.g., regulatory environment, technological trajectory, product characteristics] that vary across industries. This single-industry design maximizes internal validity at the expense of generalizability, a trade-off appropriate for theory testing.
**与原骨架差异**: 单行业面板的样本辩护需要完成三重正当性：(1) 制度/法规事件作为起始边界（不早不晚）；(2) 数据可得性作为终止边界；(3) 单行业选择的理论理由（holding confounds constant → internal validity > generalizability）。与多行业面板的"we used all firms in Compustat"形成对比。

### 变体 10: M7 Hausman 检验 — FE vs RE 选择 (1篇高价值)
**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**原始句锚点**: Our choice for a fixed-effects model over a mixed-effects model is appropriate, as the Hausman (1978) test indicates (χ2/d.f. = 24.6, p <.01).
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used a [Hausman test] to determine whether [fixed effects] or [random effects] was more appropriate for our panel structure. The test strongly rejected the null hypothesis that the [unit]-specific effects are uncorrelated with the regressors (χ² = [value], p < [threshold]), indicating that [fixed effects] is the preferred specification. We therefore estimated [FE_estimator] with [SE_type] clustered by [cluster_level].
**与原骨架差异**: 标准 FE/RE 选择段落。关键三步：(1) Hausman 检验结果（χ² + p-value）；(2) 解释拒绝意味着什么（"unit-specific effects correlated with regressors"）；(3) 据此选择估计器 + 标准误声明。

### 变体 11: M2 匹配样本层次回退 + 匹配平衡保守检验 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "We then matched each high-reputation firm with three firms from the same four-digit SIC code that were similar in assets, revenues, and return on assets (ROA) (Combs & Skill, 2003; Porac, Wade, & Pollock, 1999). Where appropriate matches were not found at the four-digit level, we looked at three-digit and two-digit SIC codes for similar firms (Combs & Skill, 2003). … A t-test comparing differences in firm size (total assets) revealed no significant differences between the 80 high-reputation and 211 matched companies (t = −0.35, n.s.); however, in keeping with the predictions of prior reputation research (Roberts & Dowling, 2002), there were significant differences in revenues and ROA ($35.1 vs. $16.8 billion, p < .001; and 8.97 percent vs. 4.28 percent, p < .001, respectively)."
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We used a matched sample design to construct a comparison group of [units] that did not experience [treatment] but were otherwise similar on [key dimensions]. Specifically, we matched each [treated_unit] to [N] [control_units] in the same [industry/sector] and [time_period] based on [matching_criteria: e.g., size, age, performance]. When a close match was unavailable at [strict_criteria], we relaxed the criteria to find the closest available match—a hierarchical fallback approach that prioritizes match quality while preserving sample size. To ensure that the matched groups are balanced, we compared [treated] and [control] groups on [N] characteristics using [t-tests / standardized differences]. No significant differences were found across any of the [N] dimensions (all p > [threshold]), suggesting that the matching procedure achieved adequate balance.
**与原骨架差异**: 标准匹配样本段落仅报告"we matched on X"——Pfarrer 增加了两个关键要素：(1) **层次回退**——先在严格维度匹配，无匹配时放宽标准，透明化匹配的灵活边界；(2) **匹配平衡保守检验**——使用保守的 t-test（而非仅标准差异）验证处理组和对照组在所有匹配维度上的可比性。适用于匹配样本设计中匹配质量与样本量之间存在 trade-off 的场景。

### 变体 12: M2 单行业面板 + SIC 边界意识 + 限制样本稳健性 (1篇高价值)
**来源论文**: Darby, Wowak, Ketchen, Connelly & Skowronski 2026 (Journal of Operations Management)
**原始句锚点**: However, the sample was not limited to this industry because firms may be formally classified in other industries (e.g., Proctor & Gamble in SIC 284 or General Electric in SIC 999) but still produce—and potentially recall—medical devices.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> As might be expected, the majority of [units] in our sample operate primarily in [primary_industry] ([SIC_code]). However, the sample was not limited to this industry because [units] may be formally classified in other industries ([example_codes]) but still [engage in phenomenon]. To ensure that the sample is not unduly influencing our results, we conducted an additional analysis that limited the sample to only [primary_industry] [units]. The results are consistent with our primary results.
**与原骨架差异**: 单行业研究的标准担忧是"样本是否受少数非核心行业企业驱动"。本骨架通过两步消除此担忧：(1) 先承认行业分类的模糊性——SIC code 不完全等于业务实质；(2) 报告限制样本的稳健性检验。两句话完成，不需要独立附录表。

### 变体 13: M7 随机效应选择三重辩护 — 理论+Hausman+ICC (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: We used panel regressions with random-effects estimations, because theoretically, we were more interested in the differential effects across CEOs rather than changes within CEOs. The Hausman test (p =.169) confirmed that using the random-effects (vs. fixed-effects) method was more appropriate.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used panel regressions with random-effects estimations, because theoretically, we were more interested in the differential effects across [unit] rather than changes within [unit]. The Hausman test (p = [value]) confirmed that using the random-effects (vs. fixed-effects) method was more appropriate. Also, [key_predictor] is likely to be an enduring [attribute_type] that remains stable over a short timeframe. We examined [its/their] internal consistency (ICC) using hierarchical linear modeling (HLM) to further test this premise. We used [predictor] as the outcome variable and treated [level_1_unit] as Level 1 and [level_2_unit] as Level 2 in the analyses. The ICC value ([value]) indicated that [predictor] tends to be stable within the individual but shows systematic variation across [level_2_unit]. We used robust standard errors to minimize heteroscedasticity and autocorrelation in our analyses ([citation]).
**与原骨架差异**: 本骨架与变体10（标准 Hausman→FE 选择）互补——当**理论指向 RE**时（关注跨单元差异>单元内变化），需要比单一 Hausman 更系统的辩护。Li et al. 提供了三层递进：(1) 理论理由——"more interested in differential effects across CEOs rather than changes within CEOs"；(2) Hausman 统计证据（p>.05 → RE 合适）；(3) ICC 辅助证据——用 HLM 估计关键预测变量的跨层变异比例，证明该变量确实在 Level 2 单元间存在系统性变异。注意：若理论关注单元内变化（如 within-firm dynamics），即使 Hausman 不显著也应使用 FE 并报告两者比较——本骨架仅适用于 theory→RE 的路径。
**诚实边界**: RE 选择的最低要求：(1) 理论理由（跨单元差异>单元内变化），(2) Hausman 检验结果，(3) 关键预测变量的 ICC 作为辅助证据。仅凭 "Hausman test was not significant (p > .05)" 不足以说服审稿人——需解释**为什么理论预期 RE 比 FE 更合适**。

### 变体 14: M6 全谱系控制变量 — 高 because 密度 + RavenPack事件控制 + CEO人格特质 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: We controlled for several variables to account for their unique influence on investors' reactions. The control variable data were derived from the previous quarter before the focal earnings call unless otherwise indicated.
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
**原始句锚点**: We chose the U.S. pharmaceutical industry as an appropriate setting for examining our hypotheses because it features both extensive alliance activities and competition for new products (Lichtenberg & Philipson, 2002; Mowery et al., 1996).
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M1
**骨架**:
> We chose [industry/setting] as an appropriate setting for examining our hypotheses because it features both [phenomenon A] and [phenomenon B] ([citation_1]; [citation_2]).
**与原骨架差异**: 单行业研究常用一句话完成情境正当化。关键：不罗列行业统计数字，而是点明两个与理论直接相关的现象在该情境中同时存在。Cui et al. 用 "extensive alliance activities" + "competition for new products" 同时激活 alliance 与 competition 两个理论前提。

### 变体 16: M2 多源 alliance 数据库合并与交叉验证 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: We constructed a more comprehensive alliance database by combining these three data sources. By relying on multiple sources, we minimized the possibility of double-counting alliances and of counting alliances that were announced but not realized.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M2
**骨架**:
> We first collected data on [alliances/relationships] within [industry] from [year_start] to [year_end], using [N] data sources—[source A], [source B], and [source C]—which (a) have very similar standards for reporting information, including [key fields], and (b) each normally reports only a fraction of all [activity] ([citation]). Although databases that track [activity] in [industry] are normally reliable ([citation]), we found that [source A] covers more [historical data], while [source B] and [source C] include more [recent information]. We constructed a more comprehensive [database] by combining these [N] data sources. For due diligence, we followed [citation], searching for [announcements/status reports] from [source D], [source E], and [source F]. Most [announcements] were cross-validated by at least two additional sources. By relying on multiple sources, we minimized the possibility of double-counting [alliances] and of counting [alliances] that were announced but not realized.
**与原骨架差异**: 在现有变体2（样本交集漏斗）基础上扩展为完整段落。关键要素：(1) 多数据库互补性说明；(2) 人工 due diligence（LexisNexis / 公司网站 / SEC filings）；(3) 交叉验证的两个明确目标：防重复计数、防 announced-but-not-realized。适用 alliance / network / contract 等多源合并场景。
**诚实边界**: 仍需报告关键中间匹配 N（如初始 alliance 条目、合并后条目、匹配 Compustat/FDA 后最终 dyad-year），否则仍落入"多数据库无漏斗"反模式。
**扩展（du_tsolmon2024 ORSC）**: 三层异质数据库漏斗 + 附录审计。本文示范了跨三层异质库（交易库→人员库→结构库）逐层交集的漏斗叙事：每层交集后报告 N（如 576K deals → 15,773 deals/43K managers → 2,941 deals/18,987 managers），主文只报层数与最终 N，**附录报告 match rate + 初始样本 vs 最终样本关键变量对比**（证明最终样本无系统偏差）。骨架补充："[After final merge], our estimation sample covers [N] [units]. Online Appendix [X] reports the match rates across all datasets used in constructing the estimation sample and the comparison of key variables between the initial sample ([N_initial]) and the final estimation sample ([N_final])." 适用：三层及以上异质数据库合并、需要兼顾主文简洁与可审计性的样本构建。

### 变体 17: M3 多维行为指标 → factor score → 平均值 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: We ran a factor analysis of these three items and found that all three loaded high (>0.73) on one latent factor, while the value of Cronbach's alpha is .81, which suggests that it is a reliable construct.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M3
**骨架**:
> [DV construct] describes both [dimension 1] and [dimension 2] of [actor]'s [behavior] ([citation]). This variable contains [N] items: [item 1], [item 2], and [item 3]. [Item 2] measures [definition]; [item 3] measures [definition]. [Item 3] is a more aggressive form of [behavior] than [item 2] because [theoretical rationale] ([citation]). We ran a factor analysis of these [N] items and found that all [N] loaded high (>[threshold]) on one latent factor, while the value of Cronbach's alpha is [value], which suggests that it is a reliable construct. We used the [average score] for these [N] items to measure the dependent variable.
**与原骨架差异**: 适用于多维行为 DV（如竞争攻击性 = 行动数量 + 宽度 + 深度）。关键：(1) 每个子维度的理论含义；(2) 子维度间的理论排序（如某维度更激进）；(3) factor loading + Cronbach's alpha；(4) 合成方式（平均值或 factor score）。与文本构念测量变体5（复合文本指标）互补——本骨架用于行为计数+定性深度组合。

### 变体 18: M7 dyad fixed effects + dyad 聚类标准误 + 具体混淆源举例 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: For example, if unobserved heterogeneities, such as the attractiveness of partners to one another and their tendencies to compete with each other, are constant within firm–partner dyads, then there might be an endogeneity concern. A fixed-effects estimator can rule out such a possibility by eliminating time-invariant heterogeneities.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We tested our hypotheses using fixed-effects models. The unit of analysis is [actor]-[partner]-[time], and we allowed a [N]-year lag between our predictor variables and the dependent variable. A fixed-effects estimator has superior controls for time-invariant variables ([citation]) and is an effective way to account for possible endogeneity problems. For example, if unobserved heterogeneities, such as [example 1] and [example 2], are constant within [dyad], then there might be an endogeneity concern. A fixed-effects estimator can rule out such a possibility by eliminating time-invariant heterogeneities. Fixed-effects models also allow us to account for intra-cluster correlations caused by multiple observations of the same [dyad] over time. We therefore employed [dyad] fixed-effects and clustered standard errors on [dyad] in our models.
**与原骨架差异**: 与变体7（嵌套横截面聚类 SE）互补。本骨架增加 dyad FE + 具体时不变混淆源举例（如 "attractiveness of partners to one another and their tendencies to compete"），让 FE 的识别价值从抽象变为可感知。关键：混淆源举例必须真实存在于研究情境中，而非泛泛而谈。
**诚实边界**: dyad FE 只能消除时不变遗漏变量；若存在时变混淆（如共同市场冲击），FE 无法识别因果。网络变量研究还需额外讨论反射性问题。

### 变体 19: M4 高管信心期权 moneyness 操作化 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: The average moneyness is defined as the ratio of average value per option to the average strike price. The constructs are measured with a lag relative to the measurement of the dependent variable to create temporal distance and maintain causal priority.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M4
**骨架**:
> We follow the finance and accounting literature and infer [actor] confidence from [actor]s' decisions about when to exercise company stock options ([citation]). The options-based measure uses archival data and is easily calculated from Execucomp, allowing us to examine executive confidence for a broad cross-section of firms over a long period ([citation]). [Actor] confidence is measured as the average moneyness of the exercisable options held by the [actor] in [year t]. The average moneyness is defined as the ratio of the average value per option to the average strike price ([citations]). The constructs are measured with a lag relative to the dependent variable to create temporal distance and maintain causal priority.
**与原骨架差异**: 高管信心的经典期权 moneyness 操作化。关键要素：(1) 理论直觉（自信高管延迟行使深度实值期权）；(2) 公式（average value/strike price of exercisable options）；(3) 滞后处理（避免薪酬同期受 DV 污染）。与 `micro-templates/executive-confidence-operationalization.md` 配套使用。
**诚实边界**: 必须说明该指标测量的是"基于财富的信念"而非心理学过度自信；必须报告滞后结构；样本中无 exercisable options 的高管需说明缺失值处理。

### 变体 20: M2.5 Model-Free Evidence 预览 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: We then calculate the mean and median MMM for the firms in each quartile. Consistent with H1, there is a monotonic increase in MMM from the first quartile where CEOs have the lowest level of confidence to the fourth quartile where CEOs are the most confident.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M2.5
**骨架**:
> Before presenting the model-based evidence, we provide model-free evidence on the relationship between [IV] and [DV]. We divide the sample into quartiles based on [IV] and calculate the mean and median [DV] for firms in each quartile. If [theory] holds, we should observe a monotonic [increase/decrease] in [DV] from the lowest to the highest [IV] quartile.
**与原骨架差异**: 在正式回归前用 quartile means/medians 展示无条件关系。关键：明确分位数基于 [IV]、报告 mean + median、说明预期模式（单调递增/递减）。适用于连续 IV 与连续 DV 的初步关系展示，增强读者对主效应方向的直观信心。
**诚实边界**: Model-free evidence 不能替代模型控制；必须在 Methods 中预告其探索性质，并在 Results 中明确与模型结果的对比。

### 变体 21: M7 三向交互模型设定 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: For ease of interpretation of the interaction coefficients, we follow the recommendations of prior literature (e.g., Irwin & McClelland, 2001) and mean-center CEO confidence, CMO confidence, Board independence, and CMO power before including them in the regressions.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We estimate the following model: [DV] = β₀ + β₁[IV] + β₂[IV]×[W1] + β₃[IV]×[W1]×[W2] + β₄[IV]×[W2] + β₅[W1]×[W2] + β₆[W1] + β₇[W2] + Controls + ε. For ease of interpretation of the interaction coefficients, we mean-center [IV], [W1], and [W2] before including them in the regressions ([citation]). We include all two-way interactions and the constituent terms to avoid omitted-variable bias in the three-way interaction coefficient ([citation]). We cluster the standard errors at the [firm] level to account for heteroskedasticity and within-[firm] correlation ([citation]).
**与原骨架差异**: 三向交互的标准 Methods 写法。关键要素：(1) 完整模型方程（含所有 lower-order terms）；(2) mean-centering 声明；(3) 聚类 SE 层级。适用于 X × W1 × W2 设计。
**诚实边界**: 必须包含所有 lower-order terms；mean-centering 不影响系数解释但影响常数项；若 W1/W2 偏态，±1 SD 切割需改用实际分位数。
**跨 skill 对齐**: `write-theory/corpus/variants/E_moderation.md` E6（序列嵌套调节理论推导）；`../write-results/econometric-models/三向交互.md` 变体2（连续调节变量三向交互边际效应表）。

### 变体 22: M7 GEE + AR(1) working correlation — 时不变焦点 IV 的估计量选择论证 (1篇高价值)
**来源论文**: Abdurakhmonov, Ingram & Ridge (2026, JOM)
**原始句锚点**: We follow prior CEO political ideology research by employing generalized estimating equations (GEE) with robust standard errors (Chin & Semadeni, 2017; Chin et al., 2013) because of this model's appropriateness when including time-invariant variables such as CEO liberalism (Chatterjee & Hambrick, 2007; Quigley & Hambrick, 2012).
**验证状态**: 通过（单篇入库，待第二篇交叉验证；GEE 在 corpus 中此前无独立变体）
**写入日期**: 2026-07-22
**槽位**: M7
**骨架**:
> Following prior [domain] research, we employ generalized estimating equations (GEE) with robust standard errors ([citations]) because of this model's appropriateness when including time-invariant variables such as [focal_time_invariant_IV] ([citations]). For all models, we specified an autoregressive (AR1) working correlation structure, with the [firm / unit] set as the panel unit, since it allows for the possibility that unobserved factors influencing [DV] may be correlated across adjacent [time periods] within the same [unit] ([citation]). To account for temporal and [industry / context]-specific effects, we included [year] and [industry] fixed effects in all analyses.
**与原骨架差异**: 与变体 10（Hausman FE vs RE）和变体 13（RE 三重辩护 theory+Hausman+ICC）互补而非重叠——两者基于 Hausman / ICC 选择 FE / RE；本变体基于 **焦点 IV 的时不变性** 选择 GEE。当核心 IV 是时不变稳定特质（CEO 政治意识形态、人格、创始人身份、性别、教育背景等）时，firm FE 会吸收或丢弃该变量使主效应无法识别。GEE 提供第三条路径：(1) AR(1) working correlation 建模序列相关；(2) robust SE 校正规范误；(3) year / industry FE（而非 firm FE）吸收时间 / 行业冲击而保留 focal IV。关键三要素：① 显式说明"因 focal IV 时不变，firm FE 不适用"；② working correlation structure 选择依据（AR1 = 时间相邻期相关；exchangeable = 同单元任意两期等相关）；③ FE 声明（year / industry 而非 firm——因 firm FE 再次吸收时不变 IV）。
**诚实边界**: 必须显式声明不使用 firm FE 的理由（"because [focal_IV] is time-invariant, firm FE would absorb it"），不能默默省略；working correlation structure 选择应说明依据，不能默认 AR1；GEE 是 population-average 估计器，与 RE（subject-specific）在系数解释上有重要区别，应说明是 marginal effect 而非 unit-specific effect；firm FE 不可用时应在 M8 / Limitations 诚实说明残余威胁（time-varying unobservables 仍可能混淆），并通过 IV / Heckman / matching 补强。
**适用**: 焦点预测变量为时不变稳定特质（政治意识形态、人格、性别、出生地、教育背景、创始人身份）的 panel 研究；任何 firm FE 会"杀死"主效应的情境。
**跨 skill 对齐**: `../write-results/econometric-models/OLS-FE.md`（稳健性中可用 LPM + firm FE 作方向性对照，但主模型用 GEE 保留时不变 IV）。

### 变体 23: M1 行业统计 + 先例对齐的设置辩护 (1篇高价值)
**来源论文**: Pupovac, Astvansh, Carrillat & Legoux 2026 (POM)
**原始句锚点**: Measuring recalls' contagion from a manufacturer-customer to a supplier requires an empirical setting in which manufacturers and suppliers are interdependent in the product market (Cho et al., 2021). The automotive industry meets this requirement because suppliers produce 70% of an automobile, on average (McGee, 2017), suggesting high interdependence.
**验证状态**: 通过（单篇高价值，待第二篇交叉验证）
**写入日期**: 2026-07-21
**槽位**: M1
**骨架**:
> Measuring [theoretical relationship] requires an empirical setting in which [actor_A] and [actor_B] are interdependent in [domain] ([citation]). [Industry] meets this requirement because [industry statistic], suggesting high interdependence.
>
> [Actor_B]'s [stakeholders] may expect [event] to be frequent events ([citation]). Consequently, a [small event] will elicit little or no reaction from [stakeholders]. Indeed, many [industry] studies sample "[large]" [events] (e.g., [citation_1]; [citation_2]). Consistent with these precedents, we sample [large events], defined as [threshold]. These [events] are large enough to attract [stakeholders]' attention and frequent enough to create [theoretical condition].
**与原骨架差异**: 与 Desai 变体9 的"制度断点辩护"和 Cui 变体15 的"双重现象辩护"互补。本变体适用于**单行业事件研究**：(1) 用行业统计数字证明行为者间相互依赖；(2) 用"大事件"抽样标准平衡信号强度与样本量；(3) 明确对齐先例研究。关键：抽样阈值必须理论上合理（既能引发市场反应，又不过于罕见）。
**诚实边界**: "大事件"标准可能导致选择偏差——大事件对应的公司/关系可能系统性地不同于小事件。需在M8报告放宽/收紧阈值的稳健性。

### 变体 24: M4 法律强制披露阈值 → 自愿披露操作化 (1篇高价值)
**来源论文**: Pupovac, Astvansh, Carrillat & Legoux 2026 (POM)
**原始句锚点**: U.S. law requires a publicly traded supplier to disclose in its annual report (i.e., the Form 10-K the firm files with the SEC) the sales revenue it received from each "major" customer—that is, a customer from whom the supplier received at least 10% of its total sales revenue in the focal year.
**验证状态**: 通过（单篇高价值，待第二篇交叉验证）
**写入日期**: 2026-07-21
**槽位**: M4
**骨架**:
> [Country] law requires a publicly traded [actor] to disclose in [report] the [information type A] it received from each "[major]" [counterparty]—that is, a [counterparty] from whom the [actor] received at least [threshold]% of its total [revenue/metric] in the focal year. The law implies that [actor] has discretion in reporting [information type B] from "[minor]" [counterparties]—[counterparties] from whom it received [below threshold]% ([citation]). [Accounting standard body] states that the [actor] "need not disclose" [information type A] either ([source]). The inconsistency between the law and [accounting standard body] has perhaps prevented [regulator] from enforcing the law ([citation]).
>
> We leverage this voluntariness to construct [variable], coded 1 if [actor] disclosed [information] in [period t-1], and 0 otherwise. Assuming [event] in year [t], we set [variable] based on [actor]'s disclosure in year [t-1].
**与原骨架差异**: 将**法律-会计准则张力**转化为构念操作化的核心论证。关键：(1) 强制披露阈值定义"major" vs "minor"；(2) 会计准则的"自愿"声明创造实证上的变异空间；(3) 用滞后一期披露避免同期内生性。适用于任何依赖强制/自愿披露边界的研究（客户披露、ESG披露、Segment报告等）。
**诚实边界**: 必须验证 [regulator] 确实不强制执法；若样本中多数公司都披露，"自愿"变异的解释力会下降。滞后一期处理假设披露决策在 [event] 前已确定，否则需用CF/IV进一步处理内生性。

### 变体 25: M3 DV 文献基准锚定 — 均值与前人文献对比 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: The mean TMT retention rate in our sample is 54.8%, which is comparable to the mean retention rates found in the two empirical studies on postacquisition turnover: 55% in Hambrick and Cannella (1993), who examined 109 acquisitions from 1980 to 1984, and 59.4% in Krug and Hegarty (1997), who examined 207 acquisitions of U.S. firms by domestic and foreign acquirers from 1986 to 1988.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-25
**槽位**: M3
**骨架**:
> Our [first] dependent variable is [DV]. Following prior work, we measure [DV] as [operationalization] ([citation]). For example, if [concrete numerical example], the [unit] would have a [DV] of [value]. The mean [DV] in our sample is [X]%, which is comparable to the mean [DV] found in [N] prior empirical studies on [phenomenon]: [Y]% in [Author] ([year]), who examined [sample 1], and [Z]% in [Author] ([year]), who examined [sample 2].
**与原骨架差异**: 面板数据-OLS 现有变体无 DV 外部效度锚定。本变体三要素：(1) **具体数值示例**（5→3=0.60）让操作化可想象；(2) 报告样本均值；(3) **与 2+ 篇前人文献的均值对比**建立 DV 跨样本可比性——把"我的测量"锚定到"领域基准"。一句话完成外部效度论证，比单独报告均值更有说服力。适用于新构建的比率/计数 DV（retention rate、turnover、disclosure rate、adoption rate 等）。
**诚实边界**: 前人研究样本/时代/情境不同需说明（若本文是全球样本而前人是美国样本，需交代可比性边界）；均值可比不代表分布可比，若分布形状关键需补充。

### 变体 26: M2 跨库手工匹配（无共同标识符）+ 多源漏斗 (1篇高价值)
**来源论文**: Malshe & Agarwal (2015, Journal of Marketing)
**原始句锚点**: We obtained firms' financial information on balance sheets, income statements, and cash flow statements from S&P's Compustat database. Because there is no common firm-level identifier between the ACSI and Compustat, we manually matched ACSI brands belonging to corresponding Compustat firms.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-30
**槽位**: M2
**骨架**:
> "We assembled a data set using multiple sources, including [source 1], [source 2], [source 3], [source 4], and [source 5]. [Table] provides a description of these variables and the source of the specific data items. We obtained [financial data] from [database A]. Because there is no common [firm-level] identifier between [database A] and [database B], we **manually matched** [database B units] belonging to corresponding [database A entities]. Because one of our research questions pertains to [shareholder value], we retained only those [firms] that are [publicly listed] at any time during our sample period. We obtained [market data] from [database C]. Finally, we obtained [ownership data] from [database D] and derived [other ownership] from [database E]. After we merged the [N] data sets and removed [M] [firm-year] observations pertaining to [excluded segment, e.g., financial firms], our final sample consisted of [N_final] [firm-year] observations spanning a [Y]-year period ([year_start]–[year_end]) for which all the relevant variables have nonmissing values."
**与原骨架差异**: 区别于变体16（多源 alliance **自动**交叉验证）与变体2（逐步样本交集漏斗）——本变体处理两个核心数据库**无共同标识符**的硬情况（如 ACSI 品牌与 Compustat 企业无公用 firm ID），须**手工匹配**（manually matched）下游单位到上游实体。三要素：(1) 五库多源 + 每变量的数据源声明表；(2) **手工匹配的明示**（不可假装自动 merge）；(3) 合并后漏斗（合并 N 库 → 排除 M 个 [金融行业] 观测 → 最终 N_final，且限定"上市"以配合股东价值 RQ）。配套反模式（见"多数据库无漏斗"）：即便无法逐步漏斗，也须报告关键交集 N。适用于营销-金融、营销-会计等跨职能多源面板（ACSI/Compustat/CRSP/ExecuComp/Thomson Reuters 组合）。
**诚实边界**: 手工匹配的匹配率与匹配规则须报告（多少 brand 成功匹配到 firm？规则是否可复现？）；限定"上市"会引入生存偏误（上市公司更大更老），须在 limitation 讨论。

### 变体 27: M4 构念形成窗—结果观察窗分离 + 双代理收敛 (1篇高价值)
**来源论文**: Schumacher, Keck & Tang (2020, Strategic Management Journal)
**原始句锚点**: We employ two separate measures of overconfidence derived from the prior literature to test our hypotheses. This helps us to ensure that our findings are not driven by the idiosyncrasies of any specific measure of CEO overconfidence and to overcome some of the limitations that each individual measure might have.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-08-03
**槽位**: M2 / M4 / M8
**骨架**:
> To reduce contamination between [stable actor trait] and the outcomes used to test its consequences, we use nonoverlapping windows. We construct the trait from observable behavior during the first [k] periods of each actor's tenure and estimate its relationship with outcomes only in subsequent periods. We operationalize the trait with two proxies grounded in different data-generating processes: [public-description/text proxy] and [revealed-choice/portfolio proxy]. Convergent directional results reduce dependence on any one proxy, while each proxy's distinct contamination channel is examined separately.

**与原骨架差异**: 变体19采用同期/滞后期权 moneyness；本变体把**完整构念形成期**与**完整结果观察期**切开，并将媒体描述与期权行为两种方法异质的痕迹并行使用。它同时完成时间优先性与测量三角化，但不应被写成外生性识别。

**适用**: 相对稳定的 CEO/TMT 特质；trait proxy 可能被同期企业结果反向污染；拥有两类以上独立痕迹数据。

**诚实边界**: 非重叠时间窗仍不能排除早期企业环境的共同影响；双代理同向不证明代理纯度。必须逐一说明媒体、投资组合、文本或行为代理的替代解释。若 trait 在形成窗之后可能变化，需报告稳定性或短窗敏感性分析。

**配套微模板**: `micro-templates/executive-confidence-operationalization.md` 选项4–5。

### 变体 28: M7 Binary-panel GEE + 全零单元保留 + 正式曲线识别链 (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: Second, many of our observations are zero for all years for one firm. We need to include these observations in our regression as they contain relevant venturing information.
**验证状态**: 通过（单篇高价值；与变体22共同验证 GEE 的可迁移性，但选择理由不同）
**写入日期**: 2026-08-04
**槽位**: M5 / M7 / M8
**骨架**:
> We estimate a generalized estimating equation (GEE) model for three design-specific reasons. First, repeated observations within [unit] may be correlated. Second, many units record zero outcomes in every period; these units still contain theoretically relevant variation in [IV], whereas a fixed-effects binary model would remove them. Third, robust GEE inference accommodates heteroskedasticity and misspecification of the working covariance. Because [DV] is binary, we specify a binomial family with a logit link, a [exchangeable / AR(1)] working correlation justified by [within-unit dependence assumption], and robust standard errors. We include [year] and [industry/context] fixed effects.
>
> A significant quadratic coefficient alone does not establish the hypothesized [U/inverted-U]. We therefore require the squared term to have the predicted sign, the slope at the lower bound to be significantly [positive/negative], the slope at the upper bound to be significantly opposite, and the turning point with its [Fieller/bootstrap] confidence interval to fall within the observed support of [IV].

**与变体22的差异**: 变体22因焦点 IV 时不变、firm FE 会吸收主效应而选择 GEE，并使用 AR(1)。本变体的首要理由是**保留结果始终为零但 X 仍有信息的面板单元**，同时处理单元内相关和异方差；working correlation 为 exchangeable。新增的第二段把曲线理论翻译为四个事前统计约束，阻止“负二次项=倒 U”的不充分检验。

**适用**: 二元面板结果中存在大量 all-zero units，且理论关注 population-average 关系；假设包含 U/倒 U及其调节。

**诚实边界**:
- GEE 保留全零单元但不吸收所有 unit-level time-invariant confounds；不得写成 firm FE 的因果等价物。
- exchangeable 与 AR(1) 必须依据相关结构选择，不能为了软件方便默认。
- Fieller 区间或 turning point 落入样本范围只确认函数形态，不确认理论机制。
- 若极端 X 区间样本稀疏，应报告支持范围、观测密度并进行敏感性分析。

**跨 skill 对齐**: `../write-results/econometric-models/Logit-Probit-Ordered-Probit.md` 变体9–11（正式 U-test、条件曲线概率图与经济成本换算）；`../write-theory/corpus/subprotocols/hypothesis_derivation_patterns.md`（two-phase curvilinear argumentation）。

### 变体 29: M4 召回严重度理论分类 — 后果类型二元操作化 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: To measure the effects of the severity of product recall, we classify two severity types based on the consequence of product failure described in the data. Severity type 1 product recalls, which increase the chance of crash or fire, involves an immediate safety concern.

**验证状态**: EMERGING（单篇；与 Kashmiri 2017 severity 边界声明互补）

**槽位**: M4

**骨架**:
> To measure the severity of [product-harm event], we classify events into two types based on the consequence of product failure described in [regulatory/administrative data]. [Severity type 1] events [increase immediate catastrophic risk — e.g., crash or fire] and reflect an immediate safety concern; an example is [defective brake pedal]. [Severity type 2] events [increase injury risk conditional on an exogenous accident — e.g., airbag/seatbelt failure when crash is not caused by the defect] and therefore may trigger less negative consumer response than type 1. [Severity_it] equals one for type 1 and zero for type 2. In our sample, [percentage]% of events are type 1 and [percentage]% are type 2.

**与原骨架差异**: 召回家族现有 time-to-recall、裁量权子样本（Hoffmann）与 regulatory indicator（Kashmiri）；本变体把 **NHTSA 后果描述 → 心理学归因可辩护的二元 severity** 写进 M4，并给每类一个可想象例子 + 样本占比。

**诚实边界**: 二元分类损失 severity 连续信息；须在稳健性报告 alternative coding 或 include continuous units recalled。

---

### 变体 30: M4 媒体覆盖 — 双索引相关度阈值 + 互补数据源 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: LexisNexis assigns a relevancy score for each index (e.g., product recall) of each article. We use this score to ensure the articles do indeed discuss the recall events of the firm of interest and that they are not incidental mentions.

**验证状态**: EMERGING（单篇；待与 `文本构念测量` 交叉验证）

**槽位**: M4

**骨架**:
> We obtain print media reports about [events] from [LexisNexis/Factiva]. We search [all major outlets / firm name within study window] using two index terms: ["product recall" as subject] and [firm name as company tag]. [Provider] assigns a relevancy score for each index in each article; we retain articles only if relevancy scores for both indices are at least [threshold: e.g., 60%], ensuring discussion concerns the focal firm's [events] rather than incidental mentions. We complement [provider A] with [provider B: e.g., Wall Street Journal via Factiva company/subject tags] using parallel exclusion rules for irrelevant articles. [Media_ijt] is the count of qualifying articles in [period t] for [unit ij].

**与原骨架差异**: 区别于 generic media count——本变体强制 **双索引 relevancy 阈值** 作为 face-validity 链，并写 **双数据源互补** 与 irrelevant-mention 排除逻辑。召回 shock 研究可复用。

**诚实边界**: 阈值（60%）为 judgment call，须报告敏感性；print-only 遗漏 social/streaming 渠道。

---

### 变体 31: M2/M4 异频数据时间对齐 — 事件聚合至结果频率 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: To fully utilize the monthly sales and advertising data, we aggregate the product recall data for each month and each car nameplate. Although all car characteristics and price data are annual, the advertising expenditures and product recall data are monthly.

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M2 / M4

**骨架**:
> [Sales/advertising/outcome data] are observed at [monthly] frequency, whereas [event registry data] are recorded at [event/day level] and [product characteristics/prices] are [annual]. To utilize the high-frequency marketing and outcome data, we aggregate [event counts/intensity] to [monthly unit-level totals] (e.g., total units recalled per month per [nameplate]). Annual [characteristic/price] variables are held constant within year but enter the [monthly] demand system with [CPI deflation / interpolation rule stated explicitly].

**与原骨架差异**: 面板 OLS 变体2/26 强调多库交集 N；本变体解决 **event-day vs month vs year 三频对齐**——Marketing/IO 面板常见但未在召回语料显式化。

**诚实边界**: 月内事件堆叠假设事件效应在月内可加；年度价格仅 CPI 月变会低估 within-year price variation——须 limitation 承认 MSRP 代理限制。

### 变体 32: M4 结构二元特征操作化为「kind」而非「degree」— 相对 majority-independence 的 discrete construct (EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: Our independent variable is whether the focal board of directors was a lone-insider board. To capture the most conservative specification, we coded firms as "1" if the CEO was the only inside or affiliated member on the board; other board structures were coded as "0."
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-05
**槽位**: M4
**骨架**:
> Our independent variable is whether the focal [unit] adopted [extreme categorical structure: e.g., a lone-insider board]. To capture the most conservative specification, we code [units] as 1 if [threshold that removes an entire historically represented group—e.g., the CEO is the only inside or affiliated director], and 0 otherwise. [Units] may move into and out of [the structure] over the panel. We theorize that [this structure] is categorically different from simply increasing [continuous alternative: e.g., the proportion of independent directors]: removing [the last non-CEO insider] is a change in kind rather than degree because it eliminates [information / contestation / succession] benefits that majority-[independence] alone does not remove. We therefore do not treat [continuous independence / insider count] as interchangeable with our indicator. Below (and in robustness), we verify that effects are not reducible to a linear [insider-count / independence] gradient—including tests that replace the indicator with [adjacent category: e.g., dual-insider], examine continuous [independence] among non-[focal-structure] units, and compare the [1→2] jump with later increments.

**与原骨架差异**: 现有 M4 变体多为连续构念、阈值披露或双代理收敛；本变体专门处理**治理/组织「极端结构」二元化**时必须完成的构念辩护：(1) 保守编码规则；(2) 理论声明 kind ≠ degree（相对 majority-independence / 连续计数）；(3) Methods 即预告 kind-vs-degree 稳健性电池。诚实边界：若经验分布上「2+」类别极少，二分损失的信息有限——须报告类别频数；不能仅靠理论断言，Results 必须出现 dual-category / continuous / Chow 类检验（见 write-results IV-2SLS 变体 10）；若理论其实是线性 dose-response，不应使用本骨架。

**适用**: 董事会 lone-insider、完全独立委员会、单一大股东、零内部人等高阶离散结构相对「比例/计数」连续操作化的研究。

**跨 skill 对齐**: IV 内生采纳见 `IV-2SLS.md` 变体 12；Results kind-vs-degree 电池见 write-results `IV-2SLS.md` 变体 10。

---

### 变体 33: M1 单一中介机构设置辩护 — a/b/c 三理由 + 单一机构一致性 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: We used ratings by MSCI ESG Research as our empirical context because MSCI: (a) is a publicly traded firm, which allowed us to obtain information on its institutional investors' holdings; (b) is the largest and arguably most influential ESG rating provider in the world; and (c) provides the most extensive coverage. Using a single rating agency also mitigates issues arising from divergence in the methodologies across different rating agencies.
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M1
**骨架**:
> We used [intermediary] as our empirical context because [intermediary]: (a) [data-accessibility property — e.g., is publicly traded, allowing us to obtain ownership/holdings data]; (b) is the [superlative position — largest / most influential] provider in the world ([citations]); and (c) provides the most extensive coverage. Using a single [intermediary] also mitigates issues arising from divergence in the methodologies across different [intermediaries] ([citations]).

**与原骨架差异**: 现有 M1 变体为单行业设置（变体15 双重现象、变体23 行业统计+先例）——本变体是**单一中介机构选择辩护**（评级机构/平台/审核方作为研究情境）：a/b/c 三理由各自对应数据可得性、影响力、覆盖度，末句用单一机构一致性论证回应"为什么只研究一家"的质疑（方法差异被单机构设计消解）。适用于以某个具体中介/平台/机构为情境的研究（评级机构、平台市场、审核机构）。
**诚实边界**: a/b/c 必须真实对应数据需求；"single [intermediary] mitigates divergence" 只有在理论机制与中介机构内部运作相关时才成立；若多个机构可用且方法差异是关键变异来源，本骨架不适用。

**适用**: 评级机构（ESG/信用）、平台（App Store/Amazon）、审核/认证机构、媒体机构作为研究情境的论文。

---

### 变体 34: M2 多源清单 + 覆盖边界定样本窗 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: We collected remaining data from multiple sources, including institutional ownership data from Thomson Reuters Institutional (13F) Holdings; geographic operations data from 10-K filings (via EDGAR); firm financial data from Compustat; ... Since coverage of the MSCI ESG Ratings Time Series database is not comprehensive before 2013, our sample period ranges from 2013 to 2019, where 2019 is the final year for which all data sources were available. The sample includes 2,787 unique firms with 12,634 firm-year observations.
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M2
**骨架**:
> We collected data from multiple sources, including [source 1: data type from database]; [source 2: data type from database]; ... and [source N: data type from database]. Since coverage of the [main database] is not comprehensive before [year_start], our sample period ranges from [year_start] to [year_end], where [year_end] is the final year for which all data sources were available. The sample includes [N] unique [units] with [N] [unit-year] observations.

**与原骨架差异**: 区别于变体 9（制度事件定起始）——本变体是**数据覆盖边界定样本窗**：起点=主数据库覆盖不足的年份、终点=全部数据源可得的最后一年；多源清单以"data type from database"格式枚举后直接报告交集最终 N（与变体 2 的逐层漏斗互补——多库枚举后直接交集，不强制每库 N）。适用于依赖多个专有数据库交集的面板研究。
**诚实边界**: 若可构建逐层漏斗（变体 2）应优先使用；数据覆盖边界需说明"not comprehensive"的判断依据（如数据库官方说明）；最终 N 前可补一句中间交集说明（"of the [N] firms in [primary], [N] could be matched"）增强可审计性。

**适用**: 多数据库交集面板（13F/Compustat/专有库混合）、数据库覆盖有时间边界的研究。

---

### 变体 35: M3 离散化等级 DV 的边界距离操作化 + 边际影响预检验 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: Because the variable is initially continuous, the central limit theorem applies, which implies that if MSCI had not preset the letter rating for each firm, the distribution of industry-adjusted scores would likely fall close to a normal distribution... the scores (before being categorized into letters) cluster heavily at the boundaries of each letter rating's interval... We find that the correlation between rival–MSCI CIO and distance from upper boundary is negative and statistically significant (r = -0.080, p < .001), which suggests that firms with industry-adjusted scores closer to the upper boundaries have higher levels of rival common ownership with MSCI, as our theory would predict.
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M3
**骨架**:
> [DV] is measured on a [N]-point [letter/number] scale ([source]). [Optional: distributional logic — because the underlying variable is initially continuous, the central limit theorem implies an approximately normal distribution, yet scores cluster heavily at the boundaries of each interval, deviating from normality.] Although our theory implies that [predictor] may influence [DV], we do not anticipate that [influence] carries such weight that it drastically [moves a unit multiple categories]. Instead, we expect the influence to happen on the margins. To examine this prediction, we construct a new variable, [distance from upper boundary], which equals [formula per interval]. To illustrate the importance of these boundaries, consider a [unit] with a [score] of [value]: this [unit] would have a distance from upper boundary of [value], meaning its [score] would be just below the level needed to receive the next higher [rating] ([threshold]). We find that the correlation between [predictor] and [distance] is [sign] and statistically significant ([r], p < [threshold]), which suggests that [units] with [scores] closer to the upper boundaries have higher levels of [predictor], as our theory would predict.

**与原骨架差异**: 现有 M3 变体（factor score、文献基准锚定）——本变体是**离散化等级 DV 的边界距离操作化**：①分布逻辑（连续底层 → 边界聚集偏离正态）②"influence happens on the margins" 预期声明（不跃级，只推边际）③边界距离变量分区间公式 ④图→变量→相关性三段预检验（Figure → 变量构造 → 相关系数）。适用于 letter-grade/分档型 DV（评级、星级、等级），理论预期影响发生在类别边界而非跨类别。
**诚实边界**: 边界距离变量须与主 DV 在同一尺度（区间内线性距离）；相关性预检验是描述性证据，不可替代主回归；"influence on the margins" 的理论依据须在 Theory 明确。

**适用**: ESG/信用评级、星级评价、字母分档等离散化等级 DV 的研究。

---

### 变体 36: M4 复合测量构念分步构建 + 阈值辩护 + 可行性论证 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: After obtaining institutional ownership data from Thomson Reuters Institutional (13F) Holdings, we retained investors that owned more than 1% of outstanding shares in each firm (i.e., at least 1% in MSCI and 1% in another firm) because such investors have been shown to have sufficient incentives and power to actively intervene in corporate decision-making (Connelly et al., 2019; Gilje, Gormley & Levit, 2020). The average number of investors with at least 1% ownership in MSCI each year is 20, making it feasible for MSCI executives to be aware of each large investor.
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M4
**骨架**:
> Our independent variable, [composite IV], captures [construct definition]. After obtaining [ownership data] from [source], we retained [actors] that owned more than [threshold]% of outstanding shares in each firm because such investors have been shown to have sufficient incentives and power to actively [intervene] ([citations]). [Feasibility argument: the average number of [actors] above the threshold is [N], making it feasible for [target actors] to be aware of each large [actor]]. We used the following formula to calculate [composite IV]: [formula]. For each [unit]'s [rival] pairs, we first calculated [step 1: within-actor aggregation], then computed [step 2: product across the two sides], and then calculated [step 3: aggregation across rivals].

**与原骨架差异**: 现有 M4 变体（三层 because、moneyness、阈值披露）——本变体是**复合乘积构念的分步构建**：①阈值辩护（1% → 激励权力 + 引用）②可行性论证（平均 N 家 → 高管可知晓每家）③分步计算（先内部聚合 → 再跨侧乘积 → 再跨对手平均）。适用于两个持有侧乘积/交集型复合构念（共同所有权、重叠关系、跨市场关联）。
**诚实边界**: 阈值选择须有文献依据；可行性论证（"average N makes it feasible for executives to be aware"）须与机制一致——若理论不依赖知晓，可行性论证是加分项而非必需；分步公式须与 Results 变量定义完全一致。

**适用**: common ownership、共同持股、双角色重叠、跨侧乘积构念的研究。

---

### 变体 37: M6 rival 镜像控制变量惯例 — 引用前例 + 命名规则 + 聚合方式 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: To address cross-rival effects on ESG ratings, we followed Guo, Sengul, and Yu (2020) to control for rival characteristics, denoted by the word "rival" (e.g., rival firm slack). Each variable is measured as the average value among all rivals identified by the FIC-100.
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M6
**骨架**:
> To address cross-[rival] effects on [DV], we followed [citation] to control for [rival] characteristics, denoted by the word "[rival]" (e.g., [rival] [variable]). Each variable is measured as the average value among all rivals identified by [classification source].

**与原骨架差异**: 现有 M6 变体（分层 because、全谱系+事件控制）——本变体是**对手侧镜像控制惯例**：引用既有惯例（如 Guo, Sengul & Yu 2020）+ 命名规则（"rival" 前缀标记）+ 聚合方式（对手平均值）——一句完成跨主体效应控制。适用于 focal unit 与其 rivals/peers 竞争互动的面板（对手特征可能同时影响 DV 与 IV 的关联）。
**诚实边界**: 引用惯例必须真实存在且适用；命名规则须贯穿 Methods/Results/Table（"rival" 前缀一致）；若对手定义随分类变动（FIC-100 vs 替代分类），须与 M4 对手识别一致。

**适用**: 竞争动态、同伴效应、对手特征控制的面板研究。

---

### 变体 38: M7 理论-估计量对齐 + 不滞后辩护（Bellemare 反向论证）(1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: Since our theory focuses on between-firm effects, we used pooled OLS models with industry-year fixed effects, where industries are defined by the FIC-100 (Hoberg & Phillips, 2010, 2016). In each industry-year, the median (mean) value of the number of rivals with MSCI ESG ratings is 14 (24), and the minimum (maximum) value is 2 (189), making it feasible to make cross-sectional comparisons. ... Since investors most likely exert their influence on firms and ESG rating agencies during their current holding periods, we did not lag the explanatory variables, as doing so could cause incorrect inferences (Bellemare, Masaki & Pepinsky, 2017).
**验证状态**: 通过（单篇 EMERGING；待第二篇交叉验证）
**写入日期**: 2026-08-09
**槽位**: M7
**骨架**:
> Since our theory focuses on between-[unit] effects, we used pooled OLS models with [industry]-year fixed effects, where industries are defined by [classification] ([citations]). [Feasibility of cross-sectional comparison: in each industry-year, the median (mean) number of [comparison units] is [N] ([range]), making it feasible to make cross-sectional comparisons.] We clustered standard errors at the [industry-year] level to address potential correlations of residuals within each [cluster] ([citation]). To alleviate potential influence of outliers, we winsorized all continuous control variables at the [1st and 99th] percentiles, but the results are similar without winsorizing. Since [actors] most likely exert their influence during their current [holding] periods, we did not lag the explanatory variables, as doing so could cause incorrect inferences ([citation]).

**与原骨架差异**: 现有 M7 变体（Hausman、GEE、dyad FE）——本变体是**between-firm 理论 → pooled OLS 显式对齐** + **Bellemare 不滞后辩护**：五要素——①理论-估计量对齐（between-unit 理论 → pooled OLS，不用 firm FE 作主模型）②行业-年聚类 + 可比单元数可行性（median/mean + range）③winsorize + "results similar without" ④不滞后辩护（当前持有期影响 → 滞后导致错误推断，Bellemare et al. 2017）⑤交互中心化（表注预告）。适用于 between-unit 变异为主的理论（构念在单元间差异而非单元内变化）。
**诚实边界**: 不滞后必须引用 Bellemare et al. (2017) 且论证机制发生在当前期；若领域惯例是滞后，需显式说明偏离理由；firm FE 版本（稳健性）须在 Results 报告并解释效应缩小。

**适用**: between-unit 理论（共同所有权、行业竞争结构、评级偏差）、当前期影响机制的面板研究。

---

### 变体 39: M2.5 时间间隔声明 — DV t+1 / IV & controls t 的反向因果预先化解（2026-08-12）

**来源论文**: Ridge, Hill, Ingram, Kolomeitsev & Worrell 2024 (*Academy of Management Journal*)
**原始句锚点**: "All the dependent variables are measured in year t + 1, while all independent and control variables are measured in year t to establish temporal spacing."（英文原句——源论文为英文，非中文锚点）
**验证状态**: EMERGING（单篇；`section_variant`）
**写入日期**: 2026-08-12
**槽位**: M2.5
**骨架**:
> All the dependent variables are measured in year [t + 1], while all independent and control variables are measured in year [t] to establish temporal spacing.
**与原骨架差异**: 区别变体 20（Model-Free Evidence 预览）与变体 27（构念形成窗—结果观察窗分离）——本变体是**单句时间间隔声明**（DV t+1 / IV t），把反向因果威胁在 Methods 层面预先化解，是 CEO 特质→结果类纵贯面板的高性价比 baseline 承诺。更通用：任何 lead-DV / lag-IV 面板都可复用。
**诚实边界**: 时间间隔只缓解反向因果，不解决遗漏变量/选择偏差；若机制实际发生在同期（如投资者当期反应），须按 Bellemare 反向论证（见变体 38）说明为何不滞后。

### 变体 40: M6 控制变量"双面 because" — 对 DV 一条理由 + 对 IV 共变一条理由（2026-08-12）

**来源论文**: Ridge, Hill, Ingram, Kolomeitsev & Worrell 2024 (*Academy of Management Journal*)
**原始句锚点**: "We control for firm size (logarithm of total assets), market performance (measured as Tobin's Q), and tax aggressiveness... because lobbying and competitive actions may be affected by all three. Likewise, there is reason to expect that each may covary with paranoia, given tendencies of those higher in the trait to avoid attention."（英文原句——源论文为英文，非中文锚点）
**验证状态**: EMERGING（单篇；`section_variant`）
**写入日期**: 2026-08-12
**槽位**: M6
**骨架**:
> We include several control variables that may covary with the focal outcomes and [IV]. We control for [control 1], [control 2], and [control 3] because [DV] may be affected by all three ([citation]). Likewise, there is reason to expect that each may covary with [IV], given [mechanism linking controls to the trait]. From a [stakeholder/governance] perspective, we control for [control 4] and [control 5] given that these variables are potential outcomes of [focal behavior] ([citation]). Finally, at the [actor] level, we include [actor-level controls] because [reason].
**与原骨架差异**: 区别变体 14（Li et al. 2026 高 because 密度——强调每个控制的 DV 面理由）——本变体是**"双面结构"**：每个控制对 DV 一条理由（"may be affected by all three"）+ 对 IV 共变一条理由（"each may covary with [IV], given tendencies of those higher in the trait to [behavior]"），形成平行论证。CEO 特质研究最常被质疑"控制为何与特质共变"，双面 because 预先回答此质疑。
**诚实边界**: 对 IV 的共变理由必须指向真实机制（如"高特质者倾向回避关注"），不能泛泛而谈；若某控制对 IV 的共变理由无法给出，应质疑是否真的需要控制它。

---

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **多数据库无漏斗** | 多数据库合并（Compustat + Execucomp + CRSP + ...）后仅报告最终 N，未说明各数据库交集前后的 N 损失 | 如无法构建完整逐层漏斗（因多源合并非逐步筛选），至少报告："Of the [N_initial] firm-quarters in [primary_source], [N_matched] could be matched to [secondary_source], yielding [N_intersection]." |
| **多源合并后中间 N 缺失** | 合并多个数据库后仅报告最终 N，未报告 alliance/relationship 条目、样本匹配前后损失 | 报告关键中间匹配 N，如 "Of the [N_initial] [alliances] from [source A], [N_matched] could be matched to [source B], yielding [N_final] [dyad-years]." |
| **事件-企业多源匹配无每步N审计** | 事件研究+横截面设计中，识别事件、识别行为者总体、按关系匹配后仅报告最终 dyad 数，未报告每步的 N 损失 | 在M2中显式报告：(1) 初始事件数，(2) 行为者总体数，(3) 匹配后 dyad 数，(4) 各回归子样本数；若无法获得精确起始N，说明原因并讨论选择偏误风险。 |
| **控制变量全部外包至附录** | 控制变量列表和理由完全放在附录表/注中，主文 Methods 段缺少 because 逻辑 | 主文M6至少对每层控制变量提供总起句和代表性 because 论证，并将完整列表和详细理由放在附录。 |
| **调节效应论文 Methods 未报告交互项构造** | 论文核心贡献是调节效应，但 Methods 未说明交互项、去心化或二次项 | 在 M5/M7 明确说明交互项形式、是否 mean-centered、是否包含二次项及其构造方式 |
| **仅凭 Hausman 选择 RE** | 仅报告 "Hausman test not significant (p > .05), so we use RE"，无理论理由 | 参见变体13——RE 选择需理论理由（跨单元差异>单元内变化）+ Hausman + ICC 三重辩护 |
| **控制变量无 because** | 罗列变量名和操作化但不解释"为什么控制这个变量" | 每个控制变量必须回答：(1) 为什么影响 DV，(2) 为什么可能与 IV 相关 |
| **理论检验型面板缺设置合法性论证（M1 反模式）** | S&P 1500 等样本框仅作为样本呈现，未论证为何该情境适合检验理论前提 | M1 至少一句情境正当化：指出该情境中理论相关的两个前提现象并存（见变体 15 双重现象、变体 23 行业统计、变体 33 单一中介机构） |
| **行业/年度 dummy 替代 firm FE 未辩护 + 未声明聚类 SE 层级（M7 反模式）** | 面板用行业/年度 dummy 而非 firm FE，却不解释取舍；未说明标准误聚类层级 | 明示为何不取 firm FE（如 Tobit/NB 收敛、时不变焦点 IV、between-unit 理论对齐，见变体 13/22/38），并声明聚类 SE 层级（firm/industry-year/嵌套） |

## 诚实边界

- **RE vs FE 选择**：必须基于理论（跨单元差异 vs 单元内变化）而非仅凭 Hausman。若理论关注单元内变化但 Hausman 不显著 → 仍应使用 FE 并报告两者比较。ICC 可用于辅助论证但非决定性。
- **多数据库合并**：报告交集前后的 N 差异。若某一数据库匹配率极低（<50%），应解释原因并讨论选择偏误风险。
- **控制变量数量**：19+ 控制变量需提供理论或方法论引用支撑（如 "following [citation], we include a comprehensive set of controls"），且在稳健性中报告简化模型。
- **网络变量与 FE 的交互**：当模型同时包含 dyad FE 和网络变量时，网络变量的 within-dyad 变异可能很小，导致系数估计不稳健，需在 M8 讨论。
