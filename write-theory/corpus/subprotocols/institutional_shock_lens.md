# 制度冲击类研究的 Theory Lens 适配

> 外置自 `write-theory/SKILL.md` Phase 2.3 与 Phase 3.2 [2c]。触发条件：Phase 1.3 制度冲击检测命中（IV / DiD / RDD / 自然实验 / 政策冲击信号）。

如果你的研究使用自然实验、制度冲击或准实验设计（IV, DiD, RDD），Theory Lens 段需要额外完成以下论证任务：

#### 1. 制度冲击的 Theory Lens 模板

```
We argue that [policy/shock] alters [actor]'s incentives to [action] by [mechanism].
This setting is particularly informative because [policy] creates exogenous variation in [treatment]
that is plausibly unrelated to [unobserved confounders], allowing us to isolate the causal effect
of [treatment] on [outcome] from [alternative explanations].
```

**三层论证要求**：
- **第一层（外生性）**：说明制度冲击为什么是外生的——对谁来说是外生的？为什么受影响企业的特征不太可能导致制度变化？
- **第二层（机制）**：制度变化如何通过理论机制影响行为？（与标准 Theory Lens 的 why chain 相同）
- **第三层（识别基础）**：为什么这个情境在理论上适合识别因果关系？（见下）

#### 2. 识别策略的理论论证（必须在 Theory 部分完成，不能只在 Methods 中呈现）

**IV 研究的 Theory 要求**：
- 为什么工具变量与结果无直接联系（排除限制）在理论上是成立的？
- 工具变量通过什么理论渠道影响处理变量？（第一阶段不仅是统计要求，更是理论要求）
- 用 1-2 句话在 Theory Lens 段预告："[Instrument] affects [treatment] through [theoretical channel] but does not directly influence [outcome] except via [treatment], because..."

**DiD 研究的 Theory 要求**：
- 为什么处理组和控制组在没有处理时会有平行趋势？（共同趋势假设的理论基础）
- 处理效应的异质性来源在理论上是什么？（Sun-Abraham / Callaway-Sant'Anna 问题的理论预判）
- 用 1-2 句话在 Theory Lens 段预告："Absent the [policy], treated and control firms would have followed parallel trends because [theoretical reason, e.g., they operate in the same product market with similar demand shocks]."

**RDD 研究的 Theory 要求**：
- 为什么断点附近的企业在制度实施前是可比较的？（局部随机化的理论基础）
- 断点两侧的制度差异在理论上是什么？（如 regulatory threshold, eligibility cutoff）

#### 3. 时间动态机制的 Theory 论证（生存分析 / Cox 模型）

如果你的研究使用 Cox 比例风险模型或时间动态分析，Theory 部分需要解释：
- 为什么时间是一个理论上有意义的维度（而非仅仅控制变量）？
- 为什么风险率（hazard rate）的理论比"是否发生"的二元理论更丰富？
- 比例风险假设在理论上为什么合理？（即：协变量对风险率的影响不随时间变化，这一假设在理论上是否可信？）

**生存分析 Theory Lens 句式模板**：
```
We theorize that [treatment] does not merely increase the probability of [event] but
alters the *rate* at which [actor] approaches the [decision threshold]. This temporal
dimension matters because [theoretical reason, e.g., decision-makers face escalating institutional pressure over time, and the hazard of [event] increases non-linearly with exposure to [trigger condition]].
```

---

## 4. why chain 嵌入位置速查（原 Phase 3.2 [2c]）

如果你的研究使用 IV / DiD / RDD，Theoretical Reasoning 部分必须在 why chain 中嵌入对识别假设的理论论证，而非仅在 Methods 中呈现统计假设。

| 识别策略 | 必须在 Theory 中论证的内容 | Theory 嵌入位置 |
|---|---|---|
| **IV** | 为什么工具变量与结果无直接联系（排除限制）在理论上是成立的？工具变量通过什么理论渠道影响处理变量？ | 在 why chain 的 X→M 步骤后插入 1 句："[Instrument] influences [treatment] through [channel] but does not directly affect [outcome] because [theoretical reason, e.g., it operates at the state level while outcomes vary at the firm level]." |
| **DiD** | 为什么处理组和控制组在没有处理时会有平行趋势？处理效应的异质性来源在理论上是什么？ | 在 why chain 开头插入 1 句："Absent [policy], treated and control [units] would have followed parallel trajectories because [theoretical reason, e.g., they face identical demand shocks prior to the regulatory change]." |
| **RDD** | 为什么断点附近的企业在制度实施前是可比较的？断点两侧的制度差异在理论上是什么？ | 在情境描述后插入 1 句："Firms just above and below the [threshold] are observationally similar in [key dimensions] because [theoretical reason], yet they face sharply different [treatment] due to the [institutional rule]." |