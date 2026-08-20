# Phase 1: module map and coverage

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 1 — Theory 功能模块映射与粗粒度解构

读取 Theory 全文，按**功能模块**（T1–T6）进行粗粒度标注。标注时只定位模块功能边界，不做深入分析。

### 模块映射表（与 write-theory 对齐）

| 模块 | 功能 | 识别标准 | 粗粒度标注任务 |
|------|------|----------|----------------|
| T1 Construct Definition | 界定核心构念，建立概念基础 | 定义段落；标志词："We define..." / "...refers to..." / "...is conceptualized as..." | 标记定义策略（采纳/修正/新建）、scope condition 是否明确、是否区分易混淆构念 |
| T2 Theoretical Lens | 引入理论视角，建立解释框架 | 理论引入段落；标志词："Drawing on..." / "Building on..." / "We adopt..." | 标记理论来源、是否与 Gap 文献独立（Two-literature clarity）、是否提供 overarching figure |
| T3 Mechanism Chain | 推演构念间的因果/关联机制 | 机制段落；呈现 step-by-step why chain | 标记机制步数、每步的理论依据、是否有 boundary condition 嵌入 |
| T4 Hypothesis Derivation | 从机制推演中形式化假设 | 假设陈述段落；标志词："Therefore," / "Thus," / "Accordingly," | 标记假设编号、方向、条件、推导完整性（why chain → hypothesis） |
| T5 Boundary Condition | 论证边界条件或调节机制 | 边界段落；标志词："However, this effect..." / "The relationship is contingent on..." | 标记边界逻辑（moderator 引入时机、理论依据） |
| T6 Closure | 收束论证，建立假设间逻辑联系 | 收束段落；标志词："Taken together..." / "In sum..." | 标记是否总结整体理论框架、是否预告实证策略 |

### 跨 Section 对齐检查（grill-with-docs 模式）

在粗粒度解构阶段，**交叉验证 Theory 与 Introduction / Methods / Results 的一致性**：

| 对齐检查项 | 检查位置 | 问题 |
|-----------|----------|------|
| T2 Theoretical Lens ↔ Introduction I5 | 理论来源是否一致 | Introduction 承诺了制度理论但 Theory 用了 RBV？ |
| T4 Hypotheses ↔ Introduction I7 | 假设是否兑现贡献声明 | I7 声称 Mechanism 贡献但 T4 无中介假设？ |
| T4 Hypotheses ↔ Methods M4/M5 | 假设变量是否在 Methods 中操作化 | T4 提出三向交互但 Methods 未报告交互项？ |
| T3 Mechanism Chain ↔ Introduction I3 Gap | 机制是否回应了 Gap | I3 指出 "缺乏边界条件" 但 T3 无 boundary 论证？ |
| T6 Closure ↔ Results R9 | 理论框架总结是否与 Results 发现一致 | T6 预告的方向与 Results 系数方向相反？ |

发现矛盾时，在 `contradictions_or_gaps` 中记录，并在 Phase 2 Theory Logic 中标记为 "Theory Contract 风险"。

### 特殊排列记录

记录该 Theory 是否使用标准模块顺序（T1→T2→T3→T4→T5→T6）或变体：
- **理论先引入**: T2 在 T1 之前？（常见：先给理论框架再界定构念）
- **边界定理嵌入**: T5 嵌入 T3 内部？（常见：机制推演到某步时引入 contingency）
- **构念辨析主导**: T1 占主导地位（构念辨析型常见，大篇幅区分 A vs B）
- **假设树展开**: T4 分散在多个 T3 之后？（假设树型：每分支推导一个假设）
- **过程阶段**: T3 按时间/阶段展开（质性过程理论型）

### 输出格式

```yaml
phase_1_module_map:
  T1_construct_definition:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    definition_strategy: "采纳现有 / 修正现有 / 新建"
    scope_condition_present: true/false
    construct_differentiation: true/false
  T2_theoretical_lens:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    theoretical_source: "[理论名称]"
    independent_from_gap_literature: true/false
    overarching_figure_present: true/false
  T3_mechanism_chain:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    mechanism_steps: "[N]"
    boundary_embedded: true/false
  T4_hypothesis_derivation:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    hypotheses_derived: ["H1", "H2", "H3"]
    derivation_completeness: "完整 / 部分 / 跳跃"
  T5_boundary_condition:
    located: true/false
    paragraph_range: "[第X段或嵌入T3]"
    boundary_type: "调节 / 中介 / 条件"
    theoretical_basis: true/false
  T6_closure:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    summarizes_framework: true/false
    previews_empirical_strategy: true/false
    # v1.3.0：write-theory v3.3.0 已取消独立 T6 强制要求；记录实际收束策略
    # （局部收束 / 嵌入框架总结 / 独立 Closure 段 / Discussion 开篇整合）。
    # T6 扩展检查（knot_fully_tied / voice_check / institutional_shock_extra /
    # narrative_energy）见 Phase 1.5 的 t6_closure_quality 输出块，此处不重复。
actual_module_sequence: ["T1", "T2", "T3", "T4", "T5", "T6"]
deviation_from_standard: "T2 在 T1 之前; T5 嵌入 T3 第2步"
```

---

## Phase 1.25 — 制度冲击类研究 Theory Lens 特殊适配提取（v1.2.0 新增）

如果论文使用自然实验、制度冲击或准实验设计（IV, DiD, RDD, 生存分析），Theory 部分需要额外完成识别策略的理论论证。蒸馏时需提取以下内容：

### 1. 制度冲击 Theory Lens 模板提取

检查 T2/T3 是否包含以下三层论证：

| 层级 | 论证内容 | 标志句 | 蒸馏记录 |
|------|---------|--------|---------|
| **第一层（外生性）** | 制度冲击为什么外生？对谁外生？ | "[policy] creates exogenous variation in [treatment] that is plausibly unrelated to [unobserved confounders]" | 记录外生性论证句 |
| **第二层（机制）** | 制度变化如何通过理论机制影响行为？ | "[policy] alters [actor]'s incentives to [action] by [mechanism]" | 记录机制句 |
| **第三层（识别基础）** | 为什么这个情境适合识别因果关系？ | "allowing us to isolate the causal effect of [treatment] on [outcome] from [alternative explanations]" | 记录识别基础句 |

### 2. 识别策略的理论论证提取

| 识别策略 | 必须在 Theory 中论证的内容 | 标志句模式 | 缺失风险 |
|----------|------------------------|-----------|---------|
| **IV** | 排除限制的理论基础；工具变量通过什么理论渠道影响处理变量 | "[Instrument] affects [treatment] through [channel] but does not directly influence [outcome] except via [treatment], because..." | Theory 与 Methods 脱节 |
| **DiD** | 平行趋势的理论基础；处理效应异质性的理论预判 | "Absent the [policy], treated and control firms would have followed parallel trends because [theoretical reason]" | Methods 中跑 DiD 但 Theory 无平行趋势论证 |
| **RDD** | 断点可比性的理论基础；断点两侧制度差异的理论含义 | "Firms just above and below the [threshold] are observationally similar in [key dimensions] because [theoretical reason]" | 断点选择缺乏理论依据 |
| **生存分析 (Cox)** | 时间维度的理论意义；风险率vs二元结果的理论丰富性；比例风险假设的理论合理性 | "[treatment] alters the *rate* at which [actor] approaches the [decision threshold] because [theoretical reason]" | 时间仅作为控制变量而非理论维度 |

### 3. 输出格式

```yaml
phase_1_25_institutional_shock:
  design_type: "IV / DiD / RDD / 生存分析 / 无"
  theory_lens_three_layers:
    exogeneity: {present: true/false, text: "[论证句]", location: "P[段号]"}
    mechanism: {present: true/false, text: "[论证句]", location: "P[段号]"}
    identification_foundation: {present: true/false, text: "[论证句]", location: "P[段号]"}
  identification_argument_in_theory:
    iv_exclusion_restriction: {present: true/false, text: "[论证句]", location: "P[段号]"}
    iv_first_stage_channel: {present: true/false, text: "[论证句]", location: "P[段号]"}
    did_parallel_trends: {present: true/false, text: "[论证句]", location: "P[段号]"}
    did_heterogeneity_theory: {present: true/false, text: "[论证句]", location: "P[段号]"}
    rdd_comparability: {present: true/false, text: "[论证句]", location: "P[段号]"}
    survival_temporal_dimension: {present: true/false, text: "[论证句]", location: "P[段号]"}
    survival_hazard_richness: {present: true/false, text: "[论证句]", location: "P[段号]"}
  theory_methods_gap: "[如果 Theory 未论证而 Methods 详细描述了识别策略，记录此处]"
```

**注意**：如果论文**不**使用制度冲击/自然实验设计，此 Phase 输出 `design_type: "无"`，其余字段省略。

---

## Phase 1.5 — 模块覆盖检查与理论质量摘要

这是质量控制检查点。对照理论构建类型，检查 Theory 是否覆盖了该类型**必须出现**的模块。

### Why-Chain 边缘案例压力测试（grill-me 场景探测模式）

对 T3 Mechanism Chain 执行推理鲁棒性压力测试，验证每个机制步骤是否经得起边缘场景追问：

| 测试问题 | 通过标准 | 失败信号 |
|---------|----------|----------|
| 如果 [前因] 为真但 [边界条件] 不成立，机制是否仍然成立？ | 能指出机制失效的具体条件 | "总是成立" / "毫无疑问"（过度概括） |
| 反方向是否可能？（如 X 导致 Y，Y 是否也能导致 X？） | 已排除反向因果或说明为何不可能 | 未讨论反向因果 |
| 替代解释是否被排除？ | 至少排除了 1 个主要竞争解释 | "没有其他解释"（空洞断言） |
| 机制链的每一步是否有**独立的理论依据**？ | 每步都有明确的理论或文献支撑 | 某步只有 "显然" / "常识" 支撑 |
| 如果机制成立，是否会产生**未预见的副效应**？ | 作者已考虑或排除了主要副效应 | 完全未讨论副效应 |

**测试方式**：为每条 why chain 发明 1-2 个反事实或边缘场景，追问 "如果 X 不成立，你的理论预测会怎样？"

### 构念术语挑战（grill-with-docs 术语锐化模式）

借鉴 grill-with-docs 的 "Sharpen fuzzy language" 原则：

当论文使用**模糊或多义词**时，立即标记并挑战：

| 问题类型 | 示例 | 处理方式 |
|---------|------|----------|
| 构念名称过于宽泛 | "organizational capability" | 追问：是 dynamic capability、absorptive capacity 还是 operational capability？记录为 construct ambiguity |
| 同一术语多义使用 | "performance" 既指财务绩效又指创新绩效 | 标记为术语冲突，记录在不同位置的具体指代 |
| 新构念缺少区分维度 | 提出 "digital resilience" 但未与 "IT resilience" 区分 | 标记为 construct differentiation 不足 |
| 操作化与定义脱节 | 定义说 "routine updating" 但测量的是 "IT investment" | 标记为 construct validity 风险 |

### 构建类型强制模块表

| 构建类型 | Makadok 维度 | 强制模块 | 缺失即高风险 |
|----------|-------------|----------|--------------|
| 构念辨析型 | Constructs | T1, T2, T4, T6 | T1 缺差异化维度、T2 缺解释两个构念为何不同 |
| 机制推演型 | Mechanism | T1, T2, T3, T4, T6 | T3 缺多步 why chain（单步即薄弱）、T4 缺 "Therefore" 推导 |
| 假设树型 | Boundary / Level | T1, T2, T3, T4, T5, T6 | T5 缺 moderator 理论依据、T4 缺条件化假设 |
| 质性过程理论型 | Mode | T1, T2, T3, T6 | T3 缺时间/阶段标记、T6 缺过程模型总结 |
| 跨层次桥接 | Level | T1, T2, T3, T4, T6 | T3 缺跨层次机制（如 composition/emergence）、T1 缺层次标注 |
| 现象驱动型 | Phenomenon | T2, T3, T4, T6 | T2 可以替代 T1（现象本身即为新构念） |
| 反直觉预测型 | Output | T1, T2, T3, T4, T6 | T3 必须解释为何直觉错误、T4 方向必须与直觉相反 |

### 构建类型 × 假设结构交叉矩阵

同一构建类型下，不同的假设结构对 T1–T6 模块有差异化的强制要求。以下矩阵定义各交叉组合的**模块必要性**（M = Mandatory 强制, C = Conditional 条件, O = Optional 可选）和**高风险缺失**。

#### 机制推演型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯主效应 | M | M | **M** (≥2步因果链) | M | O | M | T3 两步链是唯一机制论证机会；纯主效应时 T3 薄弱则全文理论崩溃 |
| 主效应+中介 | M | M | **M** (≥2步，中介构念必须独立定义) | **M** (H1:X→M, H2:M→Y 配对) | O | M | T1 必须定义 mediator M；T3 每步对应一个假设；H1+H2 必须构成完整中介链 |
| 主效应+调节 | M | M | M (主效应链+调节插入点) | M (H1:主效应, H2:调节) | **C** (若调节是理论核心→M) | M | T5 必要性取决于调节是否为理论核心。若调节只是 robustness/补充分析 → T5=O；若调节回应了 I3 Gap → T5=M |
| 中介+调节混合 | M | M | **M** (链中每步都需标注调节可能插入的位置) | **M** (≥3 假设: X→M, M→Y, + 调节假设) | **M** | M | 最复杂的机制推演子类型。T3 必须显式标注 "moderation occurs at step [N] of the chain"；T5 必须区分 "moderation of X→M path" vs "moderation of M→Y path" |

#### 假设树型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯主效应+调节 | M | M | **M** (基线机制→条件化分叉) | **M** (H1:主效应, H2:调节) | **M** | M | T3 必须有 "not uniform; rather" 分叉结构；T5 必须在 T3 机制中就出现（非假设后补丁） |
| 主效应+调节（多 moderator） | M | M | **M** (多条件分叉) | **M** (H1:主效应, H2:W1调节, H3:W2调节) | **M** | M | T3 需解释多个 moderator 之间的关系（独立/叠加/竞争）；T5 每个 moderator 都需独立理论依据 |
| 中介+调节 | M | M | **M** (中介链 + 调节插入点) | **M** (H1:X→M, H2:M→Y, H3:X→M moderated by W) | **M** | M | 必须明确调节发生在中介链的哪个环节（X→M? M→Y? both?）；T5 包含 moderated mediation 语言 |
| 三向交互 | M | M | **M** (三层条件嵌套) | **M** (H1:主效应, H2:两向交互, H3:三向交互) | **M** | M | T3 需要三层嵌套论证（X→Y / X×W→Y / X×W×Z→Y）；每层嵌套的理论增量必须独立论证 |

#### 构念辨析型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯构念区分（无因果假设） | **M** (占主导，≥40% 篇幅) | M | **O** (可缺，区分即贡献) | **C** (可能收敛为 Proposition 而非 Hypothesis) | O | M | T1 必须包含差异化维度表或对比段落；T2 必须解释为什么现有理论无法区分这两个构念 |
| 构念区分+主效应 | **M** (占主导) | M | M (区分→因果过渡) | M | O | M | T1→T3 必须有过渡："Because A and B are distinct, they have different effects on Y" |
| 构念区分+调节 | **M** (占主导) | M | M | M (H1:A→Y, H2:B→Y, H3:moderated) | M | M | 比较复杂的构念辨析型；T5 需解释调节变量对 A/B 的差异化影响 |

#### 调节效应型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯调节（无主效应假设） | M | M | M (调节机制为主) | **M** (仅交互假设) | **M** | M | 审稿人常见攻击："为什么不报告主效应？" T3 必须解释为什么主效应不是理论重点 |
| 主效应+调节 | M | M | M (主效应→调节) | M (H1:主效应, H2:调节) | **M** | M | T3 必须区分 "baseline relationship" 和 "contingent relationship" |
| 跨层调节 | M | M | **M** (跨层机制+调节方向) | **M** (层级标注) | **M** | M | 必须遵循 JIBS 7步(within)或9步(cross-level)协议；T1 必须标注每个构念的分析层次 |
| 调节方向反转 | M | M | **M** (基线机制+反转论证) | **M** (H1:正调节, H2:负调节 或 H1:增强, H2:翻转) | **M** | M | T3 必须论证为什么同一调节变量在不同条件下方向相反；排除 "reverse interaction" 陷阱 |

#### 质性过程理论型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯过程（Proposition 为主） | M | M | **M** (阶段序列+过渡条件) | **C** (收敛为 Proposition，非 Hypothesis) | O | **M** | T3 必须有阶段过渡条件（"As [condition] shifts, the process moves from Phase N to Phase N+1"）；T6 必须有过程模型总结图 |
| 过程+因果 | M | M | **M** (过程嵌套因果) | M (混合: Proposition + Hypothesis) | C | M | 比较少见；需区分过程阶段内的因果机制 vs 跨阶段的过渡机制 |
| 过程+调节 | M | M | **M** (过程×条件) | M | M | M | T5 需解释调节变量如何改变过程的速度/顺序/终点 |

### 构建类型 × 机制深度交叉矩阵

机制深度不同，T3 和 T4 的最低标准不同：

| 机制深度 | T3 最低要求 | T4 最低要求 | 常见构建类型 | 风险信号 |
|---------|-----------|-----------|-------------|---------|
| **单步 (X→Y)** | 必须有独立的理论段落（非 citation list）解释 X 为什么影响 Y | 假设必须含方向 + 理论依据简述 | 构念辨析型、现象驱动型 | 在机制推演型/假设树型中，单步即薄弱——标记为 "机制深度不足" |
| **两步 (X→M→Y)** | 每步必须有独立的理论依据；M 必须在 T1 中正式定义 | 至少 H1:X→M + H2:M→Y 或等价的连续假设 | 机制推演型（标准配置）、假设树型 | M→Y 步必须有 "Consequently" / "In turn" 等递进连接词，不能只是并列第二个假设 |
| **三步+ (X→M1→M2→Y)** | M1 和 M2 必须概念独立（非同一构念的不同标签）；每步有独立的理论段落 | 假设数 ≥ 步骤数；每个中介构念至少一个假设 | 机制推演型（深度配置） | 区分 M1 和 M2 的概念差异必须清晰，否则审稿人会质疑 "why not a single mediator?" |
| **条件化步 (X→Y, moderated by W at step K)** | 必须明确基线机制 + 标注调节插入的具体步骤（"W moderates the X→M path"） | 主效应假设 + 调节假设成对出现 | 假设树型、调节效应型 | 不能只说 "W moderates the relationship"，必须说 "W moderates the X→M path because..." |
| **阶段化步 (Phase1→Phase2→Phase3)** | 每阶段必须有独立特征描述 + 过渡条件 | Proposition 而非 Hypothesis | 质性过程理论型 | 不能只有阶段名称而无过渡条件（那只是分类，不是过程理论） |

### 理论质量摘要输出

```yaml
phase_1_5_quality_gate:
  module_coverage:
    required_modules: ["T1", "T2", "T3", "T4", "T5", "T6"]
    present_modules: ["T1", "T2", ...]
    missing_modules: ["T5"]
    coverage_rate: "83%"
  type_alignment:
    detected_type: "机制推演型"
    properly_addressed: ["T3 有足够的 reasoning moves（不按变量数计）", "T4 的收敛方式与单向/竞争预测匹配"]
    inadequately_addressed: ["T3 第2步跳跃：缺少中间机制论证"]
  cross_matrix_alignment:
    detected_hypothesis_structure: "主效应+中介"
    mechanism_depth: "两个推理转换；不等同于 X→M→Y"
    module_requirements: {"T1": "按构念需要", "T2": "理论透镜按需", "T3": "足够的 reasoning moves", "T4": "与实际关系形式匹配", "T5": "条件化时需要", "T6": "独立段落非强制"}
    matrix_breaches: ["T1 未定义 mediator M 的 scope condition"]
    depth_sufficiency: "根据前提→过程→预测是否完整判断，不因存在中介自动合格"
  theory_sufficiency:
    why_chain_integrity: true/false
    construct_scope_clear: true/false
    protagonist_count_valid: true/false
    two_literature_clarity: true/false
    hypothesis_form_complete: true/false
    cross_matrix_covered: true/false
  why_chain_stress_test:
    boundary_condition_tested: true/false
    reverse_causality_considered: true/false
    alternative_explanation_excluded: true/false
    each_step_has_theory_basis: true/false
  t6_closure_quality:  # v1.2.0 新增
    t6_present: true/false
    knot_fully_tied: true/false
    framework_locking: true/false
    logic_explicit: true/false
    denouement_preview: true/false
    voice_check_passed: true/false
    narrative_energy_maintained: true/false  # T6 结尾能量级 ≥ 最后假设推导段
    institutional_shock_extra_passed: true/false/null  # null 表示非制度冲击类研究
  construct_terminology:
    ambiguous_terms_found: ["capability"]
    term_conflicts: ["performance 在 T3 指财务绩效，在 T5 指创新绩效"]
    differentiation_dimensions_clear: true/false
  cross_section_alignment:
    theory_lens_consistent: true/false
    hypotheses_contribution_aligned: true/false
    hypotheses_methods_operationalized: true/false
    mechanism_gap_addressed: true/false
  contradictions_or_gaps: ["T2 声称用制度理论但 T3 机制用 RBV 语言", "T4 H2 方向与 T3 机制相反"]
  information_poverty_dimensions: ["T1 定义缺少 scope condition", "T3 只有 citation list 无机制推演"]
```

---
