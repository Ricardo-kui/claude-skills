---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 手动写入验证通过的变体。
organization: by_result_type
result_types_count: 21
created: 2026-05-18
updated: 2026-08-23
---

# Results Econometric Models Corpus

## 组织逻辑

按结果类型组织。每个文件包含：
1. **主骨架引用** — 指向 `references/slot-R*.md` 中对应设计类型的变体（按需加载规则见 `write-results/SKILL.md` → 槽位骨架加载）
2. **累积变体** — 由 `distill-results-exemplar` Phase 4 自动写入的验证通过变体

## 选择优先（变体速查表）

> 每个结果类型文件顶部现已有「变体速查表」（2026-08-08 推广）：按槽位（R1–R9）分组 + 六列表（变体 | 适用场景 | 区别 | 状态 | 来源），是类型内变体选择的唯一入口。
> **状态词表已统一（三档，2026-08-29 用户裁决，与 _evidence_registry.yaml 一致）**：ROBUST（≥5 论文跨子领域复现）> VERIFIED（≥3 论文复现，或专家审计单源）> EMERGING（1–2 论文单源/双源；含「EMERGING（可选）」）。LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。旧五档词废弃，映射关系保留一句：待交叉/待第二篇交叉验证/部分验证/EXPERIMENTAL/通过（单篇）→ EMERGING；可选变体 → EMERGING（可选）；通过（双篇/专家审计）/通过（专家审计单源）/框架级（双源）→ VERIFIED；通过（N/5 复现）→ ROBUST（registry 非 ROBUST 则 VERIFIED）。
> 检索流程：SKILL 路由确定结果类型 → 打开类型文件读速查表 → 按槽位+状态定位候选 → 精读变体正文（骨架/诚实边界/跨 skill 对齐）。

## 结果类型索引

| 文件 | 结果类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [OLS-FE](OLS-FE.md) | OLS-FE | 62 | 2026-08-20；变体 63：R3/R5 ln(时长) DV 跨列选择性显著 + 天数回译幅度拍，wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；变体 64：R3 双处理对照四拍 + Wald 系数差检验 + 跨 DV 合并幅度，post_2022_women_tmt_strategic_renewal，通过（专家审计单源；变体 65：R4 分样本镜像对照 + 组内 Wald + Chow 诚实降级，post_2022_women_tmt_strategic_renewal，通过（专家审计单源）；变体 66：R7 三威胁小节化稳健性（选择性→替代估计→构念效度），post_2022_women_tmt_strategic_renewal，通过（专家审计单源）；变体 67：R1 双路径前提描述统计（理论预言零相关 + moderator 分布/条件定义），post_2022_women_tmt_strategic_renewal，通过（专家审计单源）；变体 68：R4 交互通道分解句（调节经差值 DV 哪个分量起作用+双分量佐证），westphal_bednar2005，EMERGING；变体 69：R8 理论前提实证验证双通道（样本内切割检验+Heckman 交底；样本外前提问卷+K-S），westphal_bednar2005，EMERGING；变体 70：R2 先验支持判据声明（判定规则先于结果交代+检验变量编码），westphal_bednar2005，EMERGING）；2026-08-29 fang2025 POM 新增 2 变体：R3 显式算术除法幅度拍（β×unit=amount → amount÷base=%）、R6 null 作为竞争策略裁决证据（supports A, while supporting neither B nor C 三策略一次收束） |
| [Logit-Probit-Ordered-Probit](Logit-Probit-Ordered-Probit.md) | Logit-Probit-Ordered-Probit | 23 | 2026-08-13；变体 O：首事件建模范围辩护（理论假设+反转占比经验双轨 + In effect 理论任务收束句），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 P：四格 null 格确认性报告（In contrast 正面报告 null + generally 汇总措辞 + 双 DV 并轨导航），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 Q：四格系数 Wald 正式确认（to confirm 升级排序证据 + 双 DV 双统计量并列 + e.g. 代表例），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 R：双 DV 收敛现造理论标签（Taken together + not only/but also 递进 + whereby 边界从句），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 S：滞后结构括弧敏感性（短/长双向夹逼 + 前向结果定位 + 不敏感性结论复述），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 T：普遍信念反转收束段（despite widespread belief 让步对撞 + suggest 克制强度 + 机制级命题聚合），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28) |
| [生存分析](生存分析.md) | 生存分析 | 19 | 2026-08-01 |
| [DiD](DiD.md) | DiD | 17 | 2026-08-23；2026-08-29 fang2025 POM 新增 2 变体：R2 RDiT 事件前后 model-free 时间序列图开篇（成分分解 + 显著性入图解读 + 附录 t 值 + 过渡到估计）、R8 跨事件复制泛化（第二事件同方程重估 + 双偶然性排除收束 limited to neither A nor B） |
| [计数模型](计数模型.md) | 计数模型 | 21 | 2026-08-12；变体 22：计数模型主效应四拍 + FE/RE 双模型平行复现，ball_2018，gap HIGH；变体 23：DV-split 调节 + 跨列系数对比（无交互项），ball_2018，gap HIGH；变体 24：exp(β) 乘法解释批量幅度翻译独立段（正负系数各演一遍），ball_2018，gap HIGH；变体 25：四 threat 前瞻式总起 + 逐 threat 收束句（中介甄别/PSM/安慰剂DV/反向因果），ball_2018，gap HIGH；变体 26：R3 聚合列显著→严重度分列定位承载类，wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；变体 27：R8 剂量—反应阈值发现（Wald χ² → tipping point），wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；变体 28：R1 假设键控描述统计叙述（计数模型），anand_mukherjee_2024，VERIFIED；变体 29：R2 三步递进架构+检验驱动估计器正当化链（计数模型），anand_mukherjee_2024，VERIFIED；变体 30：R6 主效应仅全模型显著→保守判不支持（计数模型），anand_mukherjee_2024，VERIFIED；变体 31：R7 计数双威胁 IV 排他性散文+GEE exchangeable（计数模型），anand_mukherjee_2024，VERIFIED；变体 32：R8 替代注意事件机制三角+跨DV交叉学习折扣竞争解释，anand_mukherjee_2024，VERIFIED；变体 33：R8 post hoc 记忆衰退时窗+编码化解释（计数模型），anand_mukherjee_2024，VERIFIED；变体 34：R9 假设-构念映射汇总表 headline answer（计数模型），anand_mukherjee_2024，VERIFIED |
| [实验](实验.md) | 实验 | 5 | 2026-08-03 |
| [多研究](多研究.md) | 多研究 | 8 | 2026-08-02 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 4 | 2026-07-07 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 10 | 2026-08-05；变体 11：R7 排他性约束量化暴露占比辩护，wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；变体 12：R7 弱识别临界值协议报告（Cragg-Donald vs Stock-Yogo），wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；变体 13：R7 非线性主模型下线性 2SLS 稳健性轨，wowak_2020_female_directors_recalls，VERIFIED (expert_audit_override 2026-08-28 产品召回主研究领域单源足矣)；2026-08-29 fang2025 POM 新增 3 变体：R4 内生调节变量 2SLS fitted-value 交互、R7 排他性理论论证+安慰剂回归双重辩护、R7 控制变量内生性三步递进辩护（剔除复制→保守性论证→滞后 IV） |
| [匹配DiD](匹配DiD.md) | 匹配DiD | 1 | 2026-08-05 |
| [Tobit](Tobit.md) | Tobit | 1 | 2026-08-12 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [跨受众构念对比](跨受众构念对比.md) | 跨受众构念对比 | 1 | 2026-07-30 |
| [三向交互](三向交互.md) | 三向交互 | 4 | 2026-08-13 |
| [构造暴露分解](构造暴露分解.md) | 构造暴露分解 | 0 | 2026-05-18 |
| [SEM-moderated-mediation](SEM-moderated-mediation.md) | SEM/调节中介 | 7 | 2026-08-03；变体 8：两步预测中介双路径汇合 + 双 moderator 条件间接效应 + 校准收束，post_2022_women_tmt_strategic_renewal，通过（专家审计单源） |
| [事件研究法](事件研究法.md) | 事件研究法 | 8 | 2026-08-12；变体 9：检验统计量三重背书（原始出处→模拟适用域→领域惯例先例 + 逐符号公式说明），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 10：分组 CAR 假设裁决（列导航基线→分组裁决 + 理论尾从句回响 + 全窗一致性判断），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 11：分组对比 t 检验调节裁决（方向→正式检验→区间值 + 逐窗复现声明 + 证据强度前置），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 12：交互后主效应保护段（误读拦截 + prerequisite 层级逻辑 + 方法论权威背书双判决句），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 13：范围外模式最强检验框架（预测限定句 + 让步结构 + decoupled 最难情形收束），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28) |
| [VARX-PVAR](VARX-PVAR.md) | VARX-PVAR | 7 | 2026-07-15 |
| [BLP-状态空间](BLP-状态空间.md) | BLP + Kalman/GMM 结构需求 | 5 | 2026-08-05 |

## 写入规则

1. 仅 `distill-results-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

> ✅ **2026-08-13 更新（Lun–Zurbruegg–Mount–Cheong 2026 ETP，Gate ① HIGH only）**: 条件Logit 主分析 + 嵌套三向。新增（均单篇 EMERGING）：
>   - **Logit-Probit-Ordered-Probit** 变体19–23：R3 Kitazawa 半弹性；R4 AME 符号反转（Interestingly）；R7 行业内置换 null 图；R7 同二元 DV system GMM；R8 QMS post-hoc（限 aligns with）
>   - **三向交互** 变体4：中和阈值随连续 Z 下降，强制报告 weaken-but-does-not-overturn 一侧
>   反模式 +2（附录稳健性无 threat 定位；H 预测 weaken 却把边际反转写成同等 reversal）。未改 SKILL 核心。
> ✅ **2026-08-12 更新（Chen, Ganesan & Liu 2009 JM, Gate ① 全部写入）**: 事件研究法 5→8；OLS-FE 55→56。ADD 4 变体（均单篇 EMERGING / section_variant）：事件研究法 R3 分组 AR 多检验+组间 Wilcoxon 主检验（`r3_eventstudy_subgroup_ar_multitest_contrast`）、R7 Heckman 双 subsample null-λ → 原截面无偏（`r7_eventstudy_heckman_null_lambda_unbiased_confirmation`）、R9 stakeholder 反直觉收束（`r9_eventstudy_counterintuitive_stakeholder_coda`）；OLS-FE R8 二元策略 legacy Kenny 完全中介 + 市场信号（`r8_ols_strategy_complete_mediation_kenny_signal`，强制标 legacy；2026-08-20 合并后重编号为**变体 62**）。反模式 +2（跳过对照 null AR；仅 Kenny 条件计数宣称 completely mediate）。诚实边界 +3（分组 AR≠截面因果；null λ≠无内生性；legacy Kenny 须附间接效应区间或显式标 legacy）。registry 首次登记「事件研究法」estimator；填补 Patell+分组 CAR 待入库缺口。SKIP R2/截面 PROACT 四拍（≈ Pupovac）。未改 SKILL 核心 / PDM 根。

> ✅ **2026-08-12 更新（Fini, Jourdan & Perkmann 2017 AMJ, Gate ① 全部写入）**: 计数模型 16→21。ADD 5 变体（均单篇 EMERGING）：R7 Poisson-GMM 威胁电池（生成回归元→bootstrap SE / 过离散→负二项 / 调节正交→Gram-Schmidt / 离群→截尾-winsorizing）、R4 曲线调节范围级验证（Bowen 二次项轮廓 + 显式例外）、R8 同 IV 替代操作化机制裁决（相对 vs 绝对 → null → 折扣竞争机制）、R8 量化-定性访谈三角验证（explanatory sequential design）、R7 system GMM 复制（连续化 DV + 内生性分类 + AR/Hansen 诊断）。反模式 +2（枚举型稳健性条目须逐条 threat 定位；曲线调节只报交互符号不报转折点/幅度）、诚实边界 +3（marginal p<.10 须显式标；替代操作化 null 须排除低功效；访谈只作三角验证）。registry sync 修复：变体13 补登 R3，R4 槽位对齐 3 变体，R7/R8 补登新变体。核心倒U链（变体13）已在本轮前入库，本次为残差缺口。未改 SKILL 核心。

> ✅ **2026-08-12 更新（Ridge et al. 2024 AMJ）**: 首次填充「Tobit」结果类型（变体1：左删失 DV 条件幅度四拍 + 实际重要性拍5），并扩展计数模型（变体14–16：显著但实际效应小降调 / null 符号反转替代机制 / 混合结果综合 + Discussion 交接）与 OLS-FE（变体54–55：前置 RIR + naive-vs-cure 2SRI 防御 / 外部证据实际重要性）。均为单篇 EMERGING，不升 core。诚实边界 +3（显著小效应必须降调；null 符号反转只作推测推迟 Discussion；规格敏感性把 null 变显著须透明 + 系数通胀对冲）。

> ✅ **2026-08-05 更新（Zorn–Shropshire–Martin–Combs–Ketchen 2017 SMJ）**: 多 DV 治理后果 + 外部监督调节。新增 IV-2SLS 变体8–10：
>   - 变体8：多 DV 平行 climax（%/货币/OR 设计匹配幅度翻译）
>   - 变体9：调节衰减 + mean/±1SD 条件斜率 + marginal support 诚实 + 跨 DV 选择性 null
>   - 变体10：kind-vs-degree 构念电池（dual-insider 反转 / 连续独立性子样本 / Chow 跳跃）
>   均为单篇 EMERGING；因果语言：instrumented 连续结果可用 effect/influence，稀有二元主 Logit 保持 associated/more likely。未改 SKILL 核心。

> ✅ **2026-08-05 更新（Hoffmann–Cheong–Phan–Zurbruegg 2024 JM）**: DiD+conditional logit 重蒸馏校准。修正 R5 误标（处理效应衰减 % ≠ 预测概率百分点）；R3 从「三层标题」改为 OR→相对概率+低基准诚实；R4 switch-off 拆分为 **90th 文本中和**（原文）与 **四场景图**（扩展范式）。新增 R2 分步入表、R7 top-firm 敏感性。全部保持 EMERGING / 单篇，不升 core。

> ✅ **2026-08-04 更新（Lee–Park 2024）**: Logit/Probit 结果语料新增“条件转折点 + 直接 Wald 差异检验”与“选择性路径机制辨析”两种写作变体。Lee & Park 经用户专家审计为典型 U／倒 U 写作范文，因此正式曲线检验链和转折点位置型调节均登记为 **VERIFIED**；选择性路径机制辨析仍为 EMERGING，因为它不是本次曲线范文审计的对象。新增五条反模式：正式 U 检验后置、用交互项代替几何比较、预测尺度未标注、`p = .00/p < .00`、以及用“全部支持”抹平完整模型中的证据衰减。核心路由不变。

> ✅ **2026-08-03 更新（Schumacher–Keck–Tang 2020）**: OLS-FE 新增“组内方向切换但不显著→直接组间系数差异裁决”和“三类构念效度威胁定向三角验证”。前者强制区分组内斜率、组内显著性与组间差异；后者把补充分析按 rival interpretation 组织。二者均为单篇 EMERGING reference variants。

> ✅ **2026-08-03 更新（Kashmiri–Nicol–Arora 2017）**: SEM/调节中介新增“共享中介跨异质结果分支的证据账本”：a-path 只报一次，但每个 outcome 的直接关系、间接效应区间与假设判定必须分别报告，并保留 radical-innovation 分支的不支持结果。OLS-FE 与全局注册表新增高风险反模式：不得通过删除当期不显著 controls 把 `p < .10` 挽救为 `p < .05` 并升级假设判定；legacy Baron–Kenny 条件计数不得替代间接效应区间或 moderated-mediation index。

> ✅ **2026-08-03 更新（Vidal–Mitchell 2015；Moon–Tuli–Mukherjee 2023）**: 计数模型新增“双极参照点分支：先报 null、再报子类型主发现与部分支持”；IV-2SLS 新增“稳健性例外账本：稳定结论、形态变化与脆弱边界分层报告”。二者均保留单篇 EMERGING 状态与诚实边界。

> ✅ **2026-08-02 更新（Lee–Wu–Bednar, Organization Science）**: 首次填充 DiD 结果类型：新增“交互项→经济幅度→双端条件效应→逐端假设核对”和“理论前提探测式补充证据链”。同时加入两条诚实边界：显著交互项不自动等于符号反转假设完整成立；TWFE+Bacon 只作旧式诊断，不替代异质性稳健错位 DiD 与平行趋势敏感性分析。

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
>   - SEM-moderated-mediation 追加：**Reverse-Order Mediation Sensitivity Test** — 反转序列中介顺序重测；反向间接效应 CI 含零只说明未检测到该竞争序列，与提议排序相容但不能确认时间或因果顺序；区别于 qiao2026 reverse-code+Wald（那是对立通道持续性比较）
>   - 配套 write-methods：实验 变体6（measurement/moderation of process 双设计 + rival accounts battery）、多研究 变体5（Empirical Plan 因果阶段化预告段）
>
> ✅ **2026-08-03 复审修正**: 将 reverse-order mediation 从“因果排序确认”降级为竞争排序敏感性检查；实验新增变体4（三条件干预的 omnibus→组间→组内→稳定组拆解）与变体5（竞争中介排序的有界报告）。两者均为单篇 EMERGING section variant。

> ✅ **2026-08-05 gap audit（Kim & Lee 2026 SMJ）**: 对照 2026-07-22 已入库资产后，**Methods 全部 SKIP**；Results 仅新增 2 个真正缺口变体（均单篇 EMERGING；未改 SKILL 核心；因果语言保持 association/advantage）：
>   - OLS-FE 变体45：**管道阶段集中异质性** — baseline IV≈0 ⇒ 亚组吸收全部前端优势，交互在中后段熄灭（区别变体8；配套变体27）
>   - OLS-FE 变体46：**Cinelli–Hazlett 敏感性 + 强观测协变量倍数基准**（区别变体15 RIR+Oster；corpus 零命中 Cinelli）
>   - SKIP：HC quality / next job / job satisfaction null / specification curve（slot-R7 已有）/ 既有 Methods 三变体与 slot-R5/R6

> ✅ **2026-07-22 更新**: 蒸馏 Kim & Lee (2026, SMJ) "Putting a Price on Mission" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - OLS-FE 变体27：**多阶段同 IV 管道衰减 profile** — single-study single-IV multi-stage（attraction+/selection+/attrition null）+ 跨阶段对比句把"前置显著+后置 null"提升为机制发现（signaling 衰减裁决）；区别 多研究.md 的 cross-study synthesis
>   - slot-R5 追加：**WTP coefficient-ratio 经济显著性** — 系数比翻译为工资百分比 + 双 benchmark（vs prior 定位 lower end + vs other attributes 论证 higher than）；corpus 零命中 WTP
>   - slot-R6 追加：**Post-treatment selection 诚实边界**（Slough 2023）— multi-stage pipeline 后置 outcome 的 ATE undefined 承认；corpus 零命中 Slough
>   - 注：OLS-FE 表行 21→27 顺手修正 pre-existing stale（实际变体到 26）；slot-R5/R6 为槽位骨架文件不在表中，总变体数 +3

> **总变体数**: 91 (分布于 18 个结果类型文件)
>
> ✅ **2026-07-25 更新（du_tsolmon2024 ORSC 蒸馏）**: 基于 Du & Tsolmon (2024, *Organization Science*) "Post-M&A Retention of Top Managers: The Role of Structural Knowledge" 对 OLS-FE 新增 6 个变体：
>   - OLS-FE 变体29：**选择偏误三步防御**（描述性模式→CEM→Heckman + associational 收尾）
>   - OLS-FE 变体30：**预测性零结果作为机制证据**（CAR null 反转排除 selection 替代解释）
>   - OLS-FE 变体31：**替代解释三连驳斥 + 异质性模式裁决收束**（"aligns more closely... than" 比较级）
>   - OLS-FE 变体32：**外部基准阈值分割 + 边际效应图阈值发现**（连续调节三层验证）
>   - OLS-FE 变体33：**下游绩效事后分析**（时间增长 + 多指标收敛 + 提示性收尾）
>   - OLS-FE 变体34：**2×2 类型学交叉对角描述性比较**（回归前非参数类型对比）
>   - 反模式新增 2 条：显著性语言不一致（p=0.052 称 significant vs p=0.071/0.075 称 marginal）；split-sample 系数对比无 Wald 检验
>   - 注：Methods 配套新增（自创连续相似度指标 + 多数据库漏斗）见 `../write-methods/corpus/`
>
> ✅ **2026-07-22 更新（slot-R7 六维框架扩展）**: 基于 Yuan et al. (2026, JOM) 对 1,706 篇文献的系统性审查，`references/slot-R7.md` 新增 7 个子变体段落骨架 + 1 个现有变体重命名：
>   - **Preprocessing Variation (4)**: 缺失数据处理 / 离群值-错误观测处理 / 数据转换策略 / 粗心回答筛查（均 🔬 EXPERIMENTAL，保守替代为现有 threat 段落 + 说明）
>   - **Covariate Variation (2)**: 含-不含控制变量对比 / 替代控制变量集（含 DAG 理论辩护）（均 🔬 EXPERIMENTAL）
>   - **Fragility/Direct Reporting of Divergent Findings (1)**: 稳健性检验不一致时直接报告结果、边界与 overall evidence，含 happy-path 和 divergent-path 双模板（🔬 EXPERIMENTAL）
>   - **样本威胁拆分**: 原"样本威胁" → "样本威胁 — 排除敏感性" + 新增"样本威胁 — 理论驱动子样本变异"
>   - 配套更新: `_evidence_registry.yaml` 新增 3 反模式 + 2 诚实边界
>   - 来源: Yuan, Den Hartog, Liu, De Hoogh, Sun, Zhao, Riisla & Belschak (2026) *Journal of Management* — 六维稳健性分析框架
>
> ✅ **2026-07-23 更新（sync from local backup）**: 从 pre-sync 备份补回两批本地蒸馏成果：
>   - **VARX-PVAR 结果类型接入**（Borah & Tellis 2016, JMR）：7 个 Results 变体（GIRF-based halo metric、graded support language、basis-points→dollars、FEVD relative importance、Venn diagram visualization、elasticity table、wear-in/wear-out dynamics）。配套 `../write-methods/corpus/VARX-PVAR.md`。
>   - **Pupovac, Astvansh, Carrillat & Legoux (2026, POM) 蒸馏**：补回 5 个 Results 变体——事件研究法 变体 2/3/4/5、OLS-FE 变体 28（Control Function + Heckman 双阶段修正表导航）。
>   - 注：OLS-FE 变体编号因远程 86f478d 已占用 27（Kim & Lee 2026 SMJ 管道衰减），本地原 27 续编为 28。
>
> ✅ **2026-07-30 更新（pollock2015 蒸馏）**: 基于 Pollock, Lee, Jin & Lashley (2015, *ASQ*) "(Un)Tangled"——动态同时方程面板 + AB difference GMM 的 Results。OLS-FE 新增 5 个高价值变体（均单篇、待第二篇交叉验证）：
>   - OLS-FE 变体35：**动态面板 ρ 持久性百分比解释 + 跨构念持久性对比**（ρ → "% persists in t" + 62.3% vs 50.3% status/reputation 路径依赖对比 + 交互系数年衰减率翻译）
>   - OLS-FE 变体36：**分样本 Wald χ² 系数比较 + partial support 诚实叙事**（跨多个 age 阈值报告 χ²(1) 系数相等性 + 据此判定 H1a 部分支持/H1b 不支持）
>   - OLS-FE 变体37：**GMM 零结果交互的 Monte Carlo 功效分析**（OLS 功效程序不适用 → 1000 次迭代模拟，平均功效 .91，排除 Type II error——把理论关键的零结果转为确证证据）
>   - OLS-FE 变体38：**post-hoc spline 重解释意外负效应**（首/次/三例分段 + 平方项 + 信息递减理论 → diminishing returns 重解释，标 post-hoc）
>   - OLS-FE 变体39：**替代估计器 3SLS 稳健性 + LDV 偏误诚实警示**（主动报告 3SLS 的 LDV 系数膨胀/R²≈.97 缺陷症状，用替代估计器失败反向佐证 AB 选择）
>   - 配套 write-methods：动态面板-GMM（4 变体，首次填充）+ 同时方程（2 变体，首次填充）见 `../write-methods/corpus/`
>   - 配套 write-theory：developmental reversal of reciprocal-causation asymmetry (H1a/H1b) + differential persistence / lagged-DV moderation (H2)
>
> **总变体数**: 102 (分布于 18 个结果类型文件；累计 pollock +5 / malshe +3 / zhou +2 / pontikes +1)
>
> ✅ **2026-07-30 更新（malshe2015 蒸馏）**: 基于 Malshe & Agarwal (2015, *JM*) "From Finance to Marketing"——5-方程 SUR 系统的 Results。OLS-FE 新增 3 个高价值变体（均单篇、待第二篇交叉验证）：
>   - OLS-FE 变体40：**Floodlight（Johnson-Neyman）符号反转线性交互**——全调节变量范围边际效应 + 90% CI 带，报告**双转折点**（零交叉点 ~65% leverage + 显著性交叉点 ~95% leverage，中间为"净负但未显著"灰色带）；区别变体17/18（Lind-Mehlum 曲线）与变体32（外部基准阈值）
>   - OLS-FE 变体41：**同时方程系统三条件中介 + 非对称支持**（跨方程系数乘积 + Sobel/Zhao-Lynch-Chen；advertising 中介成立 H1a、R&D 不成立 H1b——失败根因精确定位到条件2 IV→M 不显著）
>   - OLS-FE 变体42：**反直觉反向结果诚实报告 + 延迟到 Discussion**（H2c 预测低增长更敏感、实为高增长；Results 当场 "in contrast to H_c" + 推迟解释，Discussion 给 post-hoc 机制 + 数据局限）；区别变体6（当场解释）与变体30（预测性零结果）
>   - 配套 write-methods：同时方程 +2（辅助反向因果方程、DWH SUR-vs-3SLS）+ 面板数据-OLS +1（跨库手工匹配）见 `../write-methods/corpus/`
>
> ✅ **2026-07-30 更新（zhou2017 蒸馏）**: 基于 Zhou, Gao & Zhao (2017, *ASQ*) "State Ownership and Firm Innovation in China"——双研究 Results。+2 变体（均单篇、待第二篇交叉验证）：
>   - 多研究 变体6：**同一模型跨 facet-DV 双研究：核心收敛 + 边缘发散 + 发散由样本/情境差异解释**（H1b/H1c/H3 两 study 收敛；H1a/H2 在 Study 2 上市企业发散 → 解释为"上市企业靠市场融资→state ownership 资源分配作用失效"的 study-level 边界）；区别变体4（跨研究差异讨论）
>   - 三向交互 变体3：**"线收敛"图解——调节变量作差距消除器（gap closer）**（SOE 与非 SOE 的 R&D 产出效率差在高竞争下收敛；state start-up 向非 SOE 靠拢）；"converge" 叙事信号区别变体1（条件分解 t-test）、变体2（边际效应表）
>   - 配套 write-methods：IV-2SLS +1（地理 IV）、多研究 +1（facet-DV 复制）、非线性模型 +1（Tobit corner-solution）
>   - 注：三向交互 INDEX 表行 1→3（顺手修正 pre-existing stale：实际已含 chung_low_rust 变体2）
>
> ✅ **2026-07-30 更新（pontikes2012 蒸馏）**: 基于 Pontikes (2012, *ASQ*) "Two Sides of the Same Coin"。+1 变体（单篇、待第二篇交叉验证），**首次填充「跨受众构念对比」结果类型**：
>   - 跨受众构念对比 变体1：**同一构念跨两类受众的镜像相反效应**（label ambiguity → consumer −101.5*** on inverse rank vs VC +1.476*** on funding；两独立模型共享同一 IV，镜像符号即核心发现 + 同图双线可视化 + 各受众分别经济显著性翻译）；配套**受众内异质性反转**（corporate VC 作 market-taker，符号反转回负，排除受众异质性混淆）；诚实边界：两受众 DV 不同须论证均测"吸引力"、样本差异须年龄/规模匹配稳健性
>   - 配套 write-methods：实证对象构建 变体5（fuzziness + leniency label-ambiguity 测量）；Intro：`tensions/04-reality-contradicts-consensus` 变体G；Theory：audience-role dichotomy 增 two-stage reconciliation

> ✅ **2026-08-01 更新（darby2025 蒸馏）**: 基于 Darby, Wowak, Ketchen & Connelly (2025, *JSCM*)——recurrent-event AFT (Weibull) 生存分析 Results。该论文已在 source_papers 中，本次补齐**已登记来源但尚未提取为变体的结果报告写法**（5 个新变体，均单篇、待第二篇交叉验证）：
>   - **生存分析** 变体15：**AFT 主效应四拍 + "every day counts" 经济显著性辩护节奏**（R3+R5）——标准四拍后插入辩护段："N days may seem modest, but [stakes]" + 诊断效应量被零值压低 + 预告 PSM 的 M 天上限；补变体1 缺失的辩护维度
>   - **生存分析** 变体16：**Dummy-coding 方向翻译交互项**（R4）——0/1 哑变量调节的符号-语义映射（design=1/manufacturing=0 → 负系数=design 更强）；区别变体2（连续调节 AME@percentiles）和变体7（简洁交互）
>   - **生存分析** 变体17：**分样本调节 — 显著 vs 不显著对照（无 Wald 检验版）**（R3+R4）——Darby2025 的 H3 split-sample 报告；构成分样本调节三代演进的中间形态（变体4 坦承功效→本变体直接对比→变体8 加 Wald 升级）；**标注 antipattern 风险**：同向仅显著性不同时须补 Wald
>   - **生存分析** 变体18：**Threat-based 稳健性四威胁报告（生存分析专属）**（R7）——omitted/reverse/measurement/alternative-estimator 四威胁分节叙述式报告；与变体11（Darby2026 表格导航 19 检查）互补：≤8 个用叙述式，>10 个用表格
>   - **生存分析** 变体19：**PSM 平均处理效应结果报告（one-to-one, ATE 天数翻译）**（R7+R5）——PSM one-to-one + 中位数 0 分割 + ATE→天数 + "Put differently" 重述；变体9（CEM 双向）的姊妹变体，构成匹配类稳健性双轨
>   - 配套 write-methods：生存分析 +7 变体（16-22）；配套 write-theory：新增 `sentences/leitmotif-section-opener.md`

> ✅ **2026-08-05 更新（liu_shankar2015 蒸馏）**: 基于 Liu & Shankar (2015, *Management Science*) "The Dynamic Impact of Product-Harm Crises…"——**首次填充「BLP-状态空间」结果类型**（Kalman filter + random-coefficient demand + GMM）：
>   - BLP-状态空间 变体1：**GMM 嵌套模型 MMSC-AIC 逐步升级**（R2）
>   - BLP-状态空间 变体2：**RQ 驱动状态参数解读（initial + σ → recovered path → 理论）**（R3）
>   - BLP-状态空间 变体3：**双层级间接通道 + 品牌强度异质性**（R3 续块）
>   - BLP-状态空间 变体4：**反事实拟合验证 + 四通道长期损失分解**（R8）
>   - BLP-状态空间 变体5：**非最优性政策模拟 scenario ladder**（R8）
>   - 未写入：Table 5 控制变量 “as expected” 流水账（通用、无范式排他性）
>   - 注：不修改 write-results SKILL 路由（单篇 EMERGING）；validation 替代传统 R7 仅作 design note
>
> ✅ **2026-08-05 更新（castellaneta_conti_kacperczyk_2017_smj 蒸馏）**: 基于 Castellaneta, Conti & Kacperczyk (2017, *SMJ*) "Money Secrets"——准自然实验 OLS / DiD-equivalent（州 UTSA 错位颁布）。DiD +4、匹配DiD 首次填充 +1（均单篇 EMERGING；不升 core）：
>   - DiD 变体7：**平均净效应开场 + 正负权变预告**（R2+R3）
>   - DiD 变体8：**交互假设完整四拍（1-SD% 幅度，无交互图）**（R3+R4+R5）
>   - DiD 变体9：**识别威胁分节电池** Matching→政治经济→供需→Placebo→Early/Late→替代测量（R7）
>   - DiD 变体10：**Null placebo（±k 期）作为识别确证**（R7）
>   - 匹配DiD 变体1：**CEM 作事前对称威胁回应**（matching-as-robustness，非主估计器）
>   - 反模式/诚实边界：边际 p≈.06 不得与 p<.05 同等“supported”；placebo null ≠ 假设支持；无 event-study 时不得暗示已检平行趋势
>   - `core_candidate`（仅报告）：对立权变理论默认“净效应→权变展开”节奏；准实验 R7 强制分节威胁电池——单篇不改核心路由

> ✅ **2026-08-05 gap audit（Bendig, Hensellek & Schulte 2024 ETP）**: 对照 2026-08-04 已入库资产后，**Methods 全部 SKIP**（变体28 已覆盖 GEE+全零保留+U-test 链）；Results 仅新增 2 个真正缺口变体 + 轻量质量边界（均单篇 EMERGING；未改 SKILL 核心；关联/likelihood 语言）：
>   - Logit 变体17：**双焦点 IV 平行倒 U** — 分模型→联合模型→并列表 U-test（区别变体8 线性双 IV / 变体9 单曲线）
>   - Logit 变体18：**同调节双模式 shift vs steepen 分图裁决**（区别变体10 单 IV 几何；OLS-FE 变体18 / Lee–Park 变体12 均为单曲线）
>   - EXTEND：变体9/10 诚实边界（不利 Y 顶点≠最优中间；X²×W 同号不裁决几何）+ 反模式 2 条
>   - SKIP：stuck-in-the-middle 独立 Results 变体（Discussion/Theory 收束；Results 只报 peak likelihood）；形式 U-test / 概率成本 / threat-indexed R7 / Methods GEE 链（已入库）
