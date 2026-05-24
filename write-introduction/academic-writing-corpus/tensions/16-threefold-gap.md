---
type: canonical_reference
canonical_id: "16-threefold-gap"
status: EXPERIMENTAL
gap_type: Incompleteness
cross_paper: SINGLE-INSTANCE
generativity: ADAPTABLE
exclusivity: HIGH
source_papers:
  - malshe_agarwal2015 (JM, 2015): "Yet little research investigates the effects of debt on marketing. This is surprising for three reasons."
created: 2026-05-24
source: Extracted from MVP30 batch_2026-05-24
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
