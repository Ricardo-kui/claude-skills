# 假设陈述句语料库

## 假设形式决策矩阵（Form–Measurement Match）

**核心原则**：假设形式必须同时匹配（1）构念的测量尺度、（2）理论关系的形状、（3）所宣称的理论概念类型（如 differential prediction vs. differential validity）。三者不一致是审稿人判定“假设措辞与理论错位”的常见原因（Pollock 2025, Ch06; Andersson et al. 2014, JIBS）。具体统计检验由 `write-methods` 选择。

### 1. 测量尺度 → 基础形式速查表

| IV 测量尺度 | DV 测量尺度 | 关系形状 | 推荐形式 | 模板句 | 禁用/弱形式 |
|---|---|---|---|---|---|
| 二分类 / 类别 | 连续 / 二分 | 线性 | **If-then** | "[Group A] will have [higher/lower] [Y] than [Group B]." | "X is associated with Y"（无方向） |
| 连续 | 连续 | 线性 | **Continuous** | "The [greater/lesser] the [X], the [greater/lesser] the [Y]." | 用 If-then 表达连续变化 |
| 连续 | 连续 | 曲线（U 型 / 倒 U 型） | **Curvilinear** | "[X] has a [positive-then-negative / negative-then-positive] relationship with [Y], peaking at [moderate X]." | 拆成两个线性假设 |
| 连续 | 连续 | 边际递减 | **Diminishing** | "[X] is positively related to [Y], but at a decreasing rate." | 仅用 linear 形式 |
| 连续/类别 | 连续/二分 | 跨组差异 | **Difference** | "[X] will have a [greater/lesser] effect on [Y] for [A] than for [B]." | 用主效应形式掩盖跨组比较 |
| 多 IV | 同一 DV | 相对影响 | **Relative comparison** | "[X1] will have a [greater/lesser] effect on [Y] than [X2]." | 分别陈述 H1、H2 但不比较 |

### 2. 调节效应形式决策表

| IV 尺度 | Moderator 尺度 | 理论含义 | 形式 | 假设中应突出的概念 | 假设模板 |
|---|---|---|---|---|---|
| 连续 | 连续 | 同向放大 | Enhancing | slope/nature 改变 | "The [positive/negative] effect of [X] on [Y] is **stronger** when [Z] is high." |
| 连续 | 连续 | 反向削弱 | Buffering | slope/nature 改变 | "The [positive/negative] effect of [X] on [Y] is **weaker** when [Z] is high." |
| 连续 | 连续 | X 与 Z 同向但交互反向 | Antagonistic | slope/nature 改变 | "Although [X] and [Z] each [positively/negatively] affect [Y], their interaction is [negative/positive]." |
| 连续 | 二分类/类别 | 关系仅在一组存在 | Existence | 跨组 slope 差异 | "[X] is [positively/negatively] related to [Y] for [A], but unrelated for [B]." |
| 连续 | 二分类/类别 | 关系方向翻转 | Competing | 跨组 slope/nature 翻转 | "[X] is positively related to [Y] for [A], but negatively for [B]." |
| 连续 | 连续/类别 | 改变关系强度（r 而非 slope） | Differential validity | strength/correlation 改变 | "The [strength/correlation] of the [X]–[Y] relationship is [greater/lesser] when [Z] is high." |

**关键区分**（Andersson et al. 2014）——这是**理论层面**的区分，具体统计检验由 `write-methods` 根据设计选择：
- **Differential prediction**：Z 改变 X→Y 的 *nature/slope*；假设中应出现 "effect... is stronger/weaker/changes" 等 slope 语言。
- **Differential validity**：Z 改变 X→Y 的 *strength/correlation*；假设中应出现 "correlation/strength" 语言，不能用 slope 语言描述。

> **边界提示**：`write-theory` 只要求作者在假设中明确自己提出的是 differential prediction 还是 differential validity；`write-methods` 负责选择对应的统计检验（如 MMR、分组回归、subgroup correlation comparison 等）。

### 3. 关系形状与措辞匹配

| 理论形状 | 推荐动词/短语 | 示例 |
|---|---|---|
| 线性正向 | "is positively related to" / "increases" | H1. CEO narcissism increases strategic risk-taking. |
| 线性负向 | "is negatively related to" / "reduces" | H2. Board independence reduces earnings management. |
| 倒 U 型 | "has an inverted-U-shaped relationship with" / "peaks at moderate" | H3. Competitive intensity has an inverted-U-shaped effect on innovation. |
| U 型 | "has a U-shaped relationship with" / "lowest at moderate" | H4. Slack has a U-shaped relationship with R&D investment. |
| 边际递减 | "is positively related to... but at a decreasing rate" | H5. Firm size increases diversification, but at a decreasing rate. |
| 阈值/阶梯 | "becomes positive once [X] exceeds [threshold]" | H6. Green investment improves performance only when institutional pressure exceeds a threshold. |
| 条件/必要 | "Given [condition], [prediction]" | H7. Given high market turbulence, decentralization improves adaptation. |

### 4. 假设形式 QC 检查清单

- [ ] IV/DV 的测量尺度是否与假设形式一致？（连续变量不用 if-then；分类变量不用 continuous 形式）
- [ ] 理论关系形状是否在假设中明确？（线性/曲线/条件/阈值）
- [ ] 调节假设是否区分了 differential prediction 与 differential validity，且措辞与概念类型一致？
- [ ] 是否存在 "X is associated with Y" 等无方向、无形式的模糊措辞？
- [ ] 假设编号（H1a/H1b 或 H1/H2）是否反映了理论结构而非随意分组？
- [ ] 每个假设是否都能从文中 why-chain 直接推导，而非仅在图/表中存在？

---

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

**原文锚点** (Han, Pollock & Paruchuri, SMJ "Public enemies?"):
> "This leads to our baseline expectation that both reputation and celebrity enhance misconduct scandalization's likelihood." ... "However, we further argue that differences in reputation and celebrity's sociocognitive content lead them to vary in when and why they attract attention and are newsworthy, resulting in different effects on the extent to which the media scandalizes a firm's misconduct."

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

**原文锚点** (Malik, Wang, Martin & Gomez-Mejia 2025, JM "Mixed Gambles in Product Recalls"):
> "Hypothesis 1a: The greater a CEO's current option wealth, the higher the likelihood that the recall is initiated on an inattentive day." ... "Hypothesis 1b: The greater a CEO's current option wealth, the higher the likelihood of strategic silence (i.e., press releases not mentioning product recalls)." ... "Hypothesis 2a: The greater a CEO's prospective option wealth, the lower the likelihood that the recall is initiated on an inattentive day."

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
| **序列中介（统计形式）** | "H[N]. [IV] is [positively/negatively] related to [DV] through the sequential mediators [M1] and [M2]." |
| **序列中介（叙事打包式）** | "H[N]. [Group A / high-X actors] exhibit [direction] [M1] and therefore [perceive/evaluate] [M2] as [direction], resulting in [direction] [DV]." |

**序列中介两种措辞对比**：序列中介（X→M1→M2→Y）可用两种句式陈述——
- **统计形式**（"through the sequential mediators M1 and M2"）：精确、AMJ/ASQ 风格，但要求读者已知 PROCESS Model 6；
- **叙事打包式**（"exhibit M1 and therefore M2, resulting in DV"）：用 "and therefore / resulting in" 把两步因果链打包成一句可读假设，SMJ/JM/JCR 风格，Theory→Methods 过渡更丝滑（读者在 Theory 阶段无需懂 PROCESS 即可理解机制）。

**语料锚定**：
- Wu 2025 (OrgSci) — digital transformation → routine updating → innovation
- Ilicic & Brennan 2026 (JM) — H2: "Conservatives (vs. liberals) exhibit a greater sense of agency and therefore perceive addictive products as less dangerous, resulting in more favorable consumer responses"（叙事打包式序列中介 X→agency→danger→responses）

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

**原文锚点** (Eilert, Jayachandran, Kalaignanam & Swartz 2017, JM "Does It Pay to Recall Your Product Early?"; Darby et al. 2023, MSOM "CEO Stock Ownership, Recall Timing, and Stock Market Penalties"):
> "H3: The higher a brand's diversification, the stronger the relationship between problem severity and time to recall." ... "The recall-slowing effect of CEO stock ownership is stronger for high-severity recalls than for low-severity recalls."

---

## 分组调节

| 形式 | 模板 | 示例 |
|------|------|------|
| **分组差异** | "H[N]. The [positive/negative] effect of [X] on [Y] will be [stronger/weaker] for [W=A] than for [W=B]." | H2. Spillover effect stronger for manufacturing defects than design defects. |
| **分组方向差异** | "H[N]. [X] is [positively/negatively] related to [Y] for [W=A], but [unrelated/positively/negatively] related to [Y] for [W=B]." | H3. Effect exists for high-severity but not low-severity recalls. |

**语料锚定**：
- Darby 2024 (MSOM) — severity 分组
- Darby 2025 (JSCM) — defect type 分组

**原文锚点** (Darby et al. 2025, JSCM "An Agency Theory Perspective on Activist Investors and Supply Chain Failures"; Darby et al. 2023, MSOM):
> "H2. The spillover effect of activist investor stock ownership on time-to-recall will differ for design-related defects and manufacturing-related defects, such that the recall-quickening effect is stronger for design-related defects relative to manufacturing-related defects." ... "H3. The spillover effect of activist investor stock ownership on time-to-recall will differ for high-severity and low-severity recalls, such that the recall-quickening effect is stronger for high-severity recalls relative to low-severity recalls."

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

**原文锚点** (Wowak et al. 2025, Management Science "The Politics of Product Safety: Top Management Team Political Ideology and Serious Medical Product Recalls"):
> "Hypothesis 1(a). There is a negative relationship between top management team liberalism and the count of recalls." ... "Hypothesis 1(b). There is a positive relationship between top management team liberalism and the count of recalls."

### 单一非定向调节（Nondirectional Competing Moderator）

**适用**: 两套对立动机/注意力理论对**同一个**调节效应给出相反方向，但不拆成 H[N]a/H[N]b；用单一 "stronger or weaker" 假设把裁决交给证据。

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **Nondirectional competing moderator** | "H[N]. The [positive/negative] relationship between [X] and [Y] is **stronger or weaker** for [units] with higher [Z] than for [units] with lower [Z]." | 连续/类别调节；理论给出两套相反动机，不预先选边 |

**收敛信号（用 Given，不用 Therefore）**:
```
"Given the presence of equivocal arguments for the moderating effect of [Z], we propose a nondirectional hypothesis:"
```

**语料锚定**:
- kalaignanametal2013 (JM) — H4 prior brand quality 对 recall magnitude → future reliability

**原文锚点** (Kalaignanam, Kushwaha & Eilert 2013, Journal of Marketing):
> "Given the presence of equivocal arguments for the moderating effect of prior brand quality, we propose a nondirectional hypothesis"

> "The positive relationship between recall magnitude and future product reliability is stronger or weaker for brands with higher prior quality than for brands with lower prior quality."

**与竞争假设对的区别**:
- 竞争假设对（Wowak）是两个方向相反的**主效应** H[N]a/H[N]b
- 本形式是**一个**调节假设内部保留方向开放；Results 用交互符号裁决，不得在 Theory 用 Therefore 收束

**反模式**:
- 把 2013 H4 写成 E3 的定向 "stronger/weaker when high/low"
- 在 Theory 段用 Results 发现（"brands with lower prior quality improve... to a greater extent"）替换非定向假设句

---

## 矩阵假设（多 IV × 多 DV）

| 形式 | 模板 |
|------|------|
| **Matrix** | "H[N]a: [X1] → [Y1] (+). H[N]b: [X1] → [Y2] (+). H[M]a: [X2] → [Y1] (-). H[M]b: [X2] → [Y2] (-)." |

**语料锚定**：
- Malik 2025 (JM) — current/prospective × timing/silence × media 2×2×2 矩阵

**原文锚点** (Malik, Wang, Martin & Gomez-Mejia 2025, JM "Mixed Gambles in Product Recalls"):
> "Hypothesis 1a: The greater a CEO's current option wealth, the higher the likelihood that the recall is initiated on an inattentive day." ... "Hypothesis 2a: The greater a CEO's prospective option wealth, the lower the likelihood that the recall is initiated on an inattentive day." ... "Hypothesis 3a: The positive relationship between a CEO's current option wealth and recall initiation on an inattentive day is weaker (less positive) with more negative media coverage."

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
- Lun et al. 2026 (ETP) — stronger (weaker) when late-stage (early-stage)
- Liu, Liu & Luo 2016 (JM) — enhanced (reduced) when cash (equity)

---

## 括号异号双调节句（parenthetical opposite-signed dual moderator，liuliuluo2016 型）

**适用**: 两个方向相反的 moderator 调节同一条基线斜率；把异号对收进一条交互假设，避免拆成 H5a/H5b 两句。

```
"The [negative/positive] impact of [X] on the likelihood of [DV] is enhanced (reduced) when the [actor] receives greater [W_short] ([W_long]) [incentive]."
```

**原文锚点** (Liu, Liu & Luo 2016, JM):
> "The negative impact of product value on the likelihood of full remedy is enhanced (reduced) when the CEO receives greater cash (equity) compensation."

**与三向 parenthetical 的区分**: 三向模板是 stronger (weaker) when A (B) 的两极情境；本模板是两个异号 moderator 一次写出对同一斜率的增强/削弱。

**禁忌**: 两个 W 必须理论方向相反；不要用于同号调节对；不要把括号当成 a/b 配对主效应。

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

---

## 散文编号假设 (Prose Numbered Hypothesis，SMJ 风格)

**适用**: SMJ 风格的假设——完整句子散文格式，带编号但不使用 "is positively related to" 的标准句式

**模板**:
```
Hypothesis H[N]. For a [firm type / condition], [IV] [reduces/heightens/increases/decreases] 
[DV] [scope condition].
```

**语料锚定**:
- toh_pyun (SMJ) — "Hypothesis H1. For a standard-owner-firm, standardization reduces uncertainty over its future financial performance in the ecosystem." / "Hypothesis H2. For a non-standard-owner-firm, standardization heightens uncertainty over its future financial performance in the ecosystem."
- han_pollock_paruchuri (SMJ) — "Hypothesis 1. The positive relationship between high reputation and misconduct scandalization strengthens as objective misconduct severity increases."

**关键特征**:
- 每个假设含: IV direction (reduces/heightens / strengthens/weakens) + firm type/condition + DV + scope condition
- 散文句式而非 "X is positively/negatively related to Y"
- "For a [type]..." 前置——先锚定适用对象, 再给预测方向
- SMJ 允许 H1 直接跟在收敛句后，不一定需要 "Therefore" 前缀

**与标准格式的区别**:
| | 散文编号 (SMJ) | 标准编号块 (AMJ/ASQ) |
|---|---|---|
| 句式 | 散文完整句 | "X is positively related to Y" |
| 收敛信号 | 可选 (段落末尾自然过渡) | 必须 (Therefore/Thus) |
| 期刊偏好 | SMJ, OS | AMJ, ASQ, JM |

---

## 调节假设矩阵格式 (Moderation Hypothesis Matrix，2×2 专用)

**适用**: 2×2 矩阵型 Theory，4 个假设全部为同一关系的调节

**模板**:
```
H1: [IV A] × [Moderator A] → [DV] (+)  [positive moderation]
H2: [IV B] × [Moderator A] → [DV] (-)  [negative moderation — opposite of H1]
H3: [IV A] × [Moderator B] → [DV] (-)  [negative moderation]
H4: [IV B] × [Moderator B] → [DV] (+)  [positive moderation — opposite of H3]
对角线对称: H1↔H4 (同方向), H2↔H3 (同方向)
```

**语料锚定**: han_pollock_paruchuri (SMJ) — reputation/celebrity × objective/perceived severity

**原文锚点** (Han, Pollock & Paruchuri, SMJ "Public enemies?"):
> "Hypothesis 1. The positive relationship between high reputation and misconduct scandalization strengthens as objective misconduct severity increases." ... "Hypothesis 4. The positive relationship between celebrity and misconduct scandalization strengthens as perceived misconduct severity increases."

**关键特征**:
- 4 个假设全部为调节 (无双主效应假设)
- 对角线对称 (H1↔H4 positive, H2↔H3 negative)
- 需在最后一个假设段落的局部收束句中显式总结对角线 pattern（不设独立 T6 收束段）
