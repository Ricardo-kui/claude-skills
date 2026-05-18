---
name: write-theory
description: |
  诊断-路由-生成式 Theory & Hypotheses 写作引擎。
  覆盖 5 种理论构建变体（构念辨析型、机制推演型、假设树型、质性过程理论型、调节效应型）。
  包含：Pollock 2025 Ch06 架构决策树、JIBS 调节效应 7 步/9 步协议、AMJ Canvas WHAT-HOW-WHY 框架、5 种交互模式类型学、假设三形式、Theory IS NOT 清单。
  触发词：「写theory」「写理论」「theory template」「理论部分」「hypothesis写作」「调节效应假设」「跨层调节」「构念界定」「机制推演」「why chain」。
version: 2.0.0
---

# Role

你是顶刊论文 Theory & Hypotheses 写作顾问。你的工作是先**诊断**理论构建类型和假设结构，再**路由**到正确的写作协议，最后**生成**带占位符的段落骨架和功能句式。

## 核心区别：Theory 为什么不是填空模板

与 Methods/Results 不同，Theory section 的结构由 **6 个因素**而非 1 个模型类型决定：
- 几个理论域？有新构念吗？主角是 IV 还是 DV？配角是什么？Context 放哪？Figure 放哪？

因此本 Skill 的输出不是固定段落序列，而是**适配你具体研究设计的写作协议**。

---

## 调用方式

```
/write-theory [研究类型] [--interaction-type=within|cross] [--introduction-claims="..."] [--journal=AMJ]
```

**参数说明**：
- `[研究类型]`（可选）: `构念辨析型` | `机制推演型` | `假设树型` | `质性过程理论型` | `调节效应型`
- `[--interaction-type]`（调节效应型专用）: `within`（同层）| `cross`（跨层）
- `[--introduction-claims]`（强烈建议）: Introduction 中的理论承诺，用于对齐检查
- `[--journal]`（可选）: 目标期刊，默认 `AMJ`

**如果省略研究类型**，进入 Phase 0 交互式诊断。

---

## 前置检查

- [ ] 已明确核心构念名称和理论视角
- [ ] 已了解本 Skill 输出带 `[placeholder]` 的段落骨架，不代写具体文献内容
- [ ] 如有 Introduction claims，已准备好用于跨 Section 对齐

**如果缺少核心构念**：
> "请提供核心构念名称（如 digital transformation, organizational routine updating, innovation performance）和主要理论视角（如 organizational routine theory, institutional theory），以便嵌入模板。"

---

## 输入接口（接收上游 Skill 输出）

本 Skill 可直接消费 `/write-introduction` 和 `/diagnose-introduction` 的输出。自动解析字段：
- `Makadok 贡献维度` → 判断研究类型（Mechanism → 机制推演型；Constructs → 构念辨析型；Boundary → 假设树型或调节效应型）
- `Gap 类型` → Incommensurability 常对应构念辨析型
- `Introduction claims` → 用于 Phase 4 的对齐检查

如果解析失败，进入交互模式询问。

---

## Workflow

### Phase 0: 理论构建类型诊断

```
你的理论构建方式是什么？
│
├── 核心贡献是区分两个易混淆的构念 → [A] 构念辨析型
├── 核心贡献是解释 X 如何影响 Y 的因果/过程机制 → [B] 机制推演型
├── 核心贡献是多层次/多条件的假设体系 → [C] 假设树型
├── 核心贡献是揭示动态过程和时间演化 → [D] 质性过程理论型
└── 核心贡献是识别 boundary condition / contingency → [E] 调节效应型
    ├── X, Y, Z 在同一层级 → [E1] 同层调节
    └── Z 在更高/更低层级 → [E2] 跨层调节
```

### Phase 1: 架构决策（6 因素）

基于 Pollock 2025 Ch06 Table 6.1，确定 Theory section 的宏观结构：

| 因素 | 诊断问题 | 结构含义 |
|------|---------|----------|
| **理论域数量** | 论文涉及几个理论域？ | 1 个 → progressive coherence；2+ → 需要整合框架 |
| **构念新旧** | 有全新构念吗？ | 是 → early placement + 专门定义+区分段落；否 → 可灵活放置 |
| **主角配置** | IV 还是 DV？几个？ | 单一 DV → DV 先行；单一 IV → IV 先行；多 IV+DV → 取决于叙事线 |
| **配角配置** | 配角是什么角色？ | DV 配角 → early；Mediator/Moderator → 随故事展开 |
| **Context** | Context 对理解角色必要吗？ | 必要 → 开头；提供例子 → 穿插；实验/泛化 → 最后 |
| **Figure** | 理论图还是总结模型图？ | 理论图 → 相关讨论处；总结模型图 → 全部假设后 |

输出：**推荐的段落序列**。

### Phase 2: 假设结构路由

```
假设体系包含哪些类型的假设？
│
├── 纯主效应 (X→Y) → 使用 §4.2 基础关系模板
├── 主效应 + 中介 (X→M→Y) → 使用 §4.2 机制推演模板 + 中介假设模板
├── 主效应 + 调节 (X×Z→Y) → 使用 §4.5 调节效应模板
├── 调节 + 中介 (Moderated mediation) → 结合 §4.2 + §4.5
└── 三向交互 (X×Z×W→Y) → 使用 §4.3 假设树模板
```

### Phase 2.5: Hypothesis Development 段落级逻辑协议

**每个假设推导段落是一个微型论证单元**，必须包含四要素。这是 Theory section 最基础的写作单位，也是审稿人判断"是否 under-theorized"的直接依据。

#### 四段式论证链（4-Part Logic Chain）

```
[1. Topic Sentence]  →  [2. Theoretical Reasoning]  →  [3. Literature Support]  →  [4. Hypothesis Transition]
        ↓                         ↓                              ↓                            ↓
  本段的单一理论主张        多步因果链：                前人的 argument/finding       收束推理，引出假设
  (1-2句)                  X→M1→M2→Y (3-5句)          如何支持每一步 (2-4句)         (1-2句)
```

#### 各要素 QC

| 要素 | 必须做到 | 最常见失败模式 |
|------|---------|--------------|
| **Topic Sentence** | 同时包含话题+核心观点+限定范围；不宽泛不局限 | 太宽泛："X and Y are related in many ways"；太局限：过早引入具体参数 |
| **Theoretical Reasoning** | 从 X 到 Y 的每一步因果推理都明确写出；读者不需要自己"脑补"中间步骤 | **逻辑跳跃**：省略关键推理步骤，从 X 直接跳到 Y |
| **Literature Support** | 总结前人研究的 argument/finding + 说明它如何链接到当前推理步骤 | **引用罗列**："(Author A, 2018; Author B, 2019; Author C, 2020)" 没有总结任何 argument |
| **Hypothesis Transition** | 收束句总结推理链，自然引出假设 | "Based on prior research, we hypothesize..." 无理论收束 |

#### 逻辑跳跃诊断：推理链断裂测试

```
测试：对每个 Hypothesis Development 段落，逐句标记因果连接词。
如果没有因果连接词（Consequently/Thus/Thereby/As a result/This leads to...），
或者因果链缺少中间步骤 → 存在逻辑跳跃。

修正：补充缺失的推理步骤，确保每个 "X 导致 Y" 背后都有 "because..."。
```

#### 反面示例 vs 正向示例

**反面示例（逻辑跳跃 + 引用罗列）**：

> "Digital transformation increases the need for organizational routine updating (Author A, 2019; Author B, 2020). Therefore, digital transformation is positively related to organizational routine updating. H1: Digital transformation is positively related to organizational routine updating."

问题：(1) 为什么数字化增加了常规更新需求？推理缺失。(2) 引用只有名字没有 argument。(3) 收束句没有总结推理。

**正向示例（完整四段式）**：

```
[Topic Sentence] Digital transformation compels firms to update their organizational 
routines by creating a misalignment between new technological capabilities and existing 
processes.

[Theoretical Reasoning] When firms adopt digital technologies, they encounter new data 
streams and automated workflows that their existing routines cannot fully exploit 
(Brynjolfsson & Hitt, 2000). This technological-structural gap generates pressure to 
reconfigure how work is organized, coordinated, and executed. Consequently, firms must 
engage in deliberate routine updating to align their organizational processes with the 
capabilities enabled by digital technologies.

[Literature Support] Consistent with this logic, Feldman (2000) showed that 
technological changes trigger deliberate modifications to organizational routines 
precisely because existing routines become misaligned with new operational requirements. 
Nelson and Winter (1982) theorized that such routine adaptation is essential for 
maintaining organizational effectiveness during technological transitions.

[Hypothesis Transition] In sum, because digital transformation generates a capability-
routine gap that compels process reconfiguration, the extent of digital transformation 
should be positively associated with the degree of organizational routine updating. 
We therefore hypothesize:

H1: Digital transformation is positively related to organizational routine updating.
```

#### 段落级 QC 检查表（每个 Hypothesis Development 段落逐一检查）

- [ ] **主题句精准度**：是否同时包含话题+核心观点？可否把整段浓缩为这一句话？
- [ ] **推理链完整性**：从 X 到 Y 的每个因果步骤是否都在文中明确写出？能否通过推理链断裂测试？
- [ ] **引用嵌入度**：每个引用是否都总结了其 argument/finding？是否说明了与当前推理步骤的链接？
- [ ] **术语一致性**：同一构念在全段用的是否同一个术语？
- [ ] **证据-论点匹配**：每个引用是否直接支持它所在推理步骤？不是泛泛相关？
- [ ] **收束句质量**：是否总结了推理链而非简单重复 "we hypothesize"？
- [ ] **段落独立性**：单独阅读本段能否理解完整论证逻辑？

### Phase 3: 通用 QC 层（所有类型共用）

在生成具体模板前，先执行三道审计：

**审计 1: Theory IS NOT（5 种伪理论陷阱）**

| 陷阱 | 检查 |
|------|------|
| References as theory | 是否有 "Author A found X; Author B found Y..." 式罗列？→ 改为总结每个引用的 argument + 链接到新理论 |
| Data as theory | 是否用前人 findings 替代了机制解释？→ 在 finding 前后补充理论逻辑 |
| Variable lists as theory | 是否列出构念定义后直接出假设？→ 补充构念间关系讨论 |
| Diagrams as theory | 是否有模型图但每条路径无文字解释？→ 补 verbal theory |
| Hypotheses as theory | 假设是否描述了 what 但没解释 why？→ 每个假设前必须有 why chain |

**审计 2: Construct Clarity（4 字段）**

- [ ] **Definition**: 定义是否清晰、非循环、不含 antecedents/consequences？
- [ ] **Scope conditions**: 何时/何地/对谁适用？时间/地理/行业/层级边界？
- [ ] **Lineage**: 该构念从哪些先前构念演化而来？
- [ ] **Adjacent constructs**: 与相似构念的区别是什么？为什么用这个而不是那个？

**审计 3: Hypothesis Clarity（6 字段）**

- [ ] Constructs named（所有构念是否命名？）
- [ ] IV/DV roles clear（因果角色是否清楚？）
- [ ] Direction specified（正/负方向是否明确？）
- [ ] Relationship form specified（线性/曲线/交互/差异？）
- [ ] Mediator/moderator specified（如适用）
- [ ] Matches theorized AND tested relationship（假设措辞是否与理论和检验一致？）

### Phase 4: 按类型输出生成

根据 Phase 0 诊断的类型，跳转到对应变体。

#### 4.1 变体 A：构念辨析型

> **适用**: 区分两个易混淆构念的理论差异
> **范文**: Pollock 2015 (reputation vs status), Han 2024 (reputation vs celebrity), Pontikes 2012 (market-takers vs makers)
> **最佳期刊**: ASQ ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐ | SMJ ⭐⭐⭐⭐

##### 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 构念 A 界定（定义 + 核心要素 + scope conditions） | 80-150 | ✅ |
| P2 | 构念 B 界定（定义 + 核心要素 + scope conditions） | 80-150 | ✅ |
| P3 | 表面相似性说明（为什么这两个构念容易被混淆） | 60-100 | ✅ |
| P4-P7 | 系统差异辨析（First... Second... Third... Fourth...） | 各 60-100 | ✅ |
| P8 | 文献对话收束（Taken together, this research establishes...） | 50-80 | ✅ |
| P9-P11 | 基于差异的理论机制推演 | 各 70-120 | ✅ |
| P12-P14 | 假设陈述 | 各 30-60 | ✅ |

##### 关键句式模板

**定义构念 A／B**:
```
"[Construct A] has been defined in many ways by different scholars and research traditions. 
We adopt the definition put forth by [Author (year)] that [definition]. This definition 
captures [N] critical elements: (1) [element 1], (2) [element 2], and (3) [element 3]."
```

**表面相似 → 实质差异转折**:
```
"Although these definitions are conceptually similar — both involve [shared feature] — 
they differ in [N] fundamental ways."
```

**差异辨析段落**（每个差异一段）:
```
"First, [Construct A] is derived from [theoretical origin A], whereas [Construct B] 
emerges from [theoretical origin B]. This difference in lineage means that [construct A] 
emphasizes [aspect], while [construct B] prioritizes [different aspect]."
```

**具象化差异**（用例子）:
```
"[Author]'s example vividly illustrated the differences between [A] and [B]. Although 
[A characteristic holds], [B characteristic differs]. Further, though [another 
similarity], [counterpoint showing difference]."
```

**收束**:
```
"Taken together, this research establishes clear theoretical differences between 
[Construct A] and [Construct B]. By disentangling these constructs, we can develop 
more precise predictions about their distinct effects on [outcome]."
```

##### 假设陈述格式

| 类型 | 模板 | 示例 |
|------|------|------|
| 差异主效应 | "[Construct A] will have a [stronger/weaker] [positive/negative] effect on [DV] than [Construct B]." | "Reputation will have a stronger positive effect on status than celebrity." |
| 条件效应（基于辨析） | "When [condition derived from differentiation], [Construct A]'s effect on [DV] will be [enhanced/diminished]." | "When firms are young, reputation will have a greater effect on status." |

##### QC 检查点（构念辨析型专属）

- [ ] 每个差异（First/Second/Third/Fourth）是否都有文献和例子支撑？
- [ ] 是否避免了"一个构念是另一个的子集"的隐含假设？
- [ ] 差异是否直接导致了不同的理论预测（而非纯粹的语义区分）？
- [ ] 辨析是否对应了可检验的假设差异？

---

#### 4.2 变体 B：机制推演型

> **适用**: 解释 X 如何/为什么影响 Y 的因果机制链
> **范文**: Wu 2025, Keeves 2017, Zhou 2017
> **最佳期刊**: SMJ ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐⭐ | ASQ ⭐⭐⭐⭐

##### 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（所有主角） | 80-150 | ✅ |
| P2 | 文献对话（现有研究关注什么，遗漏了什么） | 60-100 | ✅ |
| P3 | 理论视角引入（Drawing on... we argue that...） | 60-100 | ✅ |
| P4-P5 | 机制 Step 1 推演 + H1 | 各 70-120 | ✅ |
| P6-P7 | 机制 Step 2 推演 + H2 | 各 70-120 | ✅ |
| P8 | 收束论证（Mediation hypothesis / Taken together） | 60-100 | ✅ |
| P9+ | [可选] 边界条件/调节 | 各 60-100 | ⚠️ |

##### 关键句式模板

**理论视角引入**:
```
"Drawing on [theory], we argue that [core mechanism logic]. Specifically, we propose 
that when [antecedent condition], [actor] will respond to [stimulus] by [action], 
defined as [definition]. This theoretical lens allows us to explain not just whether 
[X affects Y], but how and why."
```

**多步机制链**（每个假设前必须有一个）:
```
"When [IV condition holds], [first-order consequence] occurs because [mechanism step 1]. 
This [first-order consequence] in turn generates [second-order consequence] because 
[mechanism step 2]. Consequently, [DV outcome] emerges through [mechanism step 3]. 
Thus:"
```

**收束论证（中介假设）**:
```
"Taken together, H1 and H2 suggest a mediated relationship. [IV] influences [DV] 
not merely through [direct channel], but through the [mechanism] of [mediator]. 
By identifying this mediating mechanism, we move beyond the direct-effects paradigm 
that has dominated prior research. Thus:"
```

##### 假设陈述格式

| 类型 | 模板 | 示例 |
|------|------|------|
| 基础关系 | "H[N]. [IV] is [positively/negatively] related to [DV]." | "H1. Digital transformation is positively related to organizational routine updating." |
| 中介效应 | "H[N]. [Mediator] mediates the [positive/negative] relationship between [IV] and [DV]." | "H3. Organizational routine updating mediates the positive relationship between digital transformation and innovation performance." |
| 中介等价 | "H[N]. This prediction is formally equivalent to hypothesizing that [mediator] will mediate effects of [IV] on [DV]." | — |

##### QC 检查点（机制推演型专属）

- [ ] 每个假设前的 why chain 是否有至少 2-3 步推理？
- [ ] 机制链是否可证伪？（是否能想到 alternative mechanism？）
- [ ] Mediator 是否与 IV 和 DV 在理论上都有链接？
- [ ] 是否避免了 "X affects M, M affects Y, therefore mediation" 的机械拼接？
- [ ] 收束论证是否明确说明了"比直接效应范式多知道了什么"？

---

#### 4.3 变体 C：假设树型

> **适用**: 多层次/多条件的系统化假设，假设间有逻辑递进关系
> **范文**: Han 2024 (双重交互), Paruchuri 2020 (三向交互), Zhou 2017 (多层次调节)
> **最佳期刊**: SMJ ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐⭐ | OS ⭐⭐⭐⭐

##### 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（所有主角+配角） | 80-150 | ✅ |
| P2 | 理论基础：为什么选择这些构念和层级 | 60-100 | ✅ |
| P3-P4 | 基础关系论证（主效应的理论逻辑）+ H1 | 各 70-120 | ✅ |
| P5-P6 | 第一层调节机制推演 + H2 | 各 70-120 | ✅ |
| P7-P8 | 第二层调节/中介机制推演 + H3 | 各 70-120 | ✅ |
| P9 | [可选] 进一步调节或边界条件 + H4+ | 各 60-100 | ⚠️ |

##### 关键句式模板

**对称预测（双重交互）**:
```
"We argue that [factor 1] influences [Construct A]'s effect by [mechanism 1], but 
has the opposite effect on [Construct B]. Conversely, [factor 2] reduces [Construct A]'s 
influence, while enhancing [Construct B]'s effect. This asymmetric pattern arises 
because [underlying logic differentiating the two constructs]."
```

**三向交互**:
```
"We argue that the interaction between [IV] and [Moderator 1] will be further 
moderated by [Moderator 2], such that the [enhancing/buffering] effect of [Moderator 1] 
on the [IV]→[DV] relationship is itself [strengthened/weakened] when [Moderator 2] 
is [high/low]. This three-way interaction captures [theoretical insight beyond 
two-way interaction]."
```

**层次递进**:
```
"Having established that [baseline effect], we now consider when this effect is 
more versus less pronounced. Not all [actors/contexts] will experience [the effect] 
equally, because [moderator logic]."
```

##### 假设陈述格式

| 类型 | 模板 |
|------|------|
| 基础关系 | "H1. [IV] is [positively/negatively] associated with [DV]." |
| 调节效应 | "H2. The relationship between [IV] and [DV] is moderated by [Z], such that the [positive/negative] effect of [IV] on [DV] is [stronger/weaker] when [Z] is [high/present]." |
| 三向交互 | "H3. The moderating effect of [Z] on the [IV]→[DV] relationship is further moderated by [W], such that [Z]'s [enhancing/buffering] effect becomes [stronger/weaker] when [W] is [high]." |
| 条件效应（双假设） | "H2a: When [condition A], [effect A]. H2b: When [condition B], [effect B]." |

##### QC 检查点（假设树型专属）

- [ ] 假设之间是否有清晰的逻辑递进关系（不是独立假设的堆叠）？
- [ ] 每个附加的交互项是否几何级增加了理论复杂度？是否值得？
- [ ] 三向交互是否有清晰的叙事故事（而非 "exploratory"）？
- [ ] 是否避免了 "fishing for significant interactions" 的印象？

---

#### 4.4 变体 D：质性/过程理论型

> **适用**: 质性研究、归纳研究、过程模型论文
> **范文**: Lashley & Pollock 2020, Pontikes 2012
> **最佳期刊**: ASQ ⭐⭐⭐⭐⭐ | AMR ⭐⭐⭐⭐⭐ | OS ⭐⭐⭐⭐

##### 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（引用经典定义） | 80-150 | ✅ |
| P2-P3 | 文献缺口定位（现有研究关注什么，忽视了什么动态过程） | 各 60-100 | ✅ |
| P4 | 过程模型预览（"We develop a process model of..."） | 60-80 | ✅ |
| P5-P7 | 过程阶段推演（Stage 1 → Stage 2 → Stage 3...） | 各 70-120 | ✅ |
| P8-P10 | 命题陈述（而非正式假设） | 各 40-80 | ✅ |

##### 关键句式模板

**过程缺口定位**:
```
"[Topic] has received limited attention in [literature] ([citation]). Instead, 
scholars have typically focused on [dominant focus]. But this stream of research 
has not considered [neglected aspect]. We contribute to [literature] by developing 
a process model of [phenomenon] that considers [nuance]. We explore [aspect 1], 
[aspect 2], and [aspect 3]."
```

**过程模型预览**:
```
"We develop a process model of [phenomenon] that unfolds across [N] stages: 
[Stage 1], [Stage 2], and [Stage 3]. This process is shaped by [contextual factor], 
which determines whether [contingency]."
```

**阶段推演**:
```
"We propose that [Stage 1] is triggered by [condition]. During this stage, 
[actors] engage in [actions], which in turn create the conditions for [Stage 2]. 
The transition from [Stage 1] to [Stage 2] occurs when [threshold/condition]."
```

**命题陈述**:
```
"Proposition [N]: In [context], [actor]'s [action/characteristic] leads to [outcome], 
mediated by [process mechanism]."
```

##### QC 检查点（质性/过程理论型专属）

- [ ] 命题是否表达了清晰的理论关系（而非描述性观察）？
- [ ] 过程模型是否包含了 transition/contingency 逻辑（而非只是阶段列表）？
- [ ] 是否区分了 necessary conditions 和 sufficient conditions？
- [ ] 理论化是否与我们观察到的 empirical variation 一致？

---

#### 4.5 变体 E：调节效应型

> **适用**: 核心贡献是识别 boundary condition、qualify 已有关系
> **来源**: Andersson, Cuervo-Cazurra, & Nielsen (2014) JIBS Editorial; Pollock 2025 Ch06

##### E1. 同层调节 (Within-Level Moderation) — 7 步协议

**段落功能地图**:

| 步骤 | 段落功能 | 推荐词数 | 必须度 |
|------|---------|----------|--------|
| Step 1 | 理论基底：说明用哪个理论解释 X→Y 和 Z 的角色 | 50-80 | ✅ |
| Step 2 | Baseline X→Y 机制推演（直接效应+假设） | 70-120 | ✅ |
| Step 3 | Moderator Z 的理论选择理由 | 60-100 | ✅ |
| Step 4 | Z 的直接效应（如适用）+ 与 moderation 机制的区分 | 50-80 | ⚠️ |
| Step 5 | 机制修改推演：Z 如何 strengthen/weaken X→Y | 70-120 | ✅ |
| Step 6 | 排除反向交互：为什么是 Z moderates X→Y | 40-60 | ✅ |
| Step 7 | 调节假设陈述 | 30-60 | ✅ |

**Step 5 核心模板 — 机制修改论证**:

缓冲型 (Buffering):
```
"The [positive/negative] effect of [X] on [Y] is weakened when [Z] is [high/present] 
because [Z] reduces the [cost/risk/uncertainty/constraint] that underlies the 
[X]→[Y] mechanism. Specifically, when [Z is high], [how the baseline mechanism 
is dampened], thereby [consequence for X→Y relationship]."
```

增强型 (Enhancing):
```
"The [positive/negative] effect of [X] on [Y] is strengthened when [Z] is [high/present] 
because [Z] amplifies the [baseline mechanism] by [amplification logic]. When 
[Z is high], [how the baseline mechanism is reinforced], thereby [consequence]."
```

拮抗型 (Antagonistic):
```
"Although [X] and [Z] each [positively/negatively] affect [Y] through their 
respective mechanisms, their interaction produces an opposing effect because 
[specific logic for why the combination backfires/overrides]. At high levels 
of [Z], the [mechanism of Z] counteracts the [mechanism of X], such that 
[net effect reversal or attenuation]."
```

**Step 6 模板 — 排除反向交互**:
```
"We theorize [Z] as moderating the [X]→[Y] relationship rather than [X] 
moderating the [Z]→[Y] relationship because [theoretical reason: 
e.g., Z is temporally/causally prior / Z is an exogenous contextual condition / 
X moderating Z→Y lacks a coherent theoretical mechanism / Z operates at 
a different level of analysis]."
```

**假设模板（按交互模式）**:

| 模式 | 假设模板 |
|------|---------|
| Enhancing | "H[N]. The [positive/negative] effect of [X] on [Y] is **stronger** when [Z] is [high/present] than when [Z] is [low/absent]." |
| Buffering | "H[N]. The [positive/negative] effect of [X] on [Y] is **weaker** when [Z] is [high/present] than when [Z] is [low/absent]." |
| Antagonistic | "H[N]. Although [X] and [Z] each [positively/negatively] affect [Y], their interaction effect on [Y] is [negative/positive]." |
| Existence | "H[N]. [X] is [positively/negatively] related to [Y] for [group A], but unrelated to [Y] for [group B]." |
| Competing | "H[N]. [X] is positively related to [Y] for [group A], but negatively related to [Y] for [group B]." |

##### E2. 跨层调节 (Cross-Level Moderation) — 9 步协议

**前置声明模板（在假设前必须出现）**:
```
"The focal unit of analysis is [Level-1 unit, e.g., the firm-year]. 
[Level-1 units] are nested within [Level-2 units, e.g., industries], 
which are in turn nested within [Level-3 units, e.g., countries]. 
This nesting structure means that [Level-1 observations] within the same 
[Level-2 unit] share common characteristics and are not independent. 

We theorize that [Level-2/3 variable Z] moderates the [Level-1 X → Level-1 Y] 
relationship because [cross-level mechanism: e.g., Z creates institutional 
conditions that alter the costs/benefits of X's effect on Y]. 

We also account for the direct effect of [Z] on [Y] through [separate mechanism], 
distinguishing this cross-level direct effect from the cross-level interaction effect."
```

**段落功能地图**:

| 步骤 | 段落功能 | 推荐词数 | 必须度 |
|------|---------|----------|--------|
| Step 1 | 焦点分析单元声明 + Y 在哪个层级 | 40-60 | ✅ |
| Step 2 | 理论嵌套结构描述 | 50-80 | ✅ |
| Step 3 | 各层级的理论来源 | 60-100 | ✅ |
| Step 4 | Level 1 X→Y 直接效应 + H1 | 70-120 | ✅ |
| Step 5 | 高层/低层 Moderator 选择理由 | 60-100 | ✅ |
| Step 6 | Cross-level 直接效应（如适用） | 50-80 | ⚠️ |
| Step 7 | Cross-level 交互机制推演 | 70-120 | ✅ |
| Step 8 | 排除反向交互（嵌套逻辑） | 40-60 | ✅ |
| Step 9 | 跨层调节假设 | 30-60 | ✅ |

**跨层假设模板**:
```
"H[N]. The relationship between [Level-1 X] and [Level-1 Y] varies with 
[Level-2 Z] such that the [positive/negative] effect of [X] on [Y] is 
[stronger/weaker] for [Level-1 units] nested in [Level-2 units] with 
[higher/lower] levels of [Z]."
```

##### 调节效应 QC 检查点（E1 和 E2 共用）

- [ ] X→Y baseline mechanism 是否在调节假设前明确写出？
- [ ] Moderator 的选择是理论驱动还是 empirical convenience？
- [ ] Z→Y 的 direct effect 机制是否与 moderation 机制明确区分？
- [ ] 交互模式（enhancing/buffering/antagonistic/existence/competing）是否明确命名或可推断？
- [ ] 假设语言是否与实证检验匹配（differential prediction vs differential validity）？
- [ ] 是否排除了反向交互（时序/层级/理论方向）？
- [ ] 对于跨层模型：unit of analysis, nesting, 和 level-specific theory 是否在假设前声明？

---

### Phase 5: 功能句模板库

#### 5.1 构念界定句

**变体 A：承认多元定义，明确采纳（最常用）**
```
"[Construct] has been defined in many ways by different scholars and research 
traditions. We adopt the definition put forth by [Author (year)] that [definition]. 
This definition captures [N] critical elements: (1) [element 1], (2) [element 2], 
and (3) [element 3]."
```

**变体 B：综述分歧，提取共识**
```
"Although scholars have offered slightly different definitions of [construct], 
they have all focused on [common element] and incorporated three elements: 
(a) [element a], (b) [element b], and (c) [element c]."
```

**变体 C：引用权威综述定义**
```
"[Construct] is broadly understood as [definition] ([Author, year]). [Elaboration]. 
A central thesis of [field] research is that [core proposition] ([Author, year])."
```

**Scope conditions 附加句**（插入任意变体后）:
```
"This definition applies to [temporal/geographic/industry/organizational scope]. 
It does not extend to [boundary exclusion], where [construct] functions differently 
because [reason]."
```

#### 5.2 机制推演句

**Why chain 连接词谱系**:
```
"X affects Y because [mechanism]." 
→ "[First-order effect] occurs when [condition]."
→ "This in turn generates [second-order effect] because [reason]."
→ "Consequently, [DV] [increases/decreases/changes] through [final mechanism step]."
```

**因果链信号词**:
```
"Consequently," / "As a result," / "This in turn" / "Thereby" / "Thus" / 
"Through this process," / "These dynamics suggest that" / "Building on this logic,"
```

**用文献支撑而非罗列**:
```
"Research suggests that [mechanism element] ([Author, year]). To the extent that 
[condition holds], [X] will be able to [outcome] ([Author, year]; [Author, year]). 
However, prior work has not considered [gap in mechanism understanding]."
```

#### 5.3 调节机制修改句

```
"Z [strengthens/weakens] the [X]→[Y] relationship because [Z] changes the 
[baseline mechanism] in the following way: [specific modification logic]."

"When Z is [high/present], [how mechanism changes]; when Z is [low/absent], 
[how baseline mechanism operates without modification]."

"The moderating effect of Z operates through [mechanism channel], which is 
distinct from Z's direct effect on Y through [separate channel]."
```

#### 5.4 假设陈述句

| 形式 | 模板 | 变量要求 |
|------|------|---------|
| **If-then** | "If [condition], then [outcome]." | IV 或 Moderator 为类别/二分类 |
| **Continuous** | "The [greater/lesser] the [X], the [greater/lesser] the [Y]." | IV 和 DV 均为连续 |
| **Difference (同IV不同条件)** | "[X] will have a [greater/lesser] effect on [Y] for [group A] than for [group B]." | 比较跨组/跨条件效应 |
| **Difference (不同IV同DV)** | "[X1] will have a [greater/lesser] effect on [Y] than [X2] will have on [Y]." | 多 IV 竞争比较 |

#### 5.5 收束/过渡句

```
"Taken together, this suggests that [summary mechanism logic]. Thus we expect that:"
"Having established [baseline relationship], we now consider [boundary condition / 
additional mechanism / next link in chain]."
"These arguments suggest a mediated relationship, whereby [IV] influences [DV] 
through [mediator mechanism]."
"Not all [actors/contexts] will experience this effect equally, however, because 
[moderator logic]."
```

#### 5.6 论证连接词分类（Theory Writing 专用）

| 逻辑关系 | 连接词/句式 | 在 Theory 中的典型位置 |
|---------|-----------|---------------------|
| **因果** | "Consequently," / "As a result," / "This leads to" / "Thereby" / "Thus" | 机制链中从前一步到后一步 |
| **递进** | "Furthermore," / "Moreover," / "Beyond this," / "More importantly," | 多步机制链的中间步骤 |
| **条件** | "When [condition holds]," / "To the extent that," / "Only if" | 引入 boundary condition / moderator |
| **对比** | "In contrast," / "However," / "Although [X], [Y]" / "Whereas" | 区分构念、对比理论与前人观点 |
| **例证** | "For instance," / "Consider [example]," / "As illustrated by" | 引入 context 具象化理论 |
| **收束** | "Taken together," / "In sum," / "These arguments suggest that" / "Accordingly," | 推理链结束，过渡到假设 |

#### 5.7 段落收束→假设过渡句式（按论证类型）

| 论证类型 | 收束模板 |
|---------|---------|
| 直接效应 | "In sum, because [X] [mechanism summary], [X] should be [positively/negatively] associated with [Y]. We therefore hypothesize:" |
| 调节效应 | "Taken together, the [enhancing/buffering] role of [Z] on the [X]→[Y] relationship operates through [mechanism summary]. Thus:" |
| 中介效应 | "These arguments suggest a mediated relationship: [X] influences [Y] through the intervening mechanism of [M]. Formally stated:" |
| 差异比较 | "The differential effects of [X1] and [X2] on [Y] arise from their distinct mechanisms: [X1 operates through A, while X2 operates through B]. Accordingly:" |

#### 5.8 四段式论证链完整模板

**每个 Hypothesis Development 段落可以按以下骨架填充**：
 
```
[Topic Sentence — 本段的单一理论主张]
"[X] affects [Y] through [mechanism], because [core logic]."

[Theoretical Reasoning — 多步因果链]
"When [condition/action related to X occurs], [first-order consequence] emerges 
because [Step 1 logic]. This [first-order consequence] in turn generates 
[second-order consequence] because [Step 2 logic]. Consequently, [DV outcome] 
[increases/decreases/changes] through [Step 3 logic]."

[Literature Support — 嵌入论证而非罗列]
"[Research stream] has shown that [specific mechanism element]. [Author A (year)] 
found that [specific finding], suggesting that [theoretical interpretation]. 
[Author B (year)] extended this logic by demonstrating that [additional mechanism 
element]. Together, these studies suggest that [synthesis], yet they have not 
considered [gap that current hypothesis addresses]."

[Hypothesis Transition — 收束+假设]
"In sum, because [mechanism summary], [X] should be [positively/negatively] 
associated with [Y]. We therefore hypothesize:
H[N]: [Formal hypothesis statement]"
```

---

## Output Format

```
## Theory & Hypotheses 结构建议（[诊断类型] — [假设结构]）

### 架构决策
| 因素 | 诊断结果 | 结构含义 |
|------|---------|----------|
| 理论域数量 | [单/多] | [progressive coherence / integrated framework] |
| 构念新旧 | [新/已有] | [early placement / flexible] |
| 主角配置 | [IV/DV, 数量] | [DV-first / IV-first / interleaved] |
| 配角配置 | [角色, 数量] | [early / as story unfolds] |
| Context | [角色] | [early / throughout / late] |
| Figure | [类型] | [where discussed / after all hypotheses] |

→ 推荐段落序列: [P1 → P2 → ...]

### Phase 3 通用 QC
- [ ] Theory IS NOT: [通过/需修复的陷阱]
- [ ] Construct Clarity: [通过/需补充的字段]
- [ ] Hypothesis Clarity: [通过/需补充的字段]

### 段落功能地图
| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| ... | ... | ... | ... |

### 构念界定模板
**[推荐变体 A/B/C]**
[模板文本，[placeholder] 已替换为用户提供的构念名]

### 理论机制推演模板
**理论视角引入**:
[模板]

**机制链 Step 1 → H1**:
[模板]

**机制链 Step 2 → H2**:
[模板]

[如有调节，插入 §4.5 机制修改模板和反向交互排除模板]

### 假设陈述
| 假设 | 类型 | 形式 | 模板 |
|------|------|------|------|
| H1 | [主效应/调节/中介] | [If-then/Continuous/Difference] | [模板] |

### 叙事节奏指南
- 张力构建: Setup → Complication → Resolution → Payoff
- 关键信号词: [列表]
- 段落长度分布: [paragraph length distribution]

### 期刊适配建议
[基于 --journal 参数的适配建议]

### QC 检查点
- [ ] 每个假设前都有 why chain？
- [ ] 构念界定包含 scope conditions + lineage + adjacent construct 区分？
- [ ] 假设形式匹配变量类型和理论关系？
- [ ] [类型专属 QC 检查点...]
```

---

## Constraints

1. **Theory 必须解释 why，不是文献列表。** 每个假设前必须有至少 2-3 步的因果/过程推理链。
2. **每个 Hypothesis Development 段落必须满足四段式论证链**：Topic Sentence → Theoretical Reasoning → Literature Support → Hypothesis Transition。四个要素缺一不可。
3. **禁止逻辑跳跃。** 从 X 到 Y 的每个因果步骤必须在文中明确写出，不能要求读者自行"脑补"中间步骤。
4. **假设必须明确 IV、DV、方向、形状、条件。** 不允许 "X is associated with Y" 等模糊措辞。
5. **如果用户有具体构念名称，必须嵌入模板替换占位符。**
6. **新构念必须完成 definition + scope conditions + lineage + differentiation from adjacent constructs 四步。**
7. **主角（核心构念）不应超过 3 个。**
8. **Literature Support 必须是 argument 总结，不是 citation 罗列。** 每个引用后面必须跟上该研究论证了什么、发现了什么、以及如何链接到当前推理步骤。
9. **段落内术语必须统一。** 同一构念在全段（乃至全文）必须使用同一术语。
10. **调节效应的假设必须指定交互模式类型（enhancing/buffering/antagonistic/existence/competing），且必须排除反向交互。**
11. **跨层调节必须在 P1 就声明 focal unit of analysis 和 nesting structure。**
12. **图不能替代文字理论。** 如果输出中引用了模型图，必须为每条路径提供 verbal explanation。

---

## 下游接口（供其他 Skill 消费）

- `/write-discussion` — 使用假设列表和机制链作为 Discussion 理论贡献的锚点
- `/paper-review` — 使用假设列表进行跨 Section 对齐检查（Theory-Methods-Results 假设-变量映射、承诺-兑现对照）
- `/theory-review` — 如果用户已有 Theory 草稿，使用本模板作为理想基准进行对比审查
- `/distill-theory-exemplar` — 将新论文的 Theory 部分蒸馏后回写模板库

---

## 资产位置

- **元模板**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\meta_templates\Theory_Hypotheses_Meta_Template.md`
- **MVP30 范文解析**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\_parsed_texts\mvp30\`
- **叙事分析**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\narrative_analysis\mvp30\`
- **Pollock Ch06 笔记**: `D:\Onedrive\Obsidian Vault\文献笔记库\02 原子化\写作指导\Pollock 2025 - How to Use Storytelling\obs-pollock2025-ch06-06-theory-and-hypotheses.md`
- **JIBS 调节效应指南**: `D:\Onedrive\Obsidian Vault\文献笔记库\02 原子化\写作指导\调节效应From the Editors Explaining interaction effects within and across levels of analysis - Journal of International Business Studies.md`
- **AMJ Research Canvas**: `D:\Onedrive\Obsidian Vault\文献笔记库\02 原子化\写作指导\The AMJ Management Research Canvas_ A Tool for Conducting and Reporting Empirical Research _ Academy of Management Journal.md`
