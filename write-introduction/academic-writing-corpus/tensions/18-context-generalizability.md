---
type: canonical_tension
canonical_id: "18-context-generalizability"
status: EMERGING
gap_type: Inadequacy (context-bound evidence)
cross_paper: EMERGING
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - li_bapuji_talluri_singh_venkataraman_2026_pom (POM, 2026): "WEIRD-bound geographical-distance→quality-risk prediction reversed/offset in non-WEIRD (Chinese) context via institutional-gradient direction"
created: 2026-07-22
source: Distilled by distill-introduction-exemplar from Li, Bapuji, Talluri, Singh & Venkataraman (2026), POM
---

# 18-context-generalizability — WEIRD↔non-WEIRD 情境泛化性 Tension

## 功能描述

当某 field 的现有证据**几乎全部来自 WEIRD（Western, Educated, Industrialized, Rich, Democratic）/ 发达市场语境**，但目标现象在非 WEIRD / 新兴市场语境中可能因**制度、文化或市场结构差异**而方向或强度不同时，用"情境泛化性"建立 gap：不是简单"缺非 WEIRD 样本"，而是论证 WEIRD-bound 的**因果机制在非 WEIRD 语境下可能不成立或被抵消**。

核心逻辑：`[WEIRD-bound finding] holds because [mechanism A in WEIRD contexts]; in [non-WEIRD contexts], [structural difference] makes [mechanism A reverse / be offset by mechanism B], so the prediction may not generalize.`

## 适用场景

- Gap 类型 = **Inadequacy**（现有证据 context-bound，对其他语境可能产生错误推断）
- 目标 field 的实证证据集中在 WEIRD / 发达市场
- 能论证同一自变量在非 WEIRD 语境下**机制方向反转 / 被抵消**（而非仅"样本不同"）
- 有跨 field 的 WEIRD-generalizability 呼吁可引用（Barkema et al. 2015; Henrich et al. 2010; Pitesa & Gelfand 2023; Wickert et al. 2024）
- 目标期刊接受 context-sensitive theorizing（POM/JOM/JBS/IB 期刊）

## 能量级

**中** — 不靠反例颠覆共识，而靠"语境差异改变机制"建立张力

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): li_bapuji_talluri_singh_venkataraman_2026_pom (POM)
- WEIRD-generalizability 是跨 field 增长议程（心理学 Arnett 2008、管理 Barkema 2015、IB），多 source 后可升 VERIFIED

### 生成力
- **GENERATIVE**: 任何"WEIRD-bound 机制 + 可论证非 WEIRD 机制差异"的研究都可套用

### 排他性
- **HIGH**: 仅当能论证机制在非 WEIRD 语境下方向/强度不同时使用；若只是"缺样本"而无机制差异 → 用 Incompleteness（01-despite-progress）

---

## 句法模板

### 变体 A：制度梯度方向反转型（li_venkataraman_2026_pom 型）

**模板**:
> "Prior empirical research on [topic] has predominantly been conducted in [WEIRD / developed-market] contexts ([citations]). In these settings, [core WEIRD-bound finding] because [mechanism A]. However, this prediction may not generalize to [non-WEIRD / emerging-market] settings. [In WEIRD contexts, focal firms [source down the institutional gradient — e.g., to weaker-institution suppliers], so [mechanism A produces the predicted effect]]. In contrast, [in non-WEIRD contexts, focal firms [source up the institutional gradient — e.g., to stronger-institution suppliers], so [the same variable's effect is reversed / offset by an opposing force]]. By failing to consider differences in [institutional context] between [WEIRD] and [non-WEIRD] countries, research on [topic] risks generating erroneous implications for theory and practice. We examine [topic] in [non-WEIRD context] to [test the generalizability / reveal the context-dependence] of [WEIRD-bound prediction]."

**原文锚定**:
> "prior empirical research on supply chain geographical complexity has mostly been conducted in research contexts that are Western, educated, industrialized, rich, and democratic (WEIRD; Henrich et al. 2010). Firms from WEIRD countries source down the institutional gradient and thus geographical distance increases risks for firms (Steven and Britto 2016). However, similar risks may not affect firms from non-WEIRD countries if they source up the institutional gradient or source from a combination of domestic and foreign suppliers from WEIRD countries. By failing to consider differences in institutional contexts between WEIRD and non-WEIRD countries, research on supply chain geographical complexity risks generating erroneous implications for theory and practice."

**来源**: li_bapuji_talluri_singh_venkataraman_2026_pom (POM), §1 P3

**关键特征**:
- **机制层差异，不是 sampling gap**: WEIRD 样本不是缺口本身——缺口是 WEIRD-bound 的因果机制在非 WEIRD 语境下可能不成立。"source down vs up the institutional gradient" 是标志句
- **"institutional gradient" 方向论证**: WEIRD 企业向下外包（弱制度供应商）vs 非 WEIRD 企业向上外包（强制度供应商）→ 同一变量（如地理距离）的效应方向可能相反或被抵消
- **风险升级**: "risks generating erroneous implications" —— 把 gap 从"值得补充"升级为"不加检验会产生错误理论/实践建议"
- **可配 "asset of foreignness" / 制度替代逻辑**: 强制度供应商环境可替代买方监督（liability → asset）

**适用**: 任何 field 中证据集中在 WEIRD/发达市场、但能论证同一机制在新兴市场因制度/文化/市场结构差异而方向或强度不同的研究。li_venkataraman_2026_pom POM（地理距离→质量风险）；可迁移到 IB、战略、组织、营销的"context-sensitive theorizing"议程。

**禁忌**:
- 必须论证"**为何非 WEIRD 不同**"（机制层），不能只说"prior research used WEIRD samples"（那只是 sampling gap → 用 Incompleteness 01）
- "institutional gradient" 等方向论证必须有理论/实证支撑，不能空断
- 不要把"非 WEIRD"当控制变量或背景条件而非理论变异来源

---

## 组装规则

### 必须配对
- **与 `write-methods` slot-M3「context-customized DV / measurement」配对**: 非 WEIRD 研究不能直接照搬 WEIRD 的测量（如 product recall 在弱制度语境下被低估 → 用 consumer complaints；观测窗口随语境调校）。gap 声称语境不同，methods 就必须相应调校测量
- **与 "context as theoretically consequential" contribution 配对**: Discussion/Contribution 须显式把"empirical context"从背景条件提升为理论变异来源
- **与 posthoc moderator that reveals the offsetting force 配对** (write-results R6): 若主效应在非 WEIRD 为 null/反转，须用一个揭示抵消力的 posthoc moderator 解释（如 li_venkataraman_2026_pom: supplier-country regulatory quality moderates distance→risk，解释 H1 null）

### 互斥
- **不能与单纯 Incompleteness (01-despite-progress) 同用**: 若只是"缺非 WEIRD 样本"而无机制差异论证，用 01；本模板要求机制层差异

### 反模式提醒
- **"WEIRD samples" 空喊**: 只列 WEIRD 局限而无机制反转论证 → 不是情境泛化性 gap
- **照搬 WEIRD 测量**: gap 声称语境不同却用同一 DV/窗口 → 自相矛盾（须配 context-customized measurement）
- **过度声称非 WEIRD 独特性**: 若机制在两种语境实际相同，不要强行声称泛化失败

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| POM/JOM/MSOM | ⭐⭐⭐ 极高 | 运营/供应链研究正经历"去 WEIRD 化"，本模板高度适配 |
| JIBS/GSJ/IB 期刊 | ⭐⭐⭐ 极高 | IB 本就是 context-sensitive theorizing 主场 |
| SMJ/AMJ | ⭐⭐ 高 | 需强机制论证，避免"样本不同"式肤浅 gap |
| ASQ/OS | ⭐⭐ 中 | 偏好深理论；须把语境差异提升到理论机制层 |
| JM/JMR | ⭐⭐ 中 | 消费者行为 WEIRD 偏严重，适配但需消费者层机制 |

---

## 诚实边界

- **EMERGING 状态**: 当前 1 篇范文。WEIRD-generalizability 是跨 field 增长议程，但本 canonical 模板需更多 source 验证其句式稳定性
- **不可降格为 sampling gap**: 若无法论证机制在非 WEIRD 语境下方向/强度不同，改用 Incompleteness（01-despite-progress-unaddressed）
- **"context" 不可只做控制变量**: 本 gap 的理论承诺是 context 为 theoretically consequential —— Discussion 必须兑现（把发现框为"context-dependent"而非"universal"）
- **须诚实报告 null/反转**: 若 WEIRD 预测在非 WEIRD 为 null/反转，必须如实报告并用 posthoc 机制解释，不能隐藏
