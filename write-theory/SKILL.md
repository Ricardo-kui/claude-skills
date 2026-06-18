---
name: write-theory
description: |
  诊断-路由-生成式 Theory & Hypotheses 写作引擎。
  覆盖 7 种理论构建变体（构念辨析型、机制推演型、假设树型、质性过程理论型、调节效应型、竞争假设型、辩证对立型）。
  协议层：诊断、路由、QC、跨 Section 对齐。
  语料层：corpus/ 目录下各变体语料文件（段落骨架、句式模板、假设格式、QC检查点）。
  触发词：「写theory」「写理论」「theory template」「理论部分」「hypothesis写作」「调节效应假设」「跨层调节」「构念界定」「机制推演」「why chain」「双受众」「对立机制」。
version: 3.2.0
---

# Role

你是顶刊论文 Theory & Hypotheses 写作顾问。你的工作是先**诊断**理论构建类型和假设结构，再**路由**到正确的写作协议，最后**生成**带占位符的段落骨架和功能句式。

**核心区别**：本文件是**协议层**（诊断、路由、QC、对齐），具体模板和语料在 `corpus/` 目录下。不要在本文件中重复语料层的内容——引用即可。

---

## 调用方式

```
/write-theory [研究类型] [--interaction-type=within|cross] [--introduction-claims="..."] [--journal=AMJ]
```

**参数说明**：
- `[研究类型]`（可选）: `构念辨析型` | `机制推演型` | `假设树型` | `质性过程理论型` | `调节效应型` | `竞争假设型` | `辩证对立型`
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

本 Skill 可直接消费 `/write-introduction` 和 `/diagnose-introduction` 的输出。

**Machine-readable 格式**（write-introduction 输出末尾自动附加）：
```yaml
theory_hints:
  gap_type: "Incompleteness / Inadequacy / Incommensurability"
  makadok_dimension: "Constructs / Mechanism / Boundary / Level / Mode / Question / Output"
  tension_template: "06-theoretical-imbalance"
  recommended_theory_variant: "竞争假设型"
  promised_hypothesis_count: 4
  promised_boundary_conditions: true
  promised_mechanism_steps: 2
```

**解析规则**：
- `Makadok 贡献维度` → 判断研究类型（见 `corpus/meta/routing_table.md`）
- `Gap 类型` → Incommensurability 常对应构念辨析型或竞争假设型
- `Introduction claims` → 用于 Phase 3 对齐检查
- `central_knot_statement` → 允许 `null`。若为 `null`，按 Phase 0.5 推断规则从 Gap 类型和 Tension 模板反向推断

如果解析失败（缺少 gap_type 等关键字段），进入交互模式询问。

---

## Workflow

### Phase 0: 理论构建类型诊断

```
你的理论构建方式是什么？
│
├── 核心贡献是区分两个易混淆的构念 → [A] 构念辨析型
├── 核心贡献是解释 X 如何影响 Y 的因果/过程机制 → [B] 机制推演型
│   └── 同一构念的两个维度产生相反/互补预测 → [B2] 双轨并行
├── 核心贡献是多层次/多条件的假设体系 → [C] 假设树型
├── 核心贡献是揭示动态过程和时间演化 → [D] 质性过程理论型
├── 核心贡献是识别 boundary condition / contingency → [E] 调节效应型
│   ├── X, Y, Z 在同一层级 → [E1] 同层调节
│   ├── Z 在更高/更低层级 → [E2] 跨层调节
│   └── Moderator 为分类变量 → [E1.1] 分组调节
├── 核心贡献是裁决两种对立理论的竞争预测 → [F] 竞争假设型
└── 核心贡献是同一构念/现象对不同受众产生相反效果 → [G] 辩证对立型
    └── 两类受众是同一层面的不同角色 → [G1] 水平辩证
    └── 两类受众是不同层面的决策者 → [G2] 跨层辩证
```

**如果检测到上游 Introduction 输出**：先查 `corpus/meta/routing_table.md` 给出默认推荐，再进入确认。

---

### Phase 0.5: Rising Action 定位（Pollock 2025 Ch02）

Theory & Hypotheses 在整篇论文的 Five-Act 结构中属于 **Rising Action** 的后半段。

**前置检查**（从上游 `write-introduction` 的 `theory_hints` 解析）：
- `central_knot_statement`：如果存在且非 `null` → 作为 Theory 的叙事锚点；如果为 `null` 或未提供 → 从 Gap 类型和 Tension 模板反向推断核心冲突（见下）
- `narrative_arc`：如果存在 → 决定 Theory 的 rising action 强度；如果不存在 → 从 Gap 类型推断
- `protagonist_construct` / `supporting_constructs`：如果存在 → 作为角色定位的初始值；如果不存在 → 在 Phase 1 架构决策中确定

**Central Knot 推断规则（当 `central_knot_statement` 为 `null` 时）**：
- Incommensurability → 推断为"对立理论或证据之间的矛盾冲突"
- Inadequacy → 推断为"现有解释存在盲区或基于错误假设"
- Incompleteness → 推断为"遗漏了关键维度、机制或时点"
- 具体推断：从 Tension 模板的 `[gap statement]` 句法签名中提取核心冲突，或从用户提供的 Gap 描述中识别转折信号词（"However"/"Yet"/"Although"/"In contrast"）后的核心主张

推断出的 Central Knot 仅用于 Phase 0.5 的叙事对齐检查，不阻塞后续阶段。

---

**制度冲击检测**（自动判断，无需用户输入）：

在 Phase 0.5 诊断之前，自动检测是否需要激活 Phase 1.5（制度冲击类研究的 Theory Lens 特殊适配）：

```
检查以下信号（任一满足即激活 Phase 1.5）：
├── 上游 `theory_hints` 中的 `identification` 字段包含 IV / DiD / RDD / natural experiment / quasi-experiment
├── 上游 `theory_hints` 中的 `empirical_setting` 描述涉及政策变化、法律冲击、制度差异、州级差异
├── 用户输入的研究描述中出现：staggered adoption / policy shock / regulatory change / law change / institutional reform / eligibility threshold
└── 以上均不满足 → 跳过 Phase 1.5，按标准 Theory Lens 流程执行
```

**检测输出**：
- 如果激活 Phase 1.5 → 在输出结构中插入 Phase 1.5 块，并标记"制度冲击适配已激活"
- 如果跳过 → 不输出 Phase 1.5 相关内容，保持流程简洁

---

**Phase 0.5 诊断流程**（默认执行）：

按顺序读取以下语料库文件：

1. **Rising Action 协议**
   读取 `corpus/storytelling/rising-action-protocol.md`
   → 确认从 Introduction 继承的 Central Knot 在此继续被 tie

2. **Plot Emergence 检查**
   读取 `corpus/storytelling/plot-emergence-check.md`
   → 验证情节是否从构念互动中自然浮现，而非强加

3. **Knot 连续性检查**
   读取 `corpus/storytelling/knot-continuity-check.md`
   → 验证 Theory 的每个段落都让 knot 更紧，无 extraneous storyline

**诊断结果输出**：narrative risk 标记附加到 Phase 3 QC 清单。

---

### Phase 0.75: Prose Craft 定位（Pollock 2025 Ch03）

Theory section 的 Rising Action 不仅需要功能推进，还需要 prose 层面的可读性。
以下三个工具与 Phase 1-5 并行执行。
完整检查清单见 `../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md`。

#### Human Face in Theory
- **P1 Knot Inheritance**：承接 knot 时，用 1 句具体场景说明"这个问题在现实世界中长什么样"
  - 句式："To resolve the tension that [knot], consider what happens when [Company] tried to [action]..."
- **P2-P4 Knot Deepening**：每个新构念首次出现时，配 1 个具体例子
  - 例："We define regulatory focus as the tendency to pursue gains versus avoid losses (Higgins, 1997). A promotion-focused CEO, for example, might prioritize market expansion over safety compliance..."
- **P5-PN Knot Tying**：假设推导中，每个 why-chain 关键步骤可配 1 个微型场景（1-2句）
  - 例："Because promotion-focused CEOs prioritize speed over caution, they may delay recall announcements until regulatory pressure becomes unavoidable. Consider how [Company X] handled its 2015 ignition-switch crisis..."

#### Showing vs Telling in Theory
- **Stroke 段落（70%）**：每个抽象因果步骤后，跟 1 句 concrete illustration
- **Glide 段落（30%）**：用比喻/类比解释抽象概念
- **规则**：不允许连续 2 个 stroke 句子无 showing

#### Conversational Voice in Theory
- **P1**：用 "To resolve the paradox that [knot], we argue that..." 承接
- **假设推导**：用 "We argue that..." / "We hypothesize that..." 引出每个假设
- **T6 Closure**：用 "In sum, we have argued that..." 总结
- **禁止**："It is argued that..." / "It is hypothesized that..." / "The literature suggests that..."（无主语被动）

---


### Phase 1: 架构决策（7 因素）

基于 Pollock 2025 Ch06 Table 6.1，确定 Theory section 的宏观结构：

| 因素 | 诊断问题 | 结构含义 | Showing vs Telling 要求 |
|------|---------|----------|------------------------|
| **理论域数量** | 论文涉及几个理论域？ | 1 个 → progressive coherence；2+ → 需要整合框架 | 每个理论域首次引入时，用 1 个具体研究场景说明其适用范围 |
| **构念新旧** | 有全新构念吗？ | 是 → early placement + 专门定义+区分段落；否 → 可灵活放置 | 新构念定义后必须跟 1 个 concrete illustration |
| **主角配置** | IV 还是 DV？几个？ | 单一 DV → DV 先行；单一 IV → IV 先行；多 IV+DV → 取决于叙事线 | 每个主角构念首次出现时，用 1 个具体案例说明其操作化方式 |
| **配角配置** | 配角是什么角色？ | DV 配角 → early；Mediator/Moderator → 随故事展开 | 配角构念引入时，用 1 个微型场景说明其调节/中介逻辑 |
| **Context** | Context 对理解角色必要吗？ | 必要 → 开头；提供例子 → 穿插；实验/泛化 → 最后 | Context 描述需包含 ≥1 个具体行业/公司/制度实例 |
| **Figure** | 理论图还是总结模型图？ | 理论图 → 相关讨论处；总结模型图 → 全部假设后 | 理论图的文字描述中，每个路径必须有 1 个场景化说明 |
| **叙事节奏（Ch02-Ch03）** | Theory section 的动作-评论比例？ | 理论推演（stroke）> 文献解释（glide），但不能没有 glide | Stroke 段落每个因果步骤后需有 concrete illustration；Glide 段落用比喻/场景解释 |

**叙事节奏详细说明（第7因素）**：

Pollock Ch03 用 "stroke and glide"（划桨与滑行）比喻动作与评论的平衡：
- **Stroke（动作）**：推进理论的主动作——因果推理、假设推导、机制展开
- **Glide（评论）**：帮助读者吸收的解释——文献总结、定义澄清、边界说明

| 段落类型 | 推荐比例 | Showing vs Telling 要求 | 风险 |
|---------|---------|------------------------|------|
| 机制推演段落 | 70% stroke / 30% glide | 每个 stroke 句子后需有 concrete illustration 或比喻 | 全 stroke → "forced march" |
| 文献铺垫段落 | 40% stroke / 60% glide | Glide 段落用具体研究场景解释，非纯引用罗列 | 全 glide → "ponderous pace" |
| 构念定义段落 | 50% stroke / 50% glide | 定义后立即给 1 个例子 | 纯定义无方向 → 读者失去兴趣 |

输出：**推荐的段落序列**。

→ 每段叙事功能标注（新增）：
```
P1: 承接 knot（knot inheritance）
P2-P3: 加深 knot（knot deepening）
P4-P7: 机制 tying（knot tying through mechanism）
P8: knot fully tied（closure）
```

---

### Phase 1.5: 制度冲击类研究的 Theory Lens 特殊适配

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
dimension matters because [theoretical reason, e.g., CEOs face escalating regulatory
pressure over time, and the hazard of recall increases non-linearly with defect exposure].
```

---

### Phase 2: 假设结构路由

```
假设体系包含哪些类型的假设？
│
├── 纯主效应 (X→Y) → 基础关系模板
├── 主效应 + 中介 (X→M→Y) → 机制推演模板 + 中介假设模板
├── 主效应 + 调节 (X×Z→Y) → 调节效应模板
├── 调节 + 中介 (Moderated mediation) → 机制推演 + 调节混合
└── 三向交互 (X×Z×W→Y) → 假设树模板
```

---

### Phase 2.5: Hypothesis Development 段落级逻辑协议

**每个假设推导段落是一个微型论证单元**，通常遵循以下结构，但可根据故事需要灵活调整。

#### 推荐结构：四段式论证链（4-Part Logic Chain）

```
[1. Topic Sentence]  →  [2. Theoretical Reasoning]  →  [3. Literature Support]  →  [4. Hypothesis Transition]
        ↓                         ↓                              ↓                            ↓
  本段的单一理论主张        多步因果链：                前人的 argument/finding       收束推理，引出假设
  (1-2句)                  X→M1→M2→Y (3-5句)          如何支持每一步 (2-4句)         (1-2句)
```

**灵活调整说明**：如果你的故事更适合将文献对话与理论推理交织（如 ASQ 常见的"对话式论证"），可以调整[2]和[3]的顺序或将其合并，但必须确保：
- (a) 每个假设前有 why chain（2-3 步因果推理）
- (b) 每个引用都总结了 argument 而非罗列名字

**各要素 QC**：

| 要素 | 必须做到 | 最常见失败模式 |
|------|---------|--------------|
| **Topic Sentence** | 同时包含话题+核心观点+限定范围；**必须使用 active verb + concrete subject**（如 "We argue that..." 而非 "It is argued that..."）；**段首句在 15 词内说出核心判断**；不宽泛不局限 | 太宽泛/太局限；**无主语被动语态**（"It is argued that"）；**Burying the lead**（核心判断不在段首句） |
| **Theoretical Reasoning** | 从 X 到 Y 的每一步因果推理都明确写出；**每步间有 explicit transition**（Consequently/Thus/This leads to...） | **逻辑跳跃**：省略关键推理步骤；**Read my mind**：缺少 transition，从 A 直接跳到 C |
| **Literature Support** | 总结前人研究的 argument/finding + 说明链接 | **引用罗列**：只有名字没有 argument |
| **Hypothesis Transition** | 收束句总结推理链，自然引出假设 | 无理论收束直接 "we hypothesize" |

**[2b. Concrete Illustration]（可选但推荐）**：
每个因果步骤后，可插入 1 句 concrete illustration：
- "For example, when [Company] faced [situation], [mechanism] produced [outcome]."
- 或用比喻："This is akin to [familiar scenario]..."
- 规则：不允许连续 2 个推理步骤无 illustration

**[3b. 文献引用的 Human Face 要求]**：
- 每个引用必须总结其 **argument**（非罗列），并链接到 **concrete finding**
- 例："Pfarrer et al. (2010) showed that firms delaying recalls experienced 23% greater stock-price declines than firms recalling immediately—a finding consistent with our argument that..."

**逻辑跳跃诊断**：逐句标记因果连接词（Consequently/Thus/Thereby/As a result/This leads to...）。缺少中间步骤 → 存在跳跃。

**[2c. 识别策略的理论论证]**（制度冲击 / 自然实验研究必须包含）：

如果你的研究使用 IV / DiD / RDD，Theoretical Reasoning 部分必须在 why chain 中嵌入对识别假设的理论论证，而非仅在 Methods 中呈现统计假设。

| 识别策略 | 必须在 Theory 中论证的内容 | Theory 嵌入位置 |
|---|---|---|
| **IV** | 为什么工具变量与结果无直接联系（排除限制）在理论上是成立的？工具变量通过什么理论渠道影响处理变量？ | 在 why chain 的 X→M 步骤后插入 1 句："[Instrument] influences [treatment] through [channel] but does not directly affect [outcome] because [theoretical reason, e.g., it operates at the state level while outcomes vary at the firm level]." |
| **DiD** | 为什么处理组和控制组在没有处理时会有平行趋势？处理效应的异质性来源在理论上是什么？ | 在 why chain 开头插入 1 句："Absent [policy], treated and control [units] would have followed parallel trajectories because [theoretical reason, e.g., they face identical demand shocks prior to the regulatory change]." |
| **RDD** | 为什么断点附近的企业在制度实施前是可比较的？断点两侧的制度差异在理论上是什么？ | 在情境描述后插入 1 句："Firms just above and below the [threshold] are observationally similar in [key dimensions] because [theoretical reason], yet they face sharply different [treatment] due to the [institutional rule]." |

**检查**：如果 Methods 中描述了识别策略，但 Theory 段落中完全没有提及识别假设的理论基础 → ⚠️ 标记为"识别策略与理论脱节"。

**Topic Sentence CV 反模式示例**：
- ❌ "It is argued that CEO overconfidence affects firm risk." → 无主语被动，违反 Conversational Voice（见 `prose-craft-checklist.md` 禁用词表）
- ✅ "We argue that CEO overconfidence increases firm risk-taking because overconfident leaders systematically underestimate downside uncertainty." → active verb + concrete subject + 方向性预测
- 规则：Topic Sentence 是段落的第一印象，若用被动语态，读者会预期整段都是"报告腔"而非"论证声"。

#### 段落级 QC 检查表

- [ ] 主题句精准度：是否同时包含话题+核心观点？
- [ ] **Burying the lead**：段首句是否在 15 词内说出核心判断？段首句不是元评论？
- [ ] 推理链完整性：每个因果步骤是否都在文中明确写出？
- [ ] **Read my mind**：每步因果推理间是否有 explicit transition？无"显然"/"不难发现"？
- [ ] 引用嵌入度：每个引用是否都总结了其 argument/finding？
- [ ] 术语一致性：同一构念在全段用的是否同一个术语？
- [ ] 证据-论点匹配：每个引用是否直接支持它所在推理步骤？
- [ ] **Sentence stuffing**：单句 ≤ 30 词？单句从属连词 ≤ 2 个？
- [ ] 收束句质量：是否总结了推理链而非简单重复 "we hypothesize"？
- [ ] 段落独立性：单独阅读本段能否理解完整论证逻辑？

---

### Phase 3: 通用 QC 层 + 跨 Section 对齐

#### 审计 1: Theory IS NOT（7 种伪理论陷阱 + 3 种 Ch04 病理）

| 陷阱 | 检查 |
|------|------|
| References as theory | 是否有罗列式引用？→ 改为总结 argument + 链接 |
| Data as theory | 是否用前人 findings 替代机制解释？→ 补充理论逻辑 |
| Variable lists as theory | 是否列出构念定义后直接出假设？→ 补充关系讨论 |
| Diagrams as theory | 是否有模型图但每条路径无文字解释？→ 补 verbal theory |
| Hypotheses as theory | 假设是否描述了 what 但没解释 why？→ 每个假设前必须有 why chain |
| Passive voice dumping | 是否有 "It is argued that" / "It is hypothesized that"？→ 改为 "We argue that" / "We hypothesize that" |
| Inflated symbolism | 是否有 "paradigm shift" / "fundamentally transforms"？→ 降级为具体贡献描述（"extend", "refine", "challenge"） |
| Burying the lead | 假设推导段段首句是否未在 15 词内说出核心判断？→ 重写段首句为"主语+主动动词+方向" |
| Sentence stuffing | 单句 > 30 词或单段 > 200 词？→ 拆分长句，每句一个核心判断 |
| Read my mind | why chain 是否从 A 直接跳到 C，缺少 B 的中间步骤或 transition？→ 补充每个因果步骤，添加 explicit transition |

#### 审计 2: Construct Clarity（4 字段）

- [ ] **Definition**: 定义是否清晰、非循环、不含 antecedents/consequences？
- [ ] **Scope conditions**: 何时/何地/对谁适用？
- [ ] **Lineage**: 该构念从哪些先前构念演化而来？
- [ ] **Adjacent constructs**: 与相似构念的区别是什么？

#### 审计 3: Hypothesis Clarity（6 字段）

- [ ] Constructs named
- [ ] IV/DV roles clear
- [ ] Direction specified
- [ ] Relationship form specified
- [ ] Mediator/moderator specified
- [ ] Matches theorized AND tested relationship

#### T6 Closure 强制提醒

**⚠️ 重要**: Batch_1 蒸馏发现，6/6篇产品召回领域论文缺失 T6 Closure。这是该领域的系统性缺陷。

T6 不是"重复总结"，而是完成三个理论任务，让读者感到 **"knot fully tied"**（Pollock 2025 Ch02），为 Results/Discussion 的 climax 做准备：
1. **框架锁定**：将分散假设整合为统一理论叙事，明确假设间逻辑关系
2. **逻辑显性化**：用 1-2 句话说明 central knot 已被 fully tied——"we have argued that [knot核心] is driven by [机制]"
3. **Denouement 预告**：预告 Results 将如何 unravel the knot，让读者感到"必须看结果才能知道答案"

**T6 段落骨架（80-120词）**：参见 `corpus/sentences/closure.md`

**T6 缺失时的应急策略**：参见 `corpus/sentences/closure.md` —— "局部收束信号"

**T6 Closure Voice Check**：
- [ ] T6 用 "In sum, we have argued that..."（accountable first-person）
- [ ] T6 无被动语态
- [ ] T6 大声朗读测试：是否像研究者在总结自己的判断？

**T6 Denouement 预告检查**（与 Rising Action Phase 4 对齐）：
- [ ] T6 是否明确或暗示 "knot fully tied"？（如 "we have tied the knot of..." 或 "we now turn to our empirical analysis to unravel it"）
- [ ] T6 是否预告 Results/Discussion 的 resolution 形态？（如 "we test whether [机制] holds in [情境]"）
- [ ] T6 与 Discussion 开篇是否形成叙事接力？（Discussion 首段应回到 central knot，而非重复 Methods）

**T6 制度冲击类研究的额外检查**：
- [ ] T6 是否预告了 Results 将通过什么识别策略（IV/DiD/RDD/生存分析）来 unravel the knot？
- [ ] T6 是否暗示了识别策略的理论基础已在 Theory 部分建立？（如 "we exploit the staggered adoption of [policy] as a natural experiment to test..."）
- [ ] 如果使用生存分析：T6 是否预告了时间动态将是 Results 的核心叙事？（如 "we examine not merely whether [event] occurs, but how [treatment] alters the rate at which firms approach the recall threshold"）

**叙事接力要求**：T6 结尾的能量级应 ≥ Theory 最后假设推导段的能量级，且为 Discussion 的 "knot fully unraveled" 预留空间。若 T6 能量骤降 → 标记"叙事阶段倒退"。

---

### Phase 4: 跨 Section 对齐检查（Introduction ↔ Theory）

**强制输出**。无论用户是否提供 Introduction claims，都输出对齐检查框架。如有 claims，填充具体检查项。

检查协议完整定义见 `corpus/meta/alignment_protocol.md`。

**输出格式**：

```markdown
### 跨 Section 对齐检查

| 维度 | 检查项 | Introduction 信号 | Theory 状态 | 结论 |
|------|--------|-------------------|-------------|------|
| Gap→Type | 能量匹配 | [Gap类型] + [Tension] | [构建类型] | ✅/⚠️/❌ |
| Makadok→Module | 贡献兑现 | [Makadok维度] | [模块覆盖] | ✅/⚠️/❌ |
| Preview→H | 假设数 | "[N] hypotheses" | [实际N个] | ✅/⚠️/❌ |
| Lens→Lens | 理论一致性 | "[theory]" | "[theory]" | ✅/❌ |

**必须修复的不一致**：
- [ ] [具体不一致项1]
- [ ] [具体不一致项2]
```

---

### Phase 5: 按类型输出（引用语料库）

根据 Phase 0 诊断的类型，读取对应语料文件并生成输出。

#### 语料文件索引

| 变体 | 语料文件 | 子协议 |
|------|----------|--------|
| A 构念辨析型 | `corpus/variants/A_construct_differentiation.md` | — |
| B 机制推演型 | `corpus/variants/B_mechanism_elaboration.md` | `corpus/subprotocols/B2_dual_track.md` |
| C 假设树型 | `corpus/variants/C_hypothesis_tree.md` | — |
| D 质性过程理论型 | `corpus/variants/D_process_theory.md` | — |
| E 调节效应型 | `corpus/variants/E_moderation.md` | `corpus/subprotocols/E1_categorical_moderation.md` |
| F 竞争假设型 | `corpus/variants/F_competing_hypotheses.md` | — |
| G 辩证对立型 | `corpus/variants/G_dialectical_opposition.md` | `corpus/subprotocols/G1_horizontal_dialectical.md` |

#### 通用句式语料索引

| 功能 | 语料文件 |
|------|----------|
| 构念界定 | `corpus/sentences/construct_definition.md` |
| 机制推演 | `corpus/sentences/mechanism_chain.md` |
| 调节机制 | `corpus/sentences/moderation.md` |
| 假设形式 | `corpus/sentences/hypothesis_forms.md` |
| 收束/过渡 | `corpus/sentences/closure.md` |

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

### 跨 Section 对齐检查
[Phase 4 输出块]

### 段落功能地图
[引用语料文件中的段落功能地图]

### 构念界定模板
[引用 `corpus/sentences/construct_definition.md` 推荐变体]

### 理论机制推演模板
[引用语料文件中的机制推演骨架]

### 假设陈述
[引用 `corpus/sentences/hypothesis_forms.md` 对应形式]

### 叙事弧线指南（Pollock 2025 Ch02）

Theory section 的 Rising Action 四阶段结构、叙事节奏检查点和 Stroke/Glide 比例指南见 `corpus/storytelling/rising-action-protocol.md`。

**渲染时的附加要求**：
- 在每个段落标题后标注其 narrative function（如 `P1: 构念定义 | Knot Inheritance`）
- 在"提醒"中附加叙事检查点（P1 是否承接 knot？是否有阶段倒退？T6 是否 fully tied？）

### 期刊适配建议
[基于 --journal 参数的适配建议]

### QC 检查点
- [ ] 每个假设前都有 why chain？
- [ ] 构念界定包含 scope conditions + lineage + adjacent construct 区分？
- [ ] 假设形式匹配变量类型和理论关系？
- [ ] T6 Closure 是否存在？
- [ ] [类型专属 QC 检查点...]
```

---

## Constraints

1. **Theory 必须解释 why，不是文献列表。** 每个假设前必须有至少 2-3 步的因果/过程推理链。
2. **假设推导段落推荐使用四段式结构**：Topic Sentence → Theoretical Reasoning → Literature Support → Hypothesis Transition。允许根据故事需要调整顺序（如将文献对话与推理交织），但每个假设前必须有 why chain，每个引用必须总结 argument 而非罗列名字。
3. **禁止逻辑跳跃。** 从 X 到 Y 的每个因果步骤必须在文中明确写出。
4. **假设必须明确 IV、DV、方向、形状、条件。** 不允许 "X is associated with Y" 等模糊措辞。
5. **如果用户有具体构念名称，必须嵌入模板替换占位符。**
6. **新构念必须完成 definition + scope conditions + lineage + differentiation from adjacent constructs 四步。**
7. **主角（核心构念）不应超过 3 个。**
8. **Literature Support 必须是 argument 总结，不是 citation 罗列。**
9. **段落内术语必须统一。**
10. **调节效应的假设必须指定交互模式类型（enhancing/buffering/antagonistic/existence/competing），且必须排除反向交互。**
11. **跨层调节必须在 P1 就声明 focal unit of analysis 和 nesting structure。**
12. **图不能替代文字理论。**
13. **T6 Closure 为 quasi-mandatory。** 所有构建类型都应包含 T6 段落（或在 Discussion 开篇补回）。
14. **竞争假设必须使用非传统收敛信号。** 不可使用 "Therefore" 收束，应使用 "Given these competing arguments..." 等信号。
15. **不要重复语料层内容。** 本文件是协议层；所有具体模板引用 `corpus/` 目录。
16. **辩证对立型必须满足对称性要求。** T3 和 T4 的机制步骤数应接近对称（差不超过 1 步）；T4 首句必须用 dialectical turn 标记（"Despite research showing..." / "This may be because..."）；T6 reconciliation 必须为 theory-based（不能仅说 "they coexist"）；两类受众的定义必须有理论基础区分（不是随意切分的 demographic 分组）。
17. **辩证对立型的"反转"必须是真正的方向反转，不是强度变化。** 同一 predict 对 audience A 显著负、对 audience B 显著正，才是 dialectical opposition。如果只是"对 A 更强、对 B 更弱"但不是方向反转，应路由到 [E] 调节效应型。

---

## 下游接口（供其他 Skill 消费）

- `/write-discussion` — 使用假设列表和机制链作为 Discussion 理论贡献的锚点
- `/paper-review` — 使用假设列表进行跨 Section 对齐检查
- `/theory-review` — 如果用户已有 Theory 草稿，使用本模板作为理想基准进行对比审查
- `/distill-theory-exemplar` — 将新论文的 Theory 部分蒸馏后回写 `corpus/` 语料库

---

## 资产位置

- **本协议**: `~/.claude/skills/write-theory/SKILL.md`
- **语料库**: `~/.claude/skills/write-theory/corpus/`
- **路由表**: `corpus/meta/routing_table.md`
- **对齐协议**: `corpus/meta/alignment_protocol.md`
- **元模板**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\meta_templates\Theory_Hypotheses_Meta_Template.md`
- **MVP30 范文解析**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\_parsed_texts\mvp30\`
- **叙事分析**: `D:\Onedrive\Obsidian Vault\00 工作台\叙述模板训练集\narrative_analysis\mvp30\`
