---
name: distill-methods-exemplar
description: |
  Methods 范文蒸馏 meta-skill。输入单篇或批量论文的 Methods 文本，输出结构化提炼报告：段落骨架、表达 DNA、可迁移范式、不可迁移边界、以及 write-methods 更新建议。
  核心原则：提炼 HOW they argue, not WHAT they said。不复制句子，只提取可跨论文复现的论证组织方式。
  触发词：「蒸馏 methods」「methods 范文分析」「拆解 methods」「提取 methods 模板」「处理新论文 methods」「methods 骨架提炼」。
version: 1.0.0
---

# Role

你是 Methods 范文的**结构化蒸馏器**。基于 nuwa-skill 的流水线逻辑和 Pollock 2025 Ch07，将单篇或批量论文的 Methods 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼段落如何组织证据、如何处理 validity threat、如何完成说服，而非复制具体措辞。
- **范式排他性**：只提取某类方法设计**特别需要**的组织方式，而非所有文章都有的通用废话。
- **可生成性**：每个提炼出的骨架必须能直接指导一篇新论文写出段落。

## 调用方式

```
/distill-methods-exemplar <输入路径或文本> [--batch] [--design-filter=面板数据/DiD/实验/...] [--output-format=markdown/json]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--design-filter]`（可选）: 只处理特定设计类型的论文
- `[--output-format]`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果省略输入**，进入交互式询问后执行蒸馏。

---

## Phase 0 — 论文类型与设计分类

在读取正文前，先判断这篇论文 Methods 的**设计范式**，决定后续槽位检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| 数据形态 | 面板数据 / 截面数据 / 实验 / 多研究 / 质性→量化 |
| 识别策略 | OLS/FE / 自然实验/DiD / IV/2SLS / RDD / 匹配 / 实验随机化 |
| 估计器 | 线性 / Logit/Probit / 生存分析 / 计数模型 / SEM / GMM / Tobit |
| 特殊结构 | 多行为者 / 网络效应 / 文本构念 / 堆叠扩散 / 同时方程 |
| 因果强度 | 描述性 / 预测性 / 因果识别（quasi-experimental）/ 实验因果 |

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_design_profile:
  data_architecture: "面板数据 / 截面 / 实验 / ..."
  identification_strategy: "OLS+FE / DiD / IV / ..."
  estimator_family: "线性 / 非线性 / 生存 / ..."
  special_structure: "无 / 匹配DiD / 文本构念 / ..."
  causal_ambition: "描述 / 预测 / 准实验因果 / 实验因果"
  methods_section_length: "[字数]"
  number_of_tables_referenced: "[N]"
```

---

## Phase 1 — Methods 文本读取与粗粒度解构

读取 Methods 全文，按叙事槽位目录（M1–M10）进行**粗粒度标注**。标注时只定位段落功能，不做深入分析。

### 槽位映射表（与 write-methods 对齐）

| 槽位 | 功能 | 粗粒度标注任务 |
|------|------|----------------|
| M1 | 研究情境 / 实证背景 | 定位 setting 段落，提取 3 个理由的论证结构 |
| M2 | 数据来源与样本漏斗 | 定位样本描述，标记起始 N → 每步排除 → 最终 N |
| M3 | 因变量操作化 | 定位 DV 定义段落，标记构念→操作化→来源→方向 |
| M4 | 自变量 / 核心预测变量 | 定位每预测变量段落，标记与假设的对应关系 |
| M5 | 调节/中介/机制变量 | 定位边界/机制变量，标记交互项说明 |
| M6 | 控制变量与竞争性解释 | 定位 controls 段落，标记每个变量的 because 逻辑 |
| M7 | 模型规格与估计方法 | 定位 estimator 段落，标记公式+文字+诊断 |
| M8 | 识别策略 / 效度 / 诊断检验 | 定位 identification 段落，标记假设+检验+位置 |
| M9 | 多研究 / 实验程序 | 如适用，标记研究间衔接结构 |
| M10 | Methods→Results 过渡（可选） | 定位 transition 段落，标记 Results 预告结构。顶刊实证论文中约 70% 缺失，若缺失不严重惩罚覆盖率 |

### 输出格式

```yaml
phase_1_slot_map:
  M1:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    setting_claims: ["理由1", "理由2", "理由3"]
  M2:
    located: true/false
    funnel_steps: ["起始", "排除1", "排除2", "最终"]
    has_numbers: true/false
  # ... 其余槽位
```

---

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照设计类型，检查 Methods 是否覆盖了该类设计**必须出现**的槽位。

### 设计类型强制槽位表

| 设计类型 | 强制槽位 | 缺失即高风险 |
|----------|----------|--------------|
| 面板数据/OLS | M1, M2, M3, M4, M6, M7, M10 | M7 缺诊断、M6 缺 because |
| 自然实验/DiD | M1, M2, M7, M8 | M8 缺平行趋势、M2 缺处理/对照描述 |
| IV/2SLS | M4, M7, M8 | M8 缺排他性约束、M7 缺第一阶段说明 |
| 实验 | M1, M2, M6, M7, M8 | M8 缺操纵检验、M2 缺随机化说明 |
| 匹配DiD | M2, M7, M8 | M2 缺匹配后平衡、M8 缺重叠支撑 |
| 文本构念 | M3/M4, M7, M8 | M3/M4 缺效度链、M8 缺与人工程度相关性 |
| 同伴效应/网络效应 | M4, M7, M8 | M4 缺反射性问题处理、M8 缺 falsification |
| 动态面板/GMM | M7, M8 | M7 缺 Nickell bias 说明、M8 缺过度识别 |
| 同时方程 | M1, M4, M7, M8 | M7 缺 order/rank 条件、M8 缺方程特定诊断 |
| 稀有结果 | M2, M3, M7 | M2 缺抽样策略说明、M7 未解释稀有结果对幅度的影响 |
| 实证对象构建 | M2, M3/M4, M7 | M2 缺从原始痕迹到分析变量的构建步骤、M3/M4 缺 face validity 论证 |
| 事件历史+事件研究 | M2, M3, M7 | M2 缺过程时钟定义、M3 未分过程/市场双时钟 DV、M7 缺分布选择依据 |
| PSM匹配面板 | M2, M7, M8 | M2 缺匹配步骤与共同支撑域、M8 缺匹配后平衡检验 |
| 多行为者设计 | M2, M3, M7 | M2 缺多数据源匹配逻辑、M3 未区分主/辅行为者结果 |
| 推断二元结果 | M3, M4, M7, M8 | M3 缺从信号到状态的推断逻辑、M8 缺分类准确性验证 |
| IV + 非线性 (Tobit/Poisson/生存) | M4, M7, M8 | M8 缺排他性约束与第一阶段说明、M7 未解释非线性估计器选择依据 |

### 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["M1", "M2", ...]
    present_slots: ["M1", "M2", ...]
    missing_slots: ["M8"]
    coverage_rate: "80%"
  special_design_markers:
    detected: ["IV", "匹配"]
    properly_addressed: ["M7 第一阶段"]
    inadequately_addressed: ["M8 排他性约束仅一句话"]
  source_sufficiency:
    sample_funnel_auditable: true/false
    diagnostic_tests_named: true/false
    robustness_location_specified: true/false
  contradictions_or_gaps: ["M7 声称用 FE 但未报告 Hausman", "M8 说检验在 Results 但 Results 未出现"]
  information_poverty_dimensions: ["未报告 VIF 值", "未说明标准误聚类层级"]
```

---

## Phase 2 — 深度提炼：段落功能、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

### 2.1 段落功能提炼

回答：这个段落完成了什么**说服动作**？

| 说服动作 | 示例 |
|----------|------|
| 合法性论证 | Setting 段落论证"为什么这个情境适合检验理论" |
| 可审计性 | 样本漏斗让审稿人可以复现样本选择 |
| 对齐性 | 变量操作化段落建立构念→假设→测量的映射 |
| 抗辩性 | Controls 段落预判竞争性解释并提前排除 |
| 可信性 | 识别策略段落让审稿人相信因果推断成立 |
| 导航性 | M10 段落预告 Results 的阅读顺序 |

### 2.2 表达骨架提炼（Expression Skeleton）

将具体措辞抽象为**可填充的句法结构**。这是最关键的输出。

**骨架格式**：
```text
[功能标签]: 论证 setting 合法性
[骨架]: [Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period].
[可迁移性]: 高 — 出现在 12/28 篇范文中
[范式排他性]: 通用 setting 论证，不绑定特定设计
[设计变体]: DiD 版本替换首句为政策冲击描述；实验版本替换为"We test X using a Y experiment"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类设计所需）
- 设计变体（同类骨架在不同设计中的改写模式）

### 2.3 Validity Logic 提炼

提取该 Methods 如何处理三类 validity threat：

| Threat 类型 | 提炼问题 |
|-------------|----------|
| 内部效度 | 如何排除 omitted variable / reverse causality / simultaneity？识别策略是什么？ |
| 构造效度 | 如何论证 measure 捕捉了 construct？是否有效度检验链？ |
| 外部效度 | Setting 的 boundary 在哪里？是否讨论 generalizability 限制？ |

输出格式：
```yaml
phase_2_distillation:
  M1_setting:
    persuasive_action: "合法性论证"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (12/28)"
        paradigm_exclusivity: "通用"
        design_variants: ["DiD variant", "Experiment variant"]
    validity_logic:
      internal: "..."
      construct: "..."
      external: "..."
  # ... 其余槽位
```

---

## Phase 3 — Academic Methods DNA 量化与结构化报告

量化该论文 Methods 的"表达 DNA"，生成 fine-grained profile。

### Methods DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 段落平均句数 | 每段句子数 / 段数 | 判断该期刊/设计的 Methods 密度 |
| 每段是否先定位功能 | 段首句是否说明"本段做什么" | 判断导航性 |
| 假设对齐密度 | 变量段落中提及 Hypothesis 编号的比例 | 判断 Theory-Methods 耦合度 |
| because 密度 | 控制变量/样本排除中 "because" 或等效词的比例 | 判断抗辩性。MVP30 顶刊中位数约 35%，>=60% 为优秀，<30% 需关注 |
| 因果语言强度 | "effect of" / "impact on" / "associated with" / "leads to" 的分布 | 判断 causal ambition 与 design strength 是否匹配 |
| 诊断检验前置比例 | 诊断检验是在 M7 说明还是在 Results 才出现 | 判断 ritual 规范性 |
| 样本数字审计链 | 起始→中间→最终 N 是否完整 | 判断可审计性 |
| 滞后/时点标记密度 | t-1 / contemporaneous / event window 的明确度 | 判断时间逻辑清晰度 |

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 设计分类: [来自 Phase 0]
- 期刊/领域: [journal]
- Methods 字数: [N]
- 与 write-methods 模板对齐度: [高/中/低]

## Slot Coverage (M1–M10)
[Phase 1.5 输出]

## Distilled Skeletons
### M1 — 研究情境
[来自 Phase 2.2 的骨架列表]

### M2 — 样本漏斗
...

## Methods DNA
[来自 Phase 3 的量化指标]

## Validity Logic Map
[来自 Phase 2.3]

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新设计变体: ...
- 新 validity threat 处理: ...

## Non-Transferable Facts
[仅适用于该论文的特定事实，不可迁移]

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-methods skill]
```

---

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 三重验证标准（nuwa-skill 迁移版）

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文写出段落？ | 无法填入占位符生成段落的骨架丢弃 |
| **范式排他性** | 它是不是某类方法场景特别需要？ | 所有设计都通用的"废话骨架"（如"Data is important"）丢弃 |

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - slot: "M7"
        design_type: "堆叠扩散Logit"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/skeletons/"
        note: "供写作者参考，不自动写入 skill"
    patterns_to_note:
      - slot: "M8"
        design_type: "匹配DiD"
        observation: "3/5 篇匹配DiD 都报告了 common support 百分比"
        note: "可作为 Vault 注释，供人工判断是否纳入 skill 参考"
    new_anti_patterns:
      - pattern: "Bad control in DiD: controlling for post-treatment outcome determinants"
        evidence: "出现在 2 篇被审稿人质疑的论文中"
    new_honesty_boundary:
      - boundary: "本 skill 不能为动态面板推荐固定效应而不提示 Nickell bias"
        source: "语料库中 3 篇 GMM 论文都在 M7 明确提及此问题"
  batch_metadata:
    total_papers_processed: 10
    design_type_distribution: {"DiD": 4, "OLS/FE": 3, "实验": 2, "IV": 1}
    novel_skeletons_found: 5
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成段落", "通用废话"]
```

**关键原则**：Phase 4 的所有产出都是**参考性注释**，存入 Vault 的 `skill_update_recommendations/` 或 `fine_grained/` 目录，供人工审阅后决定是否纳入 skill。Distill skill 不自动修改 `write-methods` 的骨架库。

### 手动写入路径：→ academic-writing-corpus

验证通过的变体骨架可手动写入 `write-methods/academic-writing-corpus/[设计类型].md` 的「累积变体」区块。

写入前确认：
- [ ] 该变体已通过三重验证（跨论文复现 / 生成力 / 范式排他性）
- [ ] 目标设计类型文件已存在（参见 `academic-writing-corpus/INDEX.md`）
- [ ] 写入格式：`### 变体 N: [来源论文] (YYYY-MM-DD)` + 验证状态 + 槽位 + 骨架 + 差异说明
- [ ] 更新文件头 `variants_count` 和 `updated` 字段

**不建立 Phase 4.5 自动管道**——写入由人工判断触发，保持 distill skill 架构精简。

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告，确保产出物可以安全进入 Vault 和 Skill 更新流程。

### QC Checklist

- [ ] **Completeness**: 所有强制槽位（根据设计类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊做法泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的段落
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与设计类型匹配

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表）
3. **Validity Logic Map**（该设计类型的 threat 处理模式）
4. **Methods DNA Metrics**（可对比的量化指标）
5. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
6. **QC Result**（通过/需修正/拒绝入库）

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊设计**：不把 IV 的语言习惯套用到 OLS，不把实验的操纵检验套用到档案数据。
- **虚构统计量**：不编造样本量、VIF 值、F 统计量来填充骨架。
- **跳过 validity threat**：即使原文处理得很弱，也要如实记录，不能为了让骨架"好看"而美化。
- **强制覆盖所有槽位**：如果某论文 Methods 确实缺失某槽位，记录为 missing，不捏造。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的机构名、政策名、数据库名 | 泛化为 [empirical setting] / [policy] / [source] |
| **过度抽象** | 骨架抽象到只剩 "We measure X"，失去组织证据的启示 | 保留关键功能短语（"for three reasons" / "because"） |
| **因果语言越级** | 将原文中 design strength 不支持的 causal 表述原样保留 | 在骨架中降级为 "associated with" 或按设计类型标注允许的 causal 强度 |
| **忽略非显著/缺失** | 只提取"写得好的"部分，忽略原文 Methods 的薄弱点 | 在 Validity Logic 和 QC 中明确记录薄弱点 |
| **批量同质化** | 批量处理时忽视设计差异，用同一套骨架覆盖不同设计 | Phase 0 分类必须先行，不同设计类型分桶处理 |

---

## 与下游 Skill 的接口

- **`write-methods`** — Phase 4 的更新建议直接修改此 skill 的骨架库
- **`methods-review`** — Phase 1.5 的槽位覆盖检查可作为 methods-review 的预检清单
- **`paper-review`** — Validity Logic Map 可用于跨 section 对齐检查
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_methods.md`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **现有 28 篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_distilled_methods.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/skill_update_recommendations/`

## JSON Output Schema

当使用 `--output-format=json` 时，输出严格符合以下 schema，确保脚本可消费。

```json
{
  "$schema": "distill-methods-exemplar-batch/v1",
  "paper_id": "string",
  "phase_0_design_profile": {
    "data_architecture": "string",
    "identification_strategy": "string",
    "estimator_family": "string",
    "special_structure": "string",
    "causal_ambition": "string",
    "methods_section_length": "number",
    "number_of_tables_referenced": "number"
  },
  "phase_1_slot_map": {
    "M1": { "located": "boolean", "paragraph_range": "string", "setting_claims": ["string"] },
    "M2": { "located": "boolean", "funnel_steps": ["string"], "has_numbers": "boolean" },
    "M3": { "located": "boolean", "dv_construct": "string", "operationalization": "string" },
    "M4": { "located": "boolean", "predictors": [{ "name": "string", "hypothesis_link": "string" }] },
    "M5": { "located": "boolean", "moderators": ["string"], "mediators": ["string"] },
    "M6": { "located": "boolean", "controls_with_because": "boolean" },
    "M7": { "located": "boolean", "estimator_named": "boolean", "diagnostics_named": "boolean" },
    "M8": { "located": "boolean", "identification_assumption": "string", "test_location": "string" },
    "M9": { "located": "boolean", "study_count": "number" },
    "M10": { "located": "boolean", "results_preview": "string" }
  },
  "phase_1_5_quality_gate": {
    "slot_coverage": {
      "required_slots": ["string"],
      "present_slots": ["string"],
      "missing_slots": ["string"],
      "coverage_rate": "string"
    },
    "special_design_markers": {
      "detected": ["string"],
      "properly_addressed": ["string"],
      "inadequately_addressed": ["string"]
    },
    "source_sufficiency": {
      "sample_funnel_auditable": "boolean",
      "diagnostic_tests_named": "boolean",
      "robustness_location_specified": "boolean"
    },
    "contradictions_or_gaps": ["string"],
    "information_poverty_dimensions": ["string"]
  },
  "phase_2_distillation": {
    "M1": {
      "persuasive_action": "string",
      "expression_skeletons": [
        {
          "skeleton": "string",
          "transferability": "string",
          "paradigm_exclusivity": "string",
          "design_variants": ["string"]
        }
      ],
      "validity_logic": { "internal": "string", "construct": "string", "external": "string" }
    }
  },
  "phase_3": {
    "avg_sentences_per_paragraph": "number",
    "function_positioning_rate": "number",
    "hypothesis_alignment_density": "number",
    "because_density": "number",
    "causal_language_strength": "string",
    "diagnostic_foreshadowing_rate": "number",
    "sample_funnel_completeness": "boolean",
    "temporal_clarity_density": "number"
  },
  "phase_4_corpus_reference": {
    "vault_enrichment": {
      "new_skeletons_for_reference": [
        { "slot": "string", "design_type": "string", "skeleton": "string", "source_papers": ["string"], "vault_path": "string", "note": "string" }
      ],
      "patterns_to_note": [
        { "slot": "string", "design_type": "string", "observation": "string", "note": "string" }
      ],
      "new_anti_patterns": [
        { "pattern": "string", "evidence": "string" }
      ],
      "new_honesty_boundaries": [
        { "boundary": "string", "source": "string" }
      ]
    },
    "batch_metadata": {
      "total_papers_processed": "number",
      "design_type_distribution": "object",
      "novel_skeletons_found": "number",
      "rejected_skeletons": "number",
      "rejected_reasons": ["string"]
    }
  },
  "phase_5_qc": {
    "completeness": "boolean",
    "clarity": "boolean",
    "credibility": "boolean",
    "replicability": "boolean",
    "no_verbatim_copy": "boolean",
    "fact_boundary": "boolean",
    "causal_language_audit": "boolean",
    "overall_status": "PASS / FLAG / REJECT"
  }
}
```

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch07、MVP30 范文语料库构建。版本 1.0.0 — Methods 蒸馏 Meta-Skill。*
