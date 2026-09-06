# Paper-State Schema — Results 输出片段（从 SKILL.md 下沉，v0.1）

> 由 write-results 输出末尾**对照使用**：附加 `### paper-state.yaml 片段` 块，供 paper-review 和 results-review 消费。
> 字段与 `../paper-state-protocol/references/schema.md` 权威 schema 对齐；本文件只定义 results 节的特有片段模板，协议层通用字段语义以 protocol 为准。

```yaml
# --- paper-state.yaml 片段 (copy to your paper-state.yaml) ---
results:
  status: drafted
  output_path: "[本次输出文件路径]"
  depends_on: ["methods"]
  updated: "[YYYY-MM-DD]"

  estimator_family: "[OLS / FE / Logit / Cox / DiD / IV/2SLS / ...]"

  hypothesis_results:
    H1: {direction: "[positive / negative / null]", significant: [true / false], baseline_verdict: "[supported / partially_supported / not_supported]", overall_evidence: "[stable / qualified / mixed / unresolved]"}
    # H2: {direction: "...", significant: ..., baseline_verdict: "...", overall_evidence: "..."}

  story_resolution:
    headline_answer: "[对 theme question 的证据约束式回答]"
    storylines:
      S1:
        status: "[supported / mixed / unsupported / unresolved]"
        evidence: ["[table/model/estimate or qualitative evidence]"]
        magnitude: "[效应量或明确说明无法估计]"
    surprises: ["[意外、反方向或敏感性发现；无则为空列表]"]
    unresolved_questions: ["[仍无法回答的问题；无则为空列表]"]

  key_findings:
    - "[核心发现1：一句话总结，含方向和幅度]"
    # - "[核心发现2]..."

  unexpected_findings:
    # 无意外发现时为空列表
    # - "[反直觉/意外发现：一句话描述]"

  robustness_plan:  # 由稳健性决策诊断生成（Yuan et al. 2026 JOM）
    mandatory: ["[必须检验的维度]"]
    recommended: ["[建议检验的维度]"]
    optional: ["[可选检验的维度]"]
    excluded:
      "[维度名]": "[排除理由]"

  revision_constraints:
    hypothesis_order: ["H1", "H2"]
    section_order: []
    terminology_required: []
    terminology_prohibited: []
    language_locks: []
    active_feedback_rule_ids: []

  validation:
    source_fidelity: "[pass / fail]"
    analysis_unit_logic: "[pass / fail]"
    paragraph_cohesion: "[pass / fail]"
    language_locks: "[pass / fail]"
    mixed_evidence_disclosure: "[pass / fail]"
```
