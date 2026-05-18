# Data Shock Hook

## 功能定义
用一组令人震惊的量化数据（通常来自权威商业机构 + 巨额经济损失 + 权威人物引语）作为开场，迅速建立问题的现实紧迫性和经济 stakes，迫使读者从"这很有趣"转变为"这必须被研究"。

## 句法模板

**模板 A（权威数据 + 经济损失 + 权威引语）**：
```
According to [Authoritative Source], [shocking percentage or absolute number] of [population] [experience adverse outcome], costing the [industry/economy] an estimated $[X billion] annually.
[Second sentence: translate the number into a concrete, imaginable loss].
[Third sentence: authority quotation that moralizes or dramatizes the stakes].
[Fourth sentence: convert to research question — but this gap has not been examined through the lens of [theory]].
```

**模板 B（趋势叠加 + 临界点）**：
```
[Verifiable trend] has accelerated dramatically.
By [year], [metric] reached [number], a [percentage] increase from [baseline year].
[Authority quotation or concrete consequence].
Yet little is known about [theoretical mechanism behind the trend].
```

## 例句（来自 MVP30）

**来源**：CEO Regulatory Focus and Myopic Marketing Management — IJRM

> "According to McKinsey & Company (2014), 63% of executives believe that short-term pressure from investors is leading to decisions that destroy long-term value. The effects of such short-termism are costly: it is estimated to have cost U.S. companies $79 billion in foregone earnings. As Warren Buffett noted, 'We know that the鼓励他们追求短期目标的做法会让他们做出愚蠢的事情...'"

**改写模板**：
> "According to [Authoritative Source (e.g., McKinsey, BCG, GAO)], [shocking percentage]% of [relevant actors] believe that [widespread problematic behavior] is [causing adverse outcome]. The effects are costly: it is estimated to have cost [relevant population] $[X billion] in [foregone earnings / lost productivity / preventable harm]. As [Iconic Authority Figure] noted, '[memorable quotation about the stakes].'"

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | AMJ, SMJ, JOM, IJRM 极度适合；ASQ 也可用，但需更快显示理论张力而非纯现象 urgency |
| **理论类型** | 最适合 **现象驱动型量化论文**（phenomenon-driven quantitative）；_upper echelons, governance, strategic decision-making_ |
| **前提条件** | 必须有真实可查的数据源；数字必须足够大（十亿级别或百分比惊人）；权威引语必须与论文核心机制相关 |
| **风险** | 数据过时（5 年前的 McKinsey 报告在 2026 年可能失效）；数据 shock 后如果理论 gap 过小，会产生"雷声大雨点小"感 |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 堆砌数字 | 连续三个数据点，没有叙事递进 | 一个核心数字 + 一个具象化翻译 + 一句权威定性 |
| 数字后无 theory bridge | "损失了 $79bn" → "所以我们研究 CEO 认知"，中间缺了理论桥梁 | 必须在数据 shock 和 research gap 之间插入一句："This widespread short-termism suggests that [theoretical mechanism] may be systematically distorted" |
| 引语装饰化 | Warren Buffett 的话很精彩，但和论文核心假设无关 | 引语必须能回响在后文的理论论证中（如 Buffett 谈"reputation"在 H2 中被理论化） |

## 数据 Shock 的三种升级路径

| 类型 | 结构 | 示例 |
|------|------|------|
| **经济损失型** | 数字 + 具象化 + 权威 | "$79bn foregone earnings" |
| **身体伤害型** | 统计 + 个体化 + 政策回应 | "150 complaints of injuries or deaths" |
| **制度异常型** | 比例 + 对比 + 悖论 | "63% of executives believe... yet 90% of boards reward..." |

## 相关语料

- 配合 `stakes/02-quantified-economic-loss.md` 使用：将 shock 数据进一步转化为具体的 shareholder wealth 损失
- 配合 `tensions/04-reality-contradicts-consensus.md` 使用：数据揭示的现实与理论共识之间的矛盾

## 验证状态
- **跨论文复现**: ✓ VERIFIED（2 additional papers across JMR, MSOM）
- **来源论文**: Singh & Grewal 2023 (JMR), Darby, Ketchen, Ball & Mukherjee 2024 (MSOM) × 3
- **生成力**: 待验证
- **排他性**: 中——数据驱动型，特别适合 JM/JMR/MSOM 等实证传统强的期刊
- **期刊限制**: 营销/运营/供应链期刊更欢迎；ASQ 偏好较弱
- **收录状态**: ✓ STANDARD
