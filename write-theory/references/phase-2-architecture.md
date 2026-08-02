# Phase 2: architecture

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

### Phase 2: 架构决策

基于 7 因素确定 Theory section 宏观结构；按情境需要前置 Institutional Background；制度冲击类研究触发 Theory Lens 特殊适配。

**2.1 架构决策（7 因素）**

基于 Pollock 2025 Ch06 Table 6.1，确定 Theory section 的宏观结构：

| 因素 | 诊断问题 | 结构含义 | Showing vs Telling 要求 |
|------|---------|----------|------------------------|
| **理论域数量** | 论文涉及几个理论域？ | 1 个 → progressive coherence；2+ → 需要整合框架 | 每个理论域首次引入时，用 1 个具体研究场景说明其适用范围 |
| **构念新旧** | 有全新构念吗？ | 是 → early placement + 专门定义+区分段落；否 → 可灵活放置 | 新构念定义后必须跟 1 个 concrete illustration |
| **主角配置** | IV 还是 DV？几个？ | 单一 DV → DV 先行；单一 IV → IV 先行；多 IV+DV → 取决于叙事线 | 每个主角构念首次出现时，用 1 个具体案例说明其操作化方式 |
| **配角配置** | 配角是什么角色？ | DV 配角 → early；Mediator/Moderator → 随故事展开 | 配角构念引入时，用 1 个微型场景说明其调节/中介逻辑 |
| **Context** | Context 对理解角色必要吗？ | 必要 → 开头；提供例子 → 穿插；实验/泛化 → 最后 | Context 描述需包含 ≥1 个具体行业/公司/制度实例 |
| **Figure** | 理论图还是总结模型图？ | 理论图 → 相关讨论处；总结模型图 → 全部假设后 | 理论图的文字描述中，每个路径必须有 1 个场景化说明 |
| **叙事节奏（Ch02-Ch03）** | Theory section 的动作-评论比例？ | 理论推演（stroke）> 文献解释（glide），但不能没有 glide | Stroke 段落每个因果步骤后需有 concrete illustration；Glide 段落用比喻/场景解释 |

**叙事节奏详细说明（第7因素）**：

Pollock Ch03 用 "stroke and glide"（划桨与滑行）比喻动作与评论的平衡——原书只给定性判据："全 stroke 无 glide → forced march（急行军）"，"全 glide 无 stroke → ponderous pace（沉闷）"（Pollock 2025 Ch03），**未给具体百分比**。下表的百分比是 **skill 的操作化建议**（把 Pollock 定性原则具体化为可执行阈值，非原书数字）：
- **Stroke（动作）**：推进理论的主动作——因果推理、假设推导、机制展开
- **Glide（评论）**：帮助读者吸收的解释——文献总结、定义澄清、边界说明

| 段落类型 | 推荐比例（skill 操作化） | Showing vs Telling 要求 | 风险（Pollock 原书定性判据） |
|---------|---------|------------------------|------|
| 机制推演段落 | 70% stroke / 30% glide | 每个 stroke 句子后需有 concrete illustration 或比喻 | 全 stroke → "forced march" |
| 文献铺垫段落 | 40% stroke / 60% glide | Glide 段落用具体研究场景解释，非纯引用罗列 | 全 glide → "ponderous pace" |
| 构念定义段落 | 50% stroke / 50% glide | 定义后立即给 1 个例子 | 纯定义无方向 → 读者失去兴趣 |

#### 章节标签惯例

管理学顶刊的 Theory 章节**不一定**有显式的 "Theory and Hypotheses" 标签（验证自 14 篇 MVP30 论文）：

| 标签做法 | 比例 | 典型期刊 |
|---------|------|---------|
| 无 "Theory" 标签，直接用主题标题进入（如 "Ingratiation and Resentment"、"State Ownership and Product Innovation"） | ~45% | ASQ, AMJ 主流 |
| "Theory and Hypotheses" 或 "Theoretical Background" | ~35% | SMJ, JM, JMS |
| "Literature Review and Conceptual Background" | ~15% | JM 特有 |
| "Institutional Background" + "Conceptual Background"（或 "Theory"） | ~5% | JMR |

**选择指南**：
- **ASQ/AMJ 目标** → 推荐使用主题标题，不强制 "Theory" 标签
- **SMJ/JM/JMS 目标** → "Theory and Hypotheses" 是安全默认
- **JM 且假设嵌入在文献回顾中** → 可用 "Literature Review and Conceptual Background"
- **情境特殊、需前置背景** → 见 Phase 2.2 Institutional Background

输出：**推荐的段落序列**。

→ 每段叙事功能标注：
```
P1: 承接 knot（knot inheritance）
P2-P3: 加深 knot（knot deepening）
P4-P(N): 机制 tying（knot tying through mechanism）
最后一个假设 → 自然收敛进入 METHODS（无独立 Closure 段）
```

**2.2 Institutional Background**（可选前置模块）

**适用场景**: 研究情境特殊、读者可能不熟悉制度/行业背景时——如果读者不理解情境，就无法理解后续的理论论证。

**判断标准**（满足任一即考虑添加）：
- 实证情境涉及特定法律制度（如召回法规、游说披露法、反SLAPP法）
- 实证情境涉及特定行业惯例（如风险投资 syndicate、FDA 审批流程）
- 实证情境的 institutional detail 是理论机制的必要前提

**位置**：Introduction 之后、Theory 之前。可作为独立章节（"Institutional Background"）或嵌入 Theory 第一节。

**范文**：
- Singh & Grewal 2023 (JMR): "Institutional Background" 章节详述汽车召回制度和游说披露法，然后进入 "Conceptual Background"（即 Theory）
- Shi, Grewal & Sridhar 2021 (JM): "Literature Review" 中包含 SEC FRR44 披露制度的说明

**关键特征**：
- 描述性而非论证性——说明制度/情境"是什么"，不在此处推演假设
- 信息密度高——不展开理论对话，只提供读者理解后续论证所需的事实基础
- 篇幅控制——通常不超过 Theory 总篇幅的 20%

**不需要此模块的情况**：
- 研究情境是通用商业现象（如 CEO 薪酬、董事会构成、并购）
- 情境信息可以 1-2 句嵌入 Theory 开篇即交代清楚

**2.3 制度冲击类研究的 Theory Lens 特殊适配**（条件触发——由 1.3 制度冲击检测结果决定）

使用自然实验/制度冲击/准实验设计（IV, DiD, RDD）时，Theory Lens 段须额外完成三层论证（外生性 / 机制 / 识别基础），且识别策略的理论论证必须在 Theory 部分完成（不能只在 Methods 呈现）。IV / DiD / RDD 各自的 Theory 要求、生存分析时间动态论证与句式模板见 `../corpus/subprotocols/institutional_shock_lens.md`。

---
