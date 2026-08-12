# 跨节一致性检查（L2 Rubric）— v1.0

目的：在同一篇论文上，校验四节 identity 是否互相印证。**只标记，不擅改**——论文自身的
不一致是值得蒸馏的学习信号（story 卡的 assessment 会用到），不是错误。四节 identity
抽取自 PDM `distill_track.*.identity`，由主循环在节蒸馏完成后填充；单节模式标 `unknown`。

## 四联 identity

| 节 | 字段 | 含义 | 来源 skill |
|---|---|---|---|
| Introduction | `gap_type` | Inadequacy / Incompleteness / Incommensurability … | distill-introduction-exemplar |
| Theory | `theory_building_type` | 构念辨析 / 机制推演 / 过程理论 / 调节 / 竞争假设 / 辩证对立 … | distill-theory-exemplar |
| Methods | `design_family` | 面板-OLS / 自然实验-DiD / 生存分析 / IV / 非线性模型 / 多研究 … | distill-methods-exemplar |
| Results | `estimator_family` | OLS-FE / DiD / Logit-Probit / 计数模型 / 生存分析 … | distill-results-exemplar |

## 检查项（全部 flag-only）

| # | 检查 | 比较什么 | 什么算 flag |
|---|---|---|---|
| C1 | gap → theory | intro 的 gap_type 与 theory 的构建类型是否同型 | Incommensurability 却无对立/裁决结构；Inadequacy 却无构念或机制修订；Incompleteness 却无机制延伸 |
| C2 | methods → results 估计器 | design_family 与 estimator_family 是否同族 | 生存设计配非生存结果；DiD 设计配纯 OLS 报告（无事件研究/稳健估计）；计数 DV 未配计数模型 |
| C3 | theory → methods 实证舞台 | theory 承诺的机制/调节是否在 methods 有对应设计 | 有中介/调节假设却无对应机制测试设计；有多 actor/多路径 story 却无相应设计 |
| C4 | intro 承诺 → results 兑现 | intro 预告的 reader_shift / 曲线 / 对比 是否在 results 有 answer | intro 承诺曲线/对比，results 未报告对应检验 |
| C5 | knot → discussion 收束（轻） | central_knot 是否在 discussion 被回应 | knot 提出后无任何收束 |

## 输出

```yaml
cross_section_identity:
  coherence: ok | flagged | partial
  flags:
    - check: C1
      observation: "intro 标 Incommensurability，theory 无对立裁决结构"
      severity: info | warn
      source: introduction
      target: theory
```

- `ok`：全部检查通过（或仅 info）。
- `flagged`：≥1 条 warn。
- `partial`：单节模式或 identity 未就位（≥1 字段 unknown）。

## 裁决纪律

- **不自动修正**：任何 flag 呈现给用户，由用户决定是"论文自身的张力（学习点）"还是"需
  复核抽取"。二者都是可接受结果。
- **跨节传递**：`flagged` 的论文在 L3 把 flags 作为 story 卡 assessment 的参考输入
  （`story_track.fed_flags: true`）——论文内部不一致、promise 未兑现，正是
  distill-story-exemplar 的 "imperfect paper" 学习模式。
- 检查以提示为主，不做重校验；C5 为可选，单节模式跳过。

## 与现有机制的关系

- `paper-story-contract/references/distillation-gate.md` 管**单变体**的 story_fidelity
  （core_candidate / section_variant / ritual_only / reject）——本 rubric 管**同一论文**
  的四节一致性，两者正交。
- `paper-story-contract/references/schema.md` 的 storyline 一致性（`storyline_id` /
  `story_alignment` / `story_resolution`）是**项目侧**（用户自己论文）的契约；本 rubric 是
  **范文侧**。不混用。
