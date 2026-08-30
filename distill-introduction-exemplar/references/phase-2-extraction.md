# Phase 2: extraction

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 2 — 深度提炼：模块功能、表达骨架、Rhetorical Logic

对 Phase 1 定位到的每个功能模块，执行三重提炼。

### 2.1 模块功能提炼（Persuasive Action）

回答：这个模块完成了什么**说服动作**？

| 说服动作 | 适用模块 | 示例 |
|----------|----------|------|
| 兴趣锚定 | Hook | 用 paradox/anomaly 让读者意识到 "这里有问题" |
| 共同体建构 | Literature Turn | 建立 "我们共享这些假设" 的读者-作者同盟 |
| 张力制造 | Tension | 在 shared assumptions 中插入裂缝，制造认知失调 |
| 重要性升级 | Stakes | 将裂缝升级为 "必须解决的理论/实践危机" |
| 框架引入 | Theory Lens | 提供新的解释透镜，让读者看到裂缝的另一面 |
| 可信度建立 | Preview | 通过方法/情境/发现的预览让读者相信 "你能回答" |
| 承诺锁定 | Contribution | 将贡献声明固化为可与 Discussion 兑现的契约 |

### 2.2 表达骨架提炼（Expression Skeleton）

**即时捕获原则（Inline Capture）**：借鉴 grill-with-docs "Update CONTEXT.md right there. Don't batch these up"——在 Phase 2 阅读到每个模块时，**立即提炼骨架**，不等到 Phase 4 再汇总。这防止模式遗忘和细节流失。

将具体措辞抽象为**可填充的句法结构**。**注意**：Introduction 的骨架是模块级的，不是段落级的——同一功能模块可以在不同论文中由不同数量的段落完成。

**骨架格式**：
```text
[功能标签]: Tension — Incompleteness 标志性开场
[骨架]: Although prior research has extensively examined [established relationship] ([citations]), the [mechanism/condition/process] through which [X] affects [Y] remains [poorly understood / unclear / largely unaddressed]. This omission is theoretically important because [theoretical consequence of not knowing].
[可迁移性]: 高 — 出现在 10/28 篇范文中
[抽象层级]: "L0 invariant / L1 route / L2 optional tactic / L3 paper signature"
[Incommensurability 路由适配]: "R1 / R2 / R3 / R4 / cross-route / n.a."
[范式排他性]: Incompleteness 专用，Inadequacy/Incommensurability 不应使用 "remains unclear"
[Gap 变体]:
  - Inadequacy 版本: "While prior research has treated [X] as [assumption], this view overlooks [specific limitation] because [reason]."
  - Incommensurability 版本: "A consensus is building that [dominant view] ([citations]). Yet [counter-evidence], suggesting that [alternative view] may be [more accurate / incomplete]."
[问题对应]: Dorobantu Q — "What is missing in prior research? What are its limitations?"
[对应语料库]: ../../write-introduction/corpus/tensions/01-despite-progress-unaddressed.md
[入库动作]: none / append_variant / create_new_file
[变体类型名]: "[如入库动作为 append_variant，给新变体起一个描述性名称，如'制度冲突型（lehman2014型）']"
[原文锚定句]: "[如入库动作非 none，提取原文中能代表该变体的 1-2 个关键句，供 Phase 4.6 写入 corpus 文件]"
[来源段落]: "[如入库动作非 none：作者_年份 (期刊), P[段落号]——从 Phase 1 module_map 的 paragraph_range 提取]"
[关键特征列表]: "[如入库动作非 none：列出 2-4 个使该变体与已有变体不同的特征。每个特征一个短句，聚焦说服机制和标志性语言，如'用 regulatory shock 而非 efficiency logic 建立共识'、'以问题收束双段而非在同一段内完成转折']"
[适用情境]: "[如入库动作非 none：什么研究情境下选这个变体而非其他变体？如'适用于有具体监管事件/政策冲击的研究场景'、'Incommensurability × Constructs 组合；ASQ 标志性双段 Hook 结构']"
[使用禁忌]: "[如入库动作非 none：使用该变体时的注意事项，如'不要在没有充分文献回顾的情况下使用'、'反例必须有具体数据/案例支撑']"

# Prose Craft 标注（Ch03）—— 新增于 v2.1.0
[prose_craft]:
  human_face:
    actor_present: true/false
    actor_name: "[具体 actor，如 Toyota/14条生命/具体公司名]"
    actor_location: "[在骨架中的槽位位置]"
  showing_vs_telling:
    concrete_illustration_paired: true/false
    illustration_type: "[案例/数字/场景/具体研究]"
    illustration_location: "[在骨架中的槽位位置]"
  conversational_voice:
    active_voice: true/false
    subject_verb_pattern: "[We argue that... / Consider... / 具体场景开头]"
    avoids_passive: true/false
```

### Incommensurability 反过拟合抽象

对该类范文，先使用 `../../write-introduction/references/incommensurability-introduction-routing.md` 的 L0–L3 profile，再提炼骨架：

1. 先写 L0 功能摘要，不看原句是否“漂亮”。
2. 用 R1–R4 标记 resolution operator；route 只缩小检索范围。
3. 将模块排列、揭示时机和对话配置标为 L2 tactic；只有它改变说服动作时才可成为新变体。
4. 将段落数、案例、比喻、具体理论和期刊修辞标为 L3；L3 只能作原文锚点。
5. 运行 leave-one-paper-out、minimal-sufficient abstraction、counterexample tolerance、route stability 与 functional novelty 五项测试。

若骨架只能复现来源论文而不能迁移到另一篇同路由论文，降为 L3；若在多篇论文中复现但不是跨路由必要功能，保留为 L2 optional variant；只有跨路由反复出现的功能才可提出 L0 核心候选。

### 语料库感知比对（Corpus-Aware Comparison）

> **核心原则**：在标记 `[入库动作]` 之前，必须读取目标 corpus 文件，将新骨架与已有变体逐一比对。不读文件就标记"新变体" = 可能重复入库。

**比对流程**：

1. **定位目标文件**：根据 `[对应语料库]` 字段确定目标 corpus 文件路径
   - 如果该路径的文件**不存在** → 这是一个全新模板，`[入库动作]` = `create_new_file`，跳过后续步骤
   - 如果文件**存在** → 进入步骤 2

2. **读取已有变体**：读取目标 corpus 文件，提取所有已有变体的句法模板（`**模板**:` 后的文本）

3. **逐变体相似度比对**：将新提炼的骨架（`[骨架]` 字段）与每个已有变体的句法模板进行功能相似度比较。比对标准（按优先级）：

   | 比对维度 | 权重 | 判断方法 |
   |---------|------|---------|
   | **说服动作** | 最高 | 两个变体完成的是否为同一说服动作？（如都在做"共识建立→反例颠覆"） |
   | **句法结构** | 高 | 核心句式是否同构？（如都是 "According to X... In reality, however..."） |
   | **槽位类型** | 中 | 占位符的类型和数量是否接近？（如都有 [consensus] + [anomaly] + [resolution hint]） |
   | **措辞层面** | 低 | 具体用词是否雷同？（措辞相似不重要——功能相似才重要） |

4. **判定入库动作**：

   | 比对结果 | `[入库动作]` | 说明 |
   |---------|-------------|------|
   | 与某个已有变体功能相似度 ≥ 70% | `none` | 该骨架已被 corpus 覆盖——记录匹配到的变体编号（如"匹配已有变体 C"） |
   | 与所有已有变体功能相似度 < 70% | `append_variant` | 这是已有 canonical_id 的新变体——填写 `[变体类型名]` 和 `[原文锚定句]` |
   | 目标文件不存在（新 canonical_id） | `create_new_file` | 这是 corpus 中没有的全新模板——还需填写 `[变体类型名]` |

   对 Incommensurability 增加一项覆盖规则：若差异只来自 L3 paper signature，强制 `none`；若是 L2 tactic 但说服动作未改变，匹配最近变体并记录确认性证据，不新建 subtype。

5. **记录比对证据**：在 Phase 2.2 输出中附一句比对摘要（不输出给用户，供 Phase 4.6 使用）：
   ```
   [比对摘要]: 与已有变体 C（效率逻辑→现实反驳型）说服动作重叠但句法结构不同（本变体用 regulatory shock 而非 efficiency logic 建立共识）→ append_variant
   ```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类 Gap 所需）
- Gap 变体（同类骨架在不同 Gap 类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题
- **对应语料库**：如该骨架与 `../../write-introduction/corpus/` 中的 canonical 模板对应，标注路径
- **入库动作**：
  - `none` = 该骨架已被已有变体覆盖，无需入库（默认值）
  - `append_variant` = 该骨架是已有 canonical_id 的新变体，Phase 4.6 将追加到对应 .md 文件
  - `create_new_file` = 该骨架属于 corpus 中不存在的全新 canonical_id，Phase 4.6 将创建新 .md 文件
- **变体类型名**（仅 `append_variant`/`create_new_file` 时填写）：给新变体起一个描述性名称，格式为 "[变体中文描述]（[来源论文]型）"，如 "监管冲击型（darby2024型）"
- **原文锚定句**（仅 `append_variant`/`create_new_file` 时填写）：提取原文中能代表该变体的 1-2 个关键句，保留原文措辞，供 Phase 4.6 写入 corpus 文件的 `**原文锚定**` 字段
- **来源段落**（仅 `append_variant`/`create_new_file` 时填写）：从 Phase 1 `module_map.[module].paragraph_range` 提取。格式：`作者_年份 (期刊), P[段落号]`。供 Phase 4.6 写入 `**来源**` 字段
- **关键特征列表**（仅 `append_variant`/`create_new_file` 时填写）：2-4 个短句，每个聚焦一个使该变体**与已有变体不同**的特征。聚焦说服机制和标志性语言——不重复模板本身的描述。供 Phase 4.6 写入 `**关键特征**` 字段
- **适用情境**（仅 `append_variant`/`create_new_file` 时填写）：1-2 句说明什么研究情境下选这个变体而非其他变体。包括 Gap×Contribution 组合偏好、期刊适配、数据/方法前提。供 Phase 4.6 写入 `**适用**` 字段
- **使用禁忌**（仅 `append_variant`/`create_new_file` 时填写）：1-2 句说明使用该变体时的注意事项。如 Phase 2.4 批评家发现了已知风险，优先记录。如无已知禁忌，填写 "暂无"。供 Phase 4.6 写入 `**禁忌**` 字段

### 2.3 Rhetorical Logic 提炼

提取该 Introduction 如何处理三类修辞/说服问题：

| 修辞问题 | 提炼问题 | 对应 Dorobantu 问题 |
|----------|----------|---------------------|
| Audience Alignment | 如何建立 common ground？如何暗示目标受众？术语是否与该社群一致？ | "Which audience should find your research interesting?" |
| Puzzle-Gap-RQ 层次 | 是否从 broad puzzle 收窄到 specific RQ？过渡是否自然？ | "What broad management question? What specific question?" |
| Contribution Contract | 贡献声明是否可被全文兑现？是否存在 overclaiming？ | "How does answering your RQ advance prior research?" |

输出格式：
```yaml
phase_2_distillation:
  hook:
    persuasive_action: "兴趣锚定"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (10/28)"
        abstraction_level: "L0 / L1 / L2 / L3"
        incommensurability_route_fit: "R1 / R2 / R3 / R4 / cross-route / n.a."
        paradigm_exclusivity: "Incompleteness 专用"
        gap_variants: ["Inadequacy 版本", "Incommensurability 版本"]
        dorobantu_question: "Why is this puzzle important?"
        corpus_path: "../../write-introduction/corpus/hooks/06-paradigm-challenge.md"
        enrichment_action: "none / append_variant / create_new_file"
        variant_name: "[如 append_variant: '监管冲击型（darby2024型）']"
        original_anchor: "[如 append_variant: '原文关键句...']"
        source_location: "[如 append_variant: 'darby2024 (MSOM), P2']"
        key_features: ["[特征1]", "[特征2]", "[特征3]"]
        applicability: "[如 append_variant: '适用于有具体监管事件/政策冲击的研究场景']"
        taboos: "[如 append_variant: '反例必须有具体数据/案例支撑']"
        comparison_summary: "[如 append_variant: '与已有变体 C 说服动作重叠但句法结构不同 → append_variant']"
    rhetorical_logic:
      audience_alignment: "..."
      puzzle_gap_rq_layering: "..."
      contribution_contract: "..."
  # ... 其余模块
```

### 2.4 骨架批评家（Skeleton Critic）—— 生成力验证

借鉴 paper_factory Step 2 的 critic-verdict 循环：每个 Phase 2.2 提炼出的骨架必须经过**生成力验证**，才能进入 Phase 3。

**验证流程**：

1. **占位符填充测试（Generativity Test）**
   - 将骨架中的 `[占位符]` 填入该论文的具体内容（现象名、构念名、理论名）
   - 生成一个"模拟段落"
   - 对比模拟段落与原文段落：是否保留了相同的**说服动作**？
   - 如果填入后生成的段落与原文功能等价 → 通过；如果丢失了关键说服动作 → REVISE

2. **事实污染检查（Fact-Boundary Test）**
   - 骨架中是否嵌入了该论文特有的机构名、政策名、数据库名？
   - 是否使用了仅适用于该行业的术语？
   - 如果有 → REVISE，泛化为 `[empirical setting]` / `[policy]` / `[source]`

3. **Gap 类型匹配检查（Type-Fidelity Test）**
   - 骨架的标志性语言是否与判定的 Gap 类型匹配？
   - 例如：Incompleteness 骨架中出现了 "conflated" → REJECT（语言错配）

**批评家裁决格式**：

```yaml
phase_2_4_skeleton_critic:
  skeleton_id: "tension_incompleteness_opening"
  verdict: "VALIDATED / REVISE / REJECT"
  verdict_reason: "..."
  generativity_test:
    mock_paragraph_generated: true/false
    persuasive_action_preserved: true/false
    notes: "..."
  fact_boundary_test:
    paper_specific_contamination: ["机构A", "政策B"]
    contamination_cleared: true/false
  type_fidelity_test:
    gap_type_match: true/false
    mismatch_details: "..."
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **VALIDATED** | 三项测试全部通过 | 骨架进入 Phase 3 和 Phase 4 |
| **REVISE** | 生成力或事实边界测试未通过，但可通过改写修复 | 标记为 "needs_revision"，在 Phase 4 中尝试改写后重新验证 |
| **REJECT** | Gap 类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库 |

**注意**：批评家裁决记录存入 `vault_enrichment` 的 `rejected_skeletons` 或 `validated_skeletons`，供 Phase 4 跨论文聚合使用。

### 批量检查点：写入轻量摘要（仅 --batch 模式）

> **目的**：将当前论文的核心蒸馏数据以轻量格式写入 `_batch_state.yaml`，使 Phase 4 聚合时无需重新加载完整上下文。

**触发条件**：当前运行标记为 `--batch` 模式。

**执行时机**：Phase 2.4 完成后、Phase 3 开始前（此时骨架已验证，数据最可靠）。

**写入内容**：从 Phase 0-2.4 输出中提取以下字段，追加到 `../../write-introduction/corpus/_batch_state.yaml`：

```yaml
- paper_id: "[从 Phase 0 paper_id 提取]"
  status: "distilled"
  combo: "[gap_type] × [contribution_dimension]"
  gap_type: "[Phase 0]"
  incommensurability_route: "[R1 / R2 / R3 / R4 / unclassified / n.a.]"
  route_confidence: "[high / medium / low / n.a.]"
  contribution_dimension: "[Phase 0]"
  hook_canonical_id: "[Phase 2.2 对应语料库字段中提取的 canonical_id]"
  tension_canonical_id: "[同上]"
  conversation_strategy: "[Phase 0]"
  hook_energy: "[Phase 0: 低/中/高]"
  narrative_structure: "[Phase 0]"
  module_sequence: "[Phase 1 actual_module_sequence 简化：standard / theory_lens_first / stakes_embedded]"
  tension_depth: "[Phase 3 DNA 指标，如已计算；否则 Phase 1.5 stakes_stress_test 推断]"
  stakes_specificity: "[Phase 3 DNA 指标，如已计算；否则 Phase 1.5 stakes_stress_test 推断]"
  has_explicit_puzzle: "[Phase 0]"
  has_stakes_paragraph: "[Phase 1.5]"
  paragraph_count: "[Phase 1 实际段落数]"
  module_ratios: {hook: N, literature_turn: N, tension: N, stakes: N, theory_lens: N, preview: N, contribution: N}
  tone: "[Phase 3 Narrative Style Profile Tone 的主语气]"
  distinctive_features: ["[Phase 3 Distinctive Feature 1]", "[Phase 3 Distinctive Feature 2]"]
  avoids: ["[Phase 3 Avoid 1]", "[Phase 3 Avoid 2]"]
  weakest_aspect: "[Phase 3 Quality Markers weakest_aspect]"
  vault_profile_path: "[Fine-Grained Profile 的 Vault 存储路径]"
```

同时更新 `combos_accumulator.[combo]` 的累积字段（追加 paper_id、hook_id、tension_id、module_sequence、tone、module_ratios、distinctive_features、avoids）；Incommensurability 论文还要累计 route、route confidence、L0 invariant 候选、L2 tactic 与 L3 signature，三层不得混合计数。

**写入方式**：Read `_batch_state.yaml` → 定位 `papers` 列表末尾 → Edit 追加新条目 → 更新 `combos_accumulator` → 更新 `papers_processed` 和 `last_updated`。

**非批量模式**：如果当前运行**未**标记 `--batch`，跳过此步骤，直接进入 Phase 3。

---
