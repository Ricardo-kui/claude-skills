# Phase 1.5: coverage

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 1.5 — 模块覆盖检查与叙事质量摘要

这是质量控制检查点。对照 Gap × Contribution 组合，检查 Introduction 是否覆盖了该组合**必须出现**的模块。

### Stakes 边缘案例压力测试（grill-me 场景探测模式）

对 Stakes 模块执行具体化压力测试，验证其重要性论证是否经得起边缘场景追问：

| 测试问题 | 通过标准 | 失败信号 |
|---------|----------|----------|
| 如果这个问题不解决，**具体会发生什么**？ | 能描述一个具体的理论后果或实践事件 | "影响理论发展" / "填补文献空白"（generic） |
| 哪类读者会因为不知道这个答案而**做出错误决策**？ | 能指出具体的学术或实践群体 | "所有研究者" / "企业管理者"（过于宽泛） |
| 现有文献的遗漏是否导致了**可观察的负面结果**？ | 有现象层面的证据或反例 | 只有 "需要更多研究" 的空洞声明 |
| Stakes 是否能用 **一句话** 概括？ | 能在 25 词内说清 why this matters | 需要整段才能勉强说清 |

**测试方式**：为每篇论文的 Stakes 模块发明 1-2 个反事实场景，追问 "如果该 gap 被填满/不被填满，具体差异是什么？"

### 组合强制模块表

| Gap 类型 | Contribution 维度 | 强制模块 | 缺失即高风险 |
|----------|------------------|----------|--------------|
| Incompleteness | Mechanism | Hook, Literature Turn, Tension, Stakes, Theory Lens, Preview, Contribution | Tension 缺 "theoretically important because"、Stakes 缺失 |
| Incompleteness | Constructs | Hook, Literature Turn, Tension, Theory Lens, Contribution | Theory Lens 缺构念辨析框架、Tension 缺 "conflated" 类语言 |
| Inadequacy | Mechanism | Hook, Literature Turn, Tension, Stakes, Theory Lens, Preview, Contribution | Tension 缺具体文献批评、Stakes 缺 theory cost |
| Inadequacy | Boundary | Hook, Literature Turn, Tension, Theory Lens, Contribution | Theory Lens 缺边界条件论证、Tension 缺 "when" 类遗漏 |
| Incommensurability | Mechanism | Hook, Literature Turn, Tension, Stakes, Theory Lens, Preview, Contribution | Hook 能量级不足（必须用 Consensus challenge）、Tension 缺反例支撑 |
| Incommensurability | Constructs | Hook, Literature Turn, Tension, Theory Lens, Contribution | Tension 缺对立理论并置、Theory Lens 缺新构念区分框架 |
| Incommensurability | Question | Hook, Literature Turn, Tension, Theory Lens, Contribution | Literature Turn 缺对话双方完整呈现、Tension 缺 "both views are incomplete" |
| Phenomenon | Any | Hook, Literature Turn, Stakes, Theory Lens, Preview, Contribution | Hook 缺现象重要性建立、Literature Turn 可以极短（新现象） |
| Level | Any | Hook, Literature Turn, Tension, Theory Lens, Contribution | Tension 缺跨层次张力、Theory Lens 缺层次桥接理论 |
| Mode | Any | Hook, Literature Turn, Tension, Theory Lens, Contribution | Tension 缺 variance/process 张力、Theory Lens 缺新 lens 合法性 |

### Prose Craft 检查（Pollock 2025 Ch03）

对每个模块执行三层 prose 质量检查，提取可模仿的 prose 策略：

#### 1. Human Face 检查

| 检查点 | 通过标准 | 失败信号 | 蒸馏记录 |
|--------|---------|---------|---------|
| Hook 有具体 actor | P1 出现 ≥1 个人名/公司名/机构名 | "many firms" / "some scholars" | 记录具体 actor 名称和出现位置 |
| 共识引用有脸 | `[dominant finding]` 槽位引用具体论文（作者名）而非 "many scholars" | 用 "prior research has shown" 无具体引用 | 记录引用策略 |
| 反例有脸 | `[anomaly]` 槽位包含具体案例或数字 | "some studies found" | 记录案例/数字来源 |
| 每个 context 有脸 | `[context 1/2/3]` 各含具体研究（作者+年份+情境） | 三个 context 来自同一篇 review | 记录 context 来源多样性 |

#### 2. Showing vs Telling 检查

| 检查点 | 通过标准 | 失败信号 | 蒸馏记录 |
|--------|---------|---------|---------|
| Major construct 首次出现配 illustration | 每个核心构念首次出现时跟 1 个例子/数字/场景 | 连续 2+ 句纯抽象描述 | 记录 illustration 类型和位置 |
| Gap statement 配场景 | `[gap statement]` 解释遗漏原因后跟 1 个"如果不解决会怎样"的场景 | 只有 "few studies have examined" | 记录场景具体内容 |
| Theory consequence 具体化 | `[theoretical consequence]` 具体到某理论的某 prediction | "theoretically important" 无解释 | 记录具体化策略 |
| Mechanism 可操作化 | `[mechanism]` 用可操作化构念命名 | "the role of X" 模糊表达 | 记录构念命名方式 |

#### 3. Conversational Voice 检查

| 检查点 | 通过标准 | 失败信号 | 蒸馏记录 |
|--------|---------|---------|---------|
| Gap/Theory Lens/Contribution 无被动 | P3 Gap / P5-P6 Theory Lens / P7-P8 Contribution 中无 "It is argued that" | 出现无主语被动语态 | 记录被动语态位置和改写建议 |
| Contribution 用第一人称主动 | P7-P8 使用 "We extend/refine/reconcile..." | "This study contributes by..." | 记录贡献声明句式 |
| 无 inflated symbolism | 无 "paradigm shift" / "fundamentally transforms" | 出现过度包装词汇 | 记录降级改写方式 |

### Module Skip 检测

根据 write-introduction 的模块跳过规则，判断论文是否跳过/压缩了模块，以及是否合理：

| 模块 | 检测问题 | 合理跳过条件（全部满足） | 检测结果 |
|------|---------|------------------------|---------|
| Stakes（实践层） | 是否独立存在？ | Hook 已承担实践重要性（人命/安全/精确量化损失/制度危机） | 跳过/存在/嵌入 |
| Stakes（理论层） | 是否嵌入 Gap 末尾？ | Gap 末尾有 1-2 句理论 Stakes | 嵌入/独立/缺失 |
| Contribution | 是否独立段落？ | Theory Lens 本身即贡献声明（构念区分型）或期刊风格偏好紧凑（JOM/MS/POM） | 压缩/独立/缺失 |
| Theory Lens | 是否独立？ | Gap 末尾已含理论名称+方向性预测 | 嵌入/独立/缺失 |
| Literature Turn | 是否独立？ | Hook 已充分展示跨文献流共识/对话，且 Introduction ≤5 段 | 嵌入/独立/缺失 |
| Preview | 是否独立？ | Theory Lens 或 Contribution 中已暗示实证 setting+发现方向 | 嵌入/独立/缺失 |

**跳过风险评级**：
- **安全压缩**：模块功能嵌入相邻段落，且满足上表"必须满足"条件
- **风险跳过**：模块功能完全缺失，且不满足跳过条件 → 记录为 "risky_skip"
- **默认策略**：未明确满足跳过条件时，标记为 "should_have_been_included"

### 叙事质量摘要输出

```yaml
phase_1_5_quality_gate:
  module_coverage:
    required_modules: ["hook", "literature_turn", "tension", "stakes", "theory_lens", "preview", "contribution"]
    present_modules: ["hook", "literature_turn", ...]
    missing_modules: ["stakes"]
    coverage_rate: "85%"
    module_skip_detected:
      stakes: {status: "embedded / skipped / present", justification: "...", risk: "safe / risky"}
      contribution: {status: "compressed / present", justification: "...", risk: "safe / risky"}
  combo_alignment:
    detected_combo: "Incompleteness × Mechanism"
    properly_addressed: ["tension 使用 'remains unclear' 标志性语言", "theory_lens 引入中介机制"]
    inadequately_addressed: ["stakes 缺失——Incompleteness 必须有 Stakes 才能避免增量感"]
  narrative_sufficiency:
    puzzle_stated_explicitly: true/false
    common_ground_established: true/false
    departure_point_clear: true/false
    audience_implied: true/false
    transition_chain_continuous: true/false
  stakes_stress_test:
    generic_gap_language: true/false
    specific_consequence_stated: true/false
    target_audience_named: true/false
    one_sentence_test: true/false
  prose_craft:
    human_face:
      hook_has_actor: true/false
      actor_name: "[具体名称]"
      consensus_has_authors: true/false
      anomaly_has_case: true/false
    showing_vs_telling:
      construct_illustration_paired: true/false
      gap_has_consequence_scene: true/false
      theory_consequence_specific: true/false
      mechanism_operationalized: true/false
    conversational_voice:
      no_passive_in_key_modules: true/false
      contribution_active_voice: true/false
      no_inflated_symbolism: true/false
  cross_section_alignment:
    theory_lens_consistent: true/false
    contribution_hypothesis_aligned: true/false
    preview_results_consistent: true/false
  contradictions_or_gaps: ["tension 声称 'theoretically important' 但 stakes 未解释为什么", "contribution 承诺 Boundary 贡献但 theory_lens 未引入边界条件"]
  information_poverty_dimensions: ["未建立 common ground（literature_turn 只有罗列）", "stakes 只有 generic 重要性声明"]
```

---
