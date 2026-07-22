# 构念界定句语料库

## 变体 A：承认多元定义，明确采纳（最常用）

**模板**：
```
"[Construct] has been defined in many ways by different scholars and research 
traditions. We adopt the definition put forth by [Author (year)] that [definition]. 
This definition captures [N] critical elements: (1) [element 1], (2) [element 2], 
and (3) [element 3]."
```

**语料锚定**：
- Pollock 2015 (ASQ) — reputation / status 界定
- Han 2024 (AMP) — reputation vs celebrity 界定

---

## 变体 B：综述分歧，提取共识

**模板**：
```
"Although scholars have offered slightly different definitions of [construct], 
they have all focused on [common element] and incorporated three elements: 
(a) [element a], (b) [element b], and (c) [element c]."
```

**语料锚定**：
- Malik 2025 (JM) — current / prospective wealth 双维度界定

---

## 变体 C：引用权威综述定义

**模板**：
```
"[Construct] is broadly understood as [definition] ([Author, year]). [Elaboration]. 
A central thesis of [field] research is that [core proposition] ([Author, year])."
```

**语料锚定**：
- Darby 2024 (MSOM) — spillover effect 引用经典定义

---

## 变体 D：双维度/双构念对称界定（竞争假设型、双轨并行型专用）

**模板**：
```
"On one end of the spectrum are [构念A], who tend to [特征1] and [特征2] 
([文献]). As such, [构念A] often [行为倾向1] ([文献]). In sum, [构念A] 
tend to prioritize [价值A], even at the expense of [价值B] ([文献]).

On the other end of the spectrum are [构念B], who, on average, emphasize 
[价值C] over [价值D] ([文献]). Consequently, [构念B] emphasize [行为倾向3]."
```

**语料锚定**：
- Wowak 2025 (MS) — liberal / conservative CEO 对称界定

---

## 变体 E：三层框架展开+表格对比型（weng_yang 型）

**功能**: 当 IV 是一个可从多个理论透镜（cognitive/social/behavioral）理解的构念时，先展示完整框架再聚焦到其中一个透镜，用表格对比构念两端的差异。

**模板**:
```
"In a recent review, [authors] ([citation]) suggest that [IV] has [N] interrelated 
aspects: [aspect 1], [aspect 2], and [aspect 3]. First, the [aspect 1] lens 
focuses on [definition + citation]. Second, the [aspect 2] lens focuses on 
[definition + citation]. Finally, the [aspect 3] lens suggests [definition + citation].

Our study applies the [chosen aspect] lens of [IV] to postulate that [Group A] 
differ from [Group B] in [N] ways (see Table [N] for a summary). First, 
[dimension 1: comparison between A and B]. Second, [dimension 2: comparison]. 
Finally, [dimension 3: comparison].

[Table [N] summarizes these differences across the three dimensions]."
```

**语料锚定**：
- Weng & Yang (JMS) — CEO political ideology 通过 Swigart et al. (2020) 三层框架定义，Table I 对比 liberal vs conservative CEOs

**关键特征**:
- 先展示完整框架（N aspects），再聚焦——让读者知道作者了解全貌但做了有意识的选择
- Table 嵌入 Theory——将构念对比正式化、可视化（JMS 风格接受；ASQ/SMJ 需谨慎）
- 三个维度为后续 H1 的两个原因（awareness + openness）提供概念基础
- "Our study applies the [chosen aspect] lens" 作为聚焦信号——从广泛框架到具体应用的过渡

**适用**: 当 IV 有多重理论透镜且需要选择一个作为分析焦点时；期刊接受 Theory 中的正式表格（JMS, AMJ）

**禁忌**: 表格维度必须与后续假设机制一一对应（不能表格说了三维度但 H1 只用了一个）；不要用表格替代文字论证——表格是总结，文字是论证

---

## 变体 E：维度独立性论证 (Dimensional Independence Argument)

**适用**: IV 具有多个维度（如 valence, source），且这些维度常被直觉性地误认为同一连续体的两端。需要在 T1 阶段论证它们是概念上独立的维度。

**模板**:
```
"It is important to note that [Dimension A] is different from the absence of [Dimension B].
An increase in [Dimension A] means that [entity] is increasingly surrounded by [specific
A markers] that are distinct from [neutral/B descriptions]. The greater is the [Dimension A]
of [domain]-related issues, the more likely will this [phenomenon] be [observed consequence].

[Dimension B], likewise, is different from the absence of [Dimension A]. [Dimension B] is
associated with specific [markers] that are distinct from a [neutral tone]. [Entity] experiencing
more [Dimension B] will [behavioral consequence different from Dimension A]."
```

**语料锚定**: shipilov_greve_rowley2019 (SMJ) — "negative media coverage is different from the absence of positive coverage" / "positive coverage is different from the absence of negative coverage" 在 T3 机制推演中反复出现

**关键特征**:
- **"X is different from the absence of Y"** → 核心句法——不是 "X and Y are independent"，而是 "X 不等于非Y"
- **维度独立性论证不是一次性 T1，而是伴随 T3/T4 反复出现的概念锚定**: 在推导每个假设前提醒读者正/负是独立维度
- **与构念辨析型的区分**: 维度独立性论证是 "一个构念的两个维度是独立的"，而非 "两个构念是不同的"
- 每个维度必须独立被操作性测量（LIWC positive tone / negative tone 是两个独立分数）
- 引用权威心理学/语言学文献支撑维度独立性（如 Baumeister et al. 2001 的正负情绪独立论）

**与变体 D（双维度对称界定）的区分**:
| | 变体 D（双维度对称界定） | 变体 E（维度独立性论证） |
|---|---|---|
| 功能 | 定义两个维度的内容 | 论证两个维度是独立的（不是同一连续体） |
| 典型句式 | "On one end... On the other end..." | "X is different from the absence of Y" |
| 时机 | T1 一次性完成 | T1 铺垫 + T3 每假设段中反复锚定 |
| 适用 | 竞争假设型、双轨并行型 | 2×2 矩阵型、正负 valence 型 |

**反模式**:
- 在维度事实上高度相关（r > 0.7）时仍坚持独立性论证 → 审稿人会指出实证不支持独立性
- 只论证一次就在 T3 中忘记 → 读者会自然地滑回 "正负是一个连续体" 的直觉
- 使用 "opposite ends of the spectrum" 句式 → 直接暗示连续体，与独立性论证矛盾

---

## 嵌入策略模板

**适用**：已有广泛接受的构念、构念数量较多（≥4个）、Theory 篇幅有限

**模板**：
```
"[Construct], [定义/操作化描述] ([文献]), [机制逻辑开头]..."
"We focus on [construct], which refers to [definition] ([文献]). In our context, 
this means [contextual specification]..."
```

**语料锚定**：
- Darby 2024 (MSOM) — time-to-recall 嵌入定义
- Eilert 2017 (JM) — recall speed 嵌入定义

---

## 变体 K：构念多层界定（标签层面 vs. 组织层面，Pontikes 2012 型）

**适用**: 区分现象的"属性本身模糊"与"实体组合模糊"两个层次；两个层次可独立操作化并通过不同机制影响结果。

**模板**:
```
[Level 1] [X] arises when a single [attribute] is itself ambiguous. [Definition + example].
[Level 2] [X] also arises when an [entity] combines multiple [attributes]. [Definition + example].
[Implication] These levels operate through distinct mechanisms.

H[X]a: [attribute-level X] is [direction] related to [outcome].
H[X]b: [entity-level X] is [direction] related to [outcome].
```

**语料锚定**: Pontikes (2012, *ASQ*) — label-level ambiguity vs organization-level ambiguity; both create confusion but operate through different mechanisms.

**关键特征**:
- 先分别定义两个层次，再说明它们通过不同机制运作
- 每个层次对应一个独立假设
- 必须说明区分的理论必要性（为什么不能合并为一个构念）

**反模式**: 两个层次假设成为同义反复；层次区分没有独立测量。

---

## Scope conditions 附加句

**模板**：
```
"This definition applies to [temporal/geographic/industry/organizational scope]. 
It does not extend to [boundary exclusion], where [construct] functions differently 
because [reason]."
```

---

## 辩论并置型构念界定（Debate Juxtaposition T1/T2）

**适用**: 研究领域存在经典辩论（两个对立的视角/学派），Theory 开篇将双方并列呈现——双方同等篇幅、同等学术+实践支撑——然后在中立立场上引入自己的贡献

**模板**:
```
"Disagreement is evident in both the academic literature and in public discussions among 
practitioners about [core debate question]. One perspective, often called [Perspective A], 
holds that [core claim] ([citations]). This perspective sees [alternative approach] as 
[negative characterization]. [Foundational citation block]. A practitioner-based example 
of this perspective can be found in [YEAR statement] issued by [authoritative body], who 
wrote that '[direct quote].'

The competing [Perspective B] holds that [core claim] ([citations]). This perspective sees 
the a priori prioritization of [A's interests] as [negative characterization]. Whereas 
[Perspective A] views tradeoffs as [inevitable], [Perspective B] allows for [alternative 
framing] ([citations]). This perspective is therefore not opposed to [A having interests 
served], but it posits that [paradoxical outcome]. [Foundational citation block]. A 
practitioner-based example of this perspective can be found in [YEAR statement] issued by 
[authoritative body], who wrote that '[direct quote].'

Indeed, [entities] face heterogeneous demands and pressures from multiple [stakeholders] 
and therefore must decide whether and how to address different [stakeholders'] interests 
and then allocate resources accordingly ([citations]). Here we use the term [core construct] 
broadly to refer to [definition] ([citation]). [Transition to own contribution].

We join the conversation pertaining to [debate domain] by exploring how [specific mechanism] 
influences [outcome]."
```

**语料锚定**: park_lange_jeon (SMJ) — Theory P1-P4 (shareholder primacy vs stakeholder perspective)

**关键特征**:
- 双方篇幅完全对称（各 ~200 词）
- 双方都有学术引用 + **实践声明**（避免 "纯学术辩论" 印象）
- "competing" / "not per se opposed" / "therefore not opposed" → 非零和博弈措辞
- 过度段承认环境复杂性（"heterogeneous demands"）
- 贡献声明用 "join the conversation" 而非 "resolve the debate"

**反模式**:
- 一方篇幅明显长于另一方 → 审稿人质疑作者偏见
- 只有学术引用无实践声明 → 缺乏 practitioners 也关心此辩论的证据
- 用 "We argue that Perspective A is wrong" → 失去中立立场
- Practitioner statements 不是来自公认权威机构

**可迁移性**: 高 — 适用于 shareholder vs stakeholder, exploitation vs exploration, agency vs stewardship 等任何经典辩论

---

## 变体 F：Typology Alignment 定义型（desai2012 型）

**适用**: 将新构念定位到已有学术分类法（typology）的特定位置，增加合法性而非声称完全原创

**模板**:
```
This [construct name] is related to [existing author]'s notion of [related concept]. 
[Author] provides a typology of [actions] that [actors] take to [goal]. Of these types, 
[our focus] is the one most appropriate to theory regarding [our specific concern]. Other 
tactics, such as [alternative 1], [alternative 2], and [alternative 3], affect [narrower 
scope]. In contrast, [our focus] may more generally affect [broader scope].
```

**语料锚定**: desai2012 (AMJ) — defensive institutional work 对齐到 Oliver (1991)的 manipulation 策略

**关键特征**:
- **"This [construct] is related to [existing typology author]'s notion of..."** → 先建立与已知分类法的联系，再说明差异
- **"Of these types, [our focus] is the one most appropriate to theory regarding [our specific concern]"** → 将自己定位在已有分类法的特定槽位
- **"Other tactics... affect [narrower scope]. In contrast, [our focus] may more generally affect [broader scope]"** → 用scope difference来论证新构念的独特性（不是完全不同的东西，而是应用于更广泛的领域）
- 核心说服逻辑：不声称"我发明了新概念"，而说"已有概念在一个新领域有未被认识的应用"

**与变体 A（承认多元定义，明确采纳）的区分**: 变体A是"选一个已有定义"，变体F是"将新东西插入已有分类"

**反模式**:
- 选择了一个与自己的构念实际差异过大的typology强行对齐
- "Other tactics... affect narrower scope" 的论断无文献支撑
- 用 "is related to" 逃避正面定义核心构念

**可迁移性**: 高 — 跨构建类型通用。特别适用于组织/战略理论中从firm-level向field-level扩展的新构念

---

## 变体 H：三层递进 T1 — Context → Framework → Dimensions（zhao-ding_gaba 型）

**适用**: 论文不使用外部理论，而是自己构建概念框架作为理论基础。T1 从宏观 context 特征出发，经过中观 conceptual framework，最终收敛到微观 construct dimensions。

**模板**:
```
[Layer 1 — Context Establishment: Why this context is different]
The growth of [digital market examples] has expanded the set of options available to 
[actors] ([citations]). Because [products] can be [actions] at very low marginal cost, 
[positions] that would be difficult to sustain in traditional markets can become viable 
in [context] ([citations]). Lower entry barriers also invite [entry pattern] by [actors] 
with diverse [characteristics] ([citations]). At the same time, [actors] must contend 
with [constraint]: They need to [requirement A] and [requirement B] ([citation]). Because 
[products] can be tailored for a broader range of [needs], the relevant [space] becomes 
increasingly multidimensional, increasing the complexity of [decisions] ([citations]). 
In short, [context] enable[s] [core phenomenon]: [definition] ([citation]).

[Layer 2 — Conceptual Framework: Core/peripheral construct definition]
Prior research on [broad domain] has long emphasized [core concept], understood as 
[definition], as an important basis for [outcome] ([citations]). [Author] (year), for 
example, show that [specific manifestation] shaped [strategies] in [context]. Similarly, 
in [another context], [concept] range from [example A] to [example Z] ([citation]).

In [focal context], implementing [concept] is comparatively easier due to [enabling 
conditions] ([citations]). [Actors] can [action A] and [action B] at low cost ([citations]). 
To target specific [needs], [actors] typically select [dimension 1] that anchors the 
[unit]'s primary [purpose] and add [dimension 2] to complement it ([citation]). 
Conceptualizing [phenomenon] as combinations of [dimension 1] and [dimension 2], therefore, 
captures [key logic] more accurately and provides a more fine-grained lens on [domain].

[Layer 3 — Construct Dimensions: IV dual-dimension differentiation]
Building on these insights, we focus on two dimensions of [IV]: [dimension 1] and 
[dimension 2]. Because [IV] stems from [source] in the [context], it reveals information 
about both [aspect A] and [aspect B]. [Actors], therefore, make two related assessments. 
First, they infer [inference 1], which shapes [DV dimension 1]. Second, they assess 
[assessment 2], which influences [DV dimension 2].
```

**语料锚定**: zhao-ding_gaba (ORSC) — Layer 1: digital markets enable hyper-differentiation; Layer 2: market positions as core/peripheral function combinations; Layer 3: dissatisfaction vs heterogeneity as two feedback dimensions

**关键特征**:
- **三层递进**: 宏观 (Context) → 中观 (Framework) → 微观 (Dimensions)，每层约 150-250 词
- **T1 占 Theory ~50% 篇幅** — 远超标准机制推演型 T1 (~15-20%)
- **Self-Built Theoretical Lens**: 不使用 "Drawing on [theory]..." — 理论框架通过概念构建而非外部导入
- Layer 1 必须建立 "why this context is different" — 否则概念框架缺乏合法性
- Layer 2 必须包含非数字 context 的对比案例 (如 music synthesizer, commercial drones) — 展示概念的跨 context 适用性
- Layer 3 的 "two related assessments" 直接映射到后续 T3 机制链的两个分叉

**适用**: Constructs + Mechanism 组合；现象驱动型；Self-Built Theoretical Lens

**禁忌**:
- 仅当论文确实引入新概念框架时使用 — 如果核心贡献是机制而非构念，T1 应压缩到 15-20%
- Layer 1 不能只有 citation list 无机制 — 必须解释 WHY digital markets are different
- Layer 2 的非数字 context 案例必须来自不同行业 — 同一行业的多个案例不构成 "跨 context" 证据

**与其他变体的区分**:
| | 变体 H (三层递进) | 变体 A (承认多元定义) | 变体 D (双维度对称界定) |
|---|---|---|---|
| T1 篇幅 | ~50% Theory | ~10-15% Theory | ~20% Theory |
| 理论透镜 | Self-Built | 外部导入 | 外部导入或 Self-Built |
| 层级 | 3 层 (Context→Framework→Dimensions) | 1 层 (直接定义) | 1-2 层 |
| 适用构建类型 | 机制推演型 (Construct-Built) | 所有类型 | 竞争假设型、双轨并行型 |

---

## 变体 I：Framework-Anchored 双构念区分（han_pollock_paruchuri 型）

**适用**: 两个构念被领域 conflated，先建立上位维度框架（如 rational/emotional/moral），再将两个构念分别锚定到不同维度。

**模板**:
```
[Construct category]'s [differentiating feature] defines audiences' expectations, and these 
expectations shape [outcome relevance] ([citation]). Differences in [differentiating feature] 
largely stem from the different emphases audiences put on the [dimension A], [dimension B], 
and [dimension C] aspects of different [constructs] ([citation]), which comprise the fundamental 
pillars of judgment and decision-making in social contexts ([citations]). The [dimension A] 
aspect "[direct quote definition]" ([citation]); the [dimension B] aspect "[direct quote 
definition]" ([citation]); and the [dimension C] aspect "[definition]" ([citation]). Although 
all [constructs] reflect all three aspects to some extent, different aspects dominate different 
[constructs] ([citation]).

[Construct A] and [Construct B] emphasize the [dimension A] and [dimension B] aspects, 
respectively ([citations]). [Construct A] builds on [audience]'s [dimension A] assessment of 
[target]'s [characteristics], which then influences future expectations ([citation]). Thus, 
conferring and maintaining [Construct A] involves [process], making the [dimension A] aspect 
dominant in [Construct A]'s [differentiating feature] ([citation]).

[Construct B], on the other hand, is primarily driven by the [dimension B] aspect, as 
[audience]'s [emotional reactions] to [portrayals/behaviors] are how [Construct B] creates 
value ([citations]). Specifically, [mechanism of persistence] ([citation]). The differences 
in [Construct A] and [Construct B]'s [differentiating feature] lead them to affect [outcome] 
differently.
```

**语料锚定**: han_pollock_paruchuri (SMJ) — reputation (rational) vs celebrity (emotional)，基于 Pollock et al. (2019) 的 rational/emotional/moral 三维度框架

**关键特征**:
- **先建框架再锚定**: 不是直接对比两个构念，而是先建立上位维度框架，再将构念分别锚定
- **直接引语定义**: 每个维度使用权威文献的直接引语定义（"reflects audiences' efforts to make reasoned assessments..."）
- **每个构念含**: 定义引用 + 价值创造机制 + 维持/更新方式 + 占主导的维度
- **"on the other hand"**: 对比但不制造对立——两个构念是互补的 (rational ↔ emotional)
- **区分→后果过渡**: 末尾明确 "The differences...lead them to affect [outcome] differently" → 自然过渡到 T3

**适用**: Constructs + Boundary 组合。特别适用于 misconduct/scandal/social evaluation 研究。

**与变体 D (双维度对称界定) 的区分**:
| | 变体 I (Framework-Anchored) | 变体 D (双维度对称界定) |
|---|---|---|
| 区分基础 | 上位三维度理论框架 | 直接对比两个构念的特征 |
| 篇幅 | ~25-30% Theory | ~20% Theory |
| 引用方式 | 直接引语定义维度 | 综述式定义 |
| 过渡 | "lead them to affect...differently" | "In sum, [A] prioritize [X]; [B] prioritize [Y]" |

---

## 变体 J：Context-Anchored Level Distinction（toh_pyun 型）

**适用**: 论文的核心概念创新是区分两个分析层次（system-level vs unit-level），并引入已有文献未触及的 "第三形式" 概念维度。

**模板**:
```
[Layer 1 — System-Level Uncertainty Portrait]:
[System type], much like a traditional [analogue], experiences various forms of uncertainty 
that contribute to variations in its overall performance and growth ([citations]). In its 
nascent stage, there is uncertainty over [aspect 1]. [Elaboration]. Even [aspect 2] may be 
uncertain. Unknowns about [aspect 3] add to market uncertainty. The presence of [competing 
alternatives] further cloud predictability.

On top of these more-typical forms of uncertainty, [system type] additionally faces 
[system-level] uncertainty arising from [specific structural challenge] ([citations]). 
A key characteristic of [system] is [structural description]. Because of these challenges, 
there are additional forms of uncertainty: (1) [convergence uncertainty]; (2) [collective 
action uncertainty].

[Layer 2 — Unit-Level Distinction + Third Form]:
For the [unit] in the [system], the [system-level] uncertainty does not account for all 
forms of uncertainty it faces. Even if [system] is on an unambiguous path to success, there 
is no guarantee that [unit] will perform well. [System-level] uncertainty is mirrored at 
[unit-level]: [two parallel concerns].

However, at the [unit-level], there is an additional layer of uncertainty—whether the [unit] 
can [key concern] in the midst of competition. Past research shows [concern] is not a given. 
[Factors that create this uncertainty, with concrete examples].

The above descriptions illustrate that [unit-level] uncertainty over [concern] can be 
pronounced and separate from [system-level] uncertainty. Not all of the above factors are 
necessarily related to [IV] though. Below, we lay out how [system-level] and [unit-level] 
uncertainty are affected by [IV].
```

**语料锚定**: toh_pyun (SMJ) — ecosystem-level uncertainty (5+ forms) vs firm-level uncertainty (adds value-appropriation as "third form")

**关键特征**:
- **系统画像 → 单元区分**: 先完整描绘系统层面的 uncertainty 全景 (3-5 种)，再区分单元层面的额外 uncertainty
- **"Third Form" Concept Innovation**: 将单元层面的独特 uncertainty 概念化为已有文献未触及的 "第三种形式"
- **具体案例贯穿**: 每层以具体 ecosystem 例子结束 (EV, semiconductor, communications, Microsoft-Intel)
- **范围限定**: 末尾 "Not all of the above factors are necessarily related to [IV]" → 自然过渡到 T2

**适用**: Level 贡献维度; 生态系统/平台/网络研究

**禁忌**:
- Layer 1 不要变成 literature review——每种 uncertainty 1-2 句即可
- "Third form" 必须确实是已有文献未触及的概念维度——不能是现有概念的 relabeling

**与变体 H (三层递进 T1) 的区分**:
| | 变体 J (Level Distinction) | 变体 H (三层递进) |
|---|---|---|
| T1 结构 | 2 层 (System → Unit + Third Form) | 3 层 (Context → Framework → Dimensions) |
| 核心贡献 | Level 跨层概念区分 | Constructs 新概念框架 |
| T1 篇幅 | ~30-35% Theory | ~40-50% Theory |
| 典型期刊 | SMJ | ORSC |

---

## 变体 G：Typology Application 定义型（paruchuri_pollock_kumar2020 型）

**适用**: 已有学术typology区分了现象的两个子类型(如两种failure)，但typology尚未被应用于解释某个特定outcome。通过"what if"问句展示已有typology在此新情境中的解释力

**模板**:
```
[Typology author(s)] argued that [phenomenon category] result from two types: [Type A] 
and [Type B]. [Type A] failures refer to "[definition]," while [Type B] failures refer to 
"[definition]" ([citation]). Most of the [literature] has focused on events that may be 
characterized as [Type B] failures. Key to [standard outcome] are that [conditions for 
standard outcome] ([citations]). However, what if [alternative condition from Type A]? 
We argue that in this situation the [dynamics] are likely to be different.
```

**语料锚定**: paruchuri_pollock_kumar2020 (SMJ) — Connelly et al. (2016) capability vs integrity failure typology → applied to reputation spillover valence

**关键特征**:
- **Typology不是原创，但应用是创造性的**: 核心贡献不是发明typology，而是用已有typology解释新现象的变异
- **"Most of the literature has focused on [Type B]"** → 展示typology中一个类型主导了文献，另一个类型被忽视
- **"However, what if [Type A condition]?"** → "What if"作为论证转折——从"文献做了什么"到"如果考虑另一个类型会怎样"
- **"We argue that in this situation the dynamics are likely to be different"** → 收敛到可检验的预测

**与变体 F（Typology Alignment）的区分**: 变体F是将自己的新构念插入已有分类法；变体G是用已有分类法作为分析框架来解释新现象的变异

**反模式**:
- Typology选择不当——typology的两个类型在解释outcome时无实质性差异
- "Most literature focused on Type B"的声称不准确——如果有大量Type A研究，声称会崩塌
- 使用typology但未充分引用typology的原创作者

**可迁移性**: 高 — 跨构建类型通用。特别适用于AMJ/SMJ中使用已有概念框架解释新现象

---

## 变体 L：New-Construct Legitimation via Multi-Construct Comparison Table（lee_wang 2026 型）

**适用**: 论文引入一个真正的新构念，需要通过与 3+ 个相关但概念不同的"兄弟"构念在多个功能维度上系统对比，来为新构念在已有概念群中开辟合法空间。表格承担"竞争性构念景观测绘"的理论工作——不是装饰。

**模板**:
```
[Concept introduction paragraph]
Building on [related perspective(s)] ([citations]), we introduce the concept of
[NEW CONSTRUCT] to describe how [defining process]. [NEW CONSTRUCT] thus highlights
how [core theoretical insight — the reallocation / cross-domain logic].

[Distinguishing features paragraph]
This definition highlights [N] features that distinguish it from related mechanisms.
First, [NEW CONSTRUCT] is [feature 1 label]: [description]. Second, it is
[feature 2 label] in nature: [description]. Table [N] highlights the distinctive
features of [NEW CONSTRUCT] in comparison to related constructs.

[Multi-construct comparison table — 3+ siblings × 5+ functional columns]
| Perspective | Core Idea | Mechanism | Pattern of Effects | Agency | Limitations |
|---|---|---|---|---|---|
| [Sibling 1] | ... | ... | ... | ... | [gap NEW fills] |
| [Sibling 2] | ... | ... | ... | ... | [gap NEW fills] |
| [Sibling 3] | ... | ... | ... | ... | [gap NEW fills] |
| [NEW CONSTRUCT] | [fills gaps above] | ... | ... | ... | [explicitly addressed] |

[Synthesis paragraph locking the new construct's position]
In sum, [NEW CONSTRUCT] arises when [trigger condition]. Unlike [Sibling 1], which
[focus A], or [Sibling 2], which [focus B], [NEW CONSTRUCT] highlights [unique angle
that fills the gaps in the Limitations column]. In doing so, it shows how [broader
theoretical implication].
```

**语料锚定**: Lee & Wang (2026, *JOM*) — "institutional crowding" 对比 Regulatory Overload / Bureaucratic Trade-Offs / Regulatory Drift & Ambiguity across 5 functional columns；2 个区分特征命名：*salience-driven* 与 *cross-domain*。

**关键特征**:
- **表格前必须有"两个区分特征"段落** — 为新构念命名其核心区分维度（如 salience-driven + cross-domain），让读者在看到表格前已有概念锚
- **列是功能性的**（Core Idea × Mechanism × Pattern × Agency × Limitations），不是单纯的 Definition 对比 — 每列承担一种差异化工作
- **至少 3 个兄弟构念** — 2 个不足以构成"景观测绘"
- **新构念放最后一行** — 让读者在了解所有兄弟后再看到 NEW 如何填补 gap
- **每个兄弟的 "Limitations" 格用于说明该兄弟无法解释什么** — 这正是 NEW 构念的卖点
- **表格后必须有综合段**（"In sum..."）锁定新构念在文献中的独特位置，不能表格即结论

**与变体 E（weng_yang 三层框架+表格对比型）的关键区分**:

| | 变体 E (weng_yang) | 变体 L (lee_wang) |
|---|---|---|
| 表格对象 | 一个构念的两个子类型 | 1 个新构念 + 3+ 个兄弟构念 |
| 列维度来源 | 已有框架的 3 维度 (Swigart 2020) | 作者自行设计的功能性列 |
| 列数 | 3 | 5+ |
| 表格功能 | 内部细分 (sub-type differentiation) | 外部合法化 (new-construct legitimation) |
| 表格后综合 | 收敛到 H1 的两个原因 | 锁定新构念在文献中的独特位置 |

**与变体 I（han_pollock_paruchuri Framework-Anchored 双构念区分）的区分**: 变体 I 通过上位三维度框架对比 2 个构念，**无表格**，对比是互补的（rational ↔ emotional）；变体 L **必须有表格**，对比是竞争性的（NEW 填充 3 个兄弟留下的 gap）

**反模式**:
- 兄弟构念过少（<3）→ 表格沦为二元对比，失去"测绘景观"功能
- 列维度过于抽象（如只有 "Definition"）→ 无法展示新构念在多个功能维度上的差异化
- 新构念自己的 "Limitations" 格为空 → 失去新构念的卖点（应诚实标注其自身边界）
- 表格替代文字论证 → 表格是总结，前后必须有段落建立和锁定新构念的合法地位
- 表格列与正文论证不一致 → 表格必须与散文论证一一对应

**可迁移性**: 高 — 适用于任何"新构念需要通过与多个相关但不同的概念区分来获得合法性"的研究场景：新治理机制、新组织形式、新战略现象、新制度压力类型等。适用于接受 Theory 中正式表格的期刊（JOM / AMJ / SMJ）；ASQ/OS 偏好纯文字理论推演，慎用。

---