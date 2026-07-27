# Intertextual Construction Playbook — Literature Turn 构造层手册

本文件是 **生成层上游手册**：当你已诊断出 `conversation_strategy`（检测层见
`golden-biddle-locke-four-moves.md`），需要构造或修复 Literature Turn 时使用。
句法模板层（变体 A–F、期刊适配、配对规则）在
`write-introduction/academic-writing-corpus/literature-turns/`，本文件不重复，
只提供模板层之上的**构造机制、组合合法性与伦理边界**。

来源：Locke & Golden-Biddle (1997)；Golden-Biddle & Locke (2007) Ch2；
Pollock (2025) Ch5 的语言标记词表。

## 0. 核心立场：文献是被构造的，不是被发现的

> "It is as if we configure and reassemble the available pieces of a jigsaw
> puzzle in such a way that they contour an opening or a space into which our
> theorized storyline will fit." — GBL 2007, Ch2

- 不存在先于写作的"该领域文献"实体。每个作者都在**主动选择、组织、重写**
  既有研究，使其轮廓出自己 storyline 需要的空间。
- 文献具有真实的流动性：同一批文献可以被 authentic 地塑造为多个方向
  （Kilduff 1993 对 March & Simon 的分析；Bazerman 1993 对 Gould &
  Lewontin 的分析）。但流动性有 **outer limits**（判据见
  `golden-biddle-locke-four-moves.md` §Outer Limits）。
- 因此 `conversation_strategy` 的选择服从**文献的真实状态与作者的构造目的**，
  不由 `gap_type` 推出。两种诊断相互独立（§2 的 3×3 矩阵）。

## 1. 三种 Coherence 的构造机制

### 1.1 Synthesized Coherence（综合）

**构造目标**：让此前被认为无关的研究显露出共同的、尚未被开发的调查关切。

**构造机制**（GBL Ch2 识别的两种典型做法）：

1. **碎片整合**：把零散引用组织为围绕同一隐性问题聚集的"bits and pieces"／
   "building blocks"（Sutton 1991；Sutton & Callahan 1987 从组织成长文献与
   稀疏的组织死亡文献中拼出"组织死亡过程模型的 building blocks"）。
2. **交点重写**（intersection rewriting）：把两个公认但分立的研究纲领**各自
   重写**，使交集显现。范文解剖——Locke (1996)：
   - 步骤 1：分别概括两个文献流，突出各自对共同现象的关切（把组织情感文献
     重写为"关注服务接触中的情感"，把服务管理文献重写为"关注接触中的情感
     展示"）；
   - 步骤 2：用共性词建立连接（common, general, shared, underlying）；
   - 步骤 3：把隐性共性显性化（implicitly, in both, make the implicit
     explicit）。

**语言标记**（Pollock Ch5）：common / general / shared / underlying；in each /
both / as did；implicitly / in both。

**失败模式**：交点被断言而未被演示（两个文献流各引一两篇就宣布交汇）；
虚假合成（两个"传统"实为同一流派的变体）。

**句法模板**：`literature-turns/02-synthesized-coherence.md`（变体 A–E）。

### 1.2 Progressive Coherence（递进）

**构造目标**：把一个公认相关的研究传统写成累积推进的知识增长，使本研究成为
其"逻辑下一步"。

**构造机制**：

1. **序列化引文**：按时间队列排列引文，展示 successive cohorts 各自推进了
   什么（Bechky 2003 的知识整合引文链）。
2. **密度 + 成熟度描述**：密集引文配合 "a considerable body of literature"
   类描述词，确立该传统的成熟度与共识（Cheek & Gibson 2003）。
3. **过滤式推进**（filtering）：范文解剖——Isabella (1990)：每一波文献都比
   上一波更窄地逼近作者需要的下一步（活动序列 → 认知解释 → 参照系转换），
   文献本身被写成对"logical next step"的铺垫，而非中性编年。

**语言标记**：recently / over the last xx years / early studies... more recent
studies... / over the years。

**失败模式**：有编年无方向（日期罗列但不收敛）；只靠引文密度宣称成熟，
没有展示知识如何累积。

**句法模板**：`literature-turns/01-progressive-coherence.md`（变体 A–F）。

### 1.3 Noncoherence（不连贯）

**构造目标**：把同一研究纲领内的文献组织为**相互不和但共同承认领域重要性**
的对垒结构，为裁决或替换腾出空间。

**构造机制**：

1. **对垒阵营**：明确命名各阵营及其代表学者（Gersick 1994 把组织适应性
   研究者分置两营）；阵营必须**双方都被充分代表**。
2. **相互抵消的发现**：展示 competing findings that nullify each other
   （Yan & Gray 1994 的 "conflicting results"；Langton 1984 的
   "contradictory assessments"）。
3. **不和但同域**：纪律——构造的是 disagreement among researchers who
   agree on the domain's importance，不是把一方写成可以忽略。

**语言标记**：on the one hand / inconsistent / conflicting / lack of consensus /
controversy / conversely / in contrast。

**失败模式**：稻草阵营（一方引文单薄或被简化）；伪平衡（证据其实一边倒时
强行构造对立）。

**句法模板**：`literature-turns/03-non-coherence.md`（变体 A–E）。

## 2. 3×3 组合矩阵：Coherence × Problematization

GBL 的核心发现：三种 coherence 与三种 problematization 之间**无一一对应**，
九种组合在顶刊中均被观察到。下表是组合的设计空间——`conversation_strategy`
服从文献状态与构造目的，`gap_type` 服从贡献的证据强度，两轴独立选择。

### 默认对角线（验证最充分，现有路由的基础）

| 组合 | 弧线 | Storyline 模板 | 核心风险 | 现有语料 |
|---|---|---|---|---|
| Progressive × Incompleteness | 累积延伸 | "领域已建成 A、B；C 尚未被检视——是发展的自然下一步" | 被读为增量研究；必须论证遗漏的理论后果 | `literature-turns/01`；MVP30 ~40% |
| Synthesized × Inadequacy | 交汇盲区 | "各文献流各自抓住了现象的一部分，交汇处存在集体盲区" | 虚假合成；桥接被读为强行 | `literature-turns/02`；MVP30 ~45% |
| Noncoherence × Incommensurability | 裁决替换 | "两个阵营不能同时正确——除非重新理解" | 稻草阵营；论调过激招致 backlash | `literature-turns/03`（zhou2017、keeves2017） |

### 合法非对角组合（有据可查）

| 组合 | 弧线 | Storyline 模板 | 核心风险 | 例证 |
|---|---|---|---|---|
| Synthesized × Incompleteness | 双重沉默 | "两个成熟文献流各自正确且充分，只是从未交叉" | "so what"——交叉点必须 consequential，不只是未被检视 | wowak2025（`literature-turns/02` 变体 D）；Locke 1996 |
| Progressive × Inadequacy | 主流盲区 | "累积成熟的传统内部存在系统性视角遗漏（去情境化/单一情境/构念混淆）" | 必须用该传统自身的标准证明遗漏 | Elsbach & Kramer 2003（GBL Ch2）；decision tree 中 decontextualization 型 |
| Noncoherence × Inadequacy | 调停（consensus creation） | "两个阵营各自部分正确；本研究通过澄清边界条件裁决分歧" | 无裁决依据的和稀泥——设计必须能真正判别（常配 write-theory 竞争假设型） | Hirsch & Lounsbury 1997；Hollenbeck 2008 |
| Progressive × Incommensurability | 共识颠覆 | "成熟共识在核心假设上错了" | 稻草人危险最高；需要决定性反例或异常证据与充分理论跑道 | gamache2023（consensus challenge + counterexample）；Hahl 2017（经典理论颠覆） |

### 可疑组合（出现时先重新诊断）

| 组合 | 问题 | 处置 |
|---|---|---|
| Noncoherence × Incompleteness | 文献既在冲突，"还有更多可知道"就 undersell 了张力 | 通常应重新诊断为 Noncoherence × Inadequacy；唯一例外：冲突被承认但某一具体机制未被检视 |
| Synthesized × Incommensurability | 两线作战：同时替换多个文献流的自我理解 | 仅适用于范式桥接级贡献；先确认证据强度足以支撑双线否定 |

### 组合选择规则

1. **先看文献真实状态**（成熟共识 / 分立并行 / 公开冲突）→ 定 coherence；
   coherence 是构造选择，但受文献状态约束——证据一边倒时不可构造 Noncoherence。
2. **再看贡献的证据强度**（遗漏可论证 / 盲区可证明 / 错误可证伪）→ 定
   problematization；Pollock 的适配判据：something wrong vs more to know。
3. **禁止反推**：不得由 `gap_type` 推出 `conversation_strategy`，反之亦然。
   对角线是默认而非规则。

## 3. 边界与接口

- **稻草人判据**：本手册的构造自由以 outer limits 为界，操作判据见
  `golden-biddle-locke-four-moves.md` §Outer Limits（Move 3 通过条件）。
- **检测层**：四步功能检查与 `gbl_four_moves` 输出见
  `golden-biddle-locke-four-moves.md`。
- **句法模板层**：变体、配对、期刊适配见
  `write-introduction/academic-writing-corpus/literature-turns/_index.md`。
- **叙事弧线层**：段落能量与阶段连续性按 `gap_type` 选择（
  `storytelling/tension-escalation-protocol.md`）；Literature Turn 内部构造按
  `conversation_strategy` 选择（本手册 §1–2）。两轴独立。
- **Move 1×3 交织（双重张力）**：现象驱动论文中 field complication 与
  theoretical complication 的交织架构（Turner 1976 范例的量化适配，含双
  resolution 纪律与删除检验）见
  `write-introduction/academic-writing-corpus/hooks/22-twin-complication.md`。
- **不替代范文类比**：本手册提供构造机制，具体论文的叙事类比仍以 MVP30
  范文库为准。
