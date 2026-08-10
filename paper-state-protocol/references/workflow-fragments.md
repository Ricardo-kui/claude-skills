# 工作流片段示例（§4）

## 4.1 write-introduction 完成后

用户在 write-introduction 输出末尾收到以下追加块：

```yaml
# --- paper-state.yaml 片段（复制到你的 paper-state.yaml）---
introduction:
  status: drafted
  output_path: "outputs/intro_v3.md"
  theory_hints:
    gap_type: "Inadequacy"
    makadok_dimension: "Mechanism"
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    central_knot_statement: "..."
    narrative_arc: "moderate_rise"
    core_constructs: ["CEO regulatory focus", "time to recall"]
  contribution_contract:
    - claim: "..."
      makadok_dimension: "Mechanism"
```

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
