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

## 与相邻语料文件的关系

- [`../sentences/construct_definition.md`](../sentences/construct_definition.md)：微观句式模板（如 "We define X as..."）
- [`../subprotocols/argumentation_patterns.md`](argumentation_patterns.md)：微观动作组合
- [`../variants/A_construct_differentiation.md`](../variants/A_construct_differentiation.md)：构念辨析型整篇结构

> **使用顺序**：先查本文件确定 T1 辨析策略 → 再查 `construct_definition.md` 填充具体句式 → 再查 `argumentation_patterns.md` 组织论证动作。
