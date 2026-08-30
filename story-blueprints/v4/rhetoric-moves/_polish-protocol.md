---
type: meta
title: "润色协议（Polish Protocol）—— 用 rhetoric-moves 语料升级用户自己的论文表达"
created: 2026-08-24
updated: 2026-08-30
status: seed
tags: [润色, 语言表达, 流畅性]
related: ["[[story-blueprints/v4/rhetoric-moves/_index]]", "[[humanizer/SKILL]]"]
---

# 润色协议：用修辞动作语料升级你的语言表达

**目标**：输入你自己的草稿句/段，输出 2–3 个**保留你的内容、升级修辞执行**的变体。语料语句（信号词、句子模板、改写演示、参照句）**可直接采用或按需组合**；唯一质量闸门是**流畅性门**——**通顺、符合学术表达习惯、句子不过长**。

**硬约束（用户裁决 2026-08-25，终版）**：**不设重复率/相似度闸门**。语料库语句（信号词表、句子模板、改写演示、参照句）可直接使用或按需组合，无需为降重复率改写（查重护栏已删除）。**必须替换的是来源特异性内容**：来源论文的专名、数字、系数、表号、样本/年份等——替换它们以防串稿（把别家论文的事实误写成自己的）。唯一闸门 = **流畅性门**：通顺、符合学术表达规范、句子不过长。

**核心策略（用户提出）**：尽量完整使用语料库。**语料优先改编**——句子/段落模块一旦确定，尽量用该动作的语料句式来改编：以语料句式（结构蓝图/信号词/参照句/改写演示）为**改编底本**，替换来源特异性内容（专名/数字/系数/表号）后填入你的内容，而非脱离语料自拟；语料无对应句式时再自拟。如需让表达更立体，可**跨源合成**——综合多个范例的句式片段来拼装（连接器/节奏/收束装置）。跨源合成是**可选的表达技巧**，不是强制步骤。

**危险点（用户预警）**：AI 强行拼接会让句子**不流畅、不自然**。因此本协议以**流畅性门**为唯一闸门——管"像不像人写的"。不过流畅性门即不输出。

## 工作流

```
用户草稿 → 1.识别动作 → 2.取蓝图+信号词(允许多源) → 3.保内容升执行(含五病灶扫描) → 4.生成变体×3(以语料句式改编;含可选跨源合成)
         → 5.流畅性门(八查:通顺/学术/句长/AI腔/节奏) → 6.输出
```

### 1. 识别动作
读 `_index.md` 动作表，判断草稿在尝试哪个修辞动作（或由用户指定）。无法归类的草稿 → 不套动作，只做微观打磨（衔接词/主被动/冗余压缩）。

### 2. 取蓝图 + 信号词（**允许多源**）
读对应 move 文件的「结构蓝图」与「信号词表」——该动作的语料句式即**改编底本**，尽量采用，替换来源特异性内容（专名/数字/系数/表号/样本年份）后填入你的内容；需要更多表达层次时，再读 1–2 个其他 move 文件（或同一动作的其他论文范例）的信号词表，为跨源合成准备句式片段。参照句可直接采用或改造；只需替换来源特异性内容。

### 3. 保内容，升执行
- **保留**：用户的领域术语、具体数字/发现、因果主张、限定语。绝不编造或替换用户的实质内容。
- **升级**：句子的逻辑排序对齐结构蓝图；连接词/强调/缓和使用信号词；消除冗余与僵尸名词化。
- **五病灶扫描（Pollock 2025 Ch04，升级操作的靶点，每个变体生成前过一遍）**：
  1. **fat suit 臃肿**——删不承载含义的词："In order to"→"To"、"the tenets of" 删、"the reason for that is"→"because"；介词短语堆叠（"of the wealth effects of their decisions" 类）换单词或删除；肯定式表述短于否定式（"He agreed" 优于 "He did not disagree"）。
  2. **burying the lead 埋首句**——主句主张前置，先结论后限定；长开场从句（"predatory clauses"）里不许藏主语。
  3. **sentence stuffing 塞句**——一句多主意（多个 and/further/in addition to）拆成多句，一句一主意；相关但不推进主意的旁注 → 脚注。
  4. **read my mind 让读者猜**——五病灶中唯一"加词"的：补连接组织（A→B→C 的推导桥）、首次出现的构念定义、未说明的测量/控制理由。注意与削肥方向相反，先扫塞句再扫漏桥。
  5. **pompous prose 浮夸**——等价常用词优先（Oppenheimer 2006：复杂措辞反而让读者觉得作者更不聪明）；删 "to wit / inter alia / obviously / as everyone knows"；非公认构念标签的外语引用删。

### 4. 生成变体 ×3（以语料句式改编；含可选跨源合成）

每个变体都以语料句式为**改编底本**——尽量采用语料句式表达，替换来源特异性内容、按需微调语气，而非脱离语料自拟。

- **变体 A（单蓝图重排）**：按一个动作的蓝图与语料句式重排逻辑序、填内容。最稳，优先推荐。
- **变体 B（跨源合成，可选）**：想让表达更立体、或一句话需要多个动作的装置时使用。从 **2–3 个不同来源**各取一个句式片段，**结构级**拼接成一句：
  - 来源 1 供连接器/对比结构（如 "A first reading is that… Weighing against this…"）
  - 来源 2 供枚举/展开装置（如 "two distinct pathways… Externally… Internally…"）
  - 来源 3 供收束/裁定装置（如 "Which dominates depends on…"）
  - **内容词全部来自用户草稿**，句式片段直接采用（替换来源特异性内容）。
- **变体 C（换主宾视角）**：主动↔被动、行动者↔机制主语、机制前置↔结果前置，保留用户结论。

### 5. 流畅性门（通顺/学术/句长，强制）

每个变体过以下七查，**任一不过即作废该变体**：

1. **主句骨架可识别**：一句话必须能画出清晰的 主—谓—宾 主干；堆了 3+ 个并列从句且无明确协调词 = 拼贴。
2. **句子不过长**（用户裁决 2026-08-24）：单句以 20–30 词为常，超过 ~40 词必须拆句。宁可两句短句，不要一句长龙——句长是通顺的第一观感。
3. **融合源 ≤3**：一句话借用的句式来源超过 3 个 = 拼贴信号，拆成两句或砍掉最弱的片段。
4. **搭配自然**：每个 名-形 / 动-宾 组合须是英语惯用搭配；陌生搭配 >1 处 → 重写（如 "steeper growth bar" 可，"heightened visibility demands of the growth" 不可）。
5. **读诵测试**：默读一遍。有节奏、能一口气读完 = 通过；磕绊、无停顿逻辑 = 重写。
6. **保义保语气**：融合不得改变用户草稿的意思或语气（假设句不变成因果断言、限定语不丢）；改变即弃。
7. **AI 腔速查**：决赛句对照下方 §AI 腔速查表逐条过；学术语域的正式词不算 AI 腔（见表尾误报护栏）。
8. **节奏与句式多样（Pollock Ch04 / Douglas 三原则）**：段落内长短句交替、列表从简到繁排序、标点当换气点——连续 3+ 句等长 = 节奏单调，改写。

### 6. 输出
给每个变体 + 流畅性门结果（哪几查通过）。用户选一个，或要求再生成。

## AI 腔速查表（humanizer 精选·学术润色版）

来源：`humanizer` skill（Wikipedia "Signs of AI writing" 35 型，本表为学术润色场景的精选）。完整清单与正反例见 `../humanizer/SKILL.md`。

| # | 模式 | 盯什么词 | 学术场景处理 |
|---|---|---|---|
| 1 | 夸大重要性 | stands as / a testament to / pivotal / crucial / underscores / marks a shift / evolving landscape | 把"标记转折/证明遗产"降为具体事实句 |
| 2 | -ing 浅分析 | highlighting / underscoring / reflecting / fostering / showcasing… | 简单事实后挂 -ing 从句装深刻 → 删或改为具体机制句 |
| 3 | 销售腔 | boasts / vibrant / rich (比喻) / renowned / groundbreaking | 学术描述零容忍，直接删饰词 |
| 4 | 模糊来源 | Experts argue / Some critics / Industry reports | 管理学语境：换成具名文献；无来源则删主张 |
| 5 | 高频 AI 词 | delve / landscape (抽象) / tapestry / pivotal / crucial / enhance / underscore / interplay | 成群出现才是信号；单独一个可保留 |
| 6 | 逃避 is/are | serves as / stands as / boasts / features 代替 is/has | 换回简单动词："X serves as Y" → "X is Y" |
| 7 | 强迫三连 | 任何凑成三项的排比 | 保留真实三项；凑数项删 |
| 8 | Not X but Y / 剪截否定尾 | "not just X, it's Y" / "no guessing" 类 | 改为直陈句 |
| 9 | 填充短语 | in order to / due to the fact that / it is important to note that | "In order to"→"To"、"due to the fact that"→"because"、删 "it is important to note that" |
| 10 | 限定语堆叠 | could potentially / might arguably / to be fair | 证据支持的限定语保留一个，其余删 |
| 11 | 假装揭示真相 | The real question is / at its core / fundamentally | 删壳，直陈那个主张 |
| 12 | 假深度格言 | X is the Y of Z / the currency of | 换成带细节的具体主张 |

**误报护栏（不可无脑套用）**：正式学术词 ≠ AI 腔（§5 只针对成群高频词）；单个 however/additionally 不是信号；有来源的限定语、真实的 scope statement 保留；引用/题名内的短语不改。判 AI 腔看**多信号同段聚集**，单条证据不定罪。

## Pollock Ch04 速查（line-editing 十条）

来源：Pollock (2025) *How to Use Storytelling* Ch04（Vault 笔记 `obs-pollock2025-ch04-04`）。润色终检逐条过：

1. 结果表述用 **"not significant"**，禁 "insignificant"（后者指效应量微不足道，两回事）。
2. **affect**=动词、**effect**=名词、**impact**=名词；"A impacts B" 是坏语法，写 "A affects B"。
3. **that** 引限制性从句（去掉变义）、**which** 引非限制性从句（去掉不变义）。
4. **since**=自从、**because**=原因；因果句用 because。
5. **i.e. / e.g.** 只出现在括号内；c.f. 是"比较"不是"例如"。
6. 句首不放数字与缩写（拼写或改写句式）。
7. 句首副词生硬（"importantly" 禁用）；过渡靠结构不靠 "importantly"。
8. **关键构念禁同义词轮换**（与 write-theory 硬约束 #5 呼应）——构念术语全篇统一，变化感留给非术语表达。
9. 学术文章**不用缩略形式**（don't → do not），除非引语原文如此。
10. **&** 只用于括号内引用；正文写 "and"（"Pfeffer and Salancik's (1978) theory" ✓ / "Pfeffer & Salancik's theory" ✗）。

## 与现有资产的边界

- **Morley phrasebank（变化库）**：提供句子表面层改写变体，可充当跨源合成的"来源 3"（收束/措辞装置）；本协议在其上定"修辞动作意图层"。
- **humanizer（AI 味去除）**：已安装为独立 skill（`../humanizer/`，Wikipedia "Signs of AI writing" 35 型）；本协议 §AI 腔速查表为其学术精选，流畅性门第 7 查执行。顺序：先升级表达，再过 AI 腔速查。
- **Pollock Ch04（Vault 原子笔记）**：五病灶扫描（工作流 step 3）与 line-editing 十条的理论依据；manuscript 级 checklist 亦在该笔记。
- **write-\* corpus（功能模板）**：功能模板教论元结构，本层教句子执行。中文功能模板 + 本层信号词 = 完整执行路径。
- **多篇蒸馏联动**：跨源合成需要的"多来源句式片段"，来自不同论文的 distill 产物（blueprint 卡 + move 文件 + 各自参照句）。蒸馏越多，可借的形状越多样，表达越丰富——这是"综合多篇顶刊句式"能力的原料。

## 使用示例

示意（草稿句 + 处理路径）：
- 草稿："We examine the effect of common ownership on recall time."
- 变体 A（单蓝图重排）：按机制二链蓝图重排，直接采用语料句式并替换来源特异性内容，得到一句主谓宾清晰、20–30 词的升级句。
- 变体 B（跨源合成，可选）：综合比较结构与收束装置，让表达更立体；来源特异性内容仍须替换。
- 变体 C（换主宾视角）：主动↔被动、机制主语前置。

三个变体都过流畅性门（句长 20–30 词、主谓宾可识别、搭配自然）即交付——**不再为降重复率改写**。

## §write-* 共用纪律（write-introduction / write-theory / write-methods / write-results 四 skill 的单一事实源）

各 write-* skill 的润色与锚点段落以本节为准；skill 正文只保留指针与本 skill 差异项。

- **每句位 ≤2–3 候选**：措辞变体限量，不为变化而更换已准确的术语。
- **specificity gate**：替换后的句子若能原样放进任何一篇论文 = 不合格——必须具体到本文构念/机制/情境。
- **输出形态**：润色结果以 `### 措辞润色建议` 块附骨架末尾，不覆盖骨架原文；不改骨架占位。
- **锚点/语料使用**：语料语句可直接采用，仅替换来源特异性内容（专名/数字/系数/表号）防串稿；不设重复率闸门（见上方硬约束），唯一闸门=流畅性门。
- **骨架优先**：语料库只提供措辞变体，不替代论证结构；hedging 强度不得突破 causal-hedging 设计家族上限。
