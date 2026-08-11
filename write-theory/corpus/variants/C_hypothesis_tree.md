# 变体 C：假设树型

> **适用**: 多层次/多条件的系统化假设，假设间有逻辑递进关系
> **范文**: Han 2024 (AMP), Paruchuri 2020 (SMJ), Zhou 2017 (ASQ), Weng & Yang (JMS)
> **最佳期刊**: SMJ ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐⭐ | OS ⭐⭐⭐⭐ | JMS ⭐⭐⭐⭐

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（所有主角+配角） | 80-150 | ✅ |
| P2 | 理论基础：为什么选择这些构念和层级 | 60-100 | ✅ |
| P3-P4 | 基础关系论证（主效应的理论逻辑）+ H1 | 各 70-120 | ✅ |
| P5-P6 | 第一层调节机制推演 + H2 | 各 70-120 | ✅ |
| P7-P8 | 第二层调节/中介机制推演 + H3 | 各 70-120 | ✅ |
| P9 | [不推荐] 独立的 Closure 段落——管理学顶刊标准是假设推导完毕即进入 METHODS | — | ✗ 非标准 |
| P10 | [可选] 进一步调节或边界条件 + H4+ | 各 60-100 | ⚠️ |

> **注意**: 管理学顶刊（JMS, AMJ, SMJ, ASQ 等）不要求独立的 T6 Closure 段落。最后一个假设的自然收敛即为 Theory 部分的终点。

**段落扩展变体（T0 前置背景）**：如果 DV 是跨学科现象且需要多学科共识建立，可在 P1 前插入 T0 段落——详见 `corpus/sentences/construct_definition.md` 变体 E。

**P3-P4 变体：双原因+三方行为者对比型（weng_yang 型）**：当 IV 是一个连续谱（非二元）且存在理论上可推导的反方向行为者时，H1 段落按五拍展开：Reason1→Reason2→反方对比→中间基准→权威收束→H1。详见 `corpus/sentences/mechanism_chain.md` 变体 D。

**P5-P8 变体：Moderator 选择元框架前置（weng_yang 型）**：当 ≥2 个 moderators 且可通过 H1 的机制维度（如 awareness vs capacity）分类时，在推导具体调节假设前，用 1 段解释 moderator 选择的理论逻辑。详见 `corpus/sentences/moderation.md` 变体 "H1 机制锚定型"。

---

## Pollock 2015 型：生命周期调节 / 假设树型

**新增于**: write-theory 3.2.0 (Pollock et al. 2015 ASQ 蒸馏)

**适用**: 两种相关无形资产（如 reputation / status）在生命周期不同阶段相互塑造强度不同；或同一关系在 actor 年轻/成熟时方向性反转。

### 基线互惠作为非假设前提

当两个构念明显互惠但文献已有共识时，可作为基线假设而非正式假设：
```
Prior research has shown that [A] and [B] are positively correlated: high [A] can increase access to elite circles, while high [B] provides information and resources that enhance [A] ([citations]).
Because both [A] and [B] provide benefits that aid in developing the other, we expect them to have a positive relationship as they coevolve.
As this expectation is unsurprising, we do not present a formal hypothesis, but it forms our baseline assumption.
```

**原文锚点** (Pollock et al. 2015, ASQ "Untangled"):
> "Research has established that status and reputation are positively correlated. High reputation based on strong performance can increase access to elite social circles while high status can provide greater access to the information, opportunities, and resources that can enhance reputation." ... "Because both reputation and status provide benefits that aid in developing the other construct, we expect them to have a positive relationship as they coevolve. As this expectation is unsurprising, we do not present a formal hypothesis, but it does form our baseline assumption."

### 生命周期不对称（H1a/H1b）

```
When firms are young, they lack standing in the status hierarchy, and their initial status largely reflects founder status ([citations]).
To build [B], young firms must affiliate with high-[B] actors, which requires demonstrating energy and delivering promising deals ([citations]).
By doing so, they build [A]; these affiliations provide endorsement benefits and access to better deals, further enhancing [A].
Thus [A] must precede [B], and [A] should have a stronger effect on [B] than [B] has on [A] when firms are young:
H1a: When firms are young, [A] has a greater effect on [B] than [B] has on [A].

As firms age, [B] increases as a function of [A], giving them access to [B]-based benefits that sustain success and reinforce [A] ([citations]).
Once a new [B] equilibrium is established, [B] stabilizes and becomes less susceptible to changes in [A] ([citations]).
Therefore, in later life stages [B] should have a greater effect on [A]:
H1b: When firms are older, [B] has a greater effect on [A] than [A] has on [B].
```

**原文锚点** (Pollock et al. 2015, ASQ "Untangled"):
> "During its early years a firm has little standing in its industry's social hierarchy, and what status it has is largely the result of the founder's personal status." ... "Thus we expect that reputation will have a greater influence on status than status has on reputation during the early years of a VC firm's life, when both are more malleable." ... "As such, we expect that as firms mature, status will have a greater influence on reputation than reputation will have on status."

### 路径依赖的时间衰减（H2）

```
Initial conditions strongly influence [B] when firms are young and their [B] position is still being negotiated ([citations]).
[B] orders tend toward equilibrium and stabilize over time, so prior [B] should have a strong effect on current [B] in early years but a weaker effect as firms age ([citations]).
In contrast, [A] must be continually reinforced and therefore remains susceptible to changes in prior [A]; its path dependence should not weaken with age ([citations]).
H2: The effect of prior [B] on current [B] weakens as firms age, but the effect of prior [A] on current [A] is unaffected by age.
```

**原文锚点** (Pollock et al. 2015, ASQ "Untangled"):
> "Research has shown that initial conditions influence subsequent status when firms are young and their position in the status order is being established, that status becomes more stable and tends toward equilibrium over time, and that reputation is dynamic and needs to be continually reinforced." ... "Because reputation needs to be continually reinforced, it is always susceptible to changes in prior reputation; thus the effect of changes in prior reputation on current reputation will not weaken as the VC firm ages."

### 大事件可见性效应（H3a/H3b）

```
Highly visible positive events can alter organizational trajectories ([citations]).
Such events increase an actor's cognitive centrality, which enhances structural centrality ([B]) and subsequent performance ([A]) ([citations]).
Because general visibility is central to [A] but not to [B], and because [A] must be continually reinforced, blockbuster events should keep enhancing [A] as firms age.
For young firms, however, the visibility from such events brings them to the attention of high-[B] actors and thus boosts [B].
Once a firm's [B] position is established, additional visibility is less likely to change [B] and may even distract.

H3a: When firms are young, blockbuster events positively affect both [A] and [B].
H3b: When firms are older, blockbuster events positively affect [A] but not [B].
```

**原文锚点** (Pollock et al. 2015, ASQ "Untangled"):
> "Research on path dependence shows that significant events can change organizations' life trajectories." ... "Thus when firms are young and unknown, we expect blockbuster deals will enhance their status because they bring the firms to the attention of high-status VCs. But as a VC firm ages and its position in the status order stabilizes, the visibility and attention are less likely to affect its status."

### 先验期望违背型水平调节（H4）

```
Signals provide value only if they convey new information ([citations]).
Information that disconfirms prior beliefs is more salient than information that confirms expectations ([citations]).
Thus the lower observers' prior expectations of a blockbuster event, the bigger the surprise and the larger the effect on [A] and [B] ([citations]).
High-[A]/high-[B] actors are already expected to participate in blockbuster events, so the incremental benefit is smaller; low-[A]/low-[B] actors gain more because the event violates expectations.
H4: The positive effect of blockbuster events on current [A] and [B] is stronger when prior [A] and [B] are low than when they are high.
```

**原文锚点** (Pollock et al. 2015, ASQ "Untangled"):
> "Blockbuster deals provide valuable signals only if they provide new information, and information disconfirming prior beliefs is more salient and likely to be noticed than information confirming expectations. Thus the lower the expectation that a VC will be involved in a blockbuster deal, the bigger the surprise and the greater the effect on reputation and status participating in a blockbuster deal is likely to have."

---

## 关键句式模板

**对称预测（双重交互）**：
```
"We argue that [factor 1] influences [Construct A]'s effect by [mechanism 1], but 
has the opposite effect on [Construct B]. Conversely, [factor 2] reduces [Construct A]'s 
influence, while enhancing [Construct B]'s effect. This asymmetric pattern arises 
because [underlying logic differentiating the two constructs]."
```

**原文锚点** (Han, Pollock & Paruchuri 2024, SMJ "Public enemies?"; reputation vs celebrity 的对称反向调节):
> "We argue that objective severity, reflected in the misconduct's magnitude, influences reputation's effect by creating a bigger expectancy violation for high-reputation firms than for lower-reputation firms." ... "We argue that availability cascades weaken high reputation's influence on misconduct scandalization because the perceived severity dominates assessments of the misconduct's newsworthiness. In contrast, availability cascades complement celebrity's effect on scandalization."

**三向交互**：
```
"We argue that the interaction between [IV] and [Moderator 1] will be further 
moderated by [Moderator 2], such that the [enhancing/buffering] effect of [Moderator 1] 
on the [IV]→[DV] relationship is itself [strengthened/weakened] when [Moderator 2] 
is [high/low]. This three-way interaction captures [theoretical insight beyond 
two-way interaction]."
```

**原文锚点** (Paruchuri, Pollock & Kumar 2020, SMJ "On the tip of the brain"; 双条件互锁的三向推演):
> "Thus, for a negative event such as a capability failure to affect others' reputations, both the event and the firms affected have to be cognitively available and easily recalled together in order for the event to influence perceptions of the other firms." ... "Hypothesis 2. Given category members' high associability, the lower the salience of the differentiation-based capability failure the weaker the positive reputation spillover."

**层次递进**：
```
"Having established that [baseline effect], we now consider when this effect is 
more versus less pronounced. Not all [actors/contexts] will experience [the effect] 
equally, because [moderator logic]."
```

**原文锚点** (Han, Pollock & Paruchuri 2024, SMJ "Public enemies?"):
> "This leads to our baseline expectation that both reputation and celebrity enhance misconduct scandalization's likelihood." ... "However, we further argue that differences in reputation and celebrity's sociocognitive content lead them to vary in when and why they attract attention and are newsworthy, resulting in different effects on the extent to which the media scandalizes a firm's misconduct."

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| 基础关系 | "H1. [IV] is [positively/negatively] related to [DV]."（连续 IV/DV）；分类或方向性预测参见 `../sentences/hypothesis_forms.md` 决策矩阵——禁用无方向的 "is associated with"，见 SKILL.md 硬约束 #3 |
| 调节效应 | "H2. The relationship between [IV] and [DV] is moderated by [Z], such that the [positive/negative] effect of [IV] on [DV] is [stronger/weaker] when [Z] is [high/present]." |
| 三向交互 | "H3. The moderating effect of [Z] on the [IV]→[DV] relationship is further moderated by [W], such that [Z]'s [enhancing/buffering] effect becomes [stronger/weaker] when [W] is [high]." |
| 条件效应（双假设） | "H2a: When [condition A], [effect A]. H2b: When [condition B], [effect B]." |

**原文锚点** (Han, Pollock & Paruchuri 2024, SMJ "Public enemies?"; 调节效应假设的原文格式):
> "Hypothesis 1. The positive relationship between high reputation and misconduct scandalization strengthens as objective misconduct severity increases." ... "Hypothesis 4. The positive relationship between celebrity and misconduct scandalization strengthens as perceived misconduct severity increases."

---

## 子协议索引

- **C1 多 moderator 的统一选择框架**：参见 `corpus/subprotocols/moderator_selection_frameworks.md`（≥2 moderators 必须有理论驱动的选择理由，SKILL.md 硬约束 #11）
- **C2 假设体系的段落级组织**：参见 `corpus/subprotocols/hypothesis_organization_patterns.md`（common trunk → parallel branches / baseline→contingency / 2×2 矩阵——避免"假设树碎片化"反模式）
- **C3 序列嵌套调节（如 TMT 劝说链）**：参见 `corpus/subprotocols/intra_tmt_persuasion.md`（下级→上级信心启发式劝说，含权力放大→三向交互）

---

## QC 检查点

- [ ] 假设之间是否有清晰的逻辑递进关系（不是独立假设的堆叠）？
- [ ] 每个附加的交互项是否几何级增加了理论复杂度？是否值得？
- [ ] 三向交互是否有清晰的叙事故事（而非 "exploratory"）？
- [ ] 是否避免了 "fishing for significant interactions" 的印象？
- [ ] 最后一个假设推导是否自然收束（局部收敛信号 "Therefore/Thus/Accordingly" 清晰）？
- [ ] 如果 ≥2 个 moderators：是否有 moderator 选择的理论理由（元框架或分类逻辑）？
- [ ] 如果 IV 是连续谱：是否讨论了 IV 两端的行为差异（非只论证一个方向）？
- [ ] 如果有 T0 前置背景：T0 是否 ≤ Theory 总篇幅的 25%？

---

## Vidal & Mitchell 型：双极变化 × 行动方式的条件化假设树

**来源论文**: Vidal & Mitchell (2015, *Organization Science*)

**验证状态**: EMERGING（单篇入库；需第二篇跨论文验证）

**适用**: 同一连续变化相对参照点的正、负两端都有独立的理论动机，且研究还预测行动的不同形式；适用于假设树而非单一 U 型/倒 U 型描述。

**组织逻辑**:
1. 先建立共同树干：`[相对参照点的变化]` 可能触发 `[行动]`，但其影响并不单向。
2. 以负向偏离发展第一分支：`[负向偏离] → [纠偏/生存压力] → [行动]`，并说明为什么该压力匹配 `[行动形式 A]`。
3. 以正向偏离发展第二分支：`[正向偏离] → [维持增长/释放注意力或资源的压力] → [行动]`，并说明为什么该压力匹配 `[行动形式 B]`。
4. 最后再引入 `[状态水平]`：只有当状态水平使同一方向的变化更具诊断意义时，预测该分支被放大；不要将它作为无机制的统计交互项。

**骨架**:
```text
Relative to [reference point], a [negative change] and a [positive change] can each make [action] more likely, but for different reasons. When [negative change] occurs, [mechanism A] creates pressure to [action], especially in the form of [mode A]. When [positive change] occurs, [mechanism B] makes proactive [action] attractive, especially in the form of [mode B].

The association should be strongest when [state level] reinforces the diagnostic meaning of the corresponding change. Accordingly:
H1a: [negative change] is [direction] associated with [overall action / mode A].
H1b: [positive change] is [direction] associated with [overall action / mode B].
H2a/H2b: These associations are [stronger/weaker] when [state level] is [condition], because [boundary mechanism].
```

**原文锚点** (Vidal & Mitchell 2015, *Organization Science* "Adding by Subtracting"):
> "A negative performance gap occurs when a firm's performance is lower than that of relevant aspiration levels; in parallel, a positive performance gap occurs when a firm's performance exceeds an aspiration level." ... "We expect firms with increasing performance to be more likely to pursue partial divestitures, given the differences in pressures that they face, whereas firms with declining performance will tend toward full divestitures."

**关键约束**:
- 负/正两端必须各有独立 why-chain，不能只在第二分支套用“相反地”。
- 行动子类型必须在理论中先被区分，再进入结果拆分；不能事后依据显著性挑选子样本。
- 该模式只允许使用关联性语言，除非实证设计另有因果识别。
- H2 的条件变量必须解释“为什么放大这一方向”，不能只陈述存在交互。

**与既有变体的差异**: 生命周期不对称与先验期望违背变体围绕时间阶段或信号意外性；本变体围绕**相对参照点的两个变化方向**及其对应行动方式的匹配。
