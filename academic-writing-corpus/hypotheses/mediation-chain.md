# Mediation Chain Hypothesis

## 功能定义
陈述中介链假设——自变量通过一系列连续的中介变量影响因变量，建立"X → M1 → M2 → Y"的多步因果机制，展示现象作用的完整过程而非简单相关。

## 句法模板

**模板 A（直接中介型）**：
```
We theorize that [X] influences [Y] through [Mediator].
Specifically, [X] [increases/decreases] [Mediator] because
[theoretical mechanism]. In turn, [Mediator] [increases/decreases]
[Y] because [theoretical mechanism]. Thus:
Hypothesis [N]: [Mediator] mediates the relationship between [X] and [Y].
```

**模板 B（链式中介型）**：
```
We propose a sequential mediation mechanism in which [X] first
[increases/decreases] [M1], which subsequently [increases/decreases]
[M2], which ultimately [increases/decreases] [Y].
This chain operates because [theoretical justification for each link].
Formally:
Hypothesis [N]: The effect of [X] on [Y] is sequentially mediated by
[M1] and [M2].
```

**模板 C（间接效应型）**：
```
Building on [theory], we argue that [X] affects [Y] primarily
indirectly rather than directly. The indirect path operates through
[Mediator]: [X] shapes [Mediator] by [mechanism], and [Mediator]
in turn shapes [Y] by [mechanism].
Hypothesis [N]: [X] has a [positive/negative] indirect effect on
[Y] through [Mediator].
```

## 例句（来自 MVP30）

**来源**：From Finance to Marketing — Malshe & Agarwal, 2015 (JM)

> "We argue that financial leverage increases a firm's customer-related risk, which, in turn, leads to lower customer satisfaction."
> **Hypothesis 1:** Financial leverage has a negative effect on customer satisfaction.
> **Hypothesis 2:** Customer-related risk mediates the negative effect of financial leverage on customer satisfaction.

**来源**：Lobbying and Product Recalls — Singh & Grewal, 2023 (JM)

> "We propose that lobbying reduces product recalls through two mechanisms: (1) by reducing the likelihood of an investigation being opened, and (2) by increasing the time to recall once an investigation is opened."

**来源**：How Shareholder Litigation Risk Influences Firm Orientation toward Stakeholders

> "We argue that shareholder litigation risk increases stakeholder orientation by enhancing managers' perceived accountability to shareholders, which in turn leads to greater attention to stakeholder concerns."

**改写模板**：
> "We theorize that [X] influences [Y] through [Mediator]. Specifically,
> [X] [increases/decreases] [Mediator] because [mechanism]. In turn,
> [Mediator] [increases/decreases] [Y] because [mechanism]. Thus:
> **Hypothesis [N]:** [Mediator] mediates the relationship between
> [X] and [Y]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | JM, JAP, AMJ — 适合机制分解型论文；ASQ 偏好理论机制深度 |
| **理论类型** | 过程模型、机制解释、微观基础理论、因果链 |
| **前提条件** | 每个中介环节必须有独立理论支撑；不能只是统计中介 |
| **风险** | 中介分析极易被质疑为事后合理化；必须在理论部分预先提出完整链条 |

## 关键技巧

中介假设的核心是让读者能**逐步追踪因果链**：

| 弱表达 | 强表达 |
|--------|--------|
| "X affects Y through M" | "X shapes M by [specific mechanism], and M in turn shapes Y by [specific mechanism]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 无理论中介 | 先跑 Baron & Kenny，再编故事 | 中介假设必须在理论部分预先提出 |
| 链过长 | X → M1 → M2 → M3 → M4 → Y | 超过两步的中介链极难验证且说服力弱 |
| 反向因果 | M 可能是 Y 的结果而非原因 | 必须论证时间顺序和理论方向 |

## 相关语料

- 配合 `mechanisms/dual-path-ability-motivation.md` 使用：双路径中介是能力-动机机制的形式化
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：结果部分需报告间接效应大小
- 配合 `write-methods` skill 使用：方法部分需说明中介检验方法（Bootstrap, SEM 等）

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Malshe & Agarwal 2015; Singh & Grewal 2023）
- **来源论文**: Malshe & Agarwal (JM) × 1; Singh & Grewal (JM) × 1
- **生成力**: ✓ GENERATIVE
- **排他性**: 中——适合机制论文，不适用于纯调节论文
- **期刊限制**: JM/JAP 偏好微观基础；AMJ 适合组织层面中介
- **收录状态**: 🔬 EXPERIMENTAL
