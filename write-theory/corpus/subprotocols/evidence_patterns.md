# Evidence Patterns
> 论证角色：**Evidence**——发现锚点材料（每类论据的句式骨架；论据须回扣到它支撑的具体推理步骤）；填位规则见 `_argument-grammar.md`（story-blueprints/v4/rhetoric-moves/）

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


### 变体 A：非事件访谈证据（Interview Non-Event Warrant，ball_2018 型）
**band**: quiet偏薄弱（single_source_verified；用户裁决单源可写）
**适用场景**: 双边论证中"未发生行为"的一侧无公共记录（召回未发生、违规未披露、退出未执行），无法用档案案例实例化。
**骨架**:
Identifying actual examples of [high-discretion non-events] is more challenging, as these events are not in the public domain because [they did not occur]. As such, we spoke with a [role] at a [firm type]. The manager chronicled several [non-event] scenarios that [did not occur although guidelines required action]. We describe two such examples. In one instance, [concrete violation detail]... [decision makers] jointly opted to [not act] because [mitigating detail].
**配套动作**: 访谈实例后接一条"按官方标准本应行动"的对照句（"the FDA clearly stipulates a recall in both of these situations"），把非事件钉在客观标准上，再抛出研究问题（"why would management not recall?"）作为调节机制的入口。
**原文锚点**: "As such, we spoke with a manufacturing manager at a large, publicly traded, FDA regulated firm. The manager chronicled several product problem scenarios that did not result in recalls"
**诚实边界**: 标注样本量（n=1 访谈）；访谈实例是 warrant 不是数据，不得在 Results 中当证据用。


## Pattern: Paired Opposite-Default Interview Vignettes（反向默认对偶访谈轶事）

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**适用场景**: 需要用一手证据证明 (a) 决策裁量空间真实存在 且 (b) 上游主体确实通过默认期望塑造下游决策——但无法观测全部决策过程时。两个具名职务的访谈人 + 两个相反默认，合成"离散谱系"证据。

**结构**: Informant A（决策聚焦客户伤害 + 3 天举证期 + 默认召回）→ 归因上游（"This expectation... was established by the firm's board"）→ Informant B（Conversely；举证责任反转 + cost-benefit 优先）→ 归因上游（"driven by the board"）→ 具体激励轶事（board-approved bonus tied to no-recall objective）→ 第三方监管者访谈验证离散普遍性

**骨架**:
```
The [role A] mentioned that, at [her] firm, the [decision] focuses keenly on [stake].
[Committee] are only allowed [N days] to prove that [action] is not warranted...
The default at this firm is to [act] and to do so quickly. This expectation... was
established by the firm's [upstream actor]. In fact, it is [focal attribute members]
... who are particularly concerned with [stake]... This line of questioning sets the
tone for how [decisions] are made at this firm.

Conversely, the [role B] we spoke with indicated that, at his firm, the default is
the opposite. There, [committee] have the burden of proving that [action] is absolutely
necessary... This [alternative prioritization] is driven by the [upstream actor].
[Concrete incentive anecdote]. In other words, the tone set by this [upstream actor]
is to [opposite behavior].

Finally, our interview with [third-party validator] validated that divergence... is
very common. [Institutional reasons why discretion persists].
```

**为什么有效**: 反向默认构成自然最小对照：同一制度框架下两个极端默认并存，既证明裁量真实，又把默认的成因精确归因到上游主体；第三方监管者访谈把"离散普遍"从轶事升格为结构性事实。

**注意事项**:
- 两个 vignette 的结构必须对称（举证责任、时间窗、优先级逐项相反）
- 每个默认都要显式归因上游（不能只说"firm culture"）
- 需要第三个独立信源验证离散不是特例
- 引述须可追溯（职务+行业+匿名化声明），不得虚构

**反模式**: 只用一个正面案例（无对照即无离散证明）；轶事与后续假设的机制层次脱钩。

**原文锚点**: "The default at this firm is to recall and to do so quickly. This expectation for quick and deliberate action prioritizing customer safety was established by the firm's board."


### 变体 B：理论构念→经验情境显式桥接（fit-well bridging）

<!--
pattern_id: theory_type_to_empirical_context_bridging
build_type: 跨类型（构念-操作化桥接，经验曲线/档案研究尤适）
source_papers: ["anand_mukherjee_2024_org_science"]
confidence: medium（单篇，产品召回主题 expert_audit_override 2026-08-29 升 VERIFIED）
-->

**适用场景**: 理论构念（如 failure 类型）与档案可观察物（如 recall 类别）存在映射 leaps 时，用三步桥接句显式授权操作化并预先框定外推范围。

**骨架**:
```
[Theoretical type A] and [theoretical type B] fit well into the descriptions of
[observable category A'] and [observable category B'] ([mapping citations]).
As such, we develop our hypotheses using the empirical context of [observable
phenomenon], which are the phenomena that we observe and examine.
Subsequently, based on our results, we derive implications for the larger
context of [theoretical construct].
```

**为什么有效**: "fit well into" 完成映射、"the phenomena that we observe and examine" 完成授权、"derive implications for the larger context" 完成双向 scope 声明——一句话挡掉"你的 DV 不是你的构念"的攻击。
**注意事项**: 映射需有文献或制度依据（如召回公告的归因分类）；若映射不完美应如实声明 caveat（本篇以自愿召回为主即是一例）。
**反模式**: 无映射论证直接换词（把构念名悄悄替换成测量名）。

**原文锚点**: "As such, we develop our hypotheses using the empirical context of product recalls, which are the phenomena that we observe and examine."（§2.2 末段）

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:theory_type_to_empirical_context_bridging -->


## Pattern: Rival Readings of the Same Measure（同一测量的对立读法，zajac_westphal_2004 型）

<!--
pattern_id: rival_readings_same_measure
build_type: 跨类型（竞争假设裁决面）
source_papers: ["zajac_westphal_2004_asr"]
confidence: medium
status: VERIFIED
verification_basis: "expert_audit_override (Westphal 系裁决: 用户点名最爱学者,引言/理论单源足矣)"
-->

**适用场景**: 竞争假设设计（变体 F）中，同一因变量数据被两套理论赋予不同认识论身份——对手阵营视之为 [客观效率信号]，本方视之为 [主观符号价值的社会量化]。把"测量的含义"本身作为裁决对象之一，使实证检验同时检验预测符号与测量解释。与 `../variants/B_mechanism_elaboration.md` 的 westphal_zajac_1998 硬/软数字测量重构为姊妹模式：彼处重构单方测量的硬软属性，此处并置双读法交由数据裁决。

**骨架**:
```
[对手读法] From a [rival discipline] perspective, [Y data] provide objective data that
reflect [expected efficiency gains] from [policy implementation].
[本方读法] From a [home] perspective, we view such reactions as subjective data that
reflect the [symbolic value at issue], quantified and aggregated.
[裁决声明] Through examining change in [Y] as [X] accumulates, we are able to directly
assess [which reading holds].
```

**原文锚点** (Zajac & Westphal 2004, ASR):
> "we view such reactions as subjective data that reflect the symbolic value of adoption, neatly quantified and aggregated"

**为什么有效**: 把测量争议从审稿人的暗箭变成理论贡献的明面——"数据支持谁"与"数据是什么"被合并为同一个可检验问题；为 Discussion 的理论裁决段落（解释为何一方读法成立）预先铺设语义基础。

**注意事项**:
- 两个读法都必须被 steelman（对手读法引用对手文献的解释）
- 裁决面必须有可操作判据（系数符号/变化方向），不能停留"数据可以有两种读法"的相对主义
- 若两读法在测量构造上不可区分（同一统计量、同一解释），此模式退化为装饰

**反模式**: 只声称"我们的解释更合理"而不把两种读法绑到可判别的预测上。

<!-- wb:zajac_westphal_the_social_construction_of_market_value:rival_readings_same_measure -->


## Pattern: Counterfactual Case Replay Warrant（失败案例反事实回放，Castellaneta 2017 型）

**适用场景**: 机制步骤断言"缺少某信息/能力会导致误判"时，用具名失败案例先复盘实际损失，再用反事实句把损失显式归因到缺失的机制环节，最后升华为一般命题。与 Case-as-Warrant 原子型的差异：原子型展示机制如何正向运作，本子型展示机制缺失的代价，并让反事实推理承担归因。

**骨架**:
```
[机制步骤] [Assessment task] requires [information/capability] because [reason] ([citation]).
[失败案例引入] [Company A]'s [year] [transaction] of [Target] ([context detail]) illustrates the consequences of [mechanism failure].
[损失量化] [Time later], [Company A] was forced to [unwind action] for [fraction of price], after [trigger event] ([source]).
[反事实回放] This significant loss might have been avoided had [Company A] collected better information about [missing mechanism input].
[一般化回收] This example implies that [assessment task] requires [information/capability]. Thus, even if [strongest counterfactual], [actor] would still be less able to [task] when [condition].
```

**关键特征**:
- **损失量化锚点**: 具名购入价与退出价对比使误判代价可感知、可记忆
- **"might have been avoided had..."**: 显式承认案例非证据，归因由反事实推理承担，保持诚实边界
- **双重回收**: 先案例→命题（This example implies...），再命题→最强反方情形（even if... would still...），可与 Even-If Fallback Refutation 衔接

**原文锚点** (Castellaneta, Conti & Kacperczyk 2017, SMJ):
> "Two years after the purchase, Quaker Oats was forced to resell Snapple for just $300 million, after its brewing technique had been reverse-engineered (and so copied) by several competitors... This significant loss might have been avoided had Quaker Oats collected better information about the intangible assets of Snapple's competitors."

**诚实边界**: 失败案例只能作 warrant/说明，不能作效应大小或因果方向的证据；反事实归因必须与机制步骤一一对应，不得用案例倒推机制方向。

**注意事项**: 案例须广为人知或可溯源（新闻报道/案例研究）；单一匿名或不可溯源失败不适用本子型。

<!-- wb:castellaneta_2017_smj_how_does_trade_secret_legal_protection:counterfactual_case_replay_warrant -->


### Pattern: Pre-Study Interview Premise Warrant（自有预备访谈承重理论前提，Fini 2017 型）

**适用场景**: Theory 中某机制前提（如"评价者 ex-ante 面临不确定性，故判断重人不重案"）文献支撑不足或属领域常识缺位时，用作者为本项目自采预备访谈的逐字引语承重前提，声明句显式标记证据来源与功能。与 Interview Non-Event Warrant（ball_2018：知情者访谈证明未发生行为）与 Paired Opposite-Default Interview Vignettes（wowak_2020：成对反向默认轶事展示裁量）判别：本子型引语来自**作者自己的预备访谈**、功能是**承重理论前提**而非证据化事件或展示裁量空间。

**骨架**:
```
[前提断言] [Evaluator] faces [daunting task] in [ex-ante decision context]: [uncertainty features 1-3].
[自有访谈证据引入] Evidence from the interviews that we conducted for this project supports this conjecture.
[逐字引语] Echoing others, a [role/field] stated: "[premise-supporting quote]".
[回扣机制] The [uncertainty] surrounding [promised future outputs] makes [mechanism: inference about the actor] more salient, compared to [alternative ex-post valuation setting].
```

**关键特征**:
- **来源声明句**: "the interviews that we conducted for this project" 显式声明引语来自本文自采预备访谈——premise warrant 的证据等级介于文献与数据之间，来源声明防止审稿人误读为实证结果前置
- **引语承担前提而非预测**: 引语支撑机制前提（评价者重人轻案），不预演假设方向；假设仍由文献推导收敛
- **对照设置收尾**: 与另一评价场景（如双盲 ex-post 评审）对照，凸显前提为何在该情境下更成立，为机制的情境特异性铺垫

**原文锚点** (Fini, Jourdan & Perkmann 2017, AMJ):
> "Evidence from the interviews that we conducted for this project supports this conjecture. Echoing others, a professor specializing in infection, stated: 'When I review grant proposals, I evaluate more the person than the grant [proposal] itself.'"

**诚实边界**: 预备访谈引语只能承重前提/机制合理性，不能当效应存在或方向的证据；不得用访谈引语替代假设推导中的文献 warrant；引语须来自可声明的自采样本，不得混入二手引语而不声明。

**反模式**: 把预备访谈引语放在假设收敛处替代 "Therefore" 推导；或全文多处理人访谈引语造成 Theory 叙事证据化。

<!-- wb:fini_jourdan_perkmann_2017_amj:pre_study_interview_premise_warrant -->

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:pre_study_interview_premise_warrant -->


### 变体 C：田野引语证据质感三段式（Gulati_1998 综述文型）

**模板**:
> [抽象机制主张] [关于行动者如何依赖某机制的理论主张].
> [引语框架句] As the typical comments by [某类线人] I interviewed indicate, [主张改写为行动者语言]:
> [逐字块引] '[线人原话，保留口语质感]' ([访谈出处：作者 年份：页码]).
> [uptake 吸收句] Such comments suggest that [一句话理论收束，接续论证].

**来源**: Gulati_1998_SMJ, Theory P63-P67（formation）、P87-P89（governance）、P93-P95（referral/trust）

**原文锚点**:
> "As the typical comments by a manager I interviewed indicate, firm managers embed their new ties by relying extensively on their partners from past alliances for information..." "Such comments suggest that firms are influenced in their ability to enter new partnerships by the social network of their past alliances."

**关键特征**:
- 引语是部署性证据而非装饰：只出现在理论主张需要过程性 ground-truth 的位置（机制如何在实际决策者口中运作）
- 框架句预告引语要证明什么，uptake 句把行动者语言翻译回理论语言——三段式闭环防止引语"漂"
- 每条引语带访谈出处（作者 年份：页码），质性材料获得与文献引用同等的可追溯性
- 框架句标注线人类型（manager / executive specializing in alliances），暗示引语代表性而非孤例
**适用**: 理论综述文/概念文需要证据质感时；纯理论论证中的关键机制步
**禁忌**: 每个机制主张至多 1 条引语，密集堆放会滑向民族志（与体裁不符）；引语必须与出处可核对；uptake 句不得引出新机制（只回收已主张的机制）

<!-- wb:gulati_1998_alliances_and_networks:field_quote_evidence_texture -->


### 变体 D：田野引语三段式的假设推导内部署（Gulati_1999 实证理论节型）

<!--
pattern_id: field_quote_evidence_texture_empirical_derivation_deployment
build_type: 跨类型（证据部署变体；构念辨析/机制推演型理论节）
source_papers: ["gulati_1999_network_location_and_learning_the_influence_of_n"]
verification_status: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED)
story_fidelity: section_variant
-->

**适用场景**: 大样本实证论文的 Theory 节把作者自采访谈的逐字引语部署为**机制分支的 warrant**——与 Gulati_1998 综述文的"证据质感"三段式同构，但部署位置与密度不同：每个机制分支（如信息收益的三分法）各配 1-2 条引语，引语紧贴假设收敛处，使"机制在实践者口中真实运作"先于假设被看见。前提：引言或方法已声明访谈设计（本文：153 访谈/11 企业/2 年，"I draw on selective quotes from some of the managers I interviewed wherever relevant"），Theory 的引语使用即兑现该承诺。

**骨架**（每个机制分支一次）:
```
[机制分支命名] [Benefit name] refers to / entails [分支定义] ([canonical citation]).
[机制主张] [分支层面的理论主张：来源如何产生该收益].
[引语框架句] This is vividly illustrated by / Another [role] I interviewed [said/highlighted]:  — 预告引语要证明什么并标注线人类型
[逐字引语] '[practitioner verbatim quote]'
[uptake 回收句] Thus, it seems that / Such comments suggest that [把行动者语言翻译回理论语言] — 只回收已主张的机制，不引出新机制
```

**与综述文型（Gulati_1998）的部署差异**:
- 综述文：引语为概念论证提供质感，位置自由；实证理论节：引语锚定在**机制分支内部、假设收敛之前**，承担"机制可行性 warrant"
- 每条机制分支至多 1-2 条引语，全部服务于同一个小节假设；引语内容与分支定义一一对应（如 access→信息可得性、timing→及时性、referrals→第三方背书）
- 大样本设计下访谈引语只作机制说明不作效应证据——假设的证据责任由后续大样本检验承担

**为什么有效**: 框架句+引语+回收句的三拍闭环让每条引语"不漂"；实践者原声把抽象收益分类变成可感知场景，框架句标注线人类型暗示代表性而非孤例，访谈出处维持与文献引用同级的可追溯性。

**注意事项**: 引语来源与采样须在引言/方法交代；uptake 句不得引入分支定义之外的新机制；保留口语质感但不得把引语复制进模板。

**反模式**: 每段都塞引语（滑向民族志）；引语放在假设句之后（证据应先于预测）；引语与机制分支无对应关系。

**原文锚点** (Gulati 1999, SMJ):
> "This is vividly illustrated by the comments of an alliance manager I interviewed: 'Our network of [prior alliance] partners is an active source of information for us about new deals [alliances].'"

**原文锚点**（uptake 回收句）:
> "Thus, it seems that firm managers actively seek information about new alliances from their prior alliance partners, both with the previous partner and with other firms."

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:field_quote_evidence_texture_empirical_derivation_deployment -->
