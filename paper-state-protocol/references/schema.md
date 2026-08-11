# paper-state.yaml Schema（v1.2.0 权威定义）

```yaml
# ============================================================
# paper-state.yaml v1.2.0
# ============================================================
# 字段按 section 分组。每个 section 的核心作用是：
#   上游 section 完成后填充自己的 metadata
#   下游 section 启动时读取上游 metadata
#   人工也可以随时手动编辑（YAML 可读）
# 注意：canonical story 字段以 paper-story-contract/references/schema.md 为准（见 §1.1）

paper:
  id: "ceo-regulatory-focus-recall-timing"   # 唯一标识，kebab-case
  title: "CEO Regulatory Focus and Time to Recall"  # 论文标题
  target_journal: "AMJ"                       # 目标期刊（影响 Hook 风格、结构等）
  created: 2026-07-08
  updated: 2026-07-08

  # --- Vault 知识库连接（供 write-* Phase 0 Vault 检索步骤使用）---
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
    gap_type: "Inadequacy"                   # Incompleteness | Inadequacy | Incommensurability
    makadok_dimension: "Mechanism"           # Constructs | Mechanism | Boundary | Phenomenon | Level | Mode | Question | Output
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    central_knot_statement: "While prior work assumes firms respond to product failures uniformly, we argue that CEO regulatory focus systematically shapes when—not just whether—firms initiate recalls."  # legacy 字段：新项目用 canonical story（见 §1.1）
    narrative_arc: "moderate_rise"           # gentle_rise | moderate_rise | sharp_rise
    core_constructs: ["CEO regulatory focus", "time to recall"]

  # --- contribution_contract: 供 paper-review/pollock-qc 承诺-兑现对齐 ---
  contribution_contract:
    - claim: "We explain why CEO regulatory focus affects time to recall by identifying two timing-error weighting mechanisms."
      makadok_dimension: "Mechanism"
    - claim: "We introduce regulatory focus as a novel predictor of recall timing, extending the literature beyond governance and operational antecedents."
      makadok_dimension: "Constructs"

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
# 消费者: write-results (模型规格、变量名)
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
  hypothesis_variable_map:
    H1: {predictor: null, outcome: null, model: null}
    # H2: {predictor: null, outcome: null, model: null}

  # --- results_preview: Methods M10 段的预告（供 write-results 预期管理）---
  results_preview: null

# ============================================================
# Section 4: Results
# 生产者: write-results
# 消费者: paper-review/pollock-qc；如用户已有 Discussion 草稿，可供 discussion-review 检查主要发现与意外发现是否被正确解释
# ============================================================
results:
  status: pending
  output_path: null
  depends_on: ["methods"]
  updated: null

  estimator_family: null          # 确认的估计器

  # --- hypothesis_results: 供 Results story_resolution 与全稿审查 ---
  hypothesis_results:
    H1: {direction: null, significant: null, supported: null}
    # H2: {direction: null, significant: null, supported: null}

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
