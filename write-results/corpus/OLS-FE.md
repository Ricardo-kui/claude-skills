---
result_type: "OLS-FE"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership_jom"
  - "eilert2017_recall_timing_automobile_jm"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
  - "zhao_ding_gaba_2023_positioning_digital_markets_orsc"
  - "mannor_wowak_bartkus_gomez-mejia_2016_heavy_lies_crown_smj (Strategic Management Journal): null main + significant interaction, one-side conditional slopes, ΔR² economic significance"
  - "bamberger_homburg_wielgos_2021_wage_inequality_jm (Journal of Marketing): marginal significance 90% CI dual-interval reporting"
  - "li_chiu_kong_cropanzano_ho_2026_jom (Journal of Management): interaction percentage economic significance, low-base-rate moderator histogram, five-threat labeled robustness with RIR+Oster+CEM"
  - "ahmadi_khanagha_berchicci_jansen_2017_jms (Journal of Management Studies): 7-model hierarchical regression table navigation, three-way interaction conditional decomposition, asymmetric findings narrative"
  - "cui_yang_vertinsky_smj_attacking_partners (Strategic Management Journal): inverted U-shape + curve moderation, Lind-Mehlum three-step test, turning-point CI, flatten/steepen graph language"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): model-free quartile opening, interquartile economic significance, Heckman two-stage table navigation, alternative-DV falsification, threat-by-threat endogeneity table"
  - "kim_lee_2026_putting_a_price_on_mission_smj (Strategic Management Journal): multi-stage same-IV pipeline attenuation profile, WTP coefficient-ratio economic significance, post-treatment selection caveat, stage-concentrated demographic heterogeneity, Cinelli-Hazlett sensitivity with observed-covariate benchmark"
  - "pupovac_astvansh_carrillat_legoux_2026_pom (Production and Operations Management): cross-sectional OLS/FE on event-study CAR; Control Function + Heckman two-stage correction navigation"
  - "du_tsolmon_2024_post_ma_retention_structural_knowledge_orsc (Organization Science): selection three-step defense (descriptive→CEM→Heckman), null-finding-as-mechanism-evidence, heterogeneity-as-alternative-rebuttal, external-benchmark threshold discovery, downstream performance post hoc, 2x2 cross-diagonal typology comparison"
  - "pollock2015 (Administrative Science Quarterly, 2015): dynamic panel AB-GMM — ρ persistence % interpretation, split-sample Wald χ² coefficient comparison + partial support, Monte Carlo power for GMM null, post-hoc spline reconciliation of surprising negative, 3SLS alternative-estimator robustness with LDV-bias caveat"
  - "malshe2015 (Journal of Marketing, 2015): SUR system — floodlight (Johnson-Neyman) sign-flipping interaction dual transition points, 3-condition cross-equation mediation + asymmetric support, counterintuitive reverse deferred to Discussion"
  - "schumacher_keck_tang_2020_smj (Strategic Management Journal): direct cross-group coefficient test for an imprecise within-group reversal; construct-validity triangulation across nomological contrast, cross-firm stability, and temporal stability"
  - "kashmiri_nicol_arora_2017_jams (Journal of the Academy of Marketing Science): marginal focal result followed by significance-driven control deletion, retained as an anti-pattern rather than a reporting template"
  - "desjardine_li_shi_2025_amj (Academy of Management Journal): min/mean/max marginal-effect table with slope-direction language, collinearity-absorption explanation for full-model interaction attenuation, ITCV omitted-variable threshold defense, dual-benchmarking deviation test, acquisition quasi-natural experiment as influence-channel switch, Bushee investor-type decomposition with Wald test, sequential moderator introduction→paired→full-model navigation"
  - "ridge_et_al_2024_amj (Academy of Management Journal): front-loaded endogeneity defense (RIR replacement count + naive-vs-cure 2SRI pairing), external-evidence practical-importance beat (R5)"
  - "chenganesanliu2009 (Journal of Marketing, 2009): binary strategy as complete mediator of firm characteristics on AR — legacy Kenny joint-read + market-signal coda (R8)"
variants_count: 62
created: 2026-05-18
updated: 2026-08-13
---

# OLS-FE — Results 骨架

## 变体速查表

> 检索辅助（2026-08-08 推广）。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 导航规则

1. 先定槽位（R1–R9，`write-results/SKILL.md` 叙事槽位目录）
2. 查对应槽位组；组内按状态优先：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED
3. 槽位分不开的看「易混决策对」；单篇 EMERGING 变体仅在情境精确匹配时选用
4. 多槽位变体归入首槽位组，副槽位在适用场景列标注

### 槽位分布总览

| 槽位 | 功能 | 变体数 | 变体 |
|---|---|---|---|
| R1 | 描述统计与诊断 | 1 | 20 |
| R2 | 模型序列与表导航 | 7 | 16, 19, 22, 24, 28, 53, 56 |
| R3 | 主假设检验 | 12 | 8, 11, 17, 23, 27, 34, 35, 36, 41, 48, 57, 58 |
| R4 | 交互/调节/阈值 | 9 | 9, 14, 18, 32, 40, 43, 45, 47, 59 |
| R5 | 经济显著性 | 4 | 3, 10, 13, 55 |
| R6 | 非显著/反转/Null | 6 | 4, 6, 30, 37, 42, 60 |
| R7 | 稳健性与威胁处理 | 16 | 1, 2, 7, 12, 15, 25, 26, 29, 31, 39, 46, 49, 50, 51, 54, 61 |
| R8 | 补充/事后/机制 | 7 | 5, 21, 33, 38, 44, 52, 62 |
| R9 | 证据收束（可选） | 0 独立 | 27（R3+R9）；多研究变体4/5 亦用 |

### R1 描述统计与诊断（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 20 | 多项式/交互模型诊断 | 多项式或交互模型估计前的诊断段 | mean-centering+VIF+condition number+非中心化复制；与变体19 配套 | EMERGING | Cui SMJ |

### R2 模型序列与表导航（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 16 | 7 模型层次表导航 | 主效应→双向→三向递进的表导航 | vs 变体19 多项式版本；vs 变体28 双阶段修正 | EMERGING | Ahmadi 2017 JMS |
| 19 | 多项式+多曲线调节序列导航 | 多项式主效应+多个曲线调节的序列导航 | vs 变体16 线性层次版；配套变体20 诊断 | EMERGING | Cui SMJ |
| 22 | 无模型证据开场 | 四分位均值/中位数单调性作结果开场 | vs 变体34 2×2 类型学（分类变量版，见决策对3） | EMERGING | Chung 2022 JAMS |
| 24 | Heckman 两阶段表导航 | 第一阶段表→第二阶段列的表导航 | vs 变体28 双修正导航 vs 变体29 三步防御（决策对7） | EMERGING | Chung 2022 JAMS |
| 28 | 双阶段修正表导航 | 截面二元内生+样本选择的 CF+Heckman 表导航 | vs 变体24 仅选择修正 | EMERGING | Pupovac 2026 POM |
| 53 | 逐调节引入→成对→全模型导航 | 4+ 两向交互按理论 family 成对聚合后全模型 | vs 变体16（三向递进）：两两成对聚合+共线吸收预告 | EMERGING | DesJardine 2025 AMJ |
| 56 | Direct/Indirect/Total 路径表架构 | 中介 climax 做成 Direct vs Total 系数对照 | vs 16/53 层次列；vs 24/28 Heckman 两阶段 | VERIFIED | Kalaignanam 2013 JM |

### R3 主假设检验（10）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 8 | 主效应 null+调节显著 | 主效应不显著但交互显著的条件化再定位 | vs 变体45 亚组吸收 vs 变体27 跨阶段衰减（决策对1） | EMERGING | Mannor 2016 SMJ |
| 11 | 边际显著 90% CI 双区间 | p≈.10 结果的透明双区间报告（副槽位 R8） | 与反模式「p=.052 称显著」对照；常与变体8 配套 | EMERGING | Bamberger 2021 JM |
| 17 | Lind-Mehlum 三步倒 U | 倒 U 主效应完整验证（三步+转折点 CI+Cohen's d） | vs 变体18 倒 U **被调节**（决策对2） | EMERGING | Cui SMJ |
| 23 | P25→P75 四分位距翻译 | 主效应行文经济显著性（副槽位 R5） | vs 变体3 表格版；vs 变体13 交互联合（决策对5） | EMERGING | Chung 2022 JAMS |
| 27 | 多阶段管道衰减 profile | 同 IV 跨序贯决策阶段的方向/显著性对比+跨阶段对比句（副槽位 R9 收束） | 单研究管道 vs 多研究 cross-study；配套 Methods 多研究变体6 | EMERGING | Kim & Lee 2026 SMJ |
| 34 | 2×2 类型学对角比较 | 回归前非参数类型对比作开场 | vs 变体22 四分位单调性（连续版，决策对3） | EMERGING | Du & Tsolmon 2024 OS |
| 35 | ρ 持久性百分比解释 | 动态面板 ρ→「% persists in t」+跨构念对比（副槽位 R5） | 动态面板-GMM 专用；vs 变体23 截面四分位 | EMERGING | Pollock 2015 ASQ |
| 36 | 分样本 Wald χ² + partial support | 跨阈值 χ²(1) 系数相等性+诚实判定 H 支持（副槽位 R6） | vs 变体43 组间差异裁决（决策对6）；vs 变体8 交互条件化 | EMERGING | Pollock 2015 ASQ |
| 41 | 三条件中介+非对称支持 | 跨方程系数乘积+Sobel 三条件中介（同时方程系统） | vs 变体5 MCMC 中介（决策对4）；失败根因定位到条件 | EMERGING | Malshe 2015 JM |
| 48 | 共线吸收解释 | 全模型交互显著性下降归因调节间高相关（Cortina） | vs 变体16 序列导航（只描述不解释）；配套变体53 | EMERGING | DesJardine 2025 AMJ |
| 57 | 测量覆盖范围 warrant「学习」 | a-path 显著后用测量覆盖范围主张学习而非仅修复 | vs 变体41 检验中介是否成立 | VERIFIED | Kalaignanam 2013 JM |
| 58 | 衰减+χ²+Sobel+bootstrap 堆叠确认 | confirmatory 部分中介 | vs 变体41 SUR 非对称；vs 变体5 post-hoc MCMC | VERIFIED | Kalaignanam 2013 JM |

### R4 交互/调节/阈值（8）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 9 | 单侧边际效应报告 | ±1SD 条件边际、不显著侧诚实报告 | vs 变体43 组间裁决；vs 变体14 低基础率直方图 | EMERGING | Mannor 2016 SMJ |
| 14 | 低基础率直方图 | 调节变量低基础率时替代 ±1SD 线图 | vs 变体9 条件边际线图；vs 变体32 外部基准阈值 | EMERGING | Li 2026 JOM |
| 18 | 曲线调节 flatten/steepen | 二阶交互符号+图形语言解释曲线被调节 | vs 变体17 主效应版（决策对2）；vs 变体40 floodlight | EMERGING | Cui SMJ |
| 32 | 外部基准阈值分割 | 权威基准（如 Census）阈值分割+边际效应图双向验证 | vs 变体40 floodlight 数据驱动转折点；vs 变体14 直方图 | EMERGING | Du & Tsolmon 2024 OS |
| 40 | Floodlight 双转折点 | 线性交互符号反转：零交叉+显著性交叉+90% CI 带（副槽位 R5） | vs 变体17/18 曲线；vs 变体32 外部阈值；vs 变体9 ±1SD | EMERGING | Malshe 2015 JM |
| 43 | 组内切换→组间裁决 | 组内方向切换但不显著→直接组间系数差异检验（副槽位 R6） | vs 变体9 单侧边际；vs 变体36 分样本 Wald（决策对6） | EMERGING | Schumacher 2020 SMJ |
| 45 | 亚组吸收+阶段熄灭 | baseline≈0+交互显著→亚组吸收全部优势+中后段熄灭 | vs 变体8 单期条件化 vs 变体27 无亚组版（决策对1） | EMERGING | Kim & Lee 2026 SMJ |
| 47 | min/mean/max 三值边际效应表 | 连续/二元调节的三值边际效应表+斜率方向语言 | vs 变体9 单侧；vs 变体40 floodlight 转折点 | EMERGING | DesJardine 2025 AMJ |
| 59 | spotlight ±1SD + Δslope + region | 一侧显著一侧不显著时的 region 主张（含无方向变体） | vs 变体9 无 Δslope；vs 变体40 floodlight 变号 | VERIFIED | Kalaignanam 2013 JM |

### R5 经济显著性（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | Quartile Penalty 表 | 主效应经济显著性表格化（四分位罚金） | vs 变体23 行文版 vs 变体10 条件边际（决策对5） | VERIFIED | Darby2023 MSOM |
| 10 | ΔR²+条件边际经济显著性 | 增量方差+条件百分比联合论证（调节的条件分解） | vs 变体13 交互联合变化；vs 变体23 四分位距（决策对5） | EMERGING | Mannor 2016 SMJ |
| 13 | 交互联合百分比经济显著性 | IV×M 同时变化 1% 的联合幅度翻译（LIWC 等百分比单位变量适配） | vs 变体10 条件分解；vs 变体23 主效应四分位（决策对5） | EMERGING | Li 2026 JOM |
| 55 | 外部证据实际重要性辩护拍 | 幅度翻译后用外部文献证明微小变化净显著收益 → "likely to be particularly important in practice" | vs 变体13 联合翻译——本变体追加拍5 实际重要性辩护；vs 生存分析变体15 "every day counts" 同拍跨场景 | EMERGING | Ridge et al. 2024 AMJ |

### R6 非显著/反转/Null（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | 小样本/非显著诚实声明 | 任何非显著结果的通用收尾 | 通用兜底 vs 变体37 功效量化（理论关键 null 专用） | VERIFIED | Darby2023 MSOM |
| 6 | 符号反转+当场理论解释 | 同 IV 跨条件/阶段方向相反，定位为 boundary condition | **当场解释** vs 变体42 **延迟解释**；补变体4 未覆盖的反转报告 | EMERGING | Zhao/Ding/Gaba OS |
| 30 | 预测性 null 作机制证据 | 理论预测的 null 排除替代解释（副槽位 R8） | vs 变体37 功效分析；vs 变体25 证伪 | EMERGING | Du & Tsolmon 2024 OS |
| 37 | Monte Carlo 功效分析 | 理论关键 null 交互的功效量化（排除 Type II） | vs 变体4 通用诚实声明；vs 变体30 预测性 null | EMERGING | Pollock 2015 ASQ |
| 42 | 反直觉反转+延迟 Discussion | 预测方向反转当场承认+推迟事后解释 | vs 变体6 当场解释；vs 变体30 预测性 null | EMERGING | Malshe 2015 JM |
| 60 | 调节变量主效应 null 驳斥 rival conjecture | 非假设 null 的可审计写法 | vs 变体30 预测性机制 null | VERIFIED | Kalaignanam 2013 JM |

### R7 稳健性与威胁处理（11）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 稳健性矩阵（Table 9 模板） | 稳健性检验数量多时以矩阵总览 | 表格式 vs 变体2 叙述式 | VERIFIED | Darby2026 JOM |
| 2 | 叙事型逐 Threat 组织 | 稳健性正文逐威胁叙述（**默认首选**） | 4/5 复现，最强的通用基础版；变体15 是其五威胁升级 | VERIFIED | Eilert/Darby×3/Wowak |
| 7 | 替代 DV 作机制验证 | 替代 DV 同向复制确认机制（副槽位 R8） | vs 变体25 替代 DV **预期 null** 证伪（镜像功能） | EMERGING（可选） | Zhao/Ding/Gaba OS |
| 12 | R7 补充作跨样本复制 | 补充分析作为跨样本稳健性复制 | vs 变体21 枚举清单；vs 变体33 下游绩效完整展演 | EMERGING | Mannor 2016 SMJ |
| 15 | 五威胁标签化序列（RIR+Oster+CEM） | 遗漏变量+选择偏误组合电池（金融/会计 gold standard） | vs 变体46 Cinelli–Hazlett 单点敏感性；vs 变体2 基础四威胁；需报 Oster 参数 | EMERGING | Li 2026 JOM |
| 25 | 替代 DV 证伪段落 | 领域外结果的**预期不显著**作证伪 | vs 变体7 同向复制确认（镜像功能）；vs 变体30 预测性 null | EMERGING | Chung 2022 JAMS |
| 26 | 内生性 threat-by-threat 表叙事 | DWH+copula 等内生性检验表汇总叙事 | vs 变体15 五威胁（遗漏变量为主）；vs 变体29 选择偏误防御 | EMERGING | Chung 2022 JAMS |
| 29 | 选择偏误三步防御 | 描述性→CEM→Heckman 递进防御+关联收尾 | 递进深度 vs 变体24 导航 vs 变体26 内生性表（决策对7） | EMERGING | Du & Tsolmon 2024 OS |
| 31 | 替代解释三连驳斥 | 多个替代解释逐一排除+异质性模式裁决收束 | vs 变体25 单一 DV 证伪；vs 变体44 构念效度三角 | EMERGING | Du & Tsolmon 2024 OS |
| 39 | 替代估计器+LDV 偏误警示 | 3SLS 稳健性+用替代估计器失败**反向佐证**主估计器 | 反向佐证 vs 变体2/15 正向稳健性 | EMERGING | Pollock 2015 ASQ |
| 46 | Cinelli–Hazlett 敏感性 | 强观测协变量倍数基准的 confounder 强度论证 | vs 变体15 RIR+Oster（参数化）；corpus 首命中 Cinelli | EMERGING | Kim & Lee 2026 SMJ |
| 49 | ITCV 省略变量阈值 | 双重相关阈值+impact 阈值+最强控制对比（Frank 2000） | vs 变体46 Cinelli 倍数基准；vs 变体15 RIR+Oster | EMERGING | DesJardine 2025 AMJ |
| 50 | 双基准化偏离检验 | 构造"评级−外部基准"差变量，前门基准无关+后门差变量被影响 | vs 变体25 替代 DV 证伪（单 DV）；vs 变体7 同向复制 | EMERGING | DesJardine 2025 AMJ |
| 51 | 收购准自然实验 | 影响通道开关（私有→公开所有权切换）+ 收购前不显著 | vs 变体29 选择偏误防御（无通道切换）；vs 变体26 内生性表 | EMERGING | DesJardine 2025 AMJ |
| 54 | 前端识别防御（RIR 替换计数 + naive-vs-cure 2SRI 配对） | 内生性作为组织威胁且需前置到主结果之前：威胁定位→RIR 替换计数→naive vs 2SRI cure 配对→"consistent across approaches" | vs 变体15 五威胁标签化序列（RIR+Oster+CEM 三件套）——本变体是 RIR 量化替换 + naive-vs-cure 双轨节奏 + 前置；vs 变体2 基础四威胁 | EMERGING | Ridge et al. 2024 AMJ |
| 61 | 面板 GLS 四威胁电池 | 测量/替代估计器/分析单元上卷/滞后 BIC | vs 变体2 通用威胁；滞后 BIC 是规格辩护不是系数稳健性 | VERIFIED | Kalaignanam 2013 JM |

### R8 补充/事后/机制（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | MCMC 显式中介 | 中介机制的显式贝叶斯检验 | vs 变体41 同时方程三条件中介（决策对4）；vs 变体7/25 DV 证伪 | VERIFIED | Darby2023 MSOM |
| 21 | post-hoc 枚举清单 | 事后分析清单化+附录引用 | vs 变体33 完整展演；vs 变体12 跨样本复制 | EMERGING（可选） | Cui SMJ |
| 33 | 下游绩效 post hoc | 时间增长+多指标收敛+提示性收尾 | vs 变体21 清单；vs 变体12 复制；vs 变体5 MCMC | EMERGING | Du & Tsolmon 2024 OS |
| 38 | post-hoc spline 重解释 | 意外负效应用 spline+递减理论重解释（明标 post-hoc） | vs 变体42 延迟到 Discussion；vs 变体6 当场解释 | EMERGING | Pollock 2015 ASQ |
| 44 | 构念效度威胁三角验证 | 按 rival interpretation 组织三类效度威胁（nomological+跨情境+时序） | vs 变体31 替代解释；vs 变体15 稳健性电池 | EMERGING | Schumacher 2020 SMJ |
| 52 | 机制异质性分解（Bushee 类型） | 既有分类把动机/能力操作化为亚型+系数对比+Wald 检验 | vs 变体44 效度三角（多指标收敛）；vs 变体31 替代解释 | EMERGING | DesJardine 2025 AMJ |
| 56 | 二元策略完全中介 + 市场信号（legacy Kenny） | firm chars→策略选择 probit + 策略→AR 显著 + firm→AR 直接路径消失 → complete mediation + 信号收束 | vs 变体41 Sobel/乘积；vs 变体5 MCMC；**必须标 legacy**（决策对4） | VERIFIED | Chen, Ganesan & Liu 2009 (JM); source=chenganesanliu2009 |

## 易混决策对（跨槽位附录——槽位分不开时查这里）

| # | 决策对 | 槽位 | 裁决规则 |
|---|---|---|---|
| 1 | 8 / 27 / 45 | R3 / R3+R9 / R4 | 都处理"主效应在子群/阶段层面的命运"。**单期**（主效应 null+调节显著）→ 8；**管道无亚组分解** → 27；**管道有亚组吸收+熄灭** → 45 |
| 2 | 17 vs 18 | R3 vs R4 | 同一论文姊妹变体：17 倒 U **主效应**（Lind-Mehlum 三步），18 倒 U **被调节**（二阶交互符号+flatten/steepen）。顺序：先 17 后 18 |
| 3 | 22 vs 34 | R2 vs R3 | 都是回归前描述性证据开场：22 **连续变量**（四分位单调性），34 **分类变量**（2×2 类型学对角比较） |
| 4 | 41 vs 5 vs 56 | R3 vs R8 | 都是中介检验：41 **同时方程系统**三条件中介（Sobel+非对称支持+失败根因定位），5 **MCMC 显式中介**（贝叶斯路径，一般面板），56 **二元策略 legacy Kenny 完全中介 + 市场信号**（须标 legacy / 补间接效应区间） |
| 5 | 3 / 10 / 13 / 23 / 35 | R5 / R5 / R5 / R3 / R3 | 经济显著性翻译五件套：3 四分位罚金**表**（主效应表格化）、10 ΔR²+**条件边际**（调节的条件分解）、13 **交互联合**百分比（IV×M 同变）、23 P25→P75 **行文**翻译（主效应）、35 ρ 持久性（动态面板专用）。按效应类型选：主效应→3/23；调节条件→10；交互联合→13；动态面板→35 |
| 6 | 36 vs 43 | R3/R6 vs R4/R6 | 都是分样本系数比较：36 **跨多阈值** χ²(1) 相等性+partial support 判定（发展性假设），43 **单一边界**两侧组间差异裁决（组内切换不显著时用 Chow 类检验） |
| 7 | 24 / 28 vs 29 | R2 / R2 vs R7 | Heckman 家族三件套：24 两阶段**表导航**、28 二元内生+选择**双修正导航**（CF+Heckman）、29 选择偏误**三步防御论证**（描述性→CEM→Heckman 递进）。要导航选 24/28，要论证选 29 |

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `OLS-FE` 专用变体）。

## 累积变体

### 变体 1: 按 Threat 分类的稳健性检验汇总矩阵 (Table 9 模板)
**来源论文**: Darby2026 JOM
**原始句锚点**: "We conducted 19 robustness checks to validate our findings and address potential concerns surrounding the selection of matching covariates and matching method, omitted variables, simultaneity and reverse causality, measurement error, multicollinearity and outliers, and empirical strategy. Taken together, these analyses illustrate the robustness of our results and provide additional support for all three hypotheses."
**验证状态**: VERIFIED（1/5，但生成力极高）
**写入日期**: 2026-05-20
**槽位**: R7
**骨架**:
> We conducted [N] robustness checks to validate our findings and address potential concerns surrounding [threat_1], [threat_2], [threat_3], [threat_4], and [threat_5]. The robustness checks are detailed in the [Appendix_location], and [Table_reference] provides a summary of each approach, appendix and table numbers, and results. Taken together, these analyses illustrate the robustness of our results and provide additional support for all [N] hypotheses.
**与原骨架差异**: 当稳健性检验数量 ≥10 时，使用 Table 9 汇总矩阵按 threat 分类组织，每行包含：(1) 威胁类别；(2) 方法概述；(3) 附录位置；(4) 逐假设结果。这比逐段叙事更可审计。少量稳健性检验 (<5) 时使用叙事型更合适。

### 变体 2: 叙事型稳健性检验 — 逐 Threat 组织 (4/5 复现)
**来源论文**: Eilert2017 JM / Darby2025 JSCM / Darby2023 MSOM / Wowak2025 MS
**原始句锚点**: "Although our empirical analyses accounted for manufacturer- or firm-specific heterogeneity by using clustered standard errors, one could wonder whether there are significant differences between U.S.-, Europe-, and Asia-based manufacturers with respect to how they respond to safety investigations. To test this possibility, we included dummy variables for the manufacturer headquarters and reestimated the recall timing model."
**验证状态**: VERIFIED
**写入日期**: 2026-05-20
**槽位**: R7
**骨架**:
> **[Threat 1 — Omitted Variables]**: One concern is that [threat_description]. To address this, we [method]. The results [are substantively unchanged / continue to support Hypothesis N].
>
> **[Threat 2 — Reverse Causality]**: [...]
>
> **[Threat 3 — Measurement Error]**: Given [data_concern], we used [alternative measure / PSM]. [Key result with economic significance].
>
> **[Threat 4 — Alternative Empirical Strategy]**: To ensure results are not dependent on [specific estimator], we replicated using [alternative_estimator_1] and [alternative_estimator_2]. The results are consistent with our primary findings.
**与原骨架差异**: 标准叙事型稳健性检验模板，按威胁（而非按表格）组织。每个威胁一个段落。与变体1 (Table 9 矩阵) 互补——5-10 个检验时用叙事型，10+ 时用矩阵型。

### 变体 3: 经济显著性的 Quartile Penalty Table (1/5 复现)
**来源论文**: Darby2023 MSOM
**原始句锚点**: "To further understand the practical implications, we examined how these market penalties change across quartiles of the Time-to-Recall measure for the smallest and largest significant effect sizes. For example, Table 5 indicates that moving from the first quartile (10 days) to the second quartile (33 days)—an approximately three-week delay in time-to-recall—is associated with an increase in the stock market penalty ranging from 82% to 124%."
**验证状态**: VERIFIED（高价值）
**写入日期**: 2026-05-20
**槽位**: R5
**骨架**:
> We interpret the practical implications using the smallest ([window_1]) and largest ([window_2]) significant effect sizes to provide a range of the potential [penalty/benefit]. A one-standard-deviation increase in [DV] is associated with a [outcome] ranging from [min]% to [max]%. To further understand the practical implications, we examined how these [penalties] change across quartiles of the [DV] measure. The range of [penalties] is presented in [Table], which illustrates meaningful increases across quartiles. For example, moving from the first quartile ([N] [units]) to the second quartile ([N] [units])—[practical_interpretation]—is associated with an increase in the [outcome] ranging from [min]% to [max]%.
**与原骨架差异**: 将经济显著性从 "1 SD → X%" 升级为完整的 quartile-by-quartile 解释。Darby2023 的 Table 5 是标杆——从 Q1 (10 days) 到 Q4 (365 days) 的 penalty 递增清晰展示了非线性惩罚结构。

### 变体 4: 小样本/非显著结果的诚实声明 (1/5 复现)
**来源论文**: Darby2023 MSOM
**原始句锚点**: "Although our theorizing supports the notion that CEOs may care less about low-severity recalls given their limited ramifications, we note that the nonsignificant effect for low-severity recalls could also simply be an artifact of the small sample size for low-severity recalls."
**验证状态**: VERIFIED（所有研究都该用）
**写入日期**: 2026-05-20
**槽位**: R6
**骨架**:
> Although our theorizing supports [theoretical_explanation], we note that the [null/mixed] effect for [subset] could also simply be an artifact of the small sample size for [subset] ([N] observations).
**与原骨架差异**: 这是**非显著结果诚实报告**的标杆句式。不将 null finding 过度理论化（"CEOs care less"），而是在理论解释后立即补充统计功效的替代解释（"could also simply be an artifact of the small sample size"）。适用于任何小样本分组出现非显著结果的情况。

### 变体 5: Post Hoc — MCMC 显式中介分析 (1/5 复现)
**来源论文**: Darby2023 MSOM
**原始句锚点**: "To conduct this analysis, we used a Markov Chain Monte Carlo (MCMC) simulation method with 20,000 draws. The results indicate that time-to-recall partially mediates the relationship between CEO stock ownership and stock market returns for event windows CAR(−1,0), CAR(−1,1), and CAR(−1,5) for all recalls."
**验证状态**: VERIFIED
**写入日期**: 2026-05-20
**槽位**: R8
**骨架**:
> Our post hoc analysis addresses implied relationships—[IV] may influence [DV_2] through [DV_1]. To examine this, we used an explicit mediation approach that explores evidence of indirect effects ([citation]). The explicit mediation method simulates multiple draws of indirect effects that are the product of [coefficient_path_a] and [coefficient_path_b]. Evidence of mediation is identified by examining the 95% confidence interval for the mediation pathway. If the interval does not contain zero, mediation is supported. To conduct this analysis, we used a Markov Chain Monte Carlo (MCMC) simulation method with [N] draws ([citations]). The results indicate that [DV_1] partially mediates the relationship between [IV] and [DV_2] for [conditions]. Overall, as [IV] increases, [DV_1] increases, and this [change_in_DV_1] leads to greater [DV_2].
**与原骨架差异**: MCMC 显式中介（如 Imai et al. 或 Beer & Qi 2024 方法）替代了传统的 Baron & Kenny 三步法或 bootstrapping。关键要素：(1) 方法引用；(2) 模拟次数 (20,000 draws)；(3) 95% CI 不含 0 → mediation 成立；(4) "partially mediates" 而非 "fully mediates"（学术诚实）。

### 变体 6: 符号反转跨条件的诚实报告 — Sign Reversal Across Conditions with Theoretical Explanation (1/6 复现)
**来源论文**: Zhao/Ding/Gaba 2023 (Organization Science)
**原始句锚点**: "Instead, in Model 2, overall dissatisfaction has a negative and significant effect (p = 0.002) and evaluation heterogeneity has a positive and significant effect (p = 0.02). The magnitudes are notably smaller, roughly one-half to one-third of those for initial positioning."
**验证状态**: EMERGING（单篇入库；corpus 此前仅有 null-finding 变体4，方向反转报告为真实空白）
**写入日期**: 2026-06-17
**槽位**: R6
**骨架**:
> In the main analyses, [IV] is [pos/neg] and significant. ... These patterns do not hold for [condition/subsample]. Instead, in Model [X], [IV] has a [opposite-direction] and significant effect. The magnitudes are notably smaller, roughly [one-half to one-third] of those for [baseline condition]. In Model [Y], the interaction effect between [condition indicator] and [IV] is [opposite] and significant, suggesting that the [baseline] effect of [IV] is significantly attenuated in [condition].
>
> The sign reversal ... may also suggest a shift in how [actors] translate the same [signal] into actions, once they have accumulated [internal knowledge]. For [baseline condition], [actors] primarily seek [acquisition / first-order goal]. ... In [condition], [actors] can draw on [internal knowledge], and their objectives may shift toward [retention and monetization / second-order goal]. In that context, a high [IV] signal may be interpreted as [alternative meaning], [direction of revised behavior]. ... For [condition], [actors] no longer systematically [differentiate from / imitate] [reference] in response to [IV]. Taken together, [IV] strongly guides [baseline], but its influence diminishes as [actors] accumulate firsthand experience.
**与原骨架差异**: corpus 此前只有变体4（小样本 null finding 的诚实声明），未覆盖**同一 IV 在不同条件/阶段方向相反**的 nuanced finding。本变体的核心是"方向反转 + 幅度衰减 + 交互确认 + 反转的理论解释"四件套：(1) 先报主分析方向，再报反转方向；(2) 量化幅度衰减（one-half to one-third）；(3) 用交互项确认衰减显著；(4) **给反转一个理论解释**（不是 statistical artifact，而是 actors 的目标/信息基础随条件改变：acquisition vs retention）。关键：把反转定位为 **boundary condition**（"influence diminishes as..."），而非失败——既诚实又有理论增量。适用于任何"同 IV 跨样本/阶段/条件符号变化"的报告（如 initial vs subsequent、pre vs post、新进入者 vs 在位者、treated vs control 子群）。

### 变体 7: 替代 DV 作机制验证 — Alternative DV as Theoretical Validation (1/6 复现)
**来源论文**: Zhao/Ding/Gaba 2023 (Organization Science)
**原始句锚点**: "To examine this, we introduce an alternative dependent variable, peripheral distance to the core, which captures how far an app's peripheral functions are from its core function in the semantic space. … This provides additional evidence that dissatisfaction is associated with novelty seeking not only through differentiation from successful competitors but also through the selection of peripheral functions that are less tightly coupled to the core."
**验证状态**: EMERGING（可选；中价值，扩展 R7 的理论功能）
**写入日期**: 2026-06-17
**槽位**: R7 / R8
**骨架**:
> [Our theory / Another relevant aspect] also involves [theoretical dimension not captured by main DV]. To examine this, we introduce an alternative dependent variable, [alt-DV], which captures [theoretical dimension] — [operational definition]. Because [each construct has a vector over the keyword dictionary], we first compute [pairwise distance metric, e.g., Jensen-Shannon] for all [constructs]; we then [rescale / aggregate] and calculate the [weighted distance] between [component A] and [component B]. [IV_1] has a [pos/neg] and significant effect on [alt-DV] (p < [thr]), whereas [IV_2] is insignificant. This suggests that, when [IV_1 condition], [actors] tend to [behavior]—consistent with a [theoretical-label] positioning. This provides additional evidence that [IV_1] is associated with [mechanism] not only through [primary channel] but also through [secondary channel].
**与原骨架差异**: 现有 R7 变体（变体1 Table 9、变体2 narrative）都把稳健性定位为**威胁缓解**（rule out confound / alternative estimator）。本变体扩展 R7 的理论功能：用替代 DV **corroborate 机制**而非缓解威胁——引入一个捕捉主 DV 未覆盖维度的替代结果变量（如"peripheral 与 core 的语义距离"），若与主 DV 同向则支持机制。关键区分：明确标 "to further understand / provides additional evidence that... not only through [primary] but also through [secondary]"，把它定位为机制验证而非稳健性。当理论含多个可分离的预测通道时尤其有用。

### 变体 8: 主效应不显著但调节显著 — 条件化再定位 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: "Although the coefficient was in the expected positive direction, Model 2 shows that job anxiety was not a significant predictor of social buffering (β = 0.24, n.s.). Hypothesis 1 was thus not supported. … The significant negative coefficient on the interaction term in Model 3 (β = −0.38, p < 0.01) lends support to Hypothesis 3."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R3+R4
**骨架**:
> Hypothesis [N] predicted a [positive/negative] relationship between [IV] and [DV]. In Model [X], the coefficient for [IV] was in the predicted direction but not statistically significant (β = [value], n.s.). Hypothesis [N] was thus not supported as a main effect. However, the interaction between [IV] and [moderator] in Model [Y] was [positive/negative] and significant (β = [value], p < [threshold]), lending support to Hypothesis [N+1]. Marginal effects at [±1 SD] of [moderator] revealed a significant effect of [IV] on [DV] under [low/high moderator] conditions (dy/dx = [value], p < [threshold]) but not under [opposite] conditions (dy/dx = [value], n.s.). This pattern suggests that [IV] does influence [DV], but primarily under [boundary condition].
**与原骨架差异**: 当主效应假设被拒绝、但交互效应支撑条件关系时，本骨架将"失败"重新框定为理论条件化——方向正确但不显著→交互显著→条件分解→"does influence, but primarily under"。关键技巧：(1) 先诚实承认 H1 不被支持；(2) 迅速过渡到"However..."；(3) 报告边际效应的条件显著性；(4) 最后一句"does influence... but primarily under" 将叙事从失败转向边界发现。诚实边界：事后将不显著主效应重新框定为边界条件需要理论支持——如果交互没有事前假设，不能这样做。

### 变体 9: 调节效应边际效应的单侧显著报告 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: "We found a significant negative marginal effect of job anxiety in gain contexts (dy/dx = −1.16, p < 0.01) but no significant effect in loss contexts (dy/dx = −0.29, n.s.)."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> To further explore the nature of this interaction, we examined the conditional marginal effects of [IV] on [DV] at [low] and [high] levels of [moderator] (typically [±1 SD] from the mean). When [moderator] was [low/high], [IV] had a [positive/negative] and significant effect on [DV] (dy/dx = [value], p < [threshold]). In contrast, when [moderator] was [opposite level], the effect was not statistically different from zero (dy/dx = [value], n.s.). [Figure X] illustrates this pattern.
**与原骨架差异**: 标准交互报告通常报告两端的简单斜率，但当一侧显著、一侧不显著时，需要明确区分而非对称报告。本骨架使用"dy/dx"而非"simple slope"措辞（在 Stata 的 margins 框架下更自然），且明确将不显著侧标注为"not statistically different from zero"而非暗示有方向。

### 变体 10: ΔR² + 条件边际效应嵌入经济显著性 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> We assessed the economic significance of [IV]'s effect by examining the incremental variance explained (ΔR²) when [IV] and its interaction with [moderator] were added to the baseline model. The addition of [IV] and [moderator × IV] increased R² by [Δvalue] ([F_stat], p < [threshold]), indicating that the conditional relationship accounts for meaningful variation in [DV] beyond the control variables. Under [condition_A] ([moderator] at [level_A]), a [1-SD/unit] increase in [IV] is associated with a [N]% change in [DV] relative to its mean, representing a substantively important shift. Under [condition_B] ([moderator] at [level_B]), the marginal effect is negligible ([value], n.s.).
**与原骨架差异**: 将 ΔR² 和条件边际效应百分比联合使用来论证经济显著性：(1) ΔR² 论证"模型改进显著"；(2) 条件分解论证"在特定条件下效应有实质意义"；(3) 不显著侧的 negligible 声明呼应变体9的单侧显著性。

### 变体 11: 边际显著 90% CI 双区间透明报告 (1篇高价值)
**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**原始句锚点**: "As in Study 1, the total effect of wage inequality on short-term profitability is positive but reaches only marginal statistical significance (Est. = .21, p < .10, 95% CI: [−.01, .49], 90% CI: [.04, .44])."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R3/R8
**骨架**:
> The total effect of [IV] on [DV] is [directional] but reaches only marginal statistical significance (Est. = [value], p < .10, 95% CI: [[lower], [upper]] crosses 0, 90% CI: [[lower], [upper]] does not cross 0). This suggests that [theoretical claim] receives weak but directionally consistent support.
**与原骨架差异**: 与"p < .10"的简单声明相比——(1) 同时报告 95% 和 90% 两个 CI；(2) 明确指出哪个 CI crosses 0、哪个不跨；(3) "weak but directionally consistent support" 是标准措辞。诚实边界：p < .10 只能在有理论预测方向且与理论一致时使用；不能用于探索性分析。

### 变体 12: R7 补充分析作为跨样本稳健性复制 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**原始句锚点**: "We performed a supplementary analysis to investigate whether our strategic risk taking results were robust to alternative study contexts and measurement techniques. To do so, we constructed a sample of public company CEOs listed in the Execucomp database who began their tenures in 2008 and remained in their positions for at least four years."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> We conducted a supplementary analysis using an alternative sample to examine whether our findings generalize beyond [primary_sample]. Specifically, we replicated our core models using [alternative_sample: e.g., a sample of public firms from the same industry / external survey data / a different time period]. The results ([Appendix Table]) indicate that [key findings: e.g., the main effect of IV on DV remains significant (β = [value], p < [threshold]); the interaction between IV and moderator remains significant (β = [value], p < [threshold])]. These supplementary findings increase confidence that our results are not idiosyncratic to [primary_sample] and generalize to [broader context].
**与原骨架差异**: 跨样本复制比替代测量复制更高级——不是同一数据的另一种测量方式，而是完全不同的数据源/样本。关键：(1) 明确标注为"supplementary"而非核心发现；(2) 声明目的（generalizability > robustness）；(3) 与主分析并行的 replica 结构（逐假设报告方向+显著性）。适用于主要分析受限于特定样本（如访谈/实验样本）的研究。

### 变体 13: R5 交互效应百分比经济显著性 — 联合变化的幅度解释 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: "A 1% increase in CEO achievement expression and mortality salience was associated with a 3.17% increase in ATV around the call. A 1% increase in CEO achievement expression and mortality salience was associated with a decrease of 5.17 units in investor negative sentiment."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> A [N]% increase in [IV] and [moderator] was associated with a [N]% increase in [DV] around the [event]. / A [N]% increase in [IV] and [moderator] was associated with a decrease of [N] [units] in [DV].
**与原骨架差异**: 现有变体3（Darby Quartile Penalty Table）、变体10（Mannor ΔR²+条件边际效应）的经济显著性均针对主效应或调节效应的条件分解。本骨架针对的是**交互效应本身的联合经济含义**——当 IV 和 moderator 同时变化时的幅度翻译。Li et al. 的独特策略：(1) 将交互效应的经济显著性从"simple slope at ±1SD"翻译为"1% joint increase → Y% change"；(2) 对于不同的 DV 使用不同的翻译单位——百分比（ATV: "% increase"）和绝对单位（sentiment: "decrease of N units"）；(3) 嵌入在 R3 假设检验段落后立即给出，而非独立段落。适用于连续×连续的交互效应（特别是 LIWC 文本变量，其自然单位就是百分比）。
**诚实边界**: 联合变化的解释（"1% increase in X and M → Y% change in DV"）假设 IV 和 moderator 同时同方向变化，这在现实中可能不成立——应补充说明"when both increase by 1%"而非暗示它们总是共变。

### 变体 14: R4 低基础率调节变量的边际效应直方图 — 替代传统 ±1SD 线图 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: "We further plotted the marginal effects using histograms. Given that CEOs' use of death-related communication during the calls has a low base rate, for easier interpretation, we display different levels of mortality salience based on the actual counts of death-related words (0, 1, 3, and 5 words)."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> We further plotted the marginal effects using histograms. Given that [moderator] has a low base rate ([N]%), for easier interpretation, we display different levels of [moderator] based on the actual counts of [moderator_unit] ([count_1], [count_2], [count_3], and [count_4] [units]). Figure [N] shows that [IV] was more [positive/negative] related to [DV] when [moderator] was higher. / For [DV_2], we graphed the interaction based on cases without [moderator_unit] and those containing such [units], since most observations with [moderator] in this sample used one [moderator_unit]. Figure [N] illustrates that [IV] [effect_description] under higher [moderator].
**与原骨架差异**: 传统交互效应图使用 ±1SD 线图，但低基础率变量（如 CEO 死亡词使用率 3.61%）的 ±1SD 可能落入负值区域或无实际对应的观测值。Li et al. 的解决方案：(1) 使用**边际效应直方图**替代传统线图——X轴为 moderator 的实际离散值（0, 1, 3, 5 词），Y轴为 IV 的边际效应；(2) 在极端低基础率时（如仅 0 vs ≥1），退化为二分类比较图——"cases without death words vs cases with death words"；(3) 图中附置信区间条。关键策略：不假装低基础率变量是连续的，而是**按实际取值离散化展示**。适用于任何稀有文本特征、罕见事件计数、或高度偏态的调节变量。
**诚实边界**: 边际效应直方图（或离散比较图）必须标注每个 bin 的观测数量——低基础率变量的某些 bin 可能仅包含极少数观测，此时边际效应估计不稳定。若某 bin N < 30，应在图中或注释中标记。

### 变体 15: R7 五威胁标签化稳健性序列 — RIR+Oster+CEM组合 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**原始句锚点**: "We conducted a series of supplementary analyses to determine the robustness of our findings. First, to rule out the possibility of omitted variable bias, we performed the robustness of inference to replacement (RIR) test and Oster's delta test."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> We conducted a series of supplementary analyses to determine the robustness of our findings. First, to rule out the possibility of [threat_1: omitted variable bias], we performed the [test_1: RIR test] and [test_2: Oster's delta test]. The results from these tests indicate that our empirical findings are robust against [threat_1] ([appendix_location]). Second, we checked whether [alternative_explanation: e.g., death communication type] interacted with [IV] and [moderator]; however, we found no meaningful moderating effect on [DV] (see [appendix_location]; also refer to our [prior_studies] for the [related_type] results related to this analysis). Third, it is likely that [specific_subsample: e.g., pharmaceutical firms] may [bias_direction: use more death-related language]; we tested our models by excluding [subsample] and found consistent results ([appendix_location]). Fourth, since recent studies have measured [construct] using [alternative_measure] ([citation_1]; [citation_2]), we substituted [original_measure] with [alternative_measure]. The results show no direct effect or interaction with [IV] across the models. Additionally, the findings remain consistent when [alternative_measure] is included as a control. Finally, given the low base rate ([N]%) of [condition], we employed coarsened exact matching (CEM) to create a matched sample to reduce potential bias in the analysis. For the matching criteria, we included [matching_variables: e.g., quarter, analyst recommendation, firm size, call length, CEO gender] ([citation_1]; [citation_2]; [citation_3]). The percentage of [condition] increased to [N]% in the matched sample, aligning closely with the main test results based on the full sample ([appendix_location]). A summary of our results is available online in [appendix_summary].
**与原骨架差异**: 现有变体2（叙事型逐威胁组织）提供了标准四威胁模板（omitted variables + reverse causality + measurement error + alternative estimator）。Li et al. 升级为**五威胁+两稀有检验组合**：(1) RIR + Oster's delta 联合处理遗漏变量——这是 recent 顶刊（特别是金融/会计领域）的 gold standard，替代传统的"add more controls"；(2) 死亡类型分析——将 moderator 分解为 literal vs pseudo 子类型并检验是否调节主交互，创建"null interaction on interaction"的 meta-robustness；(3) 制药企业排除——针对特定行业的混淆检验（pharma firms 可能更频繁使用死亡相关语言）；(4) 替代测量替换——独立董事死亡替代 CEO 死亡词（construct-level replication）；(5) CEM 匹配处理低基础率选择偏误——匹配后的 moderator 比率从 3.61% 升至 11.33%。最后以 "A summary of our results is available online in Appendix [N]" 收尾。
**诚实边界**: RIR + Oster 组合需要在 Methods 或 Appendix 中解释两个检验的选择参数（如 RIR 的 replacement threshold、Oster 的 δ 和 Rmax）。仅说 "results are robust to omitted variable bias" 而不报告参数 → 审稿人会要求补充。


<!--
pattern_id: heckman_selection_preflight_rationale
build_type: 估计器前置交底型（修正型估计器动机论证）；跨估计器（任何 selection/内生性修正作为主估计策略的设计）
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定 R7-2 叙事 threat 四拍 VERIFIED）
-->

### 变体 76：R2 Heckman 选择模型前置交底 — 威胁类比 + 两阶段程序 + 风险集/SE 修正披露 (1篇高价值)

**适用场景**: selection/内生性修正（Heckman、CF、2SLS 等）是**主估计策略**而非稳健性附件时，在主结果之前用独立小节交底：为什么有选择问题（带类比论证）、估计器性质、两阶段程序、风险集与标准误修正。读者带着"修正了什么、代价是什么"的预期进主表。
**排列模式**: 威胁定位+类比 → 估计器性质论证 → 两阶段程序 → 风险集/SE 修正交底 → 预处理交底
**范文来源**: Higgins & Gulati (2003), *Organization Science*
**结构锚定**: R7-2 叙事型逐 threat 四拍（VERIFIED）的威胁定位拍改造为前置动机拍

**骨架**:
```
[威胁定位 + 类比论证]
For each set of analyses, we used Heckman selection models to guard against
the possibility of sample selection bias ([Heckman citation]). In general,
sample selection can arise when the criteria for selecting observations are
not independent of the outcome variables. As an example, [familiar analogous
setting, e.g., earnings studies of workforce participation] can run the risk
of sample selection bias if they do not account for factors that affect
[the selection process].

[映射到本文 + 估计器性质]
Here, since we are studying [outcomes] that only occur when [selection event
occurs], we want to guard against the possibility that there is some other
factor, in addition to those we study, that accounts for the likelihood of
[selection event] in the first instance. [Estimator]'s procedure generates
consistent, asymptotically efficient estimates that can enable us to
generalize to the larger population of [full risk set] ([citation]).

[两阶段程序 + 风险集/SE 交底]
In essence, the [estimator] model is a two-stage procedure that uses the
larger risk set of [full sample description] (n = [N_risk]). [First-stage
estimator] was used to estimate the likelihood of [selection event] during
the first stage, and estimates of parameters from that model were then
incorporated into a second-stage regression model to predict [DV] ([citation]).
For the first stage models, we used the information we had available for our
[full sample]—[selection predictors]—to predict likelihood of [selection event].
In the second stage, though the sample includes all [N_risk] firms, the
standard errors reported reflect the smaller sample of firms (n = [N_analytic]).

[预处理交底]
To account for the fact that we had [DV] information that spanned [time span],
we transformed our [DV] estimates into [constant-dollar adjustment] and logged
the estimates. And, in order to account for [time-varying conditions], we
included the [market condition variable] described earlier in all of our
analyses. The numbers we used were calibrated not just by the [year] but also
by the [finer temporal unit] preceding the [event], which produces fairly
fine-grained estimates.
```

**为什么有效**: 修正型估计器最大的读者障碍是"修正了什么、凭什么信"——前置小节用熟悉类比（如劳动力参与）把抽象 selection 问题翻译成直觉，再交底程序与 SE 修正的代价（第二阶段 SE 反映分析样本而非风险集），可信度论证先于结果出现；这与 Results 内表导航（变体 24/28）和事后防御（变体 29）功能互补不重叠。
**注意事项**:
- SE 修正交底是诚实亮点：明确第二阶段标准误反映分析样本（n=296）而非风险集（n=838），不可省略
- 第一阶段选择方程的预测变量须交底；现代标准还要求排除限制论证（本文未满足，采用时应补 instrument 论证，参照 r2/r7 Heckman 权威骨架）
- 估计器性质句（consistent, asymptotically efficient）保留原文表述强度，不升级为因果语言；结果段语言用 associated with
- 因果语言校准：selection 修正 ≠ 因果识别，正文判决句不得用 effect of
**反模式**: 把前置交底写成方法复述（公式推导/程序细节搬自教科书）——交底只回答"为什么需要修正+修正的代价"，技术细节留给 Methods。
**原文锚点**: "For each set of analyses, we used Heckman selection models to guard against the possibility of sample selection bias (Heckman 1979)."（Analysis 第1段）

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:heckman_selection_preflight_rationale -->

### 变体 66: R7 — 三威胁小节化稳健性：选择性/内生性 → 替代估计 → 构念效度（post_2022_women_tmt_strategic_renewal 型）

**来源论文**: Post, Lokshin & Boone 2022 (AMJ)
**验证状态**: VERIFIED（expert_audit_override, user 2026-08-29）
**槽位**: R7（独立 "Robustness Checks" 小节，falling action）

#### 报告骨架

```text
Our first robustness check addressed the possibility that [threat_1: endogeneity or
selectivity] affected our results. [treatment] may be conditional on [selection
mechanism] ([citations]). To address this possibility, we re-estimated our models on the
subsample of our data when [condition occurs]. Overall, the results do not suggest that
[threat_1] biased our results (see Online Appendix [X]). Our second robustness check
assessed the indirect paths from [treatment] to [outcomes] using [SEM/GSEM commands].
The [alternative] model differs from our [baseline] approach in that it allows for
correlations among the error terms of our [equations]. The [alternative] results are
largely similar to our reported results. Finally, to further investigate the construct
validity of our [construct] variables, we re-estimated the models substituting the focal
dependent variables with [alternative DV 1] and [alternative DV 2], respectively. As
expected, we find that [treatment] significantly [affects] [alternative DV 1],
especially when [moderator condition].
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 序数威胁命名 | "Our first/second ... robustness check addressed the possibility that ..." | threat-based 而非按表格罗列 |
| 2. 每威胁一句机制引证 | 选择机制引 Zhang & Rajagopalan 式文献 | threat 不是假想敌 |
| 3. 替代估计须说清差异 | "differs ... in that it allows for correlations among the error terms" | 告诉读者替代估计多检验了什么 |
| 4. 构念效度用替代 DV 且方向预期 | "As expected, we find ..." | 替代 DV 是收敛证据不是安慰剂 |
| 5. 细节外包 Online Appendix | 正文一句结论 + 附录指引 | 主文节奏不被稳健性淹没 |

#### 原文锚定
- "Our first robustness check addressed the possibility that endogeneity or selectivity affected our results."（results.md Robustness Checks 节）

#### 与最近变体的区别
- 区别于 r7_ols_threat_based / 变体 15（五威胁标签化序列）：本变体是"选择性/内生性 → 替代估计器（SEM 递归）→ 构念效度替代 DV"三威胁小节化组织，且第三威胁以替代 DV 的方向性预期收尾。

### 变体 16: R2 7模型层次回归表导航 — 主效应→双向→三向递进 (1篇高价值)
**来源论文**: Ahmadi, Khanagha, Berchicci & Jansen 2017 (Journal of Management Studies)
**原始句锚点**: "Model 1 includes the main effects, the traits, and manipulations, to test hypotheses 1a and 1b. … Model 5 shows the results of the three-way interaction between complexity, promotion-focused context, and promotion focus trait."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R2
**骨架**:
> [Table N] presents the descriptive statistics and correlations and [Table N+1] presents the results of the regression analyses. The power of the full model is above [N] per cent. Model 1 includes the main effects, the traits, and manipulations, to test hypotheses [H_labels]. We find that [control_finding_of_note: e.g., complexity has a direct and positive effect on DV, and this suggests that, when faced with complex decision-making tasks, managers tend to embrace exploratory activities]. Turning to our main independent variables, we find that [H_summary: e.g., the regulatory focus trait is associated with the DV]. [IV_1] is found to be [direction] associated with [DV] (B = [value], SE = [value], p < [threshold]), while [IV_2] is [direction] associated with it (B = [value], SE = [value], p < [threshold]). These findings are consistent with hypotheses [H_labels].
>
> To test hypothesis [H_interaction] relating to [moderator mechanism: e.g., regulatory fit], we followed [citation] and included the interaction of [moderator] and [IV_trait] in Models [N] to [N+n]. We find that the interaction between [condition_A] and [trait_A] is [significant/not statistically significant]. Thus, our hypothesis [H_label] is [supported/rejected]. However, the interaction between [condition_B] and [trait_B] is found to be [significant] (B = [value], SE = [value], p < [threshold]). The simple slope test confirms the difference between slopes (t = [value], p = [value]). To ease the interpretation, we plotted the interaction effect. Figure [N] shows that [condition_B] can intensify the [direction] effect of [trait_B] on [DV]. Model [N+final] includes both interaction terms.
>
> Model [N+final+1] shows the results of the three-way interaction between [moderator_1], [moderator_2], and [IV]. The coefficient is statistically significant (B = [value], SE = [value], p < [threshold]), which is consistent with hypothesis [H_3way]. Further, we tested the conditional effect of two-way interactions at the two values of [moderator_1]. The result confirmed that the two-way interaction is indeed significant (B = [value], p < [threshold]) under the high [moderator_1] condition, but non-significant (B = [value], p > [threshold]) under the low [moderator_1] condition. Moreover, we tested the difference between simple slopes. The difference is significant (t = [value], p < [threshold]) between the slope of the [condition_A]-high [moderator_1] condition and the slope of the [condition_B]-high [moderator_1] condition. However, a similar test on the difference between the slope of the [condition_A]-low [moderator_1] condition and the slope of the [condition_B]-low [moderator_1] condition proved to be non-significant (t = [value], p > [threshold]).
**与原骨架差异**: 本骨架是**实验层次回归的完整表导航模板**，适用于拥有多个特质IV、多个操纵调节变量、两向和三向交互的实验设计。Ahmadi et al. 使用7模型递进结构：(1) M1主效应（trait IV + manipulated variables）；(2) M2-M4两向交互（逐个添加交互项，Higgins et al. 2003范式）；(3) M5-M7三向交互（逐个添加三向项）。关键策略：(a) 将控制变量的显著发现也纳入叙事——"complexity has a direct and positive effect... this suggests that..."——即使不是假设的一部分，也为后续交互提供了情境锚定；(b) 逐个假设报告而非一次性报告所有模型——每段对应一个假设/一组假设，M1→H1a+b, M2-M4→H2a+b, M5-M7→H3a+b；(c) 三向交互的条件分解——在主效应中测试"在哪个调节水平上两向交互显著"，再用t-test比较跨条件的简单斜率差异。适用于任何含多个trait IV + 多个manipulated moderator的2×2实验设计。
**诚实边界**: 7模型表可能过于密集——必须在表注中明确每个模型包含哪些变量。若某些交互项的加入导致其他系数符号反转或显著性变化（如promotion focus从Model 1显著到Model 2不显著），必须在正文中讨论而非沉默。

[功能标签]: R6 非显著结果 — null 作为竞争策略裁决的证据
[骨架]: "Column [IV] of Table [X] shows that [event] did not impact [outcome] (β [value], p > [threshold]). ... [在异质性/分解处回收 null:] This finding corroborates the theoretical insight we drew from Column [II]. ... The evidence thus supports the [strategy_A], while supporting neither the [strategy_B] nor the [strategy_C]."
[关键特征]: 变量级 null（Brand Ad 不变、Recall×Price Ad 不显著）不被跳过也不降级为'部分支持'，而是被用作**裁决竞争性策略解释**的排除证据——null 排除 harm-avoidance/sales-preemption，显著项独占 quality-signaling；裁决句式 'supports [A], while supporting neither [B] nor [C]' 一次收束三个解释
[适用]: 无编号假设、以竞争策略/机制解释组织的 Results；分解设计中对不显著成分的策略性使用
[节奏标记]: [null 系数+显著性][null 实质命名（'did not impact'）][跨列回收][三策略一次裁决]
**原始句锚点**: "The evidence thus supports the quality-signaling strategy, while supporting neither the sales-preemption strategy nor the harm-avoidance strategy."
**来源**: fang_et_al_2025_rival_recall_ad_spend (POM), §5.2


<!--
pattern_id: hypothesis_verdict_chain_null_concession
build_type: 假设判决导航型（逐假设段落组织）；跨估计器（层次回归/选择模型等多模型多假设设计通用）
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定 R3 四拍主骨架——本变体管判决的段落编排，幅度拍须按主骨架补齐）
-->


<!--
pattern_id: bk_sobel_partial_mediation_cross_dv_replay
build_type: 假设化中介展演型（中介是正式假设 H 的检验而非 post hoc 机制探索）；多 DV 复制设计
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定变体 58 confirmatory 部分中介堆叠确认 VERIFIED）
-->


<!--
pattern_id: theory_motivated_additional_analyses
build_type: 理论驱动补充分析组织型（非 threat 响应的 post hoc 分析编排）；跨估计器通用
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定 R7-2 叙事四拍 VERIFIED——threat 定位拍替换为理论动机定位拍）
-->


<!--
pattern_id: r6_unsupported_verdict_with_pattern_restatement
estimator_family: OLS/FE 及分组比较设计通用（R6 非显著处理）
slot: R6（不支持裁决 + 以假设语言重述实际模式）
source_papers: ["gulati2005-adaptation-vertical"]
confidence: EMERGING（单篇 full_text_verified，待第二篇交叉验证）
-->


### 变体 83：配对反号假设的反例合并判决（gulati_sytch2007 型）

**适用场景**: 两个方向相反的配对假设（H_a 预测正向、H_b 预测负向）在检验中双双失败且失败方式不同——一个显著反号、一个 null。此时两个判决共享一句合并句，反例密度最高且不显混乱。

**报告节奏**: [配对假设重述（方向相反）] → [Contrary to our expectations：反号显著判决] → [配对 null 判决] → [Hence：双假设合并不支持判决] → [显式推迟 Discussion]（可附：曲线关系 null 一句话）

**骨架**:
```
Hypothesis [1a] predicted that [predictor_A] would [enhance] [outcome], while
hypothesis [1b] postulated that [predictor_B] would [diminish] [outcome]. Contrary to
our expectations, [predictor_A] has a significant [negative] effect on [outcome], while
the effect of [predictor_B] is not significantly different from zero. Hence, hypotheses
[1a] and [1b] are not supported. ... We also tested for a possible [curvilinear]
relationship but found no evidence of it.
```

**为什么有效**: 一句话同时交付两种失败模式（反号 vs null），判决密度极高；"Contrary to our expectations" 让反号发现的意外性成为信息而非尴尬；"Hence ... not supported" 把两个假设合并收束，避免逐假设重复辩护；显式推迟 Discussion（"we explore them further in the discussion section"）把解释责任移交给正确的章节，Results 只管判决。

**与已有变体的分工**: 变体81（不支持裁决+以假设语言重述实际模式，gulati2005 单篇 EMERGING）面向**分样本/单假设 null** 的双拍收束；本变体为其同族**第二源**，差异在配对反号假设的合并判决：反号显著与 null 两种失败模式一句话并置，且附曲线关系补充检验 null。计数模型变体30（主效应仅全模型显著→保守判不支持，VERIFIED）是第三种失败模式（显著性缩水），三者构成 null 判决族谱。

**注意事项**: 反号显著与 null 的并置必须在同一句内完成对比（while 衔接），分开写会稀释反例信息；"not supported" 判决不可软化（不得写 largely/essentially supported）；推迟 Discussion 的句子要显式（本文在 R9 收束段以 "we explore them further in the discussion section" 重申一次）；若做了补充检验（曲线关系）应紧跟判决一句话带过，不展开。

**反模式**: 只报反号不报配对 null（假设集不完整）；用 "partially supported" 软化明确失败；在 Results 内即兴展开反例解释侵占 Discussion 功能。

**验证状态**: EMERGING（单篇，待第二篇交叉验证；与变体81 同族双源后可考虑联合升级）

**原文锚定**: "Contrary to our expectations, a manufacturer's dependence advantage has a significant negative effect on performance, while the effect of supplier's dependence advantage is not significantly different from zero. Hence, hypotheses 1a and 1b are not supported."

**范文来源**: Gulati & Sytch (2007), *Administrative Science Quarterly* 52(1) — Results 节 H1a/H1b 判决段。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r6_contrary_pair_sign_reversal_null_dual_verdict -->

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r6_contrary_pair_sign_reversal_null_dual_verdict_gulati_sytch2007 -->

### 变体 81：不支持裁决 + 以假设语言重述实际模式的双拍诚实收束（Unsupported Verdict with Pattern Restatement）

**适用场景**: 假设不被支持、但数据呈现部分相关模式时（某组边沿显著、其余组为 null、且方向与预测相反）。先给明确的不支持裁决，再**在假设自身的词汇内**重述"数据实际显示什么"——既不让 null 隐身，也不把方向相反的部分模式包装成边界发现。

**报告节奏**: [假设回指] → [各组模式证据（含边沿/相反信号）] → [明确不支持裁决] → [以假设词汇重述实际模式]

**骨架**:
```
[假设回指] Hypothesis [N] predicts that [pressure X] affects [outcome of category C] more
adversely than [outcome of categories A or B].
[各组证据] Comparing the coefficient of [X] across [A], [B], and [C] (column '[a]'), we find
that it has a marginally significant [positive] effect on the performance of [C], but has an
effect indistinguishable from zero in [A] and [B].
[明确不支持裁决] We therefore conclude that Hypothesis [N] is not supported,
[模式重述] as [category A] does not do significantly worse than [category B] under conditions
of [X] (though it does [marginally] worse than [category C]).
```

**为什么有效**: 部分支持的灰色地带最容易诱发两类失真——把不支持写成"部分支持"，或把边沿显著的相反信号藏进脚注。本节奏把裁决与证据分离：裁决句无让步词（"not supported"），模式重述句才容纳全部细节（哪个类别边沿显著、方向如何、与谁比较 marginally worse），读者可同时获得结论的明确性与证据的完整性。

**注意事项**: 模式重述必须以假设中的比较对象为语法骨架（"A does not do significantly worse than B under X"），不能滑回系数叙述；边沿显著（+、p<0.10 单尾）须如实标注检验尾数；裁决后不再追加"仍需未来研究"式的软化句（软化由 Discussion 承担）。

**反模式**: 以"部分支持"或"混合证据"替代明确裁决（审稿人会追问哪一半被支持）；只报 null 不报方向相反的边沿信号（选择性报告）；裁决句与重述句相互矛盾（如裁决不支持、重述却出现"consistent with"措辞）。

**原文锚点**: "We therefore conclude that Hypothesis 4 is not supported, as external procurement does not do significantly worse than alliances under conditions of task interdependence (though it does marginally worse than internal procurement)."

**范文来源**: Gulati, Lawrence & Puranam (2005), *Strategic Management Journal* — RESULTS H4 裁决段（明确不支持 + 模式重述双拍）。

<!-- wb:gulati2005-adaptation-vertical:r6_unsupported_verdict_with_pattern_restatement -->

### 变体 79：R8 理论动机补充分析双段式 — 理论开题 + 边界条件/构念层次裁决 (1篇高价值)

**适用场景**: 主结果之后有一组非稳健性性质的补充分析（理论边界条件、构念加总层次、测量替代）时：用"two sets of additional analyses"总起，每段以理论动机开题（不是 threat 开题），以对主结果的强化或划界收尾。与 R7 threat 稳健性严格分离。
**排列模式**: [总起句] → [第一组: 理论动机开题 → 检验动作 → 交互结果 → 边界条件结论] → [第二组: 动机开题 → 层次对比 → 裁决句]
**范文来源**: Higgins & Gulati (2003), *Organization Science*

**骨架**:
```
[总起句]
We conducted two sets of additional analyses.

[第一组：理论边界条件]
First, since our claims centered on [theoretical mechanism], we tested
whether our effects were especially strong during [theoretically-relevant
condition]. In particular, we tested whether [IV] was especially valuable
to [units] when [condition holds]. Results revealed significant and
[direction] interaction effects between [moderator] and [IV variables]
suggesting that [IV] are particularly helpful to [units] in [achieving
outcome] when [condition holds]. Further, [IV] have a particularly
beneficial effect on [outcome] when [condition holds]. The latter results
held for [k] of our [N] measures of [outcome] and remained significant and
in the direction expected, even after we accounted for [mediator/control].

[第二组：构念加总层次裁决]
Second, we investigated the effects of [construct aggregated at level A]
versus [level B]. We found that [level A] was significantly and positively
associated with [outcomes]. With respect to [level B], however, we found
different results. Including a variable for [level B measure] did not have
a significant effect on [outcomes]. Thus, we found evidence to suggest that
it is [level A], rather than [level B], that account for the effects of
[IV] on [outcomes].
```

**为什么有效**: "since our claims centered on X" 开题句把 post hoc 分析锚回理论主张，使补充分析读起来是理论深化而非钓鱼挖掘；同时保留 "Additional Analyses" 标题与 post hoc 地位（红线：post hoc 机制检验与稳健性检验分开标注的正面示范）；第二组"Thus, it is A rather than B that account for the effects"裁决句把测量层次对比压缩成可引用的结论。
**注意事项**:
- 补充分析的诚实标注不可省：标题明写 Additional Analyses（而非 Robustness），分析动机写"we investigated/we tested"而非"to address the concern"
- 边界条件结果不齐时如实缩圈（"held for two of our three measures"），不得宣称全复制
- 交互结果报告保持与 R4 主骨架一致的完整性要求（本范文无 simple slopes/图是年代局限，采用时按 R4 权威变体补）
- 构念层次裁决须两个层次都实际检验过，不得只报胜者
**反模式**: 把理论补充分析混入稳健性节（"To further validate our findings, we tested whether effects were stronger under uncertainty"）——混淆 threat 响应与理论深化，削弱两者的论证力。
**原文锚点**: "since our claims centered on the signaling value of upper echelon affiliations, we tested whether our effects were especially strong during times of high uncertainty."（Additional Analyses 第1段）

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:theory_motivated_additional_analyses -->

<!--
pattern_id: bk_sobel_partial_mediation_cross_dv_replay
build_type: 假设化中介展演型（中介是正式假设 H 的检验而非 post hoc 机制探索）；多 DV 复制设计
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定变体 58 confirmatory 部分中介堆叠确认 VERIFIED）
-->

### 变体 78：R3 Baron-Kenny+Sobel 假设化部分中介 — 三条件列举 + 跨 DV 重演 + partial-vs-full 幅度裁决 (legacy, 1篇高价值)

**适用场景**: 中介本身是正式假设（H5b 类）且同一 IV→mediator→DV 链要在多个结果变量上检验时：每张 DV 表重演 direct 效应（H5a）与中介判决（H5b），最后用间接效应显著性 + 系数下降幅度裁决 partial vs full mediation。
**排列模式**: [程序引用] → [(a)(b)(c) 三条件逐一列举] → [Sobel 乘积系数+公式+p 值] → [跨 DV 重演判决] → [效应消失时的幅度裁决]
**范文来源**: Higgins & Gulati (2003), *Organization Science*
**结构锚定**: 变体 58（衰减+χ²+Sobel+bootstrap 堆叠确认部分中介，VERIFIED）的 legacy 前身——必须标 legacy

**骨架**:
```
[程序引用 + 三条件列举]
To test for partial mediation, we followed procedures outlined in
[Baron and Kenny (year)] and [Sobel (year)]. The results suggest evidence of
mediation since (a) [IV variables] were positively associated with [mediator]
and with [DV], (b) [mediator] was positively associated with [DV], and
(c) when the [mediator] variable was entered into the analyses along with
[IV variables], these effects on [DV] decreased both in magnitude and in
significance level.

[间接效应检验程序]
Further, we tested the significance of the indirect effects of [IV] on [DV]
via the mediator. Specifically, for each [IV] variable, we calculated the
regression coefficient corresponding to the mediated path, which is the
product of the coefficient from the first stage regression (predicting
[mediator]) and the coefficient from the full second stage regression
(predicting [DV]). The standard error for this combined coefficient is
calculated using [Sobel's (year)] formula. [For each IV: p-value reporting,
e.g., for [IV1], p = [.value]; for [IV2], p < [.threshold]], suggesting that
[mediator] did partially mediate the relationships between [IV] and [DV],
as hypothesis [H] predicted.

[跨 DV 重演]（每个后续 DV 表重复：direct 判决 → mediator 进入 → 判决变化）
Table [X] shows the results for [DV2]. These results also support
hypothesis [H5a]: [IV] had a significant and positive effect on [DV2].
We also found that the effect for [IV] weakened once we included [mediator],
suggesting that [mediator] may partially mediate the effects observed.

[效应消失时的幅度裁决——本变体的独门句]
When we added [mediator] to our models (models [M6] and [M7]), the effect
for [IV] on [DV3] disappeared but the significance level of the effect for
[IV2] remained the same. Further analyses, using [Sobel's (year)] formula,
suggested that while the effect of [IV] disappeared in model [M6] of
Table [X], the drop in magnitude of the coefficient was not sufficient
enough to suggest full mediation. Rather, we found additional support for
hypothesis [H]—here, that [mediator] partially mediates the relationship
between [IV] and [DV3] (p < [.threshold]).
```

**为什么有效**: 中介作为正式假设时，三条件 (a)(b)(c) 逐一列举把判定标准亮在明处；间接效应乘积系数+Sobel 公式给出可复算的程序；跨 DV 重演把单表中介升级为复制性证据；"效应消失但按幅度判 partial 而非 full"是诚实且精确的裁决——比二值化的"中介成立/不成立"信息量大。
**注意事项**:
- **legacy 标注强制**：Baron-Kenny 条件计数是 legacy 程序（对应诚实边界 hb_ols_legacy_kenny_complete_mediation 的 partial 版）；现代采用必须补 bootstrap 间接效应区间或显式标 legacy，参照变体 58 的现代堆叠确认
- 中介判决语言用 associated with / partially mediate the relationship（相关链分解），不得写 mediator transmits causal effect
- "not sufficient enough to suggest full mediation" 的裁决依据是系数下降幅度对比，采用时须报告前后系数值支撑该判断
- 跨 DV 重演须显式声明呈现方式一致（"the results are presented in a similar fashion"），否则读者会怀疑选择性呈现
**反模式**: 效应消失即宣称 full mediation（未比较系数下降幅度）——把"不显著"当"无效应"，混淆中介类型判定。
**原文锚点**: "while the effect of upper echelon downstream ties disappeared in model 6 of Table 4c, the drop in magnitude of the coefficient was not sufficient enough to suggest full mediation."（Results, Table 4c 段）

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:bk_sobel_partial_mediation_cross_dv_replay -->

<!--
pattern_id: hypothesis_verdict_chain_null_concession
build_type: 假设判决导航型（逐假设段落组织）；跨估计器（层次回归/选择模型等多模型多假设设计通用）
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证；结构模板锚定 R3 四拍主骨架——本变体管判决的段落编排，幅度拍须按主骨架补齐）
-->

### 变体 77：R3 假设判决链 — 假设重述 + 模型定位 + However 衔接 null 与支持判决 (1篇高价值)

**适用场景**: 一张表连续检验多个平行假设（H1…H4），其中混有 null 与支持判决时，把每个假设写成"重述→定位→判决"微链，用 However 把 null 判决与相邻支持判决衔接成叙事段——null 不孤立成段，支持判决获得对照背景。
**排列模式**: [H_k 重述 → model 定位 → 判决] → However → [H_{k+1} 重述 → models 定位 → 判决] →Moreover/We also found → …
**范文来源**: Higgins & Gulati (2003), *Organization Science*

**骨架**:
```
[null 判决微链]
Hypothesis [N] predicted that [predictor] would be [positively/negatively]
related to [outcome]. As shown in model [M], we did not find support for
hypothesis [N].

[However 衔接 → 支持判决微链]
However, hypothesis [N+1], that [predictor2] would be [positively/negatively]
related to [outcome], was supported, as shown in models [M2] and [M3].
Moreover, we found support for hypothesis [N+2] with respect to [predictor3],
as shown in model [M4]: [one-sentence substantive restatement of the
direction of the finding].
We also found [qualifier: substantial] support for hypothesis [N+3], as shown
in model [M5] of Table [X]: [predictor4] had a significant and [positive/
negative] effect on [outcome].

[null 假设采用时的幅度拍补齐位]
（采用本变体时按 R3 主骨架在每条支持判决微链内补幅度拍：
Substantively, a [one-SD] increase in [predictor] is associated with a
[Y-unit] [increase/decrease] in [outcome]——年代风格无此拍，不可仿效省略。）
```

**为什么有效**: 假设重述嵌入拍1使读者不用回翻 Theory 即可核对判决；However 把 null（H1）转化为支持判决（H2）的叙事铺垫而非孤立的失败；判决后追加一句实质性方向复述（"the greater X, the greater Y"）让判决落地为可引用的发现句。
**注意事项**:
- 判决动词分级可用：was supported / we found support / we found substantial support——程度词保留假设强度差异，但不得用强动词掩盖边缘 p 值
- null 判决一句带过是本文年代局限：现代标准（R6 权威变体4）要求 null 后有诚实声明或解释后手，采用本变体时须补
- 因果语言校准：骨架判决句用 related to / associated with，不用 effect of（估计器为选择修正截面回归）
**反模式**: 把全部假设判决压成一段无定位的总结（"H1-H4 were tested with mixed results"）——丢失模型定位使读者无法核对证据链。
**原文锚点**: "As shown in model 3, we did not find support for hypothesis 1. However, hypothesis 2, that upper echelon affiliations with prominent horizontal organizations would be positively related to investment bank prestige, was supported, as shown in models 4 and 5."（Results, Table 3 判决段）

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:hypothesis_verdict_chain_null_concession -->

### 变体 65: R4 — 分样本 null→significant 对 + 组内 Wald + 跨子样本 Chow 诚实降级（post_2022_women_tmt_strategic_renewal 型）

**来源论文**: Post, Lokshin & Boone 2022 (AMJ)
**验证状态**: VERIFIED（expert_audit_override, user 2026-08-29）
**槽位**: R4（亦服务 R6 诚实降级）

#### 报告骨架

```text
To test Hypothesis [H], we estimated [outcome] models separately for the
[moderator_absent] and the [moderator_present] subsamples. When [moderator] is [absent]
(Table [X], Model [N]), the coefficient for [treatment_A] is [marginally
significant/insignificant] (b = [value], p = [value]), while the effect of [treatment_B]
is insignificant (b = [value], p = [value]), and the difference in the two estimated
coefficients is not significant. Conversely, when [moderator] is [present] (Table [X],
Model [M]), the [treatment_A] effect gains in size and significance (b = [value],
p = [value]), whereas the [treatment_B] coefficient does not (b = [value], p = [value]),
and the difference in the two estimated coefficients becomes significant (p = [value]).
This pattern of findings is consistent with Hypothesis [H], although a Chow test comparing
the effect sizes of the [treatment_A] across Models [N] and [M] reveals that the
difference is not significant (p = [value]).
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 双子样本镜像句式 | absent 组报 null → present 组报 "gains in size and significance" | 调节证据由对称对照承载，不靠交互项 |
| 2. 组内 Wald（focal vs 对照 treatment） | 每个子样本内报系数差 p | 子样本内部也维持双处理对照纪律 |
| 3. 跨子样本 Chow 诚实降级 | Chow 不显著时写 "consistent with ... although ... not significant" | 方向证据与统计裁决分离，支持判断留给读者 |
| 4. 幅度翻译随显著组出现 | 仅 present 组后给百分比幅度 | null 组不硬造幅度 |

#### 原文锚定
- "This pattern of findings is consistent with Hypothesis 3a, although a Chow test comparing the effect sizes of the female appointments across Models 5 and 6 reveals that the difference is not significant (p = .60)."（results.md Table 3 段）

#### 与最近变体的区别
- 区别于 r4_ols_threshold_group_coefficient_difference（外部阈值分组）：本变体是理论状态分组（零/正 incumbency）+ 组内 Wald + 跨组 Chow 诚实降级三件套；区别于变体 43（组间系数差异裁决）：本变体把"哪组显著"的镜像节奏与 Chow 不显著时的降级句式一并沉淀。

### 变体 17: R3 主假设检验 — 倒 U 型关系（Lind-Mehlum 三步 + 转折点 CI + Cohen's d）(1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: "In Model 2 of Table 2, we tested Hypothesis 1 by introducing both the linear and quadratic terms of relative exploration. The result shows that competitive aggressiveness first increases significantly with relative exploration (b = 1.508, p = 8E−08), then decreases significantly as relative exploration continues to increase (b = −1.439, p = 1E−07). This result indicates a curvilinear relationship (inverted U-shape) between relative exploration and competitive aggressiveness, with a medium effect size (Cohen's d = 0.428). … Using the 'margins' command in Stata 12, we confirmed that when relative exploration = 0, the slope dy/dx = 1.701 (p = 4E−05), and when relative exploration = 1, the slope dy/dx = −1.561 (p = 3E−05). Third, we tested whether or not the turning point is located within the data range of relative exploration. We confirmed this using the 'nlcom' command in Stata 12 by showing that the inverted U-shape turns when relative exploration = 0.522 and that the 95% confidence interval for the turning point [0.504, 0.539] is within the value range of relative exploration."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: R3
**骨架**:
> Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome]. In Model [y] of Table [z], we tested this hypothesis by introducing both the linear and quadratic terms of [predictor]. The result shows that [outcome] first increases significantly with [predictor] (b = [linear], p = [p-value]), then decreases significantly as [predictor] continues to increase (b = [quadratic], p = [p-value]). This result indicates a curvilinear relationship (inverted U-shape) between [predictor] and [outcome], with a [effect-size] effect size (Cohen's d = [value]).
>
> We examined the marginal effects of this relationship following the three steps suggested by Lind and Mehlum (2010). First, we examined whether the second-order term is significant and of the expected sign; this is confirmed by the result. Second, we tested whether the slope is indeed sufficiently steep at both ends of the data range of [predictor]. Using the "margins" command in [software], we confirmed that when [predictor] = [low_value], the slope dy/dx = [value] (p = [p-value]), and when [predictor] = [high_value], the slope dy/dx = [value] (p = [p-value]). Third, we tested whether the turning point is located within the data range of [predictor]. We confirmed this using the "nlcom" command in [software] by showing that the inverted U-shape turns when [predictor] = [turning_point] and that the 95% confidence interval for the turning point [[lower], [upper]] is within the value range of [predictor]. We provide additional support by plotting this relationship in Figure [X]. These findings suggest that Hypothesis [x] is supported.
**与原骨架差异**: OLS-FE.md 现有 16 个变体全部针对线性关系或线性交互，曲线关系报告完全空白。本骨架提供顶刊倒 U 型关系的标准协议：线性/二次系数 → 形状判断+效应量 → Lind-Mehlum 三步（二阶项符号、两端斜率、转折点在数据范围内）→ 转折点 95% CI → 图形 → 支持判断。**范式排他性**: 多项式 OLS/FE 专用；Logit/Probit 需替换为 predicted probability / odds ratio 解释。
**诚实边界**: 曲线关系的 Cohen's d 计算应说明基准（如基于二次项或简单斜率差异），不可直接套用线性交互的 d 公式；须在 Methods 或附录说明效应量计算方式。

### 变体 18: R4 曲线调节效应 — 倒 U 型被调节（二阶交互项符号 + Cohen's d + flatten/steepen 图形解释）(1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: "In Model 3, the interaction terms between repeated alliance ties (relational embeddedness) and both the linear and quadratic terms of relative exploration are introduced in order to test Hypothesis 2: whether repeated alliance ties negatively moderates the inverted U-shaped relationship. This moderation effect is supported if the second-order interaction term is significantly positive (Hanns et al., 2016). As confirmed by our results, the second-order interaction term is indeed positive (b = 0.692, p = 6E−06), with a small-to-medium effect size (Cohen's d = 0.364). Figure 2 illustrates this moderation effect, showing that the inverted U-shape is flattened when the value of repeated alliance ties is higher, supporting Hypothesis 2."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: R4
**骨架**:
> In Model [N], the interaction terms between [moderator] and both the linear and quadratic terms of [predictor] are introduced in order to test Hypothesis [N]: whether [moderator] [positively/negatively] moderates the inverted U-shaped relationship between [predictor] and [outcome]. This moderation effect is supported if the second-order interaction term is significantly [positive/negative] ([citation]). As confirmed by our results, the second-order interaction term is indeed [positive/negative] (b = [value], p = [p-value]), with a [small/medium/large] effect size (Cohen's d = [value]). Figure [N] illustrates this moderation effect, showing that the inverted U-shape is [flattened/steepened] when the value of [moderator] is higher, supporting Hypothesis [N].
>
> Model [N+1] is the full model, including all control, independent, and interaction variables; all results from Models [X] hold.
**与原骨架差异**: 现有 OLS-FE R4 变体（变体 9、10、13、14）均针对线性交互的边际效应或百分比解释，未覆盖二次项×调节变量的曲线调节。关键语言：**二阶交互项符号预期**（positive/negative）决定 flatten/steepen；**flattened/steepened** 描述整个曲线形状变化；**M6 全模型一句收尾**确认各独立模型结果在全模型中稳定。**范式排他性**: 二次项 × 连续调节变量专用；若调节变量为二分/类别需调整图示语言。
**诚实边界**: 曲线调节的 Cohen's d 计算应基于二阶交互项或简单斜率差异，不可直接套用线性交互的 d 公式；须在 Methods 或附录说明效应量计算方式。

### 变体 19: R2 模型序列 — 多项式主效应 + 多个曲线调节 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: "We ran fixed-effects models following a hierarchical approach: Model 1 includes only the control variables, while Models 2 through 5 add the independent and interaction variables. Model 6 is the full model, including all independent and interaction variables. Variance inflation factor (VIF) scores were calculated for all models; none of the maximum VIFs exceed the value of 2.5, which is substantially lower than the rule-of-thumb cut-off of 10 (Ryan, 1997). We then used the 'coldiag' procedure in Stata to conduct the Belsley, Kuh, and Welsch (1980) multicollinearity diagnostic test, which showed that the condition number for our complete model is 7.53, well below the threshold of 30. We also ran the fixed-effects models using non-centered data; the results are consistent. Since centered estimations can make interpretation of the results less straightforward (Echambadi & Hess, 2007), we report estimations using the original variable values in Table 2."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> We ran [estimator] models following a hierarchical approach: Model 1 includes only the control variables, while Models 2 through [N-1] add the independent and interaction variables. Model [N] is the full model, including all independent and interaction variables. [Variance inflation factor (VIF) scores were calculated for all models; none of the maximum VIFs exceed [value], which is substantially lower than the rule-of-thumb cut-off of 10 ([citation]).] [We then used [procedure] in [software] to conduct [diagnostic test], which showed [result].] We also ran the [estimator] models using non-centered data; the results are consistent. Since centered estimations can make interpretation of the results less straightforward ([citation]), we report estimations using the original variable values in Table [z].
**与原骨架差异**: 与现有变体 16（Ahmadi et al. 7 模型 trait × manipulation × complexity 实验设计）不同，本结构是面板数据中的 M1 控制 → M2 多项式主效应 → M3-M5 分别加入不同曲线调节 → M6 全模型。关键：层次结构为理论服务，让读者既能看清每个假设的干净证据，又能验证结果在全模型中稳定。

### 变体 20: R1 描述性统计与诊断 — 多项式/交互模型 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: "Table 1 reports descriptive statistics and correlations for all variables, including the quadratic and interaction terms. We mean-centered the variables before creating quadratic and interaction terms in order to reduce non-essential ill-conditioning between independent variables and their higher-order terms (Aiken & West, 1991). The dependent and independent variables show considerable variance, and the correlation coefficients are consistent with our expectations."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-08
**槽位**: R1
**骨架**:
> Table [x] reports descriptive statistics and correlations for all variables, including the quadratic and interaction terms. We mean-centered the variables before creating quadratic and interaction terms in order to reduce non-essential ill-conditioning between independent variables and their higher-order terms ([citation]). The dependent and independent variables show considerable variance, and the correlation coefficients are consistent with our expectations.
>
> We ran [estimator] models following a hierarchical approach: Model 1 includes only the control variables, while Models 2 through [N-1] add the independent and interaction variables. Model [N] is the full model, including all independent and interaction variables. Variance inflation factor (VIF) scores were calculated for all models; none of the maximum VIFs exceed [value], which is substantially lower than the rule-of-thumb cut-off of 10 ([citation]). We then used [procedure] in [software] to conduct the [citation] multicollinearity diagnostic test, which showed that the condition number for our complete model is [value], well below the threshold of [threshold]. We also ran the [estimator] models using non-centered data; the results are consistent. Since centered estimations can make interpretation of the results less straightforward ([citation]), we report estimations using the original variable values in Table [z].
**与原骨架差异**: write-results SKILL.md 的 R1 通用段落未覆盖多项式/交互模型特有的 mean-centering、condition number 和非中心复制三重诊断。本文提供了完整且简洁的整合范例：诊断不是为了例行公事，而是为了说明"高阶项和交互项没有造成多重共线性问题"，并解释为何最终报告非中心化系数（便于解释）。

### 变体 67: R1 — 双路径前提描述统计：理论预言零相关 + moderator 分布与条件定义（post_2022_women_tmt_strategic_renewal 型）

**来源论文**: Post, Lokshin & Boone 2022 (AMJ)
**验证状态**: VERIFIED（expert_audit_override, user 2026-08-29）
**槽位**: R1

#### 报告骨架

```text
We identified [N] [treatment events], of which [n] ([value]%) were [focal treatment].
The majority of observations in our sample ([value]%) are [unit] observations with zero
[moderator]. In our sample, a (relatively) "[small condition]" corresponds to [definition]
and a "[large condition]" means [definition]. As we theorized, change in [mediator_A] and
change in [mediator_B] are not significantly correlated ([value], p = [value]), and
neither are change in [outcome_A] and [outcome_B] ([value], p = [value]). Table [1]
provides all descriptive statistics and pairwise correlations, which are mostly low to
moderate. The mean variance inflation factor for the variables used in the estimation
([value]) is below the commonly used threshold of [threshold] ([citation]).
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 理论预言零相关前提 | "As we theorized, ... are not significantly correlated" | 双中介路径的区分效度前提在 R1 预检，后续双路径叙事才站得住 |
| 2. moderator 经验分布先行 | 零值占比、计数分布 | 为分样本/阈值检验的样本构成提前交底 |
| 3. 条件操作化定义内嵌 | small/large cohort 的取值定义在 R1 给出 | R4/R5 分样本读者不用回翻 Methods |
| 4. 常规诊断收尾 | 相关矩阵 + mean VIF < 阈值 | 诊断不缺位但不喧宾夺主 |

#### 原文锚定
- "As we theorized, change in TMT risk-taking propensity and change in TMT change orientation are not significantly correlated (.03, p = .16), and neither are change in M&A and R&D growth (.01, p = .64)."（results.md 第1段）

#### 与最近变体的区别
- 区别于 r1_ols_standard（描述统计+VIF 常规款）：本变体新增"理论预言零相关"区分效度前提句 + moderator 分布/分样本条件定义前置。

### 变体 21: R8 补充/事后分析 — 枚举清单 + 附录引用 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**原始句锚点**: "We conducted six additional analyses, either as robustness checks or to gain additional insights into the primary relationships. These analyses investigated (a) whether the results are robust to alternative measures for relative exploration; (b) which firm in a dyad is more likely to initiate competitive actions; (c) what factors determine a firm's response to its partner's actions; (d) the extent to which the technological know-how acquired in one area and knowledge of a partner's managerial system can be applied to competition against the same partner in different technological areas; (e) whether the results are robust to different paradigms of competition; and (f) the potential moderating effects of network density and multiparty. Details of these analyses are available in the Appendix S1."
**验证状态**: EMERGING（可选；中价值）
**写入日期**: 2026-07-08
**槽位**: R8
**骨架**:
> We conducted [N] additional analyses, either as robustness checks or to gain additional insights into the primary relationships. These analyses investigated (a) [analysis_1]; (b) [analysis_2]; (c) [analysis_3]; (d) [analysis_4]; (e) [analysis_5]; and (f) [analysis_6]. Details of these analyses are available in [Appendix].
**与原骨架差异**: 现有 R8 变体 5 是 MCMC 中介的详细展开式。本文展示当稳健性/探索性分析条目较多时，正文可用枚举清单指向附录的简洁策略。关键：用 "either as robustness checks or to gain additional insights" 同时标注两类目标，但缺少逐条 threat 说明——若稳健性分析是核心识别策略的一部分，建议改用变体 1（Table 9 矩阵）或变体 2（叙事型逐 threat 组织）。
**诚实边界**: 将稳健性检验仅作为枚举清单可能削弱内部效度叙事；若可能，应在正文或附录中为每项分析标注其回应的具体威胁或探索性问题。

### 变体 22: R2 无模型证据开场 — 四分位均值/中位数单调性 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "We first present model-free evidence regarding the relationship between CEO confidence and myopic marketing management. Consistent with H1, there is a monotonic increase in MMM from the first quartile where CEOs have the lowest level of confidence to the fourth quartile where CEOs are the most confident."
**验证状态**: EMERGING
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> We first present model-free evidence regarding the relationship between [IV] and [DV]. In the [web appendix / online supplement], we show the scatter plots of [DV] against [IV] for [subgroup description: e.g., the three industries with the most observations]. In Fig. [X], we divide our sample into [four quartiles / five quintiles] based on the level of [IV] and calculate the mean and median [DV] for observations in each [group]. Consistent with Hypothesis [N], there is a monotonic [increase / decrease] in [DV] from the first [group], where [IV] is lowest, to the [fourth / fifth] [group], where [IV] is highest. The mean (median) [DV] is significantly different across the [groups].
**与原骨架差异**: 在报告回归模型之前先用无模型证据建立模式的可信度，是 upper-echelons / 行为决策类论文的常用开场。关键四拍：(1) 声明"model-free evidence"；(2) 附录散点图 + 正文分组表/图；(3) 按 IV 分位数报告 DV 的均值/中位数单调趋势；(4) 跨组显著性检验。这为后续模型结果提供了视觉和描述性锚点，降低读者对复杂识别策略的认知门槛。
**诚实边界**: 无模型证据不能替代模型检验，也不能用于因果推断；必须在后续段落中明确过渡到控制混淆变量后的模型结果。
**跨 skill 对齐**: `../write-methods/corpus/面板数据-OLS.md` 变体20（M2.5 model-free evidence 预览）；`write-introduction/hooks/24-positive-trait-dark-side` 建立的读者预期在此得到实证承接。

### 变体 23: R5 四分位距经济显著性 — 从 P25 到 P75 的幅度翻译 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "Table 4 Column 1 shows that H1 is supported: CEO confidence significantly and positively predicts MMM with δ1 = 0.287, indicating that an interquartile move in CEO confidence from the 25th percentile to the 75th percentile is associated with a 0.29 percentage point increase in MMM. In untabulated tests, we test for H1 using all firms, without restricting to those with CMOs, and continue to find support for H1 with similar economic significance."
**验证状态**: EMERGING
**写入日期**: 2026-07-08
**槽位**: R3/R5
**骨架**:
> The coefficient for [IV] is [positive / negative] and statistically significant (β = [value], p < [threshold]). An interquartile move in [IV] from the 25th percentile to the 75th percentile is associated with a [N] [unit / percentage point] [increase / decrease] in [DV]. In untabulated tests, we also find support using [alternative sample / broader sample], with similar economic significance.
**与原骨架差异**: 现有经济显著性变体多用 "one-SD change → X%"，而本变体使用 **P25–P75 四分位距移动**作为幅度基准。这适用于 IV 分布偏斜、理论意义更对应"从中等偏低到中等偏高"情境的研究。关键：报告具体单位（如 0.29 percentage points）并在括号中说明是 percentage point 还是 percent，避免审稿人误解。
**诚实边界**: P25–P75 的解释隐含了 IV 在其分布中段的比较；若 IV 呈高度偏态或存在大量零值，应报告实际对应值（如 P25 = [value], P75 = [value]）而非仅说"interquartile"。
**跨 skill 对齐**: `../write-methods/corpus/micro-templates/interquartile-economic-significance.md`（M7/M8/M10 预告）；Results 在此兑现 Methods 中预告的经济显著性解释口径。

### 变体 63：R3/R5 ln(时长) DV 的跨列选择性显著 + 天数回译幅度拍（wowak2020 型）
[功能标签]: R3 主假设检验（时长 DV 变体）+ R5 幅度嵌入
[骨架]: "We now move to our model that examines [DV_time]. In Table [y], we present the results of the [OLS FE] model that uses the natural log of the number of [time units] from [awareness event] to [action initiation] as the dependent variable. Once again, we include control variables in column (1) and then the [predictor] for all [events] (column (2)) and each [subclass] (columns (3)–(5)). The only column in which [predictor] has a significant relationship with [DV_time] is for [high-severity subclass] in column (3) (β = [value], p < [threshold]). Increasing [predictor] is associated with a faster [outcome] for the most [severe], [stakes descriptor] events needing [action]. This finding provides support for Hypothesis [N]. Interpreting similarly, a one standard deviation increase in [predictor] is associated with a [N]-[unit] acceleration in [DV_time] for the most severe [subclass]."
[关键特征]: 并行列结构中诚实报告选择性显著（"The only column in which ..."）而非逐列罗列；ln(时长) 系数不留在对数尺度，直接回译为自然单位天数（one-SD → [N]-unit acceleration）作幅度拍；"Interpreting similarly" 把幅度解释锚定到前表的解读协议
[适用]: ln(时间间隔) DV 的 OLS/FE 平行分列设计；与计数 DV 表共享分列结构（严重度分组）的双 DV 论文
[禁忌]: 跨列选择性显著不得隐藏——用 "the only column" 明示；回译幅度需给出自然单位而非只报对数点
**原文锚定**: "The only column in which FBR has a significant relationship with time-to-recall is for high-severity class 1 recalls in column (3) (β = −0.22, p < 0.05). ... Interpreting similarly, a one standard deviation increase in FBR is associated with a 16-day acceleration in time-to-recall for the most severe class 1 recalls."
**来源**: wowak_2020_female_directors_recalls (M&SOM), §5 Table 4 段

### 变体 24: R2 Heckman 两阶段表格导航 — 第一阶段 Table 3 → 第二阶段 Columns 1-4 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "Table 3 shows the results of the first-stage selection equation with our exclusion restriction, Peer CMO presence, significantly and positively predicting the likelihood of a firm having a CMO. … Column 2 includes the two-way moderating relationships, and we find support for both H2 and H4."
**验证状态**: EMERGING
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> Table [X] shows the results of the first-stage selection equation. Our exclusion restriction, [instrument], significantly and [positively / negatively] predicts [selection_DV] (β = [value], p < [threshold]), consistent with [theory / prior work: citation]. This confirms that [instrument] satisfies the relevance condition for identifying [selection_outcome]. Table [Y] reports the second-stage Heckman selection results. Column 1 tests Hypothesis [H1]: [IV] significantly and [positively / negatively] predicts [DV] (β = [value], p < [threshold]). Column 2 adds the two-way moderating relationships, providing support for Hypotheses [H2] and [H4]. Column 3 introduces the three-way interactions, supporting Hypotheses [H3] and [H5]. Column 4 shows that the results are robust to the inclusion of [firm fixed effects / alternative fixed-effect structure] instead of [industry fixed effects / original fixed-effect structure].
**与原骨架差异**: 现有 Heckman 导航（IV-2SLS.md 变体 r2_heckman_first_stage_navigation）侧重第一阶段排他性限制与相关性声明。本变体聚焦 **Results 正文中的两阶段表格递进导航**：先确认第一阶段排除限制显著（满足相关性），再逐列说明第二阶段四个模型分别检验哪些假设，使读者能清楚对应 Table 4 的列结构。适用于假设数量多、模型列数多、且使用 Heckman 选择模型的研究。
**诚实边界**: 若第一阶段工具变量不显著，不能进入第二阶段解释；必须报告逆米尔斯比（rho / lambda）的显著性，以判断选择偏误是否确实存在。
**跨 skill 对齐**: `../write-methods/corpus/两阶段模型.md` 变体3（Heckman 同行 prevalence 排他性限制）；`../write-methods/corpus/micro-templates/heckman-peer-prevalence-exclusion.md`（跨 segments 加权论证）。

### 变体 25: R7 替代 DV 证伪段落 — 领域外结果的预期不显著 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "An alternative way to establish causality is to provide a falsification test where we examine how AEM—an outcome variable that is not within the decision-making domain of the CMO—is affected by the interaction among CEO confidence, CMO confidence, and Board independence. We use the Heckman selection specification in Table 4 column 3, except that we replace the dependent variable with the level of discretionary accrual the firm has, a measure of the level of AEM (Kothari et al., 2005)."
**验证状态**: EMERGING
**写入日期**: 2026-07-08
**槽位**: R7
**骨架**:
> An alternative way to establish causality is to provide a falsification test where we examine [alternative_DV], an outcome that is [not within / outside] the decision-making domain of [focal_actor]. We use the [estimator] specification in [Table X], Column [N], except that we replace [DV] with [alternative_DV] ([operational_definition_citation]). We find that [predicted_finding: e.g., the main effect or interaction of interest behaves as expected], which is consistent with [Hypothesis / mechanism]. As expected, the [interactions / effects] involving [actor-specific variables] are insignificant, because [alternative_DV] is not within the decision-making domain of [focal_actor]. Interestingly, [unexpected_but_theoretically_interpretable finding] suggests [interpretation clause].
**与原骨架差异**: 现有 R7 变体多关注稳健性（替换估计量、样本、测量），本变体扩展 R7 的 **falsification / 机制边界功能**：用理论预期之外不应出现效应的 DV 来确认主效应的因果解释。关键结构：(1) 明确说明替代 DV 不在某行为者的决策领域内；(2) 报告应显著的效应确实显著；(3) 报告不应显著的效应确实不显著；(4) 对意外发现给出理论化解释而非忽略。这比单纯"结果稳健"更能支持因果识别。
**诚实边界**: 替代 DV 必须与主 DV 有理论上的领域边界；不能事后挑选一个"不显著"的结果作为证伪。应在 Methods 或稳健性部分预先说明为何该 DV 是合适的 falsification 目标。
**跨 skill 对齐**: `../write-methods/corpus/micro-templates/alternative-dv-falsification.md`（M8/M10 预告替代 DV 设计与替代/转换解释）。

### 变体 26: R7 内生性稳健性表叙事 — threat-by-threat Table 7 汇总 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "To complement these general endogeneity tests, we next look at specific sources of endogeneity and design tests to rule them out. We tabulate these tests in Table 7 and relegate the details to the web appendix for reasons of space. … The supporting evidence from all these complementary tests confirms the results of the DWH test that there is little reason to believe that endogeneity issues are solely driving the results we observe."
**验证状态**: EMERGING
**写入日期**: 2026-07-08
**槽位**: R7
**骨架**:
> Endogeneity is mainly caused by issues relating to omitted variables and simultaneity ([citation]). In our empirical model setup, we include [control_strategy: e.g., as many control variables as possible] to rule out omitted variables and use [temporal_strategy: e.g., lagged measures of IV] to ensure causal priority. We have also used the [DWH test / Hausman test] with strong instruments and [cannot reject / reject] the null hypothesis that [IV] is exogenous. This conclusion is also validated with the [instrument-free Gaussian copula estimation method / alternative instrument-free method].
>
> To complement these general endogeneity tests, we next look at specific sources of endogeneity and design tests to rule them out. We tabulate these tests in Table [X] and relegate the details to the [web appendix] for reasons of space. Our results are not due to [threat_1: reverse causality] because [test_1_result]. Nor are they driven by [threat_2: selection on observables / unobservables] because [test_2_result]. To rule out [threat_3: omitted executive / firm characteristics], we [test_3_method]; the results are generally similar. [threat_4: risk tolerance / alternative trait] is also unlikely to be driving the results, as we find robust results when [test_4_method]. The supporting evidence from all these complementary tests confirms the results of the [DWH / copula] test that there is little reason to believe that endogeneity issues are solely driving the results we observe.
**与原骨架差异**: 现有 R7 变体 1（Table 9 矩阵）和变体 2（叙事型逐 threat）分别适用于大量和小量稳健性检验。本变体是 **"一般性内生性检验 + threat-by-threat 表" 的复合结构**：先以 DWH / Gaussian copula 提供一般性证据，再用 Table 7 式矩阵逐项处理具体威胁（reverse causality, selection, omitted variables, alternative traits）。关键：最后一句用"little reason to believe that endogeneity issues are solely driving the results" 的谨慎措辞，避免过度因果断言。
**诚实边界**: 若 DWH 或 copula 结果不一致，必须诚实报告并讨论可能原因；不能仅因为"多数稳健性通过"就宣称完全排除内生性。"solely driving" 是审慎措辞，不应升级为"完全排除"。
**跨 skill 对齐**: `../write-methods/corpus/IV-2SLS.md` 变体5（DWH 检验 + Gaussian copula 内生性叙事）；`../write-methods/corpus/micro-templates/identification-exogeneity.md`（通用外生性论证）。

### 变体 27: 多阶段同 IV 管道衰减 profile — 同一 IV 跨序贯决策阶段的方向/显著性对比 (1篇高价值)
**来源论文**: Kim & Lee 2026 (Strategic Management Journal)
**原始句锚点**: "In summary, we fail to find compelling evidence of an association between SRO and voluntary turnover. This lack of association contrasts with the advantages that SRO companies appear to enjoy in the attraction and selection stages, and is consistent with the previously discussed possibility that SRO advantages operate primarily through signaling mechanisms that attenuate as employees gain direct experience with their employer."
**验证状态**: EMERGING
**写入日期**: 2026-07-22
**槽位**: R3+R9
**骨架**:
> [Stage 1 — Front-end] We begin by examining the association between [IV] and [stage-1 outcome]. Model [1] finds a [direction] association (p [relation] [threshold]); this remains stable in Model [2] with [controls]; Model [3] adds [fixed effects], estimating [within-unit] differences, and continues to find a [direction] association (p [relation] [threshold]) corresponding to [economic magnitude].
>
> [Stage 2 — Mid-pipeline] For the [stage-2] stage (unit = [stage-2 pair]), Model [4] estimates [direction] but imprecisely (p = [value]); Model [5] adds [characteristics]; Model [6] adds [fixed effects], producing a [stronger] association (p = [value]) [equivalent to magnitude]. Because the [within-unit] analysis is likely most informative, we interpret these as [suggestive evidence of ...].
>
> [Stage 3 — Back-end null] We use [Cox proportional hazards / estimator] for [stage-3 outcome]. Model [7] estimates [direction] and imprecise (p = [value]); Model [8] similar with [controls] (p = [value]); Model [9] with [full controls] turns the coefficient [opposite direction] but remains imprecise (p = [value]).
>
> [跨阶段对比句] In summary, we fail to find compelling evidence of an association between [IV] and [stage-3 outcome]. This lack of association contrasts with the advantages that [IV] appears to enjoy in the [stage-1] and [stage-2] stages, and is consistent with the possibility that [IV] advantages operate primarily through a [front-end / signaling mechanism] that attenuates once [actors gain direct experience]. A [signaling/attenuating mechanism] fits this pattern... We cannot definitively adjudicate, but the full-pipeline evidence suggests [mechanism that fits the front-significant/back-null pattern].
**与原骨架差异**: 区别于 多研究.md 的 cross-study synthesis（多研究独立样本收敛）——本变体是 **single-study single-IV multi-stage**：同一 IV 跨序贯决策阶段的衰减 profile。核心叙事装置是**跨阶段对比句**（"This lack of association contrasts with the advantages... in the [earlier] stages"）——把"前置显著 + 后置 null"从孤立报告提升为机制发现（用 null 在管道中的位置裁决竞争机制：signaling 随经验衰减 vs enduring preference 持续）。配套 write-methods 见 多研究.md 变体6（管道设计）；配套 post-treatment caveat 见 slot-R6（Slough 2023）。
**诚实边界**: post-treatment 样本递减让跨阶段估计量来自非随机子样本——后置 null 不可作"无效应"因果结论（见 slot-R6 Slough 变体）。机制裁决须诚实对冲（"cannot definitively adjudicate but full-pipeline evidence suggests"），不可过度断言。

### 变体 28: R2 — 截面 OLS/FE 中二元内生变量 + 样本选择的双阶段修正表导航 (1篇高价值)
**来源论文**: Pupovac, Astvansh, Carrillat & Legoux 2026 (Production and Operations Management)
**原始句锚点**: "Table 1's Column I reports the estimates from the regression that assumes the supplier's customer information disclosure is exogenous. Columns II and III present estimates from the control function method, which controls for the disclosure's potential endogeneity."
**验证状态**: EMERGING
**写入日期**: 2026-07-21
**槽位**: R2
**骨架**:
> Table [x] reports the estimates from the regression that assumes [endogenous_predictor] is exogenous. Columns II and III present estimates from the [control_function / Heckman] method, which controls for [endogeneity_type]. Column II shows that [instrument] is [positively/negatively] associated with [endogenous_predictor] (β = [value], p < [threshold]), consistent with [theory] and suggesting that the [relevance/exclusion] condition is likely satisfied. Column III reports the second-stage coefficient on [endogenous_predictor], which we use to test Hypothesis [x].
**与原骨架差异**: 现有 OLS-FE 变体 24 是 Heckman 两阶段表格导航（第一阶段 Table 3 → 第二阶段 Columns 1-4）。本论文同时使用 **Control Function（处理二元内生自变量）和 Heckman（处理样本选择）**，且两种方法的第一阶段结果都嵌入同一张表。本骨架提炼跨方法的通用 R2 导航：先报无修正列，再报第一阶段工具变量/排除限制相关性，最后报第二阶段核心系数。适用于截面 OLS/FE 中同时存在内生解释变量和选择偏误的研究。
**诚实边界**: 若第一阶段工具变量或排除限制不显著，不能进入第二阶段解释；必须报告控制函数残差项或逆米尔斯比的显著性，以判断内生性/选择偏误是否真实存在。

### 变体 29: R7 — 选择偏误三步防御：描述性模式 → CEM → Heckman + 关联非因果收尾 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "To more rigorously examine potential selection on observables, we employ a coarsened exact matching (CEM) strategy. … Accordingly, we interpret our results as associational, consistent with the proposed theoretical mechanisms, but not as definitive causal evidence."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> (1) We recognize that [treatment/IV] decisions are not random. To explore the extent to which selection may be influencing our findings, we examine patterns of [IV] across different types of [units]. We find no strong evidence that [IV] is systematically driving [selection]: [percentages across categories]; the correlations between [IV] and [selection type] are near zero ([value]). (2) To more rigorously examine potential selection on observables, we employ a coarsened exact matching (CEM) strategy, matching on [covariates]. In the matched sample, [IV] remains [direction] associated with [outcome] (B = [value], p < [threshold]). (3) We also conduct a Heckman two-stage model for selection from unobservables, using [instrument] which predicts [selection] but is uncorrelated with [outcome] (correlation = [value], n.s.). (4) These analyses suggest our findings are not merely reflective of [selection mechanism]. We interpret our results as associational, consistent with the proposed theoretical mechanisms, but not as definitive causal evidence.
**与原骨架差异**: 区别于变体 24（Heckman 表格导航）与变体 26（一般性内生性 threat-by-threat）。本变体是 **selection-specific 的递进式防御**——model-free 描述性诊断（IV 不驱动选靶）→ CEM（可观测）→ Heckman（不可观测），每一步处理更深一层的选择来源，且以"associational not causal"诚实收尾。
**诚实边界**: 三步必须递进（不能只做 CEM 就收尾）；CEM 需报告匹配变量与平衡改善位置；Heckman 必须明确报告工具变量与结果不相关；收尾必须降权为 associational。

### 变体 30: R6/R8 — 预测性零结果作为机制证据：排除替代解释的 null-finding 反转 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "Interestingly, we find no statistically significant market reaction to structural similarity at the time of deal announcements (see Cumulative Abnormal Returns (CAR) analyses in Online Appendix Table A18). This null finding suggests that the observed associations with improved performance likely reflect integration-related dynamics rather than selection at the time of the deal."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R6（零结果）/ R8（补充分析）
**骨架**:
> Interestingly, we find no statistically significant [market/early outcome] at [event time] (see [CAR/short-window] analyses in [table]). This null finding suggests that the observed associations with [long-run outcome] likely reflect [proposed mechanism] dynamics rather than [alternative explanation such as selection at event time].
**与原骨架差异**: 零结果不是失败，而是**排除替代解释的证据**——若 selection-at-event-time 成立，事件窗反应应显著；反应不显著 → 长期关联来自机制动态而非时点选择。区别于一般 R6 非显著处理（报方向→不显著→不解释幅度→不支持），本变体**主动反转利用**零结果。
**诚实边界**: 使用条件严格——零结果须被理论预测、替代解释须预测非零结果、零结果须嵌入在更大的显著结果模式中（不能孤立地用 null 论证机制）。

### 变体 31: R7 — 替代解释三连驳斥 + 异质性模式作为机制裁决收束 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "Our CEM analyses partially address this concern by matching deals on industry, firm size, and public status, characteristics often associated with organizational culture. The persistence of our findings in the matched sample suggests that cultural similarity alone may not explain our results."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> We consider [N] alternative factors. First, [alternative 1] could drive both [selection] and [outcome]. Our [method 1, e.g., CEM matching on X/Y/Z] partially addresses this concern; the persistence of our findings in the matched sample suggests [alternative 1] alone may not explain our results. Second, [alternative 2]: our [method 2] helps control for [it]. Third, [alternative 3]: our [method 3] partially addresses this, and our finding that [IV] matters more for [high-moderator conditions] suggests our mechanism extends beyond simple selection on [alternative 3]. Although we cannot eliminate all alternative explanations given our observational design, our pattern of results—particularly heterogeneous effects by [moderator 1], [moderator 2], and [moderator 3]—aligns more closely with our [mechanism] than with these alternatives.
**与原骨架差异**: 每个替代解释用 "our [method] partially addresses this" 部分回应（不夸大为完全排除），收束句用**异质性模式本身**裁决——H3-H5 的调节显著性被二次利用为替代解释驳斥工具。关键是比较级措辞（"aligns more closely... than"）而非绝对排除。
**诚实边界**: 异质性裁决必须建立在已报告的调节显著性之上；"partially addresses" 的克制措辞不可省略；比较级收束（more closely than）不可替换为绝对断言（rules out）。

### 变体 32: R4 — 外部基准阈值分割 + 边际效应图阈值发现：连续调节的三层验证 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "We split the sample by the threshold of 166 miles, which corresponds to the definition of mega-commuting distance by the U.S. Census Bureau. … The marginal effects plot using the full regression model (column 4) shows that the threshold at which distance starts to matter is around 54.6 miles, which corresponds to the "long-distance commuting" distance of 50 or more miles by the U.S. Census Bureau (Online Appendix Figure C)."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R4
**骨架**:
> (1) The estimated coefficient on the interaction term between [continuous moderator] and [IV] is [direction] and [marginally] significant (B = [value], p = [value]). (2) We split the sample by the threshold of [N units], which corresponds to the definition of [external benchmark label] by [authoritative body]. The estimated coefficient is larger and significant in the [high-moderator] subsample (B = [value], p = [value]) than in the [low-moderator] subsample. (3) The marginal effects plot shows that the threshold at which [moderator] starts to matter is around [value], which corresponds to [external label corroboration].
**与原骨架差异**: 区别于变体 9（±1SD 条件边际效应）与变体 14（低基础率直方图）。本变体的核心是**阈值的外部锚定 + 数据发现的双向验证**——分割点来自权威基准（如 Census 定义）而非任意中位数，且边际效应图发现的阈值再用外部标签印证。
**诚实边界**: 外部基准必须真实存在且可引用；边际效应图发现的阈值与外部基准不能完全等同（本文 54.6 miles vs 50 miles benchmark——需说明对应关系）；跨子样本系数对比宜配 Wald 检验（本文缺失，见反模式）。

### 变体 33: R8 — 下游绩效事后分析：时间增长 + 多指标收敛 + 提示性收尾 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "Results show that structural similarity is positively associated with ΔROA in related acquisitions (Online Appendix Table A15). The positive relationship grows over time, with a one-standard-deviation increase in similarity linked to a 76.3% rise in ROA relative to the sample average by year 6."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R8
**骨架**:
> We examine whether [IV] is associated with improved [downstream outcome]. [Outcome] is measured as [Δ metric] from pre-[event] to [1-N year] post-[event] averages. Results show that [IV] is positively associated with [outcome] in [scope condition]. The positive relationship grows over time, with a one-SD increase in [IV] linked to a [X]% rise in [outcome] relative to the sample average by year [N]. These findings are robust to alternative measures ([BHAR / Tobin's Q]); additionally, [IV] is associated with lower likelihood of [negative marker]. We note that these analyses draw on a smaller subsample and treat these results as indicative rather than conclusive, offering suggestive but consistent evidence.
**与原骨架差异**: 区别于变体 5（MCMC 中介）与变体 21（枚举清单）。本变体展示**下游结果 post hoc 的完整展演**——时间动态（效应随时间增长）+ 多指标收敛（ROA/BHAR/Q/goodwill）+ 明确降权（indicative not conclusive）。
**诚实边界**: 下游绩效分析必须标注子样本缩小；"grows over time" 需有跨年数据支撑；提示性收尾（suggestive but consistent）不可省略，不可把 post hoc 绩效当 confirmatory 证据。

### 变体 34: R3 — 2×2 类型学交叉对角描述性比较：回归前的非参数类型对比 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**原始句锚点**: "Mirroring our main results, structural matches have the highest retention rates. In the cross-diagonals, 49.9% of target managers are retained by MM acquirers from LM targets compared with 42.2% of target managers retained by LM acquirers from MM targets (the difference is significant at a 5% level)."
**验证状态**: EMERGING
**写入日期**: 2026-07-25
**槽位**: R3
**骨架**:
> [Table] reports the share of [outcome] by [actor A type] and [actor B type] in [scope condition]. Mirroring our main results, [match cells] have the highest [outcome]. In the cross-diagonals, [X]% of [outcome] for [mismatch cell A] compared with [Y]% for [mismatch cell B] (the difference is significant at [level]). This pattern suggests that [theoretical interpretation: which mismatch direction is worse and why]. We examined this more formally in a regression model ([table]): the interaction term between [dissimilarity] and [type indicator] is [direction] and significant (B = [value], p = [value]).
**与原骨架差异**: 区别于变体 22（四分位单调性 model-free 开场）。本变体处理**类型学设计的非对称交叉对角**——理论载荷在"哪个错位方向更糟"（如 LM acquirer×MM target 比 MM acquirer×LM target 更差），用非参数单元格均值为回归交互提供直觉锚定。
**诚实边界**: 交叉对角差异的检验方法必须指明（t-test 类型——本文未指明，见反模式）；2×2 单元格均值只是描述性锚定，结论须由回归交互确认；理论解读须回应"为何这个错位方向更糟"。

### 变体 35: R3/R5 — 动态面板 ρ 持久性百分比解释 + 跨构念持久性对比 (1篇高价值)
**来源论文**: Pollock, Lee, Jin & Lashley (2015, Administrative Science Quarterly)
**原始句锚点**: "Thus the results in models 3 and 4 indicate that 62.3 percent of status and 50.3 percent of reputation in year t–1 persist in year t, holding other factors fixed, suggesting the evolutionary process of status exhibits a greater persistence (or path dependence) than that of reputation. The coefficient for the interaction between age and prior status suggests that the effect of prior status decreases by 5.4 percent each year as the VC firm ages."
**验证状态**: EMERGING（动态面板-GMM / 共演设计）
**写入日期**: 2026-07-30
**槽位**: R3/R5
**骨架**:
> "The results in models [M1] and [M2] support our baseline expectation that [construct A] and [construct B] will coevolve. [A] and [B] are positively and significantly related to each other in all models. Using the results in models [M1] and [M2] to assess their respective effect sizes, a [X]-percent increase in [A] and [B] leads to [Y1]-percent and [Y2]-percent increases in [B] and [A], respectively, holding all else fixed. Thus the effect of [A] on [B] appears to be greater than that of [B] on [A]. A Wald χ²-test (p < [level]) confirmed that the effect of [A] on [B] is significantly larger than that of [B] on [A] in our models."
>
> "As discussed above, the lagged dependent variable's coefficient reflects the degree of persistence or path dependence of the evolutionary process. Thus the results in models [M3] and [M4] indicate that [P1] percent of [A] and [P2] percent of [B] in year t−1 persist in year t, holding other factors fixed, suggesting the evolutionary process of [A] exhibits a greater persistence (or path dependence) than that of [B]. The coefficient for the interaction between [moderator] and prior [A] suggests that the effect of prior [A] decreases by [P] percent each [time unit] as the [actor] ages."
**与原骨架差异**: 两个相互因果构念的**效应大小对比** + 动态面板特有的 **ρ 持久性解释**。两个核心手法：(1) "5% 增加 → 3.2% vs 0.95%"的效应大小直接陈述，再用 Wald χ² 确认不对称方向显著；(2) 把滞后因变量系数 ρ 诠释为"% of [构念] in t−1 persists in year t"的持久性百分比，并跨构念对比（62.3% status vs 50.3% reputation → status 路径依赖更强），再把交互系数翻译为"每年减弱 P%"。后者是动态面板 Results 的标志性解释——把抽象 ρ 翻译成可理解的"路径依赖百分比 + 年衰减率"。适用于 dynamic panel / coevolution / 持久性构念。

### 变体 36: R3/R6 — 分样本 Wald χ² 系数比较 + partial support 诚实叙事 (1篇高价值)
**来源论文**: Pollock, Lee, Jin & Lashley (2015, Administrative Science Quarterly)
**原始句锚点**: "Although reputation has a larger coefficient in all models and status is not statistically significant in some models predicting reputation, the difference in coefficient size is statistically significant only for firms 11 or more years old. Thus H1a is partially supported and H1b is not supported."
**验证状态**: EMERGING
**写入日期**: 2026-07-30
**槽位**: R3/R6
**骨架**:
> "[H_a] argued that [A] would have a greater effect on [B] than [B] would have on [A] when [actors] are [young], while [H_b] argued [the reverse] when [actors] are [older]. To test these hypotheses we ran a series of regressions splitting the sample into subsamples based on different [age] increments, presented in [Table]. We began with [actors] less than or equal to, and greater than, [base age] years, and increased the lower age break by [N] years in each regression. Our analysis shows that [A] has a positive and significant relationship with [B] in all models, but [B] does not have a significant relationship with [A] until [actors] are [threshold] years old. The bottom row of the table shows the results of tests comparing the coefficients. Although [A] has a larger coefficient in all models, the difference in coefficient size is statistically significant only for [actors] [threshold] or more years old. Thus [H_a] is [partially supported] and [H_b] is [not supported]."
**与原骨架差异**: 当假设是"不对称方向随发展变化"且用**分样本阈值**检验（见 write-methods 动态面板-GMM 变体4）时，Results 核心是**跨阈值报告 χ²(1) 系数相等性检验 + 诚实判定 partial support**。关键手法：(1) 报告每个 age 阈值子样本的系数方向/显著性模式（如"reputation 所有模型显著，status 直到 9 岁才显著"）；(2) 报告每个阈值的 χ²(1)（"差异仅在 ≥11 岁显著"）；(3) 据此诚实判定"H1a 部分支持、H1b 不支持"而非强行全支持。区别于变体6（符号反转）：本变体检验的是**两个非嵌套方程系数的相对大小**随发展的变化，不是单一关系符号反转。

### 变体 37: R6 — GMM 零结果交互的 Monte Carlo 功效分析 (1篇高价值)
**来源论文**: Pollock, Lee, Jin & Lashley (2015, Administrative Science Quarterly)
**原始句锚点**: "We conducted a set of power analyses to ensure that the non-significant interaction between age and prior reputation was not due to low statistical power. … Thus we can safely conclude that the non-significant finding from our model estimates does not come from a type II error but from a negligible interaction effect."
**验证状态**: EMERGING
**写入日期**: 2026-07-30
**槽位**: R6
**骨架**:
> "We conducted a set of power analyses to ensure that the [non-significant interaction] between [moderator] and [prior construct] was not due to low statistical power. As our models use the [GMM estimation technique], we could not tap the well-established power-analysis procedure employed with ordinary least squares (OLS) regressions ([citation]). Instead, we conducted multiple Monte Carlo simulations to estimate the statistical power of our model ([citation]), using a significance level of [.05] and [1,000] iterations. According to the simulation results, our models' average power was [.91], suggesting they have sufficient power to detect even small effect sizes. Thus we can safely conclude that the non-significant finding from our model estimates does not come from a type II error but from a negligible interaction effect."
**与原骨架差异**: 当一个**关键的非显著交互**（如 H2 differentiated moderation 中"不变"那半：age×prior reputation 不显著）是理论预测的一部分，零结果不能默认接受——须排除 Type II error。但 GMM 估计下标准 OLS 功效程序不适用，故用 **Monte Carlo 模拟**（1000 次迭代，报告平均功效 .91）证明模型能检测小效应。这是把"零结果"从弱点转化为"确证性证据"的关键手法。适用于任何非线性/非 OLS 估计（GMM、SEM、MLE）下的理论关键零结果。

### 变体 38: R8 — post-hoc spline 重解释意外负效应（diminishing returns / 信息递减）(1篇高价值)
**来源论文**: Pollock, Lee, Jin & Lashley (2015, Administrative Science Quarterly)
**原始句锚点**: "Our post-hoc analysis, however, indicated that what we might instead be observing is a non-linear relationship between blockbuster deals and VC status. It may be that once a firm has had more than two blockbuster deals, thereby verifying that the first blockbuster deal was not a fluke, additional blockbuster deals are less surprising, provide little new information, and do not add to a firm's cognitive centrality."
**验证状态**: EMERGING
**写入日期**: 2026-07-30
**槽位**: R8
**骨架**:
> "As an alternative approach [to the surprising negative finding], we created a spline capturing the [first], [second], and [third] [event/instance]. Each variable took on a value of zero until that [instance] number had been reached and then had the value [1], [2], or [3], respectively, every year thereafter. For [outcome], the terms for [one] and [two] [instances] were significant, and the term for the [second instance] was [significantly larger/smaller] than for the [first], which is consistent with our other findings. For the other outcome, only the [second instance] was significant."
>
> "Our post-hoc analysis indicated that what we might instead be observing is a [non-linear / diminishing-returns] relationship between [event] and [outcome]. It may be that once a [actor] has had more than [N] [instances], thereby verifying that the [first] was not a fluke, additional [instances] are less [surprising] ([citation]), provide little new information, and do not add to [theoretical construct]. Future research should continue to explore these non-linear effects."
**与原骨架差异**: 当主分析出现**意外负效应**（如 blockbuster deals 对老 VC 的 status 反而显著为负），不强行解释为真负效应，而用 **post-hoc spline（首例/次例/三例分段）+ 平方项**重解释为 **diminishing returns / 信息递减**（首例最 surprising，后续边际信息递减 → 整体正向递减、高次数甚至转负）。关键：(1) spline 把"次数"分解为首/次/三例的边际效应；(2) 配合平方项确认曲线性（inflection point 在数据范围顶端 → 保守解读为 positive but diminishing）；(3) 用 expectancy-disconfirmation 理论（信息 novelty 随重复递减）解释。明确标注为 post-hoc 探索性分析（R8 非确证性 R7），并以"future research should explore"收尾。

### 变体 39: R7 — 替代估计器稳健性（3SLS）+ LDV 偏误诚实警示反向佐证主估计器 (1篇高价值)
**来源论文**: Pollock, Lee, Jin & Lashley (2015, Administrative Science Quarterly)
**原始句锚点**: "One possible benefit of using 3SLS instead of the AB estimator is a potential efficiency gain. This comes at a substantial cost, however, because 3SLS cannot address the bias stemming from the lagged dependent variables. … The pattern of results was the same as reported here, but the coefficients of the lagged dependent variables were quite inflated when compared with our AB results, and the model R2s were excessively high (approximately .97)."
**验证状态**: EMERGING
**写入日期**: 2026-07-30
**槽位**: R7
**骨架**:
> "[Alternative estimator, e.g., 3SLS] extends [2SLS] to a system of equations by incorporating the estimation feature of seemingly unrelated regression models. One possible benefit of using [alternative estimator] instead of the [primary estimator, e.g., AB] estimator is a potential [efficiency gain]. This comes at a substantial cost, however, because [alternative estimator] cannot address the bias stemming from the [lagged dependent variables]. Given that [consistency generally takes priority over efficiency], the [primary] estimator is more appropriate for our analysis. Nonetheless, we re-ran our models using [alternative estimator] and included [firm dummies] to deal with [unobserved heterogeneity]. Given the paucity of available instruments, we assumed that [one-year lags] of all covariates except for the [simultaneously determined variables] are exogenous. The pattern of results was the same as reported here, but the coefficients of the [lagged dependent variables] were [quite inflated] when compared with our [primary] results, and the model R²s were [excessively high (approximately .97)]. Given that [alternative estimator] does not control for the bias caused by [lagged dependent variables], this was not surprising. Further analysis using [single-equation 2SLS] found the results were almost the same as those from [alternative estimator], indicating there was little efficiency gain from using [alternative estimator] and further supporting our use of the [primary] estimator."
**与原骨架差异**: 当主估计器（AB-GMM）选择基于"**一致性优先于效率**"，稳健性用**更有效但有偏的替代估计器（3SLS）**重估，并**主动报告其缺陷症状**（LDV 系数膨胀、R²≈.97 异常高），把缺陷归因于替代估计器无法处理 LDV 偏误——**用替代估计器的失败反向佐证主估计器选择正确**。再用单方程 2SLS 确认 3SLS 无效率增益。这是比"结果不变"更高明的稳健性叙事：不是简单说"替代估计器结果一致"，而是诊断替代估计器为何会给出有偏结果。适用于动态面板/同时方程论文比较 GMM vs 3SLS/2SLS/FGLS。

### 变体 40: R4/R5 — Floodlight（Johnson-Neyman）分析符号反转线性交互：双转折点 + 90% CI 带 (1篇高价值)
**来源论文**: Malshe & Agarwal (2015, Journal of Marketing)
**原始句锚点**: "To explore this moderation in more detail, we followed Spiller et al. (2013) and performed a floodlight analysis using the method described in Mohr, Lichtenstein, and Janiszewski (2012). … When leverage is at approximately 65%, customer satisfaction has no impact on Tobin's q. However, it remains statistically nonsignificant until leverage reaches approximately 95%."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-30
**槽位**: R4/R5
**骨架**:
> "To explore this moderation in more detail, we followed [Spiller et al. (2013)] and performed a floodlight analysis using the method described by [Mohr, Lichtenstein, and Janiszewski (2012)]. Floodlight analysis involves plotting the [direct impact of the independent variable on the dependent variable] at numerous values of the [moderating variable]. Specifically, we began by fixing [moderator] at [0] and using increments of [.05] until [moderator] reached [1]. In all, we obtained [N] estimates of the [direct impact]. A plot of these estimates, along with the [90% confidence interval] band, is available in the [Web Appendix].
>
> We find that the impact of [IV] on [DV] [decreases linearly] at a rate of [−coefficient] for every unit increase in [moderator]. When [moderator] is at approximately [threshold_1], [IV] has [no impact] on [DV]. From this point onward, as [moderator] increases, [IV] has a [net negative] impact on [DV]. However, it remains [statistically nonsignificant] until [moderator] reaches approximately [threshold_2]. Beyond this point, [IV] has a [statistically significant negative] impact on [DV]. [Theoretical interpretation of the high-moderator region]."
**与原骨架差异**: 区别于变体17/18（Lind-Mehlum 用于**曲线**主效应/调节）与变体32（外部基准阈值 + 边际效应图）——本变体用 **floodlight（Johnson-Neyman 全调节变量范围边际效应 + CI 带）** 处理**线性交互的符号反转**（effect 在调节变量范围内由正过零转负）。关键报告**双转折点**：(1) **零交叉点**（effect = 0，方向反转处，如 ~65% leverage）；(2) **显著性交叉点**（CI 排除零处，如 ~95% leverage）。两点通常不同——零交叉先于显著性交叉，中间存在"净效应已为负但尚未显著"的灰色带。这比 ±1SD spotlight 更完整地展示"在何种调节变量水平上 IV 对 DV 由增值变减值"，是"阈值现象"（value-enhancing below X, value-destroying above X）的标准报告法。适用于交互效应在调节变量全域内变号的研究。
**诚实边界**: 两个转折点都须报告（仅报零交叉会高估反转的统计可靠性）；CI 带须明示置信水平（90% vs 95%）；转折点须落在数据支撑范围内（若 95% leverage 接近数据顶端，须提示外推风险）。

### 变体 41: R3 — 同时方程系统中的三条件中介检验（跨方程系数乘积 + Sobel）+ 非对称支持叙事 (1篇高价值)
**来源论文**: Malshe & Agarwal (2015, Journal of Marketing)
**原始句锚点**: "Sobel's test on the product of the two coefficients (b = −.341 = −.119 × 2.862) shows a statistically significant result (t = −2.19, p ≤ .05), in support of the mediating role of advertising in the leverage–customer satisfaction link. As a result, Sobel's test suggests that R&D does not mediate the negative impact of leverage on customer satisfaction. Thus, the results support H1a but not H1b."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-30
**槽位**: R3
**骨架**:
> "[H_a] and [H_b] posit that [mediator 1] and [mediator 2] mediate the [negative] impact of [IV] on [DV], respectively. To establish the mediation effect through [mediator j], we must satisfy the following three conditions: (1) the coefficient on [mediator j] in [Equation 1, the DV equation] must be [positive] and significant, (2) the coefficient of [IV] in [Equation j, the mediator equation] must be [negative] and significant, and (3) the product of the coefficient of [IV] in [Equation j] and the coefficient of [mediator j] in [Equation 1] must be [negative] and significant. To test the significance of the product term, we used [Sobel's test statistic using the formula given by Zhao, Lynch, and Chen (2010)].
>
> [Mediator 1]: [Condition 1 met: b = ..., p ≤ ...]. [Condition 2 met: b = ..., p ≤ ...]. [Sobel on the product: b = ... = (IV→M)×(M→DV), t = ..., p ≤ ...], in support of [H_a].
> [Mediator 2]: [Condition 1 met: b = ..., p ≤ ...]. [Condition 2 FAILED: IV has no significant effect on mediator 2, b = ..., p > .10]. As a result, Sobel suggests [mediator 2] does not mediate [...]. In summary, the results support [H_a], but not [H_b]."
**与原骨架差异**: 把 Baron-Kenny 三条件中介检验适配到**同时方程系统**——条件1的 M→DV 系数与条件2的 IV→M 系数来自系统内**不同方程**，条件3的间接效应 = 跨方程系数乘积，用 Sobel（Zhao, Lynch & Chen 2010 公式）检验乘积显著性。核心叙事价值在**非对称支持**：两个平行中介（advertising、R&D）一个支持（H1a）、一个不支持（H1b），不支持的**根因精确定位**到条件2失败（IV=leverage 对 R&D 无显著效应，b≈0），而非条件1（R&D→CS 边际显著）。这种"逐条件诊断哪个中介失败、且失败在哪一环"的报告，比笼统"H supported / not supported"更具诊断力，且为 Discussion 的机制讨论提供精确入口。适用于多中介并行检验（advertising + R&D、price + quality、recruitment + training）。
**诚实边界**: 条件2失败时须如实报告 IV→M 不显著（不可因 M→DV 显著就声称中介）；Sobel 检验假设间接效应正态分布，样本小时应补 bootstrap CI；"marginal significant"（p≤.10）的中介须标明。

### 变体 42: R6 — 反直觉反向结果的诚实报告 + 延迟到 Discussion 的事后解释 (1篇高价值)
**来源论文**: Malshe & Agarwal (2015, Journal of Marketing)
**原始句锚点**: "However, in contrast to H2c, we find that the interaction between leverage and one-year sales growth is negative (b = −5.376, p ≤ .01), indicating that leverage reduces customer satisfaction more severely for high-sales-growth firms. We elaborate on this counterintuitive result in the "Discussion" section and provide guidance for further research."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-07-30
**槽位**: R6
**骨架**:
> "Finally, according to [H_c], [DV] of the [hypothesized-higher-sensitivity group] should exhibit [higher/lower] sensitivity to [IV]. However, **in contrast to [H_c]**, we find that the interaction between [IV] and [moderator] is [opposite-sign] (b = ..., p ≤ ...), indicating that [IV] [reduces/increases] [DV] more [severely] for the [hypothesized-LOWER-sensitivity] group. We **elaborate on this counterintuitive result in the "Discussion" section** and provide guidance for further research. In summary, we find empirical support for [H_a] and [H_b] but **not for [H_c]**."
>
> [In Discussion:] "We hypothesized that [predicted direction]. However, empirically we find this to be true for [opposite group]. A potential explanation for this puzzling result is that [post-hoc mechanism]. [Data limitations] do not allow us to explore this possibility, but we hope that further research can resolve this issue."
**与原骨架差异**: 区别于变体6（符号反转跨条件 + **当场**理论解释）与变体30（预测性零结果作机制证据）——本变体处理**单一调节变量上预测方向反转**，且采用**两段式诚实叙事**：(1) Results 段**当场承认反转**（"in contrast to H_c"）+ **明确推迟解释到 Discussion**（不在 Results 强行编造机制）；(2) Discussion 段给出**事后（post-hoc）机制猜想** + **数据局限声明**（"do not allow us to explore... further research can resolve"）。这种"诚实承认 + 延迟解释 + 标注 post-hoc 与局限"的三段式，比在 Results 当场硬解释更审稿人友好（避免过度解读），也比隐瞒反转更诚信。适用于调节假设方向与数据相反、且机制需推测的研究。
**诚实边界**: 须在 Results 当场标明 "in contrast to H"（不可只在 Discussion 轻描淡写）；Discussion 的事后解释必须标注为推测（post-hoc / a potential explanation）而非确证；须承认数据局限并指向 future research；不可把反转重新包装为"部分支持"。


### 变体 74: R6 — 跨情境镜像 null 收束句（opposite-pattern summary；carpenterwestphal2001 型）

**来源论文**: Carpenter & Westphal 2001 (AMJ)
**skeleton_id**: `r6_cross_context_mirror_pattern_summary`
**原始句锚点**: "Thus, the results consistently show that the strategic relatedness of board ties increases director involvement in stable environments but does not do so in unstable environments. The opposite pattern emerges in unstable environments."
**验证状态**: EMERGING（单篇入库）
**槽位**: R6
**骨架**:
> Thus, the results consistently show that [IV variant A] increases [DV] in [context A] but does not do so in [context B]. The opposite pattern emerges in [context B]: [IV variant B] [direction] [DV], while [IV variant A] is [unrelated/negative].
**与原骨架差异**: 区别于变体 60（R6 调节变量主效应 null 驳斥 rival conjecture）与 R6 现有"方向证据与统计裁决分离"降级句式——本变体是**跨情境镜像 null 的段落级收束**：把"情境 B 中主效应变量失效"这一 null 从失败复述转化为调节假设的确认证据（null 本身就是理论预测的一半），再以 "The opposite pattern emerges" 一句钉死方向反转。适用于分样本/情境劈叉设计中 null 侧承载理论确证的场景。
**诚实边界**: "consistently show" 须有逐情境结果全部一致支撑；镜像句的两侧陈述必须与表格逐列对应，不得以总结句掩盖单侧个别指标的方向例外（本文 foreign market relatedness 不显著侧例外已在假设段显式交代）。

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:r6_cross_context_mirror_pattern_summary -->

### 变体 43: R4/R6 — 组内方向切换但不显著 → 直接组间系数差异裁决 (1篇高价值)
**来源论文**: Schumacher, Keck & Tang (2020, Strategic Management Journal)
**原始句锚点**: "We find that for firms close to bankruptcy our interaction term is insignificant for firms threatened by bankruptcy and consistent with our prediction switches signs. Specifically, for the interaction term between negative distance from aspiration level and the media-based overconfidence measure we now have β = 34.71, p = .36, CI95% [−40.56, 110.01], and for the interaction with the option-based measure we now have β = 1.58, p = 0.67, CI95% [−5.81, 8.98]. Supporting Hypothesis, we next employed a Chow test to analyze the difference in the interaction term coefficients between the two samples, and find significant differences for our media-based (χ2 = 5.84, p = .014) and option-based (χ2 = 4.74, p = .018) overconfidence measures."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-08-03
**槽位**: R4 / R6
**骨架**:
> Within the [boundary-present] subsample, the focal interaction changes to the predicted direction but is estimated imprecisely ([estimate], [p-value], [confidence interval]). This within-group result alone does not establish a reversal. We therefore directly test whether the interaction coefficient differs between [boundary-present] and [boundary-absent] groups. The coefficient-difference test rejects equality ([test statistic], [p-value]), supporting heterogeneity across the boundary while leaving the exact within-boundary slope uncertain.

**与原骨架差异**: 变体36也报告分样本 Wald 比较，但聚焦两个动态方程的相对大小与 partial support；本变体处理**同一交互关系在外部阈值两侧的条件差异**。其关键价值是把三个统计命题分开：①组内方向是否改变；②组内斜率是否显著；③两组系数是否显著不同。理论边界主要由③裁决，不能由“一组显著、另一组不显著”替代。

**诚实边界**: 组间差异显著只支持异质性；若边界组内 CI 跨零，不得声称该组的反转效应已确证。分组阈值必须事前有理论/外部依据，并报告阈值两侧 N 与不平衡程度。

### 变体 44: R8 — 三类构念效度威胁的定向三角验证 (1篇高价值)
**来源论文**: Schumacher, Keck & Tang (2020, Strategic Management Journal)
**原始句锚点**: "One alternative interpretation of our results is that our overconfidence measures reflect at least to some extent CEOs' accurate perception of their own high ability rather than biased self-perceptions. … following Chatterjee and Hambrick (2007), we identified in our sample those CEOs who had already served as CEO in another public company included in our sample. This yielded 33 CEOs; we then computed the correlation between their overconfidence-media scores for their tenures in both companies. We find that the scores are highly and significantly correlated (r = .77, p = .000) showing a high degree of consistency for each CEO across successive CEO positions."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-08-03
**槽位**: R8
**骨架**:
> We evaluate three rival interpretations of [latent actor trait]. First, a theoretically related [demographic/nomological] contrast should produce the opposite conditional pattern if the proposed trait interpretation is valid. Second, the proxy should remain associated for the same actor across organizational contexts if it reflects the actor rather than the focal organization. Third, accumulated feedback should not erase the relationship over a short horizon if the trait is relatively stable. Evidence across these tests strengthens the proposed interpretation, but does not uniquely identify the latent construct.

**与原骨架差异**: 不是普通 robustness checklist。三项分析分别对应三个构念效度威胁：`真实能力或相邻特质`、`企业特定而非个人特质`、`trait 随反馈内生更新`。每项都由 rival interpretation 立项，再用最匹配的观测模式回应，形成 nomological + cross-context + temporal 三角验证。

**诚实边界**: 人口特征对比依赖额外同质性假设；跨组织重复样本可能很小；短期稳定不等于永久不变；三角验证提升解释可信度但不能证明代理只测量一个潜在构念。

### 变体 45: R4 — 管道阶段集中异质性：亚组吸收全部前端优势后下游熄灭 (1篇高价值)
**来源论文**: Kim & Lee 2026 (Strategic Management Journal)
**原始句锚点**: "By contrast, the baseline coefficient on SRO across Models 1–3 is close to zero (p = 0.66, p = 0.90, and p = 0.87), suggesting that males are equally attracted to SRO and non-SRO companies. These results suggest that while female candidates are less likely than males to express interest overall, they are disproportionately more likely to express interest in SRO employers, and account for all of the estimated advantage enjoyed by SRO employers in the initial attraction stage (see Figure 2a)."
**验证状态**: EMERGING
**写入日期**: 2026-08-05
**槽位**: R4（可嵌入多阶段管道的 falling action）
**骨架**:
> We next test whether associations between [IV] and [stage outcomes] differ by [demographic/subgroup moderator]. Table [X] extends the main [stage] models by adding [IV] × [Moderator]. At the [front-end stage], the baseline coefficient on [IV] is close to zero (p = [value]), while the interaction is [direction] and statistically significant (p [relation] [threshold]); the pattern is robust to [unit] fixed effects where feasible (p [relation] [threshold]). These estimates indicate that [non-focal subgroup] shows no detectable association with [IV], and that [focal subgroup] accounts for essentially all of the estimated [front-end] advantage. This pattern does not persist in the [mid-pipeline] and [back-end] stages: the most-specified models find [IV] × [Moderator] coefficients that are [direction] and statistically imprecise (p = [value]; p = [value]). [If using unit FE for the main pipeline:] Because within-[unit] fixed effects absorb time-invariant [Moderator], between-subgroup comparisons rely on models without [unit] FE (or on split-sample margins); do not claim within-[unit] gender/demographic contrasts from FE columns.
**与原骨架差异**: 区别于变体8（主效应 null + 交互显著的条件化再定位）与变体27（跨阶段主效应衰减、无亚组分解）——本变体的核心是**组成性裁决 + 阶段熄灭**：(1) 用接近零的 baseline [IV] 证明非焦点亚组无关联，从而把已显著的前端主效应重写为"几乎全部由焦点亚组驱动"；(2) 在同一决策管道的中后段报告交互熄灭，把异质性本身做成管道衰减故事的一部分。适用于 multi-stage recruitment / funnel / ASA 设计中人口或偏好异质性只在信息稀薄的前端成立的叙事。
**诚实边界**: "accounts for all" 须有 baseline ≈ 0 的统计支撑，不可仅因交互显著就宣称；下游交互 null 受 post-treatment selection 约束（见 slot-R6 Slough）；关联语言优先（associated with / advantages），不可升级为因果异质性效应。配套管道主叙事见变体27。

### 变体 64: R3 — 双处理对照四拍 + Wald 系数差检验（post_2022_women_tmt_strategic_renewal 型）

**来源论文**: Post, Lokshin & Boone 2022 (AMJ)
**验证状态**: VERIFIED（expert_audit_override, user 2026-08-29）
**槽位**: R3

#### 报告骨架

```text
Supporting Hypothesis [H_a], results in Table [X] (Model [N]) show that [treatment_A]
[increase/decrease] [outcome_A] (b = [value], p = [value]), while [treatment_B] does not
(b = [value], p = [value]). Wald test results indicate that the difference between these
coefficients would likely not have arisen if the effects were the same (p = [value]).
Supporting Hypothesis [H_b], the [treatment_A] coefficient is significant (b = [value],
p = [value]) and the [treatment_B] coefficient is not (b = [value], p = [value]) in the
[outcome_B] model (Table [X], Model [M]). The estimated coefficients imply that
[treatment_A], on average, [decrease/increase] [outcome_B] by [value]% and
[increase/decrease] [outcome_A] by [value]%.
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 双假设共用一张对照表 | 两个 DV 各占一列，focal 与对照 treatment 并排 | 读者一眼看到"谁动了、谁没动" |
| 2. 每假设后跟 Wald 差分检验 | 把"星号对比"升级为系数差检验 | 防止审稿人质疑 t vs t+1 星号差异 |
| 3. 幅度拍合并为一句跨 DV 百分比翻译 | 由系数换算，不逐列重复 | 两个假设一段收尾，节奏紧凑 |
| 4. 对照处理全程只报"does not / is not" | 不解释不显著对照的幅度 | 保持对照的陪衬角色 |

#### 原文锚定
- "Supporting Hypothesis 1, results in Table 2 (Model 3) show that female TMT appointments increase TMT change orientation (b = 0.051, p = .018), while male TMT appointments do not (b = -0.003, p = .479)."（results.md Table 2 段）

#### 与最近变体的区别
- 区别于 r3_ols_four_beat_standard（单一处理四拍）：本变体是双处理并排对照 + Wald 系数差检验 + 跨 DV 合并幅度句。

### 变体 46: R7 — Cinelli–Hazlett 敏感性：以强观测协变量为倍数基准 (1篇高价值)
**来源论文**: Kim & Lee 2026 (Strategic Management Journal)
**原始句锚点**: "We conduct a sensitivity analysis that estimates how strong potential unobserved confounders would need to be to fully explain away the observed associations, following the procedure developed by Cinelli and Hazlett (2020). For interpretability, we compare estimates with Log Distance—the natural log of miles between the employer and candidate—a variable that is observed to strongly predict both attraction and selection."
**验证状态**: EMERGING
**写入日期**: 2026-08-05
**槽位**: R7
**骨架**:
> Because [IV] is a non-random [unit] attribute, a concern is that observed associations with [outcomes] could be sensitive to omitted variables. We conduct a sensitivity analysis that estimates how strong potential unobserved confounders would need to be to fully explain away the observed associations, following [Cinelli & Hazlett 2020]. For interpretability, we compare the required confounder strength with [strong observed predictor — e.g., log distance / size / prior performance] — a covariate that strongly predicts both [outcome_A] and [outcome_B] in our data. For [the stages / outcomes with significant associations], unobserved confounders assumed to be [k] times as strong as [benchmark] would still be insufficient to account for the estimated associations ([appendix table]). While this analysis does not rule out unobservables, it increases confidence that the estimated associations are not artifacts of omitted-variable bias alone.
**与原骨架差异**: 区别于变体15（RIR + Oster δ/Rmax 参数化遗漏变量）——本变体用 **Cinelli–Hazlett robustness-value 逻辑 + 观测强预测变量作倍数基准**（"even k× as strong as [Log Distance] still insufficient"），把抽象敏感性阈值翻译成审稿人可直觉比较的协变量强度。适用于观察性关联设计（非 DiD/实验）且已有一个理论/经验上强的观测预测变量可作 benchmark。corpus 此前无 Cinelli–Hazlett 命中。
**诚实边界**: 敏感性不证明因果；须明确只对已显著的 association 做该检验；benchmark 必须在同模型中确实强预测 outcome，不可事后挑选弱变量夸大稳健性；措辞保持 associational（"associations… not artifacts"）。

---

### 变体 47: R4 — 连续调节的 min/mean/max 三值边际效应表 + 斜率方向解读 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Following prior literature (Busenbark, Graffin, et al., 2022; Gamache, Devers, Klein & Hannigan, 2023; Wiersema & Bowen, 2009), we calculated the marginal effect of rival–MSCI CIO on MSCI ESG rating when the moderators assume different values (see Table 3). ... when rival ESG media controversies takes its minimum value, the negative marginal effect of rival-MSCI CIO on MSCI ESG rating is relatively weak (β = -0.166, p = .020); by comparison, when rival ESG media controversies takes its maximum value, the negative marginal effect of rival-MSCI CIO on MSCI ESG rating is much stronger (β = -0.344, p = .003)."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R4
**骨架**:
> Following prior literature ([citations]), we calculated the marginal effect of [predictor] on [DV] when the moderators assume different values (see Table [N]). For Hypothesis [Na], when [moderator] takes its minimum value, the [sign] marginal effect of [predictor] on [DV] is relatively weak (β = [value], p = [threshold]); by comparison, when [moderator] takes its maximum value, the [sign] marginal effect is much stronger (β = [value], p = [threshold]). Plotted in Figure [N], the marginal effect of [predictor] is almost always [sign] and significant across different values of [moderator], and [moderator] strengthens the [sign] marginal effect, consistent with Hypothesis [Na]. [For the target-side hypothesis: ...weakens the [sign] marginal effect, as illustrated by the positive slope, which supports Hypothesis [Nb].]

**与原骨架差异**: 区别于变体 9（调节边际效应的单侧显著报告——只报一侧）与变体 40（Floodlight 双转折点）——本变体是**连续调节的 min/mean/max 三值边际效应表 + 图 + 斜率方向语言**：三值（min/mean/max）表 + 每对调节用同一节奏（最小值弱→最大值强 + "almost always negative and significant" 诚实表达 + 斜率方向语言 strengthens/weakens）。二元调节（0/1）用两值版本。适用于连续/二元调节的四拍节奏扩展版。
**诚实边界**: "almost always significant" 须属实——若有区间不显著须如实说明；min/mean/max 三值的 p 值均须报告；二元调节须用 0/1 而非 min/max。

**适用**: 主效应+调节设计、边际效应图配套、调节效应的完整区间报告。

---

### 变体 48: R3 — 全模型交互显著性下降的共线吸收解释 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Model 8 includes both sets of moderating effects, with four moderators in total. The decrease in statistical significance observed in certain interaction terms might stem from the high correlation between media controversies and ESG awards (up to 0.60), which could absorb each other's moderating effect (Cortina, Markell-Goldstein, Green & Chang, 2021)."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R3
**骨架**:
> Model [N] includes both sets of moderating effects, with [K] moderators in total. The decrease in statistical significance observed in certain interaction terms might stem from the high correlation between [moderator family 1] and [moderator family 2] (up to [r]), which could absorb each other's moderating effect ([citation]).

**与原骨架差异**: 区别于变体 16（模型序列导航——只描述递进而未解释显著性下降）——本变体是**全模型交互显著性下降的共线吸收解释**：多个相关调节并存时，单个交互项显著性下降归因于调节变量间高相关（引用 Cortina et al. 2021），诚实承认而非掩盖。适用于 4+ 相关调节并存的全模型报告。
**诚实边界**: 必须报告实际相关值（up to [r]）；"might stem from" 是假设性解释——若全模型不显著项过多（超过一半），单句解释可能不足，需补充分模型 vs 全模型的系统性对比；不可把不显著宣称成显著。

**适用**: 多调节变量并存、调节间相关高（r > 0.5）的研究。

---

### 变体 49: R7 — ITCV 省略变量阈值解释（Frank 2000）(1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Based on Model 1 of Table 2, ITCV results show that an omitted variable would need to be correlated at 0.137 (-0.137) with rival-MSCI CIO and at -0.137 (0.137) with MSCI ESG rating to invalidate the focal inference. Correspondingly, the impact of an omitted variable must be -0.019 (= -0.137 × 0.137) to invalidate our inference. Among our controls, the variable with the strongest impact is rival ESG regulatory enforcements, which equals -0.005, far from the -0.019 threshold."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R7
**骨架**:
> To estimate the influence an omitted variable would need to have to invalidate our inferences in the main effect, we applied the ITCV approach ([citation]), which has been adopted in recent management research to address omitted variable bias (e.g., [citations]). Based on Model [N], ITCV results show that an omitted variable would need to be correlated at [r] ([r]) with [predictor] and at [r] ([r]) with [DV] to invalidate the focal inference. Correspondingly, the impact of an omitted variable must be [impact = r × r] to invalidate our inference. Among our controls, the variable with the strongest impact is [control], which equals [value], far from the [threshold] threshold. Combined with our comprehensive set of controls, our focal inference is unlikely to be driven by an omitted variable.

**与原骨架差异**: 区别于变体 15（RIR + Oster δ/Rmax）与变体 46（Cinelli–Hazlett 强协变量倍数基准）——本变体是 **ITCV（Frank 2000）**：省略变量需达到的**双重相关阈值**（predictor/DV）+ **impact 阈值**（乘积）+ **最强控制变量 impact 对比**（"far from the threshold"）——量化省略变量偏误防御。
**诚实边界**: ITCV 不证明因果；阈值与最强控制的对比须报告实际数字；"unlikely to be driven by an omitted variable" 只在该对比真实成立时使用。

**适用**: 观察性关联设计、有全面控制集的主效应省略变量防御。

---

### 变体 50: R7 — 双基准化检验：评级偏离合理基准 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "To address the possibility that common ownership in an ESG rating agency and a target firm's rivals is associated with actual ESG performance, we examined the extent to which MSCI's ESG rating deviates from the reasonable ESG benchmarks. We constructed a new dependent variable, MSCI-incident difference, by using the media coverage of the target firm's ESG risk incidents as a benchmark... Higher values indicate that MSCI ESG ratings deviated more from ESG incidents covered in the media."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R7
**骨架**:
> To address the possibility that [predictor] is associated with actual [performance], we examined the extent to which [agency's rating] deviates from the reasonable [performance benchmarks]. We constructed a new dependent variable, [rating-benchmark difference], by using [benchmark 1: media coverage of risk incidents] as a benchmark, as these incidents may directly capture a firm's [performance]. [Scaling logic: we generated scaled [rating] and scaled [benchmark] by scaling both to an interval between 0 and 1 to make them comparable.] We then measured [difference] using the formula: [difference] = scaled [rating] − (1 − scaled [benchmark]). Higher values indicate that [rating] deviated more from [benchmark]. [Benchmark 2: compared to a second agency's evaluation.] As shown in Model [N], when [benchmark evaluation] is the dependent variable, the coefficient for [predictor] is statistically insignificant, suggesting that [benchmark] may not be associated with [predictor]. As shown in Model [N+1], when [difference] is the dependent variable, the coefficient for [predictor] is [value] (p < [threshold]), consistent with our arguments.

**与原骨架差异**: 区别于变体 25（替代 DV 证伪——领域外结果预期不显著）——本变体是**双基准化检验**：构造"评级−外部基准"差变量（媒体事件基准 / 另一机构基准），先证基准本身与 predictor 无关（前门），再证差变量被 predictor 影响（后门）——偏差针对性地偏离合理基准而非真实绩效差异。两个独立基准互为复制。
**诚实边界**: 缩放逻辑（0-1 区间）须透明；基准选择须与 DV 同域（媒体事件/其他机构评估）；"may not be associated" 的基准不显著是前门必要条件，若基准本身与 predictor 相关则差变量解释失效。

**适用**: 评级/评分偏差研究、需区分"真实绩效差异 vs 评估偏差"的研究。

---

### 变体 51: R7 — 收购准自然实验：影响通道开关 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Prior to the acquisition by MSCI, KLD was privately owned, meaning the common owners of a target firm's rivals and MSCI would have been unable to influence the firm's ESG assessment by KLD; however, according to our theory, a negative relationship should exist after MSCI became the owner of KLD because common owners (of MSCI and other firms) could then influence KLD's ESG ratings. ... The coefficient for this interaction is -0.746 (p < .1, two-tailed test), indicating that the association between rival-MSCI CIO and KLD score became more negative after MSCI became the owner of KLD, also consistent with our theory."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R7
**骨架**:
> To mitigate [omitted variable and reverse causality] concerns, we conducted "quasi-natural" experiments on [ownership changes] associated with [acquisitions of the intermediaries]. Such acquisitions would have shifted the [common ownership] in an [intermediary] and rated firms, but this may not have been driven by [common owners]. Therefore, a pre- and post-acquisition analysis of [ratings] around these events could illustrate to what extent the change in [ratings] stemmed from the new common owners after these acquisitions. In [year], the [intermediary] was acquired by [acquirer], making it wholly owned by [acquirer]. Prior to the acquisition, [intermediary] was privately owned, meaning the [common owners] would have been unable to influence the [assessments]; however, according to our theory, a [sign] relationship should exist after [acquirer] became the owner because [common owners] could then influence [assessments]. [Second replication with another acquisition.] The coefficient for [predictor] × post-acquisition is [value] (p < [threshold], two-tailed test), indicating that the [sign] association became stronger after the acquisition. In untabulated results, we investigated the effect of [predictor] during the pre-acquisition period: the coefficient is [value] and statistically insignificant, indicating that it did not affect [outcome] prior to the acquisition.

**与原骨架差异**: 区别于变体 29（选择偏误三步防御：描述模式→CEM→Heckman）——本变体是**收购作为影响通道开关的准自然实验**：中介机构从私有（无法影响）→公开（可影响）的所有权切换，前后对比检验理论通道。双收购复制（KLD + ASSET4）+ 交互项（predictor × post）+ 收购前不显著（untabulated 诚实报告）。
**诚实边界**: p < .1 的弱显著性须如实报告（本文两尾）；"quasi-natural" 引导词不可省略；收购可能伴随其他变化（方法变更、数据调整）——须论证收购本身不直接影响 DV 生成过程；untabulated 的收购前结果必须真实存在。

**适用**: 影响通道开关型准自然实验（所有权变更、平台开放/关闭、机构私有/上市转换）。

---

### 变体 52: R8 — Bushee 投资者类型分解：动机/能力异质性 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Following Bushee (1998), numerous studies have distinguished dedicated institutional investors, which have long investment horizons and concentrated portfolio holdings, from transient institutional investors, which have short investment horizons and diversified portfolio holdings. ... As such, if our theory is accurate, we should observe that our main effect is stronger for dedicated institutional investors than for transient institutional investors. ... Model 1 of Table 11 shows that the coefficient for rival-MSCI CIO (dedicated) is -0.931 (p < .01) and the coefficient for rival-MSCI CIO (transient) is -0.249 (p < .05). A Wald test shows that the coefficients significantly differ (p = .039, one-tailed test)."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R8
**骨架**:
> As outlined in our study, the influence we theorize is likely to hinge on [mechanism element: an actor's motivation and ability] to influence [intermediaries]. Following [classification source], numerous studies have distinguished [type A actors], which have [long horizons and concentrated holdings], from [type B actors], which have [short horizons and diversified holdings]. Compared to their [type B] counterparts, and because of their more concentrated investments, [type A actors] are assumed to have more power to influence their portfolio firms ([citations]). Moreover, given their long investment horizons, they are more motivated than [type B] actors to exert their influence. As such, if our theory is accurate, we should observe that our main effect is stronger for [type A] than for [type B]. We tested this idea by separately replicating [the IV calculation] for [type A] and [type B] [and a third group], and standardized these variables for the regression. [Model results: the coefficient for [type A] is [value] (p < [threshold]) and the coefficient for [type B] is [value] (p < [threshold]).] A Wald test shows that the coefficients significantly differ (p = [value], [one/two]-tailed test).

**与原骨架差异**: 区别于变体 44（构念效度威胁定向三角验证——多指标收敛）——本变体是**机制异质性分解**：用既有分类（Bushee 1998 投资者类型）把"动机/能力"操作化为可比较的亚型，主效应按类型分解 + 系数对比 + Wald 检验——验证"效应由该机制类型驱动"。补充分析标签（supplementary）。
**诚实边界**: 分类必须引用既有文献（不可自造）；Wald 检验是必需的（无检验的 "larger vs smaller" 描述性断言是反模式）；若亚型间差异不显著但各自显著，如实报告"both types show the effect, difference not significant"。

**适用**: 机制异质性验证（投资者类型、所有权结构、行为者类型的亚组分解）。

---

### 变体 53: R2 — 逐调节引入→成对→全模型的 8 模型导航 (1篇高价值)

**来源论文**: DesJardine, Li & Shi (2025, AMJ)
**原始句锚点**: "Model 6 includes both reputational threat moderators, and the results continue to support Hypothesis 1, Hypothesis 2a, and Hypothesis 2b. Likewise, Model 7 includes both reputational opportunity moderators and the results continue to support Hypothesis 1, Hypothesis 3a, and Hypothesis 3b. Model 8 includes both sets of moderating effects, with four moderators in total."
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-09
**槽位**: R2
**骨架**:
> [Model 1: main effect.] [Model 2-5: each moderating relationship entered separately — one per hypothesis, each with coefficient and p-value.] [Model 6: both [family-1] moderators — results continue to support H1 and the [family-1] hypotheses.] Likewise, [Model 7: both [family-2] moderators — results continue to support H1 and the [family-2] hypotheses.] [Model 8: both sets of moderating effects, with [K] moderators in total.] [Caveat: the decrease in statistical significance in certain interaction terms might stem from the high correlation between [family 1] and [family 2] (up to [r]), which could absorb each other's moderating effect ([citation]).]

**与原骨架差异**: 区别于变体 16（主效应→双向→三向递进——三向交互论文）——本变体是**4 个两向交互的逐步引入**：Model 1 主效应 → Model 2-5 各单调节 → Model 6-7 成对聚合（威胁对/机会对）→ Model 8 全模型——两两成对聚合是核心结构（成对模型既验证 family 内一致性又逐步逼近全模型）。末句共线吸收预告（与变体 48 同源）。
**诚实边界**: 成对聚合（Model 6/7）必须按理论 family 分组而非随意两两；"continue to support" 只在该模型确实支持时使用；全模型显著性下降的预告须与变体 48 解释一致。

**适用**: 多调节（4+）、可归入 2 个理论 family 的研究；主效应+两向交互的逐步引入。

---

### 变体 54: R7 前端识别防御 — RIR 替换计数 + naive-vs-cure (2SRI) 配对 (1篇高价值)

**来源论文**: Ridge, Kim, Ingram & Lee 2024 (Academy of Management Journal)
**原始句锚点**: "RIR results suggest that to alter our inferences for lobbying breadth, 675 observations would have to be replaced with observations for which there is an effect of zero, and for competitive actions, 1,793 observations would have to be replaced... we follow best practices to diagnose potential endogeneity and assess robustness across analyses."
**验证状态**: EMERGING（单篇 section_variant）
**写入日期**: 2026-08-12
**槽位**: R7
**骨架**:
> A concern in testing how [characteristic] affects [outcome] is endogeneity, especially from nonrandom [selection]. First, we use robustness of inference to replacement (RIR): to alter our inferences for [outcome 1], [N] observations would have to be replaced with observations for which there is an effect of zero, and for [outcome 2], [N] observations. Next, we pair 'naive' analyses that do not use tools to 'cure' endogeneity with analyses that attempt such a cure [e.g., two-stage residual inclusion], finding estimates are consistent across approaches.
**与原骨架差异**: 区别于变体15（Li 2026 五威胁标签化序列 RIR+Oster+CEM 三件套）与变体2（基础四威胁叙述）——本变体是**前端识别防御节奏**：内生性作为唯一组织性 threat 且**前置到主结果之前**（先建立可信度再展示证据），RIR 用**可替换观测计数**量化稳健性（675 / 1,793 obs），并以 **naive-vs-cure 配对**（不处理 vs 2SRI residual inclusion）收束于 "estimates are consistent across approaches"。RIR 的量化替换计数（"N observations would have to be replaced"）是关键节奏标记。
**诚实边界**: RIR 需在 Methods/Appendix 说明替换阈值与 Oster δ/Rmax 等参数；2SRI 需报告工具变量及其外生性论证；naive-vs-cure 配对要求两套分析在同一 DV 上可比，且 "consistent across approaches" 不可夸大为因果识别。

**适用**: 非随机选择是主要内生性威胁的非实验研究；希望在主结果之前完成识别防御的结构；RIR 已有可报告的替换计数。

---

### 变体 55: R5 外部证据实际重要性辩护拍 — "likely to be particularly important in practice" (1篇高价值)

**来源论文**: Ridge, Kim, Ingram & Lee 2024 (Academy of Management Journal)
**原始句锚点**: "Evidence suggests that even small changes in lobbying can net significant benefits such as tax rate savings... meaning the 7% decrease we observe is likely to be particularly important in practice."
**验证状态**: EMERGING（单篇 section_variant）
**写入日期**: 2026-08-12
**槽位**: R5
**骨架**:
> A [one-SD] increase in [predictor] corresponds to a [value]% [increase/decrease] in [outcome]. Evidence suggests that even small changes in [outcome] can net significant benefits such as [external evidence]. Thus, the [value]% change we observe is likely to be particularly important in practice.
**与原骨架差异**: 区别于 r5_ols_embedded_magnitude（只给幅度+语境对比）与变体13（交互联合翻译）——本变体追加**实际重要性辩护拍（拍5）**：先给幅度（"A [one-SD] increase... corresponds to a [value]% [change]"），再用**外部文献锚定**证明微小变化净显著收益（"even small changes in [outcome] can net significant benefits such as [external evidence]"），收束于 "likely to be particularly important in practice"。与生存分析变体15 "every day counts"（darby2025）同属实际重要性辩护节奏，但场景为**百分比幅度 + 外部收益锚**而非天数 + stakes 重框。
**诚实边界**: 外部证据必须来自已发表文献或可核验基准，且须与该 [outcome] 的决策场景对应；"likely to be particularly important" 是判断而非事实，须由外部锚支撑；幅度与外部锚必须同量纲可比。

**适用**: 效应量看似小的观察性研究，需要用外部证据把"小 %"翻译为"实际重要"；百分比幅度的主效应或调节效应。

---

### 变体 56: R2 Direct/Indirect/Total 路径表架构 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "We compare the coefficients for the impact of changes in recall magnitude in the direct-effects model (see Table 4) and the total-effects model (see Table 5)."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R2

**骨架**:
> We report the [direct-effects] estimates in [columns] of [Table X] and the [indirect-effects] estimates in [column] of the same table. The [direct-effects] model tests the association between changes in [predictor] and subsequent changes in [outcome_1] and [outcome_2]. The [total-effects] model, reported in [Table Y], retains that direct path and adds the indirect path through changes in [mediator]. We compare coefficients on [predictor] across the [direct-effects] and [total-effects] specifications before testing the product of paths.

**与原骨架差异**: 区别变体 16/53（层次列递增）与变体 24/28（Heckman 两阶段）——本变体是 Direct/Indirect/Total 路径表架构，把中介 climax 做成表上的系数对照。

**诚实边界**: 因果语言降为 association；比较系数不等于中介成立，须接衰减/Sobel/bootstrap。

### 变体 57: R3 测量覆盖范围 warrant「学习」而非仅修复 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "We interpret this finding as indicative of learning because the reliability measure ... is aggregated across all new models of the make in the following year (i.e., including models not affected by the recall)."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R3

**骨架**:
> Consistent with [H_a], the coefficient for changes in [predictor] on subsequent changes in [mediator] is [positive/negative] and significant ([coefficient], p < [threshold]). We interpret this association as indicative of [mechanism: learning] because the [mediator] measure is aggregated across [coverage: all new models of the unit in the following period], including [units not directly affected by the event].

**与原骨架差异**: 区别变体 41（检验中介是否成立）——本变体用测量覆盖范围为 a-path 提供学习机制 warrant，否则显著正系数只是修复被召回单元。

**诚实边界**: 写 indicative of 而非 causes learning；覆盖范围必须是测量事实，不能事后发明。

### 变体 58: R3 Direct-vs-Total 衰减 + 嵌套χ² + Sobel + bootstrap 堆叠确认 (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "Collectively, we find support for our hypotheses that product reliability partially mediates the relationship between recall magnitude and future injuries (H2b) and future recall frequency (H2c)."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R3

**骨架**:
> To test whether [mediator] transmits the association between [predictor] and [outcome], we use sequential procedures [Baron and Kenny (1986)] and compare coefficients on [predictor] in the [direct-effects] model ([Table X]) and the [total-effects] model ([Table Y]). The coefficient is [direction] in the [direct-effects] model ([value], p < [threshold]) but smaller in magnitude in the [total-effects] model ([value], p < [threshold]). This pattern implies that the association manifests in part through the [mediator] pathway. Following [prior citation], we computed Sobel's test statistic ([value], p < [threshold]; report one- vs two-tailed explicitly). Following [Zhao, Lynch, and Chen (2010)], we generated an empirical sampling distribution for the indirect effect with [N] bootstrap samples; the [95%] bootstrap confidence interval is ([lower], [upper]) and excludes zero. Nested chi-square comparisons show that the [total-effects] model fits significantly better than the [direct-effects] and [indirect-effects] models (Δχ²([df]) = [value], p < [threshold]). Collectively, [mediator] partially mediates the relationship: the indirect path is distinguishable from zero, and the remaining direct path remains significant. Thus, [H_mediation] is supported.

**与原骨架差异**: 区别变体 41（SUR 非对称失败）与变体 5（post-hoc MCMC）——本变体是 confirmatory 部分中介的堆叠确认。BK 不替代区间。

**诚实边界**: partial 不得升级 full；Sobel 单尾必须标明；一阶差分+IGLS 不得写 lead to / have an effect。

### 变体 59: R4 spotlight ±1SD + Δslope + region of manifestation（含无方向假设变体） (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "This spotlight analysis again provides evidence to support H3 and highlights the region in which this interaction effect manifests."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R4

**骨架**:
> [H_mod] posits that the [positive] association between [predictor] and [mediator] is stronger when [moderator] is higher. As evidenced in [Table X], the coefficient for the interaction is [positive/negative] and significant ([value], p < [threshold]). Thus, [H_mod] is supported: [theoretical translation of the interaction, not of the main effect]. To gain a deeper understanding of this interaction, we followed [Aiken and West 1991] and performed a spotlight analysis, shifting the mean of [moderator] up and down by one standard deviation. The association is [positive] and significant at high [moderator] ([value], p < [threshold]) but insignificant at low [moderator] (p > [threshold]). The slopes differ across high and low levels (Δslope = [value], p < [threshold]). This spotlight analysis again provides evidence to support [H_mod] and highlights the region in which this interaction effect manifests. [Nondirectional variant:] Recall that we proposed a nondirectional hypothesis for the moderating effect of [moderator]. The interaction is [negative] and significant ([value], p < [threshold]). Thus, [units] of higher [moderator] are [less] [motivated/able] than [units] of lower [moderator] to [improve the mediator].

**与原骨架差异**: 区别变体 9（无 Δslope）与变体 40（floodlight 变号）——一侧显著一侧不显著时，region 主张必须有 Δslope。无方向变体分开写。

**诚实边界**: 无交互图仍可写；无方向调节的符号解读是竞争预测裁决，不是预先定向假设的支持。

### 变体 60: R6 调节变量主效应 null 驳斥 rival conjecture (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "We do not find the direct impact of shared product assets on reliability to be statistically significant (p > .10). Thus, there is no evidence to support conjectures that sharing of product assets adversely affects reliability."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R6

**骨架**:
> We do not find the direct association of [moderator] with [mediator] to be statistically significant (p > [threshold]). Thus, there is no evidence to support conjectures that [rival claim].

**与原骨架差异**: 区别变体 30（预测性机制 null）——本变体是调节变量主效应 null 驳斥有害猜想，不是假设支持。

**诚实边界**: null 不升级为 H 支持；conjectures 措辞可保留。

### 变体 61: R7 面板 GLS 四威胁电池（测量 / IGLS vs PCSE / 单元上卷 / 滞后 BIC） (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "The results with firm as the unit of analysis are consistent with those reported for the make unit of analysis, though, as might be expected, the statistical significance for some of the findings is at marginally higher levels."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: R7

**骨架**:
> To assess the robustness of our empirical findings, we conducted a battery of additional tests. [Threat 1 — Measurement / size confound]: A potential concern about this measure is that some of the indicants might be correlated with [confound: size]. We reestimated using [subset measures that drop the confounded indicants]. As [Web Appendix Table] indicates, the substantive conclusions remain unchanged. Thus, the results are not an artifact of the measure used to operationalize [construct]. [Threat 2 — Alternate estimator]: We estimated the results using the [primary: IGLS] estimator to account for [first-order serial correlation, cross-sectional dependence, and heteroskedasticity]. We assessed robustness to [PCSE / Prais-Winsten]. The estimates are similar, though the standard errors are slightly higher for the [alternate] estimator. Importantly, the substantive conclusions are the same regardless of whether [primary] or [alternate] is used. [Threat 3 — Unit of analysis]: We reestimated using the [higher-level unit] rather than [primary unit], aggregating to [N] observations and excluding [year dummies] to conserve degrees of freedom. The results are consistent, though, as might be expected, the statistical significance for some of the findings is at marginally higher levels. [Threat 4 — Lag structure (specification justification, not coefficient robustness)]: We compared fit statistics of models with alternate lag structures using [BIC]. A specification with [one lag of the DV and one lag of the IVs, i.e., ADL(1,1)] offers the best fit. Thus, a [one-period] time lag between the independent variables and dependent variables is appropriate in this context.

**与原骨架差异**: 区别变体 2（通用威胁）与变体 39（替代估计器失败反向佐证）——本变体是 IGLS/PCSE + 分析单元上卷 + 滞后 BIC。滞后 BIC 是规格辩护，不是系数稳健性。

**诚实边界**: 分析单元上卷后须报告 marginally higher p，不得只写 consistent；滞后 BIC 不得写成结果不变。

### 变体 62: R8 — 二元策略完全中介 firm characteristics + 市场信号收束（legacy Kenny）(1篇高价值)

**来源论文**: Chen, Ganesan & Liu 2009 (Journal of Marketing)
**source**: chenganesanliu2009
**skeleton_id**: `r8_ols_strategy_complete_mediation_kenny_signal`
**原始句锚点**: Based on the steps that Kenny, Kashy, and Bolger (1998) outline, these effects indicate that product-recall strategies completely mediate the influences of firm characteristics on abnormal returns.
**验证状态**: VERIFIED（单篇 section_variant；**LEGACY**）
**写入日期**: 2026-08-12
**槽位**: R8
**骨架**:
> A question, then, is whether these [firm_characteristics] influence firms' choice of [strategy]. If we obtain significant effects of [firm_characteristics] on strategy choice, it would indicate that [strategy], as a signal to the stock market, mediate the effects of [firm_characteristics] on [AR] ([Kenny citation]). We estimate a probit on Pr([strategy]). [Key_firm_char] is significantly [negative/positive], suggesting that [theory_buffer_claim]. More important, [AR_table] and [probit_table] jointly show the mediation effects: (1) the direct impact of [strategy] on [AR] is significant, and (2) [firm_characteristics] that influence strategy choice, especially [key_firm_char], do not affect [AR] when [strategy] is included. Based on the steps that [Kenny et al.] outline, these effects indicate that [strategy] completely mediate the influences of [firm_characteristics] on [AR]. Therefore, the stock market consolidates the impact of various firm and product characteristics and reacts mainly to a firm's [strategy] as a signal to evaluate the potential consequence of the crisis.
**与原骨架差异**: 区别于变体 41（同时方程三条件 + Sobel 乘积检验）与变体 5（MCMC 显式间接效应 CI）——本变体是**二元策略中介** firm characteristics 对 AR 的 **legacy Kenny 条件计数**展演：问句 → probit 选择方程 → 联合读表（策略→AR 显著 + firm→策略显著 + firm→AR 直接路径消失）→ complete mediation → 市场以策略为危机后果信号。定位为 supplemental/mechanism（R8），非主假设四拍。
**诚实边界（强制 · LEGACY）**: 不得将 Baron–Kenny 条件计数升级为现代间接效应证据；写入时必须要求补充 indirect-effect interval（bootstrap/PROCESS/Sobel）**或**显式标注 legacy complete-mediation claim。Kashmiri 诚实边界继续有效：不得用条件计数替代间接效应区间。因果语言优先 `associated with` / `mediate the influences` 的关联读法，不可升为现代因果中介识别。

**适用**: 截面 AR/CAR + 二元策略选择；firm/product characteristics 直接影响消失、策略路径显著；仅作历史范式参考或显式 legacy 报告。

---

### 变体 68: R4 交互通道分解句 — 调节效应经差值 DV 的哪个分量起作用（westphal_bednar2005 型）
**来源论文**: Westphal & Bednar (Administrative Science Quarterly)
**原始句锚点**: "friendship ties reduce the difference between reported concern about strategy and the perception of others' concern by increasing the latter (i.e., the perceived concern of other board members) rather than by decreasing the former..."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-08-29
**槽位**: R4
**骨架**:
> Moreover, the data also indicated that [moderator] reduces [the difference between component_A and component_B] by increasing the latter (i.e., [component_B]) rather than by decreasing the former (i.e., [component_A]); although [moderator] was strongly and positively associated with [component_B] at [sample condition], it was not significantly related to [component_A].
**与原骨架差异**: 交互主报告后追加通道归属句：说明调节效应经由差值/合成 DV 的哪个分量传导——同模型内双分量证据（一分量显著、另一分量不显著）。适用于 DV 为两分量差值或合成的设计（self-report vs 对他人感知、自评 vs 他评等）。
**诚实边界**: 通道主张须由同模型内双分量系数直接佐证，不得仅凭总效应推断；分量高度相关时通道归属可能不稳定，宜补分量系数差检验或明示其为解释性证据。


### 变体 73: R4 — 分样本主检验 + 交互项复核收口（split-sample primary, product-term corroboration；carpenterwestphal2001 型）

**来源论文**: Carpenter & Westphal 2001 (AMJ)
**skeleton_id**: `r4_split_sample_primary_product_term_corroboration`
**原始句锚点**: "Complementarity in strategic relatedness is positively related to directors' perceived ability to contribute for all four dimensions of corporate strategy, supporting Hypothesis 2a. ... We also conducted separate analyses using the product term approach to test interactions between environmental stability and the independent variables, and the interactions were significant, consistent with the split-sample findings."
**验证状态**: EMERGING（单篇入库）
**槽位**: R4
**骨架**:
> [Context-B pattern sentence: "[Moderator-conditioned IV form] is positively related to [DV] for all [N] dimensions of [IV], supporting Hypothesis [N] ([Table Y])."] At the same time, the results show that [simple-effect form] does not predict [DV] [in context B]. [Null mirror sentence for context A: "In contrast, [simple-effect form] was significant in [context A] (Table X), while [moderator-conditioned form] was consistently unrelated to [DV]."] We also conducted separate analyses using the product-term approach to test interactions between [moderator] and the independent variables, and the interactions were significant, consistent with the split-sample findings.
**与原骨架差异**: 区别于变体 65（R4 分样本镜像对照 + 组内 Wald + Chow 诚实降级）与变体 3（连续调节三向交互）——本变体是**方向反转式分样本调节的收口节奏**：主检验由分样本承载后，不显著侧的"主效应 rival"被写成确认性 null（does not predict），末句用 product-term 交互复核把分样本发现升级为正式交互证据。适用于情境假设（scope-conditioned hypotheses）+ 分样本主检验、交互项只作复核而非主检验的设计。
**诚实边界**: 交互复核只报方向与显著性（significant, consistent with the split-sample findings），不解读交互系数大小；分样本裁决未经系数差检验时不得宣称"significantly stronger in B than A"——宜补组间系数差检验或按变体 65 诚实降级。

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:r4_split_sample_primary_product_term_corroboration -->

### 变体 69: R8 理论前提实证验证双通道 — 样本内前提检验 + 样本外前提问卷（westphal_bednar2005 型）
**来源论文**: Westphal & Bednar (Administrative Science Quarterly)
**原始句锚点**: "A premise of our theoretical argument is that directors tend to perceive some risk to their social esteem in expressing concerns about the viability of the current corporate strategy when those concerns are not shared by others... We assessed the validity of this premise empirically..."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-08-29
**槽位**: R8（副槽位 R7）
**骨架**:
> A premise of our theoretical argument is that [premise]. This assumption was strongly supported by the data: when [condition below threshold], the mean level of [DV] is significantly greater than when [condition above threshold] (t = [value], p < [.001]), and [DV] was not significantly correlated with [variable] within either [subsample]. Thus we tested the hypotheses for [restricted subsample]; we used the [Heckman model] to correct for sample selection bias, which allows us to generalize the results to the full sample. We also assessed the validity of this premise empirically by collecting additional survey data for [units] in our sample frame: of the [N] respondents ([rate] percent), a large majority ([share] percent) [endorsed premise items], which supports our premise that [restated premise] ([K-S] tests indicated no significant differences between the survey sample and the larger sample frame).
**与原骨架差异**: 双通道验证理论前提——(a) 样本内：阈值两侧均值对比（t 值）+ 侧内相关不显著，证明样本切割前提成立，随即以 Heckman 选择模型交底切割后果并宣称可推广回全样本；(b) 样本外：为前提命题追加独立问卷，报响应率、逐题支持百分比 + K-S 代表性收口。把"假设的前提"升格为"被检验的前提"。
**诚实边界**: 样本外前提问卷为验证性非假设检验，逐题百分比不作推断统计（当代做法：一句结论 + 在线附录，题项全文入正文属年代特征）；Heckman 的 generalization 主张限于选择方程设定正确。


### 变体 75: R8 — 连续 DV legacy Baron–Kenny 中介句（separate-analysis 包装；carpenterwestphal2001 型）

**来源论文**: Carpenter & Westphal 2001 (AMJ)
**skeleton_id**: `r8_baron_kenny_continuous_mediation_separate_analysis`
**原始句锚点**: "A separate analysis provided evidence that directors' perceived ability to contribute effectively mediated these relationships: when ability to contribute is added to models of monitoring and advice interactions, the effects of the relatedness variables become nonsignificant, and the coefficient for ability to contribute is strongly and positively significant in both models (Baron & Kenny, 1986)."
**验证状态**: EMERGING（单篇入库；**LEGACY**）
**槽位**: R8
**骨架**:
> A separate analysis provided evidence that [mediator] mediated these relationships: when [mediator] is added to models of [DV1] and [DV2], the effects of the [IV] variables become nonsignificant, and the coefficient for [mediator] is strongly and positively significant in both models ([mediation citation]).
**与原骨架差异**: 区别于变体 62（二元策略 probit 选择方程的 legacy Kenny 完全中介 + 市场信号收束）与变体 5（MCMC 显式间接效应 CI）——本变体是**连续 DV 双结果模型的 legacy Kenny 条件计数**：主检验段内以 "A separate analysis provided evidence that ..." 一句带出，三步条件（IV→M 显著、M→Y 显著、加入 M 后 IV→Y 消失）压缩进单个冒号句，服务于两个单元层假设 (H1b/c) 的机制收口。定位为机制佐证（separate analysis），非主假设四拍。
**诚实边界（强制 · LEGACY）**: 同变体 62 边界——不得将 Baron–Kenny 条件计数升级为现代间接效应证据；写入时必须要求补充 indirect-effect interval（bootstrap/PROCESS/Sobel）**或**显式标注 legacy complete/partial-mediation claim；"mediated these relationships" 措辞须降为关联读法（mediate the influences / are consistent with mediation）。

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:r8_baron_kenny_continuous_mediation_separate_analysis -->

### 变体 70: R2 先验支持判据声明 — 差值/合成检验的判定规则先行（westphal_bednar2005 型）
**来源论文**: Westphal & Bednar (Administrative Science Quarterly)
**原始句锚点**: "We regressed this measure on a dummy variable set equal to 1 for directors' concern about strategy and 0 for directors' perception that others were concerned...; a positive and significant coefficient for the dummy variable would provide support for hypothesis 1."
**验证状态**: EMERGING（单篇入库）
**写入日期**: 2026-08-29
**槽位**: R2（副槽位 R3）
**骨架**:
> We [created a dataset with two records per unit / constructed a test variable], set equal to [1] for [focal component] and [0] for [benchmark component]. We regressed this measure on [test variable(s)] together with the control variables; a [positive/negative] and significant coefficient for [test variable] would provide support for hypothesis [N]. To test hypotheses [N1–N3], we interacted [test variable] with our measures of [moderator_1], [moderator_2], and [moderator_3].
**与原骨架差异**: 在报告任何系数之前显式声明判定规则——"a [direction] and significant coefficient for [test statistic] would provide support for hypothesis [N]"——把"什么算支持"先于结果交代；同时交代检验变量的编码方式（dummy 1=[self-report] vs 0=[benchmark]）。适用于差值/合成/配对检验设计；与当代开放科学的预注册式判定规则精神兼容，语料其余 R3 四拍变体均从"Hypothesis [x] predicted..."复述开始，无此拍。
**诚实边界**: 判定规则一经声明须严格执行（含方向），不得事后改判单/双侧或显著性档位；当代报告仍须补幅度拍与 CI，本句不替代四拍。

[功能标签]: R3 幅度拍 — 显式算术除法翻译（系数→货币→占基数百分比）
[骨架]: "The [direction] and statistically significant coefficient ([coefficient], p < [threshold]) in Column [I] suggests that [treated units] responded to [event] by [direction phrase] their [outcome]. Specifically, in each [unit_1] and each [unit_2] following [event], [treated units] [outcome]—on average—[coefficient] × [unit scale] = [amount] (or [USD equivalent]) [more/less] than what they spent in a pre[event] [unit_1-unit_2], on average. This number amounts to a [X]% [drop/increase] ([amount] ÷ [base])."
[关键特征]: 拍3 不满足于 'a Y-unit change'，而是展示完整算术链：β × 度量单位 = 本币金额（括号给美元换算）→ 金额 ÷ 事件前均值基数 = 百分比；基数在括号内显式出现使读者可复算；同一基数（prerecall 均值）贯穿全部成分列，保证跨列百分比可比
[适用]: 系数度量单位与原始金额单位不同（万元、千元）需要显式换算的面板设计；多成分分解故事的幅度统一换算
[节奏标记]: [方向+显著性][换算句 β×unit=amount][除法句 amount÷base=%]
**原始句锚点**: "Specifically, in each week and each prefecture following the recall, Sagitar's substitutes spent on advertising—on average—RMB 140 (or US$19) less than what they spent in a prerecall week-prefecture, on average."
**来源**: fang_et_al_2025_rival_recall_ad_spend (POM), §4.2


### 变体 71: R2 — 估计策略宣告 + 分样本设计导航段（carpenterwestphal2001 型）

**来源论文**: Carpenter & Westphal 2001 (AMJ)
**skeleton_id**: `r2_ols_estimation_strategy_split_sample`
**原始句锚点**: "Given that all our dependent variables were continuous and that the independent variables were continuous or categorical, multiple ordinary least squares (OLS) regression analysis was the primary statistical technique employed. ... The entire sample was dichotomized at the median of the environmental stability measure..."
**验证状态**: EMERGING（单篇入库）
**槽位**: R2
**骨架**:
> Given that all our dependent variables were [continuous scale] and that the independent variables were [continuous] or [categorical], [estimator] was the primary statistical technique employed. The entire sample was dichotomized at the median of the [moderator] measure, with those units falling below the median classified as [context A] and those falling above it classified as [context B]. Thus, we ran separate sets of regressions for each subsample ([context A] and [context B]) and another set using the product-term approach to test interaction effects. Tables [X] and [Y] present regression results.
**与原骨架差异**: 区别于标准 R2 模型序列导航（Model 1→2 增量逻辑）——本变体是**调节检验设计导航**：一句由 DV/IV 测量层级正当化估计器选择，一句宣告分样本切分规则（median dichotomization 的 A/B 命名），一句预告"分样本回归 + product-term 复核"双通道设计，末句表格导航。适用于调节变量为类目型/可切分、假设以情境前缀形式写出（scope-conditioned）的设计。
**诚实边界**: 分样本切分规则必须在 Methods/本段可复现（本文用 median of environmental stability）；product-term 复核句只宣告"will test"，不得在本槽位预告结果方向。

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:r2_ols_estimation_strategy_split_sample -->


### 变体 72: R3 — 多指标假设裁决四拍（3 显著 + 1 方向分，carpenterwestphal2001 型）

**来源论文**: Carpenter & Westphal 2001 (AMJ)
**skeleton_id**: `r3_multi_indicator_hypothesis_adjudication`
**原始句锚点**: "For example, the coefficients for product-market, diversification, and internationalization relatedness were all positive and significant. ... although the coefficient for foreign market relatedness was not significant, it was positive, as hypothesized."
**验证状态**: EMERGING（单篇入库）
**槽位**: R3
**骨架**:
> Results of the [regression] testing Hypothesis [N] support the prediction that [IV family] will be positively associated with [DV] in [context] ([Table X], Model [Y]). For example, the coefficients for [indicator_1], [indicator_2], and [indicator_3] were all positive and significant; although the coefficient for [indicator_4] was not significant, it was positive, as hypothesized. [Converse sentence for the reverse-predicting rival: "Conversely, having more [IV variant B] was negatively associated with [DV]."] These results held after we controlled for [rival predictor], which is consistently unrelated to [DV] in [context].
**与原骨架差异**: 区别于 r3_ols_four_beat_standard（单系数四拍：方向→显著性→幅度→支持判断）——本变体是**假设级裁决**：一个假设由一组同构指标系数共同承载，裁决拍放在段首（support the prediction），指标拍以 "For example" 列举，不显著指标不触发 R6 降级而以"方向正确"从句并入支持证据，收口句用 "held after we controlled for [rival]" 内联排除替代解释。适用于 IV 为多维度指标族（relatedness/heterogeneity 类型变量族）、假设对指标族整体作预测的设计。
**诚实边界**: 方向分只适用于"不显著但方向与假设一致"的少数指标且多数指标已显著；不得把方向分当显著性证据（不得写 "largely significant"）；one-tailed 检验属 2001 年惯例，当代写作建议 two-tailed 并明示。
**反模式警示**: 本变体无幅度拍（未把 unstandardized 系数翻译为实质变化）——按 write-results R3 强制要求，填入时必须补幅度拍（"a [one-SD] increase in [predictor] is associated with [Y-unit] change"），不得照抄原文缺拍。

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:r3_multi_indicator_hypothesis_adjudication -->


<!--
pattern_id: switching_reg_cross_model_comparison_infrastructure
estimator_family: switching regression / endogenous switching（跨分样本模型系数比较）
slot: R3（比较基础设施 + 列子集导航）
source_papers: ["gulati2005-adaptation-vertical"]
confidence: EMERGING（单篇 full_text_verified，待第二篇交叉验证）
-->

### 变体 80：跨分样本/跨模型系数比较的推断基础设施声明——SUR 联合协方差 + 括号双轨显著标记（Cross-Model Comparison Infrastructure）

**适用场景**: 假设要求比较**分别估计的分样本/分组模型之间的系数**（make/buy/ally 分组回归、按类别分组的调节设计、或第二阶段逐组切换回归），而非单方程内的交互项检验。此时须先交底比较逻辑，再声明比较的基础设施（联合协方差矩阵），并给出括号双轨报告规则（表内普通稳健显著 + 括号跨模型联合协方差显著），随后逐假设导航到具体列子集。

**报告节奏**: [比较逻辑预告] → [分别估计声明] → [比较基础设施(SUR 联合协方差)] → [括号双轨规则] → [列子集导航]

**骨架**:
```
[比较逻辑预告] Hypotheses [N–M] require comparison of coefficients across these models, as we
are interested in testing the differences between the [marginal] effects of [X], [Z], and their
interaction across the [K categories].
[分别估计声明] The [model] was estimated separately in each subsample of transactions, i.e.,
for all transactions classified as '[category A],' '[category B],' and '[category C].'
[比较基础设施] In addition to robust standard errors (reported below each coefficient), in
order to facilitate intermodel comparison of coefficients, we calculated robust standard errors
from a combined variance–covariance matrix using the [SUR] estimation algorithm in [software].
[括号双轨规则] Significance marks and standard errors in parentheses are based on a common
robust covariance matrix across models for all [K] categories; these results and the resulting
significance levels are reported in brackets.
[列子集导航] To test Hypothesis [N], we compare the coefficients of [X] across the column '[a]'
models for [A], [B], and [C], which only includes the main effects for [X] and [Z].
```

**为什么有效**: "分组回归各自显著"无法回答组间差异问题——本文把跨模型比较的统计基础（SUR 联合协方差）当作一等公民声明，并用括号双轨制让单表同时承载"组内推断"与"组间推断"两套显著水平，读者无需翻附录即可分辨哪一轨支持跨组结论。比较逻辑预告句把 H3–H5 的检验方式与理论结构（边际效应差异）显式对齐。

**注意事项**: 现代规范应进一步给出组间 Wald 统计量而非仅括号显著标记（2005 世代惯例，正文未报统计量）；若未做正式组间检验，裁决句应保持 pattern-based 措辞。括号双轨制的报告约定（哪套标准误在外、哪套在括号）必须在表注一次说清。

**反模式**: 分组分别回归后直接按"系数大小肉眼排序"下结论（无联合协方差或 Wald 背书）；把组内显著性当成组间差异的证据；双轨制表注不完整导致读者无法解析括号含义。

**原文锚点**: "In addition to robust standard errors (reported below each coefficient), in order to facilitate intermodel comparison of coefficients, we calculated robust standard errors from a combined variance–covariance matrix using the seemingly unrelated estimation algorithm in STATA 8.2."

**范文来源**: Gulati, Lawrence & Puranam (2005), *Strategic Management Journal* — RESULTS Table 5 导航段（跨模式系数比较交底）。

<!-- wb:gulati2005-adaptation-vertical:switching_reg_cross_model_comparison_infrastructure -->


### 变体 82：假设判决驱动的系统内 Baron-Kenny 三步中介 + 联合模型校准（gulati_sytch2007 型；LEGACY）

**适用场景**: 中介假设（H_mech）与主效应假设（H_main）同属确认性检验的设计；中介 b 路径嵌在主估计系统（如联立方程/3SLS 的结果方程）内，a 路径由独立中介回归表报告。多中介并行时，协议步骤同时充当假设判决机器。

**报告节奏**: [协议声明+步骤1争议回应+保留理由] → [步骤1=H_main 判决复用] → [步骤2专用中介表：显著中介建立+null 中介直接拒证 H_mech] → [步骤3嵌套模型+拟合改善拍（χ²/R²）] → [Sobel mediation path 显著性拍] → [逐中介部分中介裁决+跨模型拟合比较] → [双中介联合模型→nearly full mediation 校准]

**骨架**:
```
To test hypotheses [H3]–[H5], we followed the rules for mediation testing suggested by
[Baron and Kenny (1986)]. The first step in testing for mediation requires us to
establish a significant relationship between the independent variable and the dependent
variable. While recent research on mediation testing ([citations]) suggests that this
step is not required, as it represents an unnecessarily strong restriction in testing
for mediation, we elected to incorporate it into our method because we predicted an
analytically proximate relationship between [predictor] and [outcome]. ... this
requirement was fulfilled with the support for hypothesis [H2].

The second step mandates that the significant relationship between the independent
variable and the mediator be established. Table [Y] reports the results of regressions
analyzing the relationship between [predictor] and the proposed mediators. Significant
relationships were established for [mediator_A] and [mediator_C], but no significant
relationships were found for [mediator_B] and [mediator_D], thus refuting hypothesis
[H4] and the part of hypothesis [H5] that focused on [mediator_D].

In the final step of testing for mediation, the dependent variable was regressed on the
independent variable and the mediator in models [3]–[5] in table [X]. [Mediator_A] has
a significant positive effect on [outcome] ..., which leads to a substantial
improvement of the overall fit of the model, as indicated by noticeable positive
changes in the values of the chi-squared and R-squared statistics. More important,
based on [Baron and Kenny's (1986)] more stringent specification of [Sobel's (1982)]
test for the significance of mediation, the partial mediating effect of [mediator_A] is
significant, as indicated by the mediation path coefficient in table [X]. ...

In model [5] in table [X], we regressed [outcome] on both mediators along with
[predictor]. All mediators are significant, while the regression coefficient for
[predictor] decreases in magnitude and remains significant, albeit at a borderline
level of significance, indicating nearly full mediation.
```

**为什么有效**: 三个协议步骤各有一句"该步骤在本文如何被满足"，中介检验从统计程序变成假设判决链条；null 中介不被隐藏而是直接转化为假设拒证（H4 全拒、H5 半拒）；步骤1争议显式回应后给出保留理由，预防"过时方法"质疑；联合模型校准句（系数下降但仍显著→nearly full mediation）给出比 partial/full 二分更细的结论颗粒度。

**与已有变体的分工**: 变体75（连续 DV legacy BK 三步句，EMERGING）与变体78（BK+Sobel 假设化部分中介跨 DV 重演，EMERGING）为本变体的同族前身——本变体是它们的**第二篇交叉验证源**，增量：①步骤1由 H_main 支持复用满足+显式回应 step-1 争议；②步骤2专用中介表使 null 中介直接裁决假设；③步骤3嵌套模型拟合改善拍（χ²/R² 变化）+跨模型比较（含中介模型 vs 拟合更优者）；④双中介联合模型的 nearly full mediation 校准。变体0（现代 BK+bootstrap+工具中介）仍是现代默认；本变体照语料诚实边界**强制标 LEGACY**——现代采用须补 bootstrap/PROCESS 间接效应区间。

**注意事项**: 确认性中介（假设在 theory 预告）与 post hoc 机制检验必须分开标注，本变体仅用于前者；reverse mediation（反向中介）检验属稳健性，另句报告；"nearly full mediation" 的前提是系数"仍显著但降级到边缘水平"——系数完全不显著才可写 full mediation；Sobel 显著性以表内 mediation path 系数行承载时，正文须指明行位置。

**反模式**: 把 BK 条件计数升级为现代间接效应证据（违反语料诚实边界）；null 中介仅报系数不落到假设裁决；多中介联合模型缺校准句使读者自行猜测中介化程度。

**验证状态**: EMERGING（单篇，待第二篇交叉验证；LEGACY——采用须补 bootstrap/PROCESS 间接效应区间或显式标注 legacy）

**原文锚定**: "All mediators are significant, while the regression coefficient for joint dependence decreases in magnitude and remains significant, albeit at a borderline level of significance, indicating nearly full mediation."

**范文来源**: Gulati & Sytch (2007), *Administrative Science Quarterly* 52(1) — Results 节中介三步（H3–H5）+ Table 8/9。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r8_in_system_baron_kenny_hypothesis_linked_mediation -->

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r8_in_system_baron_kenny_hypothesis_linked_mediation_gulati_sytch2007 -->

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **稳健性检验仅在 4.1 Post-hoc 枚举带过** | 正文未按 threat 组织稳健性叙事，仅列出分析名称 | 少量稳健性用变体 2 叙事型；大量稳健性用变体 1 Table 9 矩阵 |
| **曲线关系仅报线性+二次系数** | 倒 U 型关系未做 Lind-Mehlum 三步验证和转折点 CI | 使用变体 17 的完整协议 |
| **曲线调节只说交互显著** | 未解释二阶交互项符号、未用 flatten/steepen 描述曲线形状 | 使用变体 18 的图形语言 |
| **多项式/交互模型未报告 mean-centering 和 condition number** | 高阶项和交互项可能造成多重共线性但未诊断 | 使用变体 20 的三重诊断 |
| **显著性语言不一致** | 同一论文中 p=0.052 称 "significant" 而 p=0.071/0.075 称 "marginal" | p > 0.05 一律统一标 "marginally significant"（du_tsolmon2024 警示案例） |
| **Split-sample 系数对比无 Wald 检验** | 仅用 "larger vs smaller" 描述性断言跨子样本系数差异（0.190 vs 0.069），未检验系数相等性 | 跨子样本系数对比须配 Wald χ² / seemingly unrelated estimation 检验（du_tsolmon2024 警示案例） |
| **删除不显著控制变量以“挽救”焦点系数** | 完整模型仅 `p < .10`，随后删除当期不显著 controls 并把 `p < .05` 宣称为 stronger support | 控制变量由理论、设计或预先规则决定；完整规格保留为主结果，替代控制集只能作为透明敏感性分析，且不得升级原假设判定（Kashmiri–Nicol–Arora 2017 警示案例） |
| **仅用 Baron–Kenny 条件计数宣称 completely mediate** | 无间接效应区间/bootstrap，仅凭直接路径消失声称完全中介 | 补间接效应 CI，或显式标 legacy；优先变体 5/41 或现代中介标准（变体 62 警示） |

## 诚实边界

- **曲线关系效应量**：Cohen's d 的计算基准需在 Methods 或 Appendix 说明，不可直接套用线性公式。
- **转折点 CI**：转折点置信区间必须落在数据范围内，否则倒 U 型证据不足。
- **非中心复制**：mean-centering 后报告非中心化系数是可选策略，但需解释为何更便于解释；若中心与非中心结果不一致，需讨论。
- **Post-hoc 标签**：将 "robustness checks" 与 "additional insights" 并列时，应逐条标注哪些是确证性稳健性、哪些是探索性分析，避免审稿人质疑。
- **显著但实际效应小必须显式降调**：交互项或主效应统计显著但实际效应过小时，必须在正文显式降调（"does not appear to be particularly meaningful in practice"），不得仅以显著性宣布支持。（变体14/55）
- **null 主效应符号反转只作推测框架**：null 主效应若符号反转并读作"同一构念的另一极"，只作推测框架并推迟到 Discussion，不得声称支持。（变体15）
- **规格敏感性把 null 变显著必须透明披露并机制对冲**：规格敏感性把 null 变成显著时，必须透明披露并用系数通胀机制（如 Kalnins 2018）对冲，不得升级为假设支持。（Ridge et al. 2024 A9/A10 范本）
- **Legacy Kenny complete-mediation**：仅用条件计数宣称 completely mediate 时必须附间接效应区间或显式标 legacy；不得替代现代中介报告。（变体 62；Kashmiri 边界继续有效）
