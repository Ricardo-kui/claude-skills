# Instrumental Variable Narrative

## 功能定义
为工具变量（IV）方法提供完整的方法论叙事，包括工具变量的选择逻辑、相关性假设和排他性限制的论证——这是处理内生性的黄金标准，也是审稿人最严格审查的部分。

## 句法模板

**模板 A（标准 2SLS 型）**：
```
To address potential endogeneity of [endogenous variable], we employ
a two-stage least squares (2SLS) approach. In the first stage, we
regress [endogenous variable] on [instrument(s)] and [controls].
In the second stage, we use the predicted values from the first stage
to estimate the effect on [DV].

We use [Instrument] as our instrument because [theoretical justification
for relevance]. The instrument is relevant because [specific mechanism
linking instrument to endogenous variable]. We argue that the instrument
satisfies the exclusion restriction because [justification for why
instrument affects DV only through endogenous variable].
```

**模板 B（自然实验工具型）**：
```
We exploit [natural experiment / regulatory change / exogenous shock]
as a source of exogenous variation in [endogenous variable].
Specifically, [event] created a plausibly exogenous shock to
[endogenous variable] because [mechanism]. This allows us to isolate
the causal effect of [endogenous variable] on [DV] from [confounding
factors].
```

**模板 C（多工具/过度识别型）**：
```
We use [N] instruments: [Instrument 1] and [Instrument 2]. The first
instrument captures [dimension 1], while the second instrument captures
[dimension 2]. We test the validity of our instruments using the
Sargan-Hansen overidentification test, which [result]. The first-stage
F-statistic is [value], well above the Stock-Yogo critical value,
suggesting that weak instruments are not a concern.
```

## 例句（来自 MVP30）

**来源**：CEO Regulatory Focus and Myopic Marketing Management

> "To address potential endogeneity of regulatory focus, we use [CEO's
> early life exposure to natural disasters] as an instrumental variable.
> This instrument is relevant because early life experiences shape
> personality traits... We argue that the exclusion restriction holds
> because [natural disaster exposure in CEO's childhood] affects myopic
> marketing management only through its effect on regulatory focus."

**来源**：Lobbying and Product Recalls — Singh & Grewal, 2023 (JM)

> "We exploit the variation in lobbying created by the revolving door
> between government and industry as a source of exogenous variation
> in firms' lobbying activities."

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "We use PSM to address potential selection bias... we also conduct
> 2SLS analysis using [instrument] as the instrument for state ownership."

**改写模板**：
> "To address potential endogeneity of [endogenous variable], we employ
> a [2SLS/natural experiment] approach. We use [Instrument] as our
> instrument because [theoretical justification]. The instrument is
> relevant because [mechanism]. We argue that the exclusion restriction
> is satisfied because [justification]. The first-stage F-statistic
> is [value], well above the critical value of 10, suggesting that
> weak instruments are not a concern."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, SMJ, AMJ — IV 是所有顶级期刊认可的因果识别方法 |
| **理论类型** | 因果推断、自然实验、历史工具变量、地理工具变量 |
| **前提条件** | 必须有强理论论证工具变量的相关性和排他性；不能只是统计显著 |
| **风险** | IV 假设是审稿人攻击的首要目标；必须在正文详细论证，而非附录 |

## 关键技巧

IV 叙事的核心是让读者相信**排他性限制成立**：

| 弱表达 | 强表达 |
|--------|--------|
| "Our instrument satisfies the exclusion restriction" | "Our instrument affects Y only through X because [specific mechanism], and alternative channels [channel 1, channel 2] are ruled out by [argument / data]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 弱工具变量 | F-stat < 10 | 报告 F-stat；若弱工具变量，使用 LIML 或 GMM |
| 排他性无论证 | 只说"we assume exclusion restriction" | 必须主动论证并排除替代渠道 |
| 过度识别不检验 | 有多个工具变量但不报告 Sargan-Hansen | 必须报告过度识别检验 |

## 相关语料

- 配合 `methods-narrative/endogeneity-defense.md` 使用：IV 是内生性处理的核心方法
- 配合 `methods-narrative/robustness-threat-test.md` 使用：IV 假设需用安慰剂检验和替代工具变量验证
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：IV 系数解释需特别注意局部平均处理效应

## 验证状态
- **跨论文复现**: ✓ VERIFIED（CEO Regulatory Focus; Zhou et al. 2017; Singh & Grewal 2023）
- **来源论文**: CEO Regulatory Focus (AMJ) × 1; Zhou et al. (ASQ) × 1; Singh & Grewal (JM) × 1
- **生成力**: ✓ GENERATIVE
- **排他性**: 中——仅适用于存在可信工具变量的情境
- **期刊限制**: 无限制，但 ASQ/SMJ 对 IV 假设要求更严格
- **收录状态**: ✓ STANDARD
