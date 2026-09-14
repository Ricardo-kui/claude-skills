# 工作流片段示例（§4）

## 4.1 write-introduction 完成后

用户在 write-introduction 输出末尾收到以下追加块：

```yaml
# --- paper-state.yaml 片段（复制到你的 paper-state.yaml）---
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
  output_path: "outputs/intro_v3.md"
  updated: "[YYYY-MM-DD]"
  theory_hints:
    gap_type:                      # v1.3 嵌套结构；不再写 flat gap_type 或 legacy 别名
      primary: "Inadequacy"        # Incompleteness | Inadequacy | Incommensurability
      primary_method: "[confusion / neglect / application spotting]"
      secondary: null
      secondary_method: null
      incommensurability_resolution: null   # 仅 primary = Incommensurability 时填写，结构见 schema.md
    makadok_dimension: "Mechanism"
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    conversation_strategy: "Progressive"   # Progressive | Synthesized | Non-Coherence
  contribution_contract:
    - claim: "..."
      makadok_dimension: "Mechanism"
```

> 完整片段模板（含 incommensurability_resolution 展开结构）：`../write-introduction/references/paper-state-schema.md`。新输出只写 canonical `story` 与 v1.3 字段，不再写 `central_knot_statement`、`narrative_arc`、`core_constructs` 等重复别名（迁移映射见 schema.md 文末）。

用户复制到 paper-state.yaml 中（或用 `--paper-state` 参数指向该文件时自动填充）。

## 4.2 write-theory 启动时

Phase 0 增加自动检查：

```
[paper-state.yaml] 检测到 paper-state.yaml
  → introduction.status = drafted
  → 自动加载 theory_hints:
      gap_type: Inadequacy
      recommended_theory_variant: 机制推演型 (B)
      promised_hypothesis_count: 2
  → 跳过交互式类型诊断，直接进入确认模式
  → 默认推荐: 机制推演型 (B)
  → 用户只需确认或调整
```

如果 paper-state.yaml 不存在：回退到交互式询问（当前行为）。

## 4.3 write-theory 完成后

输出追加 paper-state.yaml 片段：

```yaml
theory:
  status: drafted
  output_path: "outputs/theory_v2.md"
  theory_variant: "机制推演型 (B)"
  constructs:
    independent: "CEO promotion focus"
    dependent: "time to recall (days)"
    mediator: "weighting of timing error type I (premature recall)"
    moderator: null
    controls: ["firm size", "ROA", "leverage", "board independence"]
  hypotheses:
    - id: "H1"
      storyline_id: "S1"
      statement: "CEO promotion focus is negatively associated with time to recall."
      type: "main"
      predicted_direction: "negative"
    - id: "H2"
      storyline_id: "S1"
      statement: "CEO prevention focus is positively associated with time to recall."
      type: "main"
      predicted_direction: "positive"
  mechanism_chains:
    - "promotion focus → sensitivity to opportunity costs of delay → overweighting type I error (premature recall) → shorter time to recall"
    - "prevention focus → sensitivity to reputational costs of error → overweighting type II error (delayed recall) → longer time to recall"
```
