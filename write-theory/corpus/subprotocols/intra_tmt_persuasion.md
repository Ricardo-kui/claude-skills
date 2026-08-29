<!--
pattern_id: intra_tmt_persuasion
build_type: 调节效应型 / 假设树型
source_papers: ["Chung_Low_Rust_2022_JAMS"]
source_exemplar: chung_low_rust_2022_jams
confidence: medium
status: EMERGING
-->

# Intra-TMT Persuasion: Lower-Level Actor Influences Higher-Level Actor

> **适用**: 研究涉及**上下级高管之间的劝说动态**——较低层级的职能高管（如 CMO、CFO、CTO、CSO）试图影响更高层级的决策者（如 CEO）的方向性决策
> **核心动作**: [lower_actor] 通过 [confidence heuristic / expertise signal / counsel] 改变 [higher_actor] 对 [focal_behavior] 的成本-收益评估
> **母变体**: E 调节效应型 / C 假设树型
> **范文**: Chung, Low & Rust (2022, JAMS) — CEO confidence × CMO confidence on myopic marketing management

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 决策权分配声明：谁最终拍板，谁只有劝说角色 | 40-60 | ✅ |
| P2 | 上下级激励结构差异：为什么 [lower_actor] 倾向于反对/支持 [focal_behavior] | 70-100 | ✅ |
| P3 | 劝说障碍：为什么 [higher_actor] 通常不听 [lower_actor] | 50-80 | ✅ |
| P4 | 信心启发式转折：高信心 [lower_actor] 如何突破劝说障碍 | 70-100 | ✅ |
| P5 | [可选] 权力放大：相对权力如何增强劝说效果 | 60-90 | ⚠️ |
| P6 | 调节/交互假设收敛 | 30-50 | ✅ |

> **管理学惯例**: 本协议通常生成一个 **two-way interaction**（H2: [higher_actor_X] × [lower_actor_W]），如果存在权力不对称进一步放大，则继续生成 **three-way nested interaction**（H3: [higher_actor_X] × [lower_actor_W] × [lower_actor_power]）。

---

## 核心骨架

### P1: 决策权分配声明

```
Decisions about [focal_domain] are ultimately made by [higher_actor], even though 
[lower_actor] plays a critical advisory role ([citations]). Although [lower_actor] 
possesses function-specific expertise, [higher_actor] retains primary control over 
[resource/decision]. As such, [lower_actor]'s influence is persuasive rather than 
authoritative.
```

### P2: 上下级激励结构差异

```
Compared with [higher_actor], [lower_actor] faces a different cost-benefit calculus 
with respect to [focal_behavior]. First, [lower_actor]'s compensation and career 
outcomes are tied more closely to [functional_metric] than to [higher_actor_metric] 
([citations]). Because [focal_behavior] undermines [functional_metric], [lower_actor] 
has stronger incentives to resist it. Second, [lower_actor]'s professional identity 
is anchored in [functional_domain], making [focal_behavior] inconsistent with their 
long-term human-capital development ([citations]). Therefore, [lower_actor] is more 
likely to counsel against [focal_behavior] than to promote it.
```

### P3: 劝说障碍

```
Despite [lower_actor]'s incentives to oppose [focal_behavior], their counsel may not 
be heeded. [Higher_actor] who are high in [trait_X] tend to be [certainty / dismissiveness 
of advice / feedback resistance] ([citations]). Such [higher_actors] are likely to 
discount input that contradicts their preferred course of action, including advice from 
[lower_actor].
```

### P4: 信心启发式转折

```
However, research on the confidence heuristic suggests that advice is more persuasive 
when the advisor displays high confidence in their judgment ([citation]). Highly 
confident [lower_actors] signal functional expertise and conviction, which can earn 
the attention of an otherwise dismissive [higher_actor]. Specifically, a confident 
[lower_actor] is better able to reframe [focal_behavior] as costly to [long-term_goal], 
thereby shifting [higher_actor]'s perceived cost-benefit balance. Thus, we expect the 
[positive/negative] effect of [higher_actor_X] on [DV] to be [weakened/strengthened] 
when [lower_actor] is highly confident.
```

### P5: 权力放大（可选，生成三向交互）

```
Whether [lower_actor]'s confidence can translate into actual influence also depends 
on their relative power vis-à-vis [higher_actor]. When [lower_actor] controls critical 
[functional_resources] and is difficult to replace, [higher_actor] has stronger 
incentives to accommodate their preferences, because losing [lower_actor] would impair 
[future_performance] ([citations]). Therefore, the buffering effect of [lower_actor] 
confidence should be strongest when [lower_actor] wields greater relative power.
```

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| Two-way persuasion moderation | "H[N]. The [positive/negative] effect of [higher_actor_X] on [DV] is [weaker/stronger] when [lower_actor_W] is high." |
| Three-way power amplification | "H[N]. The [buffering/amplifying] effect of [lower_actor_W] on the [higher_actor_X]→[DV] relationship is [stronger/weaker] when [lower_actor_power] is high." |
| No main effect for lower actor (when decision rights reside with higher actor) | "We do not expect [lower_actor_W] to have a main effect on [DV], because [resource allocation] is primarily controlled by [higher_actor]." |

---

## 语料锚定

- **Chung, Low & Rust (2022, JAMS)** — CEO confidence → myopic marketing management; CMO confidence buffers the CEO→myopia link; CMO power amplifies the buffering effect
  - P1: "Decisions within the firm are made by the CEO, with counsel from other top management team members... Although firm resource allocation is primarily decided by the CEO, the CMO can still play a critical role in influencing the firm's allocation of marketing resources."
  - P2: CMO compensation tied to product-market outcomes, not stock price; CMO dismissal tied to sales/revenue targets, not profitability
  - P3: "Highly confident CEOs' certainty in their own abilities and resultant unresponsiveness to feedback and advice imply that these CEOs are unlikely to abide by the counsel of their CMOs."
  - P4: "research has shown that advice is more likely to be well-received if the advisors display high confidence"
  - P5: "When a powerful CMO is more indispensable to future firm performance, the CEO has incentive to ensure they do not cross their CMO, due to the risk of the CMO quitting"

---

## 可替换变量清单

| 占位符 | 示例 |
|--------|------|
| `[higher_actor]` | CEO, board of directors, divisional president |
| `[lower_actor]` | CMO, CFO, CTO, CHRO, CSO, general counsel |
| `[focal_behavior]` | myopic marketing cuts, risky investment, premature scaling, accrual earnings management |
| `[trait_X]` | confidence, overconfidence, narcissism, hubris |
| `[lower_actor_W]` | confidence, expertise, tenure, functional background |
| `[lower_actor_power]` | relative power, structural power, pay ratio, title centrality |
| `[functional_metric]` | product-market performance, revenue growth, customer satisfaction, brand equity |

---

## QC 检查点

- [ ] 是否明确说明 [lower_actor] 的劝说角色（非最终决策者）？
- [ ] 是否论证了 [lower_actor] 与 [higher_actor] 在 [focal_behavior] 上的激励差异？
- [ ] 是否解释了为什么 [higher_actor] 通常不听 [lower_actor]？
- [ ] 信心启发式是否从 [lower_actor] 信心推导到 [higher_actor] 接受度（而非仅说 lower actor 更敢说话）？
- [ ] 若引入权力放大，是否说明权力如何改变 [higher_actor] 的采纳激励（而非仅说 lower actor 更有资源）？
- [ ] 假设形式是否匹配 two-way / three-way 交互设计？
- [ ] 是否声明了 [lower_actor] 无单独主效应的理论依据（当决策权在 higher actor 手中时）？

---

## 反模式

- 把 [lower_actor] 写成共同决策者（除非其确有正式否决权）→ 与 upper-echelons 权力结构矛盾
- 只论证 [lower_actor] 会反对，不解释为什么 [higher_actor] 会听 → 缺失 persuasion mechanism
- 用 [lower_actor] 的“责任感”或“道德”替代成本-收益激励 → 缺乏理论化
- 权力放大仅描述为 "more resources" 而不说明对 [higher_actor] 的代价 → 机制悬空
- 三向交互中 W2 与 W1 缺少理论联系 → 变成统计补丁
