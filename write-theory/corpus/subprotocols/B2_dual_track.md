# B2. 双轨并行机制推演型（Dual-Track Mechanism）

> **适用**: 同一构念的两个维度（current/prospective, prevention/promotion, short-term/long-term）通过不同心理机制产生差异化效应
> **范文**: Malik et al. (2025, JM)
> **母变体**: B 机制推演型

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 核心构念界定（双维度区分） | 80-150 | ✅ |
| P2 | 理论视角引入（需解释为什么构念有两个维度） | 60-100 | ✅ |
| P3-P5 | Track A 机制推演（维度A → 机制A → 行为A）+ H1a/H1b | 各 70-120 | ✅ |
| P6-P7 | Track B 机制推演（维度B → 机制B → 行为B）+ H2a/H2b | 各 70-120 | ✅ |
| P8 | [可选] 局部收束（"In summary, high [维度B] reduces..."）——非独立 Closure 段 | 50-80 | ⚠️ |
| P9+ | [可选] 边界/调节（对两条轨道的差异化调节） | 各 60-100 | ⚠️ |

> **管理学惯例**: 不要求独立 Closure 段。双轨对称结构本身即理论框架——最后假设后自然进入 METHODS。

---

## 双轨对称骨架

参见 `corpus/sentences/mechanism_chain.md` —— "双轨并行机制链（Track A / Track B）"

**核心原则**：
- Track A 和 Track B 的论证结构必须**严格对称**（段落数、文献数、机制步数）
- 两个维度必须**概念独立**（非同一维度的不同标签）
- 轨道切换必须使用 "Conversely" / "In contrast" / "Whereas" / "On the other hand"

---

## 假设陈述格式

| 类型 | 模板 |
|------|------|
| Track A 主效应 | "H[N]a: [X_A] is [positively/negatively] related to [Y]." |
| Track B 主效应 | "H[N]b: [X_B] is [positively/negatively] related to [Y]." |
| Track A 调节 | "H[M]a: The [positive/negative] effect of [X_A] on [Y] is [stronger/weaker] when [W] is [high]." |
| Track B 调节 | "H[M]b: The [positive/negative] effect of [X_B] on [Y] is [stronger/weaker] when [W] is [high]." |

---

## 语料锚定

- **Malik 2025 (JM)** — current wealth (loss aversion → strategic timing/silence) vs prospective wealth (long-term focus → open communication)
  - Track A: "A CEO holding options with a strike price of $99 while the current market price is $100... A 1% decline in stock price to $99 would cause a 100% loss..."
  - Track B: "Prospective wealth reflects the value of options if the firm's stock price rises... CEOs with high prospective wealth are oriented toward long-term growth..."
  - 轨道切换信号："Conversely, CEOs with high prospective wealth..."

---

## QC 检查点

- [ ] Track A 和 Track B 的论证结构是否**严格对称**（段落数、文献数、机制步数）？
- [ ] 两个维度是否概念独立（非同一维度的不同标签）？
- [ ] 是否使用了 "Conversely" 或 "In contrast" 明确标记轨道切换？
- [ ] 若有两条轨道，是否考虑增加调节假设解释 "何时 Track A 主导 vs Track B 主导"？
- [ ] 最后假设是否自然收敛（"Therefore/Thus" 局部收束）？

---

## 近邻变体（不要与 B2 混用）

| 模式 | 何时用 | 文件 |
|------|--------|------|
| **B2（本文件）** | 同一构念两维度 → 常异号/异行为预测 | 本文件 |
| **Sibling IVs + shared buffer** | 兄弟 IV（如 distance/dispersion）→ **同向**同 DV → 共享缓冲调节 H3a/H3b | `hypothesis_organization_patterns.md`::`sibling_ivs_mechanism_division_shared_buffer` |
| **Dual mechanism same direction** | **单** IV → 两条中介汇聚 → **一个** H | `argumentation_patterns.md`::`dual_mechanism_same_direction` |
| **Geometric sibling minimal pair** | 用图证明兄弟维度可分离（固定 A 变 B） | `construct_differentiation_patterns.md`::`geometric_sibling_construct_minimal_pair` |