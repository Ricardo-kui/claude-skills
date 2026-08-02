---
result_type: "DiD"
status: 🧪 EMERGING
source_papers:
  - lee_wu_bednar_orsc_18968 (Organization Science; DOI 10.1287/orsc.2024.18968)
variants_count: 2
created: 2026-05-18
updated: 2026-08-02
---

# DiD — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `DiD` 专用变体）。

## 证据节奏摘要

- 条件化 DiD 不能停在交互项显著：需翻译幅度、画出条件效应两端，并逐端核对理论预测。
- 补充分析可从“另一 DV”升级为“逐项探测理论前提”，但关联性结果只能提高机制可信度。
- 设计诊断按威胁组织；传统 TWFE 权重分解只作诊断，不作现代识别修复。

## 累积变体

<!-- distill-results-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: R?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

### 变体 1：交互项 → 幅度 → 双端条件效应 → 假设逐端核对（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R4 + R5 + R6

**骨架**:
> "The interaction between [treatment] and [moderator] is [direction] and statistically significant (β = [value], p [threshold]). Moving [moderator] from [low benchmark] to [high benchmark] changes the estimated treatment effect by [substantive magnitude]. Figure [x] shows that the treatment effect is [sign/direction] when [moderator] is high and [sign/direction] when it is low. The high-[moderator] pattern is consistent with the predicted [path A]. However, the low-[moderator] effect is [observed pattern], rather than the predicted [pattern]; therefore, the interaction supports the contingency but Hypothesis [x] receives only partial/no support as stated. [Clearly labeled post-hoc explanation, deferred or bounded]."

**与原骨架差异**: 把“交互项显著”与“完整支持符号反转假设”分开判定；假设若预测两端方向，必须逐端兑现。

**关键诚实规则**:
- significant interaction ≠ both simple effects have the predicted signs。
- 经济幅度要说明基准范围；不能只把 β 换算为百分比而不说相对谁。
- 意外一端的解释必须标为 post hoc，且不能回写成事前假设。

### 变体 2：理论前提探测式补充证据链（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R8（Mechanism / Corroborative Evidence）

**骨架**:
> "We next probe the observable implications of the proposed mechanism. First, we examine [communication/trace outcome] to assess whether actors adjust not only [core behavior] but also its visibility. Second, we test whether [communication capacity] conditions the response as the theory implies. Third, we examine whether [behavior] is associated with subsequent attention from each proposed intermediary. The pattern for [intermediaries A/B] is consistent with the visibility premise, whereas the null result for [intermediary C] suggests that this actor may operate through [domain-specific alternative function]. These analyses corroborate selected premises but do not identify the causal mechanism."

**与原骨架差异**: 不是罗列额外 DV；每个分析对应一个明确可观察的理论前提，并允许不同中介出现领域特定 null。

**关键诚实规则**:
- 将行为回归到中介关注度的关联不能证明 `behavior → visibility → outcome` 因果链。
- domain-specific null 应缩窄理论适用范围，不应被“总体大致一致”吞掉。
- 补充结果若与主结果同源或同样受未观测混淆，只能称 corroborative / consistent with。
