# _argument-grammar.md — 段落论证文法（argument unit，write-* 共用）

> 单一事实源：write-introduction / write-theory 渲染段内句子时共用本文法。分工：`_polish-protocol.md` 管**句子润色**（语料选用之后），本文法管**段落组装**（语料选用之前）——先有论证骨架，语料句式才上岗。
> 理论侧的段落级实现是 write-theory `corpus/subprotocols/paragraph_layout.md`（Topic→Reasoning→Tokens→Wrap 四段位 + 三类论据决策矩阵）；本文法把同一论证逻辑推广到全部 write-* 论证型段落，并把语料句式绑定到论证角色上。

## 病根与解法

语料按句位与范文型组织（mechanism_chain 按 Zhou 2017 型、hooks 按 canonical_id）——句子单独都好，但"语料优先改编"若先选句后连句，段落就是**拼贴**：没有 claim 统摄、evidence 在等一个没被提出的 reason、warrant 悬空。解法一句话：**先骨架后句子（role-first assembly）**——段落按论证角色序列组装，语料句式按角色填位，风格永远让位于角色。

## 论证单元（Booth 五问）

段落的组装单位是论证单元，不是句子。一个论证单元能回答五问：

| # | 角色 | 五问 | 段内位置 |
|---|------|------|---------|
| 1 | **Claim** | What do you want me to believe? | 段首 topic sentence **或段末收束句**可指认（推导链中段允许段首为局部前提、claim 落收束句；埋没段中且无收束才不合格）——v1.1 |
| 2 | **Reason** | Why do you say that? | 推理 moves（1–3 个；一个 move = 一次可质疑的推理转换，非一句引用） |
| 3 | **Evidence** | How do you know? | 每个**经验性承重 reason** 配发现锚点（方向/边界/量级 + 引文）；分析性/概念性桥接属 warrant 性质连接，不要求引文锚点——v1.1 |
| 4 | **Warrant** | How does that follow? | 连接 reason 与 claim 的一般性原则；仅三场合明言（跨域读者/原则有争议/claim 会被抗拒——见 write-theory `reasoning_soundness_protocol.md` §5） |
| 5 | **Acknowledgment & Response** | But what about…? | 预判的最强异议；按频次预算（0–2/篇），0 处合法 |

两个推论：
- 引用是 move 的证据，不替代 move——"Prior research shows X" 是 evidence 句，必须挂在一个 reason 下，不能自己顶一个推理环节。
- 引语锚定的归纳概括（v1.1）：概括有增量内容（个例→类别）即为归纳型 move，该引语就是它的锚点；仅复述引语内容则不是 move。
- 跨段论证：一个 reason 可以独立成段（Booth storyboard 一卡一理由），此时该段的 claim 即这个 reason；每段仍自成一个论证单元。

## 语料角色索引（角色 ≠ 风格）

选句时先定位角色，再进对应文件取句式——语料文件的排列顺序（范文型/句位型）不是段落顺序：

| 论证角色 | write-theory 语料 | write-introduction 语料 |
|---|---|---|
| **Claim** | `sentences/hypothesis_forms`、变体文件的 topic sentence | `contributions/`、`hooks/` 核心判断句、`micro-templates/thesis-models` |
| **Reason**（推理 move） | `sentences/mechanism_chain`、`subprotocols/paragraph_layout` §1 骨架 | `tensions/` 机制句、`theory-lens/` 解释句 |
| **Evidence**（发现锚点） | `subprotocols/evidence_patterns`、paragraph_layout §2 论据矩阵 | `literature-turns/literature-turn-templates` 变体 D、`stakes/` 量化变体 |
| **Warrant** | `subprotocols/reasoning_soundness_protocol` §1 [S] 类、paragraph_layout "Theory as Warrant" 行 | `theory-lens/` 的理论核心原则句 |
| **定义前提 [D]** | `sentences/construct_definition` | 构念定义句（intro 少用） |
| **A&R** | `sentences/acknowledgment_response` §2–§4 | 同左（跨节通用）+ `phrasebank/critique-phrases` |
| **Framing**（豁免） | `sentences/leitmotif-section-opener`、`sentences/closure` | `hooks/`、`transitions/`、`previews/` |

## 拼贴判据（corpus mosaic——反模式）

病征：每句都好，连起来不回答五问。任一命中即拼贴，按角色序列**重组**（句子保留，骨架重排，不推倒重写）：

1. **不承重**：删掉某句后没有任何 because/therefore 链断裂——它不承担论证功能（最小必要背景句除外）。
2. **证据孤儿**：≥2 个 evidence 句无共同 reason——证据在等一个没被提出的理由。
3. **Warrant 悬空**：warrant 句出现但段内无 reason→claim 对可连。
4. **无主段落**：读完说不出本段让你信什么——claim 缺位或埋没。
5. **引用列队**：相邻 2+ 句同层 evidence 顺序排列、句间无 because/however 关系（theory 审计 1 "References as theory" 的段落级形态；intro 侧即 anti-pattern ⑲引文堆叠的段内成因）。**例外（v1.1）**：同层例证共同挂靠一个已指认的 reason/claim、且各自带独立内容（如同一趋势的两个例子）→ 合法并列例证，不算列队。

## 完成判据

对每个论证型段落：五问各有可指认句位（framing 段豁免但标注 framing）；拼贴判据逐条不命中；承重 reason 均有 evidence 锚点或显式标注证据缺口。
