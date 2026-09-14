# paper-state.yaml Schema（v1.3.0 权威定义）

```yaml
# ============================================================
# paper-state.yaml v1.3.0
# ============================================================
# 字段按 section 分组。每个 section 的核心作用是：
#   上游 section 完成后填充自己的 metadata
#   下游 section 启动时读取上游 metadata
#   人工也可以随时手动编辑（YAML 可读）
# 注意：canonical story 字段以 paper-story-contract/references/schema.md 为准（见 §1.1）
# v1.3 变更：登记 canonical story 块、theory_hints 嵌套 gap_type + conversation_strategy、
#   methods.story_alignment / hypothesis_variable_map[*].storyline_id / methods.robustness_plan（权威位置）、
#   results.hypothesis_results 新结构（baseline_verdict + overall_evidence）、results.story_resolution。
#   legacy 字段（central_knot_statement / narrative_arc / core_constructs / flat gap_type /
#   hypothesis_results[*].supported）迁出正式 schema，见文末「Legacy 字段迁移映射」。

# ============================================================
# Canonical Story（顶层键，先于各 section）
# 唯一权威: paper-story-contract/references/schema.md；此处登记 write-introduction
# 输出片段中的 story 块结构，供协议层校验与下游读取，不重复定义语义。
# 生产者: write-introduction（Story Intake）
# 消费者: write-theory / write-methods / write-results（Phase 0 均先读 story）
# ============================================================
story:
  schema_version: 1             # story 契约自身版本（paper-story-contract 定义）
  status: "provisional"         # provisional | confirmed
  stage: "preparing"            # preparing | blocking | refining | finishing
  evidence_state: "unstable"    # unstable | mixed | stable
  theme_question: "[研究问题]"
  central_knot: "[一句话核心冲突]"
  stakes:
    theoretical: "[为什么该遗漏、误解或矛盾在理论上重要]"
    practical: "[可选]"
  characters:
    main:
      - {name: "[核心构念]", role: "[focal_predictor / focal_outcome / core_process]", level: "[分析层级]"}
    supporting:
      - {name: "[中介、调节、情境或边界构念]", role: "[mediator / moderator / context / boundary]", level: "[分析层级]"}
  storylines:
    - id: "S1"
      question: "[子问题]"
      constructs: ["[已在 characters 中声明的构念]"]
      promised_resolution: "[何种理论论证与证据将回答它]"
  reader_shift:
    from: "[读者原有理解]"
    to: "[本文希望形成的新理解]"
  integrity:
    theme_grounding: "grounded"          # grounded | provisional | unsupported
    knot_authenticity: "grounded"        # grounded | provisional | unsupported
    character_discipline: "grounded"     # grounded | provisional | unsupported
    payoff_feasibility: "grounded"       # grounded | provisional | unsupported
    unsupported_moves: []
    notes: "[项目自身故事的证据边界；不写范文、类型或框架]"

# ============================================================
# 项目标识 + Vault 连接
# ============================================================
paper:
  id: "ceo-regulatory-focus-recall-timing"   # 唯一标识，kebab-case
  title: "CEO Regulatory Focus and Time to Recall"  # 论文标题
  target_journal: "AMJ"                       # 目标期刊（影响 Hook 风格、结构等）
  created: 2026-07-08
  updated: 2026-07-08

  # --- Vault 知识库连接（供 write-introduction Phase 0 / write-theory Phase 1.2 Vault 检索使用）---
  vault:
    war_room: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/项目作战室 - CEO regulatory focus × time to recall.md"
    section_evidence_map: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/章节-证据映射 - CEO regulatory focus × time to recall.md"
    evidence_pack: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/文献证据包 - CEO regulatory focus × time to recall.md"
    claim_cards_tag: "CEO regulatory focus × time to recall"   # 论证卡库中与此项目关联的 tag
    # 以上路径均为 Vault 内相对路径。若项目不在此层级结构或使用不同文件名，修改即可。
    # 若项目尚未建立这些资产，字段为 null，write-* 回退到 Vault 全文搜索（较慢但仍有价值）。

# ============================================================
# Section 1: Introduction
# 生产者: write-introduction / diagnose-introduction
# 消费者: write-theory (Phase 0), paper-review/pollock-qc (承诺-兑现对齐)
# ============================================================
introduction:
  status: drafted               # pending | drafted | reviewed | final
  output_path: "outputs/intro_v3.md"
  updated: 2026-07-05

  # --- theory_hints: 供 write-theory Phase 0 自动读取 ---
  theory_hints:
    # gap_type: v1.3 起为嵌套结构（以 write-introduction 片段为准），不再使用 flat 字符串
    gap_type:
      primary: "Inadequacy"                    # Incompleteness | Inadequacy | Incommensurability；驱动主张力、结构复杂度与能量，不决定 Conversation
      primary_method: "neglect"                # Sandberg 找法标签: confusion | neglect | application spotting
      secondary: null                          # 可选: Incompleteness | Inadequacy | Incommensurability | null；次 gap，在 Tension 叠加
      secondary_method: null                   # 可选: confusion | neglect | application spotting | null
      incommensurability_resolution:           # 仅 primary = Incommensurability 时填写
        authenticity_gate: "pass"              # pass | fail | uncertain
        comparability:
          conversation_level: "pass"           # pass | fail | uncertain
          shared_object_or_family: "[共享理论对象或可辩护的高阶 X/Y 家族]"
          member_mapping: "[低阶构念/指标如何映射到共享对象]"
          formal_lock: "pending"               # R3/R4 的具体 X、Y、层级、时间范围、estimand: pass | fail | pending
        conflict_location: "[X / Y / mechanism / context / measurement-or-design]"
        primary_route: "R3"                    # R1 | R2 | R3 | R4
        secondary_route: null                  # R1 | R2 | R3 | R4 | null
        adjudicating_prediction: "[可直接区分本文解释与最强既有解释的预测]"
    makadok_dimension: "Mechanism"           # Constructs | Mechanism | Boundary | Phenomenon | Level | Mode | Question | Output
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    conversation_strategy: "Progressive"     # Progressive | Synthesized | Non-Coherence（v1.3 新增）

  # --- contribution_contract: 供 paper-review/pollock-qc 承诺-兑现对齐 ---
  contribution_contract:
    - claim: "We explain why CEO regulatory focus affects time to recall by identifying two timing-error weighting mechanisms."
      makadok_dimension: "Mechanism"
    - claim: "We introduce regulatory focus as a novel predictor of recall timing, extending the literature beyond governance and operational antecedents."
      makadok_dimension: "Constructs"
  # 理论论文（AMR 模式）：contribution_contract 只放一条核心贡献，并加 theory_paper: true 标记

# ============================================================
# Section 2: Theory & Hypotheses
# 生产者: write-theory
# 消费者: write-methods (变量对齐), write-results (假设-结果对齐), paper-review/discussion-review (已有草稿的理论贡献锚点)
# ============================================================
theory:
  status: pending               # pending | drafted | reviewed | final
  output_path: null
  depends_on: ["introduction"]   # 上游 section 必须 completed 才能启动
  updated: null

  theory_variant: null           # 从 write-theory Phase 0 输出
  institutional_background_included: false

  # --- constructs: 供 write-methods M1-M4 变量操作化 ---
  constructs:
    independent: null            # 如 "CEO promotion focus"
    dependent: null              # 如 "time to recall (days)"
    mediator: null               # 如 "weighting of error type I vs II"
    moderator: null              # 如无可为 null
    controls: []                 # 理论驱动的控制变量

  # --- hypotheses: 供 write-methods 假设-变量映射 + write-results 假设-结果对齐 ---
  hypotheses:
    - id: "H1"
      storyline_id: "S1"         # 对齐 story.storylines[*].id（paper-story-contract 定义的 Section Extension，write-methods/write-results 消费）
      statement: null            # "CEO promotion focus is negatively associated with time to recall."
      type: "main"               # main | mediation | moderation | competition
      iv: null
      dv: null
      predicted_direction: "negative"
    # - id: "H2"
    #   statement: null
    #   type: "main"
    #   iv: null
    #   dv: null
    #   predicted_direction: "positive"

  # --- mechanism_chains: 供 paper-review/discussion-review 检查理论贡献兑现 ---
  mechanism_chains: []

# ============================================================
# Section 3: Methods
# 生产者: write-methods
# 消费者: write-results (模型规格、变量名、story_alignment、robustness_plan)
# ============================================================
methods:
  status: pending
  output_path: null
  depends_on: ["theory"]
  updated: null

  design_type: null              # 面板数据/OLS | 自然实验/DiD | 生存分析 | ...
  estimator_family: null         # OLS | FE | Logit | Cox | DiD | IV/2SLS | ...
  sample:
    source: null                 # 数据来源描述
    n_observations: null
    n_firms: null
    time_window: null
    inclusion_criteria: []

  # --- variables: 供 write-results 槽位报告 ---
  variables:
    dv: null                      # 因变量名（如 time_to_recall_days）
    iv: null                      # 核心自变量名（如 ceo_promotion_focus）
    mediator: null                # 中介变量名
    moderator: null               # 调节变量名
    controls: []                  # 控制变量列表
    fixed_effects: []             # 固定效应（如 firm, year）

  # --- hypothesis_variable_map: 供 write-results R3 槽位 ---
  # 键为假设 id（H1/H2/...，动态键）；storyline_id 为 v1.3 登记字段，
  # 将每条假设的变量映射对齐到 story.storylines[*].id
  hypothesis_variable_map:
    H1: {storyline_id: "S1", predictor: null, outcome: null, model: null}
    # H2: {storyline_id: "S1", predictor: null, outcome: null, model: null}

  # --- story_alignment: 供 write-results Phase 0 消费（v1.3 登记；write-results SKILL.md 直接读取）---
  story_alignment:
    central_knot: null            # 从 story.central_knot 引用，不改写
    design_resolution_logic: null # 为什么该设计能回答 theme question
    storyline_model_map:          # 键为 storyline id（S1/S2/...，动态键）
      S1:
        hypotheses: ["H1"]
        constructs: []
        variables: []
        model_or_step: null       # 模型、实验比较或质性分析步骤
        identification_burden: null  # 需要满足的识别或效度条件
    unresolved_validity_threats: []  # 尚未解决的 threat；无则为空列表

  # --- results_preview: Methods M10 段的预告（供 write-results 预期管理）---
  results_preview: null

  # --- robustness_plan: 稳健性检验计划的唯一权威位置（v1.3 登记）---
  # 由 write-results 决策诊断（write-results/references/robustness-diagnosis.md）填充，或手动填写。
  # 供 write-results 缺失时触发诊断、存在时跳过诊断直接生成 R7 段落。
  # results 节不重复登记此结构（write-results 片段仅保留指针）。
  robustness_plan:               # 可选；不存在时 write-results 自动触发决策诊断
    mandatory: []                # 必须检验的维度
    recommended: []              # 建议检验的维度
    optional: []                 # 可选检验的维度
    excluded: {}                 # {维度名: 排除理由}

# ============================================================
# Section 4: Results
# 生产者: write-results
# 消费者: paper-review/pollock-qc；如用户已有 Discussion 草稿，可供 discussion-review 检查主要发现与意外发现是否被正确解释
# 注意: results.revision_constraints 与 results.validation 为 write-results
#   skill-local 字段（仅 write-results 内部 draft-revision-protocol /
#   validation-protocol 消费），v1.3 起不入本协议 state，不在此登记。
# ============================================================
results:
  status: pending
  output_path: null
  depends_on: ["methods"]
  updated: null

  estimator_family: null          # 确认的估计器

  # --- hypothesis_results: 供 Results story_resolution 与全稿审查 ---
  # v1.3 结构（以 write-results 片段为准）：baseline_verdict + overall_evidence；
  # legacy 字段 supported → baseline_verdict（见文末迁移映射）。键为假设 id（动态键）。
  hypothesis_results:
    H1: {direction: null, significant: null, baseline_verdict: null, overall_evidence: null}
    # direction: positive | negative | null
    # significant: true | false
    # baseline_verdict: supported | partially_supported | not_supported
    # overall_evidence: stable | qualified | mixed | unresolved

  # --- story_resolution: 供 paper-story-contract Section Extension 与下游审查消费（v1.3 登记）---
  story_resolution:
    headline_answer: null         # 对 story.theme_question 的证据约束式回答
    storylines:                   # 键为 storyline id（动态键）
      S1:
        status: null              # supported | mixed | unsupported | unresolved
        evidence: []              # table/model/estimate or qualitative evidence
        magnitude: null           # 效应量或明确说明无法估计
    surprises: []                 # 意外、反方向或敏感性发现；无则为空列表
    unresolved_questions: []      # 仍无法回答的问题；无则为空列表

  # --- key_findings: 供全稿审查；已有 Discussion 草稿时供 discussion-review 对照 ---
  key_findings: []
  unexpected_findings: []         # 意外/反直觉发现

# ============================================================
# Discussion — 仅保留兼容占位；标准化写作链不生成 Discussion
# ============================================================
# discussion:
#   status: skipped
#   ...

# ============================================================
# 跨 Section 对齐追踪
# ============================================================
cross_section_alignment:
  intro_theory:
    status: unchecked             # unchecked | checked_ok | checked_conflict
    checked_at: null
    notes: null
  theory_methods:
    status: unchecked
    checked_at: null
    notes: null
  methods_results:
    status: unchecked
    checked_at: null
    notes: null
  intro_discussion:
    status: skipped               # Discussion 暂不激活
    checked_at: null
    notes: null
```

## Legacy 字段迁移映射（v1.2 → v1.3）

v1.3 起以下 legacy 字段迁出正式 schema。读取旧 paper-state.yaml 时按下表迁移；新输出一律写 v1.3 字段。与 `paper-story-contract/references/schema.md` 的 Legacy Read Compatibility 表保持一致。

| v1.2 legacy 字段 | v1.3 去向 |
|------------------|-----------|
| `introduction.theory_hints.gap_type`（flat 字符串） | `introduction.theory_hints.gap_type.primary`（嵌套结构的 primary 子字段） |
| `introduction.theory_hints.central_knot_statement` | `story.central_knot` |
| `introduction.theory_hints.core_constructs` | `story.characters`（作为初始角色候选） |
| `introduction.theory_hints.narrative_arc` | 不再写入 state；仅作 stage 诊断证据（见 paper-story-contract legacy 表） |
| `results.hypothesis_results[*].supported` | `results.hypothesis_results[*].baseline_verdict` |

迁移行为：输出迁移警告；创建 `story` 块时标 `status: provisional`；新输出不写 legacy 别名；保留无关 legacy 字段以免现有消费者丢数据。
