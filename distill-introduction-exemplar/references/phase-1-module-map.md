# Phase 1: module map

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 1 — Introduction 功能模块映射与粗粒度解构

读取 Introduction 全文，按**功能模块**进行粗粒度标注。模块名称与 `write-introduction` 的 `../../write-introduction/academic-writing-corpus/` 目录结构对齐。标注时只定位模块功能边界，不做深入分析。

### 前置步骤：Rhetorical 定位（读范文前的快速语境化）

在进入功能模块映射前，先做一次轻量的 rhetorical 定位（源自 Greene & Lidinsky 2017 Ch02 *rhetorical reading* 的 situation/purpose/claims/audience 四问）。这不替代功能模块映射（那是逆向"怎么写"的骨架），而是先理解范文"为什么这么写"的语境——语境理解能提高后续模块标注的准确性。

快速四问（每问一句话即可，不展开分析）：
- **Situation**：这篇论文回应的学术/现象情境是什么？（哪个对话？哪个谜题？）
- **Purpose**：作者的修辞目的——是改变共识、创建新共识、整合分歧、还是引入新构念？（这预判 Gap 类型与 Makadok 维度）
- **Claims**：核心 claim 是什么类型——fact（经验规律）、value（理论判断/评价）、还是 policy（呼吁行动/方法）？
- **Audience**：隐含读者是谁——该领域专家、跨领域读者、还是实践者？（这影响 hook 能量级与 jargon 密度的判断基准）

> **与功能模块映射的分工**：rhetorical 定位是"理解作者意图"（why），功能模块映射是"逆向写作骨架"（how）。两者顺序执行：先四问理解语境，再映射功能模块。不要用 rhetorical 定位替代模块映射——distill 的产物是可复用骨架，不是文本理解。



### 模块映射表（与 write-introduction 对齐）

| 模块 | 功能 | 识别标准 | 粗粒度标注任务 |
|------|------|----------|----------------|
| **Hook** | 建立兴趣，锚定 Puzzle | 前 1-2 段；呈现 paradox/trend/anomaly/debate | 标记 Hook 类型、能量级、是否直接服务 puzzle |
| **Literature Turn** | 建立文献对话，定位 common ground | 文献回顾段落；呈现 synthesis 而非罗列 | 标记 Conversation 策略（Progressive/Synthesized/Non-Coherence）、核心文献数量 |
| **Tension** | 呈现 Gap / Tension / Departure point | 标志词："however" / "yet" / "despite" / "although" | 标记 Gap 类型语言、是否超越 "few studies"、是否有具体 pain |
| **Stakes** | 论证 Gap 的重要性 (So what?) | 独立段落或嵌入 Tension 末尾；呈现 gain/pain | 标记 Stakes 类型（理论/现象/实践）、是否量化 |
| **Theory Lens** | 引入解释视角 / 理论承诺 | 理论视角引入；标志词："Drawing on..." / "We argue..." | 标记理论来源、是否回应 Tension 的 gap |
| **Preview** | 本文策略/方法/发现预告 | 研究设计简述；假设预告；结果暗示 | 标记 preview 范围（仅方法 vs 方法+发现）、是否过度承诺 |
| **Contribution** | 贡献声明 (Makadok 维度) | 明确声明 "We contribute by..." / "This study is important because..." | 标记 Makadok 维度可见性、是否可被 Discussion 兑现 |

### 跨 Section 对齐检查（需要全文输入）

> **执行门控**：以下检查需要论文的 Theory、Methods、Results 文本。如果输入仅包含 Introduction（如单独的 `_narrative.md` 文件或粘贴的 Introduction 文本），**全部跳过**并标注 `skipped_insufficient_input: true`。仅当输入包含完整论文或明确提供了后续 Section 文本时执行。

在粗粒度解构阶段，**交叉验证 Introduction 与后续 Section 的一致性**：

| 对齐检查项 | 检查位置 | 问题 | 输入要求 |
|-----------|----------|------|---------|
| Theory Lens ↔ Theory Section | Introduction 的理论承诺 vs Theory 的实际理论来源 | 是否一致？是否 Introduction 承诺了制度理论但 Theory 用了 RBV？ | 需要 Theory 章节 |
| Contribution ↔ Theory Hypotheses | Makadok 声明 vs 实际假设 | Contribution 声称 Mechanism 贡献但 Theory 只有主效应无中介？ | 需要 Theory + Hypotheses |
| Contribution ↔ Methods Identification | 识别策略承诺 vs 实际估计器 | Contribution 暗示因果识别但 Methods 只有 OLS/FE？ | 需要 Methods 章节 |
| Preview ↔ Results | 结果预告 vs 实际假设检验 | Preview 暗示发现方向与 Results 系数方向相反？ | 需要 Results 章节 |

**执行规则**：
1. 检查输入类型——若为单个 `_narrative.md` 文件或纯 Introduction 文本 → 设置 `cross_section_alignment_skipped: true`，跳过全部四项检查
2. 若输入包含完整论文 PDF 或各 Section 文本 → 逐项检查，发现矛盾时在 `contradictions_or_gaps` 中记录
3. 若部分 Section 可用（如仅有 Theory 但无 Results）→ 仅检查可用项，其余标记为 `skipped_input_unavailable`

在 Phase 2 Rhetorical Logic 中标记为 "Contribution Contract 风险"（仅当检查实际执行时）。

### 特殊排列记录

记录该 Introduction 是否使用标准模块顺序（Hook→Literature Turn→Tension→Stakes→Theory Lens→Preview→Contribution）或变体：
- **Stakes 前置**: Stakes 在 Tension 之前？（罕见但存在，如以 quantified loss 开场）
- **Theory Lens 前置**: Theory Lens 在 Tension 之前？（Non-Coherence 策略常见，先给新框架再批评旧文献）
- **Preview 嵌入**: Preview 分散在多个模块中？
- **Contribution 分段**: Contribution 分为 2-3 段（常见：理论贡献→实证贡献→实践贡献）

### 输出格式

```yaml
phase_1_module_map:
  hook:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    hook_type: "Cold-start / Trend data / Paradox / Consensus challenge / Immersive narrative / Classic debate / Quote pivot"
    hook_energy_level: "低/中/高"
    serves_puzzle: true/false
  literature_turn:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    conversation_strategy: "Progressive / Synthesized / Non-Coherence"
    core_citations_count: "[N]"
    establishes_common_ground: true/false
  tension:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    gap_type_language: "[标志性语言]"
    beyond_few_studies: true/false
    has_specific_pain: true/false
  stakes:
    located: true/false
    paragraph_range: "[第X段或嵌入tension]"
    stakes_type: "理论 / 现象 / 实践 / 混合"
    quantified: true/false
  theory_lens:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    theoretical_source: "[理论名称]"
    responds_to_gap: true/false
  preview:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    preview_scope: "方法 / 方法+发现 / 方法+理论+发现"
    overclaiming_risk: true/false
  contribution:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    makadok_dimensions_visible: ["Mechanism", "Boundary", ...]
    discussable: true/false
actual_module_sequence: ["hook", "literature_turn", "tension", "stakes", "theory_lens", "preview", "contribution"]
deviation_from_standard: "theory_lens 在 tension 之前 (Non-Coherence 策略); stakes 嵌入 tension 末尾"
```

---
