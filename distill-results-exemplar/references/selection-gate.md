# Phase 0.75 — 选材 Gate（批评驱动，Skill-SP 启发）

在进入 Phase 1 深读前，用 `write-results/econometric-models/_evidence_registry.yaml` 中该估计器的 `usage_stats` 判断**这篇论文值不值得深蒸馏、优先级多高**。批评由 Claude 在 write-results 会话中自动登记，也可用 `_update_registry.py --record-critique` 批量补登（见 `phase-4-validation-writeback.md` 批评登记）。

## 三带判定（依据 registry meta.usage_stats_schema）

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap**（未覆盖） | 该估计器 slots 相对本文档覆盖存在缺口（静态，不依赖登记） | **HIGH**：ADD 候选，优先深读 |
| **critique_heavy**（批评密集） | `revise + reject >= 2` | **HIGH**：REPLACE/EXTEND 候选，优先对比已有变体质量；`common_revise_reasons` 是精炼的直接依据 |
| **quiet**（无批评） | 其余情况 | MEDIUM：正常蒸馏 |

**明确不做的**：不按使用频率/accepted_rate 淘汰或降级变体——语料是长期写作资产，频繁使用且好用应提升路由权重，而非降级（Skill-SP 语义修正，见 registry `non_signals`）。

## 执行规则

- **单篇论文（用户明确指定蒸馏）**：不拒绝，但必须输出带判定供 Phase 3 新颖度判断参考。
- **批量模式（--batch）**：按带排序（gap/critique_heavy → quiet），优先深读 HIGH 档；资源不足时 quiet 档仅做 Phase 1 粗标注，不进入 Phase 2 深提炼。
- **重复闸门**：Phase 2.2 得出骨架后，若与已有变体（corpus 或 registry）高度重叠，按 SKIP 处理——不为重复模式新增变体（对应 Skill-SP `find_duplicate_skill` 语义）。**重叠判定由 `distill-paper-exemplar/scripts/corpus_precheck.py` 确定性计算**（jaccard ≥ 0.33 或 containment ≥ 0.60 → SKIP），见 phase-4 参考文件头部的预检协议；代理不得整读语料自行比对。

## 输出格式

```yaml
phase_0_75_selection_gate:
  estimator_family: "OLS_FE"
  band: "gap | critique_heavy | quiet"
  evidence:
    revise: 1
    reject: 0
    last_critique: "2026-06-01"
    critique_reasons: ["R3 经济显著性段落缺少幅度翻译"]
  priority: "HIGH | MEDIUM"
  rationale: "1 句话：为什么这篇论文处于该带"
```

## 趋同批评聚合检查（meta-skill 轻量版）

若该估计器 `common_revise_reasons` 中**同一原因出现 ≥2 次**（趋同批评），在 Phase 0.75 输出中追加聚合检查块：

```yaml
phase_0_75_convergent_critique_check:
  estimator_family: "OLS_FE"
  convergent_patterns:
    - pattern: "R3 经济显著性段落缺少幅度翻译"
      count: 2
      last_critique: "2026-08-08"
  aggregation_suggestion: "该模式是否应升级为主骨架级修订（REPLACE 主骨架段落或增加警告行）——由本次蒸馏证据决定，仍走预览-确认 gate"
```

- **批评计数 < 2 时静默**——不输出该块，不预建机制。
- 若本次蒸馏的骨架恰好与该模式相关：Phase 4 的 `skill_update_instructions` 应包含主骨架级修订候选（`skill_main_skeleton_update`），同样先预览后确认。
- 若本次蒸馏的骨架与批评模式无关：聚合建议标记为"待后续蒸馏验证"，不强行修订。
