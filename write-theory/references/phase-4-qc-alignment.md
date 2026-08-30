# Phase 4: QC and alignment

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

### Phase 4: QC 与对齐

四层审计 + 假设收敛 + Introduction↔Theory 跨 Section 对齐。

**4.1 通用 QC 审计**（Theory IS NOT / Construct Clarity / Hypothesis Clarity / 跨假设机制复用）

逐项判定细则与生成后验证流程见 `../corpus/storytelling/post-generation-validator.md`（生成 Theory 草稿后执行）。其中跨假设机制审计要求每个后续假设明确映射到它实际改变的 trunk 机制；**不要求**每个 moderator 复用机制全集。选择性作用于某一机制可以是理论贡献，但必须说明选择依据、未触及机制的范围含义与可区分预测。

#### 审计 1: Theory IS NOT（7 种伪理论陷阱 + 3 种 Ch04 病理）

| 陷阱 | 检查 |
|------|------|
| References as theory | 是否有罗列式引用？→ 改为总结 argument + 链接 |
| Data as theory | 是否用前人 findings 替代机制解释？→ 补充理论逻辑 |
| Variable lists as theory | 是否列出构念定义后直接出假设？→ 补充关系讨论 |
| Diagrams as theory | 是否有模型图但每条路径无文字解释？→ 补 verbal theory |
| Hypotheses as theory | 假设是否描述了 what 但没解释 why？→ 每个假设前必须有 why chain |
| Passive voice dumping | 是否有 "It is argued that" / "It is hypothesized that"？→ 改为 "We argue that" / "We hypothesize that" |
| Inflated symbolism | 是否有 "paradigm shift" / "fundamentally transforms"？→ 降级为具体贡献描述（"extend", "refine", "challenge"）；mechanism 推理句是否含绝对化词（all / always / never / every / no one）超出论证支撑？→ hedge 词库与限定条件句式见 `../../write-introduction/corpus/storytelling/prose-craft-checklist.md` §5.6 |
| Burying the lead | 最小必要背景后仍未出现核心判断？→ 尽早重写为"主语+主动动词+方向/机制" |
| Sentence stuffing | 一句承担多个独立 claim、插入语遮蔽主干，或一段混入多个主导任务？→ 按理论动作拆分，不按固定词数机械切分 |
| Read my mind | why chain 是否从 A 直接跳到 C，缺少 B 的中间步骤或 transition？→ 补充每个因果步骤，添加 explicit transition |

#### 审计 2: Construct Clarity（4 字段）

- [ ] **Definition**: 定义是否清晰、非循环、不含 antecedents/consequences？
- [ ] **Scope conditions**: 何时/何地/对谁适用？
- [ ] **Lineage**: 该构念从哪些先前构念演化而来？
- [ ] **Adjacent constructs**: 与相似构念的区别是什么？
- [ ] **Justification**（新构念必须）：为什么需要引入这个新构念？它比沿用现有构念多解释了什么？（AMJ Management Research Canvas: "definition, differentiation, and justification"——新构念三步缺一不可；现有构念可豁免此项）

#### 审计 3: Hypothesis Clarity（6 字段 + form-measurement 匹配）

- [ ] **Constructs named**
- [ ] **IV/DV roles clear**
- [ ] **Direction specified**
- [ ] **Relationship form specified**：线性/曲线/条件/阈值/差异比较等，且与构念测量尺度匹配
- [ ] **Mediator/moderator specified（如适用）**：只有理论与假设实际包含中介/调节时才要求；B0 过程解释或 F 竞争假设可标 N/A，不得为填字段发明变量
- [ ] **Matches theorized AND tested relationship**：假设措辞、理论关系形状、概念类型（differential prediction vs. differential validity）三者一致；统计检验方法由 `write-methods` 选择
- [ ] **Contestability（反命题测试，Booth Ch6）**：写出假设的反命题并问"会有人愿意反驳它吗？"三种弱 claim 直接拦截：①纯主题宣告（反命题无意义）②易验证事实（反命题明显为假）③伪争议（反命题显然为真）。没人愿意反驳的 claim 不值得论证——要么升级为有张力的方向性预测，要么删除
- [ ] **Figure–hypothesis linkage（Pollock Ch06）**：若 Theory 输出含 summarizing model figure，模型图中**每一条 path（IV→DV / 调节 / 中介连线）必须标注对应的假设编号**（H1、H2a 等）。无标签的总结图让审稿人无法快速核对"假设与图是否一致"——这是 Pollock 的硬性要求（"please label each link in your model with the associated hypothesis"）。另见 character ordering 决策表 `../corpus/subprotocols/character_ordering.md` 的 figure 放置规则。

**Form–Measurement 匹配指南**见 `../corpus/sentences/hypothesis_forms.md` 的「假设形式决策矩阵」。常见错误：
- 连续 IV + 连续 DV 却写成 If-then；
- 曲线关系拆成两个线性假设；
- 声称 differential validity（关系强度变化）却用 differential prediction（slope 变化）的语言描述；
- 使用 "X is associated with Y" 等无方向、无形式措辞。

#### 审计 4: Soundness（论证可靠性，复核 Phase 3 的 Soundness Card）

协议全文见 `../corpus/subprotocols/reasoning_soundness_protocol.md`。逐项复核：

- [ ] **前提类型标注**：每个推导段的 Anchor/Warrant 前提已完成 [D]/[S]/[E] 标注；无"标注不出类型"的伪装前提残留
- [ ] **最弱前提防守兑现**：Soundness Card 上标记的最弱前提，其处置（单独防守句 / 降级 claim / 转显式假设）在正文中真实兑现；[S] 类防守句已过 **warrant 五测试**（reasonable / sufficiently limited / superior to competing warrants / appropriate to this field / covers reason+claim）
- [ ] **必要性门控兑现**：门控三问未全过的机制已删除或已补可区分预测；无装饰性机制残留
- [ ] **Conditionality gate 兑现**：主效应已证明在声明 scope 内可稳定推出；若机制依条件而变，条件关系已成为主预测，未用无依据的平均主效应掩盖理论
- [ ] **反例处置兑现**：压力测试答出的条件已写入 scope condition 或升级为 moderation 假设；无法修复的弱点已走"承认但不回应"路径（诚实承认+三姿态之一）；无"藏起来不写"的条件
- [ ] **Warrant 明言/隐去纪律**：三场合（跨领域读者 / 有争议原则 / 读者抗拒的 claim）的 warrant 已明言且场合③先立 warrant 再摆 reason+claim；显而易见的 warrant 未明言（无居高临下信号）；**硬证据规则**——claim of fact 未仅靠 warrant+reason 支撑，[E] 前提未被 [S] 顶替

**与审计 1 的分工**：审计 1 查推理**形式**（跳跃、堆砌、伪理论陷阱），审计 4 查论证**可靠性**（前提可信、机制必要、反例已防守）。形式完美的链条仍可能塌在审计 4。

**4.2 假设收敛与过渡**

管理学顶刊论文的 Theory 部分通常以最后一个假设推导段的**局部收束信号**自然结束——假设就是推导的终点，推导完毕即转入 METHODS。**不需要独立的 T6 Closure 段落**。这与 Pollock (2025) 教科书建议存在差异，但反映了管理学领域实际发表惯例。

每个假设推导段落的局部收束（"Therefore, we hypothesize:" / "Hence:" / "Accordingly:"）已承担了收敛功能。如果过度使用全局收束（"Taken together, we have argued that..."），管理学审稿人可能视为冗余。

**例外**：少数 ASQ/ASR 的理论密集型论文（特别是构念辨析型或质性过程理论型）可能在假设后作极短的整合，但这不是标准做法。只保留恢复整体模型可理解性所必需的内容，不把它作为强制模块推荐。

**4.3 跨 Section 对齐检查**（Introduction ↔ Theory，强制输出）

**强制输出**。无论用户是否提供 Introduction claims，都输出对齐检查框架。如有 claims，填充具体检查项。

检查协议完整定义见 `../corpus/meta/alignment_protocol.md`。

**输出格式**：见 `../corpus/meta/alignment_protocol.md` 的「输出格式」节（Gap→Type / Makadok→Module / Preview→H / Lens→Lens 四维检查表 + 必须修复的不一致清单）。

---
