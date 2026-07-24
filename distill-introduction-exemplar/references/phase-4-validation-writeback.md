# Phase 4: validation and writeback

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 数据来源（批量模式）

> **Phase 4 聚合不从上下文读取原始蒸馏数据。** 唯一数据源是 `../../write-introduction/academic-writing-corpus/_batch_state.yaml`。

**执行前检查**：
1. Read `_batch_state.yaml`，确认 `papers_processed ≥ 2`（至少有 2 篇论文才有聚合意义）
2. 如果文件不存在或 `papers_processed < 2` → 告知用户"批量数据不足，请先蒸馏至少 2 篇论文"，跳过 Phase 4
3. 如果文件存在且数据充足 → 从 `combos_accumulator` 和 `papers` 列表提取聚合数据

**聚合数据提取**：
- `combo_distribution` → 从 `combos_accumulator` 的 key 集合和各 combo 的 `paper_ids` 长度计算
- `module_sequence_patterns` → 从各 combo 的 `module_sequences` 列表统计
- `hook_patterns` / `tension_patterns` → 从各 combo 的 `hook_ids` / `tension_ids` 统计
- `tension_depth` / `stakes_specificity` → 从 `papers` 列表中各论文的对应字段统计
- `novel_findings` → 基于 Phase 2.2 的入库动作（已在 `_batch_state.yaml` 中不可直接获取——需辅以 Phase 2.4 的 VALIDATED skeletons 数据。如果上下文中有当前 Session 处理的论文的 Phase 2 数据，可合并使用；如果没有，仅基于 `_batch_state.yaml` 的 combo 级别模式做聚合，不做 skeleton 级别的 novel_findings）
- `style_profile_enrichment.per_combo_styles` → 从 `combos_accumulator` 的 `tones`、`distinctive_features_accumulator`、`avoids_accumulator`、`module_ratios_accumulator` 聚合计算

**非批量模式**：如果当前运行**未**标记 `--batch`（单篇蒸馏），Phase 4 基于当前论文的 Phase 2-3 数据直接产出 corpus 沉淀建议，不读 `_batch_state.yaml`。

### 四重验证标准

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个模块写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文组装出对应功能模块？ | 无法填入占位符生成模块的骨架丢弃 |
| **范式排他性** | 它是不是某类 Gap×Contribution 组合特别需要？ | 所有组合都通用的"废话骨架"（如"Research is important"）丢弃 |
| **故事忠实度** | 它是否 tie knot、澄清主角或改善 exposition 节奏？ | `story_fidelity.classification = reject` |

### 组合模式聚合分析

```yaml
phase_4_batch_analysis:
  combo_distribution: {"Incompleteness×Mechanism": 5, "Inadequacy×Boundary": 3, ...}
  module_sequence_patterns:
    standard_sequence: "hook→literature_turn→tension→stakes→theory_lens→preview→contribution (12/15)"
    theory_lens_first: "hook→theory_lens→literature_turn→tension→stakes→preview→contribution (2/15, 均为 Incommensurability)"
    stakes_embedded: "tension+stakes 合并 (4/15)"
  hook_patterns:
    dominant_by_gap:
      Incompleteness: "Cold-start definition (6/8)"
      Inadequacy: "Contrast case (4/7)"
      Incommensurability: "Consensus challenge (5/5)"
  tension_depth:
    score_3: 8
    score_2: 5
    score_1: 2
  stakes_specificity:
    high: 10
    medium: 3
    low: 2
  novel_findings:
    - "Inadequacy×Constructs 组合中 3/3 篇使用 'conflated' 类语言"
    - "Incommensurability 论文 100% 在 Tension 中使用反例支撑"
  rejected_patterns:
    - "'Few studies have examined' 出现在 4 篇论文中，全部标记为 generic gap language"
```

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - module: "tension"
        gap_type: "Inadequacy"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/intro_skeletons/"
        note: "供写作者参考，可作为 ../../write-introduction/academic-writing-corpus/tensions/ 新增 canonical 模板的候选"
    patterns_to_note:
      - module: "hook"
        gap_type: "Incommensurability"
        observation: "5/5 篇使用 consensus challenge 型 Hook"
        note: "可作为 Vault 注释，验证 Hook 能量级与 Gap 强度匹配规则"
    new_anti_patterns:
      - pattern: "Tension 使用 'few studies have examined' + Stakes 缺失"
        evidence: "出现在 3 篇 Incompleteness 论文中，均被审稿人质疑增量贡献"
    new_honesty_boundary:
      - boundary: "本 skill 不得将 Incommensurability 的 consensus challenge 骨架推荐给 Incompleteness 组合"
        source: "语料库中 Incompleteness 使用 consensus challenge 的 0/8 篇"
  batch_metadata:
    total_papers_processed: 10
    combo_distribution: {"Incompleteness×Mechanism": 5, "Inadequacy×Boundary": 3, ...}
    novel_skeletons_found: 5
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成模块", "通用废话"]
```

**关键原则**：Phase 4 先输出参考性注释。只有 `section_variant` 或 `ritual_only` 可进入 reference corpus；`core_candidate` 必须显式人工审核，且不得自动修改 SKILL.md、路由、强制模块顺序、story schema 或 stage gate。

> **corpus_enrichment / style_profile_enrichment 两个硬化输出块**的完整 YAML 格式已外置：见 `../protocols/phase4_output_blocks.md`。Phase 4 聚合输出生成时加载。

### Phase 4.5 — 证据注册表更新逻辑

Phase 4 完成后，根据 `corpus_enrichment` 块更新 `../../write-introduction/academic-writing-corpus/_evidence_registry.yaml`：

**状态自动判定规则**：

| 条件 | 新状态 |
|------|--------|
| `paper_count >= 5` 且跨 `>= 2` journals | **ROBUST** |
| `paper_count >= 3` | **VERIFIED** |
| `paper_count <= 2` | **EMERGING** |

**更新步骤**：

1. 将 Phase 4 输出的 `corpus_enrichment` YAML 块保存为临时文件（如 `/tmp/corpus_enrichment.yaml`）
2. 运行本 skill 目录下的自动化工具：
   ```bash
   python _update_registry.py /tmp/corpus_enrichment.yaml
   ```
3. 工具自动完成：
   - 读取 `_evidence_registry.yaml`
   - 对每个 `evidence_updates` 条目：追加 papers、重算 paper_count、按阈值判定 status
   - 应用 `gap_distribution_updates` 和 `anti_pattern_updates`
   - 更新 `meta.last_updated` 和 `meta.batches_processed`
   - 写回注册表

**工具位置**: `_update_registry.py`（与本 SKILL.md 同目录）

**注意**：Phase 4.5 只更新证据注册表的**定量证据**。定性内容（句法模板、关键特征、反模式提醒）由 Phase 4.6 写入 corpus .md 文件。

---

### Phase 4.6 — 语料库文件受控入库

仅将通过 Phase 2.4 且通过 Story-Fidelity Gate 的 reference-level 资产写入 corpus。核心规则变更必须停下并请求人工审核。

#### 执行门控

只有满足以下**全部条件**的骨架才触发文件写入：

| 条件 | 来源 | 说明 |
|------|------|------|
| Phase 2.4 裁决 = VALIDATED | Phase 2.4 skeleton_critic | 三项测试全部通过 |
| Phase 2.2 标记为需入库 | Phase 2.2 `[入库动作]` 字段 | 值为 `append_variant` 或 `create_new_file` |
| 非重复 | 读取目标文件后人工判断 | 新变体与已有变体的模板句法相似度 < 70% |
| Story fidelity | Phase 0.5 | 只能是 `section_variant` 或 `ritual_only` |

**跳过条件**：
- `[入库动作]` = `none` → 该骨架已被已有变体覆盖，跳过
- Phase 2.4 裁决 = REVISE → 标记为待修正，不写入（但记录在 Phase 4.6 摘要的"待修正"栏）
- Phase 2.4 裁决 = REJECT → 不写入
- `core_candidate` → 输出人工审核包，不写文件
- 任何触及 SKILL.md、路由、强制模块顺序、story schema 或 stage gate 的建议 → 不自动执行

#### 操作 A：追加变体到已有模板文件（`append_variant`）

**步骤**：

1. **读取目标文件**：Phase 2.2 `[对应语料库]` 字段指定的路径
2. **确定变体编号**：找到文件中最后一个 `### 变体 [字母]`，使用下一个字母（A→B→...→Z）
3. **组装变体块**：从 Phase 2.2 骨架字段提取数据，按以下格式组装。每个 corpus .md 字段右侧标注了数据来源——**直接从 Phase 2.2 复制，不重新阅读原文**：

```
> **入库 corpus 文件模板**（变体模板、canonical_id 文件模板、风格画像各节、Phase 4.6 入库摘要）已外置：见 `../protocols/corpus_file_templates.md`。Phase 4.6 写入 corpus 文件前加载。
