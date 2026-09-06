# Construct Differentiation Patterns

本文件收集 Theory 中 T1 构念辨析段落的可复用模式。当研究需要界定一个新构念、或重新定义一个易混淆构念时使用。

---

<!-- 
pattern_id: table_construct_differentiation
build_type: 构念辨析型 / 现象驱动型
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Table-Based Construct Differentiation

**适用场景**: 新构念与多个相关构念在多个维度上存在差异，需要建立清晰边界。
**微观动作序列**: Naming（构念命名）→ Differentiation dimensions table（多维度对比表）→ Scope condition → Theoretical consequence
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety vs product recall / scandal / brand spillover / customer complaints / algorithmic error）

**骨架**:
```
Among varied perspectives on [domain], [construct] represents a distinct form of [phenomenon] that has not received a lot of attention in extant research. In [Table X] (and an expanded literature review in [appendix]), we provide explicit comparisons of [construct] with other types of [related concepts] (e.g., [concept A], [concept B], [concept C]). In our proposed conceptual framework, [construct] represents a distinct phenomenon that requires specific consideration and that exerts unique effects on [outcome], relative to other types of [related concepts].
```

**为什么有效**: 表格将多个差异化维度同时呈现，降低读者认知负担；为后续机制推演建立清晰的研究对象边界。

**注意事项**:
- 表格维度需与后续理论论证直接相关（如 Advertising Focused? / Crisis Source / Brand Control / Digital）
- 避免维度过多导致读者疲劳；3-6 个维度为宜
- 表格后需用 1-2 句话总结最关键的差异维度及其理论后果

**反模式**: 若新构念与相关构念差异单一，不要用表格，用 1-2 句对比即可；若表格维度与后续 Theory 无关，会显得装饰性。

---

<!--
pattern_id: invariant_discriminant_spine
build_type: 构念辨析型
source_papers: ["Ridge_Hill_Ingram_Kolomeitsev_Worrell_2024_AMJ"]
confidence: emerging
status: needs_cross_paper_validation
story_fidelity: section_variant
-->

## Pattern: Invariant Discriminant Spine

**适用场景**: 新构念与相关构念在**多个维度**上看似相近，但存在**一条贯穿所有维度、恒定不变的判别主轴**（invariant discriminant spine），把新构念从相关构念中一次性区隔出来。与 Table-Based 的区别：Table-Based 是"多维并列对比"（每行一个维度、整体建立边界）；本模式是"**先声明一条不变主轴，再沿该主轴解释每个相邻构念为何被排除**"——主轴的逻辑承担全部区分工作，相邻构念是对主轴的逐个检验。

**微观动作序列**: Spine claim（声明不变判别主轴）→ Adjacent construct elimination（沿主轴排除相邻构念 A/B）→ Definition consequence（主轴蕴含的理论后果）
**范文来源**: Ridge, Hill, Ingram, Kolomeitsev & Worrell (2024), *Academy of Management Journal*（paranoia vs distrust：主轴 = "不仅是怀疑，还有对恶意的主观感知"）

**骨架**:
```
[Spine claim]
[Construct] is not only [adjacent construct] but also [invariant discriminant spine]. The distinguishing feature is [spine content]: [active perception / specific state] rather than [mere absence / passive belief].

[Adjacent construct elimination — 逐个沿主轴检验]
This distinction matters for how [construct] shapes [outcome]. [Adjacent construct A] reflects [A's content]—a [passive/specific] state that [does not carry the spine]. [Adjacent construct B], by contrast, [B's content], which [also lacks the spine / differs on the spine dimension]. Only [construct] combines [spine element 1] with [spine element 2].

[Definition consequence]
Because [construct] carries [spine], it [predicts behavior/phenomenon] in ways [adjacent constructs] do not: [consequence tied to the spine].
```

**为什么有效**: 读者只需要记住一条主轴，相邻构念的排除成为对主轴的重复检验——比"每行一个维度"更省认知、更不易被审稿人反驳；主轴直接为后续机制提供因果入口（如"主动恶意感知"→ 威胁扫描 → 回避行为）。

**注意事项**:
- 主轴必须是**不变的**（贯穿所有相邻构念的判别都回到它），不能每个相邻构念换一条判别线。
- 主轴要落在**理论后果可衔接**的位置——它必须能解释后续机制的方向（如"主动感知"支撑 hyper-vigilance），否则只是词源辨析。
- 相邻构念排除要具体（每个构念"缺什么"），不能只写"X is different"。

**反模式**: 主轴不恒定（A 用维度 1、B 用维度 2 排除）→ 退化为列表；主轴与机制无关（区分完即弃用）；相邻构念排除流于形式（无内容差异）。

---

<!--
pattern_id: simultaneously_recognize_leverage
build_type: 跨类型
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Simultaneously Recognize X but Leverage Y

**适用场景**: 研究对象与现有文献中的相关现象有相似性但机制不同，需要借用相关文献同时避免混淆。
**微观动作序列**: Recognition of difference → Leveraging similarity → Concrete illustration → Prediction transfer
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety vs contagion/spillover/proximity effects）

**骨架**:
```
We simultaneously (1) recognize that the mechanisms by which [related phenomenon] [affect actors] in [context] differ from the mechanism we propose for [construct], but we also (2) leverage insights from prior research in [domain A], [domain B], and [domain C] to derive some initial, potential explanations of why [construct] is likely to evoke [effect]. For example, [concrete illustration from domain A]. We apply this notion to [target context] to predict that [specific prediction].
```

**为什么有效**: 主动承认边界避免审稿人质疑 "这不是 A 研究吗？"，同时清晰说明借用理由；比简单 "Drawing on..." 更能处理文献流交织。

**注意事项**:
- 必须真正解释机制差异，不能流于形式；差异陈述要具体
- "leverage" 的文献必须与研究对象有足够相似性，否则显得牵强
- 建议在差异陈述后立即给出具体预测，避免停留在文献综述

**反模式**: 若相关文献与研究对象机制完全不同，不要强行 leverage；若只承认差异而不说明借用价值，会削弱理论贡献。

---

<!--
pattern_id: dichotomize_strategy_menu_by_fundamental_cut
build_type: 机制推演型（辅：策略菜单二分，非构念辨析贡献）
source_papers: ["Liu_Liu_Luo_2016_JM"]
confidence: medium
status: EMERGING
-->

## Pattern: Dichotomize Strategy Menu by Fundamental Cut

**适用场景**: 实证对象是连续/多类策略菜单，理论贡献不在新构念辨析，而在沿一条理论主轴把菜单切成二分 DV，并声明组内差异只是程度。
**范文来源**: Liu, Liu & Luo (2016), *Journal of Marketing*

**骨架**:
```
The distinction between [complete option] and [partial option] is fundamental and conceptually important, whereas the differences among the various [partial options] are more of varying degree. We therefore treat [choice] as a binary outcome: [complete] versus [partial].
```

**为什么有效**: 把测量选择写成理论切割而非数据便利；审稿人看到的是"这条切分承载假设"，而不是"我们把多类压成 0/1"。

**注意事项**: 切分轴必须是理论主轴（补偿完整性/成本），不能是样本量最大的两类。组内程度差异须诚实声明，并预告有序模型可能变弱。

**反模式**: 把策略菜单二分写成新构念辨析贡献；切分后仍用"各种补救"的连续语义解释系数。

**原文锚点**: "The distinction between full and partial remedy is fundamental and conceptually important, whereas the differences among the various partial remedies are more of varying degree."

---


### 变体 A：认识论不对称双类型构念辨析（cause-ambiguity typology）

<!--
pattern_id: failure_typology_cause_ambiguity_contrast
build_type: 假设树型内嵌 T1 构念辨析
source_papers: ["anand_mukherjee_2024_org_science"]
confidence: medium（单篇，产品召回主题 expert_audit_override 2026-08-29 升 VERIFIED）
-->

**适用场景**: 需要为后续分叉假设奠定构念基础的二分类；区分维度不是现象特征而是**认识论属性**（归因模糊度/可观察性），使类型差异直接预载差异化学习机制。
**模块**: T1 Construct Definition（服务于假设树的辨析，非独立贡献型辨析）。

**骨架**:
```
We characterize [phenomenon] as two types:
(1) those related to [execution of prescribed established rules] that we label
    [label A], and
(2) those related to [missing functionalities / incomplete knowledge] that we
    call [label B] ([typology citations]).
Whereas [A] are caused by [inappropriate application of established rules],
[B] are caused by [nonexistence of complete rules] owing to [incomplete models
or novel contexts] ([citation]).
There is less [epistemic ambiguity] about the causes of [A] than about [B].
```

**为什么有效**: 收尾的模糊度对比句是"分工装置"——类型 A 走低模糊机制（规则更新/培训），类型 B 走高模糊机制（内外搜索/知识重组），后文每个分叉假设只需援引所属类型的位置。
**注意事项**: 标签（label A/B）需在后文反复以专名回用（如"slip-up failures"），否则辨析与假设脱钩；模糊度主张需有文献锚点。
**反模式**: 区分维度与后续机制无关的纯分类学辨析（辨析做了分类却没做推导工作）。

**原文锚点**: "We characterize product failures as two types: (1) those related to the execution of prescribed established processes that we label slip-up failures, and (2) those related to missing functionalities or malfunctions that we call knowledge gap failures"（§2.1）

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:failure_typology_cause_ambiguity_contrast -->



### 变体 B：伞构念三层分层·双机制二分（Gulati_1998 综述文型）

**模板**:
> [伞构念定义·引源] A [网络] can be defined as '...' ([奠基引文]). [透镜构念] refers to the fact that [交换有历史→惯例化与稳定化].
> [双动作引文钉死] [结构影响行动的引文]：by [约束可用行动集] and by [改变行动者倾向] ([引文]).
> [底层驱动] Underlying [透镜构念] is the quest for [信息] to reduce [不确定性].
> [收益分类法] There are two broad analytical approaches... The first emphasizes the [信息收益]..., while the second highlights the [控制收益]... These two benefits are analytically distinct but also overlap.
> [机制二分] [透镜构念] may provide [信息收益] through two mechanisms. [子构念A] or [凝聚] perspectives stress [直接纽带传递细粒度信息]. [子构念B] or [位置] perspectives go beyond the immediate ties and emphasize [结构位置的信息价值]... [参照系转换：from the dyad and triad to the system].

**来源**: Gulati_1998_SMJ, Theory P13-P29（"Social Structure and the Embeddedness of Firm Behavior"）

**原文锚点**:
> "The first emphasizes the differential informational advantages bestowed by social networks, while the second highlights the control benefits..." ... "Relational embeddedness or cohesion perspectives on networks stress the role of direct cohesive ties as a mechanism for gaining fine-grained information."

**关键特征**:
- 三层递降：伞构念（奠基引文+双动作引文）→ 收益分类法（information vs control，明示 distinct but overlap 防割裂）→ 机制二分
- 每个子构念继承一条独立文献谱系（凝聚→Coleman/Granovetter；位置→Burt/Podolny），分层即分工
- 双动作引文（约束行动集 + 改变倾向）把构念的因果把手一次钉死，后续议题可直接调用任一动作
- "or" 同位语（relational embeddedness or cohesion perspectives）把新构念锚到读者已知的旧术语，降低新词成本
**适用**: 引入抽象新视角时的构念操作化段；一个大构念需要拆成可分别调用的子机制时
**禁忌**: 二分必须收益/机制都不同（不是同一机制换标签）；overlap 声明不可省略，否则读者追问"为何不合并"；子构念数≤2-3，再多应改用表格

<!-- wb:gulati_1998_alliances_and_networks:umbrella_construct_layering_two_mechanism_split -->


### 变体 C：母构念锚定型新构念散文合法化（Gulati_1999 型）

<!--
pattern_id: parent_anchored_new_construct_legitimation
build_type: 构念辨析型（单新构念 vs 多邻接构念的不对称辨析）
source_papers: ["gulati_1999_network_location_and_learning_the_influence_of_n"]
verification_status: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED)
story_fidelity: section_variant
-->

**适用场景**: 论文引入一个真正的新构念，且新构念是某个受尊敬"母构念"（资源/能力/资本）的一个子类——需要在纯散文中（无表格、无双主角）一次完成：位置重归因定义 → 母构念锚定 → 邻接构念逐个排除 → 跨层次类比映射 → 后果焦点改指。与 Pollock 2015 型双构念对称辨析的区别：这里只有**一个** focal 新构念，其余构念是"邻接排除对象"而非并列主角；与 lee_wang 变体 L 的区别：不用表格，母构念锚定替代竞争性景观测绘。

**骨架**:
```
[位置重归因定义] [NEW CONSTRUCT] inhere[s] not so much within [the conventional locus] but in [the new locus] where [actors] are located.
[母构念锚定] They are a specific form of [PARENT CONSTRUCT] that can be considered to be '[canonical definition quote]' ([奠基引文]).
[缺口句] While scholars developing [parent literature] have highlighted [adjacent factors], no attention has been given to [NEW CONSTRUCT] that emerge from [participation in the new locus] ([citation]).
[邻接排除] [NEW CONSTRUCT] are distinct from '[adjacent construct from a neighboring literature]' highlighted by [Author] ([citation]) as [adjacent definition]. Instead, [NEW CONSTRUCT] result from [own generative mechanism].
[类比映射] [NEW CONSTRUCT] is akin to [analogous construct at another level of analysis] ([citation]). [经典定义引用或块引].
[后果焦点改指] In this context, I/we consider the implications of [NEW CONSTRUCT] not so much for [the parent literature's default outcome] but, rather, as [the focal function for this paper's outcome].
```

**为什么有效**: 五步全在散文内完成：母构念锚定让新构念直接继承母文献的合法性（不必从零证明这类构念值得研究）；位置重归因一句话给出区分主轴（构念"住在哪"）；邻接排除把审稿人最可能混淆的 1-2 个外来构念逐个划出边界；类比映射借跨层次对应构念的经典定义加固；末句把后果焦点从母文献的默认 DV（绩效）改指向本文 DV（行为）——读者读完 T1 即知道新构念是什么、住在哪、不是谁、为何值得另一个 DV。

**注意事项**:
- 母构念定义必须引用可查证的奠基定义（本文引 Barney 1991 资源定义原文），自创判据会削弱锚定
- 位置重归因是区分主轴，必须与后续机制直接衔接（信息优势来自网络位置），否则只是词源辨析
- 邻接排除选 1-2 个"最可能被混淆"的构念即可，不穷尽；跨层次类比要显式声明层次差异（个体→企业）
- 后果焦点改指句是构念与本文假设的接口，不可省略

**反模式**: 把邻接构念写成并列主角（变成双构念对称辨析）；只作语义区分不declare后果焦点（辨析与假设脱钩）；无母构念锚定的裸定义（合法性缺口）。

**原文锚点** (Gulati 1999, SMJ):
> "Network resources inhere not so much within the firm but in the interfirm networks in which firms are located. They are a specific form of firm resources that can be considered to be 'strengths that firms can use to conceive of and implement their strategies'."

**原文锚点**（邻接排除句）:
> "Network resources are distinct from 'external capabilities' highlighted by Langlois (1992) as capabilities produced by and residing in a specialized market network."

**原文锚点**（后果焦点改指句）:
> "In this context, I consider the implications of network resources not so much for the performance of firms but, rather, as an important enabling condition for future cooperation."

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:parent_anchored_new_construct_legitimation -->


### 变体 D：母构念三机制分列·机制-假设一一耦合（Hypothesis-Coupled Mechanism Triad，Gulati_1999_AJS 型）

<!--
pattern_id: hypothesis_coupled_mechanism_triad
build_type: 机制推演型（多机制收敛网）
source_papers: ["gulati_1999_where_do_interorganizational_networks (AJS)"]
verification_status: VERIFIED — expert_audit_override (Gulati 系单源裁定 2026-09-06, paper_count=1)
story_fidelity: section_variant
-->

**适用场景**: 实证论文把一个抽象母构念（嵌入性/社会资本类视角构念）拆成 3 个平行机制，且每个机制需要各自推导一条假设——与变体 B（综述文定义操作化）的任务不同：这里类型学是假设生成装置，不是概念澄清。

**骨架**:
```
[母构念机制化·类型学命名句] The [信息/收益] that flows through [母构念载体] originates from [来源A], from [来源B], or from [来源C]. Each of these sources is related to specific [机制族] that shape [DV]. We refer to these mechanisms as [M1], [M2], and [M3] respectively.
[机制 i 循环 ×3]
  [Mi 命名+参照系声明] [Mi] highlights the effects of [特征i] on [DV]. The frame of reference shifts from [层级i-1] to [层级i], while the focus shifts from [渠道i-1] to [渠道i].
  [文献谱系] [Mi] 的独立谱系支撑（奠基文献+延伸文献）。
  [微观机制 1-2 步] [Mi] provides [信息/信任] through [通道], lowering [不确定性] about [DV 的前置条件]。
  [现象级证据]（可选）[field quote 一句回收]。
  [收敛] Consequently: H[n]: The probability of a new [DV 事件] between [actor A] and [actor B] increases with [Mi 的度量].
```

**为什么有效**: 类型学命名句一次性把抽象母构念切成读者可分别调用的机制清单（respectively 回指信息来源，机制与来源一一对应）；每个机制段以自己的文献谱系+假设收尾，机制与假设一一耦合，读者读完三段即持有完整假设组地图；参照系声明（dyad→triad→network-wide）防止三机制被读成同一机制换标签。

**注意事项**: 各机制判据必须互斥且观测层级递升（直接纽带→共同第三方→整体位置）；每机制继承一条独立文献谱系；机制间若有重叠需显式声明 overlap（呼应变体 B 的 distinct but overlap 纪律）；统一假设模板（见 dyadic 概率主效应句）让句式差异不干扰机制差异。

**反模式**: 三机制只有标签差异无判据差异；机制与假设交叉（Mi 推出两条假设或两条假设共享同一判据）；类型学句写成名词罗列（无 respectively 回指）。

**与近亲变体的区分**: 变体 B（伞构念三层分层·双机制二分）是综述文的定义操作化——收益分类→机制二分、无假设产出；本变体是实证论文的假设生成装置——信息来源类型学→机制三分解→每机制一条假设。变体 C（母构念锚定型）合法化单一新构念，不分解机制。

**原文锚点** (Gulati 1999, AJS):
> "Each of these sources of information is related to specific network mechanisms that shape the creation of new embedded interorganizational ties. We refer to these mechanisms as relational, structural, and positional embeddedness respectively."

<!-- wb:gulati_1999_where_do_interorganizational_networks:c1_hypothesis_coupled_mechanism_triad -->

### Micro-Move: Umbrella-Term Subsumption Criterion（上位类收编判据声明，Fini 2017 型）

**模块**: T1 Construct Definition（服务于机制前提的术语建制，非独立贡献型辨析）。

**适用场景**: 引入自建上位类目（如 indices）时，先摆既有子型分野（reputation vs status signals），再用经典定义判据（Spence 1973: costly to produce and manipulable）声明上位类与既有术语的部分交叠（"not all indices are signals"），最后把本文焦点收缩到上位类的具体子集并赋予新名（endogenous/exogenous indices）。与 Adjacent-Construct Elimination 判别：彼处沿主轴**排除**相邻构念以划清新构念边界，此处**收编**既有术语为子集、保留判据张力并把贡献落在上位类的未被覆盖子集上。

**微观动作序列**: Umbrella introduction（上位类引入+功能定位）→ Existing subtype split（既有子型按来源分野）→ Criterion declaration（经典定义判据下的部分收编声明）→ Focal narrowing + naming（焦点子集收缩并命名）。

**骨架**:
```
[上位类引入] The [candidate]'s [background] delivers a set of critical "[umbrella term]"—[definition: unalterable features determined in the past]—that [evaluators] can use to [complete the assessment].
[既有子型分野] Past works have referred to the latter as [subtype 1] signals ([citation]); these are based on [personal merit], whereas [subtype 2] signals originate in [affiliations with established social hierarchies] ([citation]).
[判据声明] While [umbrella term] might not all be [canonical term] as per [author, year]'s definition ([criterion: costly to produce and manipulable]), they are key in that [availability to evaluators].
[焦点收缩命名] [Specific type of umbrella term]—termed herein [paper's own term]—are the focus of this paper.
```

**原文锚点** (Fini, Jourdan & Perkmann 2017, AMJ):
> "While indices might not all be signals as per Spence's (1973) definition (i.e., costly to produce and manipulable by the candidate), they are key to the evaluation process in that they are available to peer evaluators."

**为什么有效**: 自建上位类若不与既有术语对账，审稿人会问"这和 signal/status 有何不同"；判据声明承认部分交叠同时保住新类目的增量（可得性而非可操纵性），随后的命名（endogenous/exogenous）让机制段可直接复用术语而不重复辨析。

**注意事项**:
- 判据必须来自可引用的经典定义，不能自创判据
- 命名子集（termed herein）应承载后续假设的核心区分，否则辨析悬空
- 与收编对象的关系是"子集/交叠"而非"替换"——不得声称既有术语错误

**反模式**: 用本微动作做全文主贡献辨析（两个构念系统对立时路由到构念辨析型 A 变体）。

<!-- wb:fini_jourdan_perkmann_2017_amj:umbrella_term_subsumption_criterion -->

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:umbrella_term_subsumption_criterion -->
<!--
pattern_id: a_umbrella_decomposition_platform_for_categorical_ordering
build_type: 构念辨析型（工具性伞构念解构——辨析为比较服务）
source_papers: ["gulati2005-adaptation-vertical"]
confidence: EMERGING（单篇，待第二篇交叉验证）
-->

### 变体 E：伞构念按问题根因解构，作为跨类别模式排序的解析平台（Umbrella Decomposition for Categorical Ordering）

**适用场景**: 一个伞构念（integration / alignment / 协调合作类）同时涵盖两种不同根因的问题（动机 vs 认知），而比较对象（类别化模式）在这两类问题的解决机制上系统性不同——先拆解伞构念、再逐模式清点机制可得性，即可支撑跨类别（含中间/混合模式）排序，无需发明新构念。

**骨架**:
```
[伞声明] [Umbrella] not only requires the alignment of [component 1: interests]
([label A]), but also the alignment of [component 2: actions] ([label B]).
[辨析缺口] The distinction between [label A] and [label B] is seldom maintained in
[field] research.
[根因1+解药] Problems of [label A] arise from [root cause 1 — motivation / self-interest].
They are resolved by [formal mechanisms: contracts/ownership/monitoring/sanctions/
future interactions] and [informal mechanisms: identification/embeddedness].
[根因2+解药] In contrast, problems of [label B] arise from [root cause 2 — cognitive
limits: unknown decision rules of others / unknowable interdependence]; they can persist
even when [root cause 1] is resolved, because [incentives do not create knowledge].
[示范证据] [Weakest-link / learning games or equivalents show coordination failure
absent conflict.]
[工具化说明] Therefore, the achievement of [umbrella] requires the resolution of both
[label A] and [label B] problems.
[平台声明] [Umbrella] between [unit pair] varies systematically across [categorical
alternatives], as these alternatives differ in the mechanisms available to generate
[label A] and [label B].
```

**为什么有效**: 辨析不是终点而是平台——按"问题根因"切开伞构念后，跨类别比较立刻获得可操作标准（各模式拥有哪类解药），排序假设的每一步都能指认机制，避免"模式 A 比 B 更 [umbrella]"的无机制断言；"seldom maintained"句交代为何值得费力拆解（回应审稿人"这不是常识吗"）。

**注意事项**: 两个子构念的根因必须概念独立（动机 vs 认知/知识），否则审稿人会问 why not a single dimension；拆解后必须回伞构念层面收拢（如 integration 需同时解决两类问题），防止读者丢失主线；解构若对应测量，需给 Methods 接口（单一 scale 同时覆盖两成分亦可，如本范文）。

**反模式**: 解构只做学术史综述而不用于比较对象排序；两个子构念边界重叠（同义反复）；拆解后无收拢句。

**原文锚点**: "Integration not only requires the alignment of interests (cooperation), but also the alignment of actions (coordination). The distinction between cooperation and coordination is seldom maintained in organizational research."（Integration in vertical relationships 段）

**范文来源**: Gulati, Lawrence & Puranam (2005), *Strategic Management Journal* — Integration 节（cooperation vs coordination 解构 + 三模式机制清点 → H2）。

<!-- wb:gulati2005-adaptation-vertical:a_umbrella_decomposition_platform_for_categorical_ordering -->

## 与相邻语料文件的关系

- [`../sentences/construct_definition.md`](../sentences/construct_definition.md)：微观句式模板（如 "We define X as..."）
- [`../subprotocols/argumentation_patterns.md`](argumentation_patterns.md)：微观动作组合
- [`../variants/A_construct_differentiation.md`](../variants/A_construct_differentiation.md)：构念辨析型整篇结构

> **使用顺序**：先查本文件确定 T1 辨析策略 → 再查 `construct_definition.md` 填充具体句式 → 再查 `argumentation_patterns.md` 组织论证动作。
