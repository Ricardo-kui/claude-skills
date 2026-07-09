<!--
pattern_id: board_governance_boundary_condition
build_type: 调节效应型
source_papers: ["Chung_Low_Rust_2022_JAMS"]
source_exemplar: chung_low_rust_2022_jams
confidence: medium
status: emerging (1p)
-->

# Board Governance as Amplifying Boundary Condition (Perverse Pressure Logic)

> **适用**: 研究涉及**公司治理机制意外放大而非抑制管理层机会主义/短视行为**的情境
> **核心动作**: 独立董事会通过 [short-term monitoring / dismissal threat / pay-for-performance pressure] 加剧 [CEO_trait] 与 [myopic_behavior] 之间的正向关系
> **母变体**: E 调节效应型
> **范文**: Chung, Low & Rust (2022, JAMS) — board independence exacerbates confident CEO's myopic marketing management

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 董事会的法定监督角色声明（agency theory baseline） | 50-80 | ✅ |
| P2 | 股东短视压力的传导机制：独立董事如何成为短视压力的放大器 | 80-120 | ✅ |
| P3 | 与 [CEO_trait] 的交互：为什么高 [trait] CEO 对董事会压力更敏感 | 70-100 | ✅ |
| P4 | [可选] 次级劝说者（CMO/confident advisor）如何削弱董事会压力 | 60-90 | ⚠️ |
| P5 | 调节假设收敛 | 30-50 | ✅ |

> **注意**: 本协议的核心贡献是**反转董事会的传统缓冲角色**。必须先承认 agency theory 的常规预测（独立董事抑制机会主义），再用 "perverse pressure" 逻辑解释为何在本情境中效果相反。

---

## 核心骨架

### P1: 法定监督角色声明

```
The board of directors is the ultimate decision-maker within the firm and is expected 
to monitor management on behalf of shareholders ([citations]). Agency theory posits 
that independent directors, by virtue of their fiduciary role, can reduce managerial 
discretion and protect shareholder interests ([citations]).
```

### P2: 股东短视压力的传导机制（反转基线）

```
However, this monitoring role can have the perverse effect of intensifying [short-termist_behavior] 
under certain conditions. Shareholders often focus on near-term performance when evaluating 
management ([citations]), leading independent boards to dismiss CEOs or cut their compensation 
when earnings expectations are missed ([citations]). When board monitoring is strong, the threat 
of [sanction] is always present, creating acute pressure on [higher_actor] to meet short-term 
performance targets. Rather than curbing [opportunistic_behavior], intense monitoring can thus 
pressure managers to engage in [myopic_action] to avoid [negative_outcome].
```

### P3: 与 [CEO_trait] 的交互

```
We expect this perverse pressure to be especially pronounced for [higher_actors] high in [trait_X]. 
Such [higher_actors] believe in their superior ability to manage the firm and therefore view 
negative assessments by an independent board as unjustified ([citations]). To avoid these assessments, 
they have stronger incentives to "borrow" from future performance through [myopic_action] in order 
to report current-period results that satisfy the board. Thus, board independence should amplify the 
[positive/negative] relationship between [trait_X] and [DV].
```

### P4: 次级劝说者的缓冲作用（可选，生成第二个调节/三向交互）

```
[Lower_actor], however, may be able to counteract this perverse pressure by persuading the board 
of the long-term value of [investment_at_risk]. When [lower_actor] is highly confident, they can 
effectively signal that [myopic_action] would damage [long-term_asset], drawing the board's scrutiny 
to [functional_domain] ([citations]). This may lead the board to resist cutting [investment_at_risk], 
thereby weakening the amplification effect of board independence.
```

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| Governance amplification (two-way) | "H[N]. [Governance_mechanism] exacerbates the [positive/negative] relationship between [CEO_trait_X] and [DV]." |
| Three-way with countervailing advisor | "H[N]. The amplifying effect of [governance_mechanism] on the [CEO_trait_X]→[DV] relationship is [weaker/stronger] when [lower_actor_confidence] is [high/low]." |
| Scope qualifier | "We are not arguing that [governance_mechanism] eliminates all long-term investment; rather, it specifically increases pressure on [higher_actor] to avoid [earnings_shortfall]." |

---

## 关键句式

**承认传统角色后反转**:
```
"Although [governance_mechanism] is designed to [intended_function], its responsiveness to 
[short-term_stakeholder] demands can produce the perverse outcome of [unintended_consequence]."
```

**perverse pressure 机制**:
```
"In the presence of intense [monitoring], the threat of [sanction] is always around the corner 
whenever [actor] does not meet [performance_target]."
```

**trait-driven sensitivity**:
```
"[Actors] high in [trait_X], who believe in their superior ability to [manage], would especially 
consider such negative assessments to be unjustifiable, and seek to avoid them."
```

---

## 语料锚定

- **Chung, Low & Rust (2022, JAMS)** — board independence exacerbates confident CEO's myopic marketing management
  - P1: "The board of directors plays a critical role in affecting the short-termist behavior of the CEO, and the board of directors is the ultimate decision-maker within the firm."
  - P2: "The responsiveness of boards to shareholders has been criticized to have the perverse impact of leading to myopic corporate behaviors, as directors bow to investors' demand for short-term performance and use short-term metrics to evaluate and assess CEOs."
  - P3: "Highly confident CEOs, who believe in their superior ability to run the firm, would especially consider such negative assessments by an independent board to be unjustifiable, and seek to avoid them."
  - P4: "a highly confident CMO may be able to convince their directors of the merits of continued investments in such assets... This may lead the board of directors to scrutinize marketing investments more closely"

---

## 可替换变量清单

| 占位符 | 示例 |
|--------|------|
| `[governance_mechanism]` | board independence, institutional ownership, analyst coverage, shareholder activism |
| `[CEO_trait_X]` | CEO confidence, CEO narcissism, CEO short-term incentive pay, CEO tenure |
| `[myopic_action]` | myopic marketing cuts, R&D cuts, accrual earnings management, share buybacks |
| `[earnings_shortfall]` | missed earnings expectations, negative earnings surprise, below-benchmark ROA |
| `[sanction]` | dismissal, compensation cut, shareholder litigation, negative media coverage |
| `[lower_actor]` | CMO, CTO, CHRO, divisional president |
| `[investment_at_risk]` | marketing assets, R&D pipeline, human capital, customer relationships |

---

## QC 检查点

- [ ] 是否先承认 agency theory 的常规预测再反转？
- [ ] 是否明确说明董事会压力如何通过 [short-term metric] 传导到 [myopic_action]？
- [ ] 是否解释为什么高 [trait_X] 的 CEO 对这种压力更敏感？
- [ ] 是否区分了 "intended governance function" 与 "perverse pressure"？
- [ ] 若加入次级劝说者，是否说明其劝说对象是董事会（而非仅 CEO）？
- [ ] 是否在结尾声明了研究的 scope qualifier（不否定董事会的所有治理功能）？

---

## 反模式

- 直接宣称 "独立董事导致短视" 而不先承认其法定监督角色 → 显得与 agency theory 对立而非发展
- 把董事会压力描述为唯一原因，忽略 [CEO_trait] 的交互作用 → 变成 governance 文献复述
- 用 "董事会也短视" 作为 folk explanation → 必须用股东压力/薪酬契约/解雇威胁等机制化语言
- 三向交互中 [lower_actor] 直接阻止董事会 → 除非有理论说明 lower actor 能影响董事会决策，否则过度赋权
- 结论泛化为 "所有治理机制都有害" → 必须限定于 [short-term_metric] 驱动的 [myopic_action] 情境
