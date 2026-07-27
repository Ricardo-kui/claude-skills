---
type: corpus
canonical_id: "prose-craft-checklist"
source: "Pollock 2025 Ch03"
created: 2026-06-01
version: 1.5.0
---

# Prose Craft Checklist（Pollock 2025 Ch03）

## 0. Paragraph Architecture（段落架构）

> 本层补充通用学术写作指南中的 paragraph-level 原则（PEEL/PEAL、paragraph length、topic sentence placement），作为 Ch03/Ch04 句法级检查的上一级检查。

### 0.0 段落体裁分型（Genre Awareness）

学术段落的"好结构"不是单一的。本节的段落规则按两种体裁分型适用：

| 体裁 | 适用 Section | 段落约定 | 代表节奏 |
|------|-------------|---------|---------|
| **说服体裁（persuasion genre）** | Introduction / Theory / Discussion | claim-first：topic sentence 段首（§0.3）；PEEL/PEAL（§0.1）；Dunleavy 六问题全部适用（§0.6） | Point → Evidence → Explanation → Link |
| **审计体裁（audit genre）** | Methods / Results | verdict-after-restatement：假设重述-first、table-first、methods-justification-first、procedure-first 均为合法段首；支持判断在假设重述之后即可（位置不限——可早可晚，见右栏两种子型） | (a) verdict-last：假设重述→证据→判决置尾；(b) verdict-early-then-interpreted：假设重述→判决前置→幅度/边际分析→解释性 wrap。样本漏斗 procedural-first（M2）；威胁-first（R7） |

**核心规则**：§0.1 PEEL/PEAL、§0.3 topic sentence placement、§0.6 Dunleavy 反模式**仅适用于说服体裁**。对 Methods/Results 段落强制执行 claim-first 是 false analogy——顶刊语料中的最佳 Results 段落（Mannor 2016, Mayo 2022, Pontikes 2012, Malik 2025）均以假设重述或表格导航开篇、判决置段中或段尾，主动违反 claim-first。审计体裁段落只适用两条通用规则：§0.2（长度）和 §0.5（coherence），外加各 slot 文件内的体裁专属 QC（write-results R1–R9、write-methods M1–M10）。

> 质性过程研究的 Findings（F1–F6）介于两种体裁之间：过程模型总览段偏说服体裁，阶段证据段偏审计体裁，按段落功能分别适用。**注意**：质性证据段的「wrap」不是假设判决（R3 Beat-4 不适用），而是可选的作者 gloss——以 informant quote 收尾合法，§0.6-5 不 flag。

---

### 0.1 PEEL / PEAL 段落结构

每个学术段落应至少包含：

| 成分 | 功能 | Introduction/Theory 中的典型对应 |
|------|------|--------------------------------|
| **P — Point（论点句）** | 段落的 controlling idea | Hook 的 puzzle、Tension 的 gap、Theory 的 why-chain claim |
| **E — Evidence（证据）** | 支撑论点的文献/数据/案例 | Literature Turn 的引用、Theory 的文献支撑、Hook 的具体 actor |
| **E — Explanation（解释）** | 说明证据为何支持论点，回答 "So what?" | Stakes 的理论/实践后果、Theory 的机制推演 |
| **L — Link（链接）** | 与下一段或研究问题的衔接 | Transitions、Contribution 的回扣、假设推导的过渡 |

**检查清单**:
- [ ] 每个段落有明确的 Point（topic sentence），且通常出现在段首或第 2 句
- [ ] Point 之后有 Evidence（引用、数据、案例），而非连续抽象推理
- [ ] Evidence 之后有 Explanation/**warrant**——点出连接证据与 claim 的机制或前提（非"支持论点"的循环重述）；构建方法见下方「Explanation/Warrant 构建指南」
- [ ] 段末或段首有 Link，明确本段与前后段的逻辑关系

**例外**: Contribution 段和 T6 Closure 段可压缩为 P + E + L，Explanation 可嵌入 Point。

**与 Dunleavy TBTW 的关系**: PEEL/PEAL 与 Dunleavy 的 Topic–Body–Tokens–Wrap 是同一说服体裁原则的两种表述——Point ≈ Topic，Evidence ≈ Tokens，Explanation ≈ Body 中的 warrant，Link + 收尾判断 ≈ Wrap。本清单以 PEEL/PEAL 为主框架；TBTW 的增量贡献是显式要求 **Wrap 句**（段末把证据上升为 claim，见 §0.6 问题 5 "Abrupt stop"）。两者不冲突，不并列使用。

#### Explanation/Warrant 构建指南（证据→claim 的桥接）

PEEL 的第二个 E（Explanation）是段落逻辑紧实度的关键。它**不是**"再说一遍证据支持论点"（那是循环），而是**点出连接证据与 claim 的底层机制或前提**——把"证据是什么"翻译成"证据为什么算数"。弱段落的标志就是跳过 warrant，从 Evidence 直接掉到 "This supports our argument"。

**四步桥接**（说服体裁 Introduction / Theory / Discussion）：
1. **陈述证据** — 引文/数据/案例的表面内容
2. **揭示隐含机制或前提** ⭐核心 — 证据为何相关？它隐含什么因果机制、什么未言明的假设？
3. **推出对 claim 的含义** — 由该机制/前提落到段落 Point（"This implies..." / "This means that..."）
4. **（可选）给边界** — 限定适用范围、承认反例、区分竞争解释

**跨体裁示例**（均锚定真实范文）：

| 段落类型 | ① Evidence（陈述） | ② Warrant（机制/前提）⭐ | ③ Implication（对 claim） |
|---------|-------------------|----------------------|------------------------|
| **Theory 机制段** | 杠杆企业削减广告与 R&D（Grullon et al. 2006） | 广告→感知/预期质量（Kirmani & Wright 1989）；感知质量是 satisfaction 的关键前因（Anderson & Fornell 2000） | ∴ 高杠杆→低广告→低感知质量→低 satisfaction（Malshe 2015 JM, H1 中介逻辑） |
| **Introduction tension 段** | 精英消费低 brow 文化已被广泛记录（Grazian 2005; Halle 1996; Bryson 1996） | distinction-seeking 只解释"为何消费广谱"，不解释"为何非低 brow 不可"；而低 brow 被标榜为 authentic 而非高品味 | ∴ 现有解释不完整——为何 high-status 偏要在低 brow 里求 authenticity 仍无理论（Hahl et al. 2017 ASR gap） |
| **Discussion 贡献段** | leverage×satisfaction 交互显著（b=−.031），floodlight 显示杠杆>95% 处 satisfaction 反转为减值 | 既有 satisfaction→value 链跨行业变异巨大且无解释（Anderson, Fornell & Mazvancheryl 2004） | ∴ firm-specific leverage 部分解释该变异，化解文献长期悬案（Malshe 2015 JM, H3 贡献） |

> Theory 机制段的 why-chain 连接词谱系见 write-theory 的 `corpus/sentences/mechanism_chain.md`；本节给出跨体裁的通用构建原则（write-theory 的 warrant 资源是其 Theory 专版实现）。

**审计体裁的 warrant 等价物**：Methods/Results 不走 PEEL warrant，其"结果→含义"桥接是**幅度/经济显著性解读**——系数→"one-SD leverage = .47 点 satisfaction = 约 $26M 净现金流"（Malshe 2015 JM）——把统计结果翻译成实质意义，由 slot-R3 Beat-3（幅度）与 slot-R5（经济显著性）管辖，不在本节。

**反模式（warrant 缺陷自检）**：
- **循环 warrant**：「该证据支持论点，因它与论点一致」——用 claim 重述冒充机制。检测：删掉 warrant 句，claim 是否仍悬空无据。
- **缺失机制**：从 Evidence 直接跳到 Point，未命名"为什么"。检测：能否在 Evidence 与 Point 间插入一句 "This is because [机制]"——插不进即缺 warrant（对应 §0.5「Read my Mind / 逻辑跳跃」）。
- **机制-证据脱钩**：所给机制不被本证据支持（证据讲 A，机制讲 B）。检测：该机制在"没有这条证据"时是否同样成立——若成立，机制与证据无关，warrant 失效。

> 本指南是 §0.5「避免逻辑跳跃」的**建设面**：§0.5 说"每个推理步骤用≥1 句话"，本节说"那句话该写什么——机制或前提"。

---

### 0.2 Paragraph Length

**健康区间**: 200–300 词（Hull LibGuides 一般建议）

**检查标准**:
- [ ] 无 < 100 词的段落（可能 evidence/explanation 不足）
- [ ] 无 > 350 词的段落（可能包含多个论点，需检查是否拆分）
- [ ] 单段 >150 词且只有 1–2 句 → 必须拆分（Sentence Stuffing 检查）

**期刊差异**:
- AMJ/ASQ: 偏好 200–300 词的充实段落
- SMJ/JM: 可接受 150–250 词的紧凑段落
- JMS/JOM: 有时使用 100–150 词的短段落，但需确保每段仍有 Point + Evidence

**来源差异说明**: Dunleavy 建议研究性文本段落 100–200 词，Hull LibGuides 建议 200–300 词。二者语境不同——Dunleavy 针对书章/学位论文（长文节奏），Hull 针对期刊文章。**期刊论文以上方期刊差异表为准**；撰写书章/学位论文时可下调至 100–200 词区间。两条规则对两种体裁（§0.0）都适用。

---

### 0.3 Topic Sentence Placement

**默认规则**: Topic sentence 放在段首，15 词内说出核心判断。

**允许延迟的两种情况**:
1. **Transition-first**: 段首 1 句专门承接前段，第 2 句给出核心判断
   - 示例: "Building on this tension, we argue that..."
2. **Background-first**: 段首 1 句提供最小必要背景，第 2 句给出核心判断
   - 示例: "In leadership settings, CEOs communicate frequently with investors. These communications..."

**禁止（仅说服体裁）**: 段首 3 句以上仍未出现 topic sentence（严重 Burying the Lead）。**适用范围：Introduction / Theory / Discussion**。Methods/Results 段落的假设重述-first（"Hypothesis 1 predicted..."）、table-first（"Table 2 reports..."）、procedure-first（"We began with..."）开头不受此限——这些是审计体裁的合法段首（见 §0.0），其"topic sentence"等效物是段尾的支持判断。

> **Key line 三分法词汇**：总起式 key line = 本节的 topic sentence；连接式 key line（承上+启下双要素句法）与总结式 key line（段末 wrap 正面语料）见 `../micro-templates/key-line-patterns.md`。"缺乏条理/没有 key line"类诊断按三分法分流修复。

---

### 0.4 Topic Sentence 的 5 种类型

| 类型 | 功能 | 在 Introduction/Theory 中的典型应用 |
|------|------|----------------------------------|
| **Statement of fact** | 用事实/统计支撑段落主旨 | Hook 中的数据冲击、Stakes 中的量化后果 |
| **Comparison / contrast** | 比较或对比多个事物/观点 | Tension 中的 "共识 vs 反例"、Theory 中的 rival mechanism 区分 |
| **Definition / explanation** | 定义或解释术语/概念 | Theory Lens 中的 interpretive frame 定义、构念辨析型 Theory 的构念界定 |
| **Cause and effect** | 解释因果/条件关系 | Mechanism Preview、Theory 的 why-chain 段落 |
| **Argument / thesis statement** | 提出段落论点 | Contribution 段、Theory 的假设推导段 |

---

### 0.5 Coherence 技术（句间连贯）

1. **重复关键词或短语**：在定义或识别重要概念时保持引用一致
2. **创建平行结构**：连续句子使用相同语法结构，帮助读者看到观点联系
3. **保持视角、时态、数的一致**：避免在 you/one、past/present、a man/they 之间跳跃
4. **使用 transition 信号词**：明确句子间逻辑关系——分类词表（递进/举例/比较/对比/因果/总结/时间，Indiana WTS）、学术偏好标注与按目的快速选择表见 `../micro-templates/transition-signals.md`；每段 1–2 个 explicit transition 足够，优先 subtle transition（关键词重复、代词回指、平行结构）。**段际衔接**（连接式 key line 的承上+启下双要素句法：转折/递进/因果/并列四型）见 `../micro-templates/key-line-patterns.md` §2

**避免逻辑跳跃**（L1 底线）：不要假设读者已经知道你在想什么（对应 **Read my Mind** 检查）；每个推理步骤用至少一句话说明。但句句相连 ≠ 论证成立——下方诊断把"逻辑紧实度"从这条 L1 底线升级为可操作的两层测试。

#### 逻辑紧实度诊断（说服体裁 Introduction / Theory / Discussion 专用）

把段落句子按序读，在**每相邻两句之间命名一个逻辑关系**，画出"关系标注链"。诊断的不是"能不能塞个连接词"（任何两句都能塞 and），而是**能否命名 fitting 的关系类型**，以及**链条是否兑现到 Point**。

**关系 taxonomy（三档）**：

| 档 | 关系 | 信号词 | 诊断意义 |
|----|------|--------|---------|
| **强**（承载推理） | 因果 / 机制 / 证据 / 兑现 | because, through this process, X found that, thus...taken together, this implies | 强关系（尤其机制/兑现）= warrant 的句际化身；出现即推理在推进 |
| 中性（必要非推进） | 对比 / 让步 / 条件 | however, although, whereas, if / when | 转折或限定，正常会有，但不能替代强关系 |
| **弱** | 列举 / 加合 | and, also, moreover, first / second / finally | 连续 ≥3 个 = 🚩清单段（局部相连、全局不推进） |

**双层测试**：
1. **局部（cohesion）**：每相邻两句能否命名一个 fitting 关系？——**显式连接词** OR **subtle transition**（关键词重复 / 代词回指 / 平行结构，见上方 4 技术）都算合法衔接；**两者皆无**处才算 🚩gap（逻辑跳跃，对应 Read my Mind）。*此条修复"强制显式连接词"与 §0.5 偏好 subtle transition 的矛盾。*
2. **全局（cash-out）**：链条是否含强关系、且末端经 warrant 兑现到段首 Point（§0.1）？句句相连但**零强关系 / 末端不兑现** = 🚩清单非论证（raw"补连接词"测试漏掉的深层缺口）。

**输出：关系标注链 + 三红旗**

```
[S1 Point] —机制→ [S2] —证据→ [S3] —兑现→ [S4 回扣 Point]   ← 健康
[S1] —列举→ [S2] —列举→ [S3] —列举→ [S4]                    ← 🚩清单
[S1] —机制→ [S2]  🚩gap  [S3] —兑现→ [S4]                    ← 🚩gap（S2→S3 无可命名关系）
[S1 Point] —证据→ [S2] —证据→ [S3]                            ← 🚩缺 warrant（无强关系兑现，Point 悬空）
```

- **🚩gap**：某对无可命名关系（逻辑跳跃）
- **🚩清单**：连续 ≥3 弱关系（局部相连、全局不推进）
- **🚩缺 warrant**：链条无强关系 / 末端不兑现 Point（= §0.6-5 abrupt stop 的深层版）

**实例对照**（同框架下分得开）：
- ✅ **Malshe 2015（杠杆→广告/R&D 段）**：`[Point:高杠杆→低广告/R&D] —机制→ [可自由支配] —证据→(Cohen/Graham) —机制→ [无形资产·回报不可测] —兑现→ "Thus, taken together..."` —— 关系多样、含多强关系、末端兑现 Point。
- 🚩 **清单段**：`[Point:杠杆影响企业] —列举→ [增风险] —列举→ [降灵活] —列举→ [美国普遍]` —— 4 连弱关系、零强关系、末端停事实、Point 悬空 → 🚩清单 + 🚩缺 warrant。

> **与 §0.1 配对**：§0.1「warrant 构建指南」教**怎么搭**推理桥（建设面）；本节教**怎么诊断**桥在不在、紧不紧（诊断面）。两者都仅说服体裁。审计体裁（Methods/Results）紧实度由 slot QC（四拍 / 漏斗 / construct-first）管辖，不走本诊断。

---

### 0.6 Dunleavy 六段落问题（说服体裁专用）

> 来源：Dunleavy（LSE Writing for Research / *Authoring a PhD*），规范性强于实证性——目前无语料库频率数据支撑各问题的发生率，也无段落结构与审稿人评价因果关系的证据。六个问题**全部仅适用于说服体裁**（§0.0）；Methods/Results 段落遵循 verdict-last 约定，问题 1–4 不适用，问题 5–6 的通用部分见标注。

> **关于 backward-link opening（回指既有研究的开头）**：Dunleavy 原六问题含此项，本清单**有意不收录**——回指既有研究 / 奠基性工作的开头（"Classic treatments depict..." / "Much of what we know comes from the seminal work of Goffman..."）在经验引言的 gap-establishing 弧线与 Theory 的 seminal-work 致敬中是标准且好的写法。实证依据：Malshe & Agarwal (2015, JM)、Hahl et al. (2017, ASR)、Lashley & Pollock (2020, ASQ) 的引言 / Theory 首段均为 backward-link 式，顶刊照发。**不 flag。**

1. **Author-name opening（作者名开头）**：段首句主语是他人姓名（"Smith (2020) argued that..."），段落沦为文献注脚而非自己的论证。
   - 检测：段首句主语为人名 + 年份。
   - 修复：作者名移到句中证据位（"We argue that X (cf. Smith, 2020)."），段首换成自己的 claim。
   - **范围**：仅 Introduction / Theory / Discussion。Results 的 "Hypothesis 1 predicted..." 是假设重述，不是本问题；Methods 的 "Following Smith (2020), we measure..." 见 slot-M3 的 construct-first QC。
   - **豁免**：单篇/理论家开头但段中**出现**作者自己的 claim（不必在段末）不算违规——理论段常链式（理论家开头→段中作者 claim→段末进一步引文，如 Pollock et al. 2015 ASQ 的 Gould 段）。仅当整段无作者自己 claim、纯文献注脚才算。

2. **Throat-clearing（清嗓开头）**：段首 1–2 句是功能性热身（"Before turning to X, it is important to note..." / "It is worth mentioning..."），推迟正事。
   - 与既有规则的关系：§5.2 已覆盖"元评论段首"（"本节讨论..."）；本类补充其余热身形式（背景铺垫式、客套式），两者检测方法相同、命名互补。
   - 修复：删除或压缩为 ≤15 词的 §0.3 合法 transition/background 句。

3. **Orphaned quote（孤儿引语）**：引语独立存在，前无 framing（"As X shows:"）、后无 interpretation（"This means..."），引语替作者说话。
   - 修复：每个引语前加 1 句 claim、后加 1 句解读；epigraph 型 Hook 必须接 pivot 句。
   - **范围**：persuasion genre 的 Hook / Theory 为主；量化 Results/Methods 几乎不用引语。**质性归纳研究的 Findings 大量使用 informant quote 作为数据展示**（非理论引语），framing 规则不同（setup 句 + quote + 作者解读为标准，quote 收尾亦合法）——见 §0.0 混合体裁条款。

4. **Caveat-first（限定先行）**：段首以让步开头（"Although prior work..." / "While X is well established..."），核心 claim 推迟到段中，削弱说服力。
   - 与 §0.3 的关系：caveat-first 不是合法的 transition-first/background-first——合法延迟句必须中性承接，caveat 句预先削弱了自己的 claim。
   - 修复：claim 前置，caveat 移到 claim 之后（"We argue X. Although Y, ..."）。
   - **范围**：仅当让步句把核心 claim 推迟到后续段落或埋过段中点才算违规；同段内 "To be sure X... However Y" 是合法辩证，不 flag。

5. **Abrupt stop（戛然而止 / 无 wrap）**：段末句是证据、引用或数据，无 wrap 句把证据上升为 claim（缺 "This suggests that..." / "Taken together..."）。
   - 检测：段末句含 citation/数字且无作者自己的判断句。
   - 修复：段末加 1 句 wrap，回扣段落 Point（PEEL 的 L）。
   - **范围**：说服体裁全适用。审计体裁的等效物是段尾支持判断（"Thus, Hypothesis 1 is supported"）——R3 四拍的 Beat-4 即 audit-genre 的 wrap，由 slot-R3 QC 覆盖，此处不重复。**例外（质性归纳 Findings 证据段）**：以 informant quote / field-data excerpt 收尾是体裁约定（data-as-evidence，让数据发声），非 abrupt stop；可选附 1 句作者 gloss，但不强制 wrap。此类段由 §0.0 混合体裁管辖，不由本条 flag。**另两类豁免（说服体裁）**：(1) **成框示意证据**——段中已陈述 claim、段末以 framed 引语/数据兑现（非孤立引语）合法（如 Pollock et al. 2015 ASQ 以 Washington & Zajac 引语收尾兑现 claim）；(2) **证据枚举链**——mixed-evidence / supporting-facts 枚举段以引文收尾、wrap 由邻段承接合法（如 Zhou et al. 2017 ASQ 的 mixed-evidence 段）。

6. **Too long / Too short**：统一见 §0.2（含 Dunleavy 100–200 与 Hull 200–300 的来源差异说明）。长度规则对两种体裁都适用，不重复列检测标准。

---

## 1. Human Face（人文面孔）

### 定义
在抽象论证中加入具体行动者（人名、公司名、场景、引语），让读者感到研究触及真实世界。

### 检查清单
- [ ] Introduction Hook 中 >=1 个具体 actor（人名、公司名、机构名）
- [ ] 全文 >=3 个具体 actor（跨 Hook、Theory、Results）
- [ ] 每个 actor 都直接映射到核心构念（不是装饰性案例）

### 五种技术（Pollock Ch03）
1. **直接经验/轶事**：作者自己的经历或观察
2. **他人叙述**：访谈引语、回忆录、第一手账户
3. **第三方描述**：新闻报道、传记中的描述
4. **虚构场景**：明确标注为假设性场景（"Imagine a manager who..."）
5. **修辞问题**：让读者代入自己的经验（"Have you ever..."）

### 嵌入点矩阵

| 段落 | Human Face 要求 | 推荐技术 | 反模式 |
|------|----------------|---------|--------|
| P1 Hook | 必须有 >=1 具体 actor | 技术2（他人叙述）或技术3（第三方描述） | 用 "many firms" 代替 "Toyota" |
| P3 Gap | 优先用具体案例支撑反例 | 技术3（第三方描述） | 用 "some studies found" 代替具体数字 |
| P5-P6 Theory Lens | 可用 1 句场景说明机制 | 技术4（虚构场景） | 纯理论推演无落地 |
| P7-P8 Contribution | **不引入新 actor** | — | Contribution 不应引入新案例 |

### 与 Hook 类型的关系
- `10-immersive-narrative`：天然 Human Face（已有具体人名）
- `02-epigraph-quote-pivot`：引语中的具体案例即 Human Face
- `03-data-shock`：需在数据后追加 1 个具体案例作为 Human Face 补充
- `06-paradigm-challenge`：反例中必须包含具体公司/人名

---

## 2. Showing vs Telling（展示而非告知）

### 定义
每个抽象主张必须配对至少一个具体例子、比喻、类比或场景。抽象解释（telling）与具体例证（showing）的比例不超过 2:1。

### 检查清单
- [ ] 每个 major construct 首次出现时，有 concrete illustration
- [ ] 每个核心发现方向，有具体场景说明"这意味着什么"
- [ ] 不允许连续 2 句纯抽象链条无例子

### Telling → Showing 转换表

| Telling（抽象） | Showing（具体） |
|----------------|----------------|
| "Digital transformation enhances innovation." | "When Siemens digitized its turbine production, engineers could test designs in simulation—cutting development time from 18 months to 6." |
| "Product recalls damage firm reputation." | "After Toyota's 2009 floor-mat recall, J.D. Power's quality score for the brand dropped 12 points within a quarter." |
| "CEO overconfidence leads to risky decisions." | "Elizabeth Holmes at Theranos raised $700 million while refusing board oversight—a pattern consistent with overconfident CEOs who dismiss contradictory data." |

### 嵌入点矩阵

| 槽位 | Showing 要求 | Telling 陷阱 |
|------|-------------|-------------|
| `[anomaly / counter-evidence]` | 必须展示具体事实/数字/案例 | "Some scholars argue..." |
| `[quantification]` | 精确数字 + 来源 + 年份 | "Millions of dollars" |
| `[mechanism / condition]` | 用可操作化构念 + 1 个场景 | "The role of X"（模糊） |
| `[theoretical consequence]` | 具体到某理论的某预测失效 | "This limits our understanding"（空话） |

---

## 3. Conversational Voice（对话式声音）

### 定义
通过 accountable first-person（"We argue"）、直接读者称呼（"Consider"）、轻量旁白，缩短作者-读者距离。

### 检查清单
- [ ] 无 "It is argued that" → 改用 "We argue that"
- [ ] 无 "It is shown that" → 改用 "We show that"
- [ ] 无 "It is hypothesized that" → 改用 "We hypothesize that"
- [ ] 无 inflated symbolism（"paradigm shift", "fundamentally transforms"）
- [ ] 无 vague attribution（"Prior research has shown..." 不说明谁）
- [ ] 被动语态 <=20%（Contribution 和 Theory Lens 段优先检查）
- [ ] Read-aloud test：大声朗读 Hook 和 Contribution，是否自然？

### 禁用词表（与 ACADEMIC_COMMUNICATION.md 对齐）

| 禁用 | 替换 | 检查位置 |
|------|------|---------|
| "It is argued that" | "We argue that" | Gap, Theory Lens, Contribution |
| "It is shown that" | "We show that" | Preview, Contribution |
| "It is hypothesized that" | "We hypothesize that" | Theory |
| "Prior research has shown..." | "[Author] ([year]) showed that..." | Lit Turn, Gap |
| "paradigm shift" | "challenge" / "refine" | Contribution |
| "fundamentally transforms" | "extends" / "clarifies" | Contribution |
| "The literature suggests that" | "[Author] ([year]) argued that..." / "We argue that..." | Lit Turn, Theory |
| "By examining..."（-ing 开头） | 直接写研究问题 | Hook, Preview |
| "值得注意的是" | 直接写内容 | 中文讨论 |

### Read-aloud Test 协议
1. 大声朗读 P1 Hook — 是否像有人在讲故事？
2. 大声朗读 P7-P8 Contribution — 是否像研究者在解释自己的判断？
3. 大声朗读 T6 Closure — 是否像总结而非重复？
4. 如果任何一句读起来像"报告"而非"对话" → 标记为需要 voice 修订

---

## 4. Motion and Pacing（动作与节奏）

### 定义
平衡推进论证的主动作（stroke）与帮助读者吸收的评论（glide）。Pollock Ch03 用"划桨与滑行"比喻：stroke 创造 motion，glide 创造 pacing。

### Stroke vs Glide 判定

| 类型 | 功能 | 典型内容 | 风险 |
|------|------|---------|------|
| **Stroke** | 推进论证 | 因果推理、假设推导、机制展开 | 全 stroke → "forced march" |
| **Glide** | 帮助吸收 | 文献总结、定义澄清、边界说明 | 全 glide → "ponderous pace" |

### 段落级比例要求

| 段落类型 | Stroke | Glide | 检查问题 |
|---------|--------|-------|---------|
| 机制推演 | 70% | 30% | 每个 stroke 句子后是否有 illustration？ |
| 文献铺垫 | 40% | 60% | glide 是否用具体场景解释，非纯引用罗列？ |
| 构念定义 | 50% | 50% | 定义后是否立即给 1 个例子？ |
| Hook | 80% | 20% | 是否有具体 actor 推进？ |
| Contribution | 60% | 40% | 是否先 claim 后 justify？ |

### 检测 "forced march"
- 连续 3+ 句都是 stroke（因果推理/假设推导）且无 glide（解释/例证）
- 修复：在关键推理步骤后插入 1 句 glide（"That is," / "For example,"）

### 检测 "ponderous pace"
- 连续 3+ 句都是 glide（文献总结/定义澄清）且无 stroke（推进）
- 修复：删除重复解释，将 glide 压缩为 1 句，然后推进到下一步推理

---

## 5. Ch04 五个病理（Pollock 2025 Ch04）

本层在 Ch03 Prose Craft（怎么讲）之上，增加**结构级病理诊断**（什么不该讲、什么不该这样讲）。五个病理与 Ch03 工具的关系：Ch03 提供正面规范，Ch04 提供负面排错。

---

### 5.1 Fat suit（臃肿铺垫）

**定义**：文章开头塞了过多背景信息，读者迟迟看不到核心问题， central knot 被淹没在铺垫中。

**检测标准（满足任一即标记）**：
- P1 Hook 词数 > 120（英文）/ > 180 字（中文）
- 前 3 段总词数 > 350（英文）/ > 500 字（中文）
- 前 3 段中纯背景信息（历史、定义、共识描述）占比 > 60%，问题/张力/悖论占比 < 40%

**修复策略**：
- 将背景压缩到 Lit Turn 段，P1 只保留理解 paradox 所需的最小上下文
- 采用"倒金字塔"结构：核心问题在 P1 前 3 句出现，背景在后
- 检测方法：删除 P1 前 3 句后的所有内容，读者是否仍能理解"问题是什么"？如果不能，说明铺垫不足；如果可以，说明铺垫可能过度

**嵌入点**：write-introduction 的 Hook 槽位和 Lit Turn 槽位；write-theory 的 P1 构念定义段

---

### 5.2 Burying the lead（埋没导语）

**定义**：段落的核心信息被埋在中间或末尾，而非段首句。读者必须读到段中或段尾才能知道段落目的。

**检测标准（满足任一即标记）**：
- 段首句未在 15 词内说出核心判断、发现或 claim
- 段首句是元评论（"本节讨论..." / "接下来我们..."）或纯过渡句，无实质信息
- 读者只读段首句时，无法判断该段支持/反对/修正什么观点
- **新增**：topic sentence 出现在第 3 句或更后（允许第 2 句出现，但第 1 句必须是明确 transition/background）

**修复策略**：
- 重写段首句为"核心判断句"：主语 + 主动动词 + 方向/发现
- 模板："We argue that [X] [verbs] [Y] because [机制]." / "[Actor] faces a tension: [具体矛盾]."
- 元评论和过渡信息移到段尾或删除
- 检查：将段首句单独提取，是否仍是一个完整且有力的学术判断？
- **新增**：如确实需要 transition-first 结构，确保第 1 句 ≤15 词且第 2 句立即给出核心判断

**嵌入点**：write-introduction 所有段落；write-theory 的 Topic Sentence（四段式论证链）和 T6 Closure

---

### 5.3 Sentence stuffing（句子 stuffing）

**定义**：一个句子塞入过多从句、括号、修饰语，导致读者 parsing 困难。本质是作者想在一句话里说太多。

**检测标准（满足任一即标记）**：
- 单句词数 > 30（英文）/ > 50 字（中文）
- 单句包含 > 2 个从属连词（which/that/because/although/while/whereas）
- 单段 > 150 词且只有 1-2 个句子
- 一句话中包含 > 1 组括号或破折号插入语

**修复策略**：
- 拆分为 2-3 个短句，每句一个核心判断
- 模板：长句 → [核心句]. [修饰/例证句]. [后果句].
- 将括号内容移到独立句子或删除
- 优先删除：非限制性定语从句（, which...）→ 常可独立成句

**嵌入点**：write-introduction 的 Stakes 和 Contribution 段（易 stuffing）；write-theory 的假设推导段和 T6 Closure

---

### 5.4 Read my mind（读心术）

**定义**：作者假设读者已经知道自己在想什么，缺少过渡和解释，造成逻辑跳跃。读者被迫"脑补"中间步骤。

**检测标准（满足任一即标记）**：
- 段落间无 explicit transition（缺少 "However"/"Consequently"/"This leads to"/"Thus" 等信号词）
- 因果推理中从 A 直接跳到 C，缺少 B 的中间步骤（如从"CEO 自恋"直接到"召回延迟"，跳过"信息过滤→风险低估"）
- 使用暗示读者已知的表述："显然" / "不难看出" / "as is well known" / " needless to say"
- 新构念首次出现时无定义或上下文，直接用于推理

**修复策略**：
- 每段段首添加 transition 信号词，明确本段与前段的关系（转折/因果/递进/对比）
- why chain 中每个因果步骤用至少 1 句话说明；检查：相邻两个 claim 之间是否可插入"因为...所以..."？
- 删除所有"显然"类表述，替换为具体推理
- 新构念首次出现必须伴随定义或指向前文定义

**嵌入点**：write-introduction 的 Gap→Stakes→Theory Lens 过渡；write-theory 的 why chain 和假设推导段

---

### 5.5 Pompous prose（浮夸文风）

**定义**：使用不必要的复杂词汇、拉丁化表达、过度正式化，掩盖思想的清晰性。与 Inflated symbolism（Ch03）的区别：后者是"过度包装贡献"，前者是"过度包装日常表达"。

**检测标准（满足任一即标记）**：
- Nominalization（动词/形容词名词化）："the transformation of"（名词）而非 "transforms"（动词）；"the applicability of" 而非 "applies"
- 不必要的 jargon："utilize"（用 use）、"leverage"（用 use）、"facilitate"（用 help/enable）、"ameliorate"（用 improve）
- 过度正式化短语："in the event that"（用 if）、"due to the fact that"（用 because）、"for the purpose of"（用 to）
- 拉丁化复杂词："commence"（用 start）、"terminate"（用 end）、"pursuant to"（用 under）

**修复策略**：
- 降级词表：将检测到的复杂词替换为简单直接词（见下表）
- 检查每个 nominalization：能否改回动词形式并仍保持语法正确？
- Read-aloud test：大声朗读，如果读起来像法律文件或政府公文而非学术对话 → 降级

**降级词表（常见学术 nominalization / 浮夸表达 → 直接表达）**：

| 浮夸表达 | 直接表达 | 检查位置 |
|---------|---------|---------|
| "conduct an analysis of" | "analyze" | Methods, Results |
| "provide a description of" | "describe" | Theory, Methods |
| "make an assumption" | "assume" | Theory |
| "have an impact on" | "affect" | Results |
| "give rise to" | "cause" / "produce" | Theory |
| "is indicative of" | "indicates" | Results |
| "in the context of" | "in" / "for" | 全文 |
| "with respect to" | "about" / "for" | 全文 |

**嵌入点**：write-introduction 的 Contribution 和 Preview；write-theory 的所有段落（尤其是构念定义和假设推导）

**注意**：本病理与 Ch03 Conversational Voice（禁用 "It is argued that"）和 Inflated symbolism（禁用 "paradigm shift"）互补。Ch03 覆盖声音和修辞包装，Ch04 覆盖句法复杂度和词汇选择。

### 5.6 Overclaiming（绝对化断言，Booth Ch6）

**定义**：claim 的确定性超出论证所能支撑。与 Pompous prose（词汇浮夸）和 Inflated symbolism（贡献包装）互补——本病理是**确定性校准**失灵。Booth §6.3："nothing damages your ethos more than arrogant certainty."

**绝对化词黑名单**（Booth §6.3.2：多数领域读者不信任 pat certainty）：
`all` / `no one` / `every` / `always` / `never`（及中文对应"所有/任何/从不/总是"）
- 检测：全文搜索这些词，逐处问"论证真的支撑全称断言吗？"
- 例外：样本边界描述（"All firms in our sample..."）与定义句合法——黑名单针对的是**经验规律与机制断言**

**Hedge 词库**（Watson & Crick 宣布 DNA 双螺旋时仍 hedge——Booth §6.3.2 逐字对照）：
- 谨慎版： "We **wish to suggest** a structure..."（not "state"）/ "**In our opinion**, this structure is unsatisfactory..." / "We **believe** that..." / "**Some** of the van der Waals distances **appear** to be too small."
- 攻击版（缺 hedge，更简洁但更 aggressive）："We **announce** here **the** structure..." / "Their structure **is** unsatisfactory" / "Their van der Waals distances **are** too small."

**限定条件句式**（Booth §6.3.1）：
- "..., **assuming today's conservation measures remain in place**."
- "**Based on available economic data**, a global recession appears unlikely."
- "**According to current climate models**, ..."
- 纪律：只提读者可能想到的限定条件（科学家不声明仪器精度——所有测量都依赖它，提了反而外行）

**平衡警告**：hedge 过度 = timid（"if you hedge too much, you will seem timid"）；各领域 hedge 密度不同，**观察本领域专家怎么 hedge 并照做**。管理实证惯例：假设句本身不 hedge（"We hypothesize that X is positively related to Y"），hedge 放在 mechanism 推理句、结果外推句与 Discussion 的 generalizability 声明。

**嵌入点**：write-theory 推导段 mechanism 句（与 soundness 层 warrant 五测试之 "sufficiently limited" 联动——过不了该测试的 warrant 往往就是含绝对化词的 warrant）；write-introduction Contribution 句；phase-4 审计 1 Inflated symbolism 行联动。

---

## 6. 清晰文风的 Williams 原则（Booth Ch15）

**来源**：Booth et al. 2024 Ch15（Williams 清晰风格理论的教材化）。与 §5.5 的分工：§5.5 是**词级**黑名单（逐词降级表）；本节是**句级**诊断——一句话为什么读起来 dense，以及怎么改。验证状态：句法原则通用（EMERGING，非管理学语料）。

**使用时机**（Booth §15.2.1 + Quick Tip）：不用于起草——"don't try to apply these principles as you write new sentences... let them guide you when you revise"；先写后改；时间不够时从**最难解释的段落**入手（那里句子最难）；大声朗读，你磕绊处读者也磕绊（与 §3 Read-aloud Test 联动）。

### 6.1 Character-Action 原则（前 6–7 词诊断）

清晰句两原则：①主语命名故事的**具体角色**（short, specific, concrete）；②关键动作用**动词**表达。

**诊断三步**（每分句，主从句都算）：
1. 高亮每分句前 6–7 词（跳过 "At first" 类短引导语）：是否已到达 simple subject？
2. 该主语是具体角色还是抽象名词？
3. 动词是具体动作（strip / damage）还是模糊动词（result / made）？任一失败 → 改。

**改写示范**（Booth §15.2 逐字三组）：
- ❌ "The reason for Locke's frequent repetition lies in his distrust of the accuracy of the naming power of words."
  ✅ "Locke frequently repeated himself because he did not trust the power of words to name things accurately."
- ❌ "The stripping of rain forests in the service of short-term economic interests could result in damage to the earth's biosphere."
  ✅ "If rain forests are stripped to serve short-term economic interests, the earth's biosphere may be damaged."
- ❌ "The hospitalization of patients without appropriate treatment results in the unreliable measurement of outcomes."
  ✅ "We cannot measure outcomes reliably when patients are hospitalized but not treated appropriately."

### 6.2 Nominalization 修复三步

名词化（-tion / -ment / -ence / -ity / -ness）的三重代价：①堆冠词介词（standardize→the standardization of）；②逼出模糊动词（made / result）；③把角色降格为修饰语（we→our，patients→of patient response）。

**修复三步**（Booth §15.2.4）：
1. 找角色：这句话讲谁的故事？找不到就发明一个（通常是 we，或核心构念作角色）
2. 找动作：动作若藏在名词里，改回动词
3. 重铸：用 "If X, then Y" / "X because Y" / "Although X, Y" / "When X, then Y" 重造分句

**豁免**：并非所有抽象名词都改——§5.5 降级词表管逐词处理；本节只处理**作主语且挤占角色位**的名词化。回指前句动词的抽象名词（如 "Locke's distrust" 回指前句 "distrusted"）是合法的旧信息压缩（Booth §15.3 点评）。

### 6.3 Old-before-New 信息流（第三原则，优先级最高）

读者跟得上故事的条件：句首 6–7 词是**旧信息**（已提及的角色/概念），新而复杂的信息放句末。

**诊断**：高亮每句前 6–7 词——读者能从中预测本句与上句的关系吗？不能 → 改。

**优先级规则**：当"角色作主语"与"旧信息置前"冲突时，**永远选 old before new**（Booth §15.3 原文 "always choose the principle of old before new"）。这是本清单唯一的优先级仲裁条款。

**Complexity Last（句末 5–6 词诊断）**：句末是自然强调位，应放：①首次出现的技术术语；②长而复杂的信息单元；③下文要展开的概念（段落首句的末尾词应在后文重复出现）。与 §0.5 coherence 联动：句末新信息 = 下一句句首旧信息，构成信息流链条。

### 6.4 被动语态豁免（对 active-voice 纪律的细化）

不机械回避被动——Booth §15.4："Followed mechanically, that advice will make your sentences *less* clear." 正确的问题不是"主动还是被动"，而是"句首是否是旧信息/主角"。

**该用被动的场合**：
- 被动能把旧信息提前、复杂信息置后时："these rain forests are now threatened with destruction by the increasing demand..." 优于 "the increasing demand ... now threatens these forests"（前者句首接上句旧角色）
- 描述**任何人都能重复的过程**（Methods 测量程序："Eye movements were measured at tenth-of-second intervals."——被动暗含可重复性）

**该用主动的场合**：
- 只有作者能做的动作：修辞动作（suggest / conclude / argue / show）与记功动作（design / solve / prove）——"We conclude that..." 在科学写作中不仅常见而且恰当（Booth §15.4）
- 这解释了论文的声音分布：Introduction/Discussion 用 we+主动，Methods 过程描述用被动——**不是不一致，是故事主角的合法切换**

**与既有纪律的关系**：§3 禁 "It is argued that"、phase-4 审计 1 禁 "It is hypothesized that"——禁的是**无主语逃避作者责任**，不是被动本身。被动+明确主语（"These forests are threatened"）完全合法。

---

## 跨 Skill 引用规则

- `write-introduction`（Constraints）和 `write-theory`（Phase 1.4 + Phase 3.2 QC）引用本文件全量 §0–§6——两者均为说服体裁
- `discussion-review` 可引用 §0.0/§0.1/§0.3/§0.6 审查用户已有 Discussion，经 `references/alignment-checks.md` 的 Paragraph Craft 节转引
- `write-results` / `write-methods` 仅引用 §0.0（体裁分型）、§0.2（长度）、§0.5（coherence）；§0.1/§0.3/§0.6 的说服体裁规则**不适用**于其审计体裁段落；体裁专属段落 QC 在各 slot 文件内
- `ACADEMIC_COMMUNICATION.md` 的 base voice 规则不重复，只交叉引用
- `humanizer` skill 作为下游工具引用，不嵌入其 29 条 pattern
