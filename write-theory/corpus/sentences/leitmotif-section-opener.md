# 段首主导动机串联句语料库（Leitmotif Section Opener）

**功能**: 当 Theory 章节包含多个假设（H1, H2, H3...）且它们共享同一个底层理论构念时，在每个假设段落（或小节）开头使用**结构重复的引导句**作为 leitmotif（主导动机），把分散的假设缝合成一个连贯的理论论证。读者每读到新假设，先被"带回"核心理论锚点，再展开该假设特有的边界逻辑。

这是对"逐段重新介绍理论"反模式的替代——不是每个 H 都从零起兴，而是用一句结构固定的"回扣句"快速重置语境，把段落正文预算留给该假设独有的论证。

---

## 单理论多假设的段首主导动机（Darby 2025 型）

**适用**: 主效应 + 多个调节假设，所有假设都从同一核心理论的同一构念派生。Incompleteness × Mechanism（主）+ Boundary（次）组合。

**模板**:
```
"[Core theory] suggests that [characteristic of the delegated task / focal 
phenomenon]—in this context, [the study's specific phenomenon]—may influence 
[the underlying construct that anchors ALL hypotheses, e.g., information 
asymmetry / perceived risk / goal congruence] ([citation]). This may influence 
[the dependent process the theory explains, e.g., the extent to which agents 
engage in the focal behavior]. [This study / We] thus examine[s] [the 
moderating / main effect of the current hypothesis's specific variable]."
```

随后展开该假设特有的机制链（buffering / enhancing / 对称对比），最后给出 H[N]。

**原文锚点** (Darby, Wowak, Ketchen & Connelly 2025, JSCM "An Agency Theory Perspective on Activist Investors and Supply Chain Failures: The Case of Product Recalls"):
> H1 段首: "At the core of agency theory is the agency problem, which arises because of (i) goal incongruence—i.e., principals and agents have different aims and risk preferences, and (ii) information asymmetry—i.e., agents know more about the firm's operations than principals know (Kauppi et al. 2024)."
> H2 段首: "Agency theory suggests that characteristics of the delegated task—in this context, managing product recalls—may influence the degree of information asymmetry between principals and agents (Eisenhardt 1989)."
> H3 段首: "Previous research suggests that the severity of an event also may influence the extent to which agents try to manage principals' perceptions (Graffin et al. 2016)."

**语料锚定**:
- Darby, Wowak, Ketchen & Connelly (2025, JSCM) — agency theory 三假设段。三个假设段落分别以结构平行的引导句开头，均回扣"information asymmetry between principals and agents"这一核心构念：
  - H1 段首（主效应）: "At the core of [agency theory] is the agency problem, which arises because of (i) goal incongruence... and (ii) information asymmetry..."
  - H2 段首（defect type 调节）: "[Agency theory] suggests that characteristics of the delegated task—in this context, managing product recalls—may influence the degree of information asymmetry between principals and agents..."
  - H3 段首（severity 调节）: "Previous research suggests that the severity of an event also may influence the extent to which agents try to manage principals' perceptions..." （severity 变体略改措辞，但同样回扣"manage principals' perceptions / impression management"这一机制锚点）

**关键特征**:
- **结构重复，内容递进**: 三个段首句法骨架相同（"[Theory] suggests that [X] may influence [anchoring construct]..."），但 [X] 逐段变化（delegated task 的整体 → defect type → severity），形成"同锚点、不同边界"的递进。
- **回扣而非重述**: 引导句不重新解释整个理论（那是 H1 之前概念段的任务），只用一句话把读者拉回核心构念，然后立刻进入该假设的独有逻辑。
- **为段落正文省预算**: 因为引导句已锁定理论锚点和该假设的切入变量，段落剩余篇幅可以专注论证"为什么这个变量改变 anchoring construct 的程度"，而非重复"什么是 agency theory"。
- **跨假设的可读性锚**: 当审稿人/读者跳读到 H3 时，段首句立刻告诉他们"这仍在 agency theory 的 information asymmetry 框架内，只是换了一个影响 asymmetry 程度的变量"。

**与"统一框架型调节变量选择"(hoffmann2024) 的区分**:
| | 段首主导动机串联 (Darby2025) | 统一框架型 (hoffmann2024) |
|---|---|---|
| 结构层级 | 句式级（每个 H 段首一句回扣） | 框架级（引入一个 organizing taxonomy） |
| 锚定对象 | 单一核心理论构念（information asymmetry） | 外部分类系统（intrinsic vs extrinsic constraint） |
| 适用假设数 | 2-4 个假设共享一个构念 | 恰好 2 个对称调节变量 |
| 出现位置 | 每个 H 小节开头（重复 N 次） | 调节讨论前的总览段（出现 1 次） |
| 风险 | 过度重复显得机械 | 框架过于庞大喧宾夺主 |

两者可叠加：先用 hoffmann2024 框架引入两个调节，再用 leitmotif 在每个调节段首回扣框架中的对应类型。

**与"理论内部嵌入型"(wang2024) 的区分**: wang2024 是把 moderator 映射到核心理论的*次级假设*（broaden vs build）；本句式是把*每个*假设都映射到*同一个*核心构念（information asymmetry），不拆分理论。wang2024 用于"理论有多个子假设"的场景；本句式用于"理论只有一个核心机制，但有多个边界条件改变其强度"的场景。

**禁忌**:
- 引导句的 [anchoring construct] 必须真正贯穿所有假设——如果 H3 实际上回扣的是另一个构念（如换成了 resource dependence），则不能用同一个 leitmotif，否则强行串联会暴露理论不连贯。
- 不要把引导句写成对核心理论的完整重述（超过两句即沦为冗余）；它应是"一句话重置"，不是"一段话复习"。
- 段首句结构重复是刻意的修辞选择，但词汇应有微变（如 H2 用 "may influence the degree of information asymmetry"，H3 改用 "may influence the extent to which agents try to manage principals' perceptions"），避免逐字雷同触发查重/审稿人疲劳。
- 单一假设（无调节）的 Theory 不需要此手法——leitmotif 的价值在多假设串联，单假设用它会显得刻意。

**反模式（corpus 应警告）**:
- "每个 H 段首都从 'Agency theory is one of the most important theories...' 开始" → 这是逐段重新起兴，不是 leitmotif 回扣。leitmotif 回扣的是*构念锚点*，不是*理论定义*。
- 三个段首句除了主语不同完全一样 → 机械重复；应让 [X] 的变化驱动句意的递进。
- H1 用 leitmotif 但 H2/H3 突然换完全不同的开篇结构 → 串联断裂，读者失去锚点。

---

## 调用与下游接口

- 与 `corpus/sentences/moderation.md`（调节机制修改句）互补：本文件管"段落怎么开头回扣理论"，moderation.md 管"回扣之后机制怎么论证"。
- 与 `corpus/subprotocols/moderator_selection_frameworks.md` 的 "information_asymmetry_meta_framework" 模式协同：后者提供"多 moderator 共享一个构念"的*选择理由*，本句式提供该结构在*写作层面*的段首实现。
- 路由：Theory 章节含 ≥2 个调节假设、且调节均锚定同一核心理论构念时，write-theory 可建议在每个 H 段首套用本 leitmotif。


### 句式 A：标签式段首+分层推进 opener（westphal_bednar2005 型）

**模板**:
> "[Moderator label]. On one level, [W] between [actors] should [lower] the perceived risk of [voicing]. [Justification] ([citations]). Accordingly, when [W is high], [actors] should be less hesitant to [voice]. Moreover, [second path]. Therefore, [convergence to construct]."

**来源**: westphal_bednar2005 (ASQ), Theory P11/P12 段首；P6 "On one level"/"At the same time"

**原文锚定**:
> "Personal friendship ties. On one level, personal friendship ties between group members should lower the perceived risk of voicing a minority opinion."
> "On one level, there are social risks from expressing a minority opinion on corporate boards."

**关键特征**:
- 段首用两三个词的裸标签（"Personal friendship ties."）命名本段 moderator，充当小标题功能而不必设正式小节
- 标签后立即接 "On one level, ..." 给出可检验的方向判断，标签与判断句加起来不足 25 词完成 Topic 拍
- "On one level... At the same time... Moreover..." 的分层递进词族贯穿全节，标记"表层判断→补充机制→反顾情境"的推理层级，是全文的节奏指纹

**适用**: 多 moderator 平行结构（每段一个 moderator）的假设推导段首；需要在不设 subsection 的前提下给段落视觉锚点的 Theory

**禁忌**: 裸标签必须是构念名本身（名词短语），不得用完整句子；"On one level" 词族在单篇使用三到五次即达饱和，逐段滥用会变成口头禅


### 句式 B：机制枢纽修辞性问句（"How then might ... ?" Pivot）

<!--
pattern_id: rhetorical_question_mechanism_pivot
build_type: 跨类型（句式级）
source_papers: ["carpenterwestphal2001_AMJ"]
confidence: high
status: VERIFIED — expert_audit_override (Westphal 系裁决: 用户点名最爱学者,引言/理论单源足矣)
sentence_position: topic_sentence
-->

**句位**: 段首 Topic 句位——在理论透镜已立、即将进入具体机制推导的分支起点，用自问句把"框架"切换为"推导"。

**句式骨架**:
```
How then might [IV] [direction verb] [actor]'s ability to [outcome] in
[context]? We suggest that [core claim of this branch].
```

**变体**（同句位措辞候选）:
- "How then might [IV] [verb] [outcome] in [context]?" — 标准形式；"then" 承接前文理论铺垫
- "How, though, does [IV] translate into [outcome]?" — 强调转换而非增强
- "Why should [IV] [verb] [outcome] when [condition]?" — 问"为什么"而非"如何"，适配 warrant 密集段

**为什么有效**: 把读者刚建立的被动理解（"有道理"）主动转化为求知状态（"怎么发生的？"），问句本身即宣布本段任务是机制推导而非框架重复；"then" 标记这是从透镜到推导的**推进**，段落分工清晰。
**注意事项**: 一条 why chain 至多使用一次（本文仅在两个情境分支起点各用一次）；问句后必须紧跟 "We suggest that ..." 给出分支核心判断，不能问完就铺文献；问句内容必须真能被本段回答。
**反模式**: 连续多段用问句开头（变成口头禅）；问句只修辞性装点、下一段并不回答它；用问句掩盖核心判断缺位（段首无方向性主张）。

**原文锚定**:
> "How then might directors' ties to other boards enhance their ability to monitor and advise management on the implementation of existing strategies in a stable environment?"
> "We suggest that directors will be better able to contribute to strategy in such an environment when their other board ties are strategically related to the focal firm."

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:sentence_rhetorical_question_mechanism_pivot -->


### 变体 C：绩效文献→行为变量改指 pivot（Gulati_1999 型）

<!--
pattern_id: performance_to_behavior_repurposing_pivot
build_type: 跨类型（句式级；Topic 句位）
source_papers: ["gulati_1999_network_location_and_learning_the_influence_of_n"]
verification_status: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED)
sentence_position: topic
-->

**句位**: 小节 Topic（引入 IV 构念的小节首段——把既有文献的默认 DV（绩效差异）改指向本文的行为 DV）

**句式骨架**:
```
[文献默认用途承认] While [scholars in the parent literature] have primarily applied [theoretical apparatus] to explain [default outcome: sustained performance differences], [variation in the construct] can also be the basis for [focal strategic behavior] ([citation]).
[本文焦点声明] In this instance, my/our concern is not with [adjacent construct type] but with [focal construct type] that enable [actors] to [focal behavior] with greater ease.
```

**变体**（同句位措辞候选）:
- "not so much for [default outcome] but, rather, as [focal function: an important enabling condition for future cooperation]" — 后果焦点改指（DV 从绩效改为行为可能性，可放在小节后部回收）
- "variation in [construct] can also be the basis for [behavior]" — 同一构念变量的新 DV 用途声明

**为什么有效**: 一句话同时完成三件事：承认借用文献的合法性（不需要新理论）、声明 DV 改指（绩效→行为）、划清与邻接构念类型的边界（not with A but with B）；预先回答"这个绩效文献传统凭什么适用于本文的行为 DV"。

**注意事项**: 默认用途承认必须准确（该文献确实以绩效为主 DV）；改指后的 DV 要有理论接口（enabling condition → 行为倾向），不能只换词；若借用涉及机制差异，需衔接"Recognize X but Leverage Y"类论证。

**反模式**: 无默认用途承认直接挪用文献（审稿人问"这不是绩效文献吗"）；改指后机制不跟（构念为绩效而生却硬套行为 DV）。

**原文锚点** (Gulati 1999, SMJ):
> "While strategy scholars have primarily applied various capabilities-based arguments to explain sustained performance differences across firms, variation in capabilities can also be the basis for strategic behavior."

**原文锚点**（后果焦点改指变体）:
> "In this context, I consider the implications of network resources not so much for the performance of firms but, rather, as an important enabling condition for future cooperation."

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:performance_to_behavior_repurposing_pivot -->


### 变体 C：阶段路标段首（"The consequences for [DV]." Stage Signpost，Gulati_Westphal_1999 型）

<!--
pattern_id: consequence_stage_signpost
build_type: 跨类型（句式级）
source_papers: ["gulati_westphal_1999_cooperative_or_controlling (ASQ)"]
confidence: high
status: VERIFIED — expert_audit_override (Gulati/Westphal 系单源裁定 2026-09-06, paper_count=1)
sentence_position: topic_sentence
-->

**句位**: 小节内段首 Topic 位——透镜/前提铺垫段之后、后果推导段起点，用一个独立短句宣布论证进入"后果"阶段。

**句式骨架**:
```
[透镜/前提铺垫段(s)]...
The consequences for [DV]. [首句展开] There are several possible consequences
of [X] on the prospects of [DV]... On one level, ...
```

**变体**（同句位措辞候选）:
- "The consequences for [DV]." — 裸路标（本文在两个极小节中逐字复用，形成节奏指纹）
- "[构念] and [DV]." — 构念对路标（变通形式）
- "The implications for [DV] are twofold." — 带预告的路标

**为什么有效**: 两段式小节（先透镜铺垫、后后果推导）用同一路标切换阶段，读者在每个小节的同一位置获得同样的结构信号；路标逐字复用让平行小节的对称性可见。
**注意事项**: 路标后首句要立即给出后果的具体展开方向（不能路标后再铺垫）；同节内复用需真平行（两小节结构同构）才形成指纹，否则是噪音。
**反模式**: 每段都加路标（段落碎成目录）；路标句后紧跟新透镜引入（阶段切换语义混乱）。
**与近亲变体的区分**: "标签式段首（westphal_bednar2005 型）"的裸标签是构念/moderator 名，功能是给平行 moderator 段做视觉锚点；本变体的路标命名的是论证阶段（consequences），功能是小节内从"铺垫"切到"推导"。
**原文锚点**:
> "The consequences for alliance formation. There are several possible consequences of independent board control on the prospects of alliance formation between the focal firm and manager-directors' home companies."


<!-- wb:gulati_westphal_1999_cooperative_or_controlling:sentence_consequence_stage_signpost -->


### 句式 D：未决不足桥接问句段首（If-X-Alone-Cannot Question Bridge，Gulati_1999_AJS 型）

<!--
pattern_id: if_alone_cannot_question_bridge
build_type: 跨类型（句式级；机制小节边界 Topic 位）
source_papers: ["gulati_1999_where_do_interorganizational_networks (AJS)"]
verification_status: VERIFIED — expert_audit_override (Gulati 系单源裁定 2026-09-06, paper_count=1)
story_fidelity: section_variant
sentence_position: topic_sentence
-->

**句位**: 机制小节开头的 Topic 位——上一机制的不足已在其小节末暴露（常配"必要不充分交棒"），本小节以问句承接并宣布本节任务。

**句式骨架**:
```
If [在位机制] alone cannot offer sufficient cues for [行动者] to [行为], how do they decide [新问题维度]?
Building on [文献综述锚点] and on [自有证据：our own fieldwork], we shall argue that [本节核心主张].
```

**为什么有效**: 问句把上一节留下的缺口复述为悬念；"alone" 一词精确地把不足归因于机制覆盖面而非机制错误（不推翻已推导的 H）；"Building on... and on our own fieldwork" 双重授权句随即接住问句——问-答间距仅一句，悬念不悬置；we shall argue 保持作者责任声。

**注意事项**: 每个机制小节至多一次；问句的"新问题维度"必须与上节末的问题改写一致（呼应交棒转场的 whom 问题）；问句后必须紧跟主张句（We shall argue / We propose），不能问完就铺文献。

**反模式**: 连续多节用问句开场（变成口头禅）；问句后先铺文献再给主张（悬置过久）；"alone" 语义滑向"机制错误"（应为覆盖面不足）。

**与句式 B 的区分**: 句式 B（How then might...?）在理论透镜已立后的分支起点切换"框架→推导"，问句不含让步从句；本句式在机制小节边界处承接上一机制的**覆盖面不足**并携带 "If X alone cannot..." 让步从句，问句本身即复述了缺口。

**原文锚点** (Gulati 1999, AJS):
> "If interdependence alone cannot offer sufficient cues for organizations to cooperate with one another, how do they decide with whom to build strategic alliances? Building on a growing body of research ... and on our own fieldwork, we shall argue that organizations address the potential hazards ... by relying on information provided by existing interorganizational networks."

<!-- wb:gulati_1999_where_do_interorganizational_networks:c7_if_alone_cannot_question_bridge -->
