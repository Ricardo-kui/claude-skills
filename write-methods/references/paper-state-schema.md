# Paper-State Schema — Methods 输出片段（从 SKILL.md 下沉，v0.1）

> 由 write-methods 输出末尾**对照使用**：附加 `### paper-state.yaml 片段` 块，供 write-results Phase 0 自动消费。
> 字段与 `../paper-state-protocol/references/schema.md` 权威 schema 对齐；本文件只定义 methods 节的特有片段模板，协议层通用字段语义以 protocol 为准。

Methods 骨架输出末尾自动附加以下片段。用户复制到项目 `paper-state.yaml` 的 `methods:` 节下：

```yaml
# --- paper-state.yaml 片段 (copy to your paper-state.yaml) ---
methods:
  status: drafted
  output_path: "[本次输出文件路径]"
  depends_on: ["theory"]
  updated: "[YYYY-MM-DD]"

  design_type: "[面板数据/OLS / 自然实验/DiD / 生存分析 / IV/2SLS / ...]"
  estimator_family: "[OLS / FE / Logit / Cox / DiD / IV/2SLS / ...]"

  sample:
    source: "[数据来源描述]"
    n_observations: [N]
    n_firms: [N]
    time_window: "[YYYY-YYYY]"
    inclusion_criteria: ["[criterion 1]", "[criterion 2]"]

  variables:
    dv: "[因变量名]"
    iv: "[核心自变量名]"
    mediator: "[中介变量名，如无则为 null]"
    moderator: "[调节变量名，如无则为 null]"
    controls: ["[控制变量1]", "[控制变量2]", ...]
    fixed_effects: ["[firm]", "[year]"]

  hypothesis_variable_map:
    H1: {storyline_id: "S1", predictor: "[var name]", outcome: "[var name]", model: "[model label]"}
    # H2: {predictor: "...", outcome: "...", model: "..."}

  story_alignment:
    central_knot: "[从 story.central_knot 引用，不改写]"
    design_resolution_logic: "[为什么该设计能回答 theme question]"
    storyline_model_map:
      S1:
        hypotheses: ["H1"]
        constructs: ["[构念]"]
        variables: ["[操作变量]"]
        model_or_step: "[模型、实验比较或质性分析步骤]"
        identification_burden: "[需要满足的识别或效度条件]"
    unresolved_validity_threats: ["[尚未解决的 threat；无则为空列表]"]

  results_preview: "[M10 预告段的核心内容摘要]"

  # 新增 v3.0.0 — 稳健性计划。由 write-results 决策诊断填充，或手动填写。
  # 供 write-results 跳过诊断直接生成 R7 段落。
  robustness_plan:  # 可选；不存在时 write-results 自动触发决策诊断
    mandatory: ["[必须检验的维度]"]
    recommended: ["[建议检验的维度]"]
    optional: ["[可选检验的维度]"]
    excluded:
      "[维度名]": "[排除理由]"
```
