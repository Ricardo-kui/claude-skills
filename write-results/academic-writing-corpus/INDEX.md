---
corpus: write-results
description: Results 填空骨架变体库，按结果类型组织。由 distill-results-exemplar 验证通过后，定性内容手动写入 .md 文件，定量证据由 _update_registry.py 自动同步到 _evidence_registry.yaml。
organization: by_result_type
result_types_count: 15
created: 2026-05-18
updated: 2026-05-22
---

# Results Academic Writing Corpus

## 组织逻辑

按结果类型组织。每个文件包含：
1. **主骨架引用** — 指向 `write-results/SKILL.md` 中的对应模板
2. **累积变体** — 由 `distill-results-exemplar` Phase 4 手动写入的验证通过变体（定性内容：句法模板、反模式提醒、关键特征）

**定量证据注册表**：`_evidence_registry.yaml`
- 记录每个骨架变体的 `paper_count`、`status`（EMERGING/VERIFIED/ROBUST）、`subfield_distribution`
- 由 `distill-results-exemplar/_update_registry.py` 自动消费 `corpus_enrichment` 块后更新
- `write-results` 调用时优先推荐 `status: ROBUST` 的骨架

## 结果类型索引

| 文件 | 结果类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [OLS-FE](OLS-FE.md) | OLS-FE | 5 | 2026-05-20 |
| [Logit-Probit-Ordered-Probit](Logit-Probit-Ordered-Probit.md) | Logit-Probit-Ordered-Probit | 0 | 2026-05-18 |
| [生存分析](生存分析.md) | 生存分析 | 5 | 2026-05-20 |
| [DiD](DiD.md) | DiD | 0 | 2026-05-18 |
| [计数模型](计数模型.md) | 计数模型 | 3 | 2026-05-20 |
| [实验](实验.md) | 实验 | 0 | 2026-05-18 |
| [多研究](多研究.md) | 多研究 | 0 | 2026-05-18 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 3 | 2026-05-20 |
| [匹配DiD](匹配DiD.md) | 匹配DiD | 0 | 2026-05-18 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 0 | 2026-05-18 |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 0 | 2026-05-18 |
| [跨受众构念对比](跨受众构念对比.md) | 跨受众构念对比 | 0 | 2026-05-18 |
| [三向交互](三向交互.md) | 三向交互 | 0 | 2026-05-18 |
| [构造暴露分解](构造暴露分解.md) | 构造暴露分解 | 0 | 2026-05-18 |

## Registry 设计说明

`_evidence_registry.yaml` 是 results 侧的**定量证据注册表**，与 introduction 侧的 `_evidence_registry.yaml` 对应但结构不同。

### 核心差异（Results vs Introduction）

| 维度 | Results Registry | Introduction Registry |
|------|-----------------|----------------------|
| 顶层索引 | `estimator_family`（16 种结果类型） | `gap_type × contribution_dimension` |
| 二级索引 | `slot`（R1–R9） | `module`（hook, tension, stakes...） |
| 骨架粒度 | 槽位级 + 句式级（四拍节奏、威胁句式） | 模块级（段落功能） |
| 状态判定 | paper_count + 跨子领域分布 | paper_count + 跨 journal |
| 刚性 | 高（R1→R9 顺序基本固定） | 低（模块排列灵活） |

### Schema 结构

```yaml
meta:
  schema_version: "1.0.0"
  registry_type: "estimator-slot-skeleton"
  last_updated: "YYYY-MM-DD"
  last_batch_id: "batch_YYYY-MM-DD"
  batches_processed: N
  total_papers_indexed: N
  subfields: [strategy, ob_hr, om, marketing, finance, accounting]

status_rules:
  EMERGING:  { paper_count_max: 2, description: "..." }
  VERIFIED:  { paper_count_min: 3, description: "..." }
  ROBUST:    { paper_count_min: 5, cross_subfields_min: 2, description: "..." }

global_anti_patterns:     # 全局反模式清单
global_honesty_boundaries: # 全局诚实边界

estimators:
  OLS_FE:
    display_name: "OLS / Fixed Effects"
    forced_slots: ["R1", "R2", "R3", "R7"]
    high_risk_missing:
      R1: "缺诊断检验"
      R3: "缺经济显著性"
    slots:
      R3:
        description: "主假设检验（四拍节奏）"
        skeleton_variants:
          - id: "r3_ols_four_beat_standard"
            skeleton: "..."
            paper_count: 15
            status: ROBUST
            subfield_distribution: { strategy: 5, ob_hr: 4, ... }
            sources: ["Smith_2021_SMJ"]
            transferability: "high"
            paradigm_exclusivity: "OLS/FE 专用"
            rhythm_tags: ["direction", "significance", "magnitude", "support"]
            notes: "..."
            corpus_path: "academic-writing-corpus/OLS-FE.md"
    cross_slot_patterns:  # 跨槽位过渡句式
    anti_patterns:        # estimator 级反模式
    honesty_boundaries:   # estimator 级诚实边界

batch_history: []
```

### 状态机

- **EMERGING** (≤2 篇): 单篇或两篇中出现，可作为实验性参考
- **VERIFIED** (≥3 篇): 稳定复现，可作为可靠备选
- **ROBUST** (≥5 篇 + 跨 ≥2 子领域): 跨领域验证，可作为默认骨架

### 更新机制

由 `distill-results-exemplar/_update_registry.py` 自动消费 `corpus_enrichment` YAML 块：

```bash
python _update_registry.py /path/to/corpus_enrichment.yaml [--dry-run]
```

- `--dry-run`: 预览变更但不写入
- 自动备份：每次运行前创建 `.backup_YYYYMMDD_HHMMSS`
- 支持 action: `create_new` / `append_skeleton_or_increment` / `increment_count`

### 写入规则

1. 仅 `distill-results-exemplar` Phase 4 验证通过的变体可写入 `.md` 文件（定性内容）
2. `_evidence_registry.yaml` 中的定量证据（paper_count、status、subfield_distribution）由 `_update_registry.py` 自动更新
3. 每个变体标注来源论文、验证状态、写入日期
4. 不覆盖现有变体，仅追加
5. 变体达到 3+ 时（VERIFIED），考虑提升为 skill 主骨架；达到 5+ 跨领域（ROBUST）时，优先作为默认推荐

## 语料库质量状态

> ✅ **2026-05-20 更新**: 五篇产品召回论文 Results 蒸馏完成，首批 16 个变体写入。
>
> **已填充结果类型**: 4/15 (OLS-FE, 生存分析, 计数模型, IV-2SLS)
> **核心骨架 (4/5 复现)**: AFT 四拍 + exponentiated beta (生存分析 变体1)
> **高频可选 (2-3/5)**: AFT 交互效应五拍、叙事型稳健性检验、Event Study→CAR 第二阶段
> **单篇高价值 (1/5)**: Shape parameter 前置、分组检验+小样本诚实、Table 9 矩阵、Quartile penalty、MCMC mediation、竞争假设报告、model-free 预览、IV 诊断嵌入
>
> **总变体数**: 16 (分布于 4 个结果类型文件)
