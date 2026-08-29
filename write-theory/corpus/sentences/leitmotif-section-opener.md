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
