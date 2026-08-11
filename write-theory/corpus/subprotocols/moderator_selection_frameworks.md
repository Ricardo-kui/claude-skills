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

## Framework: Willing-and-Able Dual-Axis（动机/能力双轴，DesJardine–Li–Shi 2025 型）

**适用场景**: 4+ 个调节变量且可分成两组时，用**机制要素双轴**组织——一组调节攻击方/施动方的**动机（motivation）**，另一组调节其**能力（ability）**（willing and able 框架）——给"为什么有这么多调节变量"提供统一理论解释，避免 moderator 堆砌感。

**范文来源**: DesJardine, Li & Shi (2025), *Academy of Management Journal*（H2a/b 威胁→motivation；H3a/b 奖项→ability）

**原文锚点**:
> "Beyond the motivation to influence information intermediaries, common owners need the ability to do so, as reflected in the notion of being willing and able (Durand, Hawn & Ioannou, 2019). In line with competitive dynamics research (Chen & Miller, 2015), where ESG reputational threats affect a common owner's motivations to engage in information-based competition, ESG reputational opportunities affect their ability to make these attacks. By ESG reputational opportunities, we mean situations or circumstances that impact a firm's public image for ESG and the malleability of that image to outside influence."

**框架结构**:
```
Beyond the motivation to influence [intermediaries], [attackers] need the ability to do so, as reflected in the notion of being willing and able ([citation]). In line with [domain research] ([citation]), where [axis-1 moderator family: threats/pressure] affect a [attacker]'s motivations to engage in [attack], [axis-2 moderator family: opportunities/resources] affect their ability to make these attacks. By [construct of axis 2], we mean [definition — situations that impact the malleability of the image to outside influence]. [Axis-2 source] can arise from a variety of factors, particularly [concrete source].

[随后每个轴一个独立小节，轴内每侧一个假设：轴 1 = H2a/H2b 镜像对；轴 2 = H3a/H3b 镜像对——见 E_moderation E9]
```

**为什么有效**:
- **机制要素映射**: 调节变量不是平行堆叠，而是分别锚定到机制链的不同环节（motivation vs ability）——给"为什么有 4 个调节变量"提供元框架，满足 write-theory 硬约束 #11（≥2 moderators 必须有理论驱动的选择理由）
- **两轴与竞争动态理论对接**: 威胁→动机、机会→能力，直接用 competitive dynamics 的 willing-and-able 传统（Chen & Miller 2015; Durand et al. 2019）——元框架有理论来源而非自造分类
- **构念定义嵌入**: "By [opportunities], we mean [definition]"——调节构念定义就地完成，不另开定义段
- **轴间顺序 = 推理依赖**: motivation 轴在前（H2）、ability 轴在后（H3）——先问"想不想"再问"能不能"，与主效应机制链的展开顺序一致

**适用条件**:
- 调节变量可干净地分成"动机/意愿侧"与"能力/机会侧"两组（威胁、压力、争议→动机；资源、奖项、信息→能力）
- 每组内部又可按角色侧镜像展开（攻击方 vs 受害方）——与 E9 配对使用
- 主效应机制链包含动机与能力两个环节（或至少能论证两轴分别作用于不同环节）

**注意事项**:
- 框架必须在引入第一组调节变量之前就明确说明
- 每轴的理论锚点必须真实（willing-and-able 是竞争动态传统，不可自造）
- 两轴调节必须都有完整 why chain——不能 motivation 轴详细而 ability 轴只列方向
- 轴内仍执行 conditionality gate（改变动机/能力 ≠ 自动成立调节）

**反模式**: 只有两个调节变量也硬套双轴；两轴构念在概念上不可分（威胁也影响能力、奖项也影响动机时，先检查概念边界）；轴名与机制链环节不匹配。


