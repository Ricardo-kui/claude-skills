# Phase 5: QC and boundaries

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 5 — 质量验证与 QC 输出

> QC Checklist、最终输出物清单与模仿风险提示模板已外置：见 `../protocols/phase5_qc.md`。Phase 5 质量验证时加载。

## 成品验证（写作 QC）

Theory & Hypotheses 写作质量检查请使用 `/theory-review`——它覆盖构念清晰度、why-chain 完整性、假设形式和角色排序，基于 Pollock Ch06 和 MVP30 范文语料库。

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊构建类型**：不把构念辨析型的对比句式套用到机制推演型，不把过程理论的时间阶段套用到假设树型。
- **跳过 why chain 薄弱点**：即使原文 T3 只有 citation list 无机制推演，也要如实记录，不能美化。
- **强制覆盖所有模块**：如果某 Theory 确实缺失某模块，记录为 missing，不捏造。
- **混淆构建类型**：如果原文的理论构建方式模糊，明确标记为 "ambiguous between 机制推演型 and 假设树型"，不强行分类。
- **泛化机制内容**：不将"某篇论文中 X→M→Y 的具体机制"提炼为"机制推演型通常使用三步链"。只提炼**组织方式**，不提炼**机制内容**。
- **不将独立 T6 Closure 作为默认推荐**：write-theory v3.3.0 已明确管理学顶刊不要求独立 Closure 段落。蒸馏时记录独立 T6 存在性，但不再标记 "T6 缺失" 为默认风险。
- **不将四段式分离结构作为唯一节奏目标**：write-theory v3.3.0 以交织式为默认。蒸馏时区分 interwoven / separated / hybrid，关注功能等价性而非机械拍数。
- **虚构连接词-类型绑定**：不声称"机制推演型必须使用 Therefore"。连接词模式是统计倾向而非语法规则。标记连接词-类型一致性为"低"时，必须附具体证据（如"条件连接词占比 25%，远超机制推演型中位数 8%"），而非仅凭印象判断。
- **交叉矩阵硬化**：构建类型×假设结构矩阵中的 M/C/O 标注是基于当前语料库的归纳，不是理论上的不可能性证明。遇到矩阵外的组合时，标记为 "unclassified combination" 并记录，不强行排除。
- **证据链不捏造**：如标志性语言确实模糊（同一段落同时包含两种类型的标志性语言），如实记录模糊信号，不在证据链中虚构 "clearly indicates"。
- **不把偏离现行规则自动判成论文缺陷**：先判断是原文薄弱点、合法变体、corpus gap 还是 write-theory 设计缺陷；设计缺陷必须进入 `design-feedback-loop.md`，不能偷偷改写为模仿风险。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的构念名、理论家名、具体理论术语 | 泛化为 [construct] / [theory] / [theoretical mechanism] |
| **过度抽象** | 骨架抽象到只剩 "We argue that X affects Y"，失去推理结构的启示 | 保留关键推理标记（"creates [state]—a [definition]—that [action]" / "Whereas [A]..., [B]..."） |
| **构建类型错配** | 将构念辨析型的 "differentiate" 骨架标记为机制推演型 | 在骨架中标注准确的构建类型适用范围 |
| **机制内容泛化** | 将原文的具体机制步骤提炼为"通常使用两步链" | 只记录"两步链的组织方式"，不记录具体机制内容 |
| **忽略 why chain 断裂** | 只提取"写得好的"部分，忽略原文 T3 的跳跃 | 在 Theory Logic 和 QC 中明确记录断裂点 |
| **批量同质化** | 批量处理时忽视构建类型差异，用同一套骨架覆盖不同类型 | Phase 0 分类必须先行，不同构建类型分桶处理 |
| **混淆 theory story 与 summary** | 将 "Smith (2010) argues..." 式 citation 记录为机制骨架 | Theory story 必须以 construct/mechanism 开头，非作者名 |

---

## 与下游 Skill 的接口

- **`write-theory`** — Phase 4 的 reference-level 模式进入模块库/骨架库；核心规则反馈进入 `write-theory/corpus/_skill_design_feedback.yaml`，达到门槛后才做有边界修订。Phase 2.5 连接词统计可为 transition 诊断提供输入；微观动作、安排模式和证据功能可沉淀为 subprotocols。
- **`theory-review`** — Phase 1.5 的模块覆盖检查和 Theory Logic Map 可作为 theory-review 的审查基准；Phase 1.25 的制度冲击适配检查可为理论审查提供识别策略论证依据；Phase 2.1.6–2.1.8 的微观动作、双边论证、证据三要素检查可为 theory-review 提供段落级论证审查清单
- **`paper-review`** — Theory Logic Map 可用于跨 section 对齐检查（Theory 承诺 vs Results 兑现）；Phase 4 的跨 Section 对齐表可直接用于 paper-review 的全稿对齐检查；write-theory Constraint Alignment 表可用于 Theory ↔ write-theory 协议一致性审查
- **`write-introduction`** — T2 Theoretical Lens 和 Closure 策略（局部收束 / 嵌入框架总结）的提炼可用于优化 Introduction 的 P5 Preview 和 P7 Contribution；Phase 0.5 的 knot 继承检查可为 Introduction→Theory 叙事接力提供验证；Phase 2.1.6 的 Anchor/Gap/Prediction 序列可为 Introduction 的 Gap→Preview 结构提供节奏参照
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_theory.md`；新发现的论证模式存入 `skill_update_recommendations/argumentation_patterns/`

## 外部资产位置

- **外置协议文件**: `../protocols/`（quick_reference.md、pollock_annotations.md、phase2_extraction_frameworks.md、connector_patterns.md、profile_template.md、corpus_taxonomy.md、writeback_reminders.md、phase5_qc.md）
- **现有语料库索引（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/_mvp30_theory_index.md`
- **蒸馏产出存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/fine_grained/batch_*/[paper]_distilled_theory.md`
- **更新建议存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/skill_update_recommendations/`

## 输出结构参考

各 Phase 输出的结构化字段见各 Phase 正文中的 YAML/Markdown 表格。完整字段名和取值枚举已在 Phase 0–5 的示例输出块中逐一定义，无需单独维护 JSON Schema。

如需机器消费格式，参考 Vault 中已蒸馏的 `fine_grained/` 目录下的实际报告文件——其结构和字段集比抽象 schema 更准确地反映真实输出。

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch02-Ch06、Dorobantu et al. (2024)、Shepherd & Wiklund (2020) 叙事规则、MVP30 范文语料库构建。版本 1.4.0 — Theory 蒸馏 Meta-Skill（同步 write-theory v3.3.0）。*
