# 变体 B：机制推演型

> **适用**: 解释 X 如何/为什么影响 Y 的因果机制链
> **范文**: Wu 2025 (OrgSci), Keeves 2017 (AMJ), Zhou 2017 (ASQ)
> **最佳期刊**: SMJ ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐⭐ | ASQ ⭐⭐⭐⭐

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（所有主角）+ 理论视角引入 | 80-150 | ✅ |
| P2 | 机制预览（"We argue that X influences Y through..."） | 60-100 | ✅ |
| P3-P4 | 机制 Step 1 推演 + H1 | 各 70-120 | ✅ |
| P5-P6 | 机制 Step 2 推演 + H2 | 各 70-120 | ✅ |
| P7 | 收束论证（Mediation hypothesis / Taken together）——自然收敛，不附加独立 Closure 段 | 60-100 | ✅ |
| P8+ | [可选] 边界条件/调节 | 各 60-100 | ⚠️ |

> **注意**: 管理学 Theory 部分的标准做法是文献回顾嵌入在构念定义和 why-chain 推导中，不以独立的"文献对话"或"文献综述"段落出现。文献引用服务于理论构建——"Prior research has established X. However, what if Y? We argue that Z."（验证自 Park & Westphal 2013 ASQ, "On the tip of the brain" SMJ, Malik et al. 2025 JM, Pollock et al. 2015 ASQ）。部分 JM 论文将 Theory 章节直接命名为 "Literature Review and Conceptual Background"（如 Malshe & Agarwal 2015, Shi et al. 2021），整章即文献回顾+假设——这是章节命名惯例，不是段落结构要求。
> 
> P1 以构念界定+理论视角引入开始，文献引用嵌入其中（非独立段）。P2 以机制预览收束定位。
> 
> **关于嵌入式文献引用**: 1-2 句嵌入构念定义或 why-chain 起点的文献引用是正常且必要的（如 "Prior research has established X. However, what if Y? We argue that Z." ——验证自 "On the tip of the brain" SMJ, Park & Westphal 2013 ASQ, Malik et al. 2025 JM）。这不同于独立的"文献对话"段落——区别在于：(1) 引用服务于理论构建，直接衔接到 "We argue that..." 的论证 pivot；(2) 独立的文献综述段若不推动 why-chain 则为冗余。

---

## 关键句式模板

**理论视角引入**：
```
"Drawing on [theory], we argue that [core mechanism logic]. Specifically, we propose 
that when [antecedent condition], [actor] will respond to [stimulus] by [action], 
defined as [definition]. This theoretical lens allows us to explain not just whether 
[X affects Y], but how and why."
```

**多步机制链**：参见 `corpus/sentences/mechanism_chain.md`

**收束论证（中介假设）**：
```
"Taken together, H1 and H2 suggest a mediated relationship. [IV] influences [DV] 
not merely through [direct channel], but through the [mechanism] of [mediator]. 
By identifying this mediating mechanism, we move beyond the direct-effects paradigm 
that has dominated prior research. Thus:"
```

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| 基础关系 | "H[N]. [IV] is [positively/negatively] related to [DV]." |
| 中介效应 | "H[N]. [Mediator] mediates the [positive/negative] relationship between [IV] and [DV]." |
| 中介等价 | "H[N]. This prediction is formally equivalent to hypothesizing that [mediator] will mediate effects of [IV] on [DV]." |

---

## 子协议索引

- **B2 双轨并行机制推演型**: 参见 `corpus/subprotocols/B2_dual_track.md`
- **B3 宽度型并行机制**: 参见 `corpus/subprotocols/hypothesis_derivation_patterns.md`（Width-Type Parallel Mechanism）
- **B4 2×2 对称假设矩阵**: 参见 `corpus/subprotocols/hypothesis_organization_patterns.md`（2×2 Symmetric Hypothesis Matrix）
- **B5 对称反向双轨机制**: 参见 `corpus/subprotocols/hypothesis_derivation_patterns.md`（Symmetric Opposing Dual-Track）
- **B6 曲线关系双阶段论证**: 参见 `corpus/subprotocols/hypothesis_derivation_patterns.md`（Curvilinear Relationship — Two-Phase Argumentation）
- **B7 T2 竞争解释管理**: 参见 `corpus/subprotocols/argumentation_patterns.md`（Preemptive Competing Account Management）

---

## 机制推演型的五种假设组织方式

机制推演型论文的核心是把"为什么 X 影响 Y"讲清楚。根据 MVP30 范文语料库，特别是 Singh & Grewal (2023, JMR)、Shen et al. (JOM)、Gamache et al. (2020, SMJ)、Zhao-Ding & Gaba (ORSC) 和 Cui et al. (SMJ) 五篇的对比，机制推演型（及相关变体）有五种主流的假设推导组织方式。选择哪一种取决于你的研究问题和理论野心。

### 方式一：深度链式（Depth Chain）

**代表**: Singh & Grewal (2023, JMR) 的铁三角机制 + Shen et al. (JOM) 的三机制 trunk
**适用**: 研究问题关注"通过什么机制"，且机制可以被拆解为多个因果步骤
**结构**:
```
X → M1 → M2 → Y
或
X → [mechanism 1 / mechanism 2 / mechanism 3] → Y
```
**优势**: 理论深度强，能回答 "how"
**风险**: 步骤过多可能让读者迷失；每个步骤都必须有独立理论依据
**调用语料**: `corpus/sentences/mechanism_chain.md` + `corpus/subprotocols/arrangement_patterns.md`

### 方式二：宽度理由并行（Width Parallel）

**代表**: Gamache et al. (2020, SMJ)
**适用**: 研究问题关注"为什么同一关系成立"，且有多个独立的理论理由共同支撑
**结构**:
```
X → Y  because [reason 1]
         because [reason 2]
         because [reason 3]
```
**优势**: 论证稳健性高，每个理由简短易读；适合 SMJ 等偏好简洁理论论证的期刊
**风险**: 如果理由不独立会显得冗赘；不能替代对"过程机制"的解释
**调用语料**: `corpus/subprotocols/hypothesis_derivation_patterns.md`（Width-Type Three-Reason Parallel）

### 方式三：条件化复杂化（Conditional Complexification）

**代表**: Singh & Grewal (2023, JMR) 的间接调节 / Shen et al. (JOM) 的 parallel 调节
**适用**: 研究问题关注"在什么条件下"，或关系本身存在边界条件
**结构**:
```
X → Y, but this effect is contingent on W1, W2, ...
或
The interaction of W2 and X mediates the moderating effect of W1
```
**优势**: 理论精确性高，能回答 "when" / "for whom"
**风险**: 容易过度复杂；每个 moderator 都需要独立理论依据；H4 类复杂假设容易论证不足
**调用语料**: `corpus/variants/E_moderation.md` + `corpus/subprotocols/moderator_selection_frameworks.md`

### 方式四：对称反向双轨（Symmetric Opposing Dual-Track）

**代表**: Zhao-Ding & Gaba (ORSC)
**适用**: 研究问题关注"两个条件如何对同一组结果产生镜像反向效应"
**结构**:
```
Condition A → DV_dimension_1: +    Condition A → DV_dimension_2: -
Condition B → DV_dimension_1: -    Condition B → DV_dimension_2: +
```
**优势**: 理论系统性强，两条机制链结构平行但方向相反，展示理论的完整图景
**风险**: 如果两条 track 不是真正的镜像，会给人"为了对称而对称"的感觉
**调用语料**: `corpus/subprotocols/hypothesis_derivation_patterns.md`（Symmetric Opposing Dual-Track）

### 方式五：曲线关系双阶段论证（Curvilinear Two-Phase）

**代表**: Cui, Yang & Vertinsky (SMJ)
**适用**: 研究问题关注"X→Y 为什么不是线性关系，而是先增后减（或先减后增）"
**结构**:
```
Low X  → increasing Y  (reason 1 + reason 2)
High X → decreasing Y  (reason 1 + reason 2)
```
**优势**: 能完整解释曲线关系的两个阶段，展示理论对关系全区间的掌控；常与调节效应结合
**风险**: 如果只有一个阶段机制强，另一个阶段薄弱，会显得牵强；转折点必须有理论依据
**调用语料**: `corpus/subprotocols/hypothesis_derivation_patterns.md`（Curvilinear Relationship — Two-Phase Argumentation）

### 如何选择？

| 如果你的核心问题是... | 选择 | 关键判断标准 |
|---------------------|------|------------|
| "X 如何通过 M 影响 Y？" | 深度链式 | 机制可被拆解为 2-3 个因果步骤 |
| "为什么 X 影响 Y 有多种理论支撑？" | 宽度理由并行 | 存在 2-3 个概念独立的理论理由 |
| "X→Y 在什么条件下成立/反向？" | 条件化复杂化 | 边界条件本身是理论核心而非稳健性检验 |
| "X 的维度 A 和维度 B 对 Y1 和 Y2 产生对称反向效应？" | 2×2 对称矩阵 | IV 有两维、DV 有两类、理论预期对称反向 |
| "两个条件如何对同一组互补维度产生镜像反向效应？" | 对称反向双轨 | 两个条件理论上是镜像，DV 两个维度是互补关系 |
| "X→Y 为什么是曲线关系（先增后减/先减后增）？" | 曲线关系双阶段论证 | 理论预期存在成本-收益权衡、激励反转或阈值效应 |

**混合策略**：一篇论文可以混合使用。例如 Singh & Grewal 在 H1 用深度链式（铁三角机制），在 H2-H4 用条件化复杂化。Shen et al. 在 H1 用深度链式（三机制 trunk），在 H2-H5 用条件化复杂化。Cui et al. 在 H1 用曲线关系双阶段论证，在 H2-H4 用宽度理由并行调节论证。

---

## QC 检查点

- [ ] 每个假设前的 why chain 是否有至少 2-3 步推理？
- [ ] 机制链是否可证伪？（是否能想到 alternative mechanism？）
- [ ] Mediator 是否与 IV 和 DV 在理论上都有链接？
- [ ] 是否避免了 "X affects M, M affects Y, therefore mediation" 的机械拼接？
- [ ] 收束论证是否明确说明了"比直接效应范式多知道了什么"？
- [ ] 最后假设是否自然收束（非突然中断）？
