---
design_type: "匹配DiD-广义DiD"
status: EMERGING
source_papers:
  - Castellaneta_Conti_Kacperczyk_2017_SMJ (SMJ; CEM on ex-ante size + industry uncertainty as staggered-law DiD robustness)
variants_count: 1
created: 2026-05-18
updated: 2026-08-05
---
# 匹配DiD-广义DiD — Methods 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | CEM 匹配 ex-ante 价值代理 + 风险代理（准实验 DiD 稳健性） | 政策/交错 DiD 主识别之后，需用匹配抗辩 ex-ante 可比性、威胁声明与匹配维度一一对应（价值代理、风险代理）时（槽位 M8） | 区别于 `PSM匹配面板` 的 CEM 五步链——说服焦点是威胁声明→双代理匹配维度→CEM→稳健性位置，而非匹配算法细节 | EMERGING | Castellaneta, Conti & Kacperczyk 2017 SMJ |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `匹配DiD-广义DiD` 专用变体）。

## 设计特征摘要

- **核心问题**: 准实验/交错政策 DiD 中，处理组与对照组在冲击前可能在价值或风险维度上系统不同，且这些维度可能同时影响政策采纳与结果。
- **匹配角色**: 匹配通常作为 **稳健性/抗辩**（非主识别），在主 DiD/准实验规格之后重建 ex ante 可比性。
- **与 PSM匹配面板 分工**: `PSM匹配面板.md` 服务面板/生存语境下的 CEM/PSM/EBM 主流程；本文件服务 **政策 DiD / 广义 DiD** 语境下的匹配抗辩叙事。
- **诚实边界**: 匹配只处理可观测选择；不可替代政策外生性论证、平行趋势或现代 staggered-DiD 估计器。

## 累积变体

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->

### 变体 1：CEM 匹配 ex-ante 价值代理 + 风险代理（准实验 DiD 稳健性）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "In a quasi-experimental setting, this ideal condition is less likely to hold, which could be a concern if the treated firms are ex ante different from control firms along some characteristics that correlate with both our treatment (i.e., UTSA enactment) and our outcome (i.e., change in firm market value). To account for such potential confounders, we reestimate the baseline specifications, while also matching the treatment and control firms on the basis of ex ante investment size, which proxies for the target's ex ante value, and industry resource–value uncertainty, which proxies for the target's business riskiness (Acharya et al., 2013; Castellaneta and Zollo, 2015; Shepherd, 1999)."

**验证状态**: EMERGING（单篇；`section_variant`；本设计类型首填）

**槽位**: M8（Matching robustness under quasi-experiment）

**骨架**:
> "In any experimental setting, random assignment establishes ex ante symmetry between treatment and control groups. In a quasi-experimental setting, this ideal is less likely to hold if treated [units] differ ex ante along characteristics that correlate with both treatment ([law/policy] enactment) and [Δoutcome]. Importantly, either the level of ex ante [risk] or the expected [value] of a [unit] may correlate with the change in [outcome] or with policymakers' effort to enact [law]—for instance, to protect riskier or more valuable [units]. To account for such confounders, we reestimate the baseline specifications while matching treatment and control on ex ante [investment size / value proxy] and [industry resource-value uncertainty / risk proxy] ([citations]). We use coarsened exact matching (CEM) as developed by [Iacus, King & Porro / citation]. Results remain robust on the matched sample ([table/appendix])."

**与原骨架差异**: 首次填充本设计类型。区别于 `PSM匹配面板` / `生存分析` 中的 CEM 五步链——本变体的说服焦点不是匹配算法细节，而是 **威胁声明（ex ante value/risk ↔ 政策采纳与 ΔV）→ 双代理匹配维度 → CEM → 稳健性位置**。匹配维度与理论混淆通道一一对应（价值代理、风险代理）。

**边界**:
- 须报告匹配后 N / 平衡表；仅说"results remain robust"不可审计。
- CEM 不解决不可观测混淆；应与政治经济外生性检验、安慰剂等并列，而非替代。
- 若主识别已是随机实验，此抗辩冗余。
