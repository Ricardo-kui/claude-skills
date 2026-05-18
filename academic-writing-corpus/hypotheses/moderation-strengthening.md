# Moderation-Strengthening Hypothesis

## 功能定义
陈述一个调节变量如何强化（strengthen/enhance/amplify）主效应关系，从而展示核心效应在何种情境下会增强——与削弱假设形成互补，完整描绘效应的边界谱系。

## 句法模板

**模板 A（直接强化型）**：
```
[Theoretical argument for why moderator strengthens the relationship].
Thus, we hypothesize:
Hypothesis [N]: The [positive/negative] relationship between [X] and
[Y] will be [stronger/more positive/more negative] when [Moderator]
is [higher/lower].
```

**模板 B（交互增强型）**：
```
We argue that [Moderator] will enhance the [positive/negative] effect
of [X] on [Y]. This is because [mechanism]. Thus:
Hypothesis [N]: The greater [actor]'s [Moderator], the stronger the
[positive/negative] association between [X] and [Y].
```

**模板 C（条件激活型）**：
```
[X] may have only a [weak/moderate] effect on [Y] in general.
However, when [Moderator] is [high/low], [theoretical mechanism],
thereby [amplifying/dampening] the effect of [X] on [Y].
Formally:
Hypothesis [N]: [Moderator] [positively/negatively] moderates the
relationship between [X] and [Y].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? (JM)

> "Overall, increase in brand diversification is likely to reduce both the ability and motivation of firms to recall quickly when faced with problems of high severity. Thus, we propose:"
> **H₃:** The higher a brand's diversification, the stronger the relationship between problem severity and time to recall.

**来源**：The Push and Pull of Attaining CEO Celebrity (AMJ)

> "We argue that the push tactics CEOs use to attract attention will enhance the influence of the pull factors of strategic nonconformity... on celebrity attainment."
> **Hypothesis 4.** The greater a CEO's use of self-promotion tactics (i.e., push tactics), the stronger the positive association between strategic nonconformity and the CEO's likelihood of achieving the highest degree of celebrity attainment.

**来源**：Activism Risk and Corporate Self-Regulation (ASQ)

> "Hypothesis 2. The positive relationship between anti-SLAPP laws and institutional CSP will be stronger for firms with greater CSI coverage in the media."

**来源**：State Ownership and Firm Innovation (ASQ)

> "Thus in a highly competitive environment, the reduced political interference and increased managerial motivation lead SOEs to employ their resources more efficiently in innovation development:"
> **Hypothesis 3 (H3):** The moderating effect of state ownership on the relationship between R&D input and innovation output is less negative when industrial competition is higher.

**改写模板**：
> "[Theoretical argument for why moderator strengthens the relationship].
> Thus, we hypothesize:
> **Hypothesis [N]:** The [positive/negative] relationship between [X]
> and [Y] will be [stronger] when [Moderator] is [higher/lower]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——AMJ/SMJ/ASQ 都接受 |
| **理论类型** | 强化机制、情境放大、互补效应 |
| **前提条件** | 必须有理论论证为什么调节变量增强主效应，且不能与削弱假设逻辑矛盾 |
| **风险** | 若主效应本身不显著，强化假设失去意义；必须先建立稳健的主效应 |

## 关键技巧

强化假设的关键是展示**机制放大**：

| 弱表达 | 强表达 |
|--------|--------|
| "M strengthens the effect of X on Y" | "M enhances the emotional appeal and resonance of X, thereby amplifying its effect on Y" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 强化无边界 | "M always strengthens X" | 明确强化发生的情境条件 |
| 与削弱假设矛盾 | 同一论文中对相似调节变量既预测强化又预测削弱 | 确保调节变量的理论方向一致 |
| 交互项解释错误 | 系数方向与假设方向相反 | 仔细区分 "strengthens a negative effect" vs. "makes effect less negative" |

## 相关语料

- 配合 `hypotheses/moderation-weakening.md` 使用：同一调节变量的两侧效应（强化 vs. 削弱）
- 配合 `mechanisms/opposing-forces.md` 使用：强化假设常由互补力量理论推导
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分展示强化后的斜率变化

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Eilert et al. 2017; Lovelace et al. 2022; Activism risk）
- **来源论文**: Eilert et al. (JM) × 1; Lovelace et al. (AMJ) × 1; Activism risk (ASQ) × 1
- **生成力**: ✓ GENERATIVE
- **排他性**: 低——通用型调节假设
- **期刊限制**: 无限制
- **收录状态**: ✓ STANDARD
