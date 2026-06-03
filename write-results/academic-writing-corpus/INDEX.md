---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 手动写入验证通过的变体。
organization: by_result_type
result_types_count: 16
created: 2026-05-18
updated: 2026-06-03
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
| [计数模型](计数模型.md) | 计数模型 | 3 | 2026-05-20 |
| [实验](实验.md) | 实验 | 0 | 2026-05-18 |
| [多研究](多研究.md) | 多研究 | 0 | 2026-05-18 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 3 | 2026-05-20 |
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
> **总变体数**: 17 (分布于 5 个结果类型文件)
