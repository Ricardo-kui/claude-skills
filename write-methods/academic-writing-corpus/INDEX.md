---
corpus: write-methods
description: Methods 填空骨架变体库，按设计类型组织。由 write-methods SKILL.md 按需加载，由 distill-methods-exemplar 持续沉淀新变体。
organization: by_design_type
design_types_count: 21
created: 2026-05-18
updated: 2026-05-22
---

# Methods Academic Writing Corpus

## 组织逻辑

按模型设计类型组织。每个文件包含：
1. **frontmatter** — `design_type`、`status`、`variants_count`、`source_papers`
2. **设计特征摘要** — 该设计类型的 because 密度标杆、控制变量层级、跨论文复现率等
3. **M1–M10 主骨架与变体** — 按槽位组织，每个槽位含 `### 主骨架（通用）` 和若干 `### 变体 N`
4. **累积变体** — 由 `distill-methods-exemplar` Phase 4 验证通过、手动写入的增量变体

## 与 write-methods 的关系

- **write-methods/SKILL.md** 不再内嵌任何骨架文本。调用 `/write-methods` 时，根据 `<模型类型>` 实时读取本目录下的对应分片文件。
- 分片文件更新后，**即时生效**，无需修改 SKILL.md。
- 新增设计类型时，创建新分片文件并更新本索引表即可。

## 设计类型索引

| 文件 | 设计类型 | 主骨架槽位数 | 变体数 | 状态 | 最后更新 |
|------|---------|------------|--------|------|---------|
| [面板数据-OLS](面板数据-OLS.md) | 面板数据-OLS | M1–M10 | 10 | VERIFIED | 2026-05-22 |
| [自然实验-DiD](自然实验-DiD.md) | 自然实验-DiD | M1–M10 | 8 | EMERGING | 2026-05-22 |
| [非线性模型](非线性模型.md) | 非线性模型 | M1–M10 | 1 | EMERGING | 2026-05-22 |
| [生存分析](生存分析.md) | 生存分析 | M1–M10 | 4 | VERIFIED | 2026-05-22 |
| [SEM](SEM.md) | SEM | M1–M10 | 2 | EMERGING | 2026-05-22 |
| [实验](实验.md) | 实验 | M1–M10 | 9 | EMERGING | 2026-05-22 |
| [多研究](多研究.md) | 多研究 | M1–M10 | 4 | EMERGING | 2026-05-22 |
| [稀有结果](稀有结果.md) | 稀有结果 | M1–M10 | 2 | EMERGING | 2026-05-22 |
| [实证对象构建](实证对象构建.md) | 实证对象构建 | M1–M10 | 1 | EMERGING | 2026-05-22 |
| [事件历史+事件研究](事件历史+事件研究.md) | 事件历史+事件研究 | M1–M10 | 3 | VERIFIED | 2026-05-22 |
| [同时方程](同时方程.md) | 同时方程 | M1–M10 | 3 | EMERGING | 2026-05-22 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | M1–M10 | 3 | EMERGING | 2026-05-22 |
| [动态面板-GMM](动态面板-GMM.md) | 动态面板-GMM | M1–M10 | 1 | EMERGING | 2026-05-22 |
| [匹配DiD-广义DiD](匹配DiD-广义DiD.md) | 匹配DiD-广义DiD | M1–M10 | 3 | EMERGING | 2026-05-22 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | M1–M10 | 3 | EMERGING | 2026-05-22 |
| [文本构念测量](文本构念测量.md) | 文本构念测量 | M1–M10 | 3 | EMERGING | 2026-05-22 |
| [PSM匹配面板](PSM匹配面板.md) | PSM匹配面板 | M1–M10 | 4 | EMERGING | 2026-05-22 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | M1–M10 | 1 | EMERGING | 2026-05-22 |
| [多行为者设计](多行为者设计.md) | 多行为者设计 | M1–M10 | 2 | EMERGING | 2026-05-22 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | M1–M10 | 1 | EMERGING | 2026-05-22 |
| [两阶段模型](两阶段模型.md) | 两阶段模型 | M1–M10 | 2 | EMERGING | 2026-05-22 |

## 状态定义

| 状态 | 含义 | 升级条件 |
|------|------|---------|
| **ROBUST** | 跨 >=3 篇顶刊范文复现，跨 >=2 个独立数据源/期刊 | paper_count >= 3 且 sources >= 2 |
| **VERIFIED** | 跨 >=2 篇顶刊范文复现 | paper_count >= 2 |
| **EMERGING** | 有骨架内容，但 paper_count < 2 或尚无 distill 验证数据 | 初始状态 |

## 写入规则

1. 主骨架迁移自 `write-methods/SKILL.md` v2.6.0 的硬编码模板；新增变体由 `distill-methods-exemplar` Phase 4 验证通过后写入。
2. 每个变体标注来源论文、验证状态、写入日期。
3. 不覆盖现有变体，仅追加。
4. 变体达到 3+ 且跨 >=2 篇论文时，考虑提升为主骨架或标记为 STANDARD。

## 语料库质量状态

> **2026-05-22 迁移完成**: 全部 21 个设计类型的主骨架与变体已从 `write-methods/SKILL.md` 迁移至本分片文件。write-methods v3.0.0 起采用按需加载模式。
>
> **已验证设计类型 (2/21)**: 面板数据-OLS (4 papers) | 生存分析 (4 papers) | 事件历史+事件研究 (3 papers)
> **活跃累积变体**: 21 个（分布于 6 个设计类型文件）
> **核心骨架确认**: 面板数据-OLS 主骨架 M6 because 分层结构 (4/4 复现)；生存分析 M7 AFT/Weibull 分布选择 (4/4 复现)
