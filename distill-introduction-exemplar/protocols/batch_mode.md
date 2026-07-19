# 批量模式上下文管理（Incremental Batch Strategy）

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：--batch 调用时先读本文件；单篇模式可跳过。

---

## 批量模式上下文管理（Incremental Batch Strategy）

> **路径基准**：本文件中 `academic-writing-corpus/...` 路径指**兄弟技能** `write-introduction` 的语料库，即 `../write-introduction/academic-writing-corpus/...`（与 `_update_registry.py` 的路径解析一致）；`protocols/...` 等相对路径以本 SKILL.md 所在目录为基准。

> **问题**：30 篇论文 × 每篇 7 个模块的骨架 → 上下文窗口无法同时持有。Phase 4 跨论文聚合不能依赖内存中的数据。
> **方案**：每篇论文蒸馏完成后，将其**轻量摘要**持久化到 `academic-writing-corpus/_batch_state.yaml`。Phase 4 只读取这个摘要文件做聚合，不依赖上下文中的原始蒸馏数据。

### 批量工作流

```
Session N: 处理论文 1-5（或用户指定的任意数量）
  For each paper:
    Phase 0→1→2→2.4 → 产出 Fine-Grained Profile（完整，存 Vault）
                    → 产出轻量摘要（写入 _batch_state.yaml，仅 15 行/篇）
  Phase 4 不运行（等待所有论文处理完毕）

Session N+1: 处理论文 6-10
  读取 _batch_state.yaml → 了解已完成论文的 combo 分布
  同上流程，追加轻量摘要

... 所有论文处理完毕后 ...

Final Session: Phase 4 聚合
  读取 _batch_state.yaml（不读任何原始蒸馏数据）
  → 执行跨论文模式验证
  → 执行 Phase 4.5/4.6 入库
```

### 轻量摘要格式（_batch_state.yaml）

每篇论文仅需 ~15 行 YAML，只包含 Phase 4 聚合需要的字段：

```yaml
batch_id: "batch_YYYY-MM-DD"
status: "in_progress"
total_papers_target: [用户指定的总数，如未知则 null]
papers_processed: N
last_updated: "YYYY-MM-DD"

papers:
  - paper_id: "darby2024"
    status: "distilled"  # distilled / pending / skipped
    combo: "Incompleteness × Mechanism"
    gap_type: "Incompleteness"
    contribution_dimension: "Mechanism"
    hook_canonical_id: "03-data-shock"
    tension_canonical_id: "01-despite-progress-unaddressed"
    conversation_strategy: "Progressive Coherence"
    hook_energy: "低"
    narrative_structure: "线性收缩"
    module_sequence: "standard"  # standard / theory_lens_first / stakes_embedded
    tension_depth: 3
    stakes_specificity: "高"
    has_explicit_puzzle: true
    has_stakes_paragraph: true
    paragraph_count: 6
    module_ratios: {hook: 15, literature_turn: 25, tension: 20, stakes: 10, theory_lens: 12, preview: 10, contribution: 8}
    tone: "cautious"
    distinctive_features: ["quantified stakes with government data", "three-reason论证法"]
    avoids: ["overclaiming causality"]
    weakest_aspect: "Stakes could be more specific — uses 'theoretically important' without quantification"
    vault_profile_path: "D:/OneDrive/.../darby2024_distilled_introduction.md"

combos_accumulator:
  "Incompleteness × Mechanism":
    paper_ids: ["darby2024", "eilert2017", "mayo2021"]
    hook_ids: ["03-data-shock", "07-cost-benefit-tension", "08-consequence-cascade"]
    tension_ids: ["01-despite-progress-unaddressed", "01-despite-progress-unaddressed", "08-cost-vs-benefit"]
    module_sequences: ["standard", "standard", "stakes_embedded"]
    tones: ["cautious", "assertive", "cautious"]
    module_ratios_accumulator: [{hook: 15, ...}, {hook: 18, ...}, ...]
    distinctive_features_accumulator: [["quantified stakes", ...], [...], ...]
    avoids_accumulator: [["overclaiming causality"], [...], ...]
```

### 操作规则

**开始批量处理时**：
1. 检查 `academic-writing-corpus/_batch_state.yaml` 是否存在
   - 存在且 `status = in_progress` → 询问用户：继续未完成的批量任务还是开始新批次？
   - 不存在或 `status = completed` → 创建新 `_batch_state.yaml`，`batch_id` 使用当前日期
2. 如果用户用 `--combo-filter` 缩小范围，在 `_batch_state.yaml` 中记录过滤条件

**每篇论文蒸馏完成后（Phase 2.4 之后）**：
1. 从 Phase 0-2.4 的输出中提取轻量摘要字段
2. 追加到 `_batch_state.yaml` 的 `papers` 列表
3. 更新 `combos_accumulator` 中对应 combo 的累积字段
4. `papers_processed += 1`，`last_updated` 更新为当前日期
5. 用 Edit 或 Write 工具写回 `_batch_state.yaml`

**所有论文处理完毕后（Phase 4 执行时）**：
1. 读取 `_batch_state.yaml`（这是 Phase 4 聚合的**唯一数据源**——不从上下文中读取原始蒸馏数据）
2. 从 `combos_accumulator` 中提取每个 combo 的聚合数据
3. 执行 Phase 4 原有的跨论文模式验证逻辑
4. 完成后将 `status` 更新为 `completed`

**跨 Session 恢复**：
- 每次启动 distill 时检查 `_batch_state.yaml`
- 如果 `status = in_progress` 且 `papers_processed < total_papers_target`，告知用户进度并询问是否继续
- 用户可以从任意论文开始继续处理（通过 `--combo-filter` 或直接指定论文）

### 上下文窗口安全边界

| 操作 | 同时持有的论文数 | 每篇上下文中数据 |
|------|----------------|----------------|
| 单篇蒸馏（Phase 0→2.4） | 1 篇 | 完整 Introduction 文本 + 完整骨架 |
| 检查点写入 | 1 篇 | 仅 ~15 行 YAML 摘要 |
| Phase 4 聚合 | 0 篇原始数据 | 仅读取 `_batch_state.yaml`（30 篇 × 15 行 = 450 行 YAML，远低于上下文限制） |
| Phase 4.5/4.6 入库 | 0 篇原始数据 | 基于 Phase 4 聚合输出 + corpus_enrichment |

**安全原则**：Phase 4 聚合**永远不**同时持有原始蒸馏数据。如果 `_batch_state.yaml` 不存在或不完整，先运行单篇蒸馏补全，再运行 Phase 4。

---
