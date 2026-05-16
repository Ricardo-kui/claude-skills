# Headline News / Current-Day Event Contrast Hook

## 功能定义
用一个近期真实新闻事件（国会调查报告、内部文件曝光、权威媒体报道）作为叙事入口，通过"当日新闻"的时效性和道德冲击力建立问题的现实紧迫性，再从事件的具体对比制造理论张力。

## 句法模板

**模板 A（政策调查报告型）**：
```
A [year] [authoritative source] report, examining [controversial event], alleged [misconduct] by [actor] ([citation]). It cited an internal [organization] document (dated [date]), in which [official] highlighted several "[wins]," such as [specific gain 1], [specific gain 2], and realizing [monetary savings] ([citation]). Yet [theoretical puzzle: why does this pattern persist, and what mechanism explains it?]
```

**模板 B（媒体报道型）**：
```
A recent story in [media outlet] reports [newsworthy organizational decision]. In the article, [analyst/authority] considers [reaction]. However, the article goes on to say that [underlying motivation]. Clearly, [topic] is a strategic decision with ramifications for [perspective 1] and [perspective 2].
```

## 例句（来自 MVP30）

**来源**：Singh & Grewal 2023 (JMR); Shi et al. 2021 (JMR, variant)

> "A [year] [authority] report, examining [event], alleged [phenomenon] by [actor] ([citation]). It cited an internal [organization] document (dated [date]), in which [official] highlighted several '[wins],' such as [specific gain 1], [specific gain 2], and realizing [monetary savings] ([citation])."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | JMR, JM 极度适合；SMJ 可用但需更快转入理论问题 |
| **理论类型** | 制度理论/非市场战略/监管研究——任何具有公共政策维度的研究 |
| **前提条件** | 新闻事件必须真实可查且有权威来源（国会报告、SEC文件、权威媒体） |
| **风险** | 新闻过时会削弱冲击力；事件如果过于 localized，国际 reviewer 可能不熟悉其背景 |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 新闻装饰化 | 新闻事件精彩但与后续理论无关 | 事件中必须包含至少一个行为，该行为直接对应后文的核心机制 |
| 事件过于陈旧 | "A 2005 report..."（超过15年） | 尽量使用 5-10 年内的热点事件；更早事件需搭配近期数据趋势 |
| 无理论回收 | 新闻冲击后直接跳到文献综述 | 必须在第二段立刻将新闻转化为理论问题 |
| 只有丑闻无制度机制 | 只描述事件但未展示它是系统性/制度性现象 | 用多行业/多事件的普遍性证明 |

## 验证状态
- **跨论文复现**: ⚠️ SINGLE-INSTANCE
- **来源论文**: Singh & Grewal 2023 (JMR) × 1; 类似变体见于 Shi et al. 2021 (JMR)
- **生成力**: 待验证
- **排他性**: 高——仅适用于具有公共政策/监管/消费者安全维度的研究
- **期刊限制**: JMR/JM 高度偏好；SMJ 需更快切入战略理论；不适用于 ASQ 纯理论型论文
- **收录状态**: 🔬 EXPERIMENTAL

## 相关语料
- 配合 `stakes/02-quantified-economic-loss.md`：将新闻事件的 monetary savings 转化为经济显著性
- 配合 `tensions/03-structural-blindspot.md`：新闻事件暗示的现象可能与某一理论视角预测相反
