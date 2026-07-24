# paper-state.yaml 输出片段（Theory → 下游）

> 外置自 `write-theory/SKILL.md` 下游接口节。Theory 骨架输出末尾自动附加以下片段；用户复制到项目 `paper-state.yaml` 的 `theory:` 节下，供 write-methods Phase 1 和 write-results Phase 0 自动消费。

Theory 骨架输出末尾自动附加以下片段。用户复制到项目 `paper-state.yaml` 的 `theory:` 节下，供 write-methods Phase 1 和 write-results Phase 0 自动消费：

```yaml
# --- paper-state.yaml 片段 (copy to your paper-state.yaml) ---
theory:
  status: drafted
  output_path: "[本次输出文件路径]"
  depends_on: ["introduction"]
  updated: "[YYYY-MM-DD]"

  theory_variant: "[A 构念辨析型 / B 机制推演型 / C 假设树型 / D 质性过程理论型 / E 调节效应型 / F 竞争假设型 / G 辩证对立型]"

  constructs:
    independent: "[核心自变量名称]"
    dependent: "[核心因变量名称]"
    mediator: "[中介变量，如无则为 null]"
    moderator: "[调节变量，如无则为 null]"
    controls: ["[控制变量1]", "[控制变量2]", ...]

  hypotheses:
    - id: "H1"
      storyline_id: "S1"
      statement: "[H1 完整陈述句]"
      type: "main"              # main | mediation | moderation | competition
      iv: "[H1 自变量]"
      dv: "[H1 因变量]"
      predicted_direction: "[positive / negative / curvilinear]"
    # - id: "H2"
    #   storyline_id: "S2"
    #   ...

  mechanism_chains:
    - "[H1 机制链: 起点触发条件 → 第二步推理 → ... → 终点可检验预测]"
    # - "[H2 机制链]..."
```
