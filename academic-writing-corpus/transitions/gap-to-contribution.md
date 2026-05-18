# Gap-to-Contribution Transition

## 功能定义
在精准定位文献缺口之后，立即展示本研究如何填补这个缺口。这是 Introduction 的"承诺段"—— 读者在这里形成对论文贡献的最初期待。好的过渡不是"所以我们研究X"，而是"因此我们提出/证明/展示了Y，这将改变读者对X的理解"。

## 句法模板

**模板 A（直接贡献型）**：
```
In this paper, we [examine / argue / show] that [core claim].
Drawing on [theory], we [explain / demonstrate / document] [mechanism].
[Third sentence: what readers will learn that they did not know before].
```

**模板 B（设计-问题匹配型）**：
```
To address this gap, we [conduct / analyze / exploit] [data / setting / method].
[Second sentence: why this setting or method is especially suited to answering the question].
[Third sentence: the headline finding in bounded form].
```

**模板 C（理论整合型）**：
```
We integrate [Theory A] and [Theory B] to explain [phenomenon].
[Second sentence: how the integration works — not by choosing sides, but by assigning each theory to a different facet].
[Third sentence: the resulting prediction or insight].
```

**模板 D（问题-答案对型）**：
```
We ask: [precise research question]?
[Second sentence: to answer this question, we analyze [data] from [setting]].
[Third sentence: our analysis reveals that [headline answer]].
```

## 例句（来自 MVP30）

**来源**：State Ownership and Firm Innovation

> "We integrate institutional and efficiency logics to explain how state ownership affects firm innovation. We argue that the relationship between state ownership and innovation is not linear but inverted U-shaped..."

**来源**：Does it Pay to Recall your Product Early?

> "Drawing on insights from the behavioral theory of the firm, we posit that time to recall is influenced by the firm's ability to fully investigate the defect and its motivation to wait for the outcome of the investigation."

**改写模板**：
> "In this [paper / study / article], we [examine / argue / demonstrate] that [core claim]. Drawing on [theory / theories], we [explain / show / document] [mechanism / relationship]. Our [analysis / investigation / evidence] reveals that [headline finding in bounded terms], which [theoretical implication / practical implication]."

## 关键技巧：贡献声明的四问法

Pollock 推荐的贡献段应该回答（显性或隐性）：
1. **What does the paper examine?** — 研究对象
2. **Why can this setting or design answer the question?** — 方法论合法性
3. **What does the paper show or argue?** — 核心发现/论点
4. **What conversation should move because of that answer?** — 理论对话的变化

最有效的贡献段通常在 **3-4 句话**内回答全部四个问题。

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| "本文研究了X" | 只回答了问题1 | 必须包含2-4 |
| 过度承诺 | "This paper fundamentally changes our understanding" | 改为"This paper clarifies a boundary condition"或"offers a more nuanced account" |
| 贡献是"第一个" | "We are the first to..." | "第一个"不是贡献，回答了什么新理论问题才是贡献 |
| 设计合法性不足 | "We use data from China" | 必须说明为什么中国/这个样本能回答这个特定问题 |

## 变体：贡献的三种逻辑

| 逻辑 | 句式 | 适用 |
|------|------|------|
| **Consensus shifting** | "We challenge the assumption that..." | 反转/修正现有理论 |
| **Consensus creation** | "We reconcile [Theory A] and [Theory B] by..." | 整合对立理论 |
| **Incompleteness filling** | "We identify [mechanism] as a previously omitted..." | 补充现有理论 |

## 验证状态
- **跨论文复现**: ✓ VERIFIED（universal pattern; all MVP30 papers contain a gap-to-contribution transition）
- **来源论文**: State Ownership and Firm Innovation (ASQ), Does it Pay to Recall your Product Early (JM), A Rising Tide Lifts All Boats (SMJ), Two Sides of the Same Coin (ASQ) — 所有论文均包含从 gap 声明到贡献预告的过渡
- **生成力**: GENERATIVE——所有学术 Introduction 的必备结构
- **排他性**: LOW——通用型 transition
- **期刊限制**: 无限制
- **收录状态**: ✓ STANDARD

## 相关语料

- 配合 `hooks/*` 各类 hook 使用：贡献必须回应 hook 中建立的 stakes
- 配合 `discussion-moves/contribution-statement.md` 使用：后文必须兑现这里的承诺
- 配合 `transitions/literature-to-gap.md` 使用：gap → contribution 是一个连续动作
