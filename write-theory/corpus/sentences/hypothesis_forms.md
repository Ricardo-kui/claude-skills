# 假设陈述句语料库

## 基础关系

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **If-then** | "If [condition], then [outcome]." | IV 或 Moderator 为类别/二分类 |
| **Continuous** | "The [greater/lesser] the [X], the [greater/lesser] the [Y]." | IV 和 DV 均为连续 |

---

## 差异比较

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **Difference (同IV不同条件)** | "[X] will have a [greater/lesser] effect on [Y] for [group A] than for [group B]." | 比较跨组/跨条件效应 |
| **Difference (不同IV同DV)** | "[X1] will have a [greater/lesser] effect on [Y] than [X2] will have on [Y]." | 多 IV 竞争比较 |

**语料锚定**：
- Han 2024 (AMP) — reputation vs celebrity 差异主效应

---

## 配对假设 (Paired Hypotheses a/b Format)

**适用**: 多 DV 设计中同一 IV 对两个 DV 产生相同方向的预测——使用 a/b 配对保持 2×N 矩阵的可读性

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **Paired (同IV双DV)** | "H[N]a: The [greater/lesser] the [IV], the [higher/lower] the likelihood of [DV1]. H[N]b: The [greater/lesser] the [IV], the [higher/lower] the likelihood of [DV2]." | 2+ DV，同一 IV，预测方向相同 |
| **Paired (调节-同IV双DV)** | "H[N]a: The [positive/negative] relationship between [IV] and [DV1] is [weaker/stronger] with more [W]. H[N]b: The [positive/negative] relationship between [IV] and [DV2] is [weaker/stronger] with more [W]." | 同一 moderator × IV，2+ DV |

**语料锚定**:
- malik_wang_martin_gomezmejia2025 (JM) — H1a/H1b (current wealth → timing/silence), H2a/H2b (prospective wealth → timing/silence), H3a/H3b, H4a/H4b

**关键特征**:
- a/b 编号暗示两个假设共享理论机制但应用于不同 DV——读者预期两个假设同时成立或同时不成立
- DV 角色必须在 T1-T3 中已明确区分（如 "strategic timing is proactive, strategic silence is passive"）
- 如果两个 DV 的预测方向相反，改用独立编号 (H1, H2) 而非配对 (H1a, H1b)

**反模式**:
- a/b 配对但两个 DV 的机制差异从未被论证 → 审稿人质疑 "why separate hypotheses?"
- a/b 配对但一个假设显著一个不显著 → Discussion 需要解释为什么机制对 DV1 成立对 DV2 不成立

---

## 条件假设 (Conditional "Given..." Hypothesis Format)

**适用**: 理论预测仅在特定条件同时满足时才成立——假设语法直接嵌入边界条件

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **单条件** | "Given [condition], [prediction]." | 条件作为 hypothesis 的前置限定 |
| **双条件交叉** | "Given [condition A], [prediction about B]." / "Given [condition B], [prediction about A]." | 两个假设互相引用对方条件，形成逻辑闭环 |

**语料锚定**:
- paruchuri_pollock_kumar2019 (SMJ) — H1: "Given the salience of the event, a firm's differentiation-based capability failure will have a positive reputation spillover on highly associable category members." H2: "Given category members' high associability, the lower the salience of the differentiation-based capability failure the weaker the positive reputation spillover."

**关键特征**:
- "Given..." 将 moderator/boundary condition 直接嵌入假设语法——不是 "X moderates the relationship" 而是 "当 condition 满足时, X → Y"
- 两个假设交叉引用对方条件: H1 以 "[condition from H2]" 为前提, H2 以 "[condition from H1]" 为前提
- 假设数量少 (仅 2 个) 但每个假设浓缩了多重理论推导
- 适合 "联合必要性" 逻辑——两个条件必须同时满足 (AND gate)

**与传统调节假设的区别**:
| | 条件假设 (Given...) | 传统调节假设 |
|---|---|---|
| 边界条件位置 | 嵌入假设语法内部 | 作为独立变量 (W) 出现在形式化假设中 |
| 条件关系 | AND gate (联合必要) | 连续调节 (W 增强/减弱 X→Y) |
| 适用场景 | 理论的必要前提条件 | 理论的 contingent effect |

**反模式**:
- "Given" 条件过于宽泛 (如 "Given the importance of..." ) → 条件必须有理论定义的边界
- 两个假设的交叉引用不闭合 (如 H1 引用 H2 的条件但 H2 未引用 H1) → 交叉引用必须对称

---

## 中介效应

| 形式 | 模板 |
|------|------|
| **主效应** | "H[N]. [IV] is [positively/negatively] related to [DV]." |
| **中介效应** | "H[N]. [Mediator] mediates the [positive/negative] relationship between [IV] and [DV]." |
| **中介等价** | "H[N]. This prediction is formally equivalent to hypothesizing that [mediator] will mediate effects of [IV] on [DV]." |

**语料锚定**：
- Wu 2025 (OrgSci) — digital transformation → routine updating → innovation

---

## 调节效应

| 形式 | 模板 |
|------|------|
| **Enhancing** | "H[N]. The [positive/negative] effect of [X] on [Y] is **stronger** when [Z] is [high/present] than when [Z] is [low/absent]." |
| **Buffering** | "H[N]. The [positive/negative] effect of [X] on [Y] is **weaker** when [Z] is [high/present] than when [Z] is [low/absent]." |
| **Antagonistic** | "H[N]. Although [X] and [Z] each [positively/negatively] affect [Y], their interaction effect on [Y] is [negative/positive]." |
| **Existence** | "H[N]. [X] is [positively/negatively] related to [Y] for [group A], but unrelated to [Y] for [group B]." |
| **Competing** | "H[N]. [X] is positively related to [Y] for [group A], but negatively related to [Y] for [group B]." |

**语料锚定**：
- Eilert 2017 (JM) — enhancing 型
- Darby 2024 (MSOM) — existence 型（severity 分组）

---

## 分组调节

| 形式 | 模板 | 示例 |
|------|------|------|
| **分组差异** | "H[N]. The [positive/negative] effect of [X] on [Y] will be [stronger/weaker] for [W=A] than for [W=B]." | H2. Spillover effect stronger for manufacturing defects than design defects. |
| **分组方向差异** | "H[N]. [X] is [positively/negatively] related to [Y] for [W=A], but [unrelated/positively/negatively] related to [Y] for [W=B]." | H3. Effect exists for high-severity but not low-severity recalls. |

**语料锚定**：
- Darby 2024 (MSOM) — severity 分组
- Darby 2025 (JSCM) — defect type 分组

---

## 竞争假设

| 形式 | 模板 | 示例 |
|------|------|------|
| **竞争假设对** | "H[N]a: [X] is [negatively/positively] related to [Y]. H[N]b: [X] is [positively/negatively] related to [Y]." | H1a: Liberalism → fewer recalls. H1b: Liberalism → more recalls. |

**收敛信号（非 Therefore）**：
```
"Given these competing arguments, we put forth the following hypotheses for 
how [X] may influence [Y]:"
"Because both arguments are theoretically plausible, we empirically test:"
```

**语料锚定**：
- Wowak 2025 (MS) — H1a/H1b 竞争假设对

---

## 矩阵假设（多 IV × 多 DV）

| 形式 | 模板 |
|------|------|
| **Matrix** | "H[N]a: [X1] → [Y1] (+). H[N]b: [X1] → [Y2] (+). H[M]a: [X2] → [Y1] (-). H[M]b: [X2] → [Y2] (-)." |

**语料锚定**：
- Malik 2025 (JM) — current/prospective × timing/silence × media 2×2×2 矩阵

---

## 极简假设陈述 (Minimalist Hypothesis Statement)

部分期刊/论文使用斜体句子作为假设，而不采用正式的 "Hypothesis N: [IV] is positively related to [DV]" 编号格式。

**示例**：
```
"_CEO stock ownership is positively associated with the time-to-recall..._"
```

**语料锚定**：
- Darby 2023 (MSOM) — italicized hypotheses without formal numbering

---

## 三向交互

| 形式 | 模板 |
|------|------|
| **Three-way** | "H[N]. The moderating effect of [Z] on the [IV]→[DV] relationship is further moderated by [W], such that [Z]'s [enhancing/buffering] effect becomes [stronger/weaker] when [W] is [high]." |

**语料锚定**：
- Paruchuri 2020 (SMJ) — 三向交互范式

---

## 斜体散文条件反转对（Prose Italic Conditional Pair，paruchuri_pollock_kumar2020 型）

**适用**: 两个条件化假设共享相同的理论要素但条件反转——H1: "Given A, B→DV"; H2: "Given B, A→DV"。使用斜体散文格式保持论证流的连续性(SMJ/OS风格)

**模板**:
```
We therefore hypothesize,
Hypothesis [N]. *Given [condition A], [prediction about condition B influencing DV in specific direction].*

...

We therefore hypothesize,
Hypothesis [N+1]. *Given [condition B], the [lower/higher] [condition A] the [weaker/stronger] [DV].*
```

**语料锚定**: paruchuri_pollock_kumar2020 (SMJ) — H1: "Given the salience of the event, a firm's differentiation-based capability failure will have a positive reputation spillover on highly associable category members." / H2: "Given category members' high associability, the lower the salience of the differentiation-based capability failure the weaker the positive reputation spillover."

**关键特征**:
- **"Given [A], [B→DV]. Given [B], [A→DV]."** → 条件反转但不冗余——两个假设分别聚焦不同条件的主导角色
- **斜体散文而非编号块格式** — 假设是论证段落的有机收敛，非分离声明块
- **"We therefore hypothesize," 后接 Hypothesis N. *斜体句*** — SMJ紧凑风格
- 每个假设是完整段落论证的自然终点，而非突兀插入

**与标准编号块格式的区别**:
| | 斜体散文格式 | 标准编号块格式 |
|---|---|---|
| 假设位置 | 嵌入段落末尾 | 独立段落 |
| 格式 | *斜体散文句* | 正体编号 + 正体陈述 |
| 期刊偏好 | SMJ, OS | AMJ, ASQ, JM |
| 论证流 | 不打断 | 更正式、更可见 |

**反模式**:
- 条件反转变为冗余("Given A, B matters. Given B, A matters." 无方向差异) → 合并为一个假设
- 两个条件实际上测量同一构念的不同侧面 → 审稿人质疑"这难道不是同一个东西？"
- 只用斜体娱乐性地标记假设但无"Given"条件结构 → 失去条件反转的逻辑对称性
