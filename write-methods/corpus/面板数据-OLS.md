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
  - "kalaignanametal2013 (Journal of Marketing): first-differenced reliability change, IGLS error-structure diagnostics, reverse-coded z-score composite moderator, t-2 instrumented LDV"
  - "lunetal2026 (Entrepreneurship Theory and Practice): functional-executive power as compensation ratio with absent-title coded 0"
  - "liuliuluo2016 (Journal of Marketing): residualize a collinear control (reputation on size) and enter the residual"
variants_count: 50
created: 2026-05-18
updated: 2026-08-13
---

# 面板数据-OLS — Methods 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M1 | 4 | 15, 23, 33, 41 |
| M2 | 11 | 2, 6, 9, 11, 12, 16, 26, 27, 31, 34, 44 |
| M2.5 | 3 | 20, 39, 43 |
| M3 | 4 | 17, 25, 35, 45 |
| M4 | 7 | 3, 19, 24, 29, 30, 32, 36 |
| M5 | 6 | 4, 5, 28, 42, 46, 49 |
| M6 | 5 | 1, 14, 37, 40, 50 |
| M7 | 8 | 7, 10, 13, 18, 21, 22, 38, 47 |
| M8 | 2 | 8, 48 |

### M1（4）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 15 | 单行业设置 — 双重现象共存辩护 | 单行业样本一句式情境正当化：两个理论前提现象同时存在 | — | EMERGING | Cui, Yang & Vertinsky SMJ |
| 23 | 行业统计 + 先例对齐的设置辩护 | 单行业事件研究：行业统计证互依 + "大事件"抽样标准 + 先例对齐 | 区别于变体9（制度断点）与变体15（双重现象）：行业统计+抽样阈值+先例对齐 | VERIFIED | Pupovac et al. 2026 POM |
| 33 | 单一中介机构设置辩护 | 以单个评级/平台/审核机构为情境：a/b/c 三理由+单一机构一致性 | 区别于变体15（双重现象）与变体23（行业统计）：中介机构选择+方法差异消解 | EMERGING | DesJardine, Li & Shi 2025 AMJ |
| 41 | 数据可得性挑战→独特档案数据集设置辩护 | 单组织/单一评价领域研究，关键结果变量部分 censored 或未披露，须自建档案数据集 | 区别于变体15（双重现象）与变体33（单一中介机构）：数据可得性挑战驱动设置合法性 + 双制度张力情境 | EMERGING | Fini et al. 2017 (AMJ) |

### M2（10）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 样本交集漏斗 | 多库合并后报告起始N到最终N的逐层排除审计 | — | VERIFIED | Darby2026/2025/2023 |
| 6 | 多通道精英/关键行为人招募 | 难以接触的研究对象（高管/董事/精英决策者）多通道招募 | — | EMERGING | Mannor et al. 2016 SMJ |
| 9 | 制度断点样本辩护 | 单行业面板：制度事件定起始、数据可得定终止、单行业理论理由 | 区别于变体15（M1 设置辩护）：M2 样本边界三重正当性 | EMERGING | Desai 2011 AMJ |
| 11 | 匹配样本层次回退 + 匹配平衡保守检验 | 匹配质量与样本量存在 trade-off 的匹配样本设计 | — | EMERGING | Pfarrer et al. 2010 AMJ |
| 12 | 单行业面板 + SIC 边界意识 + 限制样本稳健性 | 单行业样本受少数非核心行业企业驱动的担忧 | 区别于变体9（制度断点定边界）：行业分类模糊性+限制样本稳健性 | VERIFIED | Darby et al. 2026 JOM |
| 16 | 多源 alliance 数据库合并与交叉验证 | 多数据库互补合并，防重复计数、防 announced-but-not-realized | 在变体2（交集漏斗）基础上扩展为完整段落：多源互补+人工 due diligence | EMERGING | Cui, Yang & Vertinsky SMJ |
| 26 | 跨库手工匹配（无共同标识符）+ 多源漏斗 | 两核心库无共同标识符（如 ACSI↔Compustat）须手工匹配 | 区别于变体16（自动交叉验证）与变体2（逐步交集）：手工匹配明示+五库漏斗 | EMERGING | Malshe & Agarwal 2015 JM |
| 27 | 构念形成窗—结果观察窗分离 + 双代理收敛 | 稳定特质代理可能被同期结果反向污染（副槽位 M4、M8） | 区别于变体19（同期/滞后期权 moneyness）：完整形成期与观察期切开+双代理三角化 | EMERGING | Schumacher, Keck & Tang 2020 SMJ |
| 31 | 异频数据时间对齐 — 事件聚合至结果频率 | event-day vs 月 vs 年三频数据对齐（副槽位 M4） | 区别于变体2/26（强调多库交集N）：解决频率对齐 | VERIFIED | Liu & Shankar 2015 MS |
| 34 | 多源清单 + 覆盖边界定样本窗 | 多库枚举后直接交集，数据库覆盖边界定起始/终止 | 区别于变体9（制度事件定起始）：数据覆盖驱动双边界 | EMERGING | DesJardine, Li & Shi 2025 AMJ |
| 44 | 纳入零事件年作为单元自对照 | 事件史/召回等零事件年可观测的平衡面板 | 区别于变体2（漏斗）与变体28（GEE 保全零）：识别逻辑而非估计器 | VERIFIED | Kalaignanam et al. 2013 JM |

### M2.5（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 20 | Model-Free Evidence 预览 | 正式回归前以 quartile 均值/中位数展示无条件关系 | — | EMERGING | Chung, Low & Rust 2022 JAMS |
| 39 | 时间间隔声明（DV t+1 / IV & controls t） | 纵贯面板需在 Methods 层预先化解反向因果 | 区别于变体 20（model-free 预览）与变体 27（窗口分离）：单句 baseline 承诺，更通用 | EMERGING | Ridge et al. 2024 (AMJ) |
| 43 | 两步滞后链 + 年内再编码学习窗 | 冲击→中介→下游结果的纵贯链 | 区别于变体39（单句 spacing）：理论–测量–模型两步对齐；非正式 Granger 检验 | VERIFIED | Kalaignanam et al. 2013 JM |

### M3（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 17 | 多维行为指标 → factor score → 平均值 | 多维行为 DV：子维度理论含义+信度+合成方式 | — | EMERGING | Cui, Yang & Vertinsky SMJ |
| 25 | DV 文献基准锚定 — 均值与前人文献对比 | 新构建比率/计数 DV 的外部效度锚定 | 语料内首见 DV 外部效度锚定（现有变体无） | EMERGING | Du & Tsolmon 2024 ORSC |
| 35 | 离散化等级 DV 边界距离操作化 | letter-grade DV：边界距离变量+边际影响预检验 | 区别于变体17（factor score）与变体25（文献锚定）：边界聚集+边际影响声明 | EMERGING | DesJardine, Li & Shi 2025 AMJ |
| 45 | 数据源隔离理论相关事件 vs 伴生混淆 | DV 与理论对象之间夹杂伴生事件 | 区别于变体25（文献均值锚定）：用数据源能力剥离混淆通道 | VERIFIED | Kalaignanam et al. 2013 JM |

### M4（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | IV 选择三层 because 论证链 | 单一操作化同时代理多个理论机制的 IV 辩护 | — | VERIFIED | Darby2023 MSOM |
| 19 | 高管信心期权 moneyness 操作化 | 高管自信构念操作化（公式+滞后+因果优先） | — | EMERGING | Chung, Low & Rust 2022 JAMS |
| 24 | 法律强制披露阈值 → 自愿披露操作化 | 法律-会计准则张力转化为构念变异空间 | — | VERIFIED | Pupovac et al. 2026 POM |
| 29 | 召回严重度理论分类 — 后果类型二元操作化 | 监管后果描述→心理学可辩护的二元 severity | — | VERIFIED | Liu & Shankar 2015 MS |
| 30 | 媒体覆盖 — 双索引相关度阈值 + 互补数据源 | 媒体计数需 face-validity 链：双索引阈值+双源互补 | 区别于 generic media count：强制双索引 relevancy 阈值+排除逻辑 | VERIFIED | Liu & Shankar 2015 MS |
| 32 | 结构二元特征操作化为「kind」而非「degree」 | 治理/组织极端结构二元化（lone-insider 董事会等） | 区别于现有 M4 变体（连续构念/阈值披露/双代理收敛）：kind≠degree 辩护+稳健性预告 | EMERGING | Zorn et al. 2017 SMJ |
| 36 | 复合测量构念分步构建 | 乘积/交集型复合 IV：阈值辩护+可行性论证+分步计算 | 区别于变体3（三层 because 机制代理）与变体19（moneyness）：双持有侧乘积+可行性 | EMERGING | DesJardine, Li & Shi 2025 AMJ |

### M5（6）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | Mixed-effects within/between 机制分解 | 面板中区分个体内变化 vs 个体间差异的机制检验 | — | VERIFIED | Darby2023 MSOM |
| 5 | 替代变量机制对齐矩阵 | 一个构念→多个可分离机制的三角验证（配合机制对齐图） | 区别于变体4（within/between 分解）：主变量+替代变量×机制映射矩阵 | VERIFIED | Darby2023 MSOM |
| 28 | Binary-panel GEE + 全零单元保留 + 正式曲线识别链 | 二元面板大量全零单元 + U/倒U假设（副槽位 M7、M8） | 区别于变体22（时不变 IV 选 GEE）：保留全零单元为首要理由+曲线四事前约束 | VERIFIED | Bendig et al. 2024 ETP |
| 42 | 调节 dummy 的外部效度链 — 外部连续学科测量 + 定性锚定 | 自造调节 dummy（如受众身份 proximity）需辩护二分依据（副槽位 M7） | 区别于变体4/5（机制分解）与变体28（估计器曲线链）：调节变量测量本身的构造效度链，非机制或估计器 | EMERGING | Fini et al. 2017 (AMJ) |
| 46 | 反向原始指标的 z 分复合 + 反向编码 | 多指标合成且原始分与构念方向相反 | 区别于变体42（dummy 效度链）与变体36（乘积复合）：方向逻辑先于标准化 | VERIFIED | Kalaignanam et al. 2013 JM |
| 49 | 职能高管权力：有职位薪酬比，无职位编码为 0 | 结构权力代理：有 title 用薪酬比，无 title 编码为 0 | 区别于变体42（dummy 效度链）与变体46（z 分复合）：缺席=权力零 | EMERGING | Lun et al. 2026 ETP |

### M6（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 控制变量分层 because 结构 | 控制变量的黄金标准：按层级递进+每变量显式 because | — | VERIFIED | Darby2026/2025/2023 + Eilert2017 |
| 14 | 全谱系控制变量 — 高 because 密度 + 事件控制 + CEO 人格 | 文本构念+市场反应交叉领域、多种混淆来源并存 | 在变体1（分层 because）基础上三升级：RavenPack 事件控制+Big5 人格+互补DV维度 | EMERGING | Li et al. 2026 JOM |
| 37 | rival 镜像控制变量惯例 | 对手侧镜像控制：引用前例+命名规则+聚合方式一句完成 | 区别于变体1（分层 because）与变体14（全谱系）：跨主体镜像控制 | EMERGING | DesJardine, Li & Shi 2025 AMJ |
| 40 | 控制变量"双面 because" — 对 DV 一条理由 + 对 IV 共变一条理由 | CEO/个体特质 → 结果研究，控制为何与特质共变最易被质疑时 | 区别于变体14（强调 because 密度）：每个控制对 DV 与对 IV 各一条理由，平行论证结构 | EMERGING | Ridge et al. 2024 (AMJ) |
| 50 | 共线控制残差化：构念对另一控制回归后取残差 | 两个控制都要保留、但高度共线时 | 区别于变体1/14/40（because 密度）与变体37（镜像控制）：用残差隔离共线通道 | EMERGING | Liu, Liu & Luo 2016 JM |

### M7（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 7 | 嵌套横截面数据的聚类稳健标准误 | 数据嵌套（决策嵌于高管）但不足以跑多层模型 | — | EMERGING | Mannor et al. 2016 SMJ |
| 10 | Hausman 检验 — FE vs RE 选择 | 标准 FE/RE 选择三步段 | 与变体13 互补（其处理 theory→RE 路径） | EMERGING | Bamberger et al. 2021 JM |
| 13 | 随机效应选择三重辩护 — 理论+Hausman+ICC | 理论指向 RE（关注跨单元差异）时的系统辩护 | 区别于变体10（标准 Hausman→FE）：理论理由+Hausman+ICC 三层递进 | EMERGING | Li et al. 2026 JOM |
| 18 | dyad fixed effects + dyad 聚类标准误 | dyad 面板 + 需具体时不变混淆源举例 | 与变体7（嵌套横截面聚类）互补：dyad FE+混淆源实例化 | EMERGING | Cui, Yang & Vertinsky SMJ |
| 21 | 三向交互模型设定 | X×W1×W2 设计：完整方程+mean-centering+聚类SE | — | EMERGING | Chung, Low & Rust 2022 JAMS |
| 22 | GEE + AR(1) working correlation — 时不变焦点 IV | 焦点 IV 时不变（意识形态/人格/创始人身份等），firm FE 会吸收主效应 | 区别于变体10/13（Hausman/ICC 选 FE/RE）：按 IV 时不变性选 GEE | EMERGING | Abdurakhmonov et al. 2026 JOM |
| 38 | 理论-估计量对齐 + 不滞后辩护 | between-unit 理论 → pooled OLS 显式对齐；当前期机制 → 不滞后（Bellemare） | 区别于变体10/13（Hausman/ICC）：理论对齐+不滞后反向论证 | EMERGING | DesJardine, Li & Shi 2025 AMJ |
| 47 | 一阶差分变化规格 | 短/中面板、关注 within-unit 变化、水平方程已含 FE | 区别于变体10（水平 FE）与 DiD ΔV 等价：FD 变化规格 + 丢掉 unit dummy | VERIFIED | Kalaignanam et al. 2013 JM |

### M8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 8 | 回顾性偏差三角检验 | 依赖事后自我报告的数据：控制情感变量+定性定量一致性+替代测量复制 | — | EMERGING | Mannor et al. 2016 SMJ |
| 48 | 误差结构三诊断 → IGLS | 嵌套面板 + FD + LDV 后误差不干净 | 区别于变体8（自我报告偏差）与 GEE 先验相关结构：诊断驱动 GLS | VERIFIED | Kalaignanam et al. 2013 JM |

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
**验证状态**: VERIFIED
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


#### 变体：M6 动态模型的「全一阶差分」控制声明 + 分层 because 链（post_2022_women_tmt_strategic_renewal 型，EXTEND）
- **功能标签**：在变体 1 的分层 because 结构之上，增加动态模型特有的控制变量处理声明（全差分）+ 供给侧（候选池）控制逻辑
- **骨架**：Our analyses controlled for time-variant characteristics of [CEO], [TMT], [firms], and [countries], some of which were variables in studies published with subsets of our data (see [Table reference]). To estimate dynamic models, all control variables, unless noted otherwise, are in first differences (from year [t-1] to [t]), accounting for the change in these characteristics in all models. [Level] controls. We included [control], because [rival explanation]. Because [contextual/societal factor] may influence the strength of [relationship], we controlled for such disparities, with [measure]. We also controlled for [supply-side factor]—the availability of [candidates] in the [labor market]—by including [measure].
- **原文锚定**："Because societal disparities between men and women may influence the strength of women's influence at upper echelons (Hoobler et al., 2018; Post & Byron, 2015), we controlled for such disparities, with the gender gap index (World Economic Forum, 2015)."（post_2022_women_tmt_strategic_renewal, AMJ 2022, Control Variables 节）
- **区别于**：变体 1（分层 because 结构）是静态控制变量的 because 密度范本；本变体新增两个维度：(a) 「为配合动态模型，所有控制变量（除注明外）均取一阶差分」的全局声明句式；(b) 供给侧控制——除需求侧竞争性解释外，还控制「候选池可得性」（women in management）这类生成机制变量
- **反模式对照**：行业控制用 12 个 industry dummy 但未解释与固定 industry effects 的分工（M7 用 fixed industry effects + M6 再放 industry dummies 存在重复吸收嫌疑）——写入时带一行警告

### 变体 2: 样本交集漏斗 (3/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Darby2023 MSOM
**原始句锚点**: The intersection of these datasets resulted in a sample of 2982 high severity recalls across 69 publicly traded firms from 2002 to 2020.
**验证状态**: VERIFIED
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
**验证状态**: VERIFIED (1/4，但生成力极高)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> We used [IV] as our primary measure because it is a broad, comprehensive measure that reflects the [number] related, but distinct, mechanisms we theorized about in [Hypothesis]—[mechanism_1], [mechanism_2], and [mechanism_3]. First, [theoretical_rationale_1] ([citation]), and research indicates that [IV] is one of the most effective tools to do so ([citation]). Second, research suggests that [IV_property_2] ([citation]). Third, [IV_property_3] ([citation]). Overall, prior studies conclude that [IV] is key to understanding [theoretical_consequence] ([citation]), which is why we use it as our primary measure, although we examine alternative measures in [location].
**与原骨架差异**: 一般论文在M4中简单报告"We measure X as Y"，而此骨架构建了从构念→操作化→多机制映射的完整论证链。适用于任何**单一操作化同时代理多个理论机制**的情境。关键策略：(1) 理论机制枚举（"three related, but distinct, mechanisms"）；(2) 每个机制有独立文献链；(3) 末句预告替代变量检验（"although we examine alternative measures"），建立M4→M5的叙事桥梁。

### 变体 4: Mixed-effects within/between 机制分解
**来源论文**: Darby2023 MSOM
**原始句锚点**: The results suggest that the effect of CEO stock ownership is driven by the within-component rather than the between-component. That is, it is not the difference in CEO stock ownership between firms, but, rather, a relative increase in stock ownership for a given CEO within the same firm that explains recall delays.
**验证状态**: VERIFIED (1/4，机制检验设计特有)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> We used mixed-effects models to explore the within-[unit] and between-[unit] effects of [IV], and the results are reported in [Table_reference]. Model ([ref]) indicates that the within-component of [IV] has a [direction] and [significance] relationship with [DV] (β = [value], p < [threshold]), whereas the between-component is [not statistically significant / opposite direction]. The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not the difference in [IV] between [units], but, rather, a relative increase in [IV] for a given [unit] within the same [cluster] that explains [DV].
**与原骨架差异**: 这是将统计结果翻译为机制语言的核心句式。关键策略：(1) 报告within/between系数对比；(2) "it is not... but, rather..."句式将统计输出转化为理论叙事；(3) 明确指出是"个体内部变化"还是"个体间差异"驱动效应。适用于任何面板数据中需要区分个体内变化vs个体间差异的机制检验。

### 变体 5: 替代变量机制对齐矩阵
**来源论文**: Darby2023 MSOM
**原始句锚点**: To probe these three mechanisms at a more granular level, we replicated our recurrent-event AFT analyses using two alternative measures of CEO stock ownership—specifically, CEO Equity-Based Compensation and CEO Ownership (Monetary).
**验证状态**: VERIFIED (1/4，需配合 Figure 1 机制对齐图使用)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> Following extant research ([citation]), we used [Primary_IV] as our primary measure because it broadly reflects [number] mechanisms: [mechanism_list]. To probe these mechanisms at a more granular level, we replicated our analyses using two alternative measures of [construct]—[Alternative_1] and [Alternative_2]. We measured [Alternative_1] as [definition]. We measured [Alternative_2] as [definition]. [Figure_reference] details each measure and its alignment with our theorized mechanisms. Both our primary measure and the alternative measures inherently reflect [shared_mechanism]. [Alternative_1] also proxies for [mechanism_A] because [rationale] ([citation]), whereas [Alternative_2] also proxies for [mechanism_B] because [rationale] ([citation]). Thus, although our primary measure is comprehensive and reflects all [number] mechanisms, the alternative measures help us examine whether, indeed, all [number] mechanisms contribute to [DV].
**与原骨架差异**: 这是**三角验证**策略在 variable construction 层面的应用。关键要素：(1) 主变量+替代变量矩阵；(2) Figure 1 机制对齐图（每个变量→哪些机制→理论基础）；(3) 部分重叠的机制映射（变量A覆盖机制1+2，变量B覆盖机制1+3，变量C覆盖机制2+3）；(4) "虽然主变量全面，但替代变量帮我们检验是否所有机制都起作用"的诚实表述。适用于任何"一个构念→多个可分离机制"的构念效度设计。

### 变体 6: M2 多通道精英/关键行为人招募 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: Recognizing the challenge of the last criterion in particular, we used four methods to recruit participants. First, several key advocates for our research served on the boards of Fortune 500 companies and agreed to contact as many of their director colleagues as possible on our behalf.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We recruited [actors] through [N] channels to maximize sample diversity and reduce selection bias. First, we partnered with [organization_type_A: e.g., board advocacy group] which provided access to [actor_pool_A]. Second, we worked with [organization_type_B: e.g., consulting firm] to identify [actor_pool_B]. Third, we contacted [organization_type_C: e.g., alumni office] for [actor_pool_C]. Finally, we used snowball sampling through [references] to reach additional participants. This multi-channel approach yielded [N_final] [actors] representing [N_firms/units] across [N_industries] industries.
**与原骨架差异**: 针对难以接触的研究对象（高管、董事会成员、精英决策者），单一招募渠道会导致样本集中于某一类型——多通道招募通过制度多样性（advocacy groups vs consulting partners vs alumni networks）增加样本覆盖。关键要素：每个通道说明其提供哪类参与者，最终汇总样本的行业分布。

### 变体 7: M7 嵌套横截面数据的聚类稳健标准误 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: To account for the nonindependence in our data (i.e., the multiple strategic decisions per executive), we specified Huber/White/sandwich standard errors using the “robust” option in Stata 12. Decisions were clustered by executive.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> Because our data involve [lower_unit] nested within [higher_unit] (e.g., decisions nested within executives), observations are not independent. We therefore estimated [models] with [SE_type] robust standard errors clustered by [cluster_level] to account for within-[cluster] correlation of the error terms ([citation]). This approach treats each [cluster] as an independent sampling unit while allowing [lower_units] within the same [cluster] to share unobserved characteristics.
**与原骨架差异**: 当数据具有嵌套结构（如多个决策嵌套在同一高管/公司内）但不足以运行多层模型（样本量/top-level 单元数不足）时，聚类稳健SE是最小负担的解决方案。关键：明确说明嵌套层级和聚类层级，解释为什么这样聚类（共享不可观测特征）。

### 变体 8: M8 回顾性偏差三角检验 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: We thus took steps to ensure that the lengthier time horizon for some of the decisions did not introduce retrospective bias into our study. First, and as we discuss later, we controlled for executives' self-ratings of decision quality and recent performance in all models.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M8
**骨架**:
> A potential concern with [retrospective/interview-based] data is that [actors]'s recollections may be colored by [outcome knowledge/hindsight]. We addressed this concern through a triangulation approach: First, we controlled for [affective/outcome variables: e.g., satisfaction with decision outcome] to partial out post-hoc rationalization. Second, we compared [qualitative/text patterns] with [quantitative/archival patterns] to check consistency. Third, we replicated our findings using [alternative measure/sample] that is less susceptible to retrospective bias. Results were consistent across all approaches.
**与原骨架差异**: 适用于任何依赖事后自我报告的研究（访谈、问卷、回忆数据）。三管齐下：(1) 控制情感/结果变量（partial out halo）；(2) 定性-定量一致性检查；(3) 替代测量复制。

### 变体 9: M2 制度断点样本辩护 — 行业收缩+时间边界双重正当性 (1篇高价值)
**来源论文**: Desai 2011 (Academy of Management Journal)
**原始句锚点**: I tested these hypotheses on a panel of all U.S. class I railroad firms operating between 1980 and 2003. The U.S. railroad industry was deregulated in 1980, making prior years incomparable with later ones (Smith & Grimm, 1987).
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> The sample period begins in [year_start] because [institutional_event: e.g., regulatory change / industry deregulation] fundamentally altered [key_process] in [industry]. Before [year_start], [condition_A]; after [year_start], [condition_B], making the post-[year_start] period uniquely suited to testing our theory. The sample ends in [year_end], the last year for which [data_source] was available. We focus on a single industry—[industry_name]—to hold constant [confounds: e.g., regulatory environment, technological trajectory, product characteristics] that vary across industries. This single-industry design maximizes internal validity at the expense of generalizability, a trade-off appropriate for theory testing.
**与原骨架差异**: 单行业面板的样本辩护需要完成三重正当性：(1) 制度/法规事件作为起始边界（不早不晚）；(2) 数据可得性作为终止边界；(3) 单行业选择的理论理由（holding confounds constant → internal validity > generalizability）。与多行业面板的"we used all firms in Compustat"形成对比。

### 变体 10: M7 Hausman 检验 — FE vs RE 选择 (1篇高价值)
**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**原始句锚点**: Our choice for a fixed-effects model over a mixed-effects model is appropriate, as the Hausman (1978) test indicates (χ2/d.f. = 24.6, p <.01).
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used a [Hausman test] to determine whether [fixed effects] or [random effects] was more appropriate for our panel structure. The test strongly rejected the null hypothesis that the [unit]-specific effects are uncorrelated with the regressors (χ² = [value], p < [threshold]), indicating that [fixed effects] is the preferred specification. We therefore estimated [FE_estimator] with [SE_type] clustered by [cluster_level].
**与原骨架差异**: 标准 FE/RE 选择段落。关键三步：(1) Hausman 检验结果（χ² + p-value）；(2) 解释拒绝意味着什么（"unit-specific effects correlated with regressors"）；(3) 据此选择估计器 + 标准误声明。

### 变体 11: M2 匹配样本层次回退 + 匹配平衡保守检验 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "We then matched each high-reputation firm with three firms from the same four-digit SIC code that were similar in assets, revenues, and return on assets (ROA) (Combs & Skill, 2003; Porac, Wade, & Pollock, 1999). Where appropriate matches were not found at the four-digit level, we looked at three-digit and two-digit SIC codes for similar firms (Combs & Skill, 2003). … A t-test comparing differences in firm size (total assets) revealed no significant differences between the 80 high-reputation and 211 matched companies (t = −0.35, n.s.); however, in keeping with the predictions of prior reputation research (Roberts & Dowling, 2002), there were significant differences in revenues and ROA ($35.1 vs. $16.8 billion, p < .001; and 8.97 percent vs. 4.28 percent, p < .001, respectively)."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> We used a matched sample design to construct a comparison group of [units] that did not experience [treatment] but were otherwise similar on [key dimensions]. Specifically, we matched each [treated_unit] to [N] [control_units] in the same [industry/sector] and [time_period] based on [matching_criteria: e.g., size, age, performance]. When a close match was unavailable at [strict_criteria], we relaxed the criteria to find the closest available match—a hierarchical fallback approach that prioritizes match quality while preserving sample size. To ensure that the matched groups are balanced, we compared [treated] and [control] groups on [N] characteristics using [t-tests / standardized differences]. No significant differences were found across any of the [N] dimensions (all p > [threshold]), suggesting that the matching procedure achieved adequate balance.
**与原骨架差异**: 标准匹配样本段落仅报告"we matched on X"——Pfarrer 增加了两个关键要素：(1) **层次回退**——先在严格维度匹配，无匹配时放宽标准，透明化匹配的灵活边界；(2) **匹配平衡保守检验**——使用保守的 t-test（而非仅标准差异）验证处理组和对照组在所有匹配维度上的可比性。适用于匹配样本设计中匹配质量与样本量之间存在 trade-off 的场景。



### 变体 67：完备性准则漏斗 + 总体代表性 t 检验（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "The initial sample frame for this study included [population definition]. The final sample included all [units] for which complete data on [variable domain 1], [variable domain 2], and [variable domain 3] were available. This criterion yielded [N] [units]. T-tests revealed that [units] in this sample were not significantly different in [dimension 1] or [dimension 2] from [units] in the larger population."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Sample and Data Collection（P1）

**原文锚定**:
> "T-tests revealed that companies in this sample were not significantly different in sales or profitability (return on assets) from companies in the larger population."

**关键特征**:
- 三步漏斗（总体框架→完备性准则→N）极简但每步可审计：排除规则是一条统一的"数据完备"准则而非逐条剔除，N 直接由准则导出——多变量域合并样本的合法省步模式
- 样本代表性不靠声明靠检验：对未入样总体做 sales/ROA 双维 t 检验并把"无显著差异"写进 Methods——把外部效度质疑转化为一个可复核的统计事实
- 观察窗与事件窗分离声明（数据 1982-1992、采纳事件 1985-1991，因滞后结构需要前后缓冲）——窗宽由模型结构（lag structure）论证而非随意

**适用**: 多数据库合并的完备性准则抽样（compensation+governance+market data 交集型）；被质疑"完整数据可得性准则造成选择偏误"的大样本档案研究

**禁忌**: 代表性 t 检验的维度必须是与因变量机制相关的维度（本篇规模+盈利），不能只挑好看维度；完备性准则造成的幸存者偏误若理论相关，需在 Discussion 承接

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 12: M2 单行业面板 + SIC 边界意识 + 限制样本稳健性 (1篇高价值)
**来源论文**: Darby, Wowak, Ketchen, Connelly & Skowronski 2026 (Journal of Operations Management)
**原始句锚点**: However, the sample was not limited to this industry because firms may be formally classified in other industries (e.g., Proctor & Gamble in SIC 284 or General Electric in SIC 999) but still produce—and potentially recall—medical devices.
**验证状态**: VERIFIED
**写入日期**: 2026-07-07
**槽位**: M2
**骨架**:
> As might be expected, the majority of [units] in our sample operate primarily in [primary_industry] ([SIC_code]). However, the sample was not limited to this industry because [units] may be formally classified in other industries ([example_codes]) but still [engage in phenomenon]. To ensure that the sample is not unduly influencing our results, we conducted an additional analysis that limited the sample to only [primary_industry] [units]. The results are consistent with our primary results.
**与原骨架差异**: 单行业研究的标准担忧是"样本是否受少数非核心行业企业驱动"。本骨架通过两步消除此担忧：(1) 先承认行业分类的模糊性——SIC code 不完全等于业务实质；(2) 报告限制样本的稳健性检验。两句话完成，不需要独立附录表。

### 变体 13: M7 随机效应选择三重辩护 — 理论+Hausman+ICC (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: We used panel regressions with random-effects estimations, because theoretically, we were more interested in the differential effects across CEOs rather than changes within CEOs. The Hausman test (p =.169) confirmed that using the random-effects (vs. fixed-effects) method was more appropriate.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We used panel regressions with random-effects estimations, because theoretically, we were more interested in the differential effects across [unit] rather than changes within [unit]. The Hausman test (p = [value]) confirmed that using the random-effects (vs. fixed-effects) method was more appropriate. Also, [key_predictor] is likely to be an enduring [attribute_type] that remains stable over a short timeframe. We examined [its/their] internal consistency (ICC) using hierarchical linear modeling (HLM) to further test this premise. We used [predictor] as the outcome variable and treated [level_1_unit] as Level 1 and [level_2_unit] as Level 2 in the analyses. The ICC value ([value]) indicated that [predictor] tends to be stable within the individual but shows systematic variation across [level_2_unit]. We used robust standard errors to minimize heteroscedasticity and autocorrelation in our analyses ([citation]).
**与原骨架差异**: 本骨架与变体10（标准 Hausman→FE 选择）互补——当**理论指向 RE**时（关注跨单元差异>单元内变化），需要比单一 Hausman 更系统的辩护。Li et al. 提供了三层递进：(1) 理论理由——"more interested in differential effects across CEOs rather than changes within CEOs"；(2) Hausman 统计证据（p>.05 → RE 合适）；(3) ICC 辅助证据——用 HLM 估计关键预测变量的跨层变异比例，证明该变量确实在 Level 2 单元间存在系统性变异。注意：若理论关注单元内变化（如 within-firm dynamics），即使 Hausman 不显著也应使用 FE 并报告两者比较——本骨架仅适用于 theory→RE 的路径。
**诚实边界**: RE 选择的最低要求：(1) 理论理由（跨单元差异>单元内变化），(2) Hausman 检验结果，(3) 关键预测变量的 ICC 作为辅助证据。仅凭 "Hausman test was not significant (p > .05)" 不足以说服审稿人——需解释**为什么理论预期 RE 比 FE 更合适**。


### 变体 60: M2.5 预测变量组内变异预展示为 FE 设计发证 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: Figure 1 shows that FBR experiences fluctuation within firms across time, which is pivotal for our examination of how within-firm changes in FBR influence future recall decisions.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M2.5（识别前铺路）

**骨架**:
> In [Figure X], we summarize the within-[unit] variation of [the predictor] across time in our study. The y-axis represents [average within-unit change] in [the predictor] for each [period], and the x-axis is [the periods examined]. [Figure X] shows that [the predictor] experiences fluctuation within [units] across time, which is pivotal for our examination of how within-[unit] changes in [the predictor] influence [the outcome].

**与原骨架差异**: 区别于变体 20（model-free evidence 预览结果模式）——本变体预览的不是 outcome 而是**预测变量的组内变异**：在 Methods 里用一张图先证明"组内有足够的变异可供 FE 识别"，把识别策略的可行性论证前置到测量节。

**诚实边界**: 展示组内变异存在 ≠ 变异外生；不得把它当识别证据呈报；若变异集中于少数单元，应补充分布统计而非只给均值轨迹。

### 变体 14: M6 全谱系控制变量 — 高 because 密度 + RavenPack事件控制 + CEO人格特质 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: We controlled for several variables to account for their unique influence on investors' reactions. The control variable data were derived from the previous quarter before the focal earnings call unless otherwise indicated.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M6
**骨架**:
> We controlled for several variables to account for their unique influence on [DV]. The control variable data were derived from [time_period] before the focal [event] unless otherwise indicated. First, we controlled for [control_1] ([operationalization]), as [because_reason]. We controlled for [control_2], calculated as [formula]. We accounted for [control_3] from [source] ([scale_description]). We used [aggregation_method] by [source_type] based on [selection_criterion] before the [event] ([citation]). We controlled for [control_4], measured in [unit], since [because_reason]. We controlled for [control_5] ([operationalization]), measured as [calculation_detail] ([citation]). We accounted for the confounding effects of [event_type_1] and [event_type_2] on [DV] ([citation_1]; [citation_2]). All pertinent news was sourced from the "[category_1]" and "[category_2]" categories from the [database]. We included only news articles with a relevance score of [threshold], indicating [rationale]. Furthermore, we kept only the first occurrence of each [event_type] that appeared in any news outlet within a [time_window].
>
> In addition, we controlled for [actor] [demographic_1], [demographic_2], and [demographic_3] ([citation]). We controlled for [actor] displayed [psychological_state_1] and [psychological_state_2], generated using [text_tool] [version] default dictionary, because [rationale] ([citation]). We controlled for [actor] use of [linguistic_feature] ([citation]) because, similar to [key_predictor], [linguistic_feature] might [threat_rationale]. [Actor] personality traits ([trait_list]) were controlled because they may impact [outcome]; they were measured based on [citation]. We controlled for [complementary_DV_dimension] to account for the [opposite_dimension] in [data_source], measured with [dictionary/method]. Finally, we included [fixed_effect_1] and [fixed_effect_2] in each model.
**与原骨架差异**: 在变体1（分层 because 结构）基础上的三个升级：(1) **RavenPack 事件控制**——新产品公告和M&A新闻的 confounding effects 需明确控制，且需报告 relevance score 阈值和去重策略（"first occurrence within a one-day window"）；(2) **CEO 人格特质控制**（Big 5）——在 CEO 沟通研究中，人格特质可能同时影响语言使用和投资者感知，但极少论文控制此维度；(3) **互补 DV 维度控制**——如主DV为负向情绪时，控制正向情绪维度。本骨架的 because 密度目标为 ~100%——每个控制变量（共19个）都附带 because 理由。适用于任何理论预测多种混淆来源的研究（特别是文本构念+市场反应的交叉领域）。
**诚实边界**: 19个控制变量可能引发 overfitting 担忧——应在稳健性中报告仅含核心控制的简化模型。若某控制变量的 because 无法给出，应质疑是否真的需要控制。






### 变体 65：时间括弧控制 + 反向相关保守性声明（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We also ran [N] sets of supplementary analyses in which we controlled for [adoption of alternative changes] and [change in the outcome domain], with these variables measured for one of the following three time periods: (1) period t (the period of [the focal event]), (2) period t+1, or (3) period t through t+1. These analyses assess whether any effects of [the focal predictor] result from the simultaneous or subsequent adoption of other changes in [the outcome domain]. The results were substantively unchanged from the results presented below. Moreover, these control variables were [negatively] correlated with [the focal predictor], [so any remaining bias works against the hypothesized finding]. We also ran separate analyses including dummy variables for [industry classification] codes and found that controlling for industry differences had essentially no effect on the results."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Control Variables（P3）

**原文锚定**:
> "These analyses assess whether any effects of symbolic LTIP adoption result from the simultaneous or subsequent adoption of other changes in board composition or incentive compensation. ... Moreover, these control variables were negatively correlated with symbolic LTIP adoption."

**关键特征**:
- 时间括弧设计：同一组替代变化在 t / t+1 / t…t+1 三种时间窗分别入模型——把"焦点采纳只是同时期其他改革的代理"这一竞争性解释在三个时间位点上逐一封死，每窗对应一个明确的检验目的句
- "these control variables were negatively correlated with [focal predictor]" 是控制变量段的保守性点睛：控制与焦点预测变量负相关意味着控制只会削弱而非制造 focal 效应——一句相关系数陈述完成 omitted-variable 方向论证
- 稳健性链条按"假设→检验→结果→方向"四拍收束（assess whether→results unchanged→moreover negatively correlated→industry dummies no effect），每拍一句，无冗余

**适用**: 焦点事件与其他同期改革并存、被质疑"效应实为同期改革"的采纳/改革研究；控制变量与 focal IV 负相关且方向对假设不利（即保守）时

**禁忌**: 保守方向声明必须基于实际计算的相关（方向要对假设不利才可写），不得反向包装；时间括弧窗需与"实施可能延迟"的实质窗口匹配，窗太短则检验无效

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 64：风险集排他型控制变量剔除（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We controlled for prior [levels of the outcome domain] in all models, since prior levels might influence subsequent changes as well as [the focal reaction]. We used the following commonly used indicators of [the construct] ([citation]): (1) [indicator 1] ([citation]); (2) [indicator 2]; (3) [indicator 3]; and (4) [indicator 4], which we excluded from models predicting [change in that same indicator], since only [units] with [the antecedent state] are at risk of [the change]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Control Variables（P2）

**原文锚定**:
> "and (4) CEO/board-chair separation, which we excluded from models predicting separation of the CEO and board chair position, since only firms with combined CEO/board chair positions are at risk of separation."

**关键特征**:
- 控制变量清单内嵌一条"反向剔除"规则：某指标在预测其自身变化时不进模型——because 从句给出事件史风险集逻辑（只有处于风险中的单位才可能经历事件），机械列变量不可能产生这句
- "since prior levels might influence subsequent changes as well as [the focal reaction]" 一句给整组控制变量统一 because：先验水平同时威胁主效应与反应测量，两个排除目标一句覆盖
- 指标引用链挂在各指标之后（cf. 式），清单本身保持可读——控制变量段的多源惯例对齐不牺牲叙事流

**适用**: 事件史/变化模型中控制"前一状态"的研究；某控制指标与某因变量在定义上互斥（未处于风险集的单位）的模型设定

**禁忌**: 风险集剔除必须真是定义性互斥（未合并职位的公司不可能分离），不能拿"理论无关"冒充定义互斥；剔除后需确认该指标仍在其余模型中出现，否则构成选择性报告

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 58: M3 DV 观察窗对齐治理决策钟 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: Recall count is the number of recalls initiated by a firm in the 12 months following the annual shareholder meeting, because this is when board composition is determined for the upcoming year.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M3

**骨架**:
> [DV] is the number of [events] initiated by a firm in the [window] following [the governance event that resets the predictor], because this is when [the predictor] is determined for the upcoming period. This approach measures the influence of [the predictor] on [events] initiated until [the next reset].

**与原骨架差异**: 区别于变体 54（lead-DV 泛化的一年滞后对齐 + 双理由子样本排除）——变体 54 把 DV 窗口锚到"IV 测量年的下一年"；本变体把窗口锚到**预测变量被决定的具体治理事件**（如年度股东大会重新选举董事会）并给出 because 解释，时间序论证从"滞后一年"细化到"治理决策钟"。亦区别于变体 35（DV 文献基准锚定）与变体 27（构念窗—结果窗分离）。

**诚实边界**: 窗口必须与真实决策钟一致；若预测变量在年内发生临时变动（如董事辞职），固定窗会稀释归因，应报告替代窗稳健性。

### 变体 15: M1 单行业设置 — 双重现象共存辩护 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: We chose the U.S. pharmaceutical industry as an appropriate setting for examining our hypotheses because it features both extensive alliance activities and competition for new products (Lichtenberg & Philipson, 2002; Mowery et al., 1996).
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M1
**骨架**:
> We chose [industry/setting] as an appropriate setting for examining our hypotheses because it features both [phenomenon A] and [phenomenon B] ([citation_1]; [citation_2]).
**与原骨架差异**: 单行业研究常用一句话完成情境正当化。关键：不罗列行业统计数字，而是点明两个与理论直接相关的现象在该情境中同时存在。Cui et al. 用 "extensive alliance activities" + "competition for new products" 同时激活 alliance 与 competition 两个理论前提。

### 变体 16: M2 多源 alliance 数据库合并与交叉验证 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: We constructed a more comprehensive alliance database by combining these three data sources. By relying on multiple sources, we minimized the possibility of double-counting alliances and of counting alliances that were announced but not realized.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M2
**骨架**:
> We first collected data on [alliances/relationships] within [industry] from [year_start] to [year_end], using [N] data sources—[source A], [source B], and [source C]—which (a) have very similar standards for reporting information, including [key fields], and (b) each normally reports only a fraction of all [activity] ([citation]). Although databases that track [activity] in [industry] are normally reliable ([citation]), we found that [source A] covers more [historical data], while [source B] and [source C] include more [recent information]. We constructed a more comprehensive [database] by combining these [N] data sources. For due diligence, we followed [citation], searching for [announcements/status reports] from [source D], [source E], and [source F]. Most [announcements] were cross-validated by at least two additional sources. By relying on multiple sources, we minimized the possibility of double-counting [alliances] and of counting [alliances] that were announced but not realized.
**与原骨架差异**: 在现有变体2（样本交集漏斗）基础上扩展为完整段落。关键要素：(1) 多数据库互补性说明；(2) 人工 due diligence（LexisNexis / 公司网站 / SEC filings）；(3) 交叉验证的两个明确目标：防重复计数、防 announced-but-not-realized。适用 alliance / network / contract 等多源合并场景。
**诚实边界**: 仍需报告关键中间匹配 N（如初始 alliance 条目、合并后条目、匹配 Compustat/FDA 后最终 dyad-year），否则仍落入"多数据库无漏斗"反模式。
**扩展（du_tsolmon2024 ORSC）**: 三层异质数据库漏斗 + 附录审计。本文示范了跨三层异质库（交易库→人员库→结构库）逐层交集的漏斗叙事：每层交集后报告 N（如 576K deals → 15,773 deals/43K managers → 2,941 deals/18,987 managers），主文只报层数与最终 N，**附录报告 match rate + 初始样本 vs 最终样本关键变量对比**（证明最终样本无系统偏差）。骨架补充："[After final merge], our estimation sample covers [N] [units]. Online Appendix [X] reports the match rates across all datasets used in constructing the estimation sample and the comparison of key variables between the initial sample ([N_initial]) and the final estimation sample ([N_final])." 适用：三层及以上异质数据库合并、需要兼顾主文简洁与可审计性的样本构建。


### 变体 62: M6 求而不得的控制变量 — 因变异不足主动弃用并声明 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: We also sought to control for CEO gender, but only two companies had female CEOs in our data set, so there was not sufficient variation in this measure.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M6

**骨架**:
> We also sought to control for [a theoretically expected covariate], but only [n] [units] had [the characteristic] in our data set, so there was not sufficient variation in this measure.

**与原骨架差异**: 区别于变体 40（控制变量双面 because）与变体 50（共线控制残差化）——本变体处理的是**审稿人预期会问、但数据无法支撑的控制变量**：不静默删除，而是"we sought to"主动声明纳入意图 + 给出弃用的数据原因，抢在审稿人质询前完成交代。

**诚实边界**: 弃用声明最好附一句被遗漏变量可能相关的方向判断；若该变量恰与核心预测变量相关（如女性 CEO 与女性董事比例），须在局限中承认残余混淆可能。

### 变体 17: M3 多维行为指标 → factor score → 平均值 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: We ran a factor analysis of these three items and found that all three loaded high (>0.73) on one latent factor, while the value of Cronbach's alpha is .81, which suggests that it is a reliable construct.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M3
**骨架**:
> [DV construct] describes both [dimension 1] and [dimension 2] of [actor]'s [behavior] ([citation]). This variable contains [N] items: [item 1], [item 2], and [item 3]. [Item 2] measures [definition]; [item 3] measures [definition]. [Item 3] is a more aggressive form of [behavior] than [item 2] because [theoretical rationale] ([citation]). We ran a factor analysis of these [N] items and found that all [N] loaded high (>[threshold]) on one latent factor, while the value of Cronbach's alpha is [value], which suggests that it is a reliable construct. We used the [average score] for these [N] items to measure the dependent variable.
**与原骨架差异**: 适用于多维行为 DV（如竞争攻击性 = 行动数量 + 宽度 + 深度）。关键：(1) 每个子维度的理论含义；(2) 子维度间的理论排序（如某维度更激进）；(3) factor loading + Cronbach's alpha；(4) 合成方式（平均值或 factor score）。与文本构念测量变体5（复合文本指标）互补——本骨架用于行为计数+定性深度组合。

### 变体 18: M7 dyad fixed effects + dyad 聚类标准误 + 具体混淆源举例 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: For example, if unobserved heterogeneities, such as the attractiveness of partners to one another and their tendencies to compete with each other, are constant within firm–partner dyads, then there might be an endogeneity concern. A fixed-effects estimator can rule out such a possibility by eliminating time-invariant heterogeneities.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We tested our hypotheses using fixed-effects models. The unit of analysis is [actor]-[partner]-[time], and we allowed a [N]-year lag between our predictor variables and the dependent variable. A fixed-effects estimator has superior controls for time-invariant variables ([citation]) and is an effective way to account for possible endogeneity problems. For example, if unobserved heterogeneities, such as [example 1] and [example 2], are constant within [dyad], then there might be an endogeneity concern. A fixed-effects estimator can rule out such a possibility by eliminating time-invariant heterogeneities. Fixed-effects models also allow us to account for intra-cluster correlations caused by multiple observations of the same [dyad] over time. We therefore employed [dyad] fixed-effects and clustered standard errors on [dyad] in our models.
**与原骨架差异**: 与变体7（嵌套横截面聚类 SE）互补。本骨架增加 dyad FE + 具体时不变混淆源举例（如 "attractiveness of partners to one another and their tendencies to compete"），让 FE 的识别价值从抽象变为可感知。关键：混淆源举例必须真实存在于研究情境中，而非泛泛而谈。
**诚实边界**: dyad FE 只能消除时不变遗漏变量；若存在时变混淆（如共同市场冲击），FE 无法识别因果。网络变量研究还需额外讨论反射性问题。

### 变体 19: M4 高管信心期权 moneyness 操作化 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: The average moneyness is defined as the ratio of average value per option to the average strike price. The constructs are measured with a lag relative to the measurement of the dependent variable to create temporal distance and maintain causal priority.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M4
**骨架**:
> We follow the finance and accounting literature and infer [actor] confidence from [actor]s' decisions about when to exercise company stock options ([citation]). The options-based measure uses archival data and is easily calculated from Execucomp, allowing us to examine executive confidence for a broad cross-section of firms over a long period ([citation]). [Actor] confidence is measured as the average moneyness of the exercisable options held by the [actor] in [year t]. The average moneyness is defined as the ratio of the average value per option to the average strike price ([citations]). The constructs are measured with a lag relative to the dependent variable to create temporal distance and maintain causal priority.
**与原骨架差异**: 高管信心的经典期权 moneyness 操作化。关键要素：(1) 理论直觉（自信高管延迟行使深度实值期权）；(2) 公式（average value/strike price of exercisable options）；(3) 滞后处理（避免薪酬同期受 DV 污染）。与 `micro-templates/executive-confidence-operationalization.md` 配套使用。
**诚实边界**: 必须说明该指标测量的是"基于财富的信念"而非心理学过度自信；必须报告滞后结构；样本中无 exercisable options 的高管需说明缺失值处理。

### 变体 20: M2.5 Model-Free Evidence 预览 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: We then calculate the mean and median MMM for the firms in each quartile. Consistent with H1, there is a monotonic increase in MMM from the first quartile where CEOs have the lowest level of confidence to the fourth quartile where CEOs are the most confident.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M2.5
**骨架**:
> Before presenting the model-based evidence, we provide model-free evidence on the relationship between [IV] and [DV]. We divide the sample into quartiles based on [IV] and calculate the mean and median [DV] for firms in each quartile. If [theory] holds, we should observe a monotonic [increase/decrease] in [DV] from the lowest to the highest [IV] quartile.
**与原骨架差异**: 在正式回归前用 quartile means/medians 展示无条件关系。关键：明确分位数基于 [IV]、报告 mean + median、说明预期模式（单调递增/递减）。适用于连续 IV 与连续 DV 的初步关系展示，增强读者对主效应方向的直观信心。
**诚实边界**: Model-free evidence 不能替代模型控制；必须在 Methods 中预告其探索性质，并在 Results 中明确与模型结果的对比。

### 变体 21: M7 三向交互模型设定 (1篇高价值)
**来源论文**: Chung, Low & Rust (2022, JAMS)
**原始句锚点**: For ease of interpretation of the interaction coefficients, we follow the recommendations of prior literature (e.g., Irwin & McClelland, 2001) and mean-center CEO confidence, CMO confidence, Board independence, and CMO power before including them in the regressions.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: M7
**骨架**:
> We estimate the following model: [DV] = β₀ + β₁[IV] + β₂[IV]×[W1] + β₃[IV]×[W1]×[W2] + β₄[IV]×[W2] + β₅[W1]×[W2] + β₆[W1] + β₇[W2] + Controls + ε. For ease of interpretation of the interaction coefficients, we mean-center [IV], [W1], and [W2] before including them in the regressions ([citation]). We include all two-way interactions and the constituent terms to avoid omitted-variable bias in the three-way interaction coefficient ([citation]). We cluster the standard errors at the [firm] level to account for heteroskedasticity and within-[firm] correlation ([citation]).
**与原骨架差异**: 三向交互的标准 Methods 写法。关键要素：(1) 完整模型方程（含所有 lower-order terms）；(2) mean-centering 声明；(3) 聚类 SE 层级。适用于 X × W1 × W2 设计。
**诚实边界**: 必须包含所有 lower-order terms；mean-centering 不影响系数解释但影响常数项；若 W1/W2 偏态，±1 SD 切割需改用实际分位数。
**跨 skill 对齐**: `write-theory/corpus/variants/E_moderation.md` E6（序列嵌套调节理论推导）；`../write-results/corpus/三向交互.md` 变体2（连续调节变量三向交互边际效应表）。

### 变体 22: M7 GEE + AR(1) working correlation — 时不变焦点 IV 的估计量选择论证 (1篇高价值)
**来源论文**: Abdurakhmonov, Ingram & Ridge (2026, JOM)
**原始句锚点**: We follow prior CEO political ideology research by employing generalized estimating equations (GEE) with robust standard errors (Chin & Semadeni, 2017; Chin et al., 2013) because of this model's appropriateness when including time-invariant variables such as CEO liberalism (Chatterjee & Hambrick, 2007; Quigley & Hambrick, 2012).
**验证状态**: EMERGING（单篇入库；GEE 在 corpus 中此前无独立变体）
**写入日期**: 2026-07-22
**槽位**: M7
**骨架**:
> Following prior [domain] research, we employ generalized estimating equations (GEE) with robust standard errors ([citations]) because of this model's appropriateness when including time-invariant variables such as [focal_time_invariant_IV] ([citations]). For all models, we specified an autoregressive (AR1) working correlation structure, with the [firm / unit] set as the panel unit, since it allows for the possibility that unobserved factors influencing [DV] may be correlated across adjacent [time periods] within the same [unit] ([citation]). To account for temporal and [industry / context]-specific effects, we included [year] and [industry] fixed effects in all analyses.
**与原骨架差异**: 与变体 10（Hausman FE vs RE）和变体 13（RE 三重辩护 theory+Hausman+ICC）互补而非重叠——两者基于 Hausman / ICC 选择 FE / RE；本变体基于 **焦点 IV 的时不变性** 选择 GEE。当核心 IV 是时不变稳定特质（CEO 政治意识形态、人格、创始人身份、性别、教育背景等）时，firm FE 会吸收或丢弃该变量使主效应无法识别。GEE 提供第三条路径：(1) AR(1) working correlation 建模序列相关；(2) robust SE 校正规范误；(3) year / industry FE（而非 firm FE）吸收时间 / 行业冲击而保留 focal IV。关键三要素：① 显式说明"因 focal IV 时不变，firm FE 不适用"；② working correlation structure 选择依据（AR1 = 时间相邻期相关；exchangeable = 同单元任意两期等相关）；③ FE 声明（year / industry 而非 firm——因 firm FE 再次吸收时不变 IV）。
**诚实边界**: 必须显式声明不使用 firm FE 的理由（"because [focal_IV] is time-invariant, firm FE would absorb it"），不能默默省略；working correlation structure 选择应说明依据，不能默认 AR1；GEE 是 population-average 估计器，与 RE（subject-specific）在系数解释上有重要区别，应说明是 marginal effect 而非 unit-specific effect；firm FE 不可用时应在 M8 / Limitations 诚实说明残余威胁（time-varying unobservables 仍可能混淆），并通过 IV / Heckman / matching 补强。
**适用**: 焦点预测变量为时不变稳定特质（政治意识形态、人格、性别、出生地、教育背景、创始人身份）的 panel 研究；任何 firm FE 会"杀死"主效应的情境。
**跨 skill 对齐**: `../write-results/corpus/OLS-FE.md`（稳健性中可用 LPM + firm FE 作方向性对照，但主模型用 GEE 保留时不变 IV）。


### 变体 72: M6 同构替代目标控制 — 同一构念对同类目标重算以封堵"普遍信念"替代解释 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: As the relation between rival– (target firm–)MSCI CIO and MSCI ESG rating might be driven by investors' beliefs in the value of ESG, we controlled for rival–other agency CIO ... to capture common ownership in other publicly traded ESG rating agencies.
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-09-05
**槽位**: M6
**骨架**:
> As the relation between [IV] and [DV] might be driven by [actors'] [general beliefs/preferences] in the value of [DV domain], we controlled for [unit]–[other target] [construct] and [focal unit]–[other target] [construct] to capture [the same construct] with respect to [other publicly traded members of the same target class].[^n（脚注枚举替代目标名单）]

**与原骨架差异**: 区别于变体 37（rival 镜像控制——同一变量聚合到对手侧、同一目标）与变体 40（双面 because）——本变体是**同构（isomorphic）而非镜像（mirror）**：把 focal 构念原式重算到**同类替代目标**上入模。说服逻辑：若效应来自"行为者对该机构类别的普遍信念/偏好"（omitted variable），同构控制应吸收之；focal 构念在控制后仍有解释力，则支持理论化的**特定目标**机制。一句话完成（点名替代机制 + 同构重算 + 脚注列名单），把本应放 robustness 的 placebo 式检验前置为 baseline 控制。
**诚实边界**: 前提是存在可测同一构念的同类替代目标（其他上市评级机构/媒体/认证方）——目标类稀缺时不可用；同构控制吸收的是"类别层面普遍信念"，若替代解释是"对某替代目标本身的特定偏好"则需对该目标逐一控制；控制入模后 focal 系数解释变为"net of 类别信念"效应，Results 须相应措辞。

**适用**: 第三方中介/评估者设计（评级、认证、媒体、审计、分析师）中"行为者对整个机构类别有普遍偏好"类替代解释的封堵；亦可推广为 sibling-target placebo 控制。

<!-- wb:desjardine_2025_information_based_competition_the_case_of_ri:isomorphic_alternative_target_control -->

### 变体 23: M1 行业统计 + 先例对齐的设置辩护 (1篇高价值)
**来源论文**: Pupovac, Astvansh, Carrillat & Legoux 2026 (POM)
**原始句锚点**: Measuring recalls' contagion from a manufacturer-customer to a supplier requires an empirical setting in which manufacturers and suppliers are interdependent in the product market (Cho et al., 2021). The automotive industry meets this requirement because suppliers produce 70% of an automobile, on average (McGee, 2017), suggesting high interdependence.
**验证状态**: VERIFIED（单篇高价值）
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
**验证状态**: VERIFIED（单篇高价值）
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
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-25
**槽位**: M3
**骨架**:
> Our [first] dependent variable is [DV]. Following prior work, we measure [DV] as [operationalization] ([citation]). For example, if [concrete numerical example], the [unit] would have a [DV] of [value]. The mean [DV] in our sample is [X]%, which is comparable to the mean [DV] found in [N] prior empirical studies on [phenomenon]: [Y]% in [Author] ([year]), who examined [sample 1], and [Z]% in [Author] ([year]), who examined [sample 2].
**与原骨架差异**: 面板数据-OLS 现有变体无 DV 外部效度锚定。本变体三要素：(1) **具体数值示例**（5→3=0.60）让操作化可想象；(2) 报告样本均值；(3) **与 2+ 篇前人文献的均值对比**建立 DV 跨样本可比性——把"我的测量"锚定到"领域基准"。一句话完成外部效度论证，比单独报告均值更有说服力。适用于新构建的比率/计数 DV（retention rate、turnover、disclosure rate、adoption rate 等）。
**诚实边界**: 前人研究样本/时代/情境不同需说明（若本文是全球样本而前人是美国样本，需交代可比性边界）；均值可比不代表分布可比，若分布形状关键需补充。

### 变体 26: M2 跨库手工匹配（无共同标识符）+ 多源漏斗 (1篇高价值)
**来源论文**: Malshe & Agarwal (2015, Journal of Marketing)
**原始句锚点**: We obtained firms' financial information on balance sheets, income statements, and cash flow statements from S&P's Compustat database. Because there is no common firm-level identifier between the ACSI and Compustat, we manually matched ACSI brands belonging to corresponding Compustat firms.
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-30
**槽位**: M2
**骨架**:
> "We assembled a data set using multiple sources, including [source 1], [source 2], [source 3], [source 4], and [source 5]. [Table] provides a description of these variables and the source of the specific data items. We obtained [financial data] from [database A]. Because there is no common [firm-level] identifier between [database A] and [database B], we **manually matched** [database B units] belonging to corresponding [database A entities]. Because one of our research questions pertains to [shareholder value], we retained only those [firms] that are [publicly listed] at any time during our sample period. We obtained [market data] from [database C]. Finally, we obtained [ownership data] from [database D] and derived [other ownership] from [database E]. After we merged the [N] data sets and removed [M] [firm-year] observations pertaining to [excluded segment, e.g., financial firms], our final sample consisted of [N_final] [firm-year] observations spanning a [Y]-year period ([year_start]–[year_end]) for which all the relevant variables have nonmissing values."
**与原骨架差异**: 区别于变体16（多源 alliance **自动**交叉验证）与变体2（逐步样本交集漏斗）——本变体处理两个核心数据库**无共同标识符**的硬情况（如 ACSI 品牌与 Compustat 企业无公用 firm ID），须**手工匹配**（manually matched）下游单位到上游实体。三要素：(1) 五库多源 + 每变量的数据源声明表；(2) **手工匹配的明示**（不可假装自动 merge）；(3) 合并后漏斗（合并 N 库 → 排除 M 个 [金融行业] 观测 → 最终 N_final，且限定"上市"以配合股东价值 RQ）。配套反模式（见"多数据库无漏斗"）：即便无法逐步漏斗，也须报告关键交集 N。适用于营销-金融、营销-会计等跨职能多源面板（ACSI/Compustat/CRSP/ExecuComp/Thomson Reuters 组合）。
**诚实边界**: 手工匹配的匹配率与匹配规则须报告（多少 brand 成功匹配到 firm？规则是否可复现？）；限定"上市"会引入生存偏误（上市公司更大更老），须在 limitation 讨论。

### 变体 27: M4 构念形成窗—结果观察窗分离 + 双代理收敛 (1篇高价值)
**来源论文**: Schumacher, Keck & Tang (2020, Strategic Management Journal)
**原始句锚点**: We employ two separate measures of overconfidence derived from the prior literature to test our hypotheses. This helps us to ensure that our findings are not driven by the idiosyncrasies of any specific measure of CEO overconfidence and to overcome some of the limitations that each individual measure might have.
**验证状态**: EMERGING（单篇入库）
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
**验证状态**: VERIFIED（单篇高价值；与变体22共同验证 GEE 的可迁移性，但选择理由不同）
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

**跨 skill 对齐**: `../write-results/corpus/Logit-Probit-Ordered-Probit.md` 变体9–11（正式 U-test、条件曲线概率图与经济成本换算）；`../write-theory/corpus/subprotocols/hypothesis_derivation_patterns.md`（two-phase curvilinear argumentation）。



### 变体 61: M7 FE 去均值选择 + 时不变因素按设计吸收 + 组内系数解读协议 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: The regression coefficients in our results are interpreted as the effect of increasing FBR, within a firm, across time, on changes in future recall measures within a firm, across time.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M7

**骨架**:
> Because our data contain repeated measures across time for the same [unit], we use a FE demeaning regression approach. Panelized data enable demeaning, which reduces time-invariant omitted variable bias leading to endogeneity. Factors that do not change across time for a given [unit], such as [a unit indicator], are accounted for by design in such models and are thus not included. Because we use an FE model, we are conducting a within-[unit] analysis, which influences how we interpret coefficients: the regression coefficients are interpreted as the effect of increasing [the predictor], within a [unit], across time, on changes in [the outcome] within a [unit], across time. In other words, our model, by design, examines how changing [the predictor] within a [unit] influences how that [unit] makes subsequent [decisions].

**与原骨架差异**: 区别于变体 47（一阶差分）与变体 4（mixed within/between 机制分解）——本变体是**FE 去均值路线的三拍论证**：选择理由（重复测量→去均值消时不变 OVB）→"时不变因素按设计吸收故不纳入"的省略辩护→系数解读协议（显式把 coefficient 语言限制在 within-unit across-time 变化上），最后一句"In other words"把识别语义翻译回理论问题。

**诚实边界**: FE 吸收全部组间变异，结论只覆盖组内变化的效应；不得升级为跨单元比较主张；非线性 FE（如 negative binomial FE）的条件估计在计量上有争议（Allison & Waterman 批评），应引用正当化来源并准备 PQR/线性概率替代检验。

### 变体 59: M3/M7 证据架构服从决策拆分 — DV 按严重度分组 + 假设→符号预登记 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: Support for Hypothesis 1 would be indicated by a positive and significant beta coefficient for FBR on class 3 recalls, whereas support for Hypothesis 2 would be indicated by a negative and significant beta coefficient for FBR on class 1 time-to-recall.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M3（配合 M7 估计器分配）

**骨架**:
> To test our hypotheses, we distinguish our dependent variables by [severity dimension]: the [initiation margin] is observed as a prospective count of [low-severity events], whereas the [timing margin] is observed as the interval between [when the firm first became aware of the problem] and [when it acted] for [high-severity events]. This approach is similar to other [event] studies that segregate the dependent variable to examine [severity]. We test all [severity classes] for completeness. Support for [Hypothesis 1] would be indicated by a [positive] and significant coefficient for [the predictor] on [subgroup A], whereas support for [Hypothesis 2] would be indicated by a [negative] and significant coefficient on [subgroup B].

**与原骨架差异**: 区别于变体 53（ball_2018 型 severity-split）——变体 53 在**同一 DV 类型内**按官方严重度分配子样本实现调节假设对（H2a/H2b）；本变体则让**不同决策边际换不同 DV 类型**（发起边际→前瞻计数；时机边际→知晓到发起区间）并配不同估计器，且追加"Support for Hypothesis X would be indicated by a [sign] and significant coefficient"的假设→符号预登记句，使 Results 的配对呈报不会被误读为"普遍多召回/普遍更快"。亦区别于变体 29（severity 作为单个 DV 的二元操作化）。

**诚实边界**: 子群拆分必须映射到**理论上真实不同的决策边际**，不能从任意子群制造两个故事；拆分会缩小单元格数量，需报告子群样本量；"for completeness"的补充检验不承担假设检验功能。

### 变体 29: M4 召回严重度理论分类 — 后果类型二元操作化 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: To measure the effects of the severity of product recall, we classify two severity types based on the consequence of product failure described in the data. Severity type 1 product recalls, which increase the chance of crash or fire, involves an immediate safety concern.

**验证状态**: VERIFIED（单篇；与 Kashmiri 2017 severity 边界声明互补）

**槽位**: M4

**骨架**:
> To measure the severity of [product-harm event], we classify events into two types based on the consequence of product failure described in [regulatory/administrative data]. [Severity type 1] events [increase immediate catastrophic risk — e.g., crash or fire] and reflect an immediate safety concern; an example is [defective brake pedal]. [Severity type 2] events [increase injury risk conditional on an exogenous accident — e.g., airbag/seatbelt failure when crash is not caused by the defect] and therefore may trigger less negative consumer response than type 1. [Severity_it] equals one for type 1 and zero for type 2. In our sample, [percentage]% of events are type 1 and [percentage]% are type 2.

**与原骨架差异**: 召回家族现有 time-to-recall、裁量权子样本（Hoffmann）与 regulatory indicator（Kashmiri）；本变体把 **NHTSA 后果描述 → 心理学归因可辩护的二元 severity** 写进 M4，并给每类一个可想象例子 + 样本占比。

**诚实边界**: 二元分类损失 severity 连续信息；须在稳健性报告 alternative coding 或 include continuous units recalled。

---

### 变体 30: M4 媒体覆盖 — 双索引相关度阈值 + 互补数据源 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: LexisNexis assigns a relevancy score for each index (e.g., product recall) of each article. We use this score to ensure the articles do indeed discuss the recall events of the firm of interest and that they are not incidental mentions.

**验证状态**: VERIFIED（单篇；待与 `文本构念测量` 交叉验证）

**槽位**: M4

**骨架**:
> We obtain print media reports about [events] from [LexisNexis/Factiva]. We search [all major outlets / firm name within study window] using two index terms: ["product recall" as subject] and [firm name as company tag]. [Provider] assigns a relevancy score for each index in each article; we retain articles only if relevancy scores for both indices are at least [threshold: e.g., 60%], ensuring discussion concerns the focal firm's [events] rather than incidental mentions. We complement [provider A] with [provider B: e.g., Wall Street Journal via Factiva company/subject tags] using parallel exclusion rules for irrelevant articles. [Media_ijt] is the count of qualifying articles in [period t] for [unit ij].

**与原骨架差异**: 区别于 generic media count——本变体强制 **双索引 relevancy 阈值** 作为 face-validity 链，并写 **双数据源互补** 与 irrelevant-mention 排除逻辑。召回 shock 研究可复用。

**诚实边界**: 阈值（60%）为 judgment call，须报告敏感性；print-only 遗漏 social/streaming 渠道。

---

### 变体 31: M2/M4 异频数据时间对齐 — 事件聚合至结果频率 (1篇高价值)

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: To fully utilize the monthly sales and advertising data, we aggregate the product recall data for each month and each car nameplate. Although all car characteristics and price data are annual, the advertising expenditures and product recall data are monthly.

**验证状态**: VERIFIED（单篇）

**槽位**: M2 / M4

**骨架**:
> [Sales/advertising/outcome data] are observed at [monthly] frequency, whereas [event registry data] are recorded at [event/day level] and [product characteristics/prices] are [annual]. To utilize the high-frequency marketing and outcome data, we aggregate [event counts/intensity] to [monthly unit-level totals] (e.g., total units recalled per month per [nameplate]). Annual [characteristic/price] variables are held constant within year but enter the [monthly] demand system with [CPI deflation / interpolation rule stated explicitly].

**与原骨架差异**: 面板 OLS 变体2/26 强调多库交集 N；本变体解决 **event-day vs month vs year 三频对齐**——Marketing/IO 面板常见但未在召回语料显式化。

**诚实边界**: 月内事件堆叠假设事件效应在月内可加；年度价格仅 CPI 月变会低估 within-year price variation——须 limitation 承认 MSRP 代理限制。

### 变体 32: M4 结构二元特征操作化为「kind」而非「degree」— 相对 majority-independence 的 discrete construct (EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: Our independent variable is whether the focal board of directors was a lone-insider board. To capture the most conservative specification, we coded firms as "1" if the CEO was the only inside or affiliated member on the board; other board structures were coded as "0."
**验证状态**: EMERGING（单篇）
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
**验证状态**: EMERGING（单篇）
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
**验证状态**: EMERGING（单篇）
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
**验证状态**: EMERGING（单篇）
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
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: M4
**骨架**:
> Our independent variable, [composite IV], captures [construct definition]. After obtaining [ownership data] from [source], we retained [actors] that owned more than [threshold]% of outstanding shares in each firm because such investors have been shown to have sufficient incentives and power to actively [intervene] ([citations]). [Feasibility argument: the average number of [actors] above the threshold is [N], making it feasible for [target actors] to be aware of each large [actor]]. We used the following formula to calculate [composite IV]: [formula]. For each [unit]'s [rival] pairs, we first calculated [step 1: within-actor aggregation], then computed [step 2: product across the two sides], and then calculated [step 3: aggregation across rivals].

**与原骨架差异**: 现有 M4 变体（三层 because、moneyness、阈值披露）——本变体是**复合乘积构念的分步构建**：①阈值辩护（1% → 激励权力 + 引用）②可行性论证（平均 N 家 → 高管可知晓每家）③分步计算（先内部聚合 → 再跨侧乘积 → 再跨对手平均）。适用于两个持有侧乘积/交集型复合构念（共同所有权、重叠关系、跨市场关联）。
**诚实边界**: 阈值选择须有文献依据；可行性论证（"average N makes it feasible for executives to be aware"）须与机制一致——若理论不依赖知晓，可行性论证是加分项而非必需；分步公式须与 Results 变量定义完全一致。

**适用**: common ownership、共同持股、双角色重叠、跨侧乘积构念的研究。

---


### 变体 73: M5 共有制子集镜像调节 — 聚合域限定为理论激活的传导子集 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: We measured rival ESG media controversies as the average value of ESG media controversies among rivals with common institutional ownership with MSCI.
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-09-05
**槽位**: M5（镜像调节对：H2a/H2b、H3a/H3b 双侧）
**骨架**:
> For [H2a] and [H2b], our moderators are [rival-side construct] and [target-side construct], respectively, which capture [the reputational force] faced by [portfolio firms] and [target firms] based on their [domain activities]. Following existing studies ([citation]), we used [database] to construct these variables. [Database] screens [N] [sources] to detect [issue types] ... We used this coding to measure [target-side construct] as [operationalization] in each [unit-year]. We measured [rival-side construct] as the average value of [the construct] among [rivals with common institutional ownership with the intermediary].

**与原骨架差异**: 区别于变体 37（镜像控制——聚合于全部 FIC-100 对手、用于 M6 控制）——本变体用于 M5 调节，且**聚合域限定为共有制子集**（rivals with common ownership with the intermediary，非全部对手）：只有与中介机构有共同所有权的对手才在传导链上，聚合域本身携带理论。与变体 42（调节 dummy 效度链）的区别：本变体调节变量是连续/百分比聚合量，效度由数据库编码能力（severity×reach 加权）承担。同一构念 target 侧与 rival 侧操作化可不对称（ln 加权计数 vs 子集均值百分比）。
**诚实边界**: 子集镜像使调节变量与 IV 共享同一对手集合，共线风险升高（子集大时趋近全对手均值）；须报告子集镜像与全对手镜像的相关或并报全对手版本稳健性；双侧操作化不对称（计数变换 vs dummy）时交互解释须注明量纲。

**适用**: 多行为者中介设计（共同所有权、银团、连锁董事、分析师覆盖）中调节经由"特定连接子集"传导的研究。

<!-- wb:desjardine_2025_information_based_competition_the_case_of_ri:common_owner_subset_moderator_mirror -->

### 变体 37: M6 rival 镜像控制变量惯例 — 引用前例 + 命名规则 + 聚合方式 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: To address cross-rival effects on ESG ratings, we followed Guo, Sengul, and Yu (2020) to control for rival characteristics, denoted by the word "rival" (e.g., rival firm slack). Each variable is measured as the average value among all rivals identified by the FIC-100.
**验证状态**: EMERGING（单篇）
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
**验证状态**: EMERGING（单篇）
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

### 变体 41: M1 数据可得性挑战→独特档案数据集设置辩护 (1篇高价值) (2026-08-12)

**来源论文**: Fini, Jourdan & Perkmann (2017, *Academy of Management Journal*)

**原始句锚点**: "Studying how industry evaluation affects the peer evaluation of academic scientists is challenging in terms of data requirements. While awarded grants may be known, data on unsuccessful grant applications are often neither disclosed by the funders, nor reported by the scientists."

**验证状态**: EMERGING

**写入日期**: 2026-08-12

**槽位**: M1

**骨架**:
> Studying how [IV] affects [DV] is challenging in terms of data requirements. While [the observable part of the outcome — e.g., awarded grants] may be known, data on [the censored/unreported part — e.g., unsuccessful applications] are often neither disclosed by [the funding body / regulator], nor reported by [the actors]. We therefore assembled a unique archival dataset covering [population] over [period]. [Setting rationale: this institutional arena combines [tension_1 — e.g., scientific-excellence logic] and [tension_2 — e.g., commercialization mission], making it an ideal context to observe [multi-audience evaluation] ([citation]).]

**与原骨架差异**: 现有 M1 变体为单行业设置（变体 15 双重现象、变体 23 行业统计+先例、变体 33 单一中介机构 a/b/c）——本变体是**数据可得性挑战驱动**的单组织/单一评价领域设置合法性：DV 的关键部分（未成功申请）被 censored 或未披露，迫使研究者自建独特档案数据集；末句用双制度张力（而非"最大/最有影响力"中介属性）锚定情境的理论价值。适用于以单一组织（大学、平台、监管体）为情境、结果变量部分不可观测、须自建数据的研究。主识别叙事（Poisson GMM）见 非线性模型 变体16。

**诚实边界**: 单组织情境的外推须留给 Discussion（跨组织一般化不是 Methods 声明）；censored/未披露的部分无法从档案验证，估计只对可观测子样本成立；数据可得性驱动必须与理论选择绑定——若只是"恰好有这家组织的数据"而非"这家的制度张力恰好检验理论"，本骨架不适用。

---

### 变体 42: M5 调节 dummy 的外部效度链 — 外部连续学科测量 + 定性锚定 (1篇高价值) (2026-08-12)

**来源论文**: Fini, Jourdan & Perkmann (2017, *Academy of Management Journal*)

**原始句锚点**: "To operationalize identity proximity with industry, we selected a measure that indicates a candidate's membership in a disciplinary grouping rather than an individual measure of proximity, because grant applications are evaluated by members of those broader disciplinary groupings... We validated the identity proximity variable by using a discipline-specific measure of proximity based on university–industry collaboration intensity (Tijssen 2012)."

**验证状态**: EMERGING

**写入日期**: 2026-08-12

**槽位**: M5 / M7

**骨架**:
> To operationalize [moderator], we selected a measure that indicates a [unit]'s membership in a [grouping] rather than an individual measure of [proximity/attribute], because [outcome decisions] are evaluated by members of those broader [groupings]. [Moderator] equals one for [definition of the =1 group: e.g., engineering and medicine] and zero otherwise. We validated [moderator] by using an external continuous measure of [proximity] based on [university–industry collaboration intensity] ([citation]); across the [groups], the external index takes values of [0.071, 0.061, 0.046, 0.039], consistent with the ordering implied by our dummy. We corroborated the grouping boundary through [interviews / expert validation], which confirmed that the [theoretical boundary condition] aligns with the observed classification.

**与原骨架差异**: 现有 M5 变体处理机制分解（变体 4 within/between、变体 5 机制对齐矩阵）与估计器曲线链（变体 28 GEE）——本变体是**调节变量测量本身的构造效度链**：①二分依据（评价由更宽学科组成员执行）；②外部连续学科测量（Tijssen U-I 强度）逐组给出数值验证顺序；③访谈定性锚定边界。回应审稿人对"自造调节 dummy 的二分凭什么成立"的质疑。适用于身份 proximity、受众类别、制度距离等自造调节分类的研究。

**诚实边界**: 外部效度测量的数据窗口可能在样本窗之后（如 Tijssen 2009–2013 验证 2001–2012 样本）——须声明属事后锚定并说明为何仍相关；dummy 二分损失连续 proximity 的信息，稳健性应报告连续版或替代阈值；外部指标只佐证构念效度，不替代理论边界论证（"为什么正好是这两组"）。

---


### 变体 43: M2.5 理论–测量–模型两步滞后链 + 年内再编码学习窗 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "A rigorous test of our hypotheses requires a close alignment of the theory, measures, and empirical model. We followed two steps to achieve this."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M2.5

**骨架**:
> A rigorous test of our hypotheses requires a close alignment of the theory, measures, and empirical model. We followed two steps to achieve this. First, we model the impact of [IV] in time period [t-1] on [mediator] in time period [t] and [DV1] and [DV2] in time period [t+1]. The temporal separation enables us to test the hypothesized chain of events after [the shock]. Second, we classified the [period] of [event] according to whether they occurred in the first or second half of the [period]. This classification implies that the time window between [event] and future [mediator] is between [min] and [max] [months]. In summary, our data setup and lag structure (1) ensures that there is sufficient time lapsed after [event] for [mechanism] and (2) allows the results to be interpreted as Granger causality.

**与原骨架差异**: 区别变体 39（单句 DV t+1 / IV t spacing）——本变体是冲击→中介→下游结果的两步对齐，并含年内再编码学习窗。滞后结构只支持 Granger 口径，不是正式 Granger 检验。

**诚实边界**: 未做正式 Granger 检验时，第二句不得写成因果识别完成；年内再编码是学习窗操作，不是外生冲击。


### 变体 44: M2 纳入零事件年作为单元自对照 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "including both types of make/years obviates the need to assemble a control sample. In other words, each make serves as an implicit control for itself."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M2

**骨架**:
> Our balanced panel of [N] [unit]/[period] observations includes [N_event] [unit-periods] when [event] occurred as well as [N_zero] [unit-periods] when [event] did not occur; including both types of [unit-periods] obviates the need to assemble a control sample. In other words, each [unit] serves as an implicit control for itself. This benefit makes panel data well suited for [within-unit comparisons] in comparison with purely cross-sectional designs ([citation]).

**与原骨架差异**: 区别变体 2（逐步排除漏斗）与变体 28（GEE 保留全零是为估计器）——这里是识别逻辑：零事件年让每单元成为自身对照。骨架用 within-unit comparisons，不用 drawing causal inferences。

**诚实边界**: 平衡面板自对照不是准实验识别；不得把 panel vs CS 写成 drawing causal inferences。


### 变体 45: M3 数据源隔离理论相关事件 vs 伴生混淆事件 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "This data source enables us to isolate injuries attributable to vehicle-related problems and exclude accidents that occurred due to driver-related problems."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M3

**骨架**:
> We assembled [DV] from [source]. This data source enables us to isolate [outcome] attributable to [construct-relevant cause] and exclude [outcome] that occurred due to [confounded cause]. Again, we normalized this variable by [scale denominator] of the [unit] in the previous [period].

**与原骨架差异**: 区别变体 25（用前人均值锚定新 DV）——本变体用数据源能力把理论相关事件从伴生混淆事件中剥离，否则中介无法对应 DV。

**诚实边界**: 隔离只保证构念通道，不保证外生；须声明仍可能有未观测的同通道混淆。


### 变体 46: M5 反向原始指标的 z 分复合调节 + 反向编码 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "Lower (higher) scores on these indicants imply greater (lesser) sharing of product assets. For example, an automaker with fewer manufacturing plants, fewer platforms, a narrower range of engine sizes, and fewer models implies greater sharing of product assets."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M5

**骨架**:
> To operationalize [moderator], we collected data on [K] indicants: ([1]) [indicant_1], ([2]) [indicant_2], ([3]) [indicant_3], and ([4]) [indicant_4]. These [K] indicants reflect the extent to which [units] would be able to [mechanism]. Lower (higher) scores on these indicants imply greater (lesser) [construct]. For example, [concrete illustration of the reverse direction]. Because the range and spread of scores on each of these indicants is different, we computed z scores for each indicant by [unit] and [period]. The sum of z scores on the [K] indicants is our measure of [moderator] (for an alternate measure, see [robustness location]). We reverse-coded the measure for ease of interpretation; therefore, higher (lower) z scores reflect higher (lower) levels of [construct].

**与原骨架差异**: 区别变体 42（自造 dummy 外部效度链）与变体 36（乘积型复合）——本变体是原始指标与构念方向相反时的 z 分求和 + 反向编码。

**诚实边界**: 部分 indicant 可能与规模相关；须在稳健性中丢掉疑似规模指标。方向逻辑必须先于标准化。


### 变体 47: M7 一阶差分变化规格（消未观测效应 + 避伪回归） (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "The advantage of first-differencing is that it eliminates unobserved effects (see Boulding and Staelin 1995; Kim and McAlister 2011; Mizik and Jacobson 2007) and avoids the spurious regression problem (Granger and Newbold 1974)."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M7

**骨架**:
> We transform [levels equation] into a change specification by applying the first-differencing operator. The advantage of first-differencing is that it eliminates unobserved effects ([citations]) and avoids the spurious regression problem ([citation]). Because the first-differencing accounts for [unit]- and [cluster]-specific time-invariant fixed effects, the terms [unit FE] and [cluster FE] are no longer needed in the preceding equation. To control for time-specific unobserved effects, we include dummies for [period].

**与原骨架差异**: 区别变体 10（水平 FE dummy）与自然实验-DiD 变体10（ΔV 写成截面 DiD 等价）——本变体是水平方程之后的 FD 变化规格。

**诚实边界**: FD 消除时不变混淆，不创造外生变异；骨架不写 effect of。FD 后 LDV 内生须另工具化（见动态面板-GMM 变体 5）。


### 变体 48: M8 误差结构三诊断 → IGLS (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "In summary, the estimation must account for first-order serial correlation, cross-sectional dependence, and heteroskedasticity in Models 1b, 2b, and 3b. ... we use the iterative generalized least squares (IGLS) estimator"

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M8

**骨架**:
> Last, there are a few econometric issues pertaining to the error structure in [equations] that need to be addressed. First, it is possible that first-differencing does not eliminate autocorrelation because of the presence of the lagged dependent variable. We tested for first-order autocorrelation. The [Wooldridge AR test] for [each equation] is [stat] (p < [threshold]). This confirms the presence of first-order serial correlation. Second, because the data comprise [N nested units] of [N clusters], there is likely to be cross-sectional dependence between [nested units] of the same [cluster]. For example, [concrete pair]. We test for cross-sectional dependence using the [Breusch-Pagan LM test] ([citation]). These tests indicate that there is cross-sectional dependence in the data. Third, we tested for the presence of heteroskedasticity in the panel errors. These findings suggest the presence of panel-level heteroskedasticity. In summary, the estimation must account for first-order serial correlation, cross-sectional dependence, and heteroskedasticity. Following procedures advocated in previous research ([citations]), we use the iterative generalized least squares (IGLS) estimator and specify a heteroskedastic, spatially and serially correlated error structure (for an alternate estimator, see [robustness location]).

**与原骨架差异**: 区别变体 8（回顾性偏差三角）与 GEE 变体 22/28（先验 working correlation）——本变体是点名三诊断后再选 IGLS。

**诚实边界**: IGLS 是效率修正，不是识别策略；须预告替代估计器（PCSE）。嵌套举例必须真实（如同一母公司下的两个 make）。

### 变体 49: M5 职能高管权力：有职位薪酬比，无职位编码为 0 (2026-08-13)

**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (*Entrepreneurship Theory and Practice*)
**原始句锚点**: "If there is a COO, we calculated their power by dividing the COO's total remuneration ... by the total remuneration of the CEO. Firms without a COO were coded as [0]—as COO power was not present inside the organization."
**验证状态**: EMERGING
**写入日期**: 2026-08-13
**槽位**: M5
**骨架**:
> To test our moderating argument in [H2] regarding [functional-executive] power, we follow prior research and use compensation as an observable indicator of executive power ([citation]). Indeed, the link between executive power and compensation is unequivocal in the literature and therefore represents a valid structural proxy ([citation]). First, we identified whether [units] had an executive in the [TMT] with a [title]. If there is a [title-holder], we calculated their power by dividing the [title-holder]'s total remuneration by the total remuneration of the [CEO]. [Units] without a [title-holder] were coded as [0]—as [role] power was not present inside the organization.
**与原骨架差异**: 变体 42=调节 dummy 外部效度链；变体 46=多指标 z 分复合。本变体=缺席=0 的结构权力代理。
**诚实边界**: 薪酬比是结构代理，不能写成质量倡导、注意力或决策权重的直接证据。

### 变体 50: M6 共线控制残差化 — 构念对另一控制回归后取残差 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "To cope with the correlation between company size and reputation, we regress the reputation scores on company size and use the residuals as the measure of reputation (Reputation)."
**验证状态**: EMERGING
**写入日期**: 2026-08-13
**槽位**: M6
**骨架**:
> To control for the potential impact from [construct], we follow previous research ([citation]) and include the [raw scores] from [source]. To cope with the correlation between [collinear covariate] and [construct], we regress the [construct] scores on [collinear covariate] and use the residuals as the measure of [Construct].
**与原骨架差异**: 变体 1/14/40 解决的是 because 密度与双面理由；变体 37 是对手镜像控制。本变体是共线处理：两个控制都要保留时，把焦点构念对共线协变量回归，用残差进入方程。
**诚实边界**: 残差化丢掉与 [collinear covariate] 共享的构念变异；不得把残差系数解释为原始构念的全效应。残差化不是识别策略。


### 变体 51：M1 制度冲击型 setting 三重理由论证（ball_2018 型，gap HIGH）
- **出处**: ball_2018 (SMJ)，产品召回面板，band=gap HIGH
- **槽位**: M1 研究情境
- **可迁移性**: 高（通用 setting 论证的制度冲击变体）
- **区别于**: 通用 setting 论证 — 本变体三理由功能分工明确：制度设计制造理论变异 / 共同监管降噪 / 结果利害重大
[骨架]:
[Empirical setting] was selected as our setting for [N] reasons. First, [institution/policy], and [its specific mechanism] in particular, was specifically designed to [create the theoretically relevant variation], thus creating a unique and ideal setting to answer our research questions. Second, [regulatory commonality] helps reduce spurious sources of variation across firms. Third, [outcome salience] makes [DV process] critical in this sector.
- **原始句锚点**（ball_2018 原文）: "We selected the pharmaceutical industry as our setting for three reasons. First, the Hatch-Waxman Act in general, and the ANDA process in particular, was specifically designed to increase product competition..."


### 变体 52：M3 构念边界排除 — 排除替代结果类别并预告 falsification DV（ball_2018 型，gap HIGH）
- **出处**: ball_2018 (SMJ)，产品召回面板，band=gap HIGH
- **槽位**: M3 因变量操作化
- **可迁移性**: 中（适用于构念下含多个结果类别、需论证主 DV 构念纯度的设计）
- **区别于**: 变体 35（M3 离散化等级 DV 边界距离操作化）— 本变体不是 DV 分级，而是在二分结果类别中论证被排除类别与 IV 结构性无关，从而确立主 DV 并预告 falsification DV
[骨架]:
[Construct] has two primary categories of [outcomes]: [target category] and [excluded category]. [Excluded category] stems from [alternative cause] rather than [target process]. While [treated units] can experience [excluded category], we contend it is unlikely these [outcomes] are influenced by [IV], as [structural constraint]. [Authority], however, provides considerable flexibility as it pertains to [target process]... Because [constraint], the [target process] is an intuitive place for firms to compete, and this is why we use [target DV] as our primary dependent variable.
- **原始句锚点**（ball_2018 原文）: "While ANDA drugs can be recalled due to design issues, we contend it is unlikely these recalls are influenced by product competition, as firms cannot meaningfully change the drug's design from the original, pioneer drug."


### 变体 53：M3/M5 调节假设以 DV 官方分级拆分实现 — severity-split 配对假设（ball_2018 型，gap HIGH）
- **出处**: ball_2018 (SMJ)，产品召回面板，band=gap HIGH
- **槽位**: M3 因变量 / M5 调节变量
- **可迁移性**: 中（适用于调节构念在结果上有官方/客观分级可循的设计）
- **区别于**: 常规 M5 交互项调节 — 本变体不设交互项，而以 DV 按官方严重度分级拆分为主 DV 配对假设（低自主权子样本 vs 高自主权子样本），一句映射完成假设-测量对齐
[骨架]:
To measure the varying levels of [moderator construct] that exist in [outcome decisions] for [H2a] and [H2b], we differentiate our dependent variable according to [official classification] provided by [authority]. According to [authority], [category A] have the potential to [serious harm] and thus have little [moderator construct], while [category B] have no such potential and thus have significant [moderator construct]. Consistent with this perspective, we use [all outcomes] to examine [H1], [category A] to examine [H2a], and [category B] to examine [H2b].
- **原始句锚点**（ball_2018 原文）: "Consistent with this perspective, we use all manufacturing-related recalls to examine Hypotheses 1, Class 1 and 2 recalls to examine Hypothesis 2a, and Class 3 recalls to examine Hypothesis 2b."


### 变体 54：M2 lead-DV 滞后对齐 + 理论驱动子样本排除双理由（ball_2018 型，gap HIGH）
- **出处**: ball_2018 (SMJ)，产品召回面板，band=gap HIGH
- **槽位**: M2 数据来源与样本漏斗
- **可迁移性**: 高（滞后 DV 面板设计通用）
- **区别于**: 变体 8（M8 回顾性偏差三角检验）— 本变体不做回顾性偏差检验，而是显式声明 DV 滞后一年（leads all other variables by one year）并以"数量过少 + 无理论构念"双理由排除子样本
[骨架]:
Our main [DV] measure is the total number of [events] by a firm for the year following the year of the independent and control variable measures. In other words, the dependent variable is a [count] measure that leads all other variables by one year... In our analysis, we include only [subset] for two reasons. First, there were an insignificant number of [complement] to analyze separately; our panel only has [N small] [complement], compared to [N large] [subset]. Second, by their very nature, [complement] contain no [theoretical construct], as they are mandated by [authority].
- **原始句锚点**（ball_2018 原文）: "In our analysis, we include only voluntary recalls for two reasons. First, there were an insignificant number of involuntary recalls to analyze separately; ... Second, by their very nature, involuntary recalls contain no discretion, as they are mandated by the FDA."


### 变体 55：M4 新颖测量构建的档案来源链 — 数据缺口→补全行动→测量能力声明（ball_2018 型，gap HIGH）
- **出处**: ball_2018 (SMJ)，产品召回面板，band=gap HIGH
- **槽位**: M4 自变量/核心预测变量
- **可迁移性**: 中（适用于需多请求/多年档案重建的新颖构念测量）
- **区别于**: 常规 M4 变量定义段 — 本变体以 provenance 链论证测量可信性：来源局限（缺口）→ 补全行动（获取全档案）→ 逐字段用途清单 → 精确测量能力声明
[骨架]:
To create this novel [construct] measure, we used data from [source]... However, [source limitation]. In order to determine [precise quantity], which is necessary to obtain a precise measure of [construct] for each [unit-time], we needed to acquire [full historical archive]. We were able to obtain [archive span] through multiple [access requests] to [authority]... This [archive] data allowed us to precisely measure the [construct components] by each [unit], in each [period].
- **原始句锚点**（ball_2018 原文）: "In order to determine the exact year a drug was discontinued, which is necessary to obtain a precise measure of product competition for each firm-year, we needed to acquire every Orange Book published since 1984."


### 变体 56: M1 监管在场但裁量权在厂商的设置辩护 (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: Additionally, although the FDA has legal authority to mandate recalls, they seldom do so and did not do so for the firms and years we examined.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M1

**骨架**:
> We collected data from all [regulated firms] regulated by [agency] that [manufacture focal products]. We focused on [this setting] because these firms frequently experience [focal failures] that have significant [stakeholder] effects. Additionally, although [agency] has legal authority to mandate [the focal outcome], it seldom does so and did not do so for the firms and years we examined — [the outcome] thus remains a discretionary firm decision.

**与原骨架差异**: 区别于变体 15（单行业双重现象辩护）与变体 33（单一中介机构 a/b/c 辩护）——本变体处理的是**监管型 outcome** 的设置合法性：监管机构法律上有强制权但实践中极少行使，借此把 outcome 的裁量权留在厂商内部，为组织层面解释（而非监管执行）铺路。

**诚实边界**: "seldom mandates" 是可核查的经验主张——若研究年份内监管机构确曾强制行动，该辩护失效；必须对研究窗口内核实。


### 变体 57: M2 同一现象双边际分渠道取数 + 多库交集报最终 N (VERIFIED)

**来源论文**: Wowak, Mannor, Wowak & Bu 2020 (Manufacturing & Service Operations Management)
**原始句锚点**: Recall counts were collected via a Freedom of Information Act (FOIA) request, whereas recall timing was provided by senior FDA leaders.

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**槽位**: M2

**骨架**:
> We collected [focal event] data in two ways: [event counts] were collected via [a public records request], whereas [event timing] was provided by [senior regulatory officials]. In combination, these data include [date first aware], [date action initiated], [responsible unit], and [severity classification]. [Covariate] data were obtained from [database A] and [database B]. The intersection of these datasets led to a sample of [N] [unit-period] observations from [start year] to [end year] that spanned all [M] [firms] that existed during our focal years.

**与原骨架差异**: 区别于变体 2（样本交集漏斗）与变体 16（多源数据库交叉验证）——那两类用多源验证**同一构念**；本变体因**没有任何单一来源同时提供计数的边际与时点的边际**，把同一现象的两个测量边际分别取自两个渠道，再与协变量库求交集、报最终 N 与全总体覆盖。

**诚实边界**: 计数与时点来自不同渠道可能覆盖口径不一致；非正式渠道（如高管提供）需在附录给出provenance 辩护；交集漏斗仍应报告交集前后的 N 差异。


### 变体 63：二分变量交互的四格哑变量拆分 + 判定标准前置（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "In effect, [H#] predicts an interaction effect between [dichotomous X] and [dichotomous W] on [the likelihood of Y]. The product-term approach cannot be used to test the interaction between dichotomous variables ([citation]). Thus, to test whether [X] has stronger effects on [Y] when [W] is present, whether or not [the implementation condition], we created separate dichotomous variables for the four different categories of [X × W]: (1) [X present with W]; (2) [X present without W]; (3) [X absent with W]; and (4) [X absent without W]. The base case is [neither condition], as [W] cannot occur without [X]. [H#] is thus supported if variables (1) and (3) are stronger predictors of [Y] than variables (2) and (4)."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Independent Variables / Agency Explanations（P3）

**原文锚定**:
> "The product-term approach cannot be used to test the interaction between dichotomous variables (Jaccard, Turrisi, and Wan, 1990). Thus, to test whether LTIP adoption has stronger effects on board changes when an agency explanation is used, ... we created separate dichotomous variables for the four different categories of adoption."

**关键特征**:
- 方法论依据前置：先引方法论文献宣告乘积项对二分变量不可用，再给四格拆分——技术选择是"被规则强制"而非"作者偏好"，免疫"为何不做交互项"的审稿质疑
- base case 逻辑显式论证（"as there can be no [W] without [X]"）——参照组的理论合理性一句话说清，防止"四哑变量+截距"的共线性/解释性质疑
- 假设支持判据在 Methods 就写死（"H4 is thus supported if (1) and (3) are stronger predictors than (2) and (4)"）——把结果解释规则前置为公共知识，Results 无需重新仲裁

**适用**: X 与 W 均为二分（采纳×框架、进入×退出、处理×披露）的交互检验；分类因变量模型中交互不宜用乘积项时的标准替代方案

**禁忌**: 四格必须互斥且穷尽（base case 排他性要能一句话论证），否则哑变量组间比较无因果解释；判定标准前置后 Results 必须严格按该标准报告，不得事后更改比较组

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


### 变体 66：先前状态构念的 PCA 合成控制（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "Given that prior [levels of the construct] might influence [subsequent changes] as well as [the focal reaction], we controlled for prior [construct] in all models. We used the following commonly used indicators of [the construct] ([citation]): (1) [indicator 1]; (2) [indicator 2]; (3) [indicator 3]; and (4) [indicator 4]. We combined these variables into a single measure using principal components analysis ([citation]). The results of this analysis yielded only one eigenvalue greater than one, and the scree plot also suggested that only this first component should be retained. We also estimated separate models [in which one component was entered separately from the others], and the results were substantively unchanged."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Control Variables（P2）

**原文锚定**:
> "The results of this analysis yielded only one eigenvalue greater than one, and the scree plot also suggested that only this first component should be retained."

**关键特征**:
- 多指标控制变量合成不靠断言而靠双重统计判据：eigenvalue>1 与 scree plot 各自独立支持单因子保留——合成合法性由数据结构而非研究者便利背书
- "cf." 式指标清单（"commonly used indicators of [construct] (cf. [prior work])"）先把四个指标锚定为领域惯例，再合成——惯例性化解"为何是这四个指标"的质疑
- 合成后立即补"分量表分别入模"的稳健性：防止 PCA 合成被质疑掩盖个别指标驱动，一步到位

**适用**: 多个高度相关指标刻画同一"先前状态/能力/控制强度"构念、需合成单变量以避免共线性的控制变量段

**禁忌**: eigenvalue 与 scree 双判据必须一致支持单因子，结果矛盾时不可强行合成；PCA 载荷方向需确认后统一符号，否则合成变量方向不可解释

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)



#### 变体：M7 一阶差分动态对齐 + 滞后构念部分调整（post_2022_women_tmt_strategic_renewal 型，gap HIGH）
- **功能标签**：把「处理→认知→行动」的动态中介主张落实为测量与时序架构——DV 与协变量全一阶差分、解释变量滞后一期、滞后 DV 作部分调整
- **骨架**：To capture within-firm change in [DV], we computed the first difference (from [t] to [t+1]) of [measure]. To estimate dynamic models, all control variables, unless noted otherwise, are in first differences (from year [t-1] to [t]). We estimated dynamic [OLS] models on an unbalanced panel (i.e., not all firms have the same number of observations) of [N] observations on [K] firms from [year] to [year]. We controlled for unobserved heterogeneity by way of fixed [industry] effects, and by taking the first difference of our time-varying explanatory variables at the [level] level, all lagged by one year. Thus, all models are truly dynamic as within-firm changes in the dependent variables are linked to within-firm changes in [treatment], while controlling for within-firm changes in relevant control variables. To test [hypotheses], we included past levels of [construct], implying that we modeled temporal shifts in [construct] as a partial adjustment process. As the nature of [construct] might be path dependent, including past levels of [construct] in the model allowed for a gradual temporal adjustment of [construct], following an external event (i.e., [treatment]), due to "regression to the mean."
- **原文锚定**："Thus, all models are truly dynamic as within-firm changes in the dependent variables are linked to within-firm changes in TMT appointments, while controlling for within-firm changes in relevant control variables."（post_2022_women_tmt_strategic_renewal, AMJ 2022, Analytical Strategy 节）
- **区别于**：变体 54（lead-DV 滞后对齐）是对齐 DV 与预测窗口；本变体是全模型差分对齐——"truly dynamic" 句式把差分结构一句话立为识别主张，且部分调整（path dependence/regression to the mean）给出含滞后 DV 的理论理由而非仅计量理由
- **下游接口**：与 IV-2SLS.md 拟合值中介链配套——第一阶段产出的认知位移预测值继承同一时序架构，使两个中间构念（change orientation / risk-taking）可区分、再分别进入下游结果模型


#### 变体：M8 子样本分割调节 + 「不限制其他协变量系数」辩护 + Chow 检验（post_2022_women_tmt_strategic_renewal 型，gap HIGH）
- **功能标签**：在链式（中介型）设计里用子样本分割替代乘法交互项，并显式给出为什么交互项不合适的理由
- **骨架**：To test the moderation effects in [hypotheses], we estimated [DV] models on different subsamples: [low (zero)] versus [high (positive)] [moderator], and [small (below the sample mean value [x])] versus [large (above the sample mean value [x])] [second moderator]. A subsample approach generates the most straightforward insights into the chain of effects from [treatment] to [outcome], because it puts no restrictions on the coefficients of the other covariates and allows the influence of all variables to differ across different [integration settings], which is not the case with models specifying multiplicative interaction effects. We report the Chow tests on the differences in coefficients between the subsamples in a later section of this paper. To investigate if the moderating effect of [moderator] diminishes at high levels of [moderator] ([hypothesis]), we estimated threshold interaction effects.
- **原文锚定**："A subsample approach generates the most straightforward insights into the chain of effects from female appointments to strategic renewal, because it puts no restrictions on the coefficients of the other covariates and allows the influence of all variables to differ across different integration settings."（post_2022_women_tmt_strategic_renewal, AMJ 2022, Analytical Strategy 节）
- **区别于**：变体 42（moderator-dummy 外部效度链）是把连续调节变量二分化做外部效度；本变体是在动态中介链中为「系数全自由度」辩护——两种二分化动机不同（外部效度 vs 链式可解释性），且本变体附 Chow 检验 + threshold interaction 的收口


### 变体 68：M2 排除阈值的双向代价论证 + 放宽阈值补充分析回环（anand_mukherjee_2024 型）
- **出处**: Anand & Mukherjee 2024 (Organization Science)，医疗设备/制药召回面板
- **槽位**: M2 数据来源与样本漏斗
- **可迁移性**: 高（任何需要最小观测窗/最小事件数阈值的面板设计）
- **区别于**: 变体 54（lead-DV 滞后对齐 + 理论驱动双理由排除）— 变体 54 用双理由论证"排除什么"；本变体论证"为什么阈值本身合理"：先摆双向代价（含进去→噪声与偏差；排出去→损失样本与信息），再用放宽阈值的补充分析闭合循环
- **原始句锚点**（Anand & Mukherjee 2024 原文）: "On the one hand, including firms with insufficient observation periods is likely to provide noisy and biased estimates of learning. ... On the other hand, excluding these firms reduces the sample size and potentially eliminates information on some firms, which otherwise could have impacted the results."
- **验证状态**: VERIFIED (expert_audit_override, user 2026-08-29: 用户裁决产品召回主题全部蒸馏成果升 VERIFIED)
- **写入日期**: 2026-08-29
[骨架]:
From these, we removed [units] that did not exist [with at least threshold observations] within the observation period because of [attrition mechanism]. [Mechanism] are frequent occurrences in [the industry]. Therefore, identifying an observation unit over the entire sample observation period is complex. [The mechanism being studied] occurs over time and based on experience, so [units] with insufficient observation periods do not leave enough observations to estimate it. On the one hand, including [units] with insufficient observation periods is likely to provide noisy and biased estimates of [the estimand]. On the other hand, excluding these [units] reduces the sample size and potentially eliminates information on some [units], which otherwise could have impacted the results. Therefore, for the main analysis, we do not include [units] with less than [threshold] of observations. However, a supplementary analysis with all [units] using an unbalanced panel data set gives comparable results to those for our main analyses.

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:m2_threshold_exclusion_two_sided_robustness -->


### 变体 69：M7 三步渐进模型设定的复制式中步叙事（anand_mukherjee_2024 型）
- **出处**: Anand & Mukherjee 2024 (Organization Science)，医疗设备/制药召回面板
- **槽位**: M7 模型规格与估计方法
- **可迁移性**: 高（controls→基线主效应→交互的渐进设定通用）
- **区别于**: 既有 M7 变体多为单一模型的设定与诊断叙事 — 本变体组织的是多步模型族的叙事：每步目的显式命名，且把"非假设的复制步"辩护为对既有研究的对齐复制，预防"基线模型为何要估"的质疑
- **原始句锚点**（Anand & Mukherjee 2024 原文）: "Although the main effect of learning from accumulated recalls is not a hypothesized relationship in our research, this step replicates the relationship analyzed in previous studies (Haunschild and Rhee 2004, Thirumalai and Sinha 2011)."
- **验证状态**: VERIFIED (expert_audit_override, user 2026-08-29: 用户裁决产品召回主题全部蒸馏成果升 VERIFIED)
- **写入日期**: 2026-08-29
[骨架]:
Our analysis of [outcome] consists of three progressive steps. In Step 1, we include the effects of the control variables, [controls], on [DV]. We include the explanatory variables, [IVs], in Step 2 to assess the main effect of [the base relationship]. Although the main effect is not a hypothesized relationship in our research, this step replicates the relationship analyzed in previous studies ([citations]). In Step 3, we test the moderation effects posited in [Hypotheses] by incorporating relevant interaction terms. The complete model is shown here, with subscripts for [i] representing [unit], [j] representing [group], and [t] representing [time].

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:m7_progressive_three_step_narrative -->


### 变体 70：M2 自维护档案 vs 第三方收割库的比较性数据质量辩护（fini_jourdan_perkmann_2017 型）

**来源论文**: Fini, Jourdan & Perkmann 2017 (*Academy of Management Journal*)
**原始句锚点**: "This means that our publication records are author-approved, and hence more accurate than records downloaded from bibliographic databases which frequently suffer from name disambiguation issues (Azoulay, Stellman, & Zivin, 2006)."
**验证状态**: EMERGING（单篇；`section_variant`）
**槽位**: M2（数据来源与样本漏斗）
**骨架**:
> We extracted [construct] data from a system that mandates [actors] to edit their [records] as harvested from [upstream databases], and publish them as an edited, approved list on [an official channel]. This means that our records are [approved by the actors themselves], and hence more accurate than records downloaded from [third-party harvested databases], which frequently suffer from [named quality failure mode — e.g., entity name disambiguation] ([citation]).
**与原骨架差异**: 变体41 辩护"为什么必须自建档案"（数据可得性），变体55 的 provenance 链是"缺口→补全→能力声明"；本变体辩护"自维护档案为什么比第三方收割库更准"——把数据质量写成**比较性主张**：制度化强制自维护机制（收割后必须人工核订）→ 官方渠道发布 → 点名第三方库的失效模式（name disambiguation）→ 权威 citation 锚。适用于有 actor 自维护记录制度的档案情境（大学人事/发布系统、投稿系统、监管申报库）。
**诚实边界**: 比较性主张以制度化编辑机制为前提——没有强制核验环节就退化为普通来源声明，不得套用 "more accurate" 措辞；点名失效模式须有 citation 支撑，不得凭空指控第三方库。

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:m2_author_curated_records_data_quality_defense -->


### 变体 71：M1 设置含义调查佐证链 — 预先封存"活动被污名化"替代解读（fini_jourdan_perkmann_2017 型）

**来源论文**: Fini, Jourdan & Perkmann 2017 (*Academy of Management Journal*)
**原始句锚点**: "Results from a 2013 survey among the Minerva faculty suggest that while collaboration with industrial partners is seen as mission-critical ... it is perceived as serving the ultimate purpose of advancing the frontiers of science, rather than as a goal in itself."
**验证状态**: EMERGING（单篇；`section_variant`）
**槽位**: M1（研究情境设置）
**骨架**:
> [Setting institution] combines [tension_1 — e.g., scientific-excellence logic] and [tension_2 — e.g., commercialization mandate], making it an ideal context to observe [multi-audience evaluation]. Results from a [year] survey among [site actors] suggest that while [focal cross-audience activity] is seen as mission-critical both in terms of [its resource contribution] and [its effect on the primary mission], it is perceived as serving [the primary mission], rather than as a goal in itself.
**与原骨架差异**: 变体41 的 Setting rationale 槽位只用一句陈述双制度张力；本变体补上**证据链**——用设置内部的调查数据证实 actor 自己如何理解该活动的含义（服务于主使命而非目标本身），预先封存"跨受众活动被成员视为污名/怨恨"的替代解读：若科学家普遍抵触产业合作，identity proximity 的调节解释将失效。适用于任何"跨边界活动可能被成员负面解读"的单一组织情境。
**诚实边界**: 调查须为设置内真实施测并注明年份；一句话概括感知分布即可，不得把调查结果写成外部效度主张（单组织调查不支撑跨组织推广）。

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:m1_setting_dual_tension_survey_corroboration -->


### 变体 74: M2 可得性损耗对比 + 范围限制保守检验声明 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Availability of analysts' estimates ... reduced the 4,365 firm-year full sample to 3,107 firm-year observations. ... These characteristics suggested our sample provided a conservative test of our hypotheses since they result in some restriction of range to primarily large and well-performing firms."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: M2
**骨架**:
> Availability of [analyst-forecast data] for each year reduced the [starting_N] full sample to [final_N] firm-year observations. T-tests comparing the full and reduced samples showed that the firms with [data] available had significantly more [attribute_1] ([mean_A] vs. [mean_B], p < [.05]), greater [attribute_2] ([mean_A] vs. [mean_B], p < [.01]), and higher [attribute_3] ([mean_A] vs. [mean_B], p < [.001]) than firms with missing [data]. These characteristics suggested our sample provided a conservative test of our hypotheses since they result in some restriction of range to primarily [restricted_population].
**与原骨架差异**: 漏斗收尾只报「降到 N」是常态——Pfarrer 多两拍：(1) **损耗方向量化**——全样本 vs 缩减样本三属性 t 检验，数字齐全，把数据可得性损耗的选择效应写透明；(2) **保守检验 reframe**——不辩护代表性（与变体 67 的「无显著差异→安心」相反），而是承认缩减样本偏大偏好，并把 restriction of range 重构为使假设更难获支持的 conservative test。与变体 65（控制相关方向保守性）同属「偏误对我不利」家族，但作用于样本层而非控制层。适用于任何因数据可得性收缩样本的档案面板。

<!-- wb:pfarrer_pollock_and_rindova_2010:m2_attrition_conservative_test -->


### 变体 75: M6 1/n 衰减加权历史自控制 + 权重窗稳健性 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Drawing from organizational research on learning and contagion (...), we generated a weighted sum that assigned a weight of 1/n for each year prior to a focal year ... We constructed 15-, 10-, 5-, and 3-year summed variables, utilizing the 1/n 'decay' rates for each of the variables, and obtained the same results for each alternative."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: M6
**骨架**:
> We used several variables to control for multiple aspects of [units'] histories that could affect our relationships of interest. Drawing from organizational research on [learning and contagion] ([cites]), we generated a weighted sum that assigned a weight of 1/n for each year prior to a focal year for [past outcome] (to control for a [halo] effect), prior [focal behavior A and B] (to control for "[habitual actors]"), prior [related behavior] (to control for [mechanism]), and prior [focal assets] (to control for the historical levels of these assets), with n designating the number of years prior to the focal year. We constructed [15-, 10-, 5-, and 3-year] summed variables, utilizing the 1/n "decay" rates for each of the variables, and obtained the same results for each alternative.
**与原骨架差异**: 控制变量的 because 密度 corpus 已充分（变体 1 分层 because / 变体 40 双面 because / 变体 14 全谱系）——本变体的新 HOW 是**历史自控制的功能形式**：(1) 理论出口（learning and contagion 文献）直接正当化 1/n 递减权重——近因权重大、远因衰减，与习惯形成/传染的机制时间结构对齐；(2) 每个 prior 项括号内命名被堵的机制（halo effect / "habitual surprisers" / earnings guidance / 历史资产水平），控制即抗辩；(3) 把 focal 资产自身的 prior 水平也作控制，防「资产惯性」替代解释；(4) 权重窗（15/10/5/3 年）本身做稳健性并一句收口。适用于事件可重复发生（surprise、召回、违规、融资）的面板——「是否惯犯」需历史加权聚合而非单年滞后。

<!-- wb:pfarrer_pollock_and_rindova_2010:m6_decay_weighted_prior_behavior_controls -->


### 变体 76: M2 双名单合并 + 重叠率验证 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "We combined information from the two lists because Fortune only listed the top 10 firms in an industry between 1997 and 1998, and only the top 20 firms between 1999 and 2005. Of the 25 different firms listed in Fortune's top 10/top 20 list between 1999 and 2005, 22 were also named in the Wall Street Journal (WSJ)/Harris top 25, showing strong overlap between the two lists and validating our choice to combine the information from them."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: M2/M4
**骨架**:
> Following past research, we obtained data on [unit status] using the rankings in [list A] ([cites]), as well as [list B] ([cite]), and coded a [unit] as [high status] if it appeared among the [top N] firms on either list in a given year. We combined information from the two lists because [list A] [coverage drift: only listed the top 10 in some years and the top 20 in others]. Of the [N_A] [units] listed in [list A] in the comparable period, [N_overlap] were also named in [list B], showing strong overlap between the two lists and validating our choice to combine the information from them.
**与原骨架差异**: 区别于变体 16（多源合并求全 + 防 double-counting）——本变体合并的动因是**单源覆盖口径随年份漂移**（list A 某些年只发 top 10、另一些年 top 20，单源构成时变缺口），并用**重叠率（22/25）作合并决策的经验验证**而非仅引惯例；编码规则是「任一名单达标即编码」的并集，重叠证据在合并句之后收口。三拍结构：并集规则→漂移动因→重叠验证。适用于榜单/评级/名录类构念的多源年份数据。

<!-- wb:pfarrer_pollock_and_rindova_2010:m2_dual_list_overlap_validation -->


### 变体 77: M8 操作化定义稳健性 — 未列表替代阈值段 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "To ensure that our definition of material surprises did not drive results, in analyses not reported here we also tested definitions based on top and bottom percentile cutoffs of 20, 30, and 40 percent ... The results were substantively the same as those reported here."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: M8
**骨架**:
> The final sample included [N1 material positive X], [N2 material negative X], [N3 exact threshold], and [N4 sub-threshold X]. To ensure that our definition of [material X] did not drive results, in analyses not reported here we also tested definitions based on [alternative_1: percentile cutoffs of 20, 30, and 40 percent] (cf. [cites]), as well as [alternative_2: an absolute threshold on X] (cf. [cites]). The results were substantively the same as those reported here.
**与原骨架差异**: micro-templates/robustness-foreshadowing 只有一句预告；非线性模型 变体 8 是 Results 层的稳健性三角组织——本变体是 **Methods 内 DV 定义层的完整执行段**：(1) 被检对象明确是操作化定义本身（our definition of X did not drive results），与估计器/样本稳健性分开声明；(2) in analyses not reported here 诚实标注未列表地位，不假装是正文表格；(3) 每个替代定义带 cf. 引用，锚定到 field 惯例（这些 cutoff 别人也用过）；(4) substantively the same 收口（非 statistically identical）。前置可加四类构成计数（N1–N4）让阈值后果可审计。适用于任何依赖 materiality/cutoff 定义的二分 DV。

<!-- wb:pfarrer_pollock_and_rindova_2010:m8_definition_robustness_untabulated -->


### 变体 78: M6 冲突证据→无假设控制声明 + 池化样本行业中位数归一（gulati1999 型）

**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "Given the conflicting claims about the role of material resource considerations for alliances, I did not put forth specific hypotheses for them. Following prior research, however, I included several commonly considered material-resource-based considerations"（同段）
**验证状态**: VERIFIED（单源；expert_audit_override 2026-09-05）
**写入日期**: 2026-09-05
**槽位**: M6
**骨架**:
> [文献综述定位] While the primary focus of this study is [focal construct family], there may also be [alternative consideration family] that could affect [DV]. [冲突证据归纳] Evidence on the effects of [these factors] is mixed and in many instances conflicting: [some conclude direction A] ([citations]), [others have observed direction B] ([citations]), still others suggest [the relationship may be nonlinear] ([citations]). [无假设声明] Given the conflicting claims about [the alternative family], we did not put forth specific hypotheses for them. Following prior research, however, we included several commonly considered [considerations] ... [归一化 because] We used [measure], defined as [formula] ... This was normalized to the [industry median] because the sample was pooled across [multiple industries].
**与原骨架差异**: 常规 M6 变体给每个控制变量配 because（堵特定替代解释）；本变体处理**证据冲突族**——当一类前置因素文献结论互相矛盾、无法给出方向性预测时：不回避（完整综述冲突史，含正/反/非线性三方位引用）、不硬编假设（显式说 did not put forth specific hypotheses）、但声明"遵循先行研究"全部纳入，并用预测符号表中 NP（no prediction）列把"无方向"状态显式登记给审稿人。配套句：跨行业池化时把财务控制按行业中位数归一，because 从句直接绑定池化设计本身（而非变量语义）。区别于变体 59（假设→符号方向预登记）：变体 59 登记的是**有**假设变量的方向；本变体登记的是**无**假设控制的 NP 状态。
**诚实边界**: "无假设"不等于"无方向预期"——Results 不得对 NP 控制做选择性解读，否则声明失去一致性；NP 控制系数只在审稿人问及时讨论。冲突综述本身不消除混淆，只说明为何不将其升格为假设。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:m6_no_hypothesis_controls_conflicting_evidence -->


### 变体 79：备择解释具名→控制变量化→可检验判据+边界让步（Named-Alternative-as-Control，Gulati_1999_AJS 型）

<!--
pattern_id: named_alternative_as_control
build_type: 面板/事件设计通用（M6 控制变量段——备择解释排除拍）
source_papers: ["gulati_1999_where_do_interorganizational_networks (AJS)"]
verification_status: VERIFIED — expert_audit_override (Gulati 系单源裁定 2026-09-06, paper_count=1)
story_fidelity: section_variant
-->

**适用场景**: 某个 rival 理论对该领域同一条经验规律有现成的竞争解读（如"网络效应"vs"合法性跟随"、"能力"vs"声望"），且 rival 机制有公认代理变量可买——控制变量段最有力的一拍。

**骨架**:
```
[备择机制陈述] An alternative interpretation for [the focal dynamic] is [rival theory] linking [X] to [rival mechanism]. [Rival theory] claims that [mechanism in one sentence, with canonical citation]. Applied to this context, it would suggest that [rival reading of the very pattern the paper explains].
[利害句] If this were the case, [focal construct] might simply be capturing [rival process], rather than [the effects proposed in our model].
[控制变量化+判据预声明] To account for this alternative explanation, we included [a named control], defined as [operationalization]. If the effect of [focal construct] is only capturing [rival process], the inclusion of [control] should make the effect of [focal construct] insignificant, thus bringing into question the validity of our claims.
[边界让步] The [focal] model, however, does not preclude [a rival effect], because [rival process] and [focal process] effects need not be mutually exclusive.
```

**为什么有效**: rival 解读被赋予最大善意——机制陈述、情境翻译、利害推演三步完整，然后才被控制变量化；判据预声明（"inclusion should make it insignificant ... bringing into question"）把显著性检验变成预登记的裁决规则，读者知道结果无论何向都有解读位；边界让步句是点睛之笔——承认两机制不互斥，既堵住"你只是没测出 rival"的反攻，又为 Results 侧两系数并存的格局预留理论空间。

**注意事项**: 判据句是双向保险（rival 显著+焦点不显著=质疑自己；两者并存=模型声明不互斥）——写作时须与 Results 实际格局核对；rival 机制须有公认代理（无代理时改用设计排除）；"need not be mutually exclusive" 只用于真可共存的机制对，不得用来豁免一切不一致。

**反模式**: rival 解读只用半句稻草人带过；控制变量入了名但无判据（"we control for X"）；让步句写成对 rival 的全面投降；判据预声明与 Results 报告格局矛盾。

**与近亲变体的区分**: 家族 M6 既有条目管 because 逻辑与一阶差分控制声明；本变体是"整段以一个具名 rival 理论为组织轴"的 M6 排除拍——控制变量的 because 从变量功能升级为理论裁决，直接回应 registry common_failure「控制变量无 because 逻辑——仅列举变量名」的高阶形态。

**原文锚点** (Gulati & Gargiulo 1999, AJS):
> "If the effect of structural differentiation is only capturing density-driven legitimacy, the inclusion of alliance density should make the effect of structural differentiation insignificant, thus bringing into question the validity of our claims."

<!-- wb:gulati_1999_where_do_interorganizational_networks:c4_m6_named_alternative_as_control -->
### 变体 80：M2 源清单生存者条件化修复 — 回收消亡事件单元 + 风险集合并（higgins_2003_OS 型）

**来源论文**: Higgins & Gulati 2003 (Organization Science)
**原始句锚点**: "Further, to guard against sample selection bias associated with this listing, we collected information on firms that went public in the same time frame as our sample but that did not survive in their original form by 1996."
**验证状态**: EMERGING（单篇）
**槽位**: M2
**骨架**:
> Our primary list of [units] was obtained from [industry listing] ([n]). Unlike other sources, this listing does not include [tangentially participating corporations]; hence, ours is a narrower definition of [domain] than that employed by other researchers (e.g., [prior studies]) and is in line with more recent research on the industry (e.g., [recent studies]). Further, to guard against sample selection bias associated with this listing, we collected information on [units] that [underwent the focal event] in the same time frame as our sample but that did not survive in their original form by [list year]. From these sources, we identified an additional [n] [units] that had experienced [name changes / mergers / acquisitions]. Combining these [recovered event units] with [the complementary non-event units] yielded a final combined sample size of [N].

**与原骨架差异**: 变体 34（多源清单+覆盖边界定样本窗）以数据覆盖定样本窗、变体 67（完备性准则漏斗+代表性 t 检验）以数据完备准则导出 N——两者修的是"覆盖/完备"缺口；本变体修的是**生存者条件化**：行业清单以"存活至编表年"为隐含条件，事件单元若在编表年前消亡（改名/被并购/清算）即从清单消失，事件样本因此有选择性。修复动作是主动回收"同窗内经历事件但未存活到编表年"的单元并入事件样本，再与非事件单元合并成风险集（本文 281→+15 回收→+542 私有→838）。概念边界先例对齐（"narrower definition ... in line with recent research"）是配套微动作。
**诚实边界**: 回收单元与存活单元的信息可得性不对称（消亡单元档案更薄），须说明数据来源如何覆盖消亡单元；回收判据（名称变更/并购/清算）应显式列出；若理论机制与"消亡"本身相关（如研究退出行为），回收并不能完全修复选择偏差，需在局限承接。
**适用**: 以"编表年后视镜"型行业清单（year-t stock list）为抽样框、focal 事件发生在历史窗口内的档案研究（IPO/退市/召回/关厂）；事件单元存活状态与抽样框条件化相关的任何设计。

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:m2_survivorship_repair_sample_frame -->


### 变体 81：M4 第三方榜单阈值化突出名单 → 生涯纽带计数 → 团队规模标准化（higgins_2003_OS 型）

**来源论文**: Higgins & Gulati 2003 (Organization Science)
**原始句锚点**: "Since the number of ties covaries with the size of the upper echelon, we divided upstream, horizontal, and downstream tie measures by upper echelon size, consistent with recent research (Geletkanycz and Hambrick 1997)."
**验证状态**: EMERGING（单篇）
**槽位**: M4
**骨架**:
> [Focal construct] was assessed by identifying and manually coding [the observable carrier, e.g., the last five years of employment and board memberships], as listed in [artifact source]. We assessed the number of ties each individual had to prominent [category A/B/C] organizations. To gauge whether particular affiliations were with prominent institutions, we used [third-party ranking basis] as the criterion for prominence: we [generated the list] from [ranking source, editions/years], coding any [institution] that appeared [top-N in relevant categories / anywhere on the listing] at any time during [window] as prominent (n = [count]). We supplemented this list with [notable institutions not captured by the ranking, e.g., private or foreign organizations with comparable scale] (n = [k]). Since the number of ties covaries with the size of the [team], we divided the [category] tie measures by [team size], consistent with recent research ([citation]). [Per-category base rate: the [teams] in our sample generally had [k] members with at least one tie to a prominent [category] organization.]

**与原骨架差异**: 变体 36（复合测量构念分步构建+阈值辩护+可行性论证）的阈值筛选的是"哪些 actors 进入构念计算"、构念为双侧重积型；本变体是**名单式突出性判定链**：(1) 第三方榜单+出现阈值（top-N 类别榜/任一年上榜）→构造"突出机构名单"并报名单量级与稳定性（"a total of N ... this was a relatively stable list"）；(2) 跨榜单时代接续——排名口径随数据可得性分段（前期仅美国、后期含国际），并补私有/外国同规模机构；(3) 对团队成员生涯纽带逐人计数并**按团队规模标准化**（引先例背书）；(4) 每类测量附样本内基率句（"generally had two people with at least one tie"）让审稿人看到构念实测变异。适配多类别（上游/同业/下游）网络/声望构念的测量叙述。
**诚实边界**: 榜单阈值（top-10/top-30）须给依据或先例引用；跨时代口径拼接处（榜单覆盖起止年不同）应显式声明；除以团队规模改变解释单位，须与理论中"个体纽带 vs 团队禀赋"层次一致；基率句是描述性证据，不能替代构念效度论证。
**适用**: 生涯史/履历档案中构造"与突出组织的纽带"类构念（声望、地位、endorsement 潜力）；任何以第三方榜单为突出性判据、以团队成员为单位计数并聚合到组织层的设计。

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:m4_prominence_list_threshold_tie_normalization -->


### 变体 82：M3 采纳标准指数 DV 的出处—通行度—缺失—替代基准四拍链（higgins_2003_OS 型）

**来源论文**: Higgins & Gulati 2003 (Organization Science)
**原始句锚点**: "Carter and Dark's (1992) analyses suggest that these measures provide a finer-grained evaluation than a simpler market share alternative (e.g., Megginson and Weiss 1991)."
**验证状态**: EMERGING（单篇）
**槽位**: M3
**骨架**:
> [DV] was measured using an index developed by [author, year] and then updated by [author, year]. The measures are based on [observable artifact] and have been cited widely in both [field A] and [field B] research ([citations]); this information was available for all but [n] of the [units] in our dataset ([accounting for m firms]). Scores may assume a value ranging from [floor, indicating lowest level], to [ceiling, indicating highest level]; in our data set, the mean score was [x]. [Author]'s ([year]) analyses suggest that these measures provide a [finer-grained] evaluation than a simpler [alternative] measure ([citation]). We obtained [the measure inputs] from [artifact source].

**与原骨架差异**: 变体 25（DV 文献基准锚定）对比的是样本均值与前人均值（跨样本可比性）、面向自建比率/计数 DV；本变体面向**采纳他人标准指数**的场景，四拍顺序为：(1) 出处双拍——原始开发者+更新版本（测量随时间被维护）；(2) 通行度——"cited widely in both [field A] and [field B]" 跨领域引用列表；(3) 缺失计数——"available for all but n"（缺失落到多少个 unit，双口径：25 家承销商/55 家企业）；(4) 替代基准优越性——引第三方验证研究论证该指数比更简单的替代（如市场份额）**更细粒度**。末尾以量表端点+样本均值完成标定。适用于存在公认标准指数/评级的 DV。
**诚实边界**: "cited widely" 须附真实跨领域引文（2+ 领域各至少 1 条）；缺失计数须同时给测量级与组织级口径；"finer-grained than alternative" 的依据必须来自第三方验证研究而非自评；若指数更新版本与原始版本口径有变，须声明采用哪个版本。
**适用**: 采纳既定评级指数为 DV 或关键变量（承销商声望类 tombstone 指数、信用评级、榜单分数、期刊指数）；任何"不自建测量而采纳领域标准量表"的档案研究。

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:m3_adopted_index_provenance_chain -->


### 变体 83：M4 有界异质性指数双测量 + 零锚定 + 工作例翻译（higgins_2003_OS 型）

**来源论文**: Higgins & Gulati 2003 (Organization Science)
**原始句锚点**: "For example, a firm with an upper echelon with 10 members, two of whom had ties to prominent pharmaceutical organizations, would receive a score of 1, while a firm with the same-sized upper echelon that included ... would receive a score of 2."（同段连续原文，删节处省略）
**验证状态**: EMERGING（单篇）
**槽位**: M4
**骨架**:
> We measured [range/heterogeneity of the construct] two ways. First, we used a variation of the [Herfindahl-Hirschman index], H = 1 − Σ p_i², in which H is the measure of heterogeneity or range and p is the percentage of [members] who [have property in category i]. This variable was set to equal zero when the [team] had no relevant [properties]. This measure is equivalent to [Blau's (1977)] index of heterogeneity. Second, we measured [range] as the count, 0 to [K], of the number of [categories] covered. For example, a [team] with [N] members, [k] of whom [property of one category], would receive a score of [1], while a [team] with the same-sized [team] that included [members spanning two categories] would receive a score of [2].

**与原骨架差异**: 变体 17（factor score）、变体 46（z 分复合调节）、变体 36（分步构建）讲"怎么算出"复合测量，均未处理**指数的可读性与解释单位**。本变体四要素：(1) 双测量并置——连续指数（H=1−Σp²）与有界计数（0..K）互为替身；(2) 零值锚定——显式声明"无相关属性时 H=0"，堵住"未连接团队如何编码"的疑问；(3) 谱系等价——"equivalent to Blau's index"把自定义公式挂到已知测量家族；(4) **工作例翻译**——两个具体团队（同规模、不同覆盖）演示打分差异，把抽象指数翻译成审稿人可复算的数字。
**诚实边界**: 工作例数字须与公式严格一致（可复算）；零值锚定是编码决定而非数据事实，若"无纽带"与"纽带数据缺失"不可区分须声明处理；双测量若结果分歧须在 Results 承接而非只报有利者。
**适用**: 团队/组合层面异质性、多样性、覆盖范围构念（职能异质性、affiliation 类别覆盖、组合多元化）；任何用 Herfindahl/Blau/Gini 型指数且审稿人需要"这个数怎么读"的研究。

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:m4_heterogeneity_index_worked_example -->


### 变体 84：M2 档案研究中的田野佐证组件 — 过程复杂度访谈 + 常驻专家通报人（higgins_2003_OS 型）

**来源论文**: Higgins & Gulati 2003 (Organization Science)
**原始句锚点**: "The individuals to whom we spoke at the service organizations were all intimately involved in various IPO deals in the biotechnology industry during the period of our study and provided extremely helpful information to us about the complexities involved in taking a firm public."
**验证状态**: EMERGING（单篇）
**槽位**: M2
**骨架**:
> Finally, we conducted field and ethnographic analysis at [n] [focal organizations], [k] [service organizations], and [m] [complementary organizations]. The individuals to whom we spoke at the [service organizations] were all intimately involved in [the focal process] during the period of our study and provided [helpful] information to us about the complexities involved in [the focal process]. Among the [focal organizations], we completed [n] formal interviews, ranging in length from [x] to [y] hours each. [Interviewee composition: n1 in business-related positions, n2 in technical/senior research positions.] In addition, we solicited ongoing input from one expert informant who [has worked at multiple organizations and was centrally involved in the focal process].

**与原骨架差异**: 变体 6（多通道精英招募）招募的是**估计样本本身**（访谈对象即数据）；本变体的访谈对象**不进入估计**——田野组件服务于档案研究的两类可信度：(1) 过程复杂度通报（了解事件如何展开，校准手工编码与解释）；(2) 测量接地（semi-structured interviews 采集与档案测量同构的信息以交叉验证）。要素：多类场所枚举（focal firms + 服务机构 + 互补机构）、受访者与焦点过程的直接参与声明（"intimately involved in ... during the period of our study" 的时间与角色对齐）、访谈量与时长、商界/技术界受访者构成、常驻专家通报人。
**诚实边界**: 田野访谈不进入估计样本须明确（避免被误读为混合方法设计）；访谈证据用于解释与编码校准而非假设检验；专家通报人的利益关联宜在伦理/局限处交代。
**适用**: 档案数量研究嵌小规模田野（IPO/召回/危机响应等过程复杂、编码依赖行业知识的研究）；为手工编码的档案测量提供过程接地。

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:m2_archival_fieldwork_triangulation -->


### 变体 85：M1/M2 问卷前置田野与抽样框-受访者双核验（gulati_2007 型）

**来源论文**: Gulati & Sytch 2007 (Administrative Science Quarterly)
**原始句锚点**: "We verified the comprehensiveness of this list with several executives in the industry and also by comparing it with component lists used by the firms to monitor the quality of their own parts."
**验证状态**: EMERGING（单篇）
**槽位**: M1/M2
**骨架**:
> The analysis presented in this paper is based on fieldwork, followed by a survey of [respondent role] at [Organization A] and at [Organization B]. Prior to launching the survey, we conducted a total of [N] interviews ([n1] at [A] and [n2] at [B]). The initial interviews were exploratory and open ended and were intended to clarify the nature of [the focal phenomenon]. In later interviews, we sought clarification on our central constructs of [C1], [C2], [C3], and [C4]. The unit of analysis for the survey instrument is the [unit], with each survey respondent providing data on [focal content], as well as data on [partner content]. This sampling approach is akin to one used by [seminal study] in their study of [the industry]. Drawing on previous studies of [the industry] and discussions with informants, we used a list of [N_frame] [units]. We verified the comprehensiveness of this list with several [industry experts] and also by comparing it with [lists] used by the firms themselves. For each [unit], [senior managers] supplied the names of [respondents] with oversight for [the activity]; the [independent office] in each company verified the expert status of each survey respondent.

**与原骨架差异**: 变体 84（档案研究田野佐证组件）的访谈对象**不进估计样本**、服务于过程复杂度通报与测量接地；本变体是问卷前置田野的**生产性使用**：(1) 两阶段访谈（探索性开放→构念澄清）直接产出测量工具；(2) 抽样框以"外部专家核验 + 企业内部清单比对"双路验证完备性；(3) 受访者以"高管提名 + 独立办公室（如 controller's office）资格核验"双环把关。与变体 6（多通道精英招募）的分界：彼处招募的是估计样本本身，本变体核验的是**抽样框与受访者资格**。近亲 实证对象构建 变体7（专家报告人资格核验三环链，EMERGING 文件）为资格核验拍的家族成员。

**诚实边界**: "akin to [seminal study]" 的先例锚定须真实可引；清单核验的两个判据（外部专家+内部清单）缺一会削弱完备性主张；独立资格核验需真实存在的组织内第三方，不能由提名者自证。

**适用**: 关键 informant 问卷、组织间 dyad 调查、需要抽样框完备性主张的调查设计；田野访谈服务于工具开发而非假设检验的研究。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:m2_fieldwork_frame_and_respondent_verification -->


### 变体 86：M2 问卷响应率-非应答 K-S-范围排除段级全链（gulati_2007 型）

**来源论文**: Gulati & Sytch 2007 (Administrative Science Quarterly)
**原始句锚点**: "We examined the nonresponse bias by comparing the characteristics of the components for which responses were received against those for which no response was received ... using the Kolmogorov-Smirnov test (Siegel and Castellan, 1988)."
**验证状态**: EMERGING（单篇）
**槽位**: M2
**骨架**:
> We took several steps to ensure a good response rate for the survey ([method citation]), ranging from having [senior management] endorse the project to conducting multiple follow-ups with non-respondents. [n1] [respondents] responded from [Site A], and [n2] from [Site B], representing response rates of [p1] percent and [p2] percent, respectively, and a total response rate of [p] percent. We examined the nonresponse bias by comparing the characteristics of [units] for which responses were received against those for which no response was received for [k] key [unit] characteristics ([anchoring prior study]) using the [Kolmogorov-Smirnov] test ([citation]). We found no significant differences between the categories of respondents and non-respondents. The respondents provided information on [N_obs] [exchange relationships]. We eliminated [n1] observations with missing data and [n2] observations [outside the intended scope], leaving [N_final] observations for [relations] with [N_unique] unique [partners].

**与原骨架差异**: micro 层已有两条非应答 K-S 句式链（robustness-foreshadowing.md：westphal_bednar2005 K-S+Heckman 双统计；carpenterwestphal2001 K-S+双层代表性）——均为句式级。本变体是**段级全链**，三个增量拍：(1) 响应率工程句前置（高层背书→多轮跟进，方法程序带引用）；(2) **检验特征锚定先例研究**——把"哪些特征算关键"外包给领域经典（"for [k] key characteristics ([seminal study])"），免自选嫌疑；(3) 漏斗以范围性排除（内制/自供组件）+ 双口径收口（observations / unique partners）。与变体 67（完备性准则漏斗+总体代表性 t 检验）的分界：彼处对比对象是未入样总体（档案可得），本篇对比对象是**非响应者**（问卷专属），统计用 K-S（分布形状）而非 t（均值）。

**诚实边界**: 非应答检验特征须真是先例研究中的关键特征且对非响应者可得；K-S 只查单变量分布差异——多变量选择威胁仍需 Heckman 或代表性声明补强（见 micro 两条链）；响应率分层口径须与发放口径一致。

**适用**: 关键 informant 问卷、组织间 dyad 调查、任何需封 nonresponse bias 质疑的单波调查。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:m2_survey_response_nonresponse_funnel -->


### 变体 87：M3/M4 量表双构念区分+旋转交叉验证+低 α 保守反驳链（gulati_2007 型）

**来源论文**: Gulati & Sytch 2007 (Administrative Science Quarterly)
**原始句锚点**: "Although these reliabilities fall short of the frequently used threshold of .70 (Nunnally, 1978), ... this should not be considered a benchmark every scale has to pass."
**验证状态**: EMERGING（单篇）
**槽位**: M3/M4
**骨架**:
> To ensure the reliability and discriminant validity of our constructs, we relied primarily on items used in prior research and subjected them to a thorough pretest; we eliminated items that were [unclear], [ambiguous], or led to perceived overlaps in constructs. [Exploratory factor analysis] yielded a [k]-factor solution, with factor 1 reflecting [construct A] and factor 2 reflecting [construct B]; taken together, the factors explained over [x] percent of the variance. [Items i], [item j], and [item k] could not differentiate between our two constructs, and we dropped them from scale construction. We adopted this factor structure because we (1) had at least three items loading on each factor, (2) eliminated items with high cross-factor loadings, and (3) retained factors with eigenvalues of at least 1.0 ([citations]). Here and throughout the paper, loadings resulting from the [orthogonal rotation] procedure were verified using the [oblique rotation] form ([citation]). Items were standardized to eliminate differences in variance due to scaling and averaged to construct the [construct A] (Cronbach's α = [.x1]) and [construct B] (α = [.x2]) scales. Although these reliabilities fall short of the frequently used threshold of [.70] ([citation]), [methodological authorities] have explicitly stated that this should not be considered a benchmark every scale has to pass; according to [classical test theory], losses in reliability of constructs only make it harder to capture significant relationships between constructs, hence making our analysis more conservative while leaving the likelihood of our making a type I error intact ([citations]).

**与原骨架差异**: 变体 66 是 PCA 把先前状态构念合成**控制变量**（eigenvalue+scree 双判据）；micro manual-coding-validation 变体 B 六环链（预测试→题项依据→反偏差→信度→因子效度→计分）为通用流程。本变体三个增量拍：(1) **双构念区分**——EFA 同时容纳两个焦点构念，跨构念不区分的题项点名剔除（区分效度成为剔除判据，而非仅看载荷高低）；(2) **旋转交叉验证**——正交旋转报告+斜交旋转核验双轨声明，"here and throughout the paper" 一句覆盖全文所有量表；(3) **低 α 保守检验反驳**——不辩"信度够高"，而辩"信度低只削弱检验力、不膨胀 type I error"，把合规短板反转成保守检验主张。与文本构念测量 变体 20（编码者异质程序性保守）同族异机制：彼处是程序设计压低信度仍高，本篇是信度低于阈值但衰减逻辑保护结论方向。

**诚实边界**: 低 α 反驳的前提是构念概念化效度已有独立论证（否则沦为测量失败找补）；衰减论证只保护"检验力不足"方向（不易显著），不保护"虚假显著"方向；三题项下限+eigenvalue≥1.0 是最低标准而非充分标准，勿省略交叉载荷剔除拍。

**适用**: 多题项感知量表、单波问卷多构念同时测量、α 低于 .70 但先例与理论支撑充分的量表。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:m3_scale_discrimination_and_low_alpha_defense -->


### 变体 88：M4 复合构念替代规格三段防御+spline 分解（gulati_2007 型）

**来源论文**: Gulati & Sytch 2007 (Administrative Science Quarterly)
**原始句锚点**: "Given that we had two distinct categories of actors, we opted for the precision of spline estimation, which allowed us to explore the possible variations ... that would not be uncovered in a single variable approach."
**验证状态**: EMERGING（单篇）
**槽位**: M4
**骨架**:
> The [additive] specification of [composite construct] is directly in line with [the original theoretical proposition] ([canon]) and was the choice of other research on similar issues ([citations]). An alternative specification is the [product] of the two components. Because we focus on [ongoing exchange relationships], we have no [zero-dependence cases] and thus run no risk of misrepresenting [the composite] in the instances of [the degenerate case]. More generally, while the [additive] score may be more accurate than the [product] score in some situations ([numeric pair 1]), it could be less accurate in others ([numeric pair 2]). We hence verified our results using a [product] score, and they remained similar. [The stronger alternative] would have to apply at the level of [predictor] and [outcome] given [design constraint], the latter of which is unattainable. We used a [spline] specification to measure the direction of [asymmetry] and differentiate between [side A]'s and [side B]'s [advantage] ([citation]); a single variable would needlessly constrain [one side], eliminating the flexibility and the precision of [spline] estimation ([citation]). Following this decomposition, our sample returned [n1] [dyads] in which [side A] held an [advantage] and [n2] in which [side B] did.

**与原骨架差异**: 变体 83 并置双测量解决**指数可读性**（同构念两个读法+工作例）；文本构念测量 变体 4 用"高相关+统计性质 because"做**多选一**辩护。本变体是复合构念**替代规格的三段防御**：(1) 先例+理论锚定所选规格（原始命题出处+同领域先例清单，"directly in line with ... was the choice of other research"）；(2) 替代规格偏误场景分析——先排除断点退化情形（零依赖），再用具体数值对（如 9–1 vs 3–3 / 1–9 vs 5–5）展示两种规格各自更准的场景，然后以"用替代规格重跑、结果相似"稳健收口（"We hence verified our results using ..., and they remained similar"）；(3) **不可行性边界声明**（语料零覆盖拍）——承认更强技术（如 Edwards polynomial 分解）在本设计下因约束（构念互为 DV/IV、同时性偏误）不可达，以边界诚实替代技术堆叠。spline 变奏：方向性非对称构念用 spline 而非单变量，因为单变量法 "needlessly constrain" 一侧、损失估计灵活性与精度；并报告两侧各占样本量，证明两侧均有变异可估。

**诚实边界**: 不可行性声明须真实——polynomial 不可达的前提（同时性偏误+构念互为 DV/IV）要写明，否则读作偷懒；"results remained similar" 应指向 Results 的具体稳健性表；spline 两侧样本量若严重失衡（如 90/10）须讨论一侧系数的脆弱性。

**适用**: 双边依赖/非对称构念（spline 分解）、加总 vs 乘积复合构念、差值 score 面临 polynomial 质疑的截面与面板设计。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:m4_spline_spec_alternative_defense -->

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
| **用滞后结构声称 Granger causality 但无正式检验（M7 反模式）** | 「allows the results to be interpreted as Granger causality」仅由 t-1/t/t+1 + LDV 支撑，未报检验统计量与 lag 阶数 | 滞后链可写 Granger *口径*；若声称 Granger causality，须报正式检验。Kalaignanam et al. 2013 JM 警示案例 |
| **以 panel vs cross-section 声称 drawing causal inferences（M1 反模式）** | 平衡面板自对照写成 drawing causal inferences | 写 within-unit comparisons；平衡面板不是准实验。Kalaignanam et al. 2013 JM 警示案例 |

## 诚实边界

- **RE vs FE 选择**：必须基于理论（跨单元差异 vs 单元内变化）而非仅凭 Hausman。若理论关注单元内变化但 Hausman 不显著 → 仍应使用 FE 并报告两者比较。ICC 可用于辅助论证但非决定性。
- **多数据库合并**：报告交集前后的 N 差异。若某一数据库匹配率极低（<50%），应解释原因并讨论选择偏误风险。
- **控制变量数量**：19+ 控制变量需提供理论或方法论引用支撑（如 "following [citation], we include a comprehensive set of controls"），且在稳健性中报告简化模型。
- **网络变量与 FE 的交互**：当模型同时包含 dyad FE 和网络变量时，网络变量的 within-dyad 变异可能很小，导致系数估计不稳健，需在 M8 讨论。
