---
type: storytelling_tool
canonical_id: "knot-continuity-check"
source: "Pollock 2025 Ch02"
created: 2026-06-01
required: false
estimated_lines: 138
dependencies: []
---

# Knot Continuity Check（跨 Section Knot 连续性检查）

## 定义

Central knot 必须从 Introduction 传递到 Theory，再到 Methods、Results、Discussion，形成一个**连续的叙事弧线**。如果某个 section 的 knot 与其他 section 不一致，读者会感到"这是另一篇论文"。

> "The ending should bring the readers back to the beginning and offer them a fresh perspective on the subject studied." — Pollock 2025, Ch02（引述 Johanson 1994）

## 跨 Section Knot 追踪表

| Section | Knot 表述 | 角色 | 能量级 | 检查 |
|---------|----------|------|--------|------|
| **Title** | [一句话暗示 knot] | — | 1-2 | Title 是否暗示了 central knot？ |
| **Abstract** | [压缩版 knot] | — | 2-3 | Abstract 是否包含 knot 的核心张力？ |
| **Introduction** | [完整版 knot] | 主角+对手暗示 | 1-9 | Introduction 是否 fully tied the knot？ |
| **Theory** | [继承+加深 knot] | 主角+配角展开 | 2-9 | Theory 是否继续 tying the knot？ |
| **Methods** | [检验 knot 的路径] | — | — | Methods 是否设计来检验 knot？ |
| **Results** | [knot 开始解开] | — | — | Results 是否直接回应 knot？ |
| **Discussion** | [knot 完全解开] | — | — | Discussion 是否回到 knot 并给出新视角？ |

## 连续性检查规则

### Introduction → Theory

| 检查项 | Introduction | Theory | 一致标准 | 不一致信号 |
|--------|-------------|--------|---------|-----------|
| Knot 表述 | `central_knot_statement` | P1 是否提及/暗示 | Theory P1 必须包含 Introduction knot 的关键词 | P1 用完全不同的词汇描述问题 |
| 主角 | `protagonist_construct` | 核心 DV/IV | 名称一致 | Theory 引入了新的核心构念 |
| 对手 | `antagonist_construct` | 被挑战的理论/现象 | 身份一致 | Theory 挑战了不同的理论 |
| 能量 | `contribution_energy` | P1 能量级 | Theory P1 ≥ Introduction Contribution - 1 | Theory 开头能量骤降 |
| Davis 有趣性 | `daviss_index_types` | Theory 机制 | Theory 的机制支撑 Introduction 承诺的有趣性 | Theory 无法支撑有趣性 |

### Theory → Methods

| 检查项 | Theory | Methods | 一致标准 | 不一致信号 |
|--------|--------|---------|---------|-----------|
| 假设 | H1-HN | 检验变量 | Methods 的变量与 Theory 的假设完全对应 | 变量缺失或多余 |
| 机制 | why chain | 识别策略 | Methods 的设计能检验 why chain 的每一步 | 识别策略无法检验机制 |
| Context | 情境描述 | 样本选择 | Methods 的样本来自 Theory 描述的情境 | 样本与 Theory 情境不符 |

### Theory → Results

| 检查项 | Theory | Results | 一致标准 | 不一致信号 |
|--------|--------|---------|---------|-----------|
| 假设 | H1-HN | 假设检验 | Results 按 H1-HN 的顺序呈现 | Results 遗漏假设或增加未假设的发现 |
| 方向 | 假设方向 | 系数方向 | 方向一致 | 方向相反（除非有合理的后 hoc 解释） |
| 机制 | 中介/调节机制 | 机制检验 | Results 包含机制检验（如中介分析、调节分析） | 只报告主效应，不检验机制 |

### Results → Discussion

| 检查项 | Results | Discussion | 一致标准 | 不一致信号 |
|--------|---------|------------|---------|-----------|
| Knot | 结果解开 knot | Discussion 总结 resolution | Discussion 回到 central knot | Discussion 讨论与 knot 无关的话题 |
| 意外发现 | 非显著/意外结果 | Discussion 解释 | 解释与 Theory 的逻辑一致 | 强行解释或忽略 |
| 贡献 | 发现支持/不支持假设 | Discussion 声明贡献 | 贡献声明与 Results 的实际发现匹配 | 过度承诺或回避 |

## 常见断裂模式

| 断裂模式 | 表现 | 检测 | 修复 |
|---------|------|------|------|
| **Introduction 讲 A，Theory 讲 B** | Intro 的 knot 是"好公司做坏事"，Theory 的假设是"绩效→创新" | 检查 Theory P1 是否承接了 Intro 的 knot | 统一 knot，重写 Theory P1 或 Intro |
| **Theory 讲机制 A，Methods 检验机制 B** | Theory 推导了中介机制，Methods 只做了 OLS | 检查 Methods 的变量是否包含中介变量 | 补充中介检验，或修改 Theory 假设 |
| **Results 发现 X→Y 负向，Discussion 解释为正向** | 方向不一致 | 检查 Discussion 是否诚实面对反向结果 | 重新解释，或承认假设未被支持 |
| **Discussion 引入新理论** | Discussion 用 Theory C 解释结果，但 Theory section 用的是 Theory A | 检查 Discussion 是否回到 Theory section 的理论 | 删除新理论，或用 Theory A 重新解释 |
| **Title/Abstract 的承诺未兑现** | Title 暗示颠覆性发现，Results 只有增量贡献 | 检查 Results 是否兑现了 Title/Abstract 的承诺 | 降低 Title/Abstract 的能量级，或加强 Results |

## 修复动作

### 跨 Section 对齐流程

```
Step 1: 从 Introduction 提取 central_knot_statement
Step 2: 检查 Theory P1 是否包含该 statement 的关键词
Step 3: 检查 Theory 的假设是否直接回应该 statement
Step 4: 检查 Methods 的变量是否与 Theory 假设完全对应
Step 5: 检查 Results 是否按假设顺序呈现
Step 6: 检查 Discussion 是否回到 central_knot_statement 并给出 resolution
Step 7: 如果任何一步不一致 → 标记断裂位置，给出修复建议
```

### 修复优先级

| 优先级 | 断裂类型 | 为什么优先 |
|--------|---------|-----------|
| P0 | Theory P1 未承接 Introduction knot | 读者会立即感到"这是另一篇论文" |
| P0 | 假设方向与 Results 相反 | 严重的方法-结果不一致 |
| P1 | Methods 变量与 Theory 假设不对应 | 实证设计无法检验理论 |
| P1 | Discussion 未回到 knot | 论文缺乏 resolution |
| P2 | Title/Abstract 与 Introduction 不一致 | 前端转化漏斗失败 |
| P2 | Discussion 引入新理论 | 理论框架漂移 |

## 能量曲线连续性

跨 Section 的能量曲线应形成**连续的弧线**：

```
Energy
   ^
 9 |                                                      [Discussion resolution]
 8 |                                            [Results climax]
 7 |                                    [Theory fully tied]
 6 |                            [Theory tying]
 5 |                    [Theory deepening]
 4 |            [Introduction climax]
 3 |      [Introduction rising]
 2 |[Introduction exposition]
 1 |
   +----+----+----+----+----+----+----+----+----+----
     Tt   Ab   In   Th   Th   Th   Th   Me   Re   Di
```

**规则**：
- Introduction 的结尾（Contribution）能量应 ≤ Theory 的开头（P1）能量
- Theory 的结尾（T6）能量应 ≤ Results 的开头能量
- Results 的结尾能量应 ≤ Discussion 的开头能量
- 如果任何 section 的开头能量低于前 section 的结尾能量 → 标记 ⚠️ "能量断裂"

## 范文：Mishina et al. (2010) 的跨 Section 连续性

| Section | Knot 表述 | 检查 |
|---------|----------|------|
| Title | "Why 'good' firms do bad things" | ✅ 直接暗示 knot |
| Abstract | "prominent and successful firms... risk engaging in illegal actions" | ✅ 压缩了 knot |
| Introduction | "why and under what conditions prominent and successful firms would risk engaging in illegal actions" | ✅ 完整 knot |
| Theory P1 | "This is how we began tying the knot that our study would unravel" | ✅ 明确承接 knot |
| Theory H1-H4 | 绩效→违法 + prominence 调节 | ✅ 直接回应 knot |
| Methods | 样本：被 caught 的违法公司 | ✅ 能检验 knot |
| Results | 支持主效应，部分支持调节 | ✅ 直接回应假设 |
| Discussion | "why more and less prominent firms reacted similarly... but differently" | ✅ 回到 knot，给出 resolution |

**Johanson 标准**：Discussion 的结尾"brings the readers back to the beginning and offers them a fresh perspective" → Mishina et al. 的 Discussion 解释了 prominence 的不同作用模式，确实提供了新视角。
