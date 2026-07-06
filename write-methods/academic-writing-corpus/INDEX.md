---
corpus: write-methods
description: Methods 填空骨架变体库，按设计类型组织。由 distill-methods-exemplar 手动写入验证通过的变体。
organization: by_design_type
design_types_count: 22
created: 2026-05-18
updated: 2026-07-07
---

# Methods Academic Writing Corpus

## 组织逻辑

按模型设计类型组织。每个文件包含：
1. **主骨架引用** — 指向 `write-methods/SKILL.md` 中的对应模板
2. **累积变体** — 由 `distill-methods-exemplar` Phase 4 手动写入的验证通过变体

## 设计类型索引

| 文件 | 设计类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [面板数据-OLS](面板数据-OLS.md) | 面板数据-OLS | 5 | 2026-05-20 |
| [自然实验-DiD](自然实验-DiD.md) | 自然实验-DiD | 0 | 2026-05-18 |
| [非线性模型](非线性模型.md) | 非线性模型 | 1 | 2026-07-06 |
| [生存分析](生存分析.md) | 生存分析 | 6 | 2026-06-16 |
| [SEM](SEM.md) | SEM | 0 | 2026-05-18 |
| [实验](实验.md) | 实验 | 1 | 2026-07-06 |
| [多研究](多研究.md) | 多研究 | 2 | 2026-07-06 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 5 | 2026-07-07 |
| [稀有结果](稀有结果.md) | 稀有结果 | 0 | 2026-05-18 |
| [实证对象构建](实证对象构建.md) | 实证对象构建 | 0 | 2026-05-18 |
| [事件历史+事件研究](事件历史+事件研究.md) | 事件历史+事件研究 | 4 | 2026-05-20 |
| [同时方程](同时方程.md) | 同时方程 | 0 | 2026-05-18 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 4 | 2026-06-16 |
| [动态面板-GMM](动态面板-GMM.md) | 动态面板-GMM | 0 | 2026-05-18 |
| [匹配DiD-广义DiD](匹配DiD-广义DiD.md) | 匹配DiD-广义DiD | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [文本构念测量](文本构念测量.md) | 文本构念测量 | 7 | 2026-07-06 |
| [PSM匹配面板](PSM匹配面板.md) | PSM匹配面板 | 3 | 2026-06-16 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [多行为者设计](多行为者设计.md) | 多行为者设计 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [两阶段模型](两阶段模型.md) | 两阶段模型 | 2 | 2026-05-19 |

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
> **已填充变体**: 36个 (分布于 11个设计类型文件)
> **新设计类型解锁**: 实验、多研究实验、定性过程研究
>
> ✅ **2026-06-16 更新**: 蒸馏 Qiao, Hiatt & Sine (2026, SMJ) "dual imprinting" 新增 3 个高价值变体（均单篇、不可跨论文复现声明已标注）：
>   - 生存分析 变体6：**因 Cox 比例风险失败（Schoenfeld）→ piecewise exponential + 理论时段分割**（估计器由诊断驱动 + 分段由理论驱动）
>   - IV-2SLS 变体4：**外部自然事件（自然灾害）作工具变量 + 三因排除限制论证**（外生性 / 制度缝隙渠道 / 结果文献反推无直接渠道）
>   - PSM匹配面板 变体3：**Entropy Balancing (EBM)** — 重加权、保留全部观测，适用于处理组稀少/需保全样本的研究
>   - 配套 write-results：IV-2SLS 变体4（control-function 残差作非线性 DWH + 有限样本偏误诚实提示）、SEM-moderated-mediation（reverse-code + Wald 检验对立通道持续性差异）
>   - 配套 write-theory：mechanism_chain.md 新增"双重印记对立通道 + 效果持续性差异 + 底物匹配调节"骨架；write-introduction：theory-lens/05-maxim-contrast 变体B（单句历史名言作 foil）
