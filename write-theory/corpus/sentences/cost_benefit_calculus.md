<!--
corpus_id: cost_benefit_calculus
function: mechanism voice
type: sentence corpus
source_exemplar: chung_low_rust_2022_jams
confidence: medium
status: emerging (1p)
-->

# 成本-收益计算机制句语料库

> **功能**: 为 "行为者如何感知某行动的高收益 + 低成本" 提供可复用的机制表达
> **来源范文**: Chung, Low & Rust (2022, JAMS) — CEO confidence → myopic marketing management
> **核心逻辑**: 决策者面对 [current_benefit] 与 [long_term_cost] 的权衡；[IV] 通过提升前者/降低后者的感知来改变行动概率

---

## 基础权衡框架

```
[Actors] have to weigh the benefits of [action] to boost [short-term_outcome] against 
the long-term costs of [action] ([citations]). Thus, [actor]'s view of [future_state] 
will impact the perceived costs and benefits of engaging in [action].
```

```
[Action] represents a trade-off between [short-term_benefit] and [long-term_cost]. 
When [actor] perceives the former to be high and the latter to be low, [action] becomes 
more attractive.
```

---

## 感知高收益句

```
[Actors] high in [IV] see any drop in [metric] due to [negative_event], and the ensuing 
[consequence_1] and [consequence_2], as unwarranted and not reflective of [future_state]. 
As such, to a high-[IV] [actor], the costs of [negative_event] are perceived to be 
relatively high, and [action] becomes more attractive.
```

```
Because high-[IV] [actors] are [bullish/optimistic] about [future_performance] under 
their leadership, they view [short-term_benefit] as especially salient. In their assessment, 
[action] is an efficient way to avoid [undesired_outcome] without sacrificing what they 
believe will be superior future results.
```

```
High-[IV] [actors] are inclined to believe that [short-term_metric] is temporarily 
depressed and that [action] can bridge the gap without altering the firm's fundamental 
trajectory ([citations]).
```

---

## 感知低成本句

```
Although the long-term value loss that comes with [action] should generally deter 
[actor] from considering such [action_type], a high-[IV] [actor] is likely to perceive 
this long-term cost to be lower. [Actors] high in [IV] are inclined to think that the 
potential future losses due to current [action] can be made up for with higher firm 
performance under their leadership from other parts of the firm, thereby obviating and 
reducing any economic losses stemming from their [action_type] ([citations]).
```

```
High-[IV] [actors] tend to believe that any deterioration in [long_term_asset] caused 
by [action] can be reversed through their own subsequent actions or through superior 
performance elsewhere in the firm.
```

```
Because high-[IV] [actors] discount the likelihood of [adverse_long_term_state], they 
are less deterred by the prospective costs of [action].
```

---

## 综合收敛句

```
Overall, we expect the perceived higher benefits and lower long-term costs from [action] 
to drive [actor] to "borrow" from future [outcome] to cover any current potential 
[shortfall].
```

```
In sum, when [actor] simultaneously views [action] as delivering [short-term_benefit] 
and imposing a manageable long-term cost, [action] becomes the preferred response to 
[pressure].
```

```
Taken together, these arguments suggest that [IV] shifts [actor]'s cost-benefit calculus 
toward [action] by raising the perceived cost of [inaction] and lowering the perceived 
cost of [action].
```

---

## 反方行为者对比（同一 TMT 内上下级激励差异）

```
In contrast to [higher_actor], [lower_actor] faces [lower_benefit] and [higher_cost] 
from [action]. [Lower_actor]'s compensation is tied more closely to [functional_metric] 
than to [financial_market_metric], and [action] directly undermines [functional_metric] 
([citations]). Furthermore, [lower_actor]'s performance evaluation depends more on 
[functional_target] than on [profitability_target], so [action] would adversely affect 
their career outcomes ([citations]).
```

```
Whereas [higher_actor] can capture [stock-based_benefit] from [action], [lower_actor] 
bears the [functional_cost] without receiving a commensurate share of the [short-term_gain].
```

---

## 语料锚定

- **Chung, Low & Rust (2022, JAMS)** — CEO confidence and myopic marketing management
  - 权衡声明: "CEOs have to weigh the benefits of cutting marketing investments to boost reported earnings against the long-term performance costs."
  - 高收益: "confident CEOs see any drop in stock price due to missing earnings benchmarks, and the ensuing negative wealth and reputational impacts, as unwarranted and not reflective of the future"
  - 低成本: "a confident CEO is likely to perceive this long-term cost to be lower... the potential future losses due to current marketing cuts can be made up for with higher firm performance under their leadership from other parts of the firm"
  - 综合收敛: "Overall, we expect the perceived higher benefits and lower long-term costs from myopic marketing management may drive confident CEOs to 'borrow' from future earnings to cover any current potential earnings shortfall."
  - 上下级对比: "compared to the CEO, there are fewer stock price benefits for CMOs to boost accounting numbers... the CMO's short-term gains from having the firm beat earnings expectations, and their motivation for myopic marketing cuts, are greatly reduced compared to the CEO."

---

## 可替换变量清单

| 占位符 | 示例 |
|--------|------|
| `[action]` | cutting marketing spending, reducing R&D, delaying maintenance, share repurchases |
| `[short-term_outcome]` | reported earnings, EPS, stock price |
| `[long-term_cost]` | eroded brand equity, reduced innovation capacity, customer attrition |
| `[negative_event]` | missing earnings expectations, earnings shortfall |
| `[actor]` | CEO, manager, division head |
| `[IV]` | confidence, overconfidence, short-term incentive pay |
| `[higher_actor]` | CEO |
| `[lower_actor]` | CMO, CFO, CTO |

---

## 使用提示

1. **先建立权衡框架**：在使用高收益/低成本句之前，必须先说明行为者面临的是 [short-term_benefit] vs [long-term_cost] 的 trade-off。
2. **双向不对称可写**：如果研究涉及两个行为者（如 CEO vs CMO），使用 "反方行为者对比" 句说明同一行动对两人的成本-收益含义不同。
3. **避免 folk 解释**："perceived benefits" 和 "perceived costs" 必须有具体的心理机制（如乐观偏差、自我效能感、控制幻觉）支撑，不能只说 "他们觉得划算"。
4. **与 mechanism_chain.md 配合**：本语料提供 voice，具体 why-chain 结构请参见 `corpus/sentences/mechanism_chain.md` 的 "成本-收益计算机制链" 小节。
