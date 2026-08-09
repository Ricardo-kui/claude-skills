# Paper-State Schema — Results 输出片段（从 SKILL.md 下沉，v0.1）

> 由 write-results 输出末尾**对照使用**：附加 `### paper-state.yaml 片段` 块，供 paper-review 和 results-review 消费。

```yaml
# --- paper-state.yaml 片段 (copy to your paper-state.yaml) ---
results:
  status: drafted
  output_path: "[本次输出文件路径]"
  depends_on: ["methods"]
  updated: "[YYYY-MM-DD]"

  estimator_family: "[OLS / FE / Logit / Cox / DiD / IV/2SLS / ...]"

  hypothesis_results:
    H1: {direction: "[positive / negative / null]", significant: [true / false], supported: [true / false]}
    # H2: {direction: "...", significant: ..., supported: ...}

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
```
