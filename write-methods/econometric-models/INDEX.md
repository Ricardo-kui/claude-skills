---
corpus: write-methods
description: Methods 填空骨架变体库，按设计类型组织。由 distill-methods-exemplar 手动写入验证通过的变体。
organization: by_design_type
design_types_count: 24
created: 2026-05-18
updated: 2026-08-05
---

# Methods Econometric Models Corpus

## 组织逻辑

按模型设计类型组织。每个文件包含：
1. **主骨架引用** — 指向 `references/slot-M*.md` 中对应设计类型的变体（按需加载规则见 `write-methods/SKILL.md` → 槽位骨架加载）
2. **累积变体** — 由 `distill-methods-exemplar` Phase 4 自动写入的验证通过变体

另：`micro-templates/` 子目录为 18 类句法级微模板（槽位映射与使用协议见其 `INDEX.md`），由 `write-methods` 在表达润色时按需选读。

## 选择优先（变体速查表）

> 每个设计类型文件顶部现已有「变体速查表」（2026-08-08 推广）：按槽位（M1–M10）分组 + 六列表（变体 | 适用场景 | 区别 | 状态 | 来源），是类型内变体选择的唯一入口。
> **状态词表已统一（五档）**：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。旧词表映射：EMERGING→待第二篇交叉验证；VERIFIED / 框架级（双源）→通过（双篇/专家审计）；部分验证→待交叉；EXPERIMENTAL（slot 文件用语）→待第二篇交叉验证（其「保守替代」提示随槽位骨架保留）；LEGACY-DIAGNOSTIC 保留（工具诊断类）。
> 检索流程：SKILL 路由确定设计类型 → 打开类型文件读速查表 → 按槽位+状态定位候选 → 精读变体正文（骨架/诚实边界/跨 skill 对齐）。

## 设计类型索引

| 文件 | 设计类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [面板数据-OLS](面板数据-OLS.md) | 面板数据-OLS | 32 | 2026-08-05 |
| [自然实验-DiD](自然实验-DiD.md) | 自然实验-DiD | 13 | 2026-08-05 |
| [非线性模型](非线性模型.md) | 非线性模型 | 15 | 2026-08-05 |
| [生存分析](生存分析.md) | 生存分析 | 22 | 2026-08-01 |
| [SEM](SEM.md) | SEM | 4 | 2026-05-18 |
| [实验](实验.md) | 实验 | 6 | 2026-08-03 |
| [多研究](多研究.md) | 多研究 | 9 | 2026-08-02 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 6 | 2026-07-07 |
| [稀有结果](稀有结果.md) | 稀有结果 | 1 | 2026-08-05 |
| [实证对象构建](实证对象构建.md) | 实证对象构建 | 5 | 2026-07-30 |
| [事件历史+事件研究](事件历史+事件研究.md) | 事件历史+事件研究 | 11 | 2026-08-02 |
| [同时方程](同时方程.md) | 同时方程 | 4 | 2026-07-30 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 13 | 2026-08-05 |
| [动态面板-GMM](动态面板-GMM.md) | 动态面板-GMM | 4 | 2026-07-30 |
| [匹配DiD-广义DiD](匹配DiD-广义DiD.md) | 匹配DiD-广义DiD | 1 | 2026-08-05 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 4 | 2026-07-30 |
| [文本构念测量](文本构念测量.md) | 文本构念测量 | 13 | 2026-08-05 |
| [PSM匹配面板](PSM匹配面板.md) | PSM匹配面板 | 3 | 2026-06-16 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [多行为者设计](多行为者设计.md) | 多行为者设计 | 1 | 2026-07-08 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 1 | 2026-08-05 |
| [两阶段模型](两阶段模型.md) | 两阶段模型 | 7 | 2026-08-05 |
| [VARX-PVAR](VARX-PVAR.md) | VARX-PVAR | 8 | 2026-07-15 |
| [结构需求-state-space](结构需求-state-space.md) | 结构需求-state-space | 6 | 2026-08-05 |

## 写入规则

1. 仅 `distill-methods-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

> ✅ **2026-08-05 更新（Zorn–Shropshire–Martin–Combs–Ketchen 2017 SMJ）**: S&P 1500 lone-insider boards + 2SLS。新增：
>   - **IV-2SLS** 变体12–13：industry leave-out 均值 IV（CEO 推动采纳内生性）+ 连续 DV 用 2SLS/FE、稀有二元放弃 FE 改聚类 Logit（IV-Probit 稳健性预告）
>   - **面板数据-OLS** 变体32：结构二元「kind rather than degree」相对 majority-independence 的构念辩护
>   - **稀有结果** 变体1（**首填**）：低事件率 → FE 丢样本 → 年份虚拟+单元聚类 Logit
>   均为单篇 EMERGING；未改 SKILL.md 核心路由。配套 Results：`../write-results/econometric-models/IV-2SLS.md` 变体8–10。

> ✅ **2026-08-05 更新（Castellaneta–Conti–Kacperczyk 2017 SMJ 蒸馏）**: 交错 UTSA + PE buyout 持有窗截面。新增：
>   - **自然实验-DiD** 变体8–13：dual-sale setting、持有窗处理+staggered 示例、IRR/ΔV≈DiD 一阶差分等价、entry/exit 年 FE 栈、政治经济外生性电池、±k 年日历安慰剂
>   - **匹配DiD-广义DiD** 变体1（**首填**）：CEM 匹配 ex-ante 价值+风险代理作为准实验稳健性
>   均为单篇 EMERGING；不将 IRR≈DiD 提升为现代面板 staggered-DiD 默认路由；未改 SKILL.md 核心。

> ✅ **2026-08-05 gap audit（Kim & Lee 2026 SMJ）**: Methods **无需新增**（多研究变体6 / 非线性变体10 / 文本构念变体12 已覆盖）；配套 Results 缺口补写见 `../write-results/econometric-models/`（OLS-FE 变体45–46）。

> ✅ **2026-08-05 更新（Liu & Shankar 2015 MS 蒸馏）**: **首次填充**设计类型 `结构需求-state-space`（BLP + Kalman + GMM，product-harm crises 需求侧动态）变体1–6；扩展 `面板数据-OLS` 变体29–31（severity 理论分类、媒体 relevancy 阈值、异频月聚合）、`两阶段模型` 变体7（价格 BLP-IV + 广告双端 CF + 跨品类媒体 IV）。均为单篇 EMERGING；与 survival/time-to-recall 召回家族分工，不修改核心路由。

> ✅ **2026-08-05 更新（Hoffmann et al. 2024 JM 重蒸馏）**: 修正既有 hoffmann2024 slot 变体中的两处事实错误（误写 firm FE / incidental parameters；原文为 year+industry FE + always-zero DV collinearity）。新增：
>   - **自然实验-DiD** 变体4–7：Marketing quasi-experiment 识别栈、无 firm FE 辩护、POST 共线性说明、裁量权/行业扩展漏斗
>   - **非线性模型** 变体15：Schmitz reduced-form 三阶交互 + staggered collinearity
>   - **文本构念测量** 变体13：validated dictionary 相对净得分 + 大规模语料辩护
>   - **推断二元结果** 变体1（首填）：裁量权边界子样本
>   - slot-M1/M2/M7/M8 EXPERIMENTAL 变体同步升级（paper_id: `hoffmann_cheong_phan_zurbruegg2024`）
>   均为单篇 EMERGING；未使用 Sun–Abraham 估计器，不提升为核心路由规则。

> ✅ **2026-08-04 更新（Lee–Park 2024）**: 非线性模型新增两条写作型变体：有界结果的“估计尺度—正式形状标准—可解释尺度”契约，以及“先声明几何对象、再直接比较条件转折点”的位置型曲线调节。Lee & Park 经用户专家审计为典型 U／倒 U 写作范文，两条变体均登记为 **VERIFIED**。同步加入术语与边界：quadratic vertex 不称 inflection point；二次项和交互项的符号不能替代端点斜率、内部转折点及直接差异检验。主 skill 路由不变。

> ✅ **2026-08-03 更新（Schumacher–Keck–Tang 2020）**: 面板数据-OLS 新增“任期早期构念形成窗与后续结果观察窗完全分离 + 媒体/期权方法异质双代理”变体；`executive-confidence-operationalization` 同步补入 M4 生成骨架与两条诚实边界：窗口分离不等于外生性，双代理同向不等于构念纯度。该变体为单篇 EMERGING reference，不提升为默认核心规则。

> ✅ **2026-08-03 更新（Kashmiri–Nicol–Arora 2017）**: `executive-confidence-operationalization` 增加“视觉显著性 + 传播显著性 + 相对现金/非现金薪酬”的 CEO narcissism 复合代理，并加入 succession-year exclusion、同一 CEO 跨期稳定性与同一企业继任 CEO 对照；`model-selection-comparison` 增加多结果 `measurement property → estimator → interpretation scale` 路由；M3 新增 product-harm crisis 与 recall timing/strategy/severity 的强制边界声明。均为单篇 EMERGING reference，不改变核心槽位。

> ✅ **2026-08-03 更新（Vidal–Mitchell 2015；Moon–Tuli–Mukherjee 2023）**: 非线性模型新增“随机效应面板 Poisson：分布诊断—estimand 对齐”变体；IV-2SLS 新增“同行 IV 距离梯度组合”变体；两阶段模型新增“多内生性威胁—修正方法配对账本”变体。均为 reference-level / EMERGING，不替代既有 Tobit、地理 IV 或单一控制函数变体。

> ✅ **2026-08-02 更新（Lee–Wu–Bednar, Organization Science）**: 首次填充自然实验-DiD：跨层级冲击映射与样本漏斗、有符号计数衍生 DV 的估计器选择、错位 DiD 三层诊断栈。第三项标记为 **LEGACY-DIAGNOSTIC**：Bacon 分解只诊断传统 TWFE，不替代 Callaway–Sant'Anna / Sun–Abraham 与平行趋势敏感性分析。

> ✅ **2026-05-20 更新**: 五篇产品召回论文 (Darby2026 JOM / Darby2025 JSCM / Eilert2017 JM / Darby2023 MSOM / Wowak2025 MS) 交叉验证完成。
>
> **设计家族**: 4篇生存分析(AFT+Weibull) + 1篇IV-2SLS(Lewbel heteroskedastic identified instrument)
> **核心骨架 (5/5 必现)**: Time-to-Recall操作化 (days from defect awareness to recall initiation)、firm+year FE
> **高频可选模块 (3-4/5)**: 控制变量分层because、复发事件处理、样本交集漏斗
> **双篇高价值 (2/5)**: 事件研究法、CEM匹配、CPH稳健性对比
> **单篇高价值 (1/5)**: 分布选择BIC比较、右删失处理、IV三层because论证链、mixed-effects机制分解、替代变量机制矩阵、CAR非参数检验双报告、信息泄露检验、Lewbel三步法、IV诊断链完整报告、政治意识形态操作化
>
> ✅ **2026-07-06 更新**: 蒸馏 Cutolo & Ferriani 2024 (JM) "How Narratives Can Help Atypical Actors Increase Market Appeal" 新增 4 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 文本构念测量 变体5：**复合文本指标构建**（多子维度 → 分别测量 → 平均合成）
>   - 文本构念测量 变体6：**类别相对文本常规性操作化**（LDA topic → category-average regression slope）
>   - 文本构念测量 变体7：**文本测量人工验证**（随机样本检查）
>   - 非线性模型 变体1：**计数模型选择**（负二项回归 + 过度分散诊断）
>   - 配套 write-results：count-model moderation translation、text-measure robustness bundle、composite text component disaggregation
>
> ✅ **2026-07-06 更新（续）**: 蒸馏 Falchetti, Cattani & Ferriani (SMJ) "Start with 'Why,' but only if you have to" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 多研究 变体1：**多研究实验项目总览**（研究梯度图：audience × stimulus × DV 变异矩阵）
>   - 多研究 变体2：**操纵检验 Pilot Study 段落**（嵌入主 Methods 的操纵验证）
>   - 实验 变体1：**单实验 Methods 标准段落**（被试→材料→操纵→测量）
>   - 配套 write-results：experimental ANOVA four-beat、Hayes PROCESS mediation reporting、cross-study synthesis
>
> ✅ **2026-07-07 更新**: 蒸馏 Lashley & Pollock 2020 (ASQ) "Waiting to Inhale" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁新设计类型「定性过程研究」：
>   - 定性过程研究 变体1：**现象与方法正当化**（limited understanding → inductive qualitative approach）
>   - 定性过程研究 变体2：**极端情境选择理由**（extreme situation + theoretical tensions visible + background stability）
>   - 定性过程研究 变体3：**多源数据角色分配**（observations / interviews / archives 各捕获什么）
>   - 定性过程研究 变体4：**过程阶段划分与编码进阶**（chronology → bracketing → open coding → axial coding → aggregate dimensions）
>   - 定性过程研究 变体5：**可信性机制组合**（triangulation + prolonged engagement + peer debriefing + secondary coding）
>   - 配套 write-results：process-model overview、front-stage/backstage contrast、side-stage negotiation、audience-specific success assessment
>
> **已填充变体**: 49个 (分布于 13个设计类型文件)
> **新设计类型解锁**: 实验、多研究实验、定性过程研究
>
> ✅ **2026-06-16 更新**: 蒸馏 Qiao, Hiatt & Sine (2026, SMJ) "dual imprinting" 新增 3 个高价值变体（均单篇、不可跨论文复现声明已标注）：
>   - 生存分析 变体6：**因 Cox 比例风险失败（Schoenfeld）→ piecewise exponential + 理论时段分割**（估计器由诊断驱动 + 分段由理论驱动）
>   - IV-2SLS 变体4：**外部自然事件（自然灾害）作工具变量 + 三因排除限制论证**（外生性 / 制度缝隙渠道 / 结果文献反推无直接渠道）
>   - PSM匹配面板 变体3：**Entropy Balancing (EBM)** — 重加权、保留全部观测，适用于处理组稀少/需保全样本的研究
>   - 配套 write-results：IV-2SLS 变体4（control-function 残差作非线性 DWH + 有限样本偏误诚实提示）、SEM-moderated-mediation（reverse-code + Wald 检验对立通道持续性差异）
>   - 配套 write-theory：mechanism_chain.md 新增"双重印记对立通道 + 效果持续性差异 + 底物匹配调节"骨架；write-introduction：theory-lens/05-maxim-contrast 变体B（单句历史名言作 foil）
>
> ✅ **2026-07-07 更新**: 蒸馏 Mayo, Ball & Mills (2022, POM) "CEO Tenure and Recall Risk Management" 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁复发事件风险模型子类型：
>   - 生存分析 变体7：**复发事件指数风险模型 + 连续递增时间 + 备选分布稳健性**
>   - 生存分析 变体8：**三分位离散化 IV（等样本量理由 + 同模型双向检验）**
>   - 生存分析 变体9：**Goldman-Huang 三步 CEO 被迫离职分类**（协议逐字引用+频次报告）
>   - 生存分析 变体10：**SEC 10-K 披露作为事件裁量权测量**（GAAP 重大性杠杆）
>   - 生存分析 变体11：**表格式控制变量辩护（"Potential Factor of Influence"列）**
>   - 生存分析 变体12：**CEM 匹配程序（双向处理、作为稳健性非主识别）**
>   - 配套 write-results：风险模型三拍+exp(β)−1百分比、交互效应简洁报告、分样本Wald χ²+null确证叙事、CEM双向ATE、替代机制交互检验+诚实收尾
>
> ✅ **2026-07-07 更新（续）**: 蒸馏 Haunschild, Polidoro & Chandler (2015, ORSC) 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 非线性模型 变体2：**负二项回归选择 — 竞争焦点 DV 的模型论证**（ZINB 排除 + e^β−1 预告）
>   - 非线性模型 变体3：**竞争焦点 DV 互控 — 排除伪 trade-off**（双向互控 + 无互控稳健性）
>   - 非线性模型 变体4：**替代测量构造效度三角 — 双层测量正当性**（广义vs特定响应区分）
>   - 配套 write-results：计数模型 变体7-9（主效应四拍+e^β−1、无显式交互项调节效应、跨测量复制）
>
> ✅ **2026-07-07 更新（续2）**: 蒸馏 Mannor, Wowak, Bartkus & Gomez-Mejia (2016, SMJ) 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 文本构念测量 变体8：**LIWC 双成分净得分 + face validity 引语锚定**
>   - 面板数据-OLS 变体6：**多通道精英/关键行为人招募**
>   - 面板数据-OLS 变体7：**嵌套横截面数据的聚类稳健标准误**
>   - 面板数据-OLS 变体8：**回顾性偏差三角检验**
>   - 配套 write-results：OLS-FE 变体8-10（主效应不显著但调节显著、单侧边际效应、ΔR²经济显著性）
>
> ✅ **2026-07-07 更新（续3）**: 蒸馏 Pfarrer, Pollock & Rindova (2010, AMJ) 新增 3 个高价值变体：
>   - 事件历史+事件研究 变体5：**事件窗口+市场模型+标准软件声明**
>   - 非线性模型 变体5：**RE 面板 Logit + odds-ratio 报告惯例**
>   - 非线性模型 变体6：**理想型二分化 + 复合媒体构念测量**
>   - 配套 write-results：Logit-Probit-Ordered-Probit 变体1-3（首次填充该结果类型）
>
> ✅ **2026-07-07 更新（续4）**: 蒸馏 Desai (2011, AMJ) 新增 3 个高价值变体：
>   - 非线性模型 变体7：**条件 FE 负二项 + 全零面板审计**
>   - 面板数据-OLS 变体9：**制度断点样本辩护**
>   - 配套 write-results：计数模型 变体10-11（负主效应+正交互条件反转、跨模型共线性说明）
>
> ✅ **2026-07-07 更新（续5）**: 蒸馏 Bamberger, Homburg & Wielgos (2021, JM) 新增 3 个高价值变体：
>   - 多研究 变体3：**混合方法多研究设计的情境+数据源衔接**
>   - 面板数据-OLS 变体10：**Hausman FE vs RE 检验**
>   - 配套 write-results：多研究 变体2（跨研究镜像首句）、SEM-moderated-mediation 变体2（不一致中介→抑制变量）、OLS-FE 变体11（边际显著 90% CI）
>
> > ✅ **2026-07-07 更新（续6）**: 蒸馏 Li, Chiu, Kong, Cropanzano & Ho (2026, JOM) "A Sensemaking Model of Investor Reactions to CEO Achievement Expression" 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 面板数据-OLS 变体13：**RE 选择三重辩护 — 理论+Hausman+ICC**
>   - 面板数据-OLS 变体14：**全谱系控制变量 — 高because密度+RavenPack事件控制+CEO人格特质**
>   - 文本构念测量 变体10：**LIWC 默认字典效度链 — 效度引用+补充实验验证+区段聚焦理由**
>   - 实验 变体2：**开放式文本 RA 评分操纵检验 — 替代 traditional self-report**
>   - 多研究 变体4：**三研究递进设计论证 — 内部效度→概念复制→生态效度**
>   - 事件历史+事件研究 变体7：**三DV互补市场反应测量体系 — CAR+ATV+投资者文本情绪**
>   - 配套 write-results：实验变体3（被调节的中介五拍）、OLS-FE 变体13-15（交互百分比经济显著性/低基础率边际直方图/五威胁标签化稳健性）、多研究变体3（三研究递进结果叙事）、新建事件研究法文件

> ✅ **2026-07-07 更新（续7）**: 蒸馏 Ahmadi, Khanagha, Berchicci & Jansen (2017, JMS) "Are Managers Motivated to Explore in the Face of a New Technological Change?" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 实验 变体3：**视频操纵 + 两阶段数据收集** — 替代纯文本vignette，T1特质/T2实验时间分离
>   - 实验 变体4：**双极量表选择辩护** — continuous vs orthogonal 测量论证
>   - 实验 变体5：**专业样本同质性辩护** — 单组织内同质管理者群体
>   - 配套 write-results：OLS-FE 变体16（7模型层次回归表导航）、三向交互 变体1（三向交互条件分解，首次填充）、多研究 变体4（跨研究差异嵌入Results讨论）

> ✅ **2026-07-08 更新**: 蒸馏 Cui, Yang & Vertinsky (SMJ) "Attacking your partners: Strategic alliances and competition between partners in product markets" 新增 10 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁/填充 5 个设计类型：
>   - **同伴效应-网络效应**（首次填充）变体1-3：**degree centrality 差值**、**common ties 计数**、**ego network density via two-mode incidence transformation**
>   - **多行为者设计**（首次填充）变体1：**multiparty alliance 拆 dyad + 混淆控制**
>   - **面板数据-OLS** 变体15-18：**双重现象设置辩护**、**多源 alliance 交叉验证**、**多维行为 factor score**、**dyad FE + dyad 聚类 SE + 具体混淆源举例**
>   - **文本构念测量** 变体11：**手工 content analysis 编码规则 + 边界案例 + 焦点 actor 视角**
>   - **实证对象构建** 变体2：**FDA 监管产品竞争组构建**
>   - 新增反模式：调节效应论文 Methods 未报告交互项构造、手工内容分析未报告编码者间一致性
>
> ✅ **2026-07-08 更新**: 蒸馏 Chung, Low & Rust (2022, JAMS) "Executive confidence and myopic marketing management" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - **面板数据-OLS** 变体19-21：**高管信心期权 moneyness 操作化**、**model-free evidence 预览**、**三向交互模型设定（mean-centering + 完整 lower-order terms + 聚类 SE）**
>   - **两阶段模型** 变体3：**Heckman 选择模型 + 同行 CMO prevalence 排他性限制（跨 segments 加权）**
>   - **IV-2SLS** 变体5：**DWH 检验 + Gaussian copula 内生性叙事**
>   - 配套微模板：executive-confidence-operationalization、interquartile-economic-significance、heckman-peer-prevalence-exclusion、alternative-dv-falsification
>
> ✅ **2026-07-22 更新**: 蒸馏 Ilicic & Brennan (2026, JM) "Political Ideology Shapes Consumer Responses to Addictive Products" 新增 2 个高价值变体（均单篇、待第二篇交叉验证声明已标注）——首次填充 consumer psychology 机制证明传统：
>   - 实验 变体6：**测量过程+操纵过程双设计 + rival accounts battery** — Spencer, Zanna & Fong (2005) 双过程收敛机制设计；一次研究测量 9+ 竞争中介并逐一排除 + 随机化中介呈现顺序（区别于 slot-R8 的 1-2 个替代中介结果报告）
>   - 多研究 变体5：**Empirical Plan 因果阶段化预告段** — foundation→effect→process→intervention 理论因果阶梯（区别于变体4 的方法论效度阶梯）；含 foundation pilot（现象建立型）+ "Having established... we next investigated whether..." 因果阶段转折句
>   - 配套 write-results：多研究 变体5（逐研究 Discussion 接力立项）、SEM-moderated-mediation（reverse-order mediation 仅作竞争排序敏感性检查；不能确认序列中介的时间或因果顺序）
>   - 配套 write-theory：hypothesis_forms（序列中介叙事打包式）、hypothesis_derivation_patterns（counterintuitive direction-reversal via mechanism substitution）

> ✅ **2026-07-22 更新**: 蒸馏 Kim & Lee (2026, SMJ) "Putting a Price on Mission" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）——empirical strategy / strategic human capital 风格（首篇多阶段决策管道 + WTP）：
>   - 多研究 变体6：**同一 IV 跨决策阶段管道** — 各阶段不同分析单元 + 条件性样本递减（attraction/selection/attrition，Schneider ASA）；区别变体1-5 的 cross-study 独立样本梯度
>   - 非线性模型 变体10：**revealed-preference WTP 三估计器系数比**（LPM/conditional logit/mixed logit，-beta_X/beta_price）；corpus 零命中 WTP/mixed logit；顺手修复 variants_count 重复键 typo
>   - 文本构念测量 变体12：**手工二元编码 + 多源聚合 + embedded/peripheral 构念边界**（区别变体11 的边界案例披露，本变体理论上限定构念范围到 core identity）
>   - 配套 write-results：OLS-FE 变体27（多阶段管道衰减 profile + 跨阶段对比句）、slot-R5（WTP 经济显著性双 benchmark）、slot-R6（Slough post-treatment selection 诚实边界）

> **已填充变体**: 120个 (分布于 14个设计类型文件；本轮 Bendig et al. 2024 +1：面板数据-OLS M7 +1)
> **新设计类型解锁**: 同伴效应-网络效应、多行为者设计

> ✅ **2026-08-04 更新（Bendig, Hensellek & Schulte 2024 ETP 蒸馏）**: 面板数据-OLS 变体28新增 **binary-panel GEE + all-zero panel retention + formal U-test chain**。该变体与既有 GEE 变体22构成“同估计器、不同选择理由”的对照：变体22服务于时不变 IV；变体28服务于保留始终无事件但焦点活动有变异的企业，并预先要求二次项、两端斜率、拐点与 Fieller 区间共同支持曲线。
>
> ✅ **2026-07-23 更新（sync from local backup）**: 从 pre-sync 备份补回两批本地蒸馏成果：
>   - **VARX-PVAR 设计类型接入**（Borah & Tellis 2016, JMR）：8 个 Methods 变体（行业情境 4-reason 辩护、品牌选择 + quasi-experiment、第三方 NLP 数据 + 人工匹配、算法准确率双重验证、VARX 框架 3-reason 辩护、Granger causality 外生性论证、VARX 方程规格、VARX 估计细节）。配套 `../write-results/econometric-models/VARX-PVAR.md`（7 个 Results 变体）。
>   - **Pupovac, Astvansh, Carrillat & Legoux (2026, POM) "Product Recall Contagion in the Supply Chain" 蒸馏**：补回 7 个 Methods 变体——事件历史+事件研究 变体 8/9/10、两阶段模型 变体 4/5、面板数据-OLS 变体 23/24；含 2 个新反模式（事件-企业多源匹配无每步 N 审计、控制变量全部外包至附录）。
>   - 注：面板数据-OLS 变体编号因远程 86f478d 已占用 22（GEE，Abdurakhmonov et al. 2026 JOM），本地原 22/23 续编为 23/24。
>
> ✅ **2026-07-25 更新（du_tsolmon2024 ORSC 蒸馏）**: 基于 Du & Tsolmon (2024, *Organization Science*) "Post-M&A Retention of Top Managers: The Role of Structural Knowledge"：
>   - **实证对象构建** 变体3：**连续相似度指数构建**（base unit 计数比率公式 1−|A−B|/(A+B) + 0.1 平滑零值 + 0-1 归一化 + identical/moderate/extreme 三数值示例 + binary 替代版本）
>   - **面板数据-OLS** 变体25：**DV 文献基准锚定**（retention rate 54.8% vs Hambrick & Cannella 55% / Krug & Hegarty 59.4%——均值与前人文献对比建立跨样本可比性）
>   - **面板数据-OLS** 变体16 EXTEND：**三层异质数据库漏斗 + 附录审计**（交易库→人员库→结构库 576K→15,773→2,941 + 附录 match rate + 初始vs最终样本变量对比）
>   - 可改进警示（反哺反模式）：0.1 平滑常数无 because/敏感性检验；相似度公式对称性未讨论
>   - 配套 Results 新增 6 变体见 `../write-results/econometric-models/OLS-FE.md` 变体 29-34

> ✅ **2026-07-30 更新（pollock2015 蒸馏）**: 基于 Pollock, Lee, Jin & Lashley (2015, *ASQ*) "(Un)Tangled"——新创 VC 企业 status↔reputation 共演，动态同时方程面板 + AB difference GMM。**首次填充 2 个设计类型** + 扩展 2 个，共 +8 变体（均单篇、待第二篇交叉验证）：
>   - **动态面板-GMM**（首次填充）变体1–4：**AB difference GMM 三源内生性统一处理**（LDV/同时性/异质性逐一列举→AB 作统一解）、**difference vs system GMM 选择**（young firms 远未稳态→放弃效率选一致性）、**工具变量滞后结构 per-sample 经验精调**（外生性类别定起始阶→Hansen J/diff-Sargan/AR(2) 三诊断逐变量精调，分样本各自精调）、**发展性调节无理论断点→多阈值分样本检验**（跨多个 age 阈值展示效应梯度）
>   - **同时方程**（首次填充）变体1–2：**动态同时双方程规格**（path dependence + simultaneity + FE 三特征显式映射到方程）、**堆叠非嵌套 Wald χ² 检验**（Weesie 1999 stack + vce(cluster) 恢复跨方程协方差，解决非嵌套系数比较难题——H1a/H1b 不对称方向检验的关键创新）
>   - **同伴效应-网络效应** 变体4：**Bonacich beta centrality 作 status 全局网络中心性测量**（区别 degree centrality 的局部结构；全数据库计算 + 移动窗口平滑 + 标准化跨构念比较）
>   - **实证对象构建** 变体4：**multi-item formative objective index + 跨年 rescaling 100 分制**（reputation 客观指标测量；形成性指标 + 排除理论需另用变量 + 年内排序保持/年际市场方差消除 + 标准化跨构念比较）
>   - 配套 write-results：见 OLS-FE.md（路径依赖 ρ 解释、分样本系数比较叙事、零结果 Monte Carlo 功效分析、partial support 叙事）
>   - 配套 write-theory：developmental reversal of reciprocal-causation asymmetry (H1a/H1b) + differential persistence / lagged-DV moderation (H2) 见 hypothesis_derivation_patterns.md

> ✅ **2026-07-30 更新（malshe2015 蒸馏）**: 基于 Malshe & Agarwal (2015, *JM*) "From Finance to Marketing"——5-方程 SUR/3SLS 系统（leverage↔advertising/R&D↔customer satisfaction↔firm value）。共 +3 变体（均单篇、待第二篇交叉验证）：
>   - **同时方程** 变体3：**辅助反向因果方程**（system 内增设 policy-variable 作 DV、下游变量滞后项作预测变量的方程，吸收"下游需求→政策变量"reverse-causal channel；区别变体1 的当期同时性）
>   - **同时方程** 变体4：**DWH 检验裁决"是否需要 IV"**（SUR 有效 vs 3SLS 一致；DWH 不显著→内生性不是问题→选 SUR）+ Hansen-Sargan 工具有效性——与"用 IV 处理内生性"常规叙事反向；与 `write-results/OLS-FE` 变体39（替代估计器失败佐证主估计器）互补
>   - **面板数据-OLS** 变体26：**跨库手工匹配（无共同标识符）+ 多源漏斗**（ACSI↔Compustat 无公用 firm ID → manually matched + 五库合并 + 限定上市 + 排除金融行业漏斗）
>   - 配套 write-results：OLS-FE 变体40-42（floodlight 符号反转交互双转折点、同时方程三条件中介+非对称支持、反直觉反向延迟到 Discussion）

> ✅ **2026-07-30 更新（zhou2017 蒸馏）**: 基于 Zhou, Gao & Zhao (2017, *ASQ*) "State Ownership and Firm Innovation in China"——双研究（new product ratio Tobit + patent Poisson）、institutional vs efficiency logics 整合。共 +3 Methods 变体（均单篇、待第二篇交叉验证）：
>   - **IV-2SLS** 变体10：**地理外生性工具变量（Frankel-Romer 型）**——用省会到大港口（香港/上海）的 Great Circle 物理距离作 institutional development 的 IV；区别自然灾害 IV（变体4）、Bartik（变体7）；配套第一阶段 F=144.12
>   - **多研究** 变体7：**同一理论模型跨 facet-DV 双研究复制**——Study 1 new product ratio（commercial, Tobit）+ Study 2 patent（fundamental, Poisson）；区别 cross-study 独立样本梯度（变体1-6）
>   - **非线性模型** 变体11：**Tobit corner-solution**——非负、零聚集 DV（R&D intensity、new product ratio）；区别负二项（count, 变体1）、面板 Logit（binary, 变体5）
>   - 配套 Intro：`03-non-coherence` 变体A 增"双层 non-coherence（理论对立+实证 mixed 三方向）+ facet-decomposition resolution"；Theory：`hypothesis_derivation_patterns` dual-logic 增"moderator-as-remedy（H3/H4：竞争/start-up 作 agency 低效的解药）"；Results：多研究 变体6（双研究核心收敛+样本解释的发散）、三向交互 变体3（线收敛=差距消除器）

> ✅ **2026-07-30 更新（pontikes2012 蒸馏）**: 基于 Pontikes (2012, *ASQ*) "Two Sides of the Same Coin"——software 行业 label ambiguity 跨受众评估。共 +1 Methods 变体（单篇、待第二篇交叉验证）：
>   - **实证对象构建** 变体5：**label-ambiguity 从共属重叠构建（fuzziness + leniency）**——fuzz = 1 − contrast；leniency = fuzz × ln(不同其他标签数)，区分"重叠到同一标签（仍 constraining）"vs"重叠到多标签（不 constraining）"；fuzzy-set grade of membership（部分归属 μ∈[0,1]）+ 加权聚合到 actor 层。构念是**标签属性**从成员共属网络结构推导，区别 Jaccard/计数比率/形成性指数。
>   - 配套 Intro：`tensions/04-reality-contradicts-consensus` 变体G（共识惩罚 vs 行为持续 + 修辞问 pivot）；Theory：audience-role dichotomy 增"two-stage complementary process reconciliation"（temporal staging 化解 VC/consumer 相反偏好的 irony）；Results：跨受众构念对比 变体1（首次填充——同一构念跨两类受众镜像相反效应 + 受众内 corporate-VC 反转）
>   - 注：发现 `write-theory/.../hypothesis_derivation_patterns.md` 中 audience-role dichotomy 模式**重复两次**（pre-existing duplication）——本次 two-stage 扩展通过 replace_all 同步写入两份，保持一致；建议日后 dedup。

> ✅ **2026-08-01 更新（darby2025 蒸馏）**: 基于 Darby, Wowak, Ketchen & Connelly (2025, *JSCM*) "An Agency Theory Perspective on Activist Investors and Supply Chain Failures"——recurrent-event AFT (Weibull) + frailty + PSM + CPH/marginal risk set 稳健性的生存分析。该论文（darby2025_activist_investors）已在 source_papers 中，本次蒸馏补齐**已登记来源但尚未提取为变体的方法学写法**（7 个新变体，均单篇、待第二篇交叉验证）：
>   - **生存分析** 变体16：**AFT 显式方程 + 双向固定效应嵌入**（M7）——变体1 是纯叙述引入，本变体补显式广义估计方程 Log(t_ijt)=β₀+βX+ΣFirm+ΣYear+u，使 FE 识别逻辑在数学层可见
>   - **生存分析** 变体17：**构念构建三步法 + fuzzy matching 多数据库链接**（M4）——13D/13D/A→13f 跨库实体链接，fuzzy score<0.95 手工核对 + conservative exclusion；区别变体14（止于 intersection）和变体8/10（单源构念）
>   - **生存分析** 变体18：**分样本调节设计（split-sample 替代交互项）**（M5）——分类调节变量（FDA Class I/II vs III）拆样本而非加交互项，理论理由=离散类别不可加性改变机制；与变体15（同模型交互）和变体8（同模型哑变量）形成对照族
>   - **生存分析** 变体19：**Threat-based 稳健性四威胁框架（生存分析专属）**（M8）——omitted（progressive controls+frailty）/ reverse（panelized FE+lagged IV）/ measurement（PSM）/ alternative estimators（CPH+marginal risk set）四威胁分节；语料库首个按威胁组织的完整稳健性架构
>   - **生存分析** 变体20：**Frailty 双层稳健性（recall-level + shared firm-level）**（M8）——Gamma frailty 两层独立报告，回应 event-level 与 firm-level 两种未观测异质性
>   - **生存分析** 变体21：**Marginal Risk Set 模型（Wei, Lin & Weissfeld 1989）**（M8）——作为复发事件处理的稳健性替代（stratification by event order），区别变体4/7（主模型复发事件处理）
>   - **生存分析** 变体22：**分析设计服务于理论构念——排除处理组以捕获"威胁而非实现"**（M7/M8）——语料库首个"样本定义=理论构念识别条件"的元层面骨架；适用于 spillover/contagion/anticipatory/deterrence 效应研究
>   - 配套 write-results：生存分析 变体15-19（"every day counts"经济显著性辩护、dummy-coding 方向翻译、分样本显著vs不显著对照、threat-based 四威胁报告、PSM ATE 天数翻译）；配套 write-theory：新增 `sentences/leitmotif-section-opener.md`（段首主导动机串联句）
