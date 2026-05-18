# 模块组装指南

## 组装工作流

```
输入：Gap类型 + 贡献维度 + [可选]研究描述 + [可选]目标期刊
│
▼
Step 1: 选择布局类型
├─ 查 layout-atlas.md → 决策树
├─ 标准型（默认，6-7段）
├─ 扩展型（Incommensurability / Phenomenon / 多理论对话）
└─ 紧凑型（Incompleteness + 单一贡献 / 成熟领域）
│
▼
Step 2: 为每段选择模块
├─ P1 Hook → 查 module-index.md Hook选择器
├─ P2 Literature → 查 Conversation策略
├─ P3 Gap → 查 module-index.md Tension选择器
├─ P4 Stakes/Theory → 查 module-index.md Stakes选择器
├─ P5 Preview → 查 layout-atlas.md 组合特定模板
└─ P6-P7 Contribution → 查 makadok-frames.md + gap-to-contribution
│
▼
Step 3: 构建 Transition 链
├─ Hook → Literature: transitions/hook-to-literature.md
├─ Literature → Gap: transitions/literature-to-gap.md
└─ Gap → Contribution: transitions/gap-to-contribution.md
│
▼
Step 4: 运行组合规则检查
├─ 必须配对检查
├─ 互斥检查
└─ 推荐组合提示
│
▼
Step 5: 质量检查（QC）
└─ 运行 QC检查点
```

---

## 模块组合规则

### 必须配对（Mandatory Pairing）

以下模块必须成对出现，单独使用会导致叙事断裂：

| 模块 A | 必须配对 | 原因 | 常见断裂 |
|--------|---------|------|---------|
| `06-paradigm-challenge` (Hook) | `04-reality-contradicts-consensus` (Tension) | 范式挑战必须后续有现实与共识的矛盾作为支撑 | 挑战后无证据，显得是稻草人 |
| `05-literature-consensus-blindspot` (Hook) | `03-structural-blindspot` 或 `05-overlooked-alternative` (Tension) | 文献盲点必须后续解释为什么是结构性/系统性盲点 | 只说"被忽视了"但不解释为什么长期被忽视 |
| `03-data-shock` (Hook) | `01-despite-progress-unaddressed` (Tension) | 数据冲击建立了stakes，但还需要解释"已有进展中遗漏了什么" | 数字震撼后直接进入理论，缺乏学术对话 |
| `04-puzzle-paradox` (Hook) | `02-implicit-assumption-wrong` (Tension) | 谜题/悖论暗示了某个隐性假设错误 | 只描述谜题但不指出假设错误 |
| `16-theory-contradiction-empirical-paradox` (Hook) | `04-reality-contradicts-consensus` (Tension) | 理论矛盾必须后续有系统性的经验悖论支撑 | 理论对立后无经验证据 |

### 互斥组合（Mutually Exclusive）

以下模块不能同时出现在同一篇 Introduction 中，会造成功能冗余或叙事冲突：

| 模块 A | 不能与 B 同用 | 原因 | 修正方案 |
|--------|--------------|------|---------|
| `03-data-shock` (Hook) | `02-quantified-economic-loss` (Stakes) | 数据冲击已含 stakes，重复会造成数字疲劳 | 若用了 data-shock， Stakes 改用 `01-resource-allocation-guidance` 或理论重要性论证 |
| `12-surprising-fact` (Hook) | `04-reality-contradicts-consensus` (Tension) | surprising fact 本身已是现实矛盾，Tension 需换种表述 | 改用 `02-implicit-assumption-wrong` 或 `03-structural-blindspot` |
| `06-paradigm-challenge` (Hook) | `01-despite-progress-unaddressed` (Tension) | 范式挑战是高能量颠覆，"尽管已有进展"是低能量渐进，能量不匹配 | 范式挑战论文的 Gap 段应使用 `04-reality-contradicts-consensus` |
| `14-cost-benefit-tension` (Hook) | `08-cost-vs-benefit` (Tension) | Hook 和 Tension 使用同一套成本-收益逻辑，造成重复 | 若 Hook 已用成本-收益张力，Gap 段改用 "despite progress" 或 "structural blindspot" |
| `08-quotation-hook` (Hook) | `19-forward-looking-shift` (Hook) | 两者都是"元话语"型 Hook，功能重叠 | 二选一，quotation-hook 适合过程理论，forward-looking-shift 适合范式转移 |

### 推荐组合（Recommended Pairing）

以下组合虽然不是必须，但能产生 1+1>2 的叙事增强效果：

| 场景 | 推荐组合 | 增强效果 |
|------|---------|---------|
| Incommensurability + Mechanism | `06-paradigm-challenge` → `04-reality-contradicts-consensus` → `opposing-forces` (Mechanism) | 从颠覆共识到展示对立力量，形成完整的"挑战-修正"叙事弧 |
| Inadequacy + Mechanism | `05-literature-consensus-blindspot` → `01-despite-progress-unaddressed` → `opposing-forces` / `context-reversal` | 从"文献片面"到"遗漏了负向机制"，形成"盲区揭示"叙事弧 |
| Incompleteness + Boundary | `03-data-shock` → `01-despite-progress-unaddressed` → `dual-path-ability-motivation` (Mechanism) | 数据建立紧迫性，渐进缺口降低防御性，双路径机制提供精细预测 |
| Inadequacy + Constructs | `01-cross-disciplinary-analogy` → `03-structural-blindspot` → 构念界定模块 | 跨学科类比展示混淆的普遍性，结构性盲点解释为什么长期未澄清 |
| Incommensurability + Boundary | `15-classic-debate-constraint` → `07-same-policy-opposite-effects` → 边界条件模块 | 经典辩论建立对立，同一政策的相反效果证明需要边界条件来调和 |
| Phenomenon 型论文 | `17-phenomenon-market-evolution` → `09-evolving-social-issue` → `02-quantified-economic-loss` | 市场演变→社会问题→经济损失，形成"现象-问题-代价"的 stakes 递进链 |

---

## 段落级组装示例

### 示例 1: Incommensurability + Mechanism（范式挑战型）

**组合**: Combo 8（Zhou 2017 模式）
**布局**: 扩展型（8段）
**期刊**: ASQ

**P1 Hook** → `06-paradigm-challenge`
> "Conventional wisdom holds that state ownership hinders firm innovation by creating dual agency problems ([citations]). This prediction seems intuitively correct because state owners may prioritize political goals over economic efficiency. However, Chinese state-owned enterprises consistently appear among the world's most innovative firms: in 2014, 106 Chinese firms appeared on the Fortune Global 500 list, two-thirds of which were SOEs. This persistence suggests that the prevailing view of state ownership may be incomplete."

**Transition** → `hook-to-literature` 模板 A
> "This tension is not merely a China-specific anomaly; it reflects a broader theoretical gap concerning how institutional logics shape firm innovation."

**P2 Literature** → Non-Coherence Conversation
> 效率逻辑 vs 制度逻辑的对立（2-3句建立对话）

**Transition** → `literature-to-gap` 模板 D
> "The efficiency logic predicts that state ownership reduces innovation; the institutional logic predicts the opposite. Yet neither perspective explains when and why one logic dominates the other."

**P3 Gap** → `04-reality-contradicts-consensus`
> "The dominant view holds that [state ownership hurts innovation] ([citations]). Yet [SOEs' innovation performance persists even in competitive global markets], suggesting that [the mechanism linking state ownership to innovation] may be [fundamentally different than theorized]."

**P4 Theory Lens** → 内部模板（制度逻辑引入）
> "Drawing on institutional theory, we argue that..."

**P5 Preview** → 对立力量机制
> "We distinguish between two countervailing effects of state ownership on innovation..."

**P6 Findings Preview** → 内部模板
> "Our analysis of [data] reveals that..."

**P7-P8 Contribution** → Makadok Mechanism
> "We explain why state ownership affects firm innovation by identifying [mechanism] as the mediating mechanism..."
> "These findings are theoretically important because they reveal..."

---

### 示例 2: Inadequacy + Constructs（构念辨析型）

**组合**: Combo 3（Pollock 2015 / Han 2024 模式）
**布局**: 标准型（6段）
**期刊**: SMJ

**P1 Hook** → `05-literature-consensus-blindspot`
> "Extensive research has established that positive firm reputation enhances stakeholder support and firm performance ([citations]). This work treats reputation's benefits as the natural endpoint of analysis. However, what happens when positive reputation becomes excessive — transforming from an asset into a liability — remains largely unexamined."

**Transition** → `hook-to-literature` 模板 A
> "This blind spot is not merely a semantic curiosity; it reflects a deeper theoretical confusion concerning the distinction between reputation and celebrity."

**P2-P3** → 构念混淆指出 + 系统差异
> "Most research on [topic] has treated [reputation and celebrity] as interchangeable..."
> "We argue that reputation and celebrity differ in three theoretically consequential ways..."

**P4** → 理论论点
> "Because reputation is based on [quality signals] whereas celebrity is based on [attention signals], their effects on [outcome] diverge when..."

**P5** → 发现预览
> "Our analysis of [data] shows that..."

**P6** → Makadok Constructs
> "We differentiate reputation from celebrity, revealing how their distinct theoretical properties produce divergent effects on firm outcomes."

---

### 示例 3: Incompleteness + Boundary（渐进缺失型）

**组合**: Combo 2（Eilert 2017 模式）
**布局**: 紧凑型（5段）
**期刊**: JM

**P1 Hook** → `14-cost-benefit-tension`
> "Recalls are costly; announcing and implementing one is associated with both direct costs in repair, restitution, or liability and indirect costs such as losses in reputation and market value. However, delaying a product recall may lead to even higher costs through fines, liability damages, and most importantly, diminished reputation."

**Transition** → `hook-to-literature` 模板 B
> "While the costs of recalls are well documented, the timing of recall decisions — and its consequences for firm performance — remains poorly understood."

**P2-P3** → `01-despite-progress-unaddressed` + 边界逻辑
> "Despite considerable progress in understanding the consequences of product recalls ([citations]), the conditions under which firms choose early versus late recall timing have remained largely unaddressed."
> "We argue that brand characteristics — specifically brand reliability — serve as a key boundary condition..."

**P4** → 发现预览
> "Our analysis of [data] reveals that..."

**P5** → Makadok Boundary
> "We identify brand reliability as a key contingency that determines whether early recall timing enhances or diminishes firm performance."

---

### 示例 4: Inadequacy + Phenomenon（新现象域型）

**组合**: Combo 6（DesJardine 2023 模式）
**布局**: 扩展型（9段）
**期刊**: SMJ

**P1 Hook** → `03-data-shock` + `17-phenomenon-market-evolution`
> "Over the past two decades, the rise of common ownership — in which large institutional investors hold significant stakes in multiple competing firms — has fundamentally altered the competitive landscape of U.S. industries."

**P2-P3** → 宏观趋势 + 核心矛盾
> "This trend has created a new governance challenge: institutional investors may simultaneously encourage cooperation and discourage competition among their portfolio firms."

**P4** → 研究问题
> "We ask: How does common ownership influence corporate social responsibility?"

**P5** → `01-despite-progress-unaddressed`
> "Although scholars have extensively studied the anticompetitive effects of common ownership ([citations]), its implications for CSR remain poorly understood."

**P6** → 理论论点
> "Drawing on agency theory and stakeholder theory, we argue that..."

**P7** → 机制阐述 + 发现预览
> "Our analysis reveals that..."

**P8-P9** → Makadok Phenomenon + Makadok Mechanism
> "We examine common ownership, offering a theoretically diagnostic context for reassessing the relationship between competition and CSR."

---

### 示例 5: Incompleteness + Mechanism（渐进缺失型）

**组合**: Combo 1（Wu 2025 模式）
**布局**: 紧凑型（5段）
**期刊**: OrgSci

**P1 Hook** → `13-domain-gap`
> "Research on corporate innovation has devoted substantial attention to how firms allocate resources to R&D and how these investments translate into patent output and new product introductions ([citations]). Yet this literature has largely overlooked the mediating organizational processes that determine whether R&D spending actually generates innovation."

**Transition** → `hook-to-literature` 模板 B
> "While the direct relationship between R&D investment and innovation is well documented, the mechanisms through which resource commitment becomes innovative output remain poorly understood."

**P2-P3** → `01-despite-progress-unaddressed` + 理论引入
> "Despite considerable progress in linking R&D intensity to innovation performance ([citations]), the specific organizational mechanisms that translate resource inputs into innovative outputs have remained largely unaddressed."
> "Drawing on organizational learning theory, we argue that absorptive capacity serves as a critical mediating mechanism..."

**P4** → 机制预览 + 识别策略
> "We distinguish between two dimensions of absorptive capacity—potential and realized—and argue that their joint configuration determines the R&D–innovation link."

**P5** → 发现预览
> "Our analysis of [panel data] reveals that..."

**P6-P7** → Makadok Mechanism
> "We explain why R&D investment affects firm innovation by identifying absorptive capacity as the mediating mechanism..."

---

### 示例 6: Inadequacy + Mechanism（视角盲区型）

**组合**: Combo 4（Keeves 2017 / Paruchuri 2020 模式）
**布局**: 标准型（6段）
**期刊**: ASQ / SMJ

**P1 Hook** → `05-literature-consensus-blindspot`
> "Extensive research has established that firms with greater prior alliance experience are more likely to form subsequent alliances and achieve better performance ([citations]). This work treats experience as uniformly beneficial, assuming that accumulated knowledge consistently improves partner selection and alliance management."

**Transition** → `hook-to-literature` 模板 A
> "This consensus, however, obscures a critical theoretical blind spot: it assumes that all experience is created equal, ignoring the possibility that certain types of experience may actually undermine future alliance success."

**P2** → `02-implicit-assumption-wrong`
> "The implicit assumption underlying this literature is that experience accumulation is monotonically beneficial. Yet this assumption overlooks the dual nature of prior experience: while repeated alliances build relational routines, they may also entrench rigid heuristics that misfit new partnership contexts."

**P3** → 对立力量机制
> "Drawing on the learning-curves literature, we argue that prior experience generates two countervailing forces—a competency effect that enhances coordination and a rigidity effect that impairs adaptation."

**P4** → 假设预览
> "We hypothesize that the relationship between prior experience and subsequent alliance performance follows an inverted U-shape..."

**P5** → 发现预览
> "Our analysis of [alliance history data] reveals that..."

**P6** → Makadok Mechanism
> "We explain why prior alliance experience affects subsequent performance by identifying the competency–rigidity trade-off as the underlying mechanism..."

---

## 常见组装错误

### 错误 1: Hook 与 Gap 强度不匹配

**症状**: Incommensurability 型论文用了冷启动定义或数据冲击 Hook。
**后果**: 读者感觉不到颠覆性，后文的 paradigm challenge 显得突兀。
**修正**: 高 Gap 强度必须配高能量 Hook（范式挑战 / 反直觉发现 / 理论矛盾）。

| Gap 强度 | 错误 Hook | 正确 Hook |
|---------|----------|----------|
| Incommensurability | `03-data-shock` | `06-paradigm-challenge` |
| Incommensurability | `13-domain-gap` | `16-theory-contradiction-empirical-paradox` |
| Incompleteness | `06-paradigm-challenge` | `03-data-shock` 或 `10-practical-puzzle` |

### 错误 2: Tension 重复或功能冗余

**症状**: 同时用了 "despite progress" 和 "reality contradicts consensus"。
**后果**: 读者困惑：到底是要渐进补充还是彻底颠覆？
**修正**: 选择一个核心 tension，其他用变体表达支撑。Incommensurability 论文不应出现 "despite progress"。

### 错误 3: Stakes 缺失或错位

**症状**: 指出 gap 后没有说明为什么重要。
**后果**: Reviewer 反问 "So what?"
**修正**: 每个 gap 声明后必须跟一个 stakes 句子。三种插入方式：
- Inline: "...has remained largely unaddressed. **This omission matters because** [theoretical consequence]."
- 独立句: "...has remained largely unaddressed. **The stakes are high**: [practical consequence]."
- 独立段（扩展型布局）: 2-3句展开 stakes。

### 错误 4: Contribution 提前出现

**症状**: 第一段就声明 "This paper contributes by..."
**后果**: 读者尚未被说服有问题存在，贡献声明显得无的放矢。
**修正**: Contribution 必须在 gap 建立之后出现，通常在 P6-P7。P1-P5 的工作是"建立问题"，P6-P7 才是"宣布答案"。

### 错误 5: Transition 链断裂

**症状**: Hook 很震撼，但下一段突然开始罗列文献；或 Gap 指出后，下一段直接进入理论细节，没有解释"为什么这个理论能回答这个问题"。
**后果**: 叙事跳跃，读者流失。
**修正**: 每段之间必须有 explicit transition。检查方法：遮住 Pn，只看 Pn-1 的最后一句和 Pn+1 的第一句，能否猜出 Pn 的内容？如果不能，说明 Transition 不足。

### 错误 6: 模块与贡献维度错位

**症状**: Mechanism 型论文用了 Constructs 的 Hook（如构念类比），或 Constructs 型论文用了 Mechanism 的 Tension（如 "机制不清楚"）。
**后果**: 读者对论文贡献的预期与后文不符。
**修正**:
- Constructs 论文的 Hook 必须让读者"意识到混淆的存在"（`05-literature-consensus-blindspot` / `12-surprising-fact`）
- Mechanism 论文的 Hook 必须让读者"感觉到解释的不足"（`05-literature-consensus-blindspot` / `06-paradigm-challenge`）
- Boundary 论文的 Hook 必须让读者"意识到情境的重要性"（`04-puzzle-paradox` / `15-classic-debate-constraint`）

### 错误 7: 忽视期刊偏好

**症状**: 给 SMJ 的论文写了 ASQ 长度的 Introduction；或给 ASQ 的论文写了 SMJ 式的紧凑 Hook。
**修正**: 查 `layout-atlas.md` 中的"期刊偏好与布局调整"表格。

---

## 组装后自检清单

### 结构完整性
- [ ] P1 Hook 存在且能量与 Gap 强度匹配
- [ ] P2-P3 Literature + Gap 形成完整的"共识→缺口"叙事弧
- [ ] P4 Stakes/Theory 解释了"为什么这个 gap 重要"或"用什么理论来回答"
- [ ] P5 Preview 不泄露过多细节，但给出足够预期
- [ ] P6-P7 Contribution 声明回答了四问（What / Why / What show / What move）

### 模块质量
- [ ] 每个使用的模块都来自语料库或内部模板，不是即兴发挥
- [ ] 必须配对的模块已配对
- [ ] 互斥组合未出现
- [ ] Transition 链无断裂
- [ ] ⭐ PREMIUM / ✓ STANDARD 模块占比 ≥ 50%？（若使用大量 🔬 EXPERIMENTAL 模块，需人工复核适配质量）
- [ ] 每个 🔬 EXPERIMENTAL 模块的 `验证状态` 区块已查阅，确认来源论文与自身研究的领域距离可控

### 一致性检查
- [ ] Hook 中建立的 stakes 在 Contribution 段得到回应
- [ ] Gap 中定位的缺口在 Preview 段得到解答预告
- [ ] Makadok 声明中的贡献维度与论文实际贡献一致
- [ ] 目标期刊的偏好已考虑（长度、理论深度、管理启示）

---

## Introduction DNA 指标

以下 5 个 DNA 指标是 Introduction 的**量化修辞指纹**，用于在组装完成后进行机器可解析的诊断，也可供下游 Skill（`/paper-review`、`/write-discussion`）调用。

| 指标 | 缩写 | 定义 | 计算方法 | 合格线 | 诊断价值 |
|------|------|------|---------|--------|---------|
| **Hook–Gap 能量一致性** | `HGEC` | Hook 的修辞能量等级与 Gap 张力等级是否同频 | 1=能量错配（如 Incommensurability 配 data-shock），2=能量守恒，3=能量递进（如 paradigm-challenge → reality-contradicts-consensus） | ≥2 | 识别"Hook 与 Gap 强度不匹配"错误 |
| **张力密度** | `TD` | P1–P4 中承载显式 tension 的段落占比 | `含 tension 模块的段落数 / P1–P4 总段落数` | ≥0.50 | 识别"Tension 重复或功能冗余"或"tension 缺失" |
| **Stakes 显化率** | `SER` | Gap 声明后 stakes 出现的及时性与充分性 | 0=完全缺失，0.5=inline 单句，1=独立段（≥2句，含理论或经验证据） | ≥0.5 | 识别"Stakes 缺失或错位" |
| **Transition 链完整性** | `TCI` | 段落间过渡是否连续无断裂 | 检查 4 个关键转接位（P1→P2, P2→P3, P3→P4, P4→P5）；每处 1=存在显式 transition，0=断裂或缺失 | ≥3/4 | 识别"Transition 链断裂" |
| **贡献四问覆盖率** | `CFQC` | Makadok 四问在 P6–P7 中的覆盖完整度 | 4-bit 向量：`[What, Why, What_show, What_move]`，每位 1=显式回答，0=缺失 | =4/4 | 识别"Contribution 提前出现"或"声明不完整" |

### DNA 指标使用规范

1. **自动计算时机**：在 Step 4（组合规则检查）之后、Step 5（QC）之前运行。HGEC 和 TCI 可直接由模块选择表推导；SER 和 CFQC 需人工标注后由机器校验。
2. **下游消费格式**：以 JSON 嵌入 `---metadata---` 区块（见 SKILL.md Output Format）。
3. **与 QC 的关系**：DNA 指标提供**量化失败信号**，QC 检查点提供**定性修复指南**。例如 `HGEC=1` 时，QC 触发"Hook 与 Gap 强度不匹配"修正方案。
4. **与三重验证的关系**：DNA 指标测量的是**本次组装的质量**；三重验证测量的是**每个模块的语料库置信度**。两者互补：即使模块本身是 🔬 EXPERIMENTAL（低语料库置信度），只要组装后的 DNA 指标全部合格，该 Introduction 仍可能是有效的——只是需要使用者承担更多的人工复核成本。
5. **可扩展性**：后续可引入 `Module_Pairing_Compliance`（必须配对遵守率）、`Journal_Length_Deviation`（段落数偏离目标期刊中位数的程度）和 `Validation_Coverage`（PREMIUM+STANDARD 模块占比）作为第 6、7、8 个指标。

---

## 模块适配手册

### 适配总则

模块不是填空题，而是**修辞模具**。模具的结构固定，但填充物（研究具体内容）必须自定义。

| 固定要素 | 可变要素 |
|---------|---------|
| 模块的修辞功能（颠覆/渐进/对比） | 研究领域、理论视角、经验设定 |
| 模块的句法骨架（连接词、逻辑关系） | 变量名称、机制描述、样本特征 |
| 模块在叙事链中的位置 | 段落长度、引用密度、语气强度 |

### Hook 适配规则

核心挑战：在你的研究领域中识别"共识"和"异常"。

**适配公式**：
```
[共识陈述：你的领域中什么被默认为真] + 
[异常证据：什么现象/数据/案例与此矛盾] + 
[暗示：现有理论可能不完整/错误]
```

**策略→组织理论示例**：
- 共识："Strategic management research assumes that competitive advantage stems from resource heterogeneity (Barney, 1991)."
- 异常："Yet empirical studies show that firms with nearly identical resource bundles often achieve vastly different performance outcomes."
- 暗示："This divergence suggests that the link between resources and advantage may be more contingent than previously theorized."

**反模式**：不要把"共识"写得像稻草人。必须引用真实文献支持。

### Tension 适配规则

核心挑战：将"缺口"从"没人研究过"升级为"理论上必须被解决"。

**适配公式**：
```
[文献已经做了什么（具体、有引用）] + 
[遗漏了什么（精确、不是泛指）] + 
[为什么这个遗漏导致理论失败（stakes）]
```

**升级检查表**：

| 弱表达 | 升级后 |
|-------|--------|
| "few studies have examined X" | "the mechanism linking X to Y remains theoretically underspecified" |
| "prior research has neglected Z" | "the implicit assumption that Z is uniformly beneficial rests on an untested boundary condition" |
| "we know little about W" | "current theories of W cannot explain why [counterexample]" |

### Stakes 适配规则

核心挑战：从"这是缺口"到"这是重要缺口"。

三种适配策略：

1. **理论级 Stakes**：如果不解决这个缺口，什么理论会崩溃？
   > "Without identifying the boundary condition of X, the [theory] risks becoming a tautology that explains all outcomes and therefore none."

2. **经验级 Stakes**：如果不解决这个缺口，什么实践决策会出错？
   > "Managers relying on the current consensus will systematically over-invest in X while neglecting Y, leading to [specific inefficiency]."

3. **学科级 Stakes**：如果不解决这个缺口，领域会走向什么死胡同？
   > "If the discipline continues to treat A and B as interchangeable, cumulative knowledge about [phenomenon] will remain fragmented."

### Transition 适配规则

核心挑战：让过渡句从你的特定内容中自然生长出来。

**不要**：使用万能过渡句（"The next section reviews the literature"）。
**要**：使用**内容桥接句**——前一段的最后一句和后一段的第一句共享一个概念。

**桥接公式**：
```
"This [anomaly/paradox/gap] is not merely a [domain-specific curiosity]; it reflects a broader [theoretical issue] concerning [core concept]."
```

### Contribution 适配规则

核心挑战：将 Makadok 声明从模板转化为不可辩驳的对话定位。

**适配公式（以 Mechanism 为例）**：
```
"We explain why [X affects Y] by identifying [mechanism] as the mediating process that translates [antecedent] into [outcome]."
→ 填充为 →
"We explain why environmental dynamism amplifies R&D returns by identifying absorptive capacity as the mediating process that translates resource commitment into innovative output."
```

**四问映射检查**：

| Makadok 问题 | 你的论文答案 | 声明位置 |
|-------------|------------|---------|
| What does the paper examine? | [自变量] → [因变量] 在 [情境] 中的关系 | P6 首句 |
| Why can this setting answer the question? | [情境] 的 [独特特征] 使机制可见 | P6 第2-3句 |
| What does the paper show? | [机制/发现] | P7 首句 |
| What conversation should move? | [理论对话] 需要修正/扩展 | P7 末句 |

### 跨领域迁移示例

同一模块在不同领域的适配：

**模块：`06-paradigm-challenge`**

| 领域 | 共识 | 异常 | 适配结果 |
|------|------|------|---------|
| 战略管理 | 资源异质性 → 竞争优势 | 相同资源 Bundle 不同绩效 | "Conventional wisdom holds that resource heterogeneity explains competitive advantage..." |
| 组织理论 | 制度同构 → 合法性 | 同构企业不同生存率 | "Conventional wisdom holds that institutional isomorphism enhances organizational survival..." |
| 营销 | 品牌资产 → 顾客忠诚 | 高资产品牌顾客流失 | "Conventional wisdom holds that strong brand assets secure customer loyalty..." |

### 适配质量速查卡

在将模块填入你的研究时，逐条核对：

- [ ] 共识陈述有 ≥2 篇真实文献支撑，不是稻草人
- [ ] 异常证据是**你研究中的具体发现/现象**，不是泛泛而谈
- [ ] Tension 句超越了 "few studies have examined" 的表述层级
- [ ] Stakes 句回答的是 "So what?" 而不是 "What?"
- [ ] Transition 句包含前一段的关键词 + 后一段的关键词
- [ ] Contribution 句中的每个术语都在论文中有对应发现
- [ ] 没有模块直接复制自单一范文，至少经过两个维度的改写（术语替换 + 逻辑调整）
