# Prose Pathology — Pollock 2025 Ch04 句子级工艺完整参考

> **何时加载**：`pollock-qc` 执行 `--section=prose` 或 `all` 时，本文件提供 Pollock Ch04 五病、active writing、sound & cadence、25 条 dos/don'ts 的完整诊断细则。SKILL.md 的 prose 检查表只保留病名 + 一句话诊断信号 + 指向本文件的指针；本文件承载全部原文依据、错例→正例、修复动作。
> **来源**：Pollock, T. G. (2025). *How to Use Storytelling in Your Academic Writing*. Ch04.（line-level 工艺章节）

---

## 区块一：五种学术写作病理（The Five Pathologies）

Pollock 指出学术写作 clutter 的根因是"恐惧、傲慢、想炫耀"（King 2000; Sword 2012; Zinsser 2006）以及"长期浸泡在 cluttered prose 中导致的 cognitive entrenchment"。五病是清晰写作的反面——清晰 = concise / direct / active / vivid / 易懂。

### 病理 1：Fat Suit（胖子西装）

**定义**：把本来锋利的句子塞进冗余词的"脂肪套装"，使轮廓变钝。对应 Strunk & White "Rule 17: Omit Needless Words"。

**诊断信号**（命中任一即标记 △/✗）：
- "In order to"（应为 "To"）、"the reason for that is"（应为 "because"）、"extant"（research 不存在就不能 suggest，"extant" 冗余）
- 堆积的介词短语（of / in / for / to / with）——Hale 测试：把词放 "the log" 前，通顺即介词；介词短语常可删或替换为单个形容词/副词
- 冗余的 clarification（"or" / "that is" / "in other words" 后跟第二个定义）——除非澄清技术 jargon，否则该用第一个定义的词
- 否定冗余："He did not disagree"（应为 "He agreed"）、"We cannot disconfirm the null hypothesis due to a lack of empirical support"（应为 "The results fail to support the hypothesis"）

**Pollock 原文示例**（经济学句，41→14 词）：
- ✗ "Control of agency problems in the decision process is important when the decision managers who initiate and implement important decisions are not the major residual claimants and therefore do not bear a major share of the wealth effects of their decisions."（41 词）
- ✓ "Controlling agency problems is important when outcomes create no financial consequences for decision makers."（14 词）

**修复动作**：逐句删除不改变 claim/evidence/reader understanding 的词。不是所有句子都要短——长复合句可以，但每个词必须服务目的。

---

### 病理 2：Burying the Lead（埋没主旨）

**定义**：主语或核心 claim 被冗长的开场从句（Evans 称 "predatory clauses"）埋没。学术写作中常表现为"先论证结论，再给出结论本身"。

**诊断信号**：
- 句首长从句（资格限定、附加事实列表）延迟主语出场
- 读者读到 50+ 词还不知道本句主旨
- 段首句不是"主语 + 主动动词"，而是长铺垫

**Pollock 原文示例**（社会学问句，65→21 词）：
- ✗ "These ideas are familiar from observations of premodern cultures (e.g., Durkheim 1915; Douglas 1966; Berger and Luckman 1966) and are responsible for the image of stasis that we frequently ascribe to such societies. It is thus interesting to note that the idea that actors are constrained by accepted models represents an important but underrecognized thread that runs through much thinking on modern organizations and markets."（65 词，主旨埋到第 54 词）
- ✓ "Underrecognized is that the barriers to change created by adherence to accepted mental models exist equally in modern and premodern societies."（21 词，主旨回到句首）

**修复动作**：把核心 claim/actor/causal action 放到句首，再追加 qualification。Evans（2017:52）："It's alright to set up the main clause with a concise introductory subordinate element...but you don't want to ramble on to the point that the reader loses interest, or doesn't notice, when you finally get to the sentence's subject."

---

### 病理 3：Sentence Stuffing（句子塞馅）

**定义**：把多个独立观点、aside、解释塞进一个句子，通常用逗号/括号/破折号隔开。

**诊断信号**：
- 一个句子含多个 "and" / "further" / "in addition to" / "as well as"
- 句子超 ~40 词且承载 2+ 独立观点
- 长 parenthetical aside 嵌在句中

**Pollock 原文示例**（Taylor 1916 句，78→38 词）：
- ✗ "In the same way maximum prosperity for each employee means not only higher wages than are usually received by men of his class, but, of more importance still, it also means the development of each man to his state of maximum efficiency, so that he may be able to do, generally speaking, the highest grade of work for which his natural abilities fit him, and it further means giving him, when possible, this class of work to do."（78 词，塞了 maximum prosperity + maximum efficiency 两个观点）
- ✓ "Maximum prosperity means paying men higher than average wages for the highest grade of work they are best suited to perform. It also requires developing their natural abilities to their maximum efficiency by regularly assigning them such work."（两句 38 词）

**修复动作**：一念一句（de-stuff by breaking up）。aside 不总是坏的——关键看 (1) 是否相关 (2) 是否推进句意 (3) 是否简短。相关但长 / 简短但不推进 → 移脚注。Pollock 不同意"脚注越少越好"——不推进主旨的必要信息（额外模型结果同、替代测量未显著）放脚注反而保护正文 motion。

---

### 病理 4：Read My Mind（读我心）

**定义**：作者省略了读者只能靠读心术才能获得的关键信息。**这是 fat suit 的反面**——不是词太多，而是（对的）词太少。它同时破坏 human face（缺示例）和 motion（节奏太快太突兀），让论文像讲座而非对话。

**诊断信号**（Ragins 2012 + Pollock 补充）：
- 陌生 jargon 未定义 / 缩写未展开
- 欠发展的概念（poorly elaborated）
- **未言明的潜在假设**（unarticulated assumptions）
- **缺失 connective tissue**——读者看不到从 A 到 B 到 C 的推理桥
- 测量理由缺失（key constructs 如何测、为何纳入特定 controls）
- 样本/informant 识别方式缺失（how and why）
- 图表指引缺失（what particular tables/figures illustrate）
- 甚至"为什么这个研究重要"未说清

**根因**：作者离自己的工作太近（Ragins 2012），connections 都在脑子里没落到纸上。Johanson（2007）：多数 review 失败源于没理解 reviewer 的 sensemaking 过程——作者应做 "sensegiving"（Gioia & Chittipeddi 1991），主动提供让 reviewer 按你意图解读的信息。

**修复动作**：补缺失信息——定义、过渡、示例、测量细节、图表指引、研究重要性论证。把论文最难写的部分（你自己曾最难理解的地方）当作 read-my-mind 嫌疑犯。**发展技巧：多 review 别人的稿子**，把 reviewer 的眼睛转向自己的写作（见 Pollock Ch13 写 developmental reviews）。

---

### 病理 5：Pompous Prose（华丽散文）

**定义**：用 jargon、抽象词、炫耀性词汇装"学术"。Crozier 的法国烟厂研究揭示：技术 jargon 如同被"意外"销毁的维修手册——圈内人借它垄断权力、排斥圈外人。

**诊断信号**：
- 有等价常用词时仍用 jargon / 长 complex 词
- "to wit" / "inter alia" / "obviously" / "as everyone knows" / "of course" / "merely"（presumptuous）
- 晦涩引用（"Like the Emperor Huang Ti..."）/ insider 引用（"As everyone who attended EGOS last year knows..."）——让读者感到低地位
- 外文引语（除非受众懂该语言，或该词是公认的构念标签如 Guanxi）

**证据**：Oppenheimer（2006）研究发现——简单写作更易处理、增强理解；尽管大词汇量与更高智力相关，但**从读者视角，用更复杂的语言会让作者显得更不聪明**。

**修复动作**：有等价常用词时限 jargon；能用短词就不用长词；删除 presumptuous 与 insider 信号；外文只用英文翻译。**示例**：reviewer 写 "Julius Caesar claimed, 'Julius Caser Malo hic esse primus quam Romae secundus.'"——即使附了翻译（countryside first better than Rome second），拉丁原文仍制造了"展示智力优越"的印象，直接用英文更不居高临下。

---

## 区块二：Active Writing（主动写作）

被动语态是学术写作最大的痼疾。但**不是所有被动都坏**——关键是 agency 是否重要。

### 主动 vs 被动的识别

| | 主动 | 被动 |
|---|---|---|
| 结构 | 主语 + 主动动词 + 宾语 | 宾语提前 + to be + 过去分词（+ by 主语或省略） |
| 示例 | "We surveyed 500 managers" | "Five hundred managers were surveyed"（by whom we know not） |
| to be 形式 | — | is/are/am/was/were/has been/have been/had been/will be/can be/will have been/being |
| "It" 开头 | — | 通常被动（"It can be seen that..." / "It is well known that..."） |

### 被动语态的四种合理场景（Evans 2017）——避免过度纠错

1. **doer 未知**："86 percent of the surveys were returned"（不知道谁退的）
2. **receiver 比_doer_更值得强调**："the cannabis dispensary owners were raided by the government"
3. **doer 已知但出于礼貌/怯懦需回避**："Your paper was rejected because it was impossible to wade through all the passive constructions"
4. **主语太长会延迟动词出场**："Surveying the homeless, who do not have fixed street addresses, phone numbers or email addresses, was accomplished by sending doctoral students into homeless encampments"

### 额外的主动化技巧

- **用所有格替代 "of" 介词短语**："the openness of managers" → "managers' openness"
- **用第一人称**（I / we）——参见 Ch03 conversational voice；"this study considers" / "research explores" / "it has been shown" 都是被去人格化的；"this writer" / "the present author" 是 Pollock 最痛恨的表达——直接说 "I"
- 国际学生因文化重视谦逊而倾向被动——但主动结构无需具有攻击性或自夸

---

## 区块三：Sound & Cadence（声音与节奏）

我们即使在默读时也"听见"文字（Douglas 2015）——因为视觉、语音、听觉中枢相连。声音/节奏对理解、motion/pacing、跨幕推进都关键。

### 句式四类型（Douglas 2015）——混用是关键

| 类型 | 结构 | 示例 |
|------|------|------|
| Simple | 一个独立主句 | "Sentences can be simple." |
| Complex | 主句 + 从句（从句不能独立） | "The major clause can stand on its own; the minor clause cannot." |
| Compound | 两个主句 + 并列连词（and/but/or/for/nor/yet/so） | "A compound sentence is comprised of two major clauses." |
| Compound-complex | 两主句 + 一从句嵌于其中 | "In a compound-complex sentence, like this one, there are two major clauses." |

**原则**：每段混用四类型，创造节奏变化。重复也可用（如 MLK "I Have a Dream"），但必须有意识。

### 标点 = 呼吸标记（Punctuation as breath marks）

把标点理解为说话时的停顿、变调、重音。**朗读测试**：
- **读一句时气不够**（需换气但无标点）→ 应加标点或拆句
- **过度换气**（连续短促呼吸）→ 去一些标点，合句为 compound/complex
- **逗号位置破坏流畅**（朗读才能发现的错位逗号）→ 调整

### 句长 / 段长变化

- **全短句** = 机关枪 rat-a-tat-tat（onomatopoeia!）
- **全长 compound-complex** = 读者溺水
- **混用长短** = 创造 motion + 给读者喘息 + exposition/action 之间的切换

**段长同理**（King 2000）：看段落结构就知道文章是否易读。满页长段 = slog；多短段 = 轻快但可能信息不足。**规则**：一段超半页就考虑拆分（尤其含 2+ 主旨时）；拆不了就让下一段短。

### 由简到复排序（Douglas 第三原则）

在复杂句、尤其列表中，把**最短、句法最简单的项放前，最长最复杂的放最后**。理由：(1) 按规模/重要性/复杂度排序创造有组织的流动；(2) 复杂项前置增加认知负荷（读者须在工作记忆中保持更多项直到句子结束）。

- ✗ "We obtained data from the Center for Research on Securities Pricing (CRSP), annual reports, a custom survey of executives and directors of Fortune 500 companies and proxies."
- ✓ "We obtained data from proxies, annual reports, the Center for Research on Securities Pricing (CRSP), and a custom survey of executives and directors of Fortune 500 companies."

---

## 区块四：Pollock 的 25 条 dos/don'ts

按"投稿前高价值"分三档。每条：规则 → Pollock 原文依据 → 错例→正例（如适用）。

### 🔴 高优先级（审稿人印象关键，投稿前必查）

**#3 构念不换同义词**
- 规则：谈理论构念时保持术语一致；在别处用同义词创造变化。
- 依据：相似词可能代表不同构念，同义词制造混淆。
- ✗ "CEO celebrity ... CEO fame ... CEO stardom"（混用）→ ✓ 全程 "CEO celebrity"

**#6 时态**
- 规则：描述他人既往研究、描述自己 methods 用过去时；讨论自己结果与结论用现在时。

**#14 Affect / Effect / Impact**
- 规则：affect = 动词（affect the outcome）；effect = 名词（the interaction effect was）；impact = 名词（have an impact）。
- ✗ "A is a moderator impacting the relationship of B with C" → ✓ "A moderates / influences the relationship of B with C"

**#15 递归 vs 非递归（recursive / non-recursive）**
- 规则：反直觉——recursive 模型是单向的；non-recursive 有反馈环或互惠效应。
- 判断：若论证某事反馈自身、或两事物互为影响 → non-recursive。

**#16 Not significant vs Insignificant**
- 规则：未达统计显著 = "not significant"（统计问题）；insignificant = 琐碎/不重要（effect size 问题）。小效应也可以重要。
- ✗ "The result was insignificant" → ✓ "The result was not statistically significant"

**#25 Ampersand（&）仅用于括号内引用**
- ✓ "Pfeffer and Salancik's (1978) theory" + "(Pfeffer & Salancik, 1978)"
- ✗ "Pfeffer & Salancik's (1978) theory"

### 🟡 中优先级（语法正确性）

**#1 Dingleberries**（段尾孤行）
- 规则：段尾最后一行不足 1/3 行宽时，重写段落消除该行（尤其面对页数限制时）。

**#2 平行结构 + signpost 过渡**
- 规则：重复相同句式结构帮助 skim 读者；结果段统一"重述假设→报告结果→Thus, Hypothesis X was supported/not supported"；清晰 signpost 标示 section 间切换。

**#5 单作者不用 we（royal we）**
- 规则：sole-authored 论文用 "I" 不用 "we"（review 中想掩盖单作者身份会 inevitably 搞砸）；多作者 "we" 可以。

**#9 数字写法**
- 规则：one through ten 拼写，除非在序列中（scale 1-5）、假设标签（H1）或表格统计值。

**#10 句首不用数字或缩写**
- 规则：句首数字拼写出来（"One third of all people..."）；缩写同理，即使之前用过也要展开。

**#13 数据单复数**
- 规则：data 是复数（the data show）；datum 单数；phenomena 复数；phenomenon 单数。

**#17 Since vs Because**
- 规则：since = "after that"（时间）；because = "why"（原因）。

**#18 That vs Which**
- 规则：that 引导限制性从句（必要理解句意）；which 引导非限制性从句（附加信息，可省）。
- ✓ "she opened the book that had all the answers"（必要）/ "her book, which was published last year"（附加）

### 🟢 低优先级（风格/惯例）

**#4 引用节制**：有目的才引；只引一次且另有两+引用同观点 → 删多余的；是缩短论文的好办法。

**#7 性别代词**：尽量用复数 "individuals/people" + "they" 回避性别问题；用单数时用 "him or her" 或交替性别；全男/全女组直接用对应。

**#8 不称 subjects**：称他们实际身份（students/mothers/clowns）或 participants/respondents/informants。

**#11 避免副词开头**：尤其恨 "importantly"——永不使用。偶尔 "similarly"/"conversely"/"finally" 可接受（替代表达）。

**#12 避免冗余修饰语**：副词/形容词与所修饰名词/动词同义时删除（hot fire / quickly speed）；多个冗余形容词用一个好的代替。副词尤易 clutter。

**#19 the 的用法**（帮非母语者）：the 指代"旧信息"/特指/独一无二（the universe）/有共同身份的复数群体（the social sciences）。

**#20 Their vs There**：their = 所有格；there = 位置。

**#21 While vs Although/But/Whereas**：while = 同时；although/but/whereas = 修饰或对比前述。

**#22 i.e. vs e.g.**：i.e. = in other words；e.g. = for example；只在括号内用（e.g., like this）；c.f. = compare（确保真在比较）。

**#23 撇号**：'s 单数所有格（even on names ending in s：the Stevens's house）；s' 复数所有格（students' grades）。

**#24 不用缩写**：期刊正文不用 contractions（I'm），除非引用他人原话。

---

## 与 SKILL.md prose 检查表的关系

SKILL.md 的 prose 表分三组：
- **故事工具组**（Human face / Action-commentary 比例 / Show don't tell / Descriptive examples）→ 对应 Pollock **Ch03**（本文件不重复，见 Ch03 笔记）
- **五病组**（Fat suit / Burying the lead / Sentence stuffing / Read my mind / Pompous prose）→ **本文件区块一**
- **工艺组**（Active voice / Sound & cadence / Terminology consistency / Parallel structure / Paragraph transitions / Clarity rewrite）→ Active voice + Sound & cadence 用**本文件区块二/三**；Terminology consistency 对应本文件 #3；Parallel structure 对应 #2

QC 执行时：prose 表每项打 ✓/△/✗ 后，对 △/✗ 项加载本文件对应区块获取修复细则。
