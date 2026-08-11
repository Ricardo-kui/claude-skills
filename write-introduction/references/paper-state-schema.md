# Paper-State Schema — Introduction 输出片段（从 SKILL.md 下沉，v0.1）

> 由 write-introduction 输出末尾**对照使用**：附加 `### paper-state.yaml 片段` 块，供下游 write-theory / write-methods / write-results 自动消费。

**下游消费协议**：四个 write skills 先读取 canonical `story`，再读取各自的 section state。`write-theory` 使用 Introduction 的 Gap、贡献承诺与故事线；`write-methods` 和 `write-results` 在后续阶段消费 Theory/Methods 映射。

**使用方式**：复制整个块到项目 `paper-state.yaml`。新输出只写 canonical `story`，不再写 `central_knot_statement`、`narrative_arc` 或 `core_constructs` 等重复别名。如用户未提及 paper-state.yaml 协议，该片段的 YAML 注释头应包含使用说明。

```yaml
# --- paper-state.yaml 片段 (copy to your paper-state.yaml) ---
story:
  schema_version: 1
  status: "[provisional / confirmed]"
  stage: "[preparing / blocking / refining / finishing]"
  evidence_state: "[unstable / mixed / stable]"
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
    theme_grounding: "[grounded / provisional / unsupported]"
    knot_authenticity: "[grounded / provisional / unsupported]"
    character_discipline: "[grounded / provisional / unsupported]"
    payoff_feasibility: "[grounded / provisional / unsupported]"
    unsupported_moves: []
    notes: "[项目自身故事的证据边界；不写范文、类型或框架]"

introduction:
  status: drafted
  output_path: "[本次输出文件路径]"
  updated: "[YYYY-MM-DD]"

  theory_hints:
    gap_type:
      primary: "[Incompleteness / Inadequacy / Incommensurability]"  # 驱动主张力、结构复杂度与能量；不决定 Conversation
      primary_method: "[confusion / neglect / application spotting]"  # Sandberg 找法标签
      secondary: "[可选: Incompleteness / Inadequacy / Incommensurability / null]"  # 次 gap，在 Tension 叠加
      secondary_method: "[可选: confusion / neglect / application spotting / null]"
      incommensurability_resolution:  # 仅 primary = Incommensurability 时填写
        authenticity_gate: "[pass / fail / uncertain]"
        comparability:
          conversation_level: "[pass / fail / uncertain]"
          shared_object_or_family: "[共享理论对象或可辩护的高阶 X/Y 家族]"
          member_mapping: "[低阶构念/指标如何映射到共享对象]"
          formal_lock: "[R3/R4 的具体 X、Y、层级、时间范围、estimand：pass / fail / pending]"
        conflict_location: "[X / Y / mechanism / context / measurement-or-design]"
        primary_route: "[R1 / R2 / R3 / R4]"
        secondary_route: "[R1 / R2 / R3 / R4 / null]"
        adjudicating_prediction: "[可直接区分本文解释与最强既有解释的预测]"
    makadok_dimension: "[Constructs / Mechanism / Boundary / Phenomenon / Level / Mode / Question / Output]"
    tension_template: "[canonical_id from _routing_tables.yaml]"
    recommended_theory_variant: "[构念辨析型 (A) / 机制推演型 (B) / 假设树型 (C) / 质性过程理论型 (D) / 调节效应型 (E) / 竞争假设型 (F) / 辩证对立型 (G)]"
    promised_hypothesis_count: [N]
    promised_boundary_conditions: [true / false]
    promised_mechanism_steps: [N]
    conversation_strategy: "[Progressive / Synthesized / Non-Coherence]"

  contribution_contract:
    - claim: "[Introduction 中第一个贡献声明原文]"
      makadok_dimension: "[Constructs / Mechanism / Boundary / ...]"
    - claim: "[第二个贡献声明原文，如有]"
      makadok_dimension: "[Constructs / Mechanism / Boundary / ...]"
```

> 理论论文（AMR 模式）分支：`contribution_contract` 只放**一条**核心贡献（单核自明，见 `references/theory-paper-amr-mode.md`），并加 `theory_paper: true` 标记。
