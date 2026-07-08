---
type: canonical_reference
canonical_id: "16-threefold-gap"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: ADAPTABLE
exclusivity: HIGH
source_papers:
  - malshe_agarwal2015 (JM, 2015): "Yet little research investigates the effects of debt on marketing. This is surprising for three reasons."
  - cui_yang_vertinsky (SMJ): "three important issues remain unaddressed: product-market competition, portfolio composition, network embeddedness"
created: 2026-05-24
updated: 2026-07-08
source: Extracted from MVP30 batch_2026-05-24 + distilled by Phase 4.6
---

# 16-threefold-gap — 结构化三方论证缺口

## 功能定义

通过"Yet little research investigates X. This is surprising for [N] reasons"结构，从实践普遍性→邻近文献证据→理论后果三个维度系统化地展开 gap 的论证，使 Incompleteness 不再停留在"文献没研究"的薄弱断言。

## 适用场景

- 从母学科向目标学科导入核心构念（跨学科研究）
- Gap 的实践重要性在文献中被广泛承认但因故未被系统研究
- 需要在 Introduction 中同时完成 Tension + Stakes 功能的紧凑写法
- 目标现象有来自邻近文献的多条间接证据链（而非完全空白）

---

## 句法模板

### 变体 A：三点论证型（malshe_agarwal2015 型）

**模板**:
> "Yet little research investigates [phenomenon X in context Y]. This is surprising for [N] reasons. First, [Reason 1: prevalence/importance of X in the real world — with statistic or authoritative citation]. Second, [Reason 2: well-documented adjacent evidence — showing that related literatures document X's effects on proximal outcomes A, B, and C, implying X SHOULD affect Y too]. Third, [Reason 3: theoretical consequence — X limits a firm's ability to exploit Y-derived benefits, creating a compound theoretical gap]. [Transition to RQs or theory commitment]."

**来源**: malshe_agarwal2015 (JM), P2-P3

**论证负载递增原则**:
- Reason 1: Practical prevalence（现象面——X 在实践中有多普遍）
- Reason 2: Proximal literature evidence（文献面——邻近文献已经记录了 X 对 A/B/C 的影响）
- Reason 3: Theoretical consequence（理论面——X 不仅影响 Y 的直接前因，还影响 Y 的价值实现）

**关键特征**:
- 每个原因的论证域不同（practical → literature → theory），不能是同一域的不同例子
- 原因排序为 impact ascending（最小→最大理论后果）
- "surprising"（而非 "unfortunate"/"concerning"）是关键词——强调反常而非哀叹
- 三个原因结束后自然过渡到 RQ 或 Theory Lens——无需独立 Stakes 段落

---

### 变体 B：三问题逐一枚举型（cui_vertinsky 型）

**模板**:
> "A thorough study of [focal relationship] is of great theoretical importance, contributing to [broader theoretical model] ([citation]). Prior studies on [sub-literature] have provided important insights into [core tension] ([citations]). For example, researchers maintain that [mechanism 1] ([citations]) and have identified important factors that influence [process], such as [factor A] ([citations]), [factor B] ([citation]), and [factor C] ([citation]). However, [N] important issues in this sphere of research remain unaddressed. First, while researchers have examined [X], prior studies focused on [within-scope outcome]; the effect of [X] on [product-market outcome] remains poorly understood. Second, prior studies provide insights into [Y] by focusing on [dominant type] while overlooking [other types] ([citation]). It is assumed that [dominant-type assumption], but [counterpoint about heterogeneity]. [Theoretical consequence]. Few studies have yet examined how [portfolio composition] affects [outcome]. Third, many prior studies have examined [Z] by focusing on characteristics of [actors per se], such as [characteristic A] ([citation]) and [characteristic B] ([citation]), while largely overlooking the impact of [network/context dimension] ([citation]). [Exception citations]. Yet the focus of these studies remains centered either on [outcome 1] or on [outcome 2]; the impact of [network/context dimension] on [focal interplay] has rarely been studied."

**来源**: cui_yang_vertinsky (SMJ), P2-P4

**原文锚定**:
> "A thorough study of this 'collaboration–competition' relationship between partners is of great theoretical importance... Prior studies on alliance learning have provided some important insights into the tension between collaboration and competition... However, three important issues in this sphere of research remain unaddressed. First, while researchers have examined aggressive learning between allies... prior studies focused on the hazards of misappropriation within alliances; the effect of alliances on competition between partners in the realm of product markets remains poorly understood. Second, prior studies provide insights into competitive learning between partners by focusing on research-based alliances while overlooking other types of collaboration... Third, many prior studies have examined the tension between cooperation and competition by focusing on characteristics of the allying firms per se... while largely overlooking the impact of the broad inter-firm alliance networks..."

**关键特征**:
- "three important issues remain unaddressed" 作为显式缺口计数，比 "little research" 更有结构感
- 三个问题分别对应不同分析单元：市场边界（within-alliance → product market）、联盟组合类型（research-based → portfolio composition）、分析层次（firm characteristics → network embeddedness）
- 每个问题内部使用 "while... remains poorly understood" / "by focusing on... while overlooking" / "largely overlooking... has rarely been studied" 等 Incompleteness 标志性语言
- 三个问题共同收敛到论文的 RQ 和理论透镜（alliance learning + network perspectives）

**适用**: 当缺口可从三个相互独立但理论相关的维度展开，且三个维度分别对应论文的不同假设群/贡献时

**禁忌**: 三个问题必须是独立的理论缺口，不能是同一缺口的三种表述；每个问题都需要具体文献引用支撑

---

## 组装规则

### 必须配对
- 与 `hooks/01-cross-disciplinary-analogy` (Hook) 配对: 跨学科导入是最自然的场景
- 与 `Incompleteness × Mechanism` 组合: 三个原因累积后导出 "我们需要理解 X→Y 的机制"

### 反模式提醒
- **原因同域**: 三个原因来自同一论证维度（如三个都是 "different industries not studied"）→ 单个原因即可
- **顺序错误**: 把最理论性的原因放在第一（读者跟丢论证链）
- **缺乏统计锚定**: Reason 1 必须是可量化的事实（80%, $X billion, N firms），不能是模糊声明
- **过度使用**: 只在 gap 确实有三个独立论证维度时才用——强行凑三个原因是反模式

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM | ⭐⭐⭐⭐⭐ | JM 偏好结构化论证，配合跨学科导入尤其有效 |
| JMR | ⭐⭐⭐⭐☆ | 可用，但需更强调方法论贡献配合 |
| OS | ⭐⭐⭐☆☆ | OS 偏好更概念化/悖论式的 gap 建构 |
| AMJ | ⭐⭐⭐☆☆ | AMJ 偏好现象驱动的 tension，三点论证偏文献驱动 |
| SMJ | ⭐⭐⭐☆☆ | 可用，但需与战略结果直接关联 |

---

## 相关语料

- 配合 `hooks/01-cross-disciplinary-analogy.md` 使用：跨学科导入 + 结构化 gap = 最强组合
- 配合 `tensions/01-despite-progress-unaddressed.md` 变体对比：后者单原因，前者多原因结构化
- 与 `write-theory` 路由：Incompleteness × (Mechanism + Boundary + Output) → 机制推演型(B) + 调节效应型(E)
