---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 手动写入验证通过的变体。
organization: by_result_type
result_types_count: 17
created: 2026-05-18
updated: 2026-07-07
---

# Results Academic Writing Corpus

## 组织逻辑

按结果类型组织。每个文件包含：
1. **主骨架引用** — 指向 `write-results/SKILL.md` 中的对应模板
2. **累积变体** — 由 `distill-results-exemplar` Phase 4 手动写入的验证通过变体

## 结果类型索引

| 文件 | 结果类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [OLS-FE](OLS-FE.md) | OLS-FE | 5 | 2026-05-20 |
| [Logit-Probit-Ordered-Probit](Logit-Probit-Ordered-Probit.md) | Logit-Probit-Ordered-Probit | 0 | 2026-05-18 |
| [生存分析](生存分析.md) | 生存分析 | 5 | 2026-05-20 |
| [DiD](DiD.md) | DiD | 0 | 2026-05-18 |
| [计数模型](计数模型.md) | 计数模型 | 6 | 2026-07-06 |
| [实验](实验.md) | 实验 | 2 | 2026-07-06 |
| [多研究](多研究.md) | 多研究 | 1 | 2026-07-06 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 4 | 2026-07-07 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 4 | 2026-06-16 |
| [匹配DiD](匹配DiD.md) | 匹配DiD | 0 | 2026-05-18 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [跨受众构念对比](跨受众构念对比.md) | 跨受众构念对比 | 0 | 2026-05-18 |
| [三向交互](三向交互.md) | 三向交互 | 0 | 2026-05-18 |
| [构造暴露分解](构造暴露分解.md) | 构造暴露分解 | 0 | 2026-05-18 |
| [SEM-moderated-mediation](SEM-moderated-mediation.md) | SEM/调节中介 | 1 | 2026-06-03 |

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
> **总变体数**: 31 (分布于 9 个结果类型文件)
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
