---
category: causal-hedging
description: 因果动词梯度——根据设计强度选择因果声称力度，防止因果越级。
function: 可信性——因果语言强度与设计可信度匹配，避免审稿人攻击 causal overclaim
slots: M3, M4, M7, M8
created: 2026-05-22
updated: 2026-05-22
---

# 因果动词梯度（Causal Hedging）

## 核心原则

**因果语言不是修辞装饰，而是对设计可信度的承诺。**

设计越弱（OLS/FE），动词越弱（associated with）；
设计越强（实验），动词越强（caused）。
越级使用会招致审稿人直接攻击。

## 强制词汇表

### 面板数据 / OLS / FE / HLM

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| associated with | increases, decreases | 无条件 |
| related to | leads to | 无条件 |
| linked to | causes | 无条件 |
| corresponds to | drives | 无条件 |
| predicts（仅限预测模型） | produces | 无条件 |

**示例**：
- ✓ `Digital transformation is associated with higher innovation.`
- ✗ `Digital transformation increases innovation.`

### 自然实验 / DiD

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| effect of... on... | causes | 仅在平行趋势/事件研究支持后 |
| associated with | leads to | 无条件（兜底） |
| impact of... on... | drives | 仅在识别假设检验通过后 |

**关键规则**：
- M7 模型设定段落：使用 "associated with" 或 "effect of... on..."
- M8 识别策略段落：可预告 "we estimate the effect of..."（前提：平行趋势检验在 Results 中已报告）
- **禁止**：平行趋势检验未通过或未在 Results 中出现时，使用 "effect of" 描述主效应

**示例**：
- ✓ `We estimate the effect of [treatment] on [outcome] using a DiD model.`（M7，模型设定）
- ✗ `The policy caused a 15% increase in [outcome].`（M7，越级——除非实验设计）

### IV / 2SLS

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| effect of... on... | causes | M8 识别假设 preview 后 |
| increases, decreases | leads to | Second-stage 汇报中 |
| associated with | produces | 无条件（兜底） |

**关键规则**：
- First-stage 描述：使用 "predicts" / "is associated with"（工具变量相关性）
- Second-stage 汇报：可用 "effect"，但避免 "causes"
- 排他性约束论证：使用 "affects... only through..."（而非 "causes... only through..."）

### 非线性模型（Logit / Probit / Tobit / 计数）

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| associated with | increases（直接） | 系数不可直接解释 |
| increases the likelihood of | decreases（直接） | 必须通过边际效应转述 |
| changes the probability of | causes | 必须通过边际效应转述 |
| predicts | leads to | 结构方程/预测模型中 |

**关键规则**：
- M7 模型设定：`Because [DV] is binary, coefficients indicate direction but substantive interpretation requires marginal effects.`
- Results 汇报：报告 Average Marginal Effects (AME) 后，才能说 "increases the probability of"

### 生存分析

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| associated with | causes | 无条件 |
| lengthens/shortens time to | leads to | AFT 模型且分布选择已论证 |
| changes the hazard of | produces | Hazard 模型且比例风险假设已检验 |
| accelerates/delays | — | 有明确时间度量单位时 |

### 实验

| 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|
| caused | — | 随机化支持后 |
| led to | — | 随机化支持后 |
| produced | — | 随机化支持后 |
| increased, decreased | — | 随机化支持后 |

**关键规则**：
- 实验是唯一允许使用 "caused" 的设计家族
- 但仍需限制 generalizability：`The manipulation caused [effect] within the experimental context.`

---

## 动词替换速查表

| 你想表达的意思 | OLS/FE | DiD/IV | 实验 |
|---------------|--------|--------|------|
| X 和 Y 正相关 | associated with | associated with | — |
| X 对 Y 有影响 | related to | effect of X on Y | caused Y |
| X 增加 Y 的概率 | — | increases the likelihood of | increased |
| X 缩短达到 Y 的时间 | — | shortens time to | shortened |
| X 通过 M 影响 Y | — | effect mediated by M | mechanism: M |

---

## 常见越级错误

| 错误表述 | 设计类型 | 越级类型 | 修正 |
|---------|---------|---------|------|
| `DT increases innovation.` | OLS/FE | 强因果词 | `DT is associated with higher innovation.` |
| `The policy led to a decline.` | DiD（平行趋势未检验） | 时序因果词 | `The policy is associated with a decline.` |
| `IV caused the outcome.` | 2SLS | 最强因果词 | `IV has an effect on the outcome.` |
| `The coefficient increases Y.` | Logit | 线性解释 | `The coefficient increases the likelihood of Y.` |
| `The hazard ratio causes...` | Cox | 比率→因果 | `The hazard ratio indicates...` |

## 试探性因果表达（weak/tentative）— Discussion 与 Theory 专用

> **来源**：Morley (2021) Ch.14 *Explaining Causality* 的 "Expressing a causal relationship tentatively" 子块。
> **与上方强制词汇表的关系**：上方词汇表管**因果越级的上限**（OLS 禁用 caused）。本节管**下限表达**——当 Discussion 解释机制、Theory 推导假设时，需要表达"弱关联/试探性因果"的措辞。两节互补：上限防越级，下限防生硬。
> **使用场景限定**：仅用于 **Discussion 机制解释**与 **Theory 假设推导**。**禁止用于 Results 主效应报告**（主效应按上方设计家族词汇表直接报告，不得弱化为 tentative）。

### 试探性关联表达（有证据但未确认因果）

- [X] appears to be linked to [Y].
- There is some evidence that [X] may [affect/influence] [Y].
- [X] may play a role in [Y].
- A weak [association/link] may exist between [X] and [Y].
- These findings are [consistent with / suggestive of] the possibility that [X] [influences] [Y].
- It is conceivable that [X] contributes to [Y] through [mechanism].

### 试探性机制归因（Discussion 解释为什么）

- [X] may [operate through / work by] [mechanism].
- One possible mechanism is that [X] [affects] [Y] via [pathway].
- [X] appears to [influence] [Y], at least in part, by [mechanism].
- The [relationship/association] between [X] and [Y] may be [attributed to / explained by] [mechanism].

### 与 hedging-strength 的配合

本节的 "appears to / may / some evidence" 对应 `write-introduction/academic-writing-corpus/phrasebank/hedging-strength.md` 的**极弱/弱档**。Discussion 解释机制时：先用本节选试探性因果动词 → 再用 hedging-strength 选匹配强度的认识论句式 → 最后用 `prose-craft-checklist.md` §5.6/§5.7 校验未越级也未过度堆叠。

**禁忌**：试探性表达不得用于掩盖设计缺陷——若某替代解释威胁严重，应做稳健性检验而非用 "may be due to" 推给未来研究（见 `write-methods/SKILL.md` three-horned dilemma 自我定位）。
