# Character Ordering — 主角/配角出场顺序决策表

> **适用**: Theory & Hypotheses 章节有多个构念（IV/DV/moderator/mediator）时，决定它们的引入顺序。源自 Pollock (2025) Ch06 Table 6.1 *Structuring the theory and hypotheses section*。
> **解决的问题**: 标准调节/机制段落只描述每个构念的测量；本表回答"谁先出场、谁后出场"——这是审稿人快速判断 Theory 是否连贯的依据。出场顺序混乱会让读者不知道该关注谁。
> **母变体**: B 机制推演型（主效应）/ E 调节效应型（含配角）。
> **与 write-introduction `character-map.md` 的分工**: 后者管 Introduction 前 3 段的角色出场；本表管 Theory 内部 IV/DV/moderator 的排序。

---

## 主角配置决策矩阵（Pollock Table 6.1 核心）

"主角" = 核心 IV/DV（你 theorize 并测量的关键变量）。根据主角的数量与 IV/DV 角色，决定引入顺序：

| 主角配置 | 推荐出场顺序 | 理由 |
|---------|-------------|------|
| 单 DV + 单 IV | 任一领先都可以 | 对称，无强制顺序 |
| **单 DV + 多 IV** | **DV 先 → IVs 后** | 先确立"被影响的对象"，再逐个引入影响者，让每个 IV 的假设都锚定同一 DV |
| **单 IV + 多 DV** | **IV 先 → DVs 后** | 先确立"影响源"，再展示它的多个后果 |
| 多 IV + 多 DV | 任一可先，或随故事展开穿插 | 复杂；通常按 storyline 分组 |
| 全部是 IV（无单一焦点 DV） | sequential 随假设引入；若做**相对比较**则成组引入后跟假设 | 比较型设计需先全展示再对比 |
| 全部是 DV（罕见） | （原文标注 rare，无独立规则） | 通常意味着研究问题不清，考虑重定义 |

---

## 配角（supporting character）出场时机

配角 = moderator / mediator / 关键 context 变量，它们改变主线但不抢主线。

| 配角配置 | 出场时机 |
|---------|---------|
| 单个 DV 配角 | 常 **early** 引入（因不先定义就无法讲故事） |
| 单个 IV 配角 | **随故事展开**引入（在需要它的那个假设前） |
| 多个配角（不论 IV/DV） | **随故事展开**逐个引入 |

**典型范例**（Pollock 引 Pfarrer et al. 2010）：earnings surprises（DV 配角）因不先定义就无法讲故事而**开局引入**；investors' responses（第二组 DV 配角）则在**第二组假设前**才引入——配角不是一次性全部登场，而是按 storyline 节奏登场。

---

## Context（研究情境）的三种放置

| 放置 | 适用条件 |
|------|---------|
| **Early** | 若对引入 characters 不可或缺（不交代情境就无法理解构念） |
| **After theory** | 若对引入 characters 非不可或缺，但有助于讲故事 |
| **Late** | 若是 lab study 或较通用情境（如 S&P 500）对故事非关键 |

---

## Figure 放置规则（与 character ordering 配套）

| 图类型 | 放置位置 | 理由 |
|--------|---------|------|
| **General-theory figure**（综述/发展一般理论的图） | 在你**讨论相关理论的地方** | 帮助读者看到理论整合 |
| **Summarizing-model figure**（汇总假设关系的模型图） | 在**发展完假设之后**（Theory 节末尾） | 早放会被遗忘，读者须反复翻回 |

**硬性要求（Pollock Ch06 原文）**: "If you employ a summarizing figure, **please label each link in your model with the associated hypothesis**." 即模型图中每一条 IV→DV（或调节/中介）的连线，都必须标注对应的假设编号（H1、H2a 等）。无标签的总结图会让审稿人无法快速核对"假设与图是否一致"。

---

## 结构决策的 6 个 contingency 因素

Pollock 明确列出影响 Theory 结构的 6 个因素，本表是其中"主角/配角"两项的展开：

1. 理论域数量（single vs multiple theoretical domains）
2. 是否引入新构念（new constructs 通常 early）
3. **主角数量与角色**（→ 本表上半）
4. **配角数量与角色**（→ 本表中段）
5. context 的功能（→ 本表 context 放置）
6. figure 的位置（→ 本表 figure 放置）

**多理论域处理**: 若有多个理论域，先提出 general overarching framework，再引入各理论的具体内容并 integrate 或 contrast；理论与假设可 sequential，或先全部理论再全部假设。

---

## 与现有资产的接口

- **`phase-2-architecture.md`** 的 7 因素表已含"主角配置/配角配置"两行但压缩为单行——本表是其展开版，phase-2 在需要详细排序决策时应引用本文件。
- **`phase-4-qc-alignment.md`** 审计 3（假设形式）应增加一条"如输出含 summarizing figure，每条 path 必须标注对应 H 编号"（见缺口B 补强）。
- **write-introduction `character-map.md`** 管 Introduction 侧角色出场；本表管 Theory 侧——两者共同保证全稿角色一致性（paper-state.yaml 的 `theory.constructs` 应与 introduction 的 character-map 对齐）。

---

## 反模式

- **所有构念一次性全部定义再发展假设**——适用于简单设计，但多 IV/多 DV 时会让读者失去焦点；应按主角配置矩阵决定顺序。
- **配角抢主线**——把 moderator 当主角大篇幅论述，喧宾夺主；配角应"随故事展开"简洁引入。
- **总结图无假设标签**——审稿人无法核对图与假设的一致性（Pollock 明确要求 label each link）。
- **context 放置一刀切**——不是所有研究都 early 或都 late；按 context 对引入 characters 是否不可或缺来决定。
