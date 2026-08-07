# Moderator Selection Frameworks

本文件收集当论文有 ≥2 个 moderators 时，解释为什么选择这些 moderator 的元框架。

---

<!-- 
pattern_id: environmental_organizational_resource_availability
build_type: 调节效应型 / 假设树型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Framework: Environmental vs. Organizational Resource Availability

**适用场景**: 当主效应涉及资源获取/资源利用的权衡，需要用多个 moderators 检验资源可得性如何改变主效应时使用。
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**框架结构**:
```
We identify shift parameters that alter the impact of [IV] on [DV] by examining 
resource availability at two levels: the environment and the firm.

At the environmental level:
- Supply side: [moderator 1, e.g., factor market development]
- Demand side: [moderator 2, e.g., industrial competition]

At the organizational level:
- Internal resource: [moderator 3, e.g., foreign shareholding]
- External resource: [moderator 4, e.g., customer concentration]
```

**为什么有效**: 
- 把四个 moderators 组织进一个 2×2 框架，避免"逐个引入"
- 每个 moderator 都有明确的位置和理论角色

**适用条件**: 
- 主效应与资源获取/利用相关
- moderators 确实可以按 environmental/organizational 或 internal/external 分类

**注意事项**: 
- 框架必须在引入第一个 moderator 之前就明确说明
- 每个 moderator 段落开头应回扣其在框架中的位置

**反模式**: 如果 moderators 之间没有 conceptual 联系，不要硬套 2×2 框架。

---

<!-- 
pattern_id: information_attention_framework
build_type: 机制推演型 / 假设树型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Framework: Information vs. Attention

**适用场景**: 当主效应涉及危机/风险情境，需要用多个 moderators 区分"信息内容"和"信息注意力"时使用。
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**框架结构**:
```
We explore variables that likely determine [actor] reactions, which in turn can inform [DV] decisions.
We categorize these variables as related to (1) the information that determines the [event] 
and (2) the attention the information receives.

Information-related moderator: [W1, e.g., defect severity]
Attention-related moderator: [W2, e.g., media coverage]
```

**为什么有效**: 把两个 moderators 放入一个清晰的分类框架，避免它们显得 arbitrary。

**适用条件**: 
- 主效应涉及信息处理或危机响应
- 一个 moderator 改变信息内容，另一个改变信息可见度/注意力

**注意事项**: 
- 框架应在 moderator 段落之前明确提出
- 建议进一步说明为什么 information 和 attention 是两个独立且互补的维度

**反模式**: 如果 moderators 不能 clean 地归入 information/attention，不要用此框架。

---

<!--
pattern_id: information_asymmetry_meta_framework_two_moderators
build_type: 假设树型 / 调节效应型
source_papers: ["Darby_2026_JOM"]
confidence: high
status: ready_for_corpus
-->

## Framework: Information Asymmetry Meta-Framework for Multi-Level Moderators

**适用场景**: 当研究包含两个及以上 moderator，分别位于不同分析层次或不同路径，需要统一理论框架解释为什么选择这些 moderator。
**范文来源**: Darby, Wowak, Ketchen & Connelly (2026), *Journal of Operations Management*（R&D intensity at firm-level + device class at product-level，均通过 information asymmetry 削弱 large institutional investors 的 monitoring effect）

**框架结构**:
```
[Core concept] is central to [theory] because it underlies the [problem] that arise in [relationship] ([citation]). As [core concept] increases, [intermediate mechanism] increases, which [consequence].

We examine this possibility using [N] moderating variables: [moderator 1] and [moderator 2]. Both reflect [core concept], but they operate through different pathways and at different levels ([citation]).

[Moderator 1] is a [level 1] characteristic capturing [attribute]. Information asymmetry arises from [pathway 1].
[Moderator 2] is a [level 2] characteristic capturing [attribute]. Information asymmetry arises from [pathway 2].
```

**为什么有效**:
- 统一框架使多个 moderator 不是“事后添加”，而是理论推导的自然延伸
- 明确不同层次/路径的差异，避免 moderator 显得 arbitrary

**适用条件**:
- 主效应涉及 principal-agent monitoring 或信息处理
- 多个 moderator 确实通过同一核心概念影响机制

**注意事项**:
- 框架必须在引入第一个 moderator 之前就明确说明
- 每个 moderator 段落开头应回扣其在框架中的位置
- 必须解释为什么 [core concept] 在不同层次/路径上产生相似效果

**反模式**: 如果 moderators 之间没有 conceptual 联系，强行用元框架包装。

---

<!--
pattern_id: three_level_moderator_framework
build_type: 机制推演型 + 调节边界
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
-->

## Framework: Incident-Brand-Consumer Three-Level Moderator Framework

**适用场景**: 当论文有 5+ 个 moderators 时，用 incident/brand/consumer 三层元框架组织 moderator，提升理论清晰度，避免 moderator 堆砌感。
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety: incident type / brand fit / consumer beliefs / brand classifications / consumer attributions & connections）

**框架结构**:
```
[Core mechanism]. This [effect], however, might be moderated by various factors, related to [level 1: e.g., the incident], [level 2: e.g., brand classifications], and [level 3: e.g., consumer-level perceptions and individual differences]. To understand these complex influences, we consider several theoretically and managerially supported moderators and boundary conditions that likely interact with [IV] to influence [mediator/DV].

[Level 1: Incident-related]
- [moderator 1: e.g., incident type/severity]
- [moderator 2: e.g., content-brand fit]

[Level 2: Brand-related]
- [moderator 3: e.g., product vs service]
- [moderator 4: e.g., utilitarian vs hedonic]

[Level 3: Consumer-related]
- [moderator 5: e.g., personal relevance/beliefs]
- [moderator 6: e.g., brand liking/commitment/connection]
```

**为什么有效**:
- 将多个 moderator 归入少数几个理论层级，避免碎片化
- 每个层级有明确的分析主体（incident / brand / consumer），便于读者理解
- 层级划分既有理论依据又兼顾管理实践

**适用条件**:
- 主效应涉及多方互动（如事件-品牌-消费者三角）
- moderators 可以 clean 地按 incident/brand/consumer 分类

**注意事项**:
- 框架必须在引入第一个 moderator 之前就明确说明
- 每个层级内的 moderator 需概念相关
- 每个 moderator 段落开头应回扣其在框架中的位置
- 层级名称可根据具体研究调整（如 firm/environment/individual 或 message/source/audience）

**反模式**: 若 moderator 之间没有清晰的层级归属，不要强行套用；可改用理论逻辑逐个引入。

---

<!--
pattern_id: ability_motivation_enablers_framework
build_type: 调节效应型 / 机制推演型
source_papers: ["Kalaignanam_Kushwaha_Eilert_2013_JM"]
confidence: medium
status: needs_validation
-->

## Framework: Ability vs. Motivation Enablers（双调节锚定）

**适用场景**: 当主效应是"从事件/经验中学习"（organizational learning, failure-induced change），且文献公认学习结果取决于**能力**（ability）与**动机**（motivation）两大正交决定因素时，用此二分框架锚定两个 moderator——一个映射能力侧（transfer enabler），一个映射动机侧（attention enabler）。

**范文来源**: Kalaignanam, Kushwaha, and Eilert (2013), *Journal of Marketing*（shared product assets = transfer enabler / ability 侧；prior brand quality = attention enabler / motivation 侧，调节 recall magnitude → future reliability）

**框架结构**:
```
It is well recognized in the [field] literature that the extent to which [actors]
[learn/change] depends on their ability and motivation to do so ([citations]).

Consistent with this stream of research, we identify "[transfer enabler]" and
"[attention enabler]" as contingency factors for [outcome]. We posit that
[structural asset Z1] enables the transfer of [learning] to [scope]
(i.e., transfer enabler). Accordingly, the conceptual model depicts [Z1] as a
moderator of the relationship between [IV] and [mediator].

Similarly, we posit that the extent to which [actors] attend to the [event]
depends on [perceptual asset Z2]. This, in turn, would alter the motivation of
[actors] to [learn] (i.e., attention enabler). Accordingly, we propose that
[Z2] moderates the relationship between [IV] and [mediator].
```

**为什么有效**:
- moderator 选择的合法性来自**文献 meta-consensus**（"ability and motivation 是学习研究的两大公认决定因素"），而非单一理论内部或事后添加——审稿人无法质疑"为什么选这两个 moderator"
- 能力/动机是**正交维度**（能否 vs 愿否），两个 moderator 各自有独立的机制内容，不存在概念重叠
- "transfer enabler" / "attention enabler" 为两个 moderator 各起一个**功能性标签**，把统计交互项转化为有名字的理论角色

**与其他框架的区别**:

| | ability–motivation 锚定（本框架） | information asymmetry 双层（darby2026） | information vs attention（Singh & Grewal 2023） |
|---|---|---|---|
| moderator 统一逻辑 | 两个**正交**维度（能否 vs 愿否） | 同一核心概念贯穿两个**层次**（firm-level vs product-level） | 信息内容 vs 信息可见度 |
| 理论来源 | 学习文献 meta-consensus | 单一核心理论（信息不对称） | 危机响应的信息处理视角 |
| moderator 机制 | 各自独立（transfer vs attention） | 同向（都削弱 monitoring） | 互补（内容 + 注意力） |

**适用条件**:
- 主效应 X→Y 是学习/改变过程（failure → improvement, event → adaptation），而非静态选择
- 领域文献确实存在 ability/motivation 二分的 meta-consensus（organizational learning, behavioral theory of the firm）
- 两个 moderator 一个偏结构性资产（决定"能否"），一个偏感知性资产（决定"愿否"）

**注意事项**:
- 框架必须在引入第一个 moderator 之前就明确说明，且每个 moderator 段落开头应回扣其在框架中的位置（"the transfer enabler..." / "the attention enabler..."）
- 若两个 moderator 实际都偏能力侧或都偏动机侧，不要硬套——退化为逐个理论引入
- 动机侧 moderator 若存在两派相反推论（如品牌质量既可能侵蚀差异化优势→增强动机，也可能产生绝缘效应→削弱动机），允许配无向假设（nondirectional H），详见 `sentences/moderation.md`「equivocal 双边论证」

**反模式**: 如果领域文献没有 ability/motivation 的公认二分，或 moderator 无法 clean 地归入"能否/愿否"，不要用此框架——强行贴标签会让审稿人质疑概念对齐。


