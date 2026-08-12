---
result_type: "Tobit"
status: 🟢 EMERGING
source_papers:
  - "ridge_et_al_2024_amj (Academy of Management Journal): Tobit left-censored conditional-magnitude four-beat + practical-importance anchor; dual-DV dual-estimator (Tobit + Negative Binomial) design"
variants_count: 1
created: 2026-08-12
updated: 2026-08-12
---

# Tobit — Results 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| R3 | 1 | 1 |

### R3（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | Tobit 左删失 DV 条件幅度四拍 + 实际重要性拍5 | 左删失连续 DV（corner-solution）主效应：方向→系数+p→条件幅度（among units that engage in at least some activity）→支持 + 外部文献锚定实际重要性 | 与计数 IRR+AME 双轨、OLS 标准四拍的区别——拍3 必须限定删失条件期望（conditional on participation），拍5 用外部证据证明小变化重要 | 待交叉 | Ridge et al. 2024 AMJ |

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `Tobit` 专用变体）。

## 证据节奏摘要

- **Tobit / corner-solution**: 系数→方向解释→条件幅度（"among firms that engage in at least some activity"）→支持判断
- **与 OLS 的关键区别**: DV 左删失（未参与 = 0），拍3 幅度必须限定在参与子样本的条件期望上，不能给全体样本的无条件幅度
- **与计数模型的关键区别**: 不用 IRR/AME/predicted count，用条件百分比变化（±1 SD → X% change among participants）
- **实际重要性**: 嵌入 R3 拍5——用外部文献证明微小变化净显著收益（tax rate savings / contracts / performance）

## 累积变体

### 变体 1: Tobit 左删失 DV 条件幅度四拍 — 条件幅度 + 实际重要性拍5 (1篇高价值)
**来源论文**: Ridge, Kim, Ingram & Lee 2024 (Academy of Management Journal)
**原始句锚点**: "Lobbying breadth is left-censored since not all firms engage in lobbying activity, and thus we use a Tobit analysis for this dependent variable. ... as CEO paranoia increases from the mean to one standard deviation (i.e., +1 SD) above the mean, the firm exhibits approximately a 7% decrease in lobbying breadth among firms that engage in at least some lobbying activity."
**验证状态**: 待第二篇交叉验证（EMERGING / 单篇 section_variant）
**写入日期**: 2026-08-12
**槽位**: R3
**骨架**:
> Hypothesis [x] predicted a [negative/positive] relationship between [predictor] and [outcome]. The coefficient in Model [y] of Table [z] is [negative/positive] and statistically significant ([coefficient], p = [value]), supporting Hypothesis [x]. As [predictor] increases from the mean to one standard deviation above the mean, [outcome] decreases by approximately [value]% among [units] that engage in at least some [activity]. Evidence suggests that even small changes in [outcome] can net significant benefits such as [external evidence], so the [value]% change is likely to be particularly important in practice.
**与原骨架差异**: Tobit/corner-solution 估计器是 corpus 静态缺口（registry 零命中）。本骨架是 Tobit 左删失 DV 的四拍：拍3 用**条件幅度**——±1 SD 变化在"至少参与部分 [activity]"的样本上的百分比变化（删失条件期望），而非全体样本的无条件幅度；拍5 用**外部文献锚定实际重要性**（即使微小变化也能带来显著收益，如税收节省）证明 7% 的量级"likely to be particularly important in practice"。与计数模型变体 1（predicted count change）和 OLS 标准四拍（Y-unit change）的区别在于必须限定参与子样本。

**诚实边界**:
- Tobit 必须报告删失结构：左删失比例 / censoring 机制（为什么未参与 = 0 而非缺失），否则审稿人无法判断删失假设是否成立。
- 拍3 条件幅度必须明确是"among [units] that engage in at least some [activity]"——不能给全体样本无条件幅度，那会低估参与者的效应。
- 保留 95% CI 报告要求（Ridge et al. 原文未报 CI，是本文可改进点，不作模板）。
- 因果语言保持关联语气（"associated with" / "supports Hypothesis"），非实验设计不越级。

---

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **Tobit 只报系数不报删失结构** | 未说明左删失比例 / 未参与为何编码为 0 | 在 R1/R2 报告删失比例与 censoring 机制 |
| **Tobit 幅度用全体样本无条件解释** | ±1 SD 幅度翻译到全部观测而非参与者 | 拍3 限定 "among firms that engage in at least some activity" |

## 诚实边界

- **删失比例透明**: R1/R2 必须报告左删失观测比例；删失假设（未参与 = 0）需在 Methods 论证。
- **条件幅度纪律**: 幅度翻译限定参与子样本（conditional expectation），不给出无条件幅度。
- **CI 要求**: 标准骨架含 95% CI（本文原文缺 CI，不沿用为模板）。
- **因果语言**: 关联语气；"support Hypothesis" 是支持判断，非因果声称。
