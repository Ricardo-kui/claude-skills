---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 手动写入验证通过的变体。
organization: by_result_type
result_types_count: 18
created: 2026-05-18
updated: 2026-07-22
---

# Results Econometric Models Corpus

## 组织逻辑

按结果类型组织。每个文件包含：
1. **主骨架引用** — 指向 `references/slot-R*.md` 中对应设计类型的变体（按需加载规则见 `write-results/SKILL.md` → 槽位骨架加载）
2. **累积变体** — 由 `distill-results-exemplar` Phase 4 自动写入的验证通过变体

## 结果类型索引

| 文件 | 结果类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [OLS-FE](OLS-FE.md) | OLS-FE | 27 | 2026-07-22 |
| [Logit-Probit-Ordered-Probit](Logit-Probit-Ordered-Probit.md) | Logit-Probit-Ordered-Probit | 8 | 2026-07-07 |
| [生存分析](生存分析.md) | 生存分析 | 14 | 2026-07-07 |
| [DiD](DiD.md) | DiD | 0 | 2026-05-18 |
| [计数模型](计数模型.md) | 计数模型 | 11 | 2026-07-07 |
| [实验](实验.md) | 实验 | 3 | 2026-07-07 |
| [多研究](多研究.md) | 多研究 | 5 | 2026-07-22 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 4 | 2026-07-07 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 4 | 2026-06-16 |
| [匹配DiD](匹配DiD.md) | 匹配DiD | 0 | 2026-05-18 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [跨受众构念对比](跨受众构念对比.md) | 跨受众构念对比 | 0 | 2026-05-18 |
| [三向交互](三向交互.md) | 三向交互 | 1 | 2026-07-07 |
| [构造暴露分解](构造暴露分解.md) | 构造暴露分解 | 0 | 2026-05-18 |
| [SEM-moderated-mediation](SEM-moderated-mediation.md) | SEM/调节中介 | 5 | 2026-07-22 |
| [事件研究法](事件研究法.md) | 事件研究法 | 1 | 2026-07-07 |

## 写入规则

1. 仅 `distill-results-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

> ✅ **2026-05-20 更新**: 五篇产品召回论文 Results 蒸馏完成，首批 16 个变体写入。
>
> **已填充结果类型**: 4/15 (OLS-FE, 生存分析, 计数模型, IV-2SLS)
> **核心骨架 (4/5 复现)**: AFT 四拍 + exponentiated beta (生存分析 变体1)
> **高频可选 (2-3/5)**: AFT 交互效应五拍、叙事型稳健性检验、Event Study→CAR 第二阶段
> **单篇高价值 (1/5)**: Shape parameter 前置、分组检验+小样本诚实、Table 9 矩阵、Quartile penalty、MCMC mediation、竞争假设报告、model-free 预览、IV 诊断嵌入
>
> ✅ **2026-07-06 更新（续）**: 蒸馏 Falchetti, Cattani & Ferriani (SMJ) "Start with 'Why,' but only if you have to" 新增实验/多研究结果报告骨架：
>   - 实验 变体1：**Experimental Main-Effect Cadence (ANOVA 五拍)** — 异常值 → F/p/η² → M/SD/CI → 图 → 假设支持
>   - 实验 变体2：**Mediation Analysis Cadence (Hayes PROCESS)** — mediator ANOVA → 替代机制排除 → b/SE/CI → 机制结论
>   - 多研究 变体1：**Cross-Study Synthesis** — 变异维度明示 + 逐研究收敛 + 边界保留
>
> ✅ **2026-07-07 更新**: 蒸馏 Lashley & Pollock 2020 (ASQ) "Waiting to Inhale" 新增 4 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁新结果类型「定性过程研究」：
>   - 定性过程研究 变体1：**Process-Model Overview** — 阶段 + 分析透镜 + 竞争目标预览
>   - 定性过程研究 变体2：**Front-Stage / Backstage Contrast** — 公开话语与私下生存行为并置
>   - 定性过程研究 变体3：**Side-Stage Negotiation** — 部分可见冲突 → 规范澄清
>   - 定性过程研究 变体4：**Audience-Specific Success Assessment** — 按受众分别评估有限进展
>
> **总变体数**: 42 (分布于 10 个结果类型文件)
> **新结果类型解锁**: 实验、多研究、定性过程研究
>
> ✅ **2026-07-06 更新**: 蒸馏 Cutolo & Ferriani 2024 (JM) "How Narratives Can Help Atypical Actors Increase Market Appeal" 新增计数模型结果报告骨架：
>   - 计数模型 变体4：**Count-Model Moderation Translation** — 负二项交互项的预测计数解释（min/max moderator → predicted count difference → penalty reduction %）
>   - 计数模型 变体5：**Text-Measure Robustness Bundle** — 文本测量的威胁组织（dictionary/tool alternative → topic granularity → component disaggregation）
>   - 计数模型 变体6：**Composite Text Component Disaggregation** — 复合文本指标分解（which facet drives the interaction）
>
> ✅ **2026-06-16 更新**: 蒸馏 Qiao, Hiatt & Sine (2026, SMJ) "dual imprinting" 新增结果报告骨架：
>   - IV-2SLS 变体4：**非线性估计器（生存/有限 DV）下的内生性检验——control-function 残差作 DWH 等价检验 + Stock-Yogo F + 有限样本偏误诚实提示**（解决"非线性主模型如何检验内生性"的普遍盲区）
>   - SEM-moderated-mediation 追加：**Reverse-code + Wald Test** 比较两条方向相反通道的持续性差异（H3 型 differential-persistence meta-hypothesis 的可检验化）
>
> ✅ **2026-07-07 更新**: 蒸馏 Mayo, Ball & Mills (2022, POM) "CEO Tenure and Recall Risk Management" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 生存分析 变体6：**风险模型三拍 + exp(β)−1 百分比解释**（Early/Late vs Middle ref 对称对立报告）
>   - 生存分析 变体7：**风险模型交互效应 — 简洁交互项实质含义翻译**（不需图示+AME）
>   - 生存分析 变体8：**分样本 H3 + Wald χ² 跨模型比较 + null-in-one-subgroup 确证叙事**（6拍节奏，"statistically independent"措辞）
>   - 生存分析 变体9：**CEM 双向处理 ATE 行格式**（正向+负向 ATE 并行报告）
>   - 生存分析 变体10：**替代机制交互检验 + 诚实收尾**（"though the alternative explanation cannot be completely ruled out"）
>
> ✅ **2026-07-07 更新（续）**: 蒸馏 Haunschild, Polidoro & Chandler (2015, ORSC) 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 计数模型 变体7：**主效应四拍 + e^β−1 百分比解释**（双DV平行报告）
>   - 计数模型 变体8：**非线性模型中的无显式交互项调节效应**（图形 + 子样本边际效应 t 检验）
>   - 计数模型 变体9：**跨测量复制的单句稳健性声明**（嵌入R3的非独立段落）
>
> ✅ **2026-07-07 更新（续2）**: 蒸馏 Mannor, Wowak, Bartkus & Gomez-Mejia (2016, SMJ) 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - OLS-FE 变体8：**主效应不显著但调节显著 — 条件化再定位**（方向正确→交互显著→条件分解）
>   - OLS-FE 变体9：**调节效应边际效应的单侧显著报告**（dy/dx + 不显著侧 "not statistically different from zero"）
>   - OLS-FE 变体10：**ΔR² + 条件边际效应嵌入经济显著性**（增量方差+条件百分比联合论证）
>
> ✅ **2026-07-07 更新（续3）**: 蒸馏 Pfarrer, Pollock & Rindova (2010, AMJ) 新增 3 个高价值变体：
>   - Logit-Probit-Ordered-Probit 变体1-3：首次填充该结果类型（R1 高密度开场、R3 OR翻译、R4 CAR分组）
>
> ✅ **2026-07-07 更新（续4）**: 蒸馏 Desai (2011, AMJ) 新增 2 个变体：
>   - 计数模型 变体10-11：负主效应正交互条件反转、跨模型共线性说明
>
> ✅ **2026-07-07 更新（续5）**: 蒸馏 Bamberger, Homburg & Wielgos (2021, JM) 新增 3 个变体：
>   - 多研究 变体2：跨研究镜像首句
>   - SEM-moderated-mediation 变体2：不一致中介→抑制变量
>   - OLS-FE 变体11：边际显著 90% CI
>
> > ✅ **2026-07-07 更新（续6）**: 蒸馏 Li, Chiu, Kong, Cropanzano & Ho (2026, JOM) "A Sensemaking Model of Investor Reactions to CEO Achievement Expression" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 实验 变体3：**被调节的序列中介五拍报告 — PROCESS first-stage moderation**
>   - OLS-FE 变体13：**交互效应百分比经济显著性 — 联合变化的幅度解释**
>   - OLS-FE 变体14：**低基础率调节变量的边际效应直方图 — 替代传统 ±1SD 线图**
>   - OLS-FE 变体15：**五威胁标签化稳健性序列 — RIR+Oster+CEM组合**
>   - 多研究 变体3：**三研究递进结果叙事 — 实验复制+现场面板三DV并行**
>   - 新建「事件研究法」结果类型：变体1 — 非显著主窗→替代窗探索
>   - 新结果类型解锁：事件研究法

> ✅ **2026-07-07 更新（续7）**: 蒸馏 Ahmadi, Khanagha, Berchicci & Jansen (2017, JMS) "Are Managers Motivated to Explore in the Face of a New Technological Change?" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - OLS-FE 变体16：**7模型层次回归表导航** — 主效应→双向→三向递进
>   - 三向交互 变体1：**三向交互条件分解** — 条件两向交互+简单斜率差异t-test+分面图（首次填充该结果类型）
>   - 多研究 变体4：**跨研究差异嵌入Results讨论** — 差异承认+理论解释+替代解释

> ✅ **2026-07-08 更新**: 蒸馏 Cui, Yang & Vertinsky (SMJ) "Attacking your partners: Strategic alliances and competition between partners in product markets" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - OLS-FE 变体17：**倒 U 型主效应 Lind-Mehlum 三步 + 转折点 CI + Cohen's d**
>   - OLS-FE 变体18：**曲线调节效应（二阶交互项符号 + flatten/steepen 图形解释）**
>   - OLS-FE 变体19：**多项式主效应 + 多个曲线调节的层次回归表导航**
>   - OLS-FE 变体20：**多项式/交互模型诊断（mean-centering + VIF + condition number + non-centered replication）**
>   - OLS-FE 变体21：**Post-hoc 枚举清单 + 附录引用**
>   - 新增反模式：稳健性检验仅在 4.1 Post-hoc 枚举带过；曲线关系未做 Lind-Mehlum 验证；曲线调节未解释二阶交互项符号
>
> ✅ **2026-07-08 更新（续）**: 蒸馏 Chung, Low & Rust (2022, JAMS) "Executive confidence and myopic marketing management" 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - **OLS-FE** 变体22：**无模型证据开场 — 四分位均值/中位数单调性**
>   - **OLS-FE** 变体23：**四分位距经济显著性 — 从 P25 到 P75 的幅度翻译**
>   - **OLS-FE** 变体24：**Heckman 两阶段表格导航 — 第一阶段 Table 3 → 第二阶段 Columns 1-4**
>   - **OLS-FE** 变体25：**替代 DV 证伪段落 — 领域外结果的预期不显著**
>   - **OLS-FE** 变体26：**内生性稳健性表叙事 — threat-by-threat Table 7 汇总（DWH + Gaussian copula）**
>   - **三向交互** 变体2：**连续调节变量三向交互 — 边际效应表（Table 5 Panels B/C 风格）**
>
> ✅ **2026-07-22 更新**: 蒸馏 Ilicic & Brennan (2026, JM) "Political Ideology Shapes Consumer Responses to Addictive Products" 新增 2 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 多研究 变体5：**逐研究 Discussion 接力立项** — 每个 Study Discussion 末段固定三拍（贡献→具体限制→下一研究如何补救），consumer psychology 多研究标志性接力节奏（区别于变体2 的 Study 开场复制声明）
>   - SEM-moderated-mediation 追加：**Reverse-Order Mediation Test** — 反转序列中介顺序重测，反向间接效应 CI 含零即确认因果排序（Fairchild & McDaniel 2017）；区别于 qiao2026 reverse-code+Wald（那是对立通道持续性比较）
>   - 配套 write-methods：实验 变体6（measurement/moderation of process 双设计 + rival accounts battery）、多研究 变体5（Empirical Plan 因果阶段化预告段）

> ✅ **2026-07-22 更新**: 蒸馏 Kim & Lee (2026, SMJ) "Putting a Price on Mission" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - OLS-FE 变体27：**多阶段同 IV 管道衰减 profile** — single-study single-IV multi-stage（attraction+/selection+/attrition null）+ 跨阶段对比句把"前置显著+后置 null"提升为机制发现（signaling 衰减裁决）；区别 多研究.md 的 cross-study synthesis
>   - slot-R5 追加：**WTP coefficient-ratio 经济显著性** — 系数比翻译为工资百分比 + 双 benchmark（vs prior 定位 lower end + vs other attributes 论证 higher than）；corpus 零命中 WTP
>   - slot-R6 追加：**Post-treatment selection 诚实边界**（Slough 2023）— multi-stage pipeline 后置 outcome 的 ATE undefined 承认；corpus 零命中 Slough
>   - 注：OLS-FE 表行 21→27 顺手修正 pre-existing stale（实际变体到 26）；slot-R5/R6 为槽位骨架文件不在表中，总变体数 +3

> **总变体数**: 85 (分布于 18 个结果类型文件)
>
> ✅ **2026-07-22 更新（slot-R7 六维框架扩展）**: 基于 Yuan et al. (2026, JOM) 对 1,706 篇文献的系统性审查，`references/slot-R7.md` 新增 7 个子变体段落骨架 + 1 个现有变体重命名：
>   - **Preprocessing Variation (4)**: 缺失数据处理 / 离群值-错误观测处理 / 数据转换策略 / 粗心回答筛查（均 🔬 EXPERIMENTAL，保守替代为现有 threat 段落 + 说明）
>   - **Covariate Variation (2)**: 含-不含控制变量对比 / 替代控制变量集（含 DAG 理论辩护）（均 🔬 EXPERIMENTAL）
>   - **Fragility/Divergent Honest Reporting (1)**: 稳健性检验结果不一致时的诚实报告，含 happy-path 和 divergent-path 双模板（🔬 EXPERIMENTAL）
>   - **样本威胁拆分**: 原"样本威胁" → "样本威胁 — 排除敏感性" + 新增"样本威胁 — 理论驱动子样本变异"
>   - 配套更新: `_evidence_registry.yaml` 新增 3 反模式 + 2 诚实边界
>   - 来源: Yuan, Den Hartog, Liu, De Hoogh, Sun, Zhao, Riisla & Belschak (2026) *Journal of Management* — 六维稳健性分析框架
