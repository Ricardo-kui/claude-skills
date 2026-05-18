---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 手动写入验证通过的变体。
organization: by_result_type
result_types_count: 15
created: 2026-05-18
---

# Results Academic Writing Corpus

## 组织逻辑

按结果类型组织。每个文件包含：
1. **主骨架引用** — 指向 `write-results/SKILL.md` 中的对应模板
2. **累积变体** — 由 `distill-results-exemplar` Phase 4 手动写入的验证通过变体

## 结果类型索引

| 文件 | 结果类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [OLS-FE](OLS-FE.md) | OLS-FE | 0 | 2026-05-18 |
| [Logit-Probit-Ordered-Probit](Logit-Probit-Ordered-Probit.md) | Logit-Probit-Ordered-Probit | 0 | 2026-05-18 |
| [生存分析](生存分析.md) | 生存分析 | 0 | 2026-05-18 |
| [DiD](DiD.md) | DiD | 0 | 2026-05-18 |
| [计数模型](计数模型.md) | 计数模型 | 0 | 2026-05-18 |
| [实验](实验.md) | 实验 | 0 | 2026-05-18 |
| [多研究](多研究.md) | 多研究 | 0 | 2026-05-18 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 0 | 2026-05-18 |
| [匹配DiD](匹配DiD.md) | 匹配DiD | 0 | 2026-05-18 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [跨受众构念对比](跨受众构念对比.md) | 跨受众构念对比 | 0 | 2026-05-18 |
| [三向交互](三向交互.md) | 三向交互 | 0 | 2026-05-18 |
| [构造暴露分解](构造暴露分解.md) | 构造暴露分解 | 0 | 2026-05-18 |

## 写入规则

1. 仅 `distill-results-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

> ⚠️ 当前全部为 📋 TEMPLATE 状态（初始骨架，未经跨论文验证）。
> 变体由 distill-results-exemplar 逐步积累。
