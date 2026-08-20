# Phase 0 — 估计器类型与 Results 结构分类

> **输入纪律（2026-08-20 起）**：若输入来自 distill-paper-exemplar 编排（PDM 工作目录），
> 只读 `<citekey>.pdm/sections/<本节>.md` 物化切片；需要全文上下文时读
> `fulltext.text-only.md`。**禁止直接读原始 paper-import MD**——其中 44–89% 字节是
> base64 图片单行巨串，读入即炸上下文。单独调用本 skill 且只有原始 MD 时，先运行
> `distill-paper-exemplar/scripts/preprocess_l0.py <MD>` 再读产物。

在读取 Results 正文前，先判断该 Results 的**证据架构**，决定后续槽位检查清单和蒸馏焦点。

## 分类维度

| 维度 | 选项 |
|------|------|
| 估计器 | OLS/FE / Logit/Probit/Ordered Probit / 生存分析 / DiD / 计数模型 / IV/2SLS / 匹配DiD / 堆叠扩散Logit / 实验(ANOVA/OLS) |
| 假设结构 | 纯主效应 / 主效应+交互 / 主效应+中介 / 三向交互 / 构造暴露分解 |
| 稳健性组织 | 按 threat 组织 / 按表格机械罗列 / 混合 |
| 预处理变异报告 | 有 / 无（新增 v1.2.0 — Yuan et al. 2026 JOM） |
| 协变量变异报告 | 有 / 无（新增 v1.2.0 — Yuan et al. 2026 JOM） |
| 非显著处理 | 全部报告 / 选择性报告 / 仅在附录 / 混合 |
| 经济显著性 | 嵌入主效应 / 独立段落 / 缺失 |
| 图形使用 | 交互图 / 平行趋势图 / AME 区域显著性图 / 无 |

## 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_results_profile:
  estimator_family: "OLS/FE / Logit / DiD / ..."
  hypothesis_structure: "主效应 / 主效应+交互 / 主效应+中介 / ..."
  robustness_organization: "按 threat / 按表格 / 混合"
  preprocessing_variation_reported: true/false  # 新增 v1.2.0
  covariate_variation_reported: true/false  # 新增 v1.2.0
  nonsignificant_reporting: "全部报告 / 选择性 / 附录 / 混合"
  economic_significance_placement: "嵌入R3 / 独立R5 / 缺失"
  figure_types: ["交互图", "平行趋势", ...]
  hypotheses_tested: ["H1", "H2", ...]
  nonsignificant_findings: ["H4"]  # 仅列编号，不计数
```
