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

---

<!--
pattern_id: transfer_vs_attention_enablers
build_type: 机制推演型 / 调节效应型
source_papers: ["kalaignanametal2013"]
confidence: medium
status: ready_for_corpus
-->

## Framework: Transfer vs Attention Enablers（能力转移 vs 动机注意，Kalaignanam et al. 2013 型）

**适用场景**: 主效应是失败/冲击后的学习或可靠性改进；恰好两个调节，一个改变**能否把教训转移到产品族**（ability / transfer），一个改变**是否把事件当回事**（motivation / attention）。不要套 Willing-and-Able 的 4+ 攻击情境。

**范文来源**: Kalaignanam, Kushwaha & Eilert (2013), *Journal of Marketing*

**原文锚点**:
> "we identify “transfer enablers” and “attention enablers” as contingency factors for improvement in product reliability."

**框架结构**:
```
It is well recognized that the extent to which [units] learn depends on their ability and motivation to do so ([citations]). Consistent with this stream, we identify “[transfer enablers]” and “[attention enablers]” as contingency factors for improvement in [mediator].

[Transfer enabler]: [shared assets / common platforms] enable the transfer of learning from the [event] in one [product] to other [products] in the family.
[Attention enabler]: the extent to which [units] attend to the [event] depends on prior [quality / reputation], which alters the motivation to learn.
```

**为什么有效**:
- 两个调节不是平行堆砌，而是分别锚定学习的能力侧与动机侧
- 比 Willing-and-Able（DesJardine 2025）更窄：这里是学习转移 vs 注意力，不是攻击意愿 vs 攻击能力
- 允许两个调节的假设形式不对称（一个定向增强，一个非定向竞争）

**适用条件**:
- 主效应是冲击后的学习/质量改进，不是多受众攻击
- 恰好两个调节，且能干净分成 transfer vs attention
- 框架必须在引入第一个调节之前说出

**注意事项**:
- 不要把 2013 的双使能误标为 E3（E3 要求 ≥3 个平行嵌入小节）
- attention 侧若理论对立，用非定向假设，不要在框架段预先选边

**反模式**: 把 cost/revenue 文献里的资产共享直接写成学习调节，却不论证 transfer；把品牌质量写成通用正向/负向调节，却不论证 attention/motivation。

---

<!--
pattern_id: uet_situation_characteristic_nested_moderators
build_type: 机制推演型 / 调节效应型
source_papers: ["lunetal2026"]
confidence: medium
status: ready_for_corpus
-->

## Framework: UET Situation–Characteristic Nested Moderators（特征→情境嵌套，Lun et al. 2026 型）

**适用场景**: 主效应来自战略姿态/实验逻辑；恰好两个调节，且必须嵌套——W1 是**高管特征/功能权力**（改变主机制如何被enact），W2 是**组织情境**（改变该特征如何转化为结果）。不要把二者写成平行 E3。

**范文来源**: Lun, Zurbruegg, Mount & Cheong (2026), *Entrepreneurship Theory and Practice*

**原文锚点**:
> "In addition to executive roles, UET also highlights that organizational context acts as a critical contingency influencing how executive characteristics translate into firm outcomes."

**框架结构**:
```
[Secondary theory] asserts that organizational outcomes reflect [executive characteristics] and that [organizational context] influences how those characteristics translate into outcomes ([citation]).

[W1 — characteristic / role power]: the [functional executive] who carries the [countervailing operational logic] makes [reliability / quality] salient in collective decisions, [buffering] the [posture]→[failure] relationship.
[W2 — situation / attentional load]: when [portfolios] concentrate in [high-uncertainty stage], demands on [executive] attention increase, reducing the extent to which [W1] can mitigate the risk; the reverse holds when [portfolios] concentrate in [stable stage].
```

**为什么有效**:
- 两个调节不是平行堆砌：W2 条件化的是 W1 的缓冲能力，对应 E6 而非 E3
- 选型理由来自 UET 自身的「特征 × 情境」命题，不是事后找两个相关变量
- 与 Dual-Lens Main/Boundary（Hoffmann）互补：那里次框架是 taxonomy；这里次理论直接规定嵌套顺序

**适用条件**:
- 主效应已由第一理论解释；第二理论是 UET 或同等的 executive-influence 理论
- W1 必须是可点名的功能角色/权力，W2 必须改变该角色的注意或转化条件
- 框架须在引入 W1 之前或 W1→W2 过渡句中说出

**注意事项**:
- 不要把 W2 写成另一个独立 two-way（那是 E3）
- 薪酬比等结构代理不能在框架段写成注意力或决策权重的直接证据

**反模式**: 选 COO/CFO 只因为数据里有 title；选生命周期只因为创新文献常用，却不论证它如何改变该高管的注意带宽。




### 变体 A：T5_moderator_metaframework_trilevel（moon2026）

**模板/骨架**:
> "Research on [lens] argues that because [scarce resource], the degree to which [actor] pays attention to [change] may depend on individual, organizational, and contextual factors. Accordingly, we examine [N] key factors: [W1], [W2], and [W3]. At the individual level, [W1 rationale]. At the organizational level, [W2 rationale]. At the environmental level, [W3 rationale]. Taken together, we expect that each of these factors shapes the degree to which [actor] [response]."

来源：Moon et al. (2026, Journal of Marketing)。




### 变体 B：存量/流量双面向 moderator 元框架（stock–flow facet pairing）

<!--
pattern_id: stock_flow_capability_moderator_pairing
build_type: 假设树型/调节效应型（多 moderator 元框架）
source_papers: ["anand_mukherjee_2024_org_science"]
confidence: medium（单篇，产品召回主题 expert_audit_override 2026-08-29 升 VERIFIED）
-->

**适用场景**: 同一能力构念提供两个操作化（存量 measure + 流量 measure）时，用存量/流量分解作元框架，使双 moderator 读作刻意拆解而非控制变量堆放（满足 C18）。

**骨架**:
```
[Capability] stocks and [capability] efforts represent two integral aspects of
[capability] ([foundation citation, e.g., absorptive capacity]).
[Stock facet] represents a firm's capabilities to [identify / discern value of /
assimilate] relevant new knowledge ([accumulated measure]).
[Flow facet] is an indication of its prevailing [innovation culture and
infrastructure] that support [ongoing search and identification] ([recent
effort measure]).
These two facets can have different impacts on [the differentiated mechanisms
across outcome types].
```

**为什么有效**: 存量面向"过去积累给了什么资源"、流量面向"当下投入维持什么状态"——两面各自映射到不同学习机制，为 2×2 单元格假设提供独立的理论依据来源。
**注意事项**: 两个 measure 必须真分属存量/流量（累计存量 vs 当期强度）；若两者高度相关需在 Methods 处理共线。
**反模式**: 同一构念的两个代理变量轮流试错式检验（无元框架，审稿人问"why these two"）。

**原文锚点**: "Firms' stocks of innovations and their innovation efforts represent two integral aspects of the innovation capabilities of firms."（§3.2）

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:stock_flow_capability_moderator_pairing -->


### 变体 C：主效应后两类因子 Moderator 路线图（Gulati_Lavie_Singh_2009 型）
> 论证角色：Framing（在主效应假设与调节分支之间插入一段元框架过渡——先声明"主效应已论证完毕"，再用两类因子给全部 moderator 定位并逐一预告）

<!-- pattern_id: moderator_roadmap_twoclass_metaframework; build_type: 调节效应型/假设树型; source_papers: ["Gulati_Lavie_Singh_2009_SMJ"]; confidence: low -->

**适用场景**: ≥2 个 moderator 并行调节同一主效应时，用一个两类因子元框架（如对手侧 vs 企业侧、环境 vs 组织）回答"为什么选这些 moderator"，并在分支展开前给出路线图。
**排列模式**: 主效应完成信号 → 条件化转折 → 两类因子元框架 → First/Then/Finally 三分支预告
**范文来源**: Gulati, Lavie, and Singh (2009), SMJ — partner distinctiveness（伙伴侧）vs firm resources & firm-specific uncertainty（企业侧）

**骨架**:
```
[主效应完成信号] Thus far, we have considered the direct effect of [X] on [Y].

[条件化转折] It is possible, however, that [X] effects may be contingent and vary
systematically with [class-1]- and [class-2]-specific factors.

[路线图预告] Next, we consider such moderating effects. First, we argue that [W1
potential benefits] are likely to depend on [class-1 factor: extent to which
novel opportunities arise]. We then propose that [W2] benefits may be contingent on
[class-2 factor: focal actor's own capacities]. Finally, we examine how [W3
perception factor] shapes the value of [X].
```

**为什么有效**: 一段话同时完成 C18 要求的 moderator 选择元框架（两类因子各管一侧）与分支地图，读者带着分类预期进入每个调节小节，不会把三个 moderator 当成随手堆砌。
**注意事项**: 两个因子类必须与 moderators 一一对应且互斥（本篇：伙伴侧 1 个 + 企业侧 2 个）；每个 moderator 的预告只给一句逻辑，细节留给分支小节，避免重复论证。
**反模式**: 无元框架逐个 "We also examine the moderating role of ..."——审稿人会问为什么是这几个 moderator。
**原文锚点** (Gulati, Lavie & Singh 2009, SMJ):
> "Thus far, we have considered the direct effect of PSE on value creation in alliances. It is possible, however, that PSE effects may be contingent and vary systematically with partner- and firm-specific factors."

<!-- wb:gulati_lavie_singh_2009_partnering_experience:moderator_roadmap_twoclass_metaframework -->

### 框架 B：意愿×机会双路径调节论证（westphal_bednar2005 型）

**模板**:
> "[Moderator W] should lower the perceived risk of [voicing]: [justification 1] ([citations]). Accordingly, when [W is high], [actors] should be less hesitant to [voice] before others have done so. Moreover, [W] increases the frequency of [informal communication] ([citations]). As a result, [actors] should not only be less reluctant to [voice], but they should also have more frequent opportunities to do so. Therefore, [W] should facilitate the discovery of [shared concerns], thus reducing [construct]."

**来源**: westphal_bednar2005 (ASQ), Theory P11-P12（friendship ties 与 demographic homogeneity 两个 moderator 内部复现）

**原文锚定**:
> "outside directors who are connected by personal friendship ties should not only be less reluctant to express their concerns about corporate strategy to each other, but they should also have more frequent opportunities to do so"

**关键特征**:
- 每个 moderator 沿同一条双路径论证：意愿路径（降低表达风险的感知）+ 机会路径（增加非正式沟通频率），"not only... but they should also..." 收束句显式并置两路径
- moderator 不是外生挑选，而是从主机制的两个薄弱环节（不敢说 / 没机会发现共识）反推出来的——调节逻辑直接焊在主机制前提上
- 双路径最后收敛到同一构念动词："facilitate the discovery of shared concerns, thus reducing [construct]"，保证 moderator 与 DV 的构念链条闭合
- 论文内部两 moderator 复现同一框架（friendship ties / demographic homogeneity 各写一遍），形成天然平行结构

**适用**: 主机制可分解为"表达意愿+表达机会"两个环节的调节假设；含行为表达中介（voicing）的抑制类构念（misperception、沉默、误判）

**禁忌**: 双路径必须都能独立成立且都指向同一中介行为，若机会路径与意愿路径冲突（如沟通更频繁反而暴露分歧）需另行处理；moderator 与主机制前提无对应关系时不得硬套此框架

## Framework B: Newcomer Voice-Integration Axis（新声音整合轴，what_changes_after_women_enter_top_manage_2020 型）

**验证状态**: VERIFIED (expert_audit_override 2026-08-29: 用户点名喜爱本篇，单源足矣)

**适用场景**: 主效应是"某类新进入者/新成员携独特视角进入集体决策体并改变其认知/输出"；恰好两个调节变量，均可由**单一整合机制**（新声音能否被听见、纳入集体思维）统一证成；两个 moderators 同时调节 X→M 的多条机制路径。moderator 在此承担 new voice integration 功能，而非泛泛边界条件。

**与近邻框架区分**:
- vs Willing-and-Able（DesJardine 2025）：那是攻击方的动机/能力双轴；本轴是**接收方对新声音的整合能力与整合难度**
- vs Information-Asymmetry（Darby 2026）：同属"核心概念统一多 moderator"家族，但核心概念是整合而非信息不对称，且本轴 moderators 可同时作用于多条中介路径
- vs UET Situation–Characteristic Nested（Lun 2026）：那是 W2 条件化 W1 的嵌套结构；本轴两 moderators 平行但共享同一整合机制证成

**框架结构**:
```
[选择理由句——单一机制统一证成]
We further theorize that the relationships between [X] and subsequent shifts
in [M1/M2] are moderated by [W1] ..., and by [W2] .... We select these
moderators as they affect [single integration mechanism] and such integration
is central to the ability of [new actors] to influence the [collective]
([citations]).

[W1: 接收端整合经验——双理由]
理由1: 集体已有整合同类差异成员的经验与技巧，刻板印象随暴露衰减.
理由2: 内群体归类——新成员被视为相似者，其（可能非传统的）观点更快被纳入集体决策
([social identity / newcomer socialization / minority voice citations]).
→ 对 M1 与 M2 的位移同时放大 (H[W1]a / H[W1]b 同构配对).

[可选阈值衰减]
W1 的放大效应在超过表示性阈值后边际递减，理由: (a) 集体已内化开放性，整合不再
依赖同类成员协助; (b) 认知已被先前的同类成员改变，新任命收益递减 (H 衰减型).

[W2: 整合难度——双理由]
理由1: 高 newcomer/incumbent 比例引发资源竞争与权力斗争，阻碍整合.
理由2: 同时进入者形成亚群（subgroup），hampering 整合.
→ 新声音整合受阻，M1/M2 位移被稀释 (H[W2]a / H[W2]b).
```

**原文锚定**: "We select these moderators as they affect the integration of new
appointees into the TMT and such integration is central to the ability of new
executives to influence the TMT."

**为什么有效**:
- 选择理由句本身是模板：一句话回答"为什么是这两个 moderator"——满足 write-theory 硬约束（≥2 moderators 必须有理论驱动的选择理由），且证成轴（整合）直接来自主效应机制（新成员须经整合才能影响集体）
- 两个 moderators 分别锚定整合的**能力侧**（接收端经验/内群体归类）与**难度侧**（竞争/亚群）——轴内对称、轴间互补，避免堆砌感
- 同时调节多条中介路径（H[W]a/H[W]b 同构配对），使调节假设族与双中介架构同构，假设体系整体对称
- 阈值衰减变体把"more is always better"的线性外推截断，预防审稿人"表示性饱和"质疑

**适用条件**:
- 主效应机制天然包含"新成员影响须经集体整合"环节（TMT/董事会/团队进入、少数群体发声类研究）
- moderators 可干净归入整合能力侧 vs 整合难度侧
- 框架须在引入第一个 moderator 之前说出选择理由句

**注意事项**:
- 整合机制须有独立文献锚（social identity / newcomer socialization / minority voice），不可自造
- 衰减阈值需要大样本支撑——样本受限时降级为讨论段建议而非正式假设
- 两个 moderators 的假设句式应同构（"...leads to a greater subsequent (a) increase in [M1] and (b) decrease in [M2]"），保持配对节律

**反模式**: 只有两个调节变量也硬造双轴（本轴恰配 2 个）；moderators 实际作用于 M→Y 第二阶段却写成 X→M 第一阶段；把"female incumbency"类接收端变量写成泛化情境强度而不指明其整合功能；无选择理由句直接并排引入两个调节。
