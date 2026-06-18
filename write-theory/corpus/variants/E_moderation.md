# 变体 E：调节效应型

> **适用**: 核心贡献是识别 boundary condition、qualify 已有关系
> **来源**: Andersson, Cuervo-Cazurra, & Nielsen (2014) JIBS Editorial; Pollock 2025 Ch06
> **最佳期刊**: AMJ ⭐⭐⭐⭐⭐ | SMJ ⭐⭐⭐⭐⭐ | OS ⭐⭐⭐⭐

---

## 段落功能地图（E1 同层调节 — 7 步协议 + T6）

| 步骤 | 段落功能 | 推荐词数 | 必须度 |
|------|---------|----------|--------|
| Step 1 | 理论基底：说明用哪个理论解释 X→Y 和 Z 的角色 | 50-80 | ✅ |
| Step 2 | Baseline X→Y 机制推演（直接效应+假设） | 70-120 | ✅ |
| Step 3 | Moderator Z 的理论选择理由 | 60-100 | ✅ |
| Step 4 | Z 的直接效应（如适用）+ 与 moderation 机制的区分 | 50-80 | ⚠️ |
| Step 5 | 机制修改推演：Z 如何 strengthen/weaken X→Y | 70-120 | ✅ |
| Step 6 | 排除反向交互：为什么是 Z moderates X→Y | 40-60 | ✅ |
| Step 7 | 调节假设陈述 | 30-60 | ✅ |
| Step 8 | T6 Closure：框架锁定 + 假设逻辑显性化 | 80-120 | **准强制** |

---

## 关键句式模板

**机制修改论证**：参见 `corpus/sentences/moderation.md`

**假设模板（按交互模式）**：

| 模式 | 假设模板 |
|------|---------|
| Enhancing | "H[N]. The [positive/negative] effect of [X] on [Y] is **stronger** when [Z] is [high/present] than when [Z] is [low/absent]." |
| Buffering | "H[N]. The [positive/negative] effect of [X] on [Y] is **weaker** when [Z] is [high/present] than when [Z] is [low/absent]." |
| Antagonistic | "H[N]. Although [X] and [Z] each [positively/negatively] affect [Y], their interaction effect on [Y] is [negative/positive]." |
| Existence | "H[N]. [X] is [positively/negatively] related to [Y] for [group A], but unrelated to [Y] for [group B]." |
| Competing | "H[N]. [X] is positively related to [Y] for [group A], but negatively related to [Y] for [group B]." |

---

## 子协议索引

- **E1.1 分组调节（Categorical/Group-based）**: 参见 `corpus/subprotocols/E1_categorical_moderation.md`
- **E2 跨层调节（Cross-Level）**: 参见下文

---

## E2. 跨层调节 (Cross-Level Moderation) — 9 步协议 + T6

**前置声明模板**：
```
"The focal unit of analysis is [Level-1 unit, e.g., the firm-year]. 
[Level-1 units] are nested within [Level-2 units, e.g., industries], 
which are in turn nested within [Level-3 units, e.g., countries]. 
This nesting structure means that [Level-1 observations] within the same 
[Level-2 unit] share common characteristics and are not independent. 

We theorize that [Level-2/3 variable Z] moderates the [Level-1 X → Level-1 Y] 
relationship because [cross-level mechanism: e.g., Z creates institutional 
conditions that alter the costs/benefits of X's effect on Y]. 

We also account for the direct effect of [Z] on [Y] through [separate mechanism], 
distinguishing this cross-level direct effect from the cross-level interaction effect."
```

**段落功能地图**：

| 步骤 | 段落功能 | 推荐词数 | 必须度 |
|------|---------|----------|--------|
| Step 1 | 焦点分析单元声明 + Y 在哪个层级 | 40-60 | ✅ |
| Step 2 | 理论嵌套结构描述 | 50-80 | ✅ |
| Step 3 | 各层级的理论来源 | 60-100 | ✅ |
| Step 4 | Level 1 X→Y 直接效应 + H1 | 70-120 | ✅ |
| Step 5 | 高层/低层 Moderator 选择理由 | 60-100 | ✅ |
| Step 6 | Cross-level 直接效应（如适用） | 50-80 | ⚠️ |
| Step 7 | Cross-level 交互机制推演 | 70-120 | ✅ |
| Step 8 | 排除反向交互（嵌套逻辑） | 40-60 | ✅ |
| Step 9 | 跨层调节假设 | 30-60 | ✅ |
| Step 10 | T6 Closure：框架锁定 + 假设逻辑显性化 | 80-120 | **准强制** |

**跨层假设模板**：
```
"H[N]. The relationship between [Level-1 X] and [Level-1 Y] varies with 
[Level-2 Z] such that the [positive/negative] effect of [X] on [Y] is 
[stronger/weaker] for [Level-1 units] nested in [Level-2 units] with 
[higher/lower] levels of [Z]."
```

---

## QC 检查点（E1 和 E2 共用）

- [ ] X→Y baseline mechanism 是否在调节假设前明确写出？
- [ ] Moderator 的选择是理论驱动还是 empirical convenience？
- [ ] Z→Y 的 direct effect 机制是否与 moderation 机制明确区分？
- [ ] 交互模式（enhancing/buffering/antagonistic/existence/competing）是否明确命名或可推断？
- [ ] 假设语言是否与实证检验匹配（differential prediction vs differential validity）？
- [ ] 是否排除了反向交互（时序/层级/理论方向）？
- [ ] 对于跨层模型：unit of analysis, nesting, 和 level-specific theory 是否在假设前声明？
- [ ] T6 Closure 是否存在？

---

## E3. 嵌入型边界条件（Embedded Boundary Conditions，kalaignanam2017 型）

**适用**: moderator 数量较多（≥3 个）且每个 moderator 有独立理论依据，独立 T5 段落会导致重复和碎片化。将边界条件完全嵌入 T3 机制推演中，通过"条件化机制修改"实现边界论证。

**与独立 T5 的区别**:

| 维度 | 独立 T5 | 嵌入型边界条件 |
|------|---------|---------------|
| 结构 | 独立段落，通常在 baseline 假设之后 | 无独立段落，嵌入在 T3 的各小节中 |
| 假设数 | 适合 1-2 个 moderator | 适合 3-6 个 moderator |
| 篇幅 | 每个 moderator 占 1 个独立段落 | 每个 moderator 占 1 个小节（含定义+机制+假设） |
| 理论深度 | 每个 moderator 有深度机制推演 | 每个 moderator 机制较浅但结构平行 |
| 适用期刊 | AMJ, ASQ, OS | JM, JMR, JOM |

**段落功能地图（每个 moderator 小节）**:

| 步骤 | 段落功能 | 推荐词数 | 必须度 |
|------|---------|----------|--------|
| Step 1 | 小节标题：明确 topic | 1 行 | ✅ |
| Step 2 | Moderator 定义 | 30-50 | ✅ |
| Step 3 | 基线机制回顾 + 条件化修改 | 60-100 | ✅ |
| Step 4 | 文献/元分析支撑 | 30-50 | ⚠️ |
| Step 5 | 对立条件对称论证 | 40-60 | ✅ |
| Step 6 | 调节假设陈述 | 30-50 | ✅ |

**关键句式**:

**小节开场**:
```
"An attribute that creates a dilemma for firms when [decision] is [moderator]. [Moderator] refers to [definition] ([citation]). Although [moderator] increases [cost] for [Option B] and favors [Option A], firms may not have the expertise to [implement]. Therefore, [reasoning A]. [Citation support]. [Reasoning B]. [Meta-analytic evidence] supports this view and suggests that [finding] ([citation]). The rationale is that [theoretical mechanism]. In contrast, when [moderator condition is low], the [advantage] is likely to be suppressed. Given these arguments, we expect [prediction]."
```

**收敛到假设**:
```
"H[N]. The [direction] effect of [IV] on [DV] is [stronger/weaker] when [moderator] is [high/low]."
```

**语料锚定**:
- kalaignanam2017 (JM) — 4 个 moderator（technological complexity, NPD capability×2, PLAF），每个 moderator 一个小节，结构完全平行

**关键特征**:
- "An attribute that creates a dilemma..." — 统一的小节开场句式
- "refers to" — 构念定义
- "Although... firms may not have... Therefore..." — 让步→推论结构
- "Meta-analytic evidence supports this view" — 用元分析增强说服力
- "In contrast, when... is suppressed" — 低条件对称论证
- "Given these arguments, we expect" — 收敛到假设

**平行结构要求**:
- 所有 moderator 小节使用相同的段落结构（定义→机制→假设）
- 所有 moderator 小节长度相近（避免某小节过短暗示论证不足）
- 假设编号连续（H1a, H1b, H2a, H2b...）

**反模式**:
- 平行结构断裂（某 moderator 缺少定义或对称论证）→ 审稿人质疑选择性论证
- moderator 之间缺少理论联系 → 看似独立论文拼接
- 嵌入型边界条件用于 1-2 个 moderator → 独立 T5 更合适
- 嵌入型边界条件用于纯理论期刊（ASQ/OS）→ 审稿人可能要求更深入的单 moderator 论证

**适用期刊**: JM, JMR, JOM, MSOM（偏好紧凑结构）；AMJ/SMJ 需评估 moderator 数量和深度需求
