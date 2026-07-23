---
corpus: write-methods
description: Methods 填空骨架变体库，按设计类型组织。由 distill-methods-exemplar 手动写入验证通过的变体。
organization: by_design_type
design_types_count: 23
created: 2026-05-18
updated: 2026-07-22
---

# Methods Econometric Models Corpus

## 组织逻辑

按模型设计类型组织。每个文件包含：
1. **主骨架引用** — 指向 `references/slot-M*.md` 中对应设计类型的变体（按需加载规则见 `write-methods/SKILL.md` → 槽位骨架加载）
2. **累积变体** — 由 `distill-methods-exemplar` Phase 4 自动写入的验证通过变体

另：`micro-templates/` 子目录为 18 类句法级微模板（槽位映射与使用协议见其 `INDEX.md`），由 `write-methods` 在表达润色时按需选读。

## 设计类型索引

| 文件 | 设计类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [面板数据-OLS](面板数据-OLS.md) | 面板数据-OLS | 24 | 2026-07-23 |
| [自然实验-DiD](自然实验-DiD.md) | 自然实验-DiD | 0 | 2026-05-18 |
| [非线性模型](非线性模型.md) | 非线性模型 | 10 | 2026-07-22 |
| [生存分析](生存分析.md) | 生存分析 | 15 | 2026-07-07 |
| [SEM](SEM.md) | SEM | 4 | 2026-05-18 |
| [实验](实验.md) | 实验 | 6 | 2026-07-22 |
| [多研究](多研究.md) | 多研究 | 6 | 2026-07-22 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 6 | 2026-07-07 |
| [稀有结果](稀有结果.md) | 稀有结果 | 0 | 2026-05-18 |
| [实证对象构建](实证对象构建.md) | 实证对象构建 | 2 | 2026-07-08 |
| [事件历史+事件研究](事件历史+事件研究.md) | 事件历史+事件研究 | 10 | 2026-07-23 |
| [同时方程](同时方程.md) | 同时方程 | 0 | 2026-05-18 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 7 | 2026-07-22 |
| [动态面板-GMM](动态面板-GMM.md) | 动态面板-GMM | 0 | 2026-05-18 |
| [匹配DiD-广义DiD](匹配DiD-广义DiD.md) | 匹配DiD-广义DiD | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 3 | 2026-07-08 |
| [文本构念测量](文本构念测量.md) | 文本构念测量 | 12 | 2026-07-22 |
| [PSM匹配面板](PSM匹配面板.md) | PSM匹配面板 | 3 | 2026-06-16 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [多行为者设计](多行为者设计.md) | 多行为者设计 | 1 | 2026-07-08 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [两阶段模型](两阶段模型.md) | 两阶段模型 | 5 | 2026-07-21 |
| [VARX-PVAR](VARX-PVAR.md) | VARX-PVAR | 8 | 2026-07-15 |

## 写入规则

1. 仅 `distill-methods-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

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
>   - 配套 write-results：多研究 变体5（逐研究 Discussion 接力立项）、SEM-moderated-mediation（reverse-order mediation test 确认序列中介因果排序）
>   - 配套 write-theory：hypothesis_forms（序列中介叙事打包式）、hypothesis_derivation_patterns（counterintuitive direction-reversal via mechanism substitution）

> ✅ **2026-07-22 更新**: 蒸馏 Kim & Lee (2026, SMJ) "Putting a Price on Mission" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）——empirical strategy / strategic human capital 风格（首篇多阶段决策管道 + WTP）：
>   - 多研究 变体6：**同一 IV 跨决策阶段管道** — 各阶段不同分析单元 + 条件性样本递减（attraction/selection/attrition，Schneider ASA）；区别变体1-5 的 cross-study 独立样本梯度
>   - 非线性模型 变体10：**revealed-preference WTP 三估计器系数比**（LPM/conditional logit/mixed logit，-beta_X/beta_price）；corpus 零命中 WTP/mixed logit；顺手修复 variants_count 重复键 typo
>   - 文本构念测量 变体12：**手工二元编码 + 多源聚合 + embedded/peripheral 构念边界**（区别变体11 的边界案例披露，本变体理论上限定构念范围到 core identity）
>   - 配套 write-results：OLS-FE 变体27（多阶段管道衰减 profile + 跨阶段对比句）、slot-R5（WTP 经济显著性双 benchmark）、slot-R6（Slough post-treatment selection 诚实边界）

> **已填充变体**: 103个 (分布于 14个设计类型文件)
> **新设计类型解锁**: 同伴效应-网络效应、多行为者设计
>
> ✅ **2026-07-23 更新（sync from local backup）**: 从 pre-sync 备份补回两批本地蒸馏成果：
>   - **VARX-PVAR 设计类型接入**（Borah & Tellis 2016, JMR）：8 个 Methods 变体（行业情境 4-reason 辩护、品牌选择 + quasi-experiment、第三方 NLP 数据 + 人工匹配、算法准确率双重验证、VARX 框架 3-reason 辩护、Granger causality 外生性论证、VARX 方程规格、VARX 估计细节）。配套 `../write-results/econometric-models/VARX-PVAR.md`（7 个 Results 变体）。
>   - **Pupovac, Astvansh, Carrillat & Legoux (2026, POM) "Product Recall Contagion in the Supply Chain" 蒸馏**：补回 7 个 Methods 变体——事件历史+事件研究 变体 8/9/10、两阶段模型 变体 4/5、面板数据-OLS 变体 23/24；含 2 个新反模式（事件-企业多源匹配无每步 N 审计、控制变量全部外包至附录）。
>   - 注：面板数据-OLS 变体编号因远程 86f478d 已占用 22（GEE，Abdurakhmonov et al. 2026 JOM），本地原 22/23 续编为 23/24。
