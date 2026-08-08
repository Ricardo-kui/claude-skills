---
result_type: "匹配DiD"
status: 🧪 EMERGING
source_papers:
  - castellaneta_conti_kacperczyk_2017_smj (Strategic Management Journal; DOI 10.1002/smj.2533)
variants_count: 1
created: 2026-05-18
updated: 2026-08-05
---
# 匹配DiD — Results 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | CEM 匹配作准实验事前对称威胁回应 | DiD/准实验把 CEM 作事前组间不对称威胁的稳健性回应：威胁句→匹配变量理论代理→CEM 引用→附录平衡表指针→remain robust（槽位 R7） | 首次填充匹配DiD——matching-as-robustness（主估计仍为 DiD-equivalent OLS），非 matched DiD 作唯一主规格；只处理可观测选择 | 待交叉 | Castellaneta, Conti & Kacperczyk 2017 (SMJ) |


## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `匹配DiD` 专用变体）。

## 证据节奏摘要

- **CEM 作 DiD/准实验稳健性**（Castellaneta et al. 2017）：匹配不是主估计器，而是回应“处理组与对照组事前不对称”威胁；匹配变量须是 ex-ante value / risk 代理，并指向平衡表附录。
- 完整识别电池（政治经济、供需、placebo 等）见 `DiD.md` 变体 9；本文件只沉淀**匹配步骤本身**的可迁移写法。

## 累积变体

<!-- distill-results-exemplar Phase 4 验证通过的变体写入此处 -->

### 变体 1：CEM 匹配作准实验事前对称威胁回应（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)

**原始句锚点**: We used a coarsened exact matching (CEM) approach as developed by Iacus, King, and Porro (2009) to perform a match between treatment and control. As shown in Table S2, our results remain robust.

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: R7

**story_fidelity**: falling_action（unravel selection-on-observables confound）

**骨架**:
> "In a quasi-experimental setting, random assignment is less likely to hold, which is a concern if treated [units] differ ex ante from controls on characteristics that correlate with both [treatment] and [outcome]. For instance, [ex-ante value] or [business risk] may correlate with policymakers' effort to enact [policy] or with subsequent [outcome] change. To account for such potential confounders, we re-estimate the baseline specifications while matching treatment and control on [value proxy] and [risk proxy]. We use coarsened exact matching (CEM) (Iacus, King, and Porro, 2009). As shown in [appendix balance/results table], our results remain robust."

**与原骨架差异**: 首次填充「匹配DiD」结果类型；本变体是 **matching-as-robustness**（主估计仍为 DiD-equivalent OLS），不是 matched DiD 作为唯一主规格。强调威胁句（ex ante asymmetry）→ 匹配变量理论代理 → CEM 引用 → appendix 指针 → remain robust。

**诚实边界**:
- CEM 只处理可观测事前差异；不可声称已解决不可观测选择。
- 须报告匹配变量；若正文不放平衡统计，附录须有，且正文至少一句“remain robust”。
- 若匹配后样本量骤降，须报告保留 N，不得只报显著性不变。
