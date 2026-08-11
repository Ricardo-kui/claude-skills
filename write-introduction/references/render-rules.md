# Render Rules — 模块渲染强制检查（从 SKILL.md Phase 3 下沉，v0.1）

> 由 write-introduction Phase 3 渲染时**必读**：对所选模块逐条过检查。规则按模块分节；🔴 = 硬性（不满足则叙事断裂），🟡 = 强推荐。
> 路径基准：`academic-writing-corpus/...` 以 write-introduction/ 为基准；语料内部 `hooks/...` 等引用以 `academic-writing-corpus/` 为基准。

## Hook

1. 🔴 **Hook→Tension 必须配对**：读 `hooks/_index.md` 的「必须配对表」，所选 Hook 必须配对兼容的 Tension（如 `22-twin-complication` 必须配 `01-despite-progress` 类田野张力）。不兼容组合 = 叙事断裂。
2. 🟡 **禁忌互斥**：所选 Hook 不与同用的其他 Hook 冲突（如 `24-positive-trait-dark-side` 不与 `06-paradigm-challenge` 同用——前者边界反转后者范式颠覆）。
3. 🟡 **human face / 理论驱动例外**：现象或案例型 Hook 优先含 ≥1 个具体 actor、案例或情境，不用 "many firms" 类泛称；若故事契约与目标期刊支持文献共识、经典争论或理论命题直接开场（如部分 ASQ/SMJ 论文），可不强制 human face，但必须在紧邻单元给出可观察的现实后果或判别性问题。
4. 🔴 **能量匹配**：Hook 能量 ≤ Gap 能量（见 SKILL.md Phase 2 能量阶梯）——Incommensurability 用中-高能量开场。

## Tension

1. 🔴 **gap 必须解释"为什么现有解释会系统性漏掉/误置它"**——"few studies have examined" 无解释 = 反模式。新数据或新方法只能说明为何现在可研究，不能单独构成理论 gap；必须落到既有假设、构念边界、分析层次、相互冲突的预测或新情境对理论条件的破坏。
2. 🔴 **被遗漏的东西必须用可操作化构念命名**——"the role of X" 模糊表达不合格；要落到具体机制/条件/过程。
3. 🟡 **theoretical consequence 必须具体**——"limits our understanding" 是废话；要落到某理论的预测能力/边界条件受何影响。
4. 🟡 **反直觉 gap 需要充分支撑**——若 gap 声明反直觉（"surprisingly"），用足以排除最直接替代解释的独立理由和匹配证据建立可信度；理由数量由争议程度决定，不把单篇范文的理由数设成配额。
5. **多 gap 组合的 Tension 写法**——主 gap 驱动主结构（如 Incompleteness 的 "despite progress, X remains unaddressed"），次 gap 作为**补充论证**嵌入同一段或紧邻段：
   - 主 Incompleteness + 次 Application："Not only has [X] been overlooked, but [theory Y], while informative, has not been examined in [new context] where [condition] may alter its predictions."
   - 主 Inadequacy + 次 Confusion："Existing work assumes [view A], but this overlooks [perspective B]—and the evidence itself is split: some studies find [result 1] while others report [result 2]."
   - **纪律**：次 gap 篇幅 ≤ 主 gap 的 1/3；两个 gap 必须有逻辑连接（不是两个独立缺口的并列）；Tension 收尾句回到**主 gap**（它驱动后续 Theory Lens/Preview）。
6. **渲染 Tension 前加载** `references/gap-deepening-reference.md`：找法标签（confusion/neglect/application spotting）+ neglect 三子版 + 三档风险权衡 + Müller-Bloch 6 类 + gap verification，微调措辞与风险预警。

## Stakes

1. 🔴 **So-what 测试**（§14.3.3 强制）：陈述读者无知/误解状态后自问 "So what?"——答不出具体后果则 stakes 不够，换更强的 stakes 类型。
2. 🟡 **量化优先，narrative 兜底**：有政府统计/行业报告/上市公司数据则量化；无法量化用具体 narrative Stakes（公司/市场/决策情境）。无数字且无具体案例 = 退回 generic，不合格。
3. 🟡 **who suffers 具体化**：落到具体 stakeholder 类型（哪类企业/决策者/群体），用 "firms"/"managers" 泛称不达标。

## Literature Turn（对话编织纪律——防止"罗列而非对话"）

1. 🔴 **每条引文必须锚定可还原的支持内容**——实证研究写方向/边界；理论研究写命题/假设；review/meta 写共识/异质性；构念来源写定义/区分；情境来源写事实。非实证来源按其真实类型书写，不强改"方向性发现"。
2. 🔴 **≥2 引文的句子说明各引文共同或分别支持什么**——"X has been widely studied (A; B; C; D)" 是堆叠而非综合；真正支持同一共识时可合并，但须由 review/meta 或代表性证据证明该共识。
3. 🟡 **多文献流必须均衡呈现**——Synthesized/Non-Coherence 策略有 2+ 文献流时，每流都要有实质发现展示，第二流也要有内容（"some studies in other fields have also examined..."是稻草人信号）。
4. 🟡 **用文献流的张力/共识/分歧驱动叙事**——显化两流的关系（although / however / while A emphasizes X, B focuses on Y / these perspectives offer incompatible predictions）。
5. 🟡 **引文来源优先用 Phase 1.5 Vault Brief 的推荐引文**（含发现方向），不凭空编造。每条文献流用足以证明其核心命题、边界或分歧的代表性证据；review/meta 仅在确实承担共识或异质性判断时优先，不设固定篇数或来源类型配额。
6. 🟡 **标签用文献流自己的术语**——"the corporate political strategy literature"若文献数据库搜不到 = 读者无法定位你在和谁对话。
7. 🟡 **Literature 是 constructed 而非 received**（GBL Ch02 Move 2）——"文献"没有预置仓库，是主动 select & shape 为贡献腾出空间（"configure the available pieces of a jigsaw puzzle so they contour an opening into which your storyline fits"）。Synthesized 要 "rewrite each literature to highlight commonality"、Non-coherence 要 "position camps against each other"——不是中立综述，是为贡献**重新组织**文献。纪律：有灵活性但 within outer limits——不能歪曲文献立场、不能像稻草人把文献描绘得比实际更片面；rewriting 是合法的学术建构，misrepresentation 不是。
8. 🟡 **区分 Literature 1 与 Literature 2**（Shepherd & Wiklund 2020）——Literature 1 = 提供 gap 的本领域文献；Literature 2 = 提供填补 gap 的理论资源（借用的理论）。两者都要在引言可见：Literature Turn 展示从 Lit 2 借了什么，Contribution 说明回馈 Lit 2 什么。只借不回馈 = 拒稿信号。

## Theory Lens

1. 🔴 **必须直接回应 Tension 的 gap**——引入的理论要能解释 Tension 指出的缺口（关键词重叠测试：Tension 的 gap 关键词与 Theory Lens 的理论核心词应有交集）。引入与 gap 无关的理论 = 反模式。
2. 🟡 **core claim 含方向性预测**——"We argue that X affects Y through [mechanism]"，不用 "we examine the role of X" 无方向表达。
3. 🟡 **与 Preview 一致 + 与 Theory 章节一致**——Theory Lens 预告的理论来源与 Preview 的研究设计、write-theory 实际发展的理论一致（不串戏）。
4. 🟡 **避免理论堆砌**——3+ 理论各担 1 句 = 反模式；多理论时说明整合机制而非并列。

## Preview

1. 🔴 **motion 信号词**——从理论世界切换到实证世界的主动信号（"To test these arguments," / "We evaluate our predictions using..."）。不用 "In the next section, we describe our methods"（纯结构导航，无 motion）。
2. 🟡 **发现预览不空承诺**——预告发现方向必须有实证数据支撑；"we find support for our hypotheses" 不合格，要说方向/大小/意外发现。
3. 🟡 **不过度承诺**——预告核心发现方向即可，细节留 Results；逐条预告所有 H1-H4 = 过度承诺。
4. 🟡 **情境 justify**——不只描述数据，用 1 句说明该情境为何适合检验理论。

## Research Question

`research-questions/[canonical_id].md`（仅当需要显式 RQ 时读取——如 JMS/JOM 目标期刊或反直觉发现需设问）。若用户不确定 RQ 或 RQ 看起来像 superficial gap-driven（"few studies have examined X"），加载 `references/knowledge-weaving-rq.md`——从 knowledge claims 的发育状态（stable/fragile/unstable）推导 RQ，而非凭空提问。

## Contribution

1. 🔴 **紧扣前文 Gap**——mechanism gap → Mechanism 贡献句式；boundary gap → Boundary 句式。贡献维度与 Gap 类型对齐，gap 说机制、贡献说构念 = 错位。
2. 🟡 **聚焦 2-3 个充分展开的贡献**（实证论文默认）；5+ 个贡献各一行 = 散弹。理论论文走 AMR 单核自明（见 `references/theory-paper-amr-mode.md`）。
3. 🟡 **每个贡献锚定不同文献流或不同 Makadok 维度**——第二贡献只是第一的 "also" = 实质是同一件事。
4. 🟡 **contrast with prior 说清 prior 具体说了什么**——"不同于 X" 太弱；用 "In contrast with prior studies suggesting [dominant view], we contend that..."。
5. 🔴 **用 Davis's Index 判断 "What will we learn"**——加载 `academic-writing-corpus/storytelling/daviss-index.md`（26 类 interestingness：Order from Chaos / What seems bad is really good / DV is IV / What seems stable is really changing 等）。**这是拒稿首要原因**——贡献必须回答"读者的理解会怎样改变"，用 Davis 类型提供改变的语言（"What seems X is really Y"）。
6. 🟡 **区分 consensus shifting vs creation**（Hollenbeck 对 Davis 的延伸）——shifting = 挑战公认假设（"Contrary to extant theory... we show..."）；creation = 澄清文献中并存的分歧线（"two clear lines of discrepant thought... we clarify/resolve"）。两种路径措辞不同，选错会让贡献声明与证据不匹配。
7. 🟡 **回馈 Literature 2**——贡献主要回到 Literature 1，但末段说明对 Literature 2 的反馈：adapt / extend / challenge。
8. 🟡 **区分 contribution output 类型**（Makadok 2018）——explanation / prediction / prescription 是三种不同 output。贡献声明明确本文产出哪种：能否说出 "theory can now explain/predict/prescribe Y that it could not before"？说不出 = 贡献声明太模糊。

## Transitions / Differentiation

- Transitions: `transitions/[canonical_id].md`（按需读取段落间过渡模板）
- Differentiation: `differentiation/01-prior-work-boundary-clarification.md`（仅当存在极易混淆的 prior work 时读取——多数论文不需要，见「模块跳过指南」）
- Differentiation 放置：嵌入 Literature Turn、Tension 或 Contribution；不在 Contribution 之后新增独立 Differentiation 段重新开启问题。

## 变体选择

- 按适用场景、证据状态、研究情境和期刊选**一个主推变体**（不默认变体 A）；仅当两个方案会实质改变故事路径时，额外给 **1 个**备选及切换条件——不为每个模块机械输出两个备选。
- 优先级：corpus 文件的变体级约束（适用场景/范文锚定）> 用户研究情境匹配 > 路由表的模板级推荐。项目故事的具体组织只能由 canonical `story` 与 `story.integrity` 的已确认内容收窄；不得由故事类型、legacy blueprint 或 exemplar 身份调制。
