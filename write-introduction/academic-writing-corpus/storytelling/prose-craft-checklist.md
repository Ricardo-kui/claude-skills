---
type: corpus
canonical_id: "prose-craft-checklist"
source: "Pollock 2025 Ch03"
created: 2026-06-01
version: 1.0.0
---

# Prose Craft Checklist（Pollock 2025 Ch03）

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

**修复策略**：
- 重写段首句为"核心判断句"：主语 + 主动动词 + 方向/发现
- 模板："We argue that [X] [verbs] [Y] because [机制]." / "[Actor] faces a tension: [具体矛盾]."
- 元评论和过渡信息移到段尾或删除
- 检查：将段首句单独提取，是否仍是一个完整且有力的学术判断？

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

---

## 跨 Skill 引用规则

- `write-introduction` 和 `write-theory` 都引用本文件
- `ACADEMIC_COMMUNICATION.md` 的 base voice 规则不重复，只交叉引用
- `humanizer` skill 作为下游工具引用，不嵌入其 29 条 pattern
