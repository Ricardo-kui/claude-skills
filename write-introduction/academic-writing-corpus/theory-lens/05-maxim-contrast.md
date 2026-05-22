---
type: canonical_theory_lens
canonical_id: "theory-lens-05-maxim-contrast"
status: VERIFIED
gap_type: Incompleteness / Inadequacy
cross_paper: VERIFIED (1 paper, distinctive)
generativity: ADAPTABLE
exclusivity: HIGH
source_papers:
  - haunschild2015 (OS, 2015): "we will not launch until proved safe to do so" vs "we will launch unless it is proved unsafe to do so"
created: 2026-05-19
source: Distilled from Haunschild, Polidoro & Chandler (2015), Organization Science
---

# Theory Lens: Maxim Contrast / 格言对比

## 功能描述

将抽象的 **trade-off / competing goals / resource tension** 理论转化为**可记忆的对立口号/格言**（maxim）。通过两句结构对称、含义对立的组织决策"座右铭"，让审稿人瞬间 grasp 核心张力，无需阅读 Theory Development 就能理解研究逻辑。

这是 Theory Lens 模块中最独特的句法创新之一——不是用学术语言解释机制，而是用组织成员的**日常决策语言**来具象化理论。

## 适用场景

- Gap 类型 = **Incompleteness / Inadequacy**
- Contribution 维度 = **Mechanism**
- 前置条件: 研究涉及 **trade-off / competing goals / resource competition**（如安全 vs 效率、探索 vs 利用、集中 vs 分权）
- 两个竞争焦点可以被具象化为**对立的决策原则/口号**
- 目标期刊: OS, ASQ, AMJ, SMJ

## 验证状态

### 跨论文复现
- **VERIFIED** (1 paper, distinctive): haunschild2015 (OS)
- **可迁移性验证**: maxim 结构（"we will [do X] until [condition A]" vs "we will [do Y] unless [condition B]"）可迁移到任何二元决策场景

### 生成力
- **ADAPTABLE**: 格言对比结构可填入任何竞争目标

### 排他性
- **HIGH**: 仅适用于存在**明确二元张力**的研究。非 trade-off 类 Mechanism（如互补效应、协同效应）禁用此骨架

---

## 句法模板

### 变体 A：资源约束 + Maxim 对比（haunschild2015 型）

> "We argue that this [pattern] occurs because, fundamentally, resources devoted to one activity cannot be devoted to another ([citations]), which creates tensions for any [actor] with limited resources. In [Context]'s case, choosing to focus on [state A] indicates a commitment to a set of behaviors that will deliver its [output] [quality standard]. In [decision context], this constitutes support for the statement '[maxim for A].' Choosing to focus on an alternative behavior, such as [state B], however, indicates a commitment to operating in a [productive fashion], adopting a set of behaviors that ensure that the [output] is delivered at [volume/cost standard]. In terms of [decision context], such a focus constitutes support for the statement '[maxim for B].' Although we do not suggest that [state A] and [state B] are diametrically opposed and mutually exclusive, we do argue that an [actor]'s relative emphases on [state A] versus other foci are related and will shift over time."

**来源**: haunschild2015 (OS), P5

**原文锚定**:
> "We argue that this oscillation occurs because, fundamentally, resources devoted to one activity cannot be devoted to another (Perrow 1984, Heimann 2005, Vaughan 2005), which creates tensions for any organization with limited resources. In NASA's case, choosing to focus on safety indicates a commitment to a set of behaviors that will deliver its product error-free (or nearly so). In deciding to launch a shuttle, this constitutes support for the statement 'we will not launch until proved safe to do so.' Choosing to focus on an alternative behavior, such as efficiency, however, indicates a commitment to operating in a productive fashion, adopting a set of behaviors that ensure that the product is delivered at maximum volume with minimum costs. In terms of a shuttle launch, such a focus constitutes support for the statement 'we will launch unless it is proved unsafe to do so.' Although we do not suggest that safety and efficiency are diametrically opposed and mutually exclusive, we do argue that an organization's relative emphases on safety versus other foci are related and will shift over time."

**关键特征**:
1. **资源约束先行**: 先用 Perrow/Heimann/Vaughan 等权威建立理论基础
2. **对称结构**: A 的选择 → A 的行为 → A 的标准 → A 的 maxim。然后 B 的选择 → B 的行为 → B 的标准 → B 的 maxim。镜像对称。
3. **Maxim 句式**: "we will [action] until [condition]" vs "we will [opposite action] unless [opposite condition]"
4. **边界限定**: "Although we do not suggest... are diametrically opposed" —— 防止审稿人攻击二元对立过于简化
5. **动态结论**: "relative emphases... are related and will shift over time" —— 不是静态分类，而是动态 oscillation

---

## 关键功能短语

| 短语 | 功能 |
|------|------|
| "resources devoted to one activity cannot be devoted to another" | 建立 trade-off 的理论基础 |
| "constitutes support for the statement" | 将理论焦点转化为组织格言 |
| "[maxim for A]" vs "[maxim for B]" | 可记忆的对立口号 |
| "Although we do not suggest... are diametrically opposed and mutually exclusive" | **边界限定句，不可省略** |
| "relative emphases... are related and will shift over time" | 动态化结论 |

---

## Maxim 创作指南

好的 maxim 需要满足：

1. **结构对称**: A 和 B 使用相同的语法结构
   - ✅ "we will not launch **until** proved safe" / "we will launch **unless** proved unsafe"
   - ✅ "innovate **until** market saturation" / "standardize **unless** demand shifts"

2. **决策场景明确**: maxim 必须来自具体的组织决策情境
   - ✅ "deciding to launch a shuttle" → "we will not launch until..."
   - ❌ "safety is important" → 无决策场景

3. **关键词对立**: A 和 B 的核心动词/条件词形成对比
   - until (肯定条件触发行动) vs unless (否定条件阻止行动)
   - maximize (增量逻辑) vs minimize (减量逻辑)

4. **长度接近**: 两句 maxim 字数差异不超过 5 个词

---

## 组装规则

### 必须配对
- **与 `14-paired-disasters` (Hook) 配对**: 极端案例建立的 safety-efficiency 张力，需要 maxim contrast 来具象化
- **与 `13-sequential-phenomenon-gap` (Tension) 配对**: sequential cycling 的 gap 需要资源竞争机制来解释

### 互斥
- **不能与互补效应/协同效应研究同用**: maxim contrast 的核心是"资源竞争导致张力"，若研究的是 A 和 B 互补（如资源协同），使用此骨架会造成类型错配
- **不能与静态分类研究同用**: 骨架结尾 "will shift over time" 假设动态 oscillation，静态研究禁用

---

## 反模式提醒

- **省略边界限定句**: "Although we do not suggest... are diametrically opposed" 若省略，审稿人会攻击二元对立假设过于简化。这是 Haunschild 论文中**最关键的自我保护句**。
- **Maxim 与理论脱节**: maxim 必须直接反映资源约束理论。若 maxim 只是"听起来好"但与资源竞争无关，会失去理论合法性。
- **过度抽象**: "We focus on quality" vs "We focus on efficiency" 不是 maxim，只是陈述。Maxim 必须包含**决策条件**（until/unless/when/if）。

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| OS | ⭐⭐⭐ 极高 | OS 偏好组织过程研究，maxim 是员工/管理者日常语言，完美适配 |
| ASQ | ⭐⭐⭐ 高 | ASQ 欣赏具象化理论，但 maxim 必须引用经典理论（如 Perrow）建立合法性 |
| AMJ | ⭐⭐⭐ 高 | 适用于心理构念的具象化（如 approach motivation: "seek gain" vs avoidance motivation: "avoid loss"） |
| SMJ | ⭐⭐ 中 | SMJ 偏好抽象理论语言，maxim 可能被视作"过于通俗" |
| JM/JMR | ⭐⭐ 中 | 需将 maxim 转化为消费者/营销决策语言 |