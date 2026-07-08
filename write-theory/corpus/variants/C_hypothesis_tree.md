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

## 关键句式模板

**对称预测（双重交互）**：
```
"We argue that [factor 1] influences [Construct A]'s effect by [mechanism 1], but 
has the opposite effect on [Construct B]. Conversely, [factor 2] reduces [Construct A]'s 
influence, while enhancing [Construct B]'s effect. This asymmetric pattern arises 
because [underlying logic differentiating the two constructs]."
```

**三向交互**：
```
"We argue that the interaction between [IV] and [Moderator 1] will be further 
moderated by [Moderator 2], such that the [enhancing/buffering] effect of [Moderator 1] 
on the [IV]→[DV] relationship is itself [strengthened/weakened] when [Moderator 2] 
is [high/low]. This three-way interaction captures [theoretical insight beyond 
two-way interaction]."
```

**层次递进**：
```
"Having established that [baseline effect], we now consider when this effect is 
more versus less pronounced. Not all [actors/contexts] will experience [the effect] 
equally, because [moderator logic]."
```

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| 基础关系 | "H1. [IV] is [positively/negatively] associated with [DV]." |
| 调节效应 | "H2. The relationship between [IV] and [DV] is moderated by [Z], such that the [positive/negative] effect of [IV] on [DV] is [stronger/weaker] when [Z] is [high/present]." |
| 三向交互 | "H3. The moderating effect of [Z] on the [IV]→[DV] relationship is further moderated by [W], such that [Z]'s [enhancing/buffering] effect becomes [stronger/weaker] when [W] is [high]." |
| 条件效应（双假设） | "H2a: When [condition A], [effect A]. H2b: When [condition B], [effect B]." |

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
