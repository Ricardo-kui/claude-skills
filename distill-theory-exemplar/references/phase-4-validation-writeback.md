# Phase 4: validation and writeback

> **写回前必跑预检（2026-08-20 起）**：候选骨架定稿后、读取任何语料前，运行
> `python ../distill-paper-exemplar/scripts/corpus_precheck.py --section <本节名> --citekey <citekey> --candidates <candidates.yaml>`
> 产出 writeback plan（选带判定 + jaccard/containment 查重 + registry 定点匹配 + insert_after 锚点）。
> **禁止为查重/选带/锚点定位而整读 corpus 或 `_evidence_registry.yaml`**（单个文件可达 54–257KB）——
> 一切以 plan 为准；仅当 plan 的 verdict 可疑时，才允许按 plan 标注的文件+行号定点核对。
>
> candidates.yaml 格式：
> ```yaml
> candidates:
>   - name: <skeleton_id>
>     target: "<目标文件或目录提示，如 OLS-FE.md / tensions>"
>     skeleton_text: "<骨架模板文本（查重输入）>"
>     keywords: ["<registry 匹配关键词，可选>"]
> ```
>
> **--auto-write**：默认仍需 gate ① 人审确认 plan 后写回；调用方显式传 `--auto-write`
> （或批量模式用户预先授权）时，可按 plan 直接写回 ADD/EXTEND 项（**SKIP 项永不写回**），
> 并在写回报告中标注 `auto-write: plan <plan路径>`。
>
> **整篇编排模式（distill-paper-exemplar 分发）下**：plan 产出即停，把 plan 路径交回
> 主循环等待批量 gate ①（四节攒齐一次呈审），不要自行进入写回；单节模式随产随审。
>
> **写回执行（gate ① 确认后，2026-08-20 起）**：用确定性执行器，不手改语料——
> `python ../distill-paper-exemplar/scripts/corpus_writeback.py --plan <plan> --paper <citekey> --journal <刊名> --gap <Gap类型>`（block_text/index_note 已在 candidates.yaml 写一遍并透传进 plan，无需 blocks.yaml）
> 默认 dry-run 打印全部 diff 供复核，`--apply` 才落盘（插块自动续 `{NEXT}` 编号、
> _index 行注、registry 计数、SKIP 拒绝）。gate ① 改判锚点文件时在 blocks.yaml 加
> `file:` 覆盖。完整 blocks.yaml 格式与示例见
> `../../distill-introduction-exemplar/references/phase-4-validation-writeback.md` 头部。
>
> **`_update_design_feedback.py` 输入 schema**：observations 必填
> `defect_id / classification / current_rule / target / diagnosis`；papers 必须嵌在
> `evidence:` 下（`evidence.papers: [{id, journal, evidence_anchor, evidence_quality}]`，
> quality ∈ full_text_verified|functional_summary|metadata_only）；非 corpus_gap 类另需
> `rule_excerpt` + `regression_cases`。先 `--dry-run` 再实写。

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 五重验证标准（nuwa-skill 迁移版）

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个模块写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文组装出对应功能模块？ | 无法填入占位符生成模块的骨架丢弃 |
| **范式排他性** | 它是不是某类构建类型特别需要？ | 所有构建类型都通用的"废话骨架"（如"Theory is important"）丢弃 |
| **故事忠实度** | 它是否让 central knot 更紧并保持角色与 storyline 一致？ | `story_fidelity.classification = reject` |
| **抽象层级正确** | 它是跨路线 L0、路线级 L1、可选 L2，还是单篇模型签名 L3？ | L3 进入核心/路由，或仅因 H 数量、变量图、方程不同而新建架构，均拒绝 |

### 构建类型模式聚合分析

```yaml
phase_4_batch_analysis:
  build_type_distribution: {"机制推演型": 8, "构念辨析型": 4, "假设树型": 3, "质性过程理论型": 2}
  incommensurability_route_distribution: {"R1": 2, "R2": 1, "R3": 4, "R4": 3, "hybrid": 1, "unclassified": 1}
  cross_route_reasoning_invariants: ["[跨 R1-R4 复现的 L0 推理功能]"]
  route_specific_architectures: {"R1": ["[L2 architecture]"], "R2": [], "R3": [], "R4": []}
  model_signature_only: ["[不得推广的 L3 特征]"]
  module_sequence_patterns:
    standard_sequence: "T1→T2→T3→T4→T5→最后假设自然收敛进入 METHODS (10/17)"
    with_independent_t6: "T1→T2→T3→T4→T5→独立 T6 段落→METHODS (1/17, 非管理学标准)"
    theory_first: "T2→T1→T3→T4→T5→最后假设 (4/17, 均为构念辨析型)"
    boundary_embedded: "T5 嵌入 T3 (3/17)"
  closure_strategies:
    local_convergence_only: "12/17 — 管理学标准做法"
    embedded_framework_summary: "3/17 — 嵌入最后假设段末尾的 2-3 句框架总结"
    discussion_opening_compensation: "2/17 — Theory 无框架总结，Discussion 开篇整合"
  why_chain_patterns:
    dominant_by_type:
      机制推演型: "两步因果链 (6/8)"
      构念辨析型: "差异化维度×后果 (4/4)"
      假设树型: "主效应→条件化分支 (3/3)"
  hypothesis_derivation:
    therefore_per_hypothesis_avg: 1.2
    derivation_jumps: 3
  protagonist_concentration:
    high: 12
    medium: 3
    low: 2
  novel_findings:
    - "假设树型论文 3/3 在 T3 中使用 'not uniform; rather' 引入 moderator"
    - "构念辨析型 4/4 使用 'Whereas A..., B...' 对比句式"
  rejected_patterns:
    - "'Based on prior research, we hypothesize...' 无 why chain (3 篇)"
    - "T3 只有 citation list 无机制推演 (2 篇)"
  micro_move_patterns:
    full_sequence_rate: "12/17"
    most_common_missing_move: "Gap/Puzzle (4/17)"
    dominant_anchor_source: "empirical_finding (10/17)"
  bilateral_argumentation:
    complete: "8/10 — 调节型论文同时论证 high/low"
    incomplete: "2/10 — 只论证增强方向"
  arrangement_patterns:
    Warrant-Embedded: "10/17"
    Cumulative: "4/17"
    Evidence-Contrast: "2/17"
    Parallel: "1/17"
  evidence_typology:
    empirical_finding_avg: "55%"
    theoretical_argument_avg: "30%"
    boundary_condition_avg: "10%"
    negative_evidence_avg: "3%"
    analogical_evidence_avg: "2%"
  evidence_function_distribution:
    support: "70%"
    qualify: "15%"
    contrast: "10%"
    pave: "4%"
    rebut: "1%"
  citation_function_match_avg: "78%"
  write_theory_constraint_alignment:
    C10_interaction_pattern_clear: "9/10"
    C20_bilateral_argumentation: "8/10"
    C18_moderator_selection_framework: "5/7"
  corpus_health_analysis:
    coverage_by_build_type:
      机制推演型:
        existing_skeletons: 8
        recommended_new: 2
        gaps: ["反直觉 Anchor 模式", "间接调节论证模板"]
      假设树型:
        existing_skeletons: 3
        recommended_new: 4
        gaps: ["多 moderator 元框架", "基线机制→条件分叉过渡"]
      构念辨析型:
        existing_skeletons: 5
        recommended_new: 0
        gaps: []
      调节效应型:
        existing_skeletons: 4
        recommended_new: 3
        gaps: ["完整双边论证模板", "common trunk + parallel branches 组织"]
    coverage_by_subprotocol:
      argumentation_patterns: {existing: 5, recommended_new: 3, gaps: ["理论驱动型 Anchor", "反直觉 Gap 构造"]}
      arrangement_patterns: {existing: 4, recommended_new: 2, gaps: ["Parallel 复杂假设组织", "Cumulative 间接调节组织"]}
      evidence_patterns: {existing: 3, recommended_new: 3, gaps: ["案例作为 Warrant", "制度逻辑作为证据"]}
      bilateral_argumentation_templates: {existing: 1, recommended_new: 3, gaps: ["high/low 完整双边", "条件连接词组合"]}
      moderator_selection_frameworks: {existing: 1, recommended_new: 2, gaps: ["environmental/organizational 二元框架", "2×2 resource source 框架"]}
    priority_queue:
      - rank: 1
        pattern: "多 moderator 选择元框架"
        corpus_path: "../corpus/subprotocols/moderator_selection_frameworks.md"
        urgency: "高"
        reason: "假设树型/调节效应型论文普遍需要，但 corpus 中模板不足"
        suggested_source_papers: ["Shen_etal_2022_JOM"]
      - rank: 2
        pattern: "间接调节/Mediated Moderation 论证"
        corpus_path: "../corpus/subprotocols/argumentation_patterns.md"
        urgency: "高"
        reason: "复杂假设论文需要，但当前缺少独立理论论证模板"
        suggested_source_papers: ["Singh_Grewal_2023_JMR"]
      - rank: 3
        pattern: "完整双边论证句法"
        corpus_path: "../corpus/subprotocols/bilateral_argumentation_templates.md"
        urgency: "中"
        reason: "C20 要求，多篇调节型论文有优质模板可沉淀"
        suggested_source_papers: ["Shen_etal_2022_JOM"]
    over_represented:
      - pattern: "两步中介机制"
        count: 12
        note: "已足够丰富，新蒸馏可不再优先收录"
      - pattern: "独立 T6 Closure 段落"
        count: 1
        note: "非管理学标准，应持续标记为反模式"
```

### 跨 Section 对齐检查（Phase 4 正式化，v1.2.0 新增）

与 write-theory Phase 4.3（跨 Section 对齐检查）对齐，执行 Introduction ↔ Theory 的强制对齐检查：

```markdown
### 跨 Section 对齐检查

| 维度 | 检查项 | Introduction 信号 | Theory 状态 | 结论 |
|------|--------|-------------------|-------------|------|
| Gap→Type | 能量匹配 | [Gap类型] + [Tension] | [构建类型] | ✅/⚠️/❌ |
| Makadok→Module | 贡献兑现 | [Makadok维度] | [模块覆盖] | ✅/⚠️/❌ |
| Preview→H | 假设数 | "[N] hypotheses" | [实际N个] | ✅/⚠️/❌ |
| Lens→Lens | 理论一致性 | "[theory]" | "[theory]" | ✅/❌ |
| Knot→T1/T2 | Knot 继承 | [central_knot_statement] | [knot_inheritance_statement] | ✅/⚠️/❌ |
| Characters→T1 | 角色一致性 | [protagonist] + [supporting] | [Theory 中出场次数] | ✅/⚠️/❌ |
| T6→Results | 框架总结与 Results 一致 | [框架总结内容 / 无] | [Results 发现方向] | ✅/⚠️/❌ |

**必须修复的不一致**（如为单篇蒸馏，记录为模仿风险提示）：
- [ ] [具体不一致项1]
- [ ] [具体不一致项2]
```

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - module: "T3"
        build_type: "假设树型"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/theory_skeletons/"
        note: "reference candidate；满足授权、证据与去重门槛时可受控写入 corpus"
    patterns_to_note:
      - module: "T1"
        build_type: "构念辨析型"
        observation: "4/4 篇使用 'Whereas...' 对比句式定义两个构念"
        note: "可作为 Vault 注释，验证构念辨析型 T1 表达模式"
    new_anti_patterns:
      - pattern: "T4 使用 'Based on prior research, we hypothesize' 无 therefore"
        evidence: "出现在 3 篇论文中，均被 reviewer 质疑 why chain"
    new_honesty_boundary:
      - boundary: "本 skill 不得为机制推演型推荐单步 why chain"
        source: "语料库中机制推演型使用单步的 0/8 篇"
  batch_metadata:
    total_papers_processed: 10
    build_type_distribution: {"机制推演型": 5, "构念辨析型": 3, "假设树型": 2}
    novel_skeletons_found: 4
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成模块", "通用废话"]
```

**关键原则**：Phase 4 同时产生 reference-corpus 建议与设计反馈。`section_variant` / `ritual_only` 可受控写入 reference corpus；`core_candidate` 先进入设计缺陷注册表。只有满足 `design-feedback-loop.md` 的证据、授权、风险和双回归门槛，才可做有边界核心修订；schema、stage gate 和高风险变更始终显式审核。

**Incommensurability 专属原则**：细分类提高推理比较和架构检索精度，不降低核心规则证据门槛。L2 即使达到 VERIFIED/ROBUST 也默认保持 route-specific optional architecture；只有跨路线复现且通过设计反馈门控的 L0 reasoning function 才可成为普遍核心候选。L3 model signature 永不晋升。

### 证据注册表回写（`write-theory/corpus/_evidence_registry.yaml`）

当一个模式实际写入 write-theory corpus（reference-level 变体或经审核的 core candidate）时，必须同步登记注册表——语料入库而未登记，等同于模式丢失（注册表曾是孤儿文件，2026-07-28 才接线）：

1. **登记来源**：在 `source_papers` 下添加论文条目（`作者_年份_期刊` 键），含 display_name / journal / year / subfield / theory_build_type。写作工艺书（非实证论文）额外标注 `source_tier: "auxiliary"`。
2. **登记 fragment**：每个入库模式一个 `tfr_NNN`（沿用全表最大编号递增），含 type / title / home_files / makadok_dimension / status。
3. **定状态**：按 `status_rules`——1–2 来源 = EMERGING，3+ = VERIFIED，5+ 且跨 2 子领域 = ROBUST。auxiliary 来源单独永远停在 EMERGING，只登记出处。
4. **更新 patterns 聚合**：若该模式已有 patterns 条目，追加 source_papers 并升级 status；没有则新建。
5. **更新 meta**：`last_updated`、`total_papers_indexed`、`batches_processed`，并在 `note` 追加一行批次摘要（蒸馏了哪篇、加了什么模式、有无纠正误分类）。
6. **检查 `next_batch_targets`**：若新论文命中某个目标模式，更新 current_sources/papers_needed；凑齐即在批次摘要中宣告状态升级。

---

## Phase 4.6 — Reference 回写提醒

> 回写提醒的完整清单见 `../protocols/writeback_reminders.md`。reference-level 变体服从 corpus 证据门槛；core candidate 不走 reference 回写通道。

**索引/路由表同步（2026-08-09 闭环补丁）**：写入 corpus 文件后，必须同步：
1. `write-theory/corpus/meta/routing_table.md`——若新增了理论构建变体类型或路由分支，更新路由表（Gap × 贡献杠杆 → 变体映射）；追加变体不改变路由时不强制
2. `write-theory/corpus/_index.md`——新增/更新模式条目（变体类型、验证状态）。`_index` 与 routing_table 是选材 Gate 的读入源，不同步会导致下轮选材看不到新变体。

## Phase 4.7 — Write-Theory 技能设计反馈

加载 `design-feedback-loop.md` 并执行：

1. 用逐字 `rule_excerpt` 证明目标规则真实存在；已支持的做法只登记 confirming evidence。
2. 区分 `corpus_gap` 与 routing / validator / output-contract / schema / stage-gate defect。
3. 为每个非 corpus 缺陷定义 positive 与 preservation 两个回归案例。
4. 每次输出 `skill_design_feedback`；运行 `_update_design_feedback.py` 持久化到 `write-theory/corpus/_skill_design_feedback.yaml`。
5. 只对 registry 判为 `safe_core_patch_candidate` 或 `conditionalize_candidate` 且通过授权/风险门控的条目实施核心修订。
6. 修订后完成 quick validation、结构检查、双回归和隔离前向测试；`applied` resolution 还必须记录目标中可逐字核验的 `rule_excerpt_after`，并在适用时声明旧绝对规则已经消失，之后才可关闭缺陷。

`corpus_enrichment` 回答“需要增加什么写作资产”；`skill_design_feedback` 回答“当前技能规则是否错误”。两者不得互相替代。

## Phase 4 收尾 — 回写后语料体检

回写完成后运行 skills 根目录的体检脚本：

```bash
PYTHONIOENCODING=utf-8 python ~/.claude/skills/corpus_health_check.py --type theory
```

- exit 0 = 正常；exit 1 = 存在 critique_heavy 类型——在输出中列出这些类型，作为下一轮蒸馏 REPLACE/EXTEND 的优先级依据。
- 脚本缺失或运行失败不阻断回写，但必须在输出中声明"体检未执行"，不得静默跳过。
