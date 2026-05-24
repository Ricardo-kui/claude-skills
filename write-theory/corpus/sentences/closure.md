# 收束/过渡句语料库

## T6 Closure 骨架（准强制）

**功能**：将分散假设整合为统一理论叙事，明确假设间逻辑关系，可选预告实证策略。

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
- 产品召回领域 6/6 篇缺失 T6，为 batch_1 发现的系统性缺陷

---

## 局部收束信号（T6 缺失时的应急策略）

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
- 全文级 T6 仍建议添加，但在多轨道设计中轨道级局部收束提供段落级认知闭合

**与全文 T6 的关系**:
- 轨道级局部收束 ≠ 全文 T6
- 最佳实践: 每条轨道局部收束 + 全文 T6 全局收束
- 次优但可接受: 每条轨道局部收束，全文 T6 在 Discussion 开篇回补
- 高风险: 无轨道级收束且无全文 T6 (singh_grewal2023 模式)

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

## T6 强制阈值规则 (T6 Mandatory Threshold Rule)

**核心规则**: T6 Closure 的必要性随假设数量递增。

| 假设数 | T6 必要性 | 替代策略 | 风险（若缺失） |
|--------|----------|---------|---------------|
| **1-2** | 推荐但非强制 | 最后一个假设的收敛句 + Discussion 开篇补回 | 低——读者可以跟踪 2 个假设间的逻辑关系 |
| **3-4** | **严格强制** | 无替代——必须有独立 T6 段落收束 | 高——审稿人可能批评 "理论碎片化" / "贡献不清晰" |
| **≥5** | **严格强制 + 理论模型图** | 无替代——T6 + Figure 都必需 | 极高——审稿人几乎必定要求添加框架图 |

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

**语料锚定**: shipilov_greve_rowley2019 (SMJ) — 4 假设但 **T6 缺失**，Discussion 开篇补回：'we presented two additional findings—one expected and one unexpected.' 这是 T6 缺失后用 Discussion 追补的典型案例。

**常见 T6 缺失场景与后果**:
| 缺失场景 | 典型表现 | 审稿人反应 |
|---------|---------|-----------|
| 2×2 矩阵 4 假设无 T6 | 最后一个假设 (H2b) 说完后直接进入 Methods | "这些假设之间是什么关系？" |
| 发散树 3 假设无 T6 | H3 末尾只有一个 "Thus" 过渡到 Methods | "整体理论框架的贡献是什么？" |
| 竞争假设 2 假设无 T6 | H2 末尾直接被 Methods 标题打断 | 风险较低——2 假设的对立关系本身即收束 |

**反模式**:
- 用 "In the next section, we describe our methods" 替代 T6 → 这不是收束，是逃避
- T6 只有一句话 "In sum, we have four hypotheses" → 没有理论整合，只是一个数字
- T6 重复每个假设的内容 → 不是整合，是摘要。应说假设间的逻辑关系，不说假设各自的预测

**例外**: SMJ 对 T6 容错度略高于 AMJ/ASQ/OS——但如果假设数≥3且论文的其他方面（如 contribution clarity）也偏弱，缺失 T6 会放大审稿人的负面印象。范例：shipilov_greve_rowley2019 (SMJ) 缺失 T6 但仍发表，因为 Discussion 的 "one expected—one unexpected" 框架有效收束了贡献。但这属于侥幸——不要以此为模板。
