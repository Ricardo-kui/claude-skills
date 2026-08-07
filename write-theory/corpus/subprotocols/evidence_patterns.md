# Evidence Patterns

本文件收集 Theory 中证据的类型、功能、摆放位置以及文献引用的三要素句式模板。

---

<!-- 
pattern_id: three_element_citation_mechanism_anchor
build_type: 跨类型
source_papers: ["Singh_Grewal_2023_JMR", "Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Three-Element Citation — Concrete Finding + Argument Summary + Link to Mechanism

**适用场景**: 所有 Theory 段落。每个 citation 都应该同时完成三件事：报告具体发现、总结其 argument、链接到当前机制步骤。
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*; Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Author] (year) found that [concrete finding] — [argument summary].
This suggests that [mechanism step], because [theoretical reason].
```

**示例**（基于 Singh & Grewal）:
```
Laffont and Tirole (1991) outline several mechanisms (e.g., bribes, lobbying, personal relationships, 
campaign contributions, public criticism) that interested parties can use to exert influence — 
a finding that highlights lobbying as a prominent means to establish political influence.
This suggests that firms can leverage lobbying to shape regulatory enforcement, 
because regulators are responsive to political pressure from firms.
```

**为什么有效**: 把 citation 从"名字罗列"升级为"机制步骤的锚点"。

**注意事项**: 
- concrete finding 必须具体（数字、关系、机制清单）
- argument summary 必须总结作者的论点，不是研究方法
- link to mechanism 必须明确说明这个发现如何支撑当前步骤

**反模式**: "Smith (2010) argues that X affects Y" — 只有 argument summary，缺少 concrete finding 和 link。

---

<!-- 
pattern_id: case_as_warrant_for_mechanism
build_type: 机制推演型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM", "Moon_Tuli_Mukherjee_2023_JM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Case as Warrant for Mechanism Step

**适用场景**: 当机制步骤比较抽象，需要让读者在经验世界中"看见"它时。用企业/行业案例作为 Warrant。
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*; Moon, Tuli, and Mukherjee (2023), *Journal of Marketing*

**骨架**:
```
[Mechanism Step] [IV] may lead to [state], which prevents firms from [action].
[Case as Warrant] For example, [company/context] [concrete situation]. 
As a result, [company] could not [action], suggesting that [mechanism step] operates in practice.
```

**示例**:
```
The resource benefits of political ties may lead to structural lock-in, preventing firms from 
streamlining existing operational systems. For example, in response to the government's call for 
a reduction in poverty, politically connected firms in China are pressured into using cost-inefficient 
suppliers from poverty-stricken regions (China Daily, 2017). Dahu Aquaculture Co. Ltd., which faced 
significant overcapacity during the COVID-19 pandemic, could not lay off 70 employees to save 
operational costs because the chair of the board was a provincial delegate and was expected to 
take care of social welfare (Hunan Daily, 2021).
```

### 子型 B：利益相关者反应作为 Audience-Reality Warrant

**骨架**:
```
[Academic evidence] establishes that [information/action] is relevant to [decision task].
Consistent with this mechanism, when [organization] changed [practice], [identified stakeholder]
publicly explained that the information had been useful for [specific task]; a separate
[institutional decision/case] elicited the same concern. These reactions do not establish
causality, but they show that the proposed audience recognizes the theorized function in practice.
Therefore, we expect [directional relationship].
```

**来源**: Moon, Tuli, and Mukherjee (2023), *Journal of Marketing*, H2 推导段

**与原子型差异**: 原子型用企业处境展示一个抽象机制如何实际运作；本子型用具名利益相关者对组织/监管决策的反应，验证理论所设定的 audience、decision task 与信息价值并非作者虚构。学术证据承担一般化，现实反应承担 face validity，理论回收句把两者重新接回假设。

**诚实边界**: Stakeholder reaction 只能作 warrant，不能作为效应大小或因果方向的证据；若只有单一匿名评论或评论者与假设中的受众不一致，不应使用。

### 子型 C：具名案例作为预设异议反驳（Named-Case Objection Rebuttal）

**骨架**:
```
[Anticipated objection — 作者替读者说出] One might think that [mechanism premise] would not
be a problem in [this context], i.e., [why the context seems special].
[Rebuttal pivot] This is not, however, always the case.
[Named case] For example, in the recent [Company/event], [actor] knew of [problem] in
[time/place], [duration] before [taking action] ([news citation]).
```

**来源**: Haunschild and Rhee (2004), *Management Science*——惯性前提看似不适用于安全召回情境（"any problem that poses a potential threat to consumer safety would be swiftly dealt with"），作者用 Firestone/Bridgestone 案例反驳：Ford 早在 1998 年就知道委内瑞拉市场的轮胎问题，两年后才更换。

**与原子型差异**: 原子型用案例**正面展示**机制如何运作（warrant）；本子型用案例**防御性反驳**"本情境例外"的预设异议——案例证明例外不存在，而非证明机制存在。功能一攻一守，不可互换。

**诚实边界**: 案例必须具名、可核查、与异议直接对应（行业特殊性异议不能用其他行业案例反驳）；反驳后立即回到机制推导，不展开案例细节；异议必须是读者真实会提出的——反驳稻草人异议反而暴露论证焦虑。

**为什么有效**: 案例把抽象机制具体化，同时显示机制的边界条件。

**注意事项**: 
- 案例必须直接对应机制步骤，不能是泛泛的行业描述
- 案例来源可以是新闻报道、案例研究、行业报告，不一定是学术论文
- 案例后要有明确的理论回收句

**反模式**: 案例只是装饰，没有回收到机制论点。

---

<!-- 
pattern_id: theory_as_warrant_conceptual_argument
build_type: 跨类型
source_papers: ["Singh_Grewal_2023_JMR", "Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Theory as Warrant — Conceptual Argument for Mechanism Step

**适用场景**: 当机制步骤需要理论合法性而非经验证据时使用。常见于机制链的第一步或最后一步。
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*; Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Mechanism Step] [IV] creates [state].
[Warrant] This is consistent with [theory], which posits that [core theoretical argument] ([foundational citation]).
```

**示例**（基于 Shen et al.）:
```
Political ties may induce complacency, decreasing firms' motivation to build an efficiency-driven culture.
This is consistent with the political embeddedness perspective, which posits that firms embedded in 
co-optation relationships with governments face both opportunities and constraints (Okhmatovskiy, 2010).
```

**为什么有效**: 理论引用为机制步骤提供合法性，避免机制变成作者的主观断言。

**注意事项**: 
- 必须说明理论的核心论点是什么
- 必须解释为什么这个理论适用于当前机制步骤
- 不能只写 "consistent with [theory]" 而不展开

**反模式**: 用理论 citation 代替机制推演（"Smith (2010) argues X affects Y. Therefore..."）。

---

<!-- 
pattern_id: evidence_function_contrast_pivot
build_type: 机制推演型 / 反直觉预测型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Evidence Function — Contrast as Pivot

**适用场景**: 当论文需要从对立理论转向自己的理论时使用。Citation 的功能不是支持，而是"设定对手"。
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[Contrast citation] From an efficiency perspective, [IV] should not affect [DV] because [reason] ([citation]).
[Pivot] However, a [theory] perspective predicts the opposite.
```

**为什么有效**: 明确区分"支持性证据"和"对比性证据"，让转折有据可依。

**注意事项**: 
- contrast citation 必须总结对立理论的 argument
- pivot 后必须立即开始建立自己的机制

**反模式**: 把 contrast citation 当成支持性证据使用。

<!--
pattern_id: practitioner_report_warrant
build_type: 跨类型（证据类型扩展）
source_papers: ["Du_Tsolmon_2024_ORSC"]
confidence: low
status: needs_validation
-->

## Pattern: Evidence Type — Practitioner Report as Warrant

**适用场景**: 当学术文献对某机制的证据不足或过于抽象，需要用 practitioner 报告/案例建立实践相关性和外部效度时。适合 M&A、战略实施、组织变革、供应链等 practitioner 文献丰富的领域。
**范文来源**: Du and Tsolmon (2024), *Organization Science*（McKinsey 200-deal 分析支撑 structural integration 重要性）

**骨架**:
```
According to a [year] [consulting firm] analysis of [N] [phenomenon], [finding]. 
The researchers note, '[quote establishing importance]' and caution that 
'[quote establishing risk].' In these critical [phase], [actor] cannot risk 
[negative outcome] as '[quote establishing mechanism].'
```

**为什么有效**: 咨询报告的大样本（如 200+ deals）为机制提供 practitioner 层面的外部效度；直接引语（'the hardest stage'/'not assured without well-executed integration'）比学术引用更具实践紧迫性；与学术证据并置形成双源 warrant；practitioner 的具象隐喻（'run water through those pipes'）为抽象构念提供直觉。

**注意事项**:
- practitioner 证据只能是 warrant（补充），不能替代学术机制论证
- 引语必须与理论主张直接相关（不能只是"行业很重要"式的泛泛引用）
- 咨询报告必须有大样本或系统性，不能用单一 anecdote
- 最佳用法是与一个学术案例并置（如 McKinsey 报告 + Haspeslagh & Jemison 钢铁案例），形成 practitioner+academic 双源 warrant

**反模式**: 用 practitioner 引语代替机制推演（"McKinsey says integration is hard. Therefore H1."）；或引用无样本规模的单一专家观点。

---

<!--
pattern_id: original_mini_analysis_premise_warrant
build_type: 跨类型（证据类型扩展）
source_papers: ["Haunschild_Rhee_2004_MS"]
confidence: low
status: needs_validation
-->

## Pattern: Evidence Type — Original Mini-Analysis as Premise Warrant

**适用场景**: 机制链依赖一个**经验性前提**（如"X 类事件比 Y 类事件更显著/更受媒体关注"），已有文献未直接证明它；前提若假，整条机制链坍塌。作者在 Theory 节内嵌入一个**小型原创描述性分析**（计数 + 比例 + 简单检验）当场证明前提，而非断言。

**范文来源**: Haunschild and Rhee (2004), *Management Science*（为支撑"非自愿召回更显著"这一 attention 阵营的承重前提，当场统计：1998 年 235 起召回中仅 22% 为非自愿，而 ABI/INFORM 368 篇商业报道中 47% 涉及非自愿召回；Pearson χ²(1)=37.2067, p<0.001）。

**骨架**:
```
[Premise to defend] We argue that [X-type events] are more [salient/visible/consequential]
than [Y-type events].
[Base rates] According to [data source], there were [N1] [events] in [period].
Of these, [p1]% were [X-type] and [p2]% [Y-type].
[Mini-analysis] We [counted/analyzed] the [coverage/reports] of these [events]:
of [N2] [articles], [q1]% discussed [X-type]. A test of [expected versus actual] is
significant ([statistic], p<[value]), supporting the idea that [premise].
[Recovery to theory] The [coverage] of [X-type events] is likely to be both a cause and
a consequence of the [premise property] of these events.
```

**为什么有效**:
- 把"作者断言"升级为"当场可验证的事实"——前提辩护不依赖读者信任。
- 在 Incommensurability/竞争假设设计中，它把某一理论阵营 steelman 到最强（前提扎实），使后续裁决更有说服力；亦满足 front-end contract 对"strongest prior conversation"的要求。
- 检验统计量的出现向审稿人发出"作者对前提与对假设同样严谨"的信号。

**注意事项**:
- 分析必须小型、描述性（计数、比例、χ²/t 检验），不得喧宾夺主变成结果节。
- 数据来源必须公开可查（本文：NHTSA 召回记录 + ABI/INFORM 报刊索引）。
- 必须有理论回收句把统计结果接回前提（本文末句：报道既是显著性的因也是果）。
- 前提必须是**承重的**——边缘前提不配原创分析；一篇论文至多一到两处。

**反模式**: 用轶事断言替代计数（"press coverage is extensive"）；或把完整计量模型搬进 Theory 节，模糊理论/实证的体裁边界。
