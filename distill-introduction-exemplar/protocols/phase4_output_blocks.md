# Phase 4 硬化输出块（corpus_enrichment / style_profile_enrichment）

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：Phase 4 聚合输出生成时加载。

---

### corpus_enrichment 硬化输出块

在 Phase 4 输出末尾，**必须附加**以下结构化 YAML 块。这是 distill 与 write-introduction 之间的**硬化接口**——write-introduction 可直接解析此块更新其证据注册表和决策知识：

```yaml
corpus_enrichment:
  batch_id: "batch_YYYY-MM-DD"
  papers_processed: N
  last_updated: "YYYY-MM-DD"

  paper_gaps:
    author_year: "Incompleteness"
    author_year2: "Inadequacy"

  evidence_updates:
    - target: "academic-writing-corpus/tensions/01-despite-progress-unaddressed.md"
      canonical_id: "01-despite-progress-unaddressed"
      module: "tensions"
      action: "append_papers"
      new_papers: ["author_year (journal)"]
      updated_paper_count: N
      new_status: "ROBUST / VERIFIED / EMERGING"

    - target: "academic-writing-corpus/hooks/03-data-shock.md"
      canonical_id: "03-data-shock"
      module: "hooks"
      action: "update_status"
      previous_status: "VERIFIED"
      new_status: "ROBUST"
      reason: "paper_count 从 3 升至 6，跨 ≥3 journals"

    - target: "academic-writing-corpus/tensions/XX-new-template.md"
      canonical_id: "XX-new-template"
      module: "tensions"
      action: "create_new"
      gap_type: "Incompleteness"
      skeleton: "Although [field] research has..."
      source_papers: ["author_year"]
      transferability: "high"
      note: "供写作者参考，可作为新增 canonical 模板的候选"

  gap_distribution_updates:
    - canonical_id: "01-despite-progress-unaddressed"
      gap_distribution: {"Incompleteness": 8, "Inadequacy": 0, "Incommensurability": 0}
      exclusivity_confirmed: true

  anti_pattern_updates:
    - target_module: "stakes"
      gap_type: "Incompleteness"
      pattern: "Incompleteness × Mechanism 中 3/5 论文 Stakes 用 generic 'theoretically important'"
      evidence: ["paper_a", "paper_b", "paper_c"]
      recommended_action: "在 write-introduction Stakes 选择器中为 Incompleteness 增加具体化提醒"

  validation_feedback:
    - canonical_id: "01-despite-progress-unaddressed"
      phase_6_validations: 0
      note: "尚无 Phase 6 验证数据"

  batch_metadata:
    combos_covered: ["Incompleteness×Mechanism", "Inadequacy×Boundary"]
    novel_skeletons_found: N
    rejected_skeletons: N
    rejected_reasons: ["仅出现1次", "不可生成模块", "通用废话", "Gap 类型错配"]
```

**corpus_enrichment 字段说明**：

| 字段 | 用途 | 消费方 |
|------|------|--------|
| `paper_gaps` | 本批次新蒸馏论文的 Gap 类型映射（`paper_id: GapType`） | `_update_registry.py` → 追加到注册表 `paper_index`，驱动 gap_distribution 自动计算 |
| `evidence_updates` | 对现有 corpus 文件的证据更新（新增论文、状态升级、新建模板） | write-introduction 加载时合并到 `_evidence_registry.yaml` |
| `gap_distribution_updates` | 更新某模板在各 Gap 类型中的分布，验证排他性 | write-introduction 决策表（Gap→模板映射） |
| `anti_pattern_updates` | 批量蒸馏发现的常见失败模式 | write-introduction 反模式清单 |
| `validation_feedback` | Phase 6 验证结果 | `_evidence_registry.yaml` validation_history |
| `batch_metadata` | 批量处理元数据 | 注册表 meta 字段 |

**`paper_gaps` 填写规则**：
- 从 Phase 0 `phase_0_combo_profile.gap_type` 提取每篇论文的 Gap 类型
- key = 论文短 ID（如 `darby2024`），value = `Incompleteness` / `Inadequacy` / `Incommensurability`
- 仅填写**本批次新蒸馏**的论文，已在注册表 `paper_index` 中的论文不需要重复

**与 Vault 注释的关系**：`corpus_enrichment` 块是**机器消费**的结构化输出；Phase 4 原有的 `vault_enrichment` 和 `patterns_to_note` 等 YAML 是**人工消费**的参考注释。两者并行产出，不互相替代。

### style_profile_enrichment 硬化输出块

在 Phase 4 输出末尾，**必须附加**以下结构化 YAML 块。这是 distill 与 write-introduction 之间关于**风格数据**的硬化接口——write-introduction 在渲染阶段读取 corpus 文件的 `## 风格画像` 章节时，此块提供跨模板、跨组合的聚合风格数据：

```yaml
style_profile_enrichment:
  batch_id: "batch_YYYY-MM-DD"
  papers_processed: N
  last_updated: "YYYY-MM-DD"

  per_template_styles:
    - canonical_id: "06-paradigm-challenge"
      module: "hooks"
      new_style_contributions:
        tone_additions:
          - tone: "assertive"
            evidence: "[原文证据句]"
            source: "[作者_年份]"
            condition: "适用于 ASQ/ASR 理论颠覆场景"
        distinctive_feature_additions:
          - feature: "[叙事标记描述]"
            example: "[原文例句]"
            source: "[作者_年份]"
        avoid_additions:
          - avoid: "[回避写法]"
            function: "[修辞功能]"
            source: "[作者_年份]"
        quality_marker_updates:
          strongest_aspect: "[如新论文的 strongest_aspect 更具体，则替换]"
          weakest_aspect: "[如新论文发现新的已知风险，则追加]"
        module_ratio:
          hook: N%
          literature_turn: N%
          tension: N%
          stakes: N%
          theory_lens: N%
          preview: N%
          contribution: N%
          source: "[作者_年份]"

  per_combo_styles:
    - combo: "Incommensurability × Mechanism"
      papers_analyzed: N
      dominant_tone: "[该组合最常出现的主语气]"
      tone_distribution: {"assertive": N, "cautious": N, "vivid": N}
      common_distinctive_features:
        - feature: "[跨模板共同出现的叙事标记]"
          prevalence: "[N/N papers]"
      common_avoids:
        - avoid: "[跨模板共同回避的写法]"
          prevalence: "[N/N papers]"
      aggregated_weaknesses:
        - weakness: "[跨论文反复出现的薄弱点]"
          prevalence: "[N/N papers]"
      module_ratio_average:
        hook: N%
        literature_turn: N%
        tension: N%
        stakes: N%
        theory_lens: N%
        preview: N%
        contribution: N%

  anti_pattern_style_updates:
    - pattern: "[风格相关的失败模式，如 'Incompleteness 论文 Tone 偏 cautious 时审稿人倾向质疑增量贡献']"
      evidence: ["[作者_年份]", "[作者_年份]"]
      recommended_action: "[给 write-introduction 的建议]"
```

**style_profile_enrichment 字段说明**：

| 字段 | 用途 | 消费方 |
|------|------|--------|
| `per_template_styles` | 每个模板新增的风格贡献——由 Phase 4.6 操作 C 写入 corpus 文件 `## 风格画像` | write-introduction 渲染阶段读 corpus 文件时获取 |
| `per_combo_styles` | Gap×Contribution 组合级别的聚合风格模式——跨模板的共同特征 | **当前无活跃消费者**（write-introduction v3.3.0 已删除 `_combo_style_profiles.yaml`）。数据仍在 Phase 4 生成，供未来使用 |
| `anti_pattern_style_updates` | 风格相关的失败模式——供反模式清单更新 | write-introduction 反模式检查 |
| `module_ratio_average` | 该组合的平均模块比重 | 当前无活跃消费者。段落结构推荐已由 write-introduction 的 `_routing_tables.yaml` §6 静态覆盖 |

**与 corpus_enrichment 的关系**：
- `corpus_enrichment` → 定量证据（paper_count、status、gap_distribution）→ 进注册表
- `style_profile_enrichment` → 风格数据（tone、rhythm、features、avoids）→ 进 corpus 文件 `## 风格画像` + 供跨模板风格推荐
- 两者在 Phase 4 末尾同时产出，互不替代
