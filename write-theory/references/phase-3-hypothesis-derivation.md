# Phase 3: hypothesis derivation

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

### Phase 3: 假设推导

Theory 写作的心脏环节：路由假设结构，为每个假设生成逻辑严密、论证充分、段内布局合理的推导段落。

**3.1 Conditionality gate 与假设结构路由**

在默认写主效应前，先回答：

1. 在声明的 scope 内，核心机制是否有理由稳定运作？
2. 是否存在理论上可预见的条件，会改变行动者的暴露、注意、能力、动机、解释或约束，从而改变机制或预测方向？
3. 去掉该条件后，仍能推出有内容且可检验的平均关系吗？

- 若 1=是且 3=是：可把主效应作为主干，再判断是否需要边界假设。
- 若 2=是且 3=否：条件关系是理论主张本身，应先写条件化假设；主效应至多作为经论证的基线，不得因格式惯例强行加入。
- 若边界条件没有机制依据：不新增 moderator，先修理论。

```
假设体系包含哪些类型的假设？
│
├── 纯主效应 (X→Y) → 基础关系模板
├── 主效应 + 中介 (X→M→Y) → 机制推演模板 + 中介假设模板
├── 主效应 + 调节 (X×Z→Y) → 调节效应模板
├── 调节 + 中介 (Moderated mediation) → 机制推演 + 调节混合
└── 三向交互 (X×Z×W→Y) → 假设树模板
```

这里的结构是统计关系的表达形式，不代表理论深度。`X→M→Y` 并不自动比 `X→Y` 更有理论；一个无中介变量的预测也可包含多项行动者层面的过程推理。

**3.2 Hypothesis Development 段落级逻辑协议**

**每个假设推导段落是一个微型论证单元**。

> **核心目标**：本阶段是 Theory 写作的**心脏环节**。不管构建类型是机制推演、调节效应、假设树还是竞争假设，最终都要落实到假设推导段落。本阶段的任务是：为每一个假设生成一个逻辑严密、论证充分、段内布局合理的推导段落。

#### 语料调用（按推理任务选择）

先用文件开头的目录定位相关模式，只读取命中的小节；不得整批预载下列八个文件。

| 触发条件 | 读取 | 用途 |
|---|---|---|
| 每条假设 | `../corpus/subprotocols/hypothesis_derivation_patterns.md` 的一个匹配模式 + `../corpus/sentences/hypothesis_forms.md` 的对应形式 | 微观动作序列与可检验表述 |
| 需要完整段落骨架 | `../corpus/subprotocols/paragraph_layout.md` | Topic→Reasoning→Tokens→Wrap |
| 证据角色或摆放不清 | `../corpus/subprotocols/evidence_patterns.md` | 区分理论、实证、案例与反事实 warrant |
| 并行、累积或对照安排 | `../corpus/subprotocols/arrangement_patterns.md` | 选择非默认段内布局 |
| 反直觉、跨域或其他特殊动作 | `../corpus/subprotocols/argumentation_patterns.md` | 加载一个特殊论证模式 |
| 调节/条件假设 | `../corpus/subprotocols/bilateral_argumentation_templates.md` | high/low 双边推导；不适用于普通主效应 |
| 完整草稿生成后 | `../corpus/subprotocols/reasoning_soundness_protocol.md` | 最弱前提、必要性与反例压力测试 |

若标准 Anchor→Mechanism→Warrant→Prediction 已足够，不再加载安排或特殊动作文件。

#### 标准结构：交织式论证链（Interwoven Logic Chain）

文献引用与理论推理**交织**而非先后排列——这是管理学顶刊的默认写法（验证自 14 篇 MVP30 论文）。完整的段内布局（Topic→Reasoning→Tokens→Wrap 四段位 + 三类论据决策 + 段内诊断）见 `../corpus/subprotocols/paragraph_layout.md`。

```
[1. Topic Sentence]  →  [2. Theoretical Reasoning + Literature Support]  →  [3. Hypothesis Transition]
        ↓                         ↓                                              ↓
  本段的单一理论主张        多步因果链，每步由文献锚定：                      收束推理，引出假设
  (1-2句)                  "Prior research shows X. However, Y                  (1-2句)
                           remains unclear. We argue that Z
                           because [mechanism] ([citations])."
```

**具体展开（动作数量按理论任务动态调整）**：
```
[Topic Sentence]  → 本段的理论主张（1-2句）
     ↓
[Reasoning Move 1] → 建立相关前提/行动者状态 → "This suggests that..."
     ↓
[Reasoning Move 2] → 说明行为或过程如何改变 → "We argue that..."
     ↓
[Reasoning Move 3（如必要）] → 连接到结果、边界或竞争预测 → "Consequently..."
     ↓
[Convergence] → 单向预测用 "Taken together.../Therefore..."；竞争预测用 "Given these competing arguments..."
```

**why-chain 计数纪律**：一个 reasoning move 是一个有内容、可质疑的推理转换（例如刺激如何改变注意，注意如何改变选择），不是模型图中的一个箭头或一个变量。通常至少需要 2 个 move；复杂或反直觉主张可能需要更多。禁止为凑“2–3 步”机械增加中介、调节或同义改写。

**备选结构：分离式（少数情况使用）**——当某一步的文献支持特别密集、需要单独展开时，可将 [Reasoning] 和 [Literature Support] 暂时分离。但整个段落的默认节奏是交织的。

**各要素 QC**：

| 要素 | 必须做到 | 最常见失败模式 |
|------|---------|--------------|
| **Topic Sentence** | 同时包含话题、核心观点与必要范围；优先使用 active verb + concrete subject（如 "We argue that..."），并在最小背景后尽早给出判断 | 太宽泛/太局限；无主语被动语态；多句热身后仍看不到本段立场 |
| **Paragraph Architecture** | 每段完成 Point + 必要 Evidence/Warrant + Explanation + Link；长度服从单一主导理论任务和目标期刊节奏 | 短段只剩断言；长段混入第二个独立 claim；缺少 explanation 导致 "So what?" |
| **Theoretical Reasoning** | 从 X 到 Y 的必要推理移动均明确；相邻移动的逻辑关系可恢复，必要时用 transition，但连接词不是充分条件 | **逻辑跳跃**：省略关键过程；用 Consequently/Thus 掩盖未论证的 A→C |
| **Literature Support** | 总结前人研究的 argument/finding + 说明链接 | **引用罗列**：只有名字没有 argument |
| **Hypothesis Transition** | 收束句总结推理链，自然引出假设 | 无理论收束直接 "we hypothesize" |

**[2b. Concrete Illustration]（按需使用）**：
当某个推理跨层、反直觉、构念抽象或读者难以模拟过程时，可插入 1 句 concrete illustration：
- "For example, when [Company] faced [situation], [mechanism] produced [outcome]."
- 或用比喻："This is akin to [familiar scenario]..."
- 例子只负责澄清，不能替代 warrant 或证据；无需为每个步骤配置例子。

**[3b. 文献引用的功能要求]**：
- 引用必须说明它支持哪一个前提、机制或边界，不能只列作者；不要求每条引用都报告具体数字。
- 若原研究提供直接且可比的 finding，可用："[Author] et al. ([year]) showed that [finding]—consistent with the premise that..."；若引用承担概念或理论 warrant，则准确概括其 argument。

**逻辑跳跃诊断**：为每句标记功能（前提/过程转换/证据/warrant/预测），再问相邻两项之间是否能被合理反驳。连接词只能显示关系，不能证明关系；没有信号词不自动失败，有信号词也不自动通过。

**[2c. 识别策略的理论论证]**（制度冲击 / 自然实验研究必须包含）：

使用 IV / DiD / RDD 时，Theoretical Reasoning 的 why chain 中必须嵌入识别假设的理论论证——IV 的排除限制与第一阶段理论渠道、DiD 平行趋势的理论基础、RDD 断点局部可比较性。各策略在 why chain 中的嵌入位置与句式见 `../corpus/subprotocols/institutional_shock_lens.md` 第 4 节。

**检查**：如果 Methods 中描述了识别策略，但 Theory 段落中完全没有提及识别假设的理论基础 → ⚠️ 标记为"识别策略与理论脱节"。

**Topic Sentence CV 反模式示例**：
- ❌ "It is argued that CEO overconfidence affects firm risk." → 无主语被动，违反 Conversational Voice（见 `../../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` 禁用词表）
- ✅ "We argue that CEO overconfidence increases firm risk-taking because overconfident leaders systematically underestimate downside uncertainty." → active verb + concrete subject + 方向性预测
- 规则：Topic Sentence 是段落的第一印象，若用被动语态，读者会预期整段都是"报告腔"而非"论证声"。

#### 段落级 QC 检查表

- [ ] 主题句精准度：是否同时包含话题+核心观点？
- [ ] **Burying the lead**：最小必要背景后是否尽早说出核心判断，且段首不是无实质内容的元评论？
- [ ] 推理链完整性：每个因果步骤是否都在文中明确写出？
- [ ] **Read my mind**：每步因果推理间是否有 explicit transition？无"显然"/"不难发现"？
- [ ] 引用嵌入度：每个引用是否都总结了其 argument/finding？
- [ ] 术语一致性：同一构念在全段用的是否同一个术语？
- [ ] 证据-论点匹配：每个引用是否直接支持它所在推理步骤？
- [ ] **Sentence stuffing**：句子是否承担过多独立 claim、插入语遮蔽主干或迫使读者回读？长度只作为定位提示，不自动失败。
- [ ] 收束句质量：是否总结了推理链而非简单重复 "we hypothesize"？
- [ ] 段落独立性：单独阅读本段能否理解完整论证逻辑？
- [ ] **作者名开头**：why-chain 段段首句主语是否为他人姓名（"Smith (2020) showed..."）？→ topic sentence 必须是自己的理论主张，引用移到证据位（见 prose-craft-checklist §0.6-1）
- [ ] **段末 wrap**：段末句是否停在引用/证据上而无 "This suggests that..." 收束（abrupt stop）？→ 段末 1 句 wrap 回扣本段 claim；与"收束句质量"项互补——那项查收束是否简单重复 "we hypothesize"，本项查收束是否缺席（见 §0.6-5）；wrap 的正面语料（总结式 key line 标记词与骨架、前后夹击变体）见 `../../write-introduction/academic-writing-corpus/micro-templates/key-line-patterns.md` §3
- [ ] **Caveat-first**：段首是否以 "Although prior work..." 让步开头，推迟核心 claim？→ claim 前置，caveat 移后（见 §0.6-4）
- [ ] **前提最弱点**：每个 Anchor/Warrant 前提已标注 [D]/[S]/[E] 类型？最弱前提是否有单独一句防守（或已降级 claim / 转显式假设）？（见 `../corpus/subprotocols/reasoning_soundness_protocol.md` §1–2）
- [ ] **机制必要性门控**：Q1 主流更简单机制推不出同一预测？Q2 本机制有可区分的额外预测？Q3 删掉本机制故事不照样成立？（见 §3）
- [ ] **反例压力测试**：最弱前提所在步骤与反直觉步骤已回答"什么条件下这一步不成立"，处置（scope / 新假设 / 删除 / **承认但不回应**）已兑现？承认句与回应句从 `../corpus/sentences/acknowledgment_response.md` 取材（见 §4）
- [ ] **Warrant 表达**：跨领域读者 / 推理原则有争议 / claim 会被抗拒——三场合的 warrant 是否已**明言**（场合③须先立 warrant 再摆 reason+claim）？显而易见的 warrant 是否未画蛇添足（居高临下信号）？[E] 类前提是否均有硬证据、未被 [S] 规定顶替（硬证据规则）？（见 `../corpus/subprotocols/reasoning_soundness_protocol.md` §5）
- [ ] **防御性技术说明文风**（声音防火墙，见 `../corpus/subprotocols/reasoning_soundness_protocol.md` §7）：协议术语（[D]/[S]/[E]、门控、五测试）是否泄漏进正文？是否每段都有 "One might object.../Granted..." 式自辩形成防御节律？防守句是否多于推进句、claim 被 caveat 包围？→ 处置：防守转译为机制/证据叙述句或按隐去纪律删除；段落声音以 derivation patterns 与 `../corpus/sentences/` 范文句式为准，朗读测试——听起来应像"向同行讲理论故事"，不像"回答想象中的审稿人"；负向设限句与 hedge 堆叠的转换句式库见 `../../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` §5.7

---
