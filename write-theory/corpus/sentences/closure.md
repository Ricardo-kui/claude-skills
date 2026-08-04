# 收束/过渡句语料库

## 全局收束骨架（⚠️ 管理学非标准——不推荐使用）

> **管理学惯例**: JMS, AMJ, SMJ, ASQ, OS 等期刊的 Theory 部分以最后假设为终点，**不要求独立的 Closure 段落**。以下骨架仅供极少数理论密集型 ASQ/ASR 论文参考——且应压缩为恢复整体模型可理解性所必需的最短内容，嵌入最后假设段末尾，而非独立成段。

**功能**（如确实需要）：将分散假设整合为统一理论叙事，明确假设间逻辑关系。

**模板**：
```
"Taken together, our theory posits that [一句话总结核心框架]. [H1/H2] establish 
the baseline [relationship/mechanism], while [H3/H4] identify the boundary conditions 
under which this [relationship/mechanism] is [strengthened/weakened/reversed]. By 
integrating [理论A] with [理论B], we provide a nuanced understanding of [phenomenon] 
that moves beyond the [direct-effects / universal-effects] paradigm dominating prior 
research. We test these predictions using [简要实证策略]."
```

**语料锚定**：
- 产品召回领域 6/6 篇无独立 Closure 段，确认为管理学标准做法

---

## 局部收束信号（管理学标准做法）

**主效应假设群末尾**：
```
"In summary, these arguments suggest that [core mechanism]."
```

**调节假设群末尾**：
```
"In sum, [moderator] systematically [strengthens/weakens] the [relationship] 
through [unifying mechanism]."
```

**Discussion 开篇补回**：
```
"Our theory posited a [结构描述] framework comprising [N] hypotheses that..."
```

---

## 轨道级局部收束 (Track-Level Local Closure)

**适用**: 双轨/多轨并行 Theory 中，每条轨道独立收束后再转入下一条轨道

**模板 (Track A 收束→H)**:
```
"In summary, [core mechanism of Track A] reduces [actors]' reliance on [behavior type], shifting the focus away from [short-term orientation]. Therefore:
- Hypothesis [N]a: [prediction for DV1]
- Hypothesis [N]b: [prediction for DV2]
```

**语料锚定**:
- malik_wang_martin_gomezmejia2025 (JM) — Track B (prospective wealth) 末尾: "In summary, high prospective wealth reduces CEOs' reliance on short-term IM tactics that may fail as additional information emerges over time, shifting the focus away from current wealth preservation. Therefore: H2a... H2b..."
- singh_grewal2023 (JMR) — H1 末尾 "Thus, if lobbying facilitates preferential treatment, we should observe..."

**关键特征**:
- "In summary" 仅收束当前轨道，非全文收束
- 后接 "Therefore:" 直接收敛到该轨道的假设
- 每条轨道末尾可独立使用此模式
**与全文收束的关系**:
- 轨道级局部收束 ≠ 全文收束
- 管理学标准: 每条轨道局部收束后直接进入下一条轨道或 METHODS（如 malik_wang_martin_gomezmejia2025 JM, singh_grewal2023 JMR）
- 可选: 如假设间逻辑关系不够自明，可在最后假设段末尾嵌入最短必要的框架总结
- 非标准: 独立的全文 T6 段落

---

## 过渡句

```
"Taken together, this suggests that [summary mechanism logic]. Thus we expect that:"
"Having established [baseline relationship], we now consider [boundary condition / 
additional mechanism / next link in chain]."
"These arguments suggest a mediated relationship, whereby [IV] influences [DV] 
through [mediator mechanism]."
"Not all [actors/contexts] will experience this effect equally, however, because 
[moderator logic]."
```

## 识别策略论证嵌入（即使非 IV/DiD/RDD 设计）

**适用**: Theory 假设因果时，识别策略的理论论证应嵌入最后假设推导段或自然过渡句中，非独立 Closure 段落。

**模板**:
> "Given the endogeneity concerns inherent in [actor]-[organization] matching, we employ [method] to control for [threat type]. Specifically, [method details] allow us to [identification claim]. We also conduct [robustness check type] to address [remaining threat]."

**语料锚定**:
- wang2024 (SMJ) — **反面教材**: 使用面板数据 + GEE，但 Theory 中完全未讨论识别策略（未讨论 CEO 自选择、未论证 GEE 选择的理论依据、未讨论固定效应如何控制时间不变混淆因素）。审稿人可能质疑："如果高 PA 的 CEO 本身就被 CSR 导向的公司任命，你的 GEE 估计能解决这个问题吗？"

**关键规则**:
- **内生性来源必须被命名**: CEO-firm matching、自选择、反向因果、遗漏变量——至少明确提及一个
- **控制方法必须有理论依据**: 不仅是 "we use FE"，而是 "firm fixed effects control for time-invariant unobserved heterogeneity such as corporate culture"
- **即使非因果设计也要讨论**: 如果论文明确是 "correlational study"，也需在最后假设推导段末尾声明识别限制

**反模式**:
- Theory 中完全忽略识别策略 → 审稿人质疑因果推断的可信度
- Methods 中突然出现识别策略讨论但 Theory 中未铺垫 → 读者感到突兀
- 只写 "we control for endogeneity" 但不具体说明如何控制 → 空话

---

## 段落收束→假设过渡（按论证类型）

| 论证类型 | 收束模板 |
|---------|---------|
| 直接效应 | "In sum, because [X] [mechanism summary], [X] should be [positively/negatively] associated with [Y]. We therefore hypothesize:" |
| 调节效应 | "Taken together, the [enhancing/buffering] role of [Z] on the [X]→[Y] relationship operates through [mechanism summary]. Thus:" |
| 中介效应 | "These arguments suggest a mediated relationship: [X] influences [Y] through the intervening mechanism of [M]. Formally stated:" |
| 差异比较 | "The differential effects of [X1] and [X2] on [Y] arise from their distinct mechanisms: [X1 operates through A, while X2 operates through B]. Accordingly:" |
| 竞争假设 | "Given these competing arguments, we put forth the following hypotheses for how [X] may influence [Y]:" |

---

## H1 收敛信号强制提醒

**反模式**: H1（或任何一个假设）直接从机制段落末尾出现，缺少显式 "Therefore" / "Thus" / "Accordingly" 收敛连接词。假设看似从天而降，而非从机制推导中自然产生。

**检测信号**:
- 假设前一句是 citation 或事实陈述，而非因果收束句
- 假设句与前一机制句之间无逻辑连接词
- 读者若只看假设句和它前面的句子，无法判断假设是从哪个机制推导出来的

**修复模板**（机制推演型 H1）:
```
"Following this discussion, we propose that [core mechanism summary]. [Optional: one-sentence
restatement of why the mechanism leads to the predicted direction].

Therefore, we hypothesize:
H1: [IV] is [direction] related to [DV]."
```

**语料锚定**: 发现于 park_lange_jeon (SMJ) H1 — Hypothesis 1 直接从 Section 2.3 段落末出现，前一句为 "Our prediction allows for both of those motivations." 无显式收敛信号。SMJ 格式可能允许此模式，但在 AMJ/ASQ/OS 中会触发审稿人 "假设推导不透明" 评论。

**例外**: SMJ 允许假设无 "Therefore" 前缀使用完整句子格式（"Hypothesis 1. [Statement]."）——但这样做的 paper 通常在假设前一至两句有收敛信号，而非完全缺失。

**强制规则**:
- 机制推演型 + AMJ/ASQ/OS 目标 → beat3→4 连接词为 **强制**
- 机制推演型 + SMJ/JM 目标 → beat3→4 连接词为 **推荐但非强制**，但收敛信号必须存在于假设前 2 句内

---

## 假设数-收敛策略参考 (Hypothesis Count vs Convergence Strategy)

> **管理学惯例**: 不要求独立 Closure 段。以下为局部收束策略参考，而非 T6 强制规则。

| 假设数 | 收敛策略 | 替代策略 |
|--------|----------|---------|---------------|
| **1-2** | 局部收束即可（最后假设的 "Therefore" 收敛） | 低——读者可跟踪 2 个假设间的逻辑 |
| **3-4** | 局部收束 + 可选框架图 | 中——确保每个假设的推导顺序清晰，假设间过渡明确 |
| **≥5** | 局部收束 + 推荐理论模型图 | 中——框架图帮助读者跟踪多假设关系，但不要求独立 Closure 段 |

**模板（≥3 假设通用）**:
```
"Taken together, our theoretical framework suggests that [core insight — 1 句话].
The [2×2 / parallel / tree / chain] structure of our hypotheses captures [theoretical
architecture description]: [H-group-1] establish [baseline logic], while [H-group-2]
extend this logic to [new domain/source/level/condition]. By integrating [theory A]
insights on [mechanism A] with [theory B] insights on [mechanism B], we provide a
[more complete/nuanced/contingent] understanding of [phenomenon] than prior research,
which [focused exclusively on / treated uniformly / assumed linearly] [limit of prior
work]. We test these predictions using [brief empirical strategy reference]."
```

**语料锚定**: shipilov_greve_rowley2019 (SMJ) — 4 假设无独立 Closure 段，Discussion 开篇以 'one expected—one unexpected' 框架整合发现。管理学惯例允许在 Discussion 而非 Theory 末尾完成框架整合。

**常见假设收束模式**（管理学标准——最后假设后直接进入 METHODS）:
| 缺失场景 | 典型表现 | 审稿人反应 |
|---------|---------|-----------|
| 2×2 矩阵 4 假设 | 最后一个假设 (H2b) 后直接进入 Methods | 管理学标准——每个假设的局部收束即可 |
| 发散树 3 假设 | H3 末尾 "Thus" 过渡到 Methods | 管理学标准——假设间的递进关系即理论框架 |
| 竞争假设 2 假设 | H2 后直接 Methods | 低风险——2 假设的对立关系本身即收束 |
| 双理论+多调节 6 假设 | 最后一个假设后直接 Methods | 管理学标准——理论模型图可作为整合工具替代 Closure 段 |

**实例：kalaignanam2017 (JM)**:
- **论文**: Kalaignanam, Kushwaha & Swartz (2017), Journal of Marketing
- **结构**: 2 个 baseline 假设 + 4 个调节假设 = 6 假设，最后假设后直接进入 Data 部分
- **结果**: 论文正常发表——管理学审稿人接受"局部收束+框架图"的整合方式，未要求独立 Closure 段
- **补救可能**: 如果 Discussion 开篇能有效整合（如 "Our findings reconcile the trade-off between..."），可部分弥补。但 JM 通常允许较紧凑的 Theory 结构，风险低于 ASQ/OS。

**如果确实需要嵌入框架总结（少数情况），避免以下写法**:
- 用 "In the next section, we describe our methods" 替代框架总结 → 没有整合
- 只有一句话 "In sum, we have four hypotheses" → 没有理论整合，只是一个数字
- 重复每个假设的内容 → 是摘要而非整合。应说假设间的逻辑关系，不说假设各自的预测
- shipilov_greve_rowley2019 (SMJ) 在 Discussion 开篇完成框架整合，这是管理学惯例允许的做法——不是"侥幸"，是标准操作。

---

## 按架构类型的整合建议（非强制）

> **管理学惯例**: 不要求独立 Closure 段。以下为按推理架构的**可选整合策略**——当假设间逻辑关系不够自明时，可在最后假设段末尾嵌入最短必要的框架总结，而非添加独立段落。

**核心**: 不同推理架构的假设间逻辑自明程度不同。矩阵型和 Y-shaped 架构的假设关系对读者最不透明，嵌入简短框架总结的收益最高。

| 推理架构 | 嵌入框架总结的收益 | 理由 | 无总结的风险 |
|---------|-------------------|------|---------|
| **线性因果链** | 低 | 链式逻辑自包含，假设间递进关系即理论框架 | 低——读者可跟踪因果链 |
| **发散树** | 中 | 分叉关系可通过过渡句暗示 | 低——分叉点在最后一个共同假设处已交代 |
| **2×2 矩阵** | **高** | 对角线对称性和整体矩阵逻辑读者无法自行拼凑 | 中——审稿人可能问 "how do these 4 hypotheses relate?" 但非致命（han_pollock_paruchuri SMJ 仍发表） |
| **Y-shaped** | **高** | 非对称设计的 rationale 需被显式说明 | 中——审稿人可能问 "why no contingencies on H1 side?" 但非致命（toh_pyun SMJ 仍发表） |
| **双轨并行** | 中 | 两条轨道的对称/反向关系可通过轨道级局部收束交代 | 低——malik_wang_martin_gomezmejia2025 JM 用 mini-closure 替代 |

**语料锚定**:
- han_pollock_paruchuri (SMJ): 2×2 矩阵 4 假设, 无框架总结 → 仍发表
- toh_pyun (SMJ): Y-shaped 5 假设, 无框架总结 → 仍发表
- malik_wang_martin_gomezmejia2025 (JM): 双轨 4 假设, 用轨道级局部收束替代 → 仍发表

**2×2 矩阵嵌入总结模板**（嵌入最后假设段末尾，只保留必要整合，非独立段落）:
```
"Taken together, our 2×2 framework reveals a [diagonal symmetry / cross-pattern]: 
[IV dimension 1]'s effect is [strengthened/weakened] by [moderator A] but 
[weakened/strengthened] by [moderator B], while [IV dimension 2] exhibits the opposite 
pattern. This diagonal symmetry underscores that [core theoretical insight about why 
the two IVs respond differently to the two moderators]."
```

**Y-shaped 嵌入总结模板**（嵌入最后假设段末尾，只保留必要整合，非独立段落）:
```
"Taken together, our Y-shaped framework suggests that while [IV] unambiguously 
[benefits/harms] [Group A] by [mechanism], its effect on [Group B] is contingent on 
[Group B]'s competitive position in [complementary domain]. Specifically, [H2's main 
effect] is [accentuated/attenuated] when [amplifying conditions] and 
[buffered/offset] when [Group B] possesses [buffering factors]. This asymmetric 
architecture highlights that [core insight about why Group A is unaffected by the 
contingencies that matter for Group B]."
```

**注意——这些不是"反模式"，而是管理学标准做法**:
- 2×2 矩阵 4 假设后直接进入 Methods（han_pollock_paruchuri SMJ）→ **正常发表**。假设的局部收束承担了收敛功能。
- Y-shaped 5 假设后直接进入 Methods（toh_pyun SMJ）→ **正常发表**。非对称设计的 rationale 在假设推导中已说明。
- 如果审稿人确实追问假设间关系，可在 Discussion 开篇回应——这比在 Theory 末尾附加独立 Closure 段更符合管理学惯例。

---

## 倒U型调节假设的局部收束

**功能**: 在 moderator 段落末尾用 "Taken together" 收束两侧机制，明确 flatten/steepen 预测。

**模板（flatten）**:
```
"Taken together, as [moderator] between [actor] and [partner] increases, [actor]'s incentive to [DV] is reduced at low to medium levels of [IV], while [actor]'s [cost of DV] is increased at medium to high levels of [IV]. Thus, at both sides of the inverted U-shape, the effect of [IV] on [DV] is reduced as [moderator] increases. The slope in the relationship between [IV] and [DV] is likely to be less steep when [moderator] is higher, and the peak lower."
```

**模板（steepen）**:
```
"Taken together, [incentive] is enhanced at low to medium levels of [IV], while [cost] is reduced at medium to high levels of [IV]. Thus, at both sides of the inverted U-shape, the effect of [IV] on [DV] is enlarged by [moderator]. The slope is likely to be steeper, and the peak higher."
```

**语料锚定**:
- Cui, Yang & Vertinsky (SMJ) — H2/H3/H4 每个 moderator 段末尾的 Taken together 收束。

**关键特征**:
- 重复 "at both sides of the inverted U-shape" 强化双侧论证。
- 从 mechanism 到 curvature prediction 的过渡自然。
- 直接后接假设形式化。

**反模式**:
- 用 "In sum, we have four hypotheses" 替代机制整合。
- 收束句只重复假设内容，不总结假设间逻辑关系。
