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
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Case as Warrant for Mechanism Step

**适用场景**: 当机制步骤比较抽象，需要让读者在经验世界中"看见"它时。用企业/行业案例作为 Warrant。
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

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
