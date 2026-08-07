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
[对应语料库]: ../../write-introduction/academic-writing-corpus/tensions/01-despite-progress-unaddressed.md
[治理动作]: NONE / REUSE / EXTEND_SOURCE / ADD_REFERENCE / PROPOSE_VARIANT
[最近邻资产 ID]: "[由 introduction_asset_catalog.py 返回的稳定 ID]"
[若合并将损失的生成能力]: "[必须是可迁移写作决策；答不出则 REUSE/EXTEND_SOURCE]"
[变体类型名]: "[仅 ADD_REFERENCE/PROPOSE_VARIANT：描述说服动作，不以领域名词制造类别]"
[原文锚定句]: "[仅作证据，不作为可复用模板长句]"
[来源段落]: "[作者_年份 (期刊), P段落号]"
[适用情境]: "[路由、证据载体、actor/层级/时间结构等边界]"
[使用禁忌]: "[真实性边界与最直接误用风险]"

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

> **核心原则**：先运行 `introduction_asset_catalog.py list-variants --parent <parent_id> --include-all`。新增是最后选项；单篇差异默认只扩展来源或增加 reference，不自动进入生成菜单。

**比对流程**：

1. **定位父策略**：根据 `[对应语料库]` 得到稳定 `parent_id`。父策略不存在时只输出 `PROPOSE_ROUTING_CHANGE` 审核包，不直接创建文件。

2. **检索已有资产**：先看最多 5 个代表性 reference；只有无法判定最近邻时才读取全部历史实例。

3. **能力比对**：比较新骨架与最近邻，而不是计算句法百分比。

   | 比对维度 | 权重 | 判断方法 |
   |---------|------|---------|
   | **说服动作** | 最高 | 两个变体完成的是否为同一说服动作？（如都在做"共识建立→反例颠覆"） |
   | **证据载体** | 高 | 是否要求不同来源类型、actor、层级、时间或比较结构？ |
   | **逻辑转折** | 高 | 共识→遗漏、共识→反例、双流→交叉等关系是否真正不同？ |
   | **句法/领域填充** | 低 | 句式、行业、事件、数字不同本身不构成新能力。 |

4. **判定治理动作**：

   | 比对结果 | `[治理动作]` | 说明 |
   |---------|-------------|------|
   | 完全覆盖 | `REUSE` | 不写 corpus，记录最近邻 |
   | 同一能力、增加跨论文证据 | `EXTEND_SOURCE` | 幂等追加来源，不新增编号 |
   | 单篇但具有有用类比 | `ADD_REFERENCE` | 保持 reference_exemplar，不进默认菜单 |
   | 合并会损失明确的可迁移决策能力 | `PROPOSE_VARIANT` | 只生成审核候选；通过证据门槛后另行 PROMOTE |
   | 只涉及领域词、案例、数字或句法 | `NONE` | 不新建资产 |

   若父策略已有 5 个 active generative variants，任何 `PROPOSE_VARIANT` 必须同时给出 merge/replacement 方案。Incommensurability 的 L3 paper signature 强制 NONE/ADD_REFERENCE；L2 tactic 未改变说服动作时使用 EXTEND_SOURCE。

5. **记录比对证据**：在 Phase 2.2 输出中附一句比对摘要（不输出给用户，供 Phase 4.6 使用）：
   ```
   [比对摘要]: 最近邻 hooks:03-data-shock:vC；差异仅为行业事件与数字 → REUSE
   ```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类 Gap 所需）
- Gap 变体（同类骨架在不同 Gap 类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题
- **对应语料库**：如该骨架与 `../../write-introduction/academic-writing-corpus/` 中的 canonical 模板对应，标注路径
- **治理动作**：默认 `NONE`/`REUSE`/`EXTEND_SOURCE`；单篇独特实例最多 `ADD_REFERENCE`；`PROPOSE_VARIANT` 不自动晋升。
- **最近邻与能力损失**：所有非 NONE 动作必须填写稳定资产 ID；ADD_REFERENCE/PROPOSE_VARIANT 必须具体说明合并会损失的能力。
- **证据与边界**：记录来源段落、可迁移功能、适用边界和禁忌；原文锚点只用于核验，不复制为模板。

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
        corpus_path: "../../write-introduction/academic-writing-corpus/hooks/06-paradigm-challenge.md"
        governance_action: "NONE / REUSE / EXTEND_SOURCE / ADD_REFERENCE / PROPOSE_VARIANT"
        nearest_neighbor_id: "hooks:06-paradigm-challenge:vA"
        capability_loss_if_merged: "[NONE，或具体的可迁移决策能力]"
        variant_name: "[仅 ADD_REFERENCE/PROPOSE_VARIANT]"
        original_anchor: "[仅作证据核验]"
        source_location: "darby2024 (MSOM), P2"
        key_features: ["[特征1]", "[特征2]", "[特征3]"]
        applicability: "[路由与证据前提]"
        taboos: "[真实性边界]"
        comparison_summary: "[最近邻 + 能力裁决 + 治理动作]"
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

**写入内容**：从 Phase 0-2.4 输出中提取以下字段，追加到 `../../write-introduction/academic-writing-corpus/_batch_state.yaml`：

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
