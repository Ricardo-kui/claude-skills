# Phase 5 — 质量验证与 QC 输出

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 5 质量验证时加载。

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告。

### QC Checklist

#### 功能层 QC（原有）
- [ ] **Completeness**: 所有强制模块（根据构建类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和适用构建类型标注
- [ ] **Credibility**: 未将单篇论文的特殊机制泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的模块
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实（特定构念定义、理论视角内容）已被明确标记
- [ ] **Build-Type Fidelity**: 骨架的推理模式与构建类型匹配（构念辨析型 ≠ 因果链骨架）
- [ ] **Dorobantu Coverage**: 核心问题链（WHAT/HOW/WHY/Theory Lens）都有对应模块
- [ ] **Why-Chain Audit**: T3 骨架中包含明确的机制步骤，无"常识跳跃"
- [ ] **Hypothesis Form Audit**: T4 骨架中假设方向、条件、IV/DV 明确

#### T6 Closure QC（v1.2.0 新增，同步 write-theory v3.3.0）

> **注意**：write-theory v3.3.0 明确——管理学顶刊（JMS, AMJ, SMJ, ASQ, OS 等）**不要求独立的 T6 Closure 段落**。最后假设推导段的局部收束信号（"Therefore, we hypothesize:" / "Thus," / "Accordingly,"）已承担收敛功能。因此本 skill 的 T6 QC 从"是否存在独立 T6"改为"是否存在合适的收束策略"。

- [ ] **局部收束信号**：每个假设前是否有 Therefore/Thus/Accordingly 等收敛信号？
- [ ] **独立 T6 段落**：是否存在独立的 "Taken together..." 段落？→ 如存在，标记为"非管理学标准但可选"；如不存在，标记为"管理学标准做法"
- [ ] **框架整合位置**：如假设间逻辑关系不够自明，框架总结出现在哪里？（A）最后假设段末尾嵌入 2-3 句 /（B）Discussion 开篇 /（C）缺失，可能导致追问
- [ ] **T6 Voice**：如存在独立或嵌入的框架总结，是否使用 accountable first-person（"we have argued"），无被动语态？
- [ ] **T6 叙事接力**：如存在独立或嵌入的框架总结，结尾能量级是否 ≥ 最后假设推导段？
- [ ] **Discussion 回补**：如 Theory 无框架总结，Results/Discussion 是否有 "one expected—one unexpected" 等整合信号？

**记录格式**：
```yaml
t6_closure_qc:
  independent_t6_present: true/false
  standard_in_management: false  # 管理学默认：false 为正常
  local_convergence_signals: ["Therefore", "Thus", "Accordingly"]
  framework_integration_strategy: "embedded / discussion_opening / missing"
  voice_check_passed: true/false/null
  narrative_energy_maintained: true/false/null
  discussion_compensation: true/false/null
```

#### Prose Craft QC（v1.2.0 新增）
- [ ] **Human Face in Theory**: P1 有具体场景说明 knot 在现实世界的样子？
- [ ] **Construct Illustration**: 每个新构念首次出现配 1 个 concrete illustration？
- [ ] **Why-chain Scenes**: 关键步骤可配微型场景（1-2句）？
- [ ] **Stroke/Glide 比例**: 机制推演段落 70% stroke / 30% glide？
- [ ] **Conversational Voice**: P1 用 "To resolve the paradox..."; 假设推导用 "We argue that..."; T6 用 "In sum, we have argued that..."
- [ ] **无被动语态**: 无 "It is argued that..." / "It is hypothesized that..." / "The literature suggests that..."
- [ ] **无 Inflated Symbolism**: 无 "paradigm shift" / "fundamentally transforms"

#### 识别策略 QC（v1.2.0 新增，制度冲击类研究）
- [ ] **IV 研究**: Theory 是否论证了排除限制的理论基础？是否说明了工具变量通过什么理论渠道影响处理变量？
- [ ] **DiD 研究**: Theory 是否论证了平行趋势的理论基础？是否预判了处理效应异质性来源？
- [ ] **RDD 研究**: Theory 是否论证了断点可比性？是否说明了断点两侧制度差异的理论含义？
- [ ] **生存分析**: Theory 是否解释了时间维度的理论意义？是否论证了比例风险假设的理论合理性？
- [ ] **Theory-Methods 识别链接**: 如果 Methods 描述了识别策略但 Theory 完全未提及 → ⚠️ 标记

#### 论证、安排与证据 QC（v1.4.0 新增，对应 write-theory v3.3.0 核心诉求）

以下检查项用于**评估范文在假设论证、论点论据安排、证据摆放三个维度上是否符合 write-theory 的协议**，并提取其偏离方式。目的是帮你在沉淀语料库时判断：哪些范做法可直接复用，哪些需要标注为"例外"或"反模式"。

- [ ] **微观动作完整性**: 每个假设推导段落是否包含 Anchor → Gap/Puzzle → Mechanism Move → Warrant → Prediction 的完整序列？缺失哪个动作？
- [ ] **双边论证完整性**: 调节/边界条件段落是否同时论证 high-condition 和 low-condition 的机制？（write-theory C20）
- [ ] **替代解释排除**: 论文是否识别并主动排除主要 competing explanations？使用什么策略？
- [ ] **安排模式识别**: 论文主要使用 Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel 中的哪一种？是否功能等价？
- [ ] **Concrete Illustration 规则**: 是否存在连续 2 个推理步骤无 illustration 的情况？
- [ ] **证据类型健康度**: Empirical finding + theoretical argument 是否占证据总数的 ≥70%？是否存在 evidence type 与论点功能错配？
- [ ] **证据功能多样性**: 是否只有 support 型引用？qualify / contrast / pave / rebut 功能是否缺失？
- [ ] **文献引用三要素**: 每个引用是否同时满足 concrete finding + argument summary + link to current mechanism？
- [ ] **交互模式明确度**: 调节假设是否明确 enhancing / buffering / antagonistic / existence / competing？（write-theory C10）
- [ ] **竞争假设收敛信号**: 竞争假设是否避免使用 "Therefore" 等传统因果收敛信号？（write-theory C14）
- [ ] **辩证对立对称性**: 两个对立机制的步骤数是否对称？方向是否真正反转（而非仅强度变化）？（write-theory C16-C17）
- [ ] **Moderator 选择框架**: 当存在 ≥2 moderators 时，是否有元框架解释为什么选择这些 moderator？（write-theory C18）
- [ ] **连续 IV 三点论证**: 连续 IV 是否论证 high / middle / low 三点的行为差异？（write-theory C19）

**记录格式**：
```yaml
argumentation_qc:
  micro_move_completeness: "5/5"  # 或缺失动作列表
  bilateral_argumentation: {high: true, low: true, symmetry: "完整"}
  alternative_explanations: {identified: ["account1"], ruled_out: ["account1"], strategy: "scope_condition"}
  arrangement_pattern: "Warrant-Embedded + Cumulative"
  illustration_gap_count: 0
  evidence_type_health: {empirical: 0.5, theoretical: 0.3, boundary: 0.1, negative: 0.1, analogical: 0.0}
  evidence_function_diversity: {support: 5, qualify: 1, contrast: 1, pave: 1, rebut: 0}
  three_element_citation_rate: "85%"
  write_theory_constraint_alignment:
    C10_interaction_pattern: "明确 enhancing"
    C14_competing_hypothesis_signal: "通过"
    C16_dialectical_symmetry: "N/A"
    C17_true_direction_reversal: "N/A"
    C18_moderator_selection_framework: "通过"
    C19_continuous_IV_three_point: "N/A"
    C20_bilateral_argumentation: "通过"
```

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表，含构建类型变体）
3. **Theory Logic Map**（Why-chain / Construct-clarity / Theory-citation 处理模式）
4. **Theory DNA Metrics**（可对比的量化指标）
5. **Dorobantu 问题链覆盖度表**
6. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
7. **QC Result**（通过/需修正/拒绝入库）
8. **模仿风险提示**（原文叙事薄弱点清单，防止用户在模仿时踩坑）

### 模仿风险提示

蒸馏过程发现的原文理论叙事薄弱点不是要被"修复"（论文已发表），而是作为**模式采纳风险评估**记录。目的是帮你在把范文做法沉淀到 `write-theory` 语料库时判断：哪些做法是安全的默认规则？哪些应降级为"例外"或"反模式"？当你自己写作时，这些提示也能帮你避开已被验证的陷阱。

**格式**：

```markdown
# 模仿风险提示: [作者_年份_期刊]

| 发现阶段 | 风险类型 | 原文表现 | 模仿后果 | 建议处理 |
|----------|----------|----------|----------|----------|
| Phase 1.5 (Why-chain 压力测试) | Why-chain 跳跃 | 从 X→Y 缺少中间机制论证 | 模仿后审稿人质疑机制 | 补充自己的中间机制论证，不要模仿跳跃 |
| Phase 2 (T1 提炼) | 构念定义模糊 | "organizational capability" 未界定类型 | 模仿后审稿人问 "what kind of capability?" | 增加 scope condition 或具体化构念 |
| Phase 2.4 (骨架批评) | 机制内容污染 | 骨架中包含 "performative tension" 等具体机制 | 模仿后变成复制特定论文的机制 | 泛化为 [theoretical mechanism]，只模仿组织方式 |
| Phase 1.5 (对齐检查) | T4→Methods 断裂 | T4 提出三向交互但 Methods 未报告交互项 | 模仿后假设与操作化脱节 | 确保 Methods 中的变量操作化与 Theory 假设严格对齐 |
| Phase 1.5 (T6 检查) | 独立 T6 Closure 段落 | 论文有独立的 "Taken together..." 段落 | 非管理学标准，可能被审稿人视为冗余 | 如需框架总结，嵌入最后假设段末尾 2-3 句，或放到 Discussion 开篇 |
| Phase 1.5 (T6 检查) | 无局部收敛信号 | 假设前无 Therefore/Thus/Accordingly | 假设像从天而降，非从机制推导 | 每个假设前必须有因果连接词收敛 |
| Phase 1.5 (T6 检查) | 框架总结能量骤降 | 框架总结用 "In conclusion, we tested..." 纯方法总结 | 破坏 Rising Action 连续性，读者失去兴趣 | 如需框架总结，用 "In sum, we have argued that..." 保持理论能量 |
| Phase 0.75 (Prose QC) | 无人脸 Theory | T1 定义只有抽象描述，无 "A promotion-focused CEO, for example..." | 模仿后读者难以将抽象构念与经验世界连接 | 每个新构念首次出现配 1 个具体例子 |
| Phase 0.75 (Prose QC) | 机器声 Theory | 假设推导用 "It is hypothesized that..." | 模仿后像模板生成而非研究者判断 | 改用 "We hypothesize that..." |
| Phase 1.25 (制度冲击) | 识别策略与理论脱节 | Methods 详细描述 IV/DiD/RDD 但 Theory 完全未论证 | 模仿后审稿人质疑"为什么这个识别策略在理论上是合理的？" | Theory 中必须嵌入识别假设的理论论证 |
| Phase 2.5 (段落 QC) | Topic Sentence 埋藏核心判断 | 段首句用 "Drawing on institutional theory..." 无方向性预测 | 读者读完整段才知道论点 | 段首句必须在 15 词内说出核心判断：主语+主动动词+方向 |
| Phase 2.5 (段落 QC) | 无收敛信号 | 假设前无 Therefore/Thus/Accordingly | 假设像从天而降，非从机制推导 | 每个假设前必须有因果连接词收敛 |
| Phase 2.5 (段落 QC) | Citation 替代机制 | T3 只有 "Smith (2010) argues... Jones (2012) found..." | 模仿后变成文献综述而非理论推演 | 每个引用必须总结 argument 并链接到机制步骤 |
| Phase 2.6 (微观动作) | 论证动作缺失 | 假设段落直接从 "We argue" 开始，无 Anchor 或 Gap | 读者不知道为什么需要这个新假设 | 补充 Anchor（学界共识）和 Gap（现有解释不足） |
| Phase 2.6 (微观动作) | Warrant 薄弱 | Mechanism Move 后只有一句 "consistent with [theory]"，无具体文献 | 机制步骤像作者臆断 | 每个 mechanism move 后嵌入 1-2 个总结 argument 的 citation |
| Phase 2.6 (双边论证) | 只论证调节增强方向 | 段落只说 "when W is high, X→Y is stronger"，未解释 low-W 条件 | 审稿人质疑机制完整性 | 同时论证 high-W 和 low-W 条件下的理论逻辑 |
| Phase 2.6 (替代解释) | 未排除竞争解释 | 论文提出新机制但 ignore 明显 alternative account | 审稿人会提出 "what about..." | 主动识别 1-2 个主要 competing explanations 并用理论/范围条件排除 |
| Phase 2.7 (安排模式) | 连续两步无 illustration | 机制链连续两个步骤都只有抽象推理，无案例/数字/场景 | 读者难以把抽象机制与经验世界连接 | 每两个推理步骤间至少插入 1 句 concrete illustration |
| Phase 2.7 (复杂假设) | 假设间关系不明 | H1 和 H2 段落无逻辑连接词，像两个独立 mini-papers | 论文理论框架显得碎片化 | 用 "Building on H1..." / "Beyond this direct effect..." 等明确假设间关系 |
| Phase 2.8 (证据类型) | 证据类型单一 | 全部 citation 都是 empirical finding，无 theoretical argument | 论证缺乏理论根基 | 每个机制步骤同时嵌入 empirical finding 和 theoretical warrant |
| Phase 2.8 (证据功能) | 只有 support 型引用 | 所有 citation 都用来"支持"，无 qualify / contrast / rebut | 论证显得 one-sided，缺乏 nuance | 在关键步骤加入限定、对比或排除替代解释的引用 |
| Phase 2.8 (文献引用三要素) | Citation 无 concrete finding | "Smith (2010) argues that..." 只有抽象主张，无具体发现 | 引用无法支撑具体机制步骤 | 改写为 "Smith (2010) found that [具体发现] — [argument summary]" |
| Phase 2.8 / C10 | 交互模式不明确 | 调节假设只说 "W moderates X→Y"，未说明 enhancing/buffering/antagonistic | 读者无法判断理论预期 | 在机制和假设中明确交互模式类型 |
| Phase 2.8 / C18 | Moderator 选择无框架 | "We also examine the moderating role of Z" 无理由逐个引入 | 审稿人质疑为什么选这些 moderator | 用元框架（如 awareness vs capacity）解释 moderator 选择 |
| Phase 2.8 / C19 | 连续 IV 只论证一端 | "High X increases Y" 但未讨论 low/middle X 的行为 | 理论预测不完整 | 对称论证 high / middle / low 三点的行为差异 |
```

**记录原则**：
- **不修复**：论文已发表，薄弱点是客观存在的
- **不美化**：不能为了让骨架"好看"而掩盖原文问题
- **可行动**：每条风险必须附带"建议处理"，告诉用户如果模仿此处该怎么做
- **跨论文可比较**：批量模式下，同类型风险的频率可作为"该构建类型的常见陷阱"沉淀

---
