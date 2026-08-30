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


### 变体 B：实施权变从句假设形式（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "[X] will [engender positive Y], whether or not [the substantive practice] is implemented."
> "[Comparative form:] [X] with [A] will engender more positive [Y] than [X] without [A], whether or not [the substantive practice] is implemented."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), H1（§2.1 末）与 H2（§2.2 末）；全节 6/6 假设复用同尾从句

**原文锚定**:
> "LTIP adoption will engender positive stock market reactions, whether or not the plan is implemented."
> "LTIP adoption with an agency explanation will engender more positive stock market reactions than LTIP adoption without an agency explanation, whether or not the plan is implemented."

**关键特征**:
- "whether or not [it] is implemented" 尾从句把核心构念（decoupling）写进假设语法本身：每个假设同时是主预测 + decoupling 判别检验的复合声明，理论-构念-设计三位一体
- 从句方向不变（主效应在实施与否两种条件下均成立）——正是"符号行动独立于实质实践起效"这一理论命题的形式化，假设语法即理论主张
- 比较式变体（H2: with X than without X）在同一尾从句上叠加符号形式的对照，扩展假设族而不破坏统一语法

**适用**: 核心构念是"形式与实质分离"（decoupling/ceremony/window dressing）的研究；任何需要在假设层面内置处理-不处理对照的符号机制论文

**禁忌**: 尾从句必须在 Methods 有对应分组检验（采纳未实施子样本），否则是空转修辞；若理论不承诺符号机制独立于实施起效，从句方向应随理论改为条件式

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

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
| **Comparative main effect (策略/极点对)** | "[Strategy A] is more [negatively/positively] related to [DV] than [Strategy B]." | 同一 continuum 两端（或两类策略）对**同一 DV** 的相对方向；非相对零的简单主效应 |

### Comparative Main Effect（比较型主效应；VERIFIED）

<!--
pattern_id: comparative_main_effect_hypothesis_form
build_type: 机制推演型 / 纯主效应
source: chenganesanliu2009
source_papers: ["Chen_Ganesan_Liu_2009_JM"]
confidence: medium
status: VERIFIED
note: VERIFIED（expert_audit_override 2026-08-29 召回主题单源裁决，chenganesanliu2009 = 召回策略→财务价值）；配套架构 audience_foil_then_focal_signal_single_H
-->

**适用**: IV 是两类策略/响应极点的比较（非连续量相对零点）；理论预测是 **A 相对 B 更负/更正**，而非 "A is negatively related to Y" 的简单方向句。

**验证状态**: VERIFIED（召回主题单源裁决，chenganesanliu2009）

**模板**:
```
H[N]. [Strategy A] is more negatively related to [DV] than [Strategy B].
```

**收敛前缀（可选）**:
```
Therefore, we propose that [strategy A] will receive greater [evaluator] attention
and be interpreted as a signal of [severe downside], so [DV] is affected more
negatively when [A] than when [B].
```

**原文锚点** (Chen, Ganesan & Liu 2009, JM):
> "Proactive product-recall strategies are more negatively related to the firms' financial value than passive product-recall strategies."

**语料锚定**：
- Chen, Ganesan & Liu (2009, *JM*) — proactive vs passive → firm financial value（比较型单 H）

**与邻近形式的判别**:
| 本形式 | Difference（跨组效应） | 简单主效应 |
|--------|----------------------|------------|
| 比较两个 **IV 极点/策略** 对同一 DV | 同一 IV 在不同 **group/condition** 上的效应强弱 | "[IV] is negatively related to [DV]"（相对零） |
| 常接 foil→focal 单 H 架构 | 常接调节/分组设计 | 无对照极点时用 |

**反模式**:
- 有明确对照极点却写成相对零的简单方向句，丢失比较信息
- 把比较句误写成调节假设（"effect stronger for A than B" 若 A/B 是 IV 水平而非 W）

**原文锚点** (Han, Pollock & Paruchuri, SMJ "Public enemies?"):
> "This leads to our baseline expectation that both reputation and celebrity enhance misconduct scandalization's likelihood." ... "However, we further argue that differences in reputation and celebrity's sociocognitive content lead them to vary in when and why they attract attention and are newsworthy, resulting in different effects on the extent to which the media scandalizes a firm's misconduct."

**语料锚定**：
- Han 2024 (AMP) — reputation vs celebrity 差异主效应

---




### 句式 D：双部分调节+中介假设句（westphal_bednar2005 型）

**模板**:
> "Hypothesis N: (a) When [baseline], the greater [W], the less [actors] will [misconceive]; (b) this relationship will be mediated by [a greater tendency for actors to M]."
> "Hypothesis N: (a) The relationship between [X] and [Y] will be negatively moderated by the extent to which [W]; (b) this interaction will be mediated by a reduced tendency for [actors] to [M]."

**来源**: westphal_bednar2005 (ASQ), H3/H4（mediated moderation）与 H5（moderated mediation）

**原文锚定**:
> "(b) this relationship will be mediated by a greater tendency for outside directors to express their concerns about corporate strategy."
> "(b) this interaction will be mediated by a reduced tendency for outside directors to express concern about corporate strategy in board meetings."

**关键特征**:
- (a) 陈述关联（调节/交互），(b) 用固定句式 "this relationship/interaction will be mediated by..." 把中介钉进同一条假设——调节与中介的统计检验对象在假设文本中一一对应
- H3/H4（被中介的调节）与 H5（被调节的中介）共用 (a)+(b) 句法但中介对象不同（relationship vs interaction），句法同一而统计结构有别，读者靠 (a) 句型即可分辨
- "negatively moderated by the extent to which..." 把调节方向压进假设措辞，交互项方向无需读者回查机制段

**适用**: 同时含调节与中介的混合假设结构（mediated moderation / moderated mediation）；需要单个假设编号覆盖两条统计路径的论文

**禁忌**: (b) 的中介变量必须是前文已独立论证的行为/状态，不得在假设句首次引入；主循环若只检验 (a) 不检验 (b)，假设应拆分而非合并

### 句式 E：行为缺失→误判强化的比较假设句（westphal_bednar2005 型）

**模板**:
> "Hypothesis N: When [baseline condition], the less [actors] have [expressed their concerns], the greater the tendency for [actors] to [underestimate shared concerns]."

**来源**: westphal_bednar2005 (ASQ), H2

**原文锚定**:
> "the less outside directors have expressed their concerns about the current corporate strategy, the greater the tendency for directors to underestimate the extent to which fellow directors share their concerns"

**关键特征**:
- "the less... the greater..." 比较级对偶句把"行为的缺失量"直接映射到"误判的强度"，中介机制（不表达→误读）在假设句法内部显形，无需额外中介假设
- 保留 "When [baseline condition]" 前置条件，使机制假设（H2）寄生在主效应情境（H1）之内，形成假设间的层级依赖
- DV 用 "tendency to underestimate" 而非二元事件，保证与 H1 的 DV 完全同构，两个假设可在同一模型中检验

**适用**: 机制中介假设（表达缺失强化误判）；DV 为连续程度型构念且自变量为行为频率/缺失的论文

**禁忌**: 比较级假设要求两个构念都可连续测量，类别变量不适用；"the less... the greater" 内嵌方向，机制段推理方向必须与之一致，不得假设句反向于推理

### 变体 A：T4_did_contrast_hypothesis（moon2026）

**模板/骨架**:
> "We expect that [treatment event] in [unit] is likely to lead to [directional change in outcome] of [treated units], as compared to [control units]. Formally: H[N]: [A unit exposed to treatment X increases its Y following X]."

来源：Moon et al. (2026, Journal of Marketing)。


## 变体 C：时间分阶增量假设（t-Staged Delta Hypothesis，what_changes_after_women_enter_top_manage_2020 型）

**验证状态**: VERIFIED (expert_audit_override 2026-08-29: 用户点名喜爱本篇，单源足矣)

**模板**（三位一体）:
```
[全模型时间戳句]
from [period] to [period], the nature of [X] causes changes in [M] that,
later, alter [Y].

[中介主效应增量假设]
Hypothesis [N]. When [X events] occur within [unit], following [X-typed]
(but not [baseline-typed]) [X events], there is a subsequent increase/decrease
in the [unit]'s [M].

[第二阶增量配对假设]
Hypothesis [N+1]. Following [X events], the greater the increase/decrease
in [M], the greater the subsequent increase/decrease in [Y].
```

**Figure 配套**: 总模型图以时间戳编码各段增量——[ΔX: t1–t0] / [ΔM: t2–t1] / [ΔY: t3–t2]，假设编号锚定在对应时间箭头上。

**原文锚定**: "Hypothesis 6. Following female TMT appointments, the greater the
increase in TMT change orientation, the greater the subsequent increase in
R&D." / "from year to year, the nature of new TMT appointees (their gender)
causes changes in TMT cognitions that, later, alter the pathway to strategic
renewal" / Figure 1: "CHANGE IN TMT GENDER COMPOSITION (t1–t0) | CHANGE IN TMT
COGNITION (t2–t1) | CHANGE IN RENEWAL STRATEGY (t3–t2)"

**为什么有效**:
- 把中介假设写成**变化量假设**（Δ-form）而非水平假设：中介的合法性来自"认知真的动了"，与面板年度增量设计直接咬合
- "the greater the change in M, the greater the subsequent change in Y" 同时是中介与强度预测——一句话完成 mediation 与 dose-response 双重主张
- 时间戳 (t1→t2→t3) 使因果排序显式化：反向因果（ΔY→ΔX）被设计排除，且静态悖论（两种相反认知共存）转为"先后作用于不同路径"的动态消解——时间排序承担 reconciliation 的因果化功能
- "(but not baseline-typed)" 内嵌对照：假设句自身携带安慰剂对照预测

**适用条件**:
- 面板/分阶数据可得（各变量可在不同时点测量变化）——非分阶设计不可套用 Δ-form
- IV 是离散事件（任命/冲击/政策）且事件类型可分对照（typed events）
- 适合 Incommensurability R3 消解型模型：时间分阶+路径匹配共同承担悖论消解

**禁忌**: Δ-form 要求正文真的测量变化量——若只有水平数据，退回普通中介句式，不可伪装增量；"subsequent" 一词依赖时间分阶真实成立，时点重叠时不可用；typed 对照（but not X）须在实证中真的检验，否则为空头对照。



### 分离编号回指竞争对（Anaphoric Disjoint-Numbered Competing Pair，zajac_westphal_2004 型）

<!--
pattern_id: hypothesis_sign_flip_anaphoric_pair_sentence
build_type: 竞争假设型
source_papers: ["zajac_westphal_2004_asr"]
confidence: medium
status: VERIFIED
verification_basis: "expert_audit_override (Westphal 系裁决: 用户点名最爱学者,引言/理论单源足矣)"
-->

**适用**: 两个竞争假设各有整节独立推演（非相邻段落）时，用独立编号 H[N] / H[N]a + 回指收敛短语显式绑定；两个假设陈述句逐字相同、仅方向词相反——"同一可观测量、反号预测"的公平配对。

**模板**:
```
Hypothesis [N]. The number of [firms] that have [adopted, but not implemented, X] is negatively associated with [Y] at the focal firm.
...
Hypothesis [N]a. The number of [firms] that have [adopted, but not implemented, X] is positively associated with [Y] at the focal firm.
```

**收敛信号（回指式，非 Therefore）**:
```
"Thus, in opposition to Hypothesis [N], [rival B perspective] leads to the following hypothesis:"
"This suggests the following alternative to Hypothesis [N]:"
```

**原文锚点** (Zajac & Westphal 2004, ASR):
> "The number of firms that have adopted, but not implemented, stock repurchase plans is negatively associated with the stock market reaction to repurchase plan adoption at the focal firm."（H2；H2a 同句仅 negatively→positively）

**与相邻 a/b 竞争对（Wowak 型）的区分**:
| | 相邻编号 H[N]a/H[N]b | 分离编号 H[N]/H[N]a |
|---|---|---|
| 推导布局 | 两方机制相邻段落对称展开 | 每方各自整节（或多段）推演 |
| 绑定方式 | 编号即绑定 | 回指短语（in opposition to / alternative to） |
| 适用 | 轻量竞争（各一段） | 重量级竞争（各一节） |

**禁忌**: 回指短语不可省略；两陈述句除方向词外必须逐字对称，任何一方加料都会破坏公平配对；方向词必须真正反号（negatively/positively）——"减弱/增强"不构成竞争对（应路由 E 调节）。

<!-- wb:zajac_westphal_the_social_construction_of_market_value:hypothesis_sign_flip_anaphoric_pair_sentence -->

### 句式 F：假设推导内嵌前提声明句（westphal_bednar2005 型）

**模板**:
> "Here, we assume a [non-linear] relationship between [X] and [private concern], such that [Y] will be generally low when [X above threshold] and generally high when [X below threshold]. This assumption is consistent with theory and research on [topic], which suggests that [substantive claim] ([citation]; see also [citations])."

**来源**: westphal_bednar2005 (ASQ), Theory P8（H1 推导内）

**原文锚定**:
> "Here, we assume a non-linear relationship between firm performance and directors' private concern about strategy"
> "This assumption is consistent with theory and research on aspiration levels, which suggests that managers are 'boundedly rational decision makers'"

**关键特征**:
- 前提不藏进脚注：在假设推导的节骨眼上用 "Here, we assume..." 显式声明关键前提（绩效→关切的非线性/阈值关系），随即用独立文献传统（aspiration levels）担保
- "such that [low when above] and [high when below]" 用对称双向陈述把阈值行为说满，防止 reviewer 追问中间区间
- 前提声明与其文献担保绑定出现（"This assumption is consistent with..."），声明与引证零距离

**适用**: 假设依赖未经假设化的前提（阈值、非线性、单调性）时的推导内声明；aspiration/threshold 类行为假设

**禁忌**: 内嵌前提的文献担保必须是成熟理论传统，临时拼凑的担保会被视为补丁堆叠；一篇 Theory 内嵌声明至多一两处，多处使用说明前提应升级为独立假设

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


### 边际内嵌 DV 假设句式（wowak_2020_female_directors_recalls）

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

假设句的 DV 措辞直接编码决策边际：whether 边际用 `count of [low-severity recalls]`，when 边际用 `the time-to-recall for [high-severity recalls]`。读者无需回到机制段即可分辨两个不可互换的决策窗口，且防止把结果误读为"召回总体增加/普遍更快"。

```
H1: An increase in [X] is positively associated with the count of [low-stakes acts].
H2: An increase in [X] is negatively associated with the time-to-[act] for [high-stakes acts].
```

**原文锚点**: "An increase in female board representation is negatively associated with the time-to-recall for high-severity recalls."

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
