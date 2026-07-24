# Phase 4: QC and alignment

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

### Phase 4: QC 与对齐

三层审计 + 假设收敛 + Introduction↔Theory 跨 Section 对齐。

**4.1 通用 QC 审计**（Theory IS NOT / Construct Clarity / Hypothesis Clarity）

逐项判定细则与生成后验证流程见 `../corpus/storytelling/post-generation-validator.md`（生成 Theory 草稿后执行）。

#### 审计 1: Theory IS NOT（7 种伪理论陷阱 + 3 种 Ch04 病理）

| 陷阱 | 检查 |
|------|------|
| References as theory | 是否有罗列式引用？→ 改为总结 argument + 链接 |
| Data as theory | 是否用前人 findings 替代机制解释？→ 补充理论逻辑 |
| Variable lists as theory | 是否列出构念定义后直接出假设？→ 补充关系讨论 |
| Diagrams as theory | 是否有模型图但每条路径无文字解释？→ 补 verbal theory |
| Hypotheses as theory | 假设是否描述了 what 但没解释 why？→ 每个假设前必须有 why chain |
| Passive voice dumping | 是否有 "It is argued that" / "It is hypothesized that"？→ 改为 "We argue that" / "We hypothesize that" |
| Inflated symbolism | 是否有 "paradigm shift" / "fundamentally transforms"？→ 降级为具体贡献描述（"extend", "refine", "challenge"） |
| Burying the lead | 假设推导段段首句是否未在 15 词内说出核心判断？→ 重写段首句为"主语+主动动词+方向" |
| Sentence stuffing | 单句 > 30 词或单段 > 200 词？→ 拆分长句，每句一个核心判断 |
| Read my mind | why chain 是否从 A 直接跳到 C，缺少 B 的中间步骤或 transition？→ 补充每个因果步骤，添加 explicit transition |

#### 审计 2: Construct Clarity（4 字段）

- [ ] **Definition**: 定义是否清晰、非循环、不含 antecedents/consequences？
- [ ] **Scope conditions**: 何时/何地/对谁适用？
- [ ] **Lineage**: 该构念从哪些先前构念演化而来？
- [ ] **Adjacent constructs**: 与相似构念的区别是什么？

#### 审计 3: Hypothesis Clarity（6 字段 + form-measurement 匹配）

- [ ] **Constructs named**
- [ ] **IV/DV roles clear**
- [ ] **Direction specified**
- [ ] **Relationship form specified**：线性/曲线/条件/阈值/差异比较等，且与构念测量尺度匹配
- [ ] **Mediator/moderator specified**
- [ ] **Matches theorized AND tested relationship**：假设措辞、理论关系形状、概念类型（differential prediction vs. differential validity）三者一致；统计检验方法由 `write-methods` 选择

**Form–Measurement 匹配指南**见 `../corpus/sentences/hypothesis_forms.md` 的「假设形式决策矩阵」。常见错误：
- 连续 IV + 连续 DV 却写成 If-then；
- 曲线关系拆成两个线性假设；
- 声称 differential validity（关系强度变化）却用 differential prediction（slope 变化）的语言描述；
- 使用 "X is associated with Y" 等无方向、无形式措辞。

**4.2 假设收敛与过渡**

管理学顶刊论文的 Theory 部分通常以最后一个假设推导段的**局部收束信号**自然结束——假设就是推导的终点，推导完毕即转入 METHODS。**不需要独立的 T6 Closure 段落**。这与 Pollock (2025) 教科书建议存在差异，但反映了管理学领域实际发表惯例。

每个假设推导段落的局部收束（"Therefore, we hypothesize:" / "Hence:" / "Accordingly:"）已承担了收敛功能。如果过度使用全局收束（"Taken together, we have argued that..."），管理学审稿人可能视为冗余。

**例外**：少数 ASQ/ASR 的理论密集型论文（特别是构念辨析型或质性过程理论型）可能在假设后有一个简短的整合段落（2-3 句），但这不是标准做法。不应将其作为强制模块推荐。

**4.3 跨 Section 对齐检查**（Introduction ↔ Theory，强制输出）

**强制输出**。无论用户是否提供 Introduction claims，都输出对齐检查框架。如有 claims，填充具体检查项。

检查协议完整定义见 `../corpus/meta/alignment_protocol.md`。

**输出格式**：见 `../corpus/meta/alignment_protocol.md` 的「输出格式」节（Gap→Type / Makadok→Module / Preview→H / Lens→Lens 四维检查表 + 必须修复的不一致清单）。

---
