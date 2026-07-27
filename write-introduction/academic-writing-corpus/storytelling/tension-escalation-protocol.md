---
type: storytelling_tool
canonical_id: "tension-escalation-protocol"
source: "Pollock 2025 Ch02"
created: 2026-06-01
required: false
estimated_lines: 152
dependencies: []
---

# 叙事阶段连续性协议（Narrative Stage Continuity Protocol）

## 定义

本协议检查 Introduction 各段落是否按照 Freytag's Pyramid 的叙事阶段顺序推进，确保读者体验到连贯的 exposition → rising action → denouement preview 弧线。

> "Everything you write should either contribute to tying or unraveling the knot at the heart of your story." — Pollock 2025, Ch02

**核心原则**：不用数字评分，用叙事功能判断——每个段落是否让 central knot 更紧或更明显？

## 各模块的叙事阶段与功能

| 模块 | 叙事阶段 | 核心功能 | 检查问题 |
|------|---------|---------|---------|
| **Hook** | Exposition | 建立背景、引入主角、暗示 central knot | knot 是否被暗示？读者是否想知道答案？ |
| **Lit Turn** | Early Rising Action | 展示已有理解的局限性 | knot 是否开始显现？ |
| **Gap** | Rising Action | 精确 tying the knot | knot 是否更紧了？ |
| **Stakes** | Rising Action | 加深 knot 的紧迫性 | 不解决会怎样？ |
| **Theory Lens** | Rising Action | 提出理论解决路径 | knot 是否 fully tied？ |
| **Preview** | Late Rising Action | 预告 empirical 检验 | 读者是否感到"必须看结果"？ |
| **Contribution** | Denouement Preview | 预告 resolution 的形态 | 是否回到 knot 并承诺解开？ |

## 连续性检查规则

### 阶段顺序规则

允许的推进序列：
```
Exposition → Early Rising Action → Rising Action → Late Rising Action → Denouement Preview
```

**禁止的倒退**：
- Rising Action → Exposition（后一段功能弱于前一段）
- Denouement Preview → Rising Action（过早给出 resolution）
- 同一阶段内功能弱化（如 Gap 的 tension 弱于 Lit Turn）

### 阶段倒退检测

| 倒退模式 | 表现 | 检测标准 | 修复 |
|---------|------|---------|------|
| **高开低走** | Hook 暗示了 strong knot，但 Gap 只是 mild incompleteness | Gap 没有让 knot 更紧 | 加强 Gap 的 problematization（用 Inadequacy/Incommensurability 替代 mere Incompleteness） |
| **缺口未填** | Gap 之后直接跳到 Contribution，跳过 Stakes | Contribution 前没有 Stakes | 补充 1-2 句 Stakes（实践代价或理论代价） |
| **过早 denouement** | Contribution 在 Preview 之前出现 | 段落顺序错误 | 调整段落顺序：Preview 必须在 Contribution 之前 |
| **阶段平台** | 连续两段都在 exposition，没有推进到 rising action | Lit Turn 和 Hook 功能相同 | 合并或加强 Lit Turn，让它展示共识的局限性 |
| **过度承诺** | Contribution 声称超出实际交付 | Contribution 的 resolution 比 Gap 的 tension 更宏大 | 降低 Contribution 的宣称或提升 Gap 的 tension |

### 阶段推进标准

每段与前一段对比，判断功能是否推进：

**Exposition → Rising Action 的推进标准**：
- [ ] 后一段是否引入了新的 complication、limitation 或 blindspot？
- [ ] 后一段是否让 central knot 的具体内容更清晰？
- [ ] 后一段是否增加了 reader 想知道答案的动机？

**Rising Action → Denouement Preview 的推进标准**：
- [ ] 后一段是否预告了 resolution 的具体形态？
- [ ] 后一段是否让读者感到"我需要看 results 才能验证"？
- [ ] 后一段是否回到 central knot 并承诺解开？

## Gap 类型与叙事弧线

> **双轴纪律**：叙事弧线按 `gap_type` 选择（本节）；Literature Turn 的内部构造按 `conversation_strategy` 选择（`literature-turns/_index.md` + `diagnose-introduction/references/intertextual-construction-playbook.md` 的 3×3 矩阵）。两轴独立——弧线强度不由 Literature Turn 策略推出，反之亦然。

### Incompleteness（温和上升）

**弧线特征**：
- Exposition 较长（Hook + Lit Turn 可能各占 2 段）
- Rising Action 平缓（Gap 温和指出遗漏，Stakes 不尖锐）
- Denouement Preview 温和（Contribution 用"extend""refine"而非"challenge"）

**典型段落功能分配**：
```
P1-P2: Exposition（背景 + 文献共识）
P3: Early Rising Action（指出遗漏）
P4: Rising Action（解释遗漏的重要性）
P5: Late Rising Action（理论解决路径 + 预览）
P6: Denouement Preview（温和贡献声明）
```

**风险**：exposition 过长导致 reader 失去兴趣 → 检查 Hook 是否有足够 concrete detail

### Inadequacy（中等上升）

**弧线特征**：
- Hook 暗示 paradox
- Gap 直接指出文献的盲区或错误假设
- Stakes 揭示具体代价
- Contribution 用"reconcile""clarify"

**典型段落功能分配**：
```
P1: Exposition（paradox）
P2: Early Rising Action（文献对话，展示盲区）
P3-P4: Rising Action（指出 inadequacy + stakes）
P5-P6: Late Rising Action（理论透镜 + 预览）
P7-P8: Denouement Preview（贡献声明）
```

### Incommensurability（急剧上升）

**弧线特征**：
- Hook 强烈挑战共识
- Gap 直接说文献是"wrong""misleading"
- Stakes 尖锐（理论代价或实践代价）
- Contribution 用"challenge""reconcile""show that...is false"

**典型段落功能分配**：
```
P1: Exposition（强冲突暗示）
P2: Early Rising Action（展示对立文献）
P3-P4: Rising Action（尖锐 gap + high stakes）
P5-P6: Late Rising Action（竞争理论 + 预览）
P7-P8: Denouement Preview（强贡献声明）
```

**风险**：tension 过高但后续 delivery 不足 → Contribution 必须匹配 Gap 的强度

## 范文叙事弧线分析

### Haunschild et al. (2015) — 产品召回（Inadequacy）

| 段落 | 叙事阶段 | 功能 | knot 推进检查 |
|------|---------|------|-------------|
| Hook (14条生命) | Exposition | 具体代价，暗示 paradox | ✅ knot 被暗示：好公司为什么做坏事 |
| Lit Turn | Early Rising Action | 文献回顾，展示共识 | ✅ knot 开始显现：文献关注X但未考虑Y |
| Gap | Rising Action | 直接指出盲区 | ✅ knot 更紧："prior research has focused on... but has not considered..." |
| Stakes (嵌入 Gap) | Rising Action | 14条生命 + 理论代价 | ✅ knot 更紧迫 |
| Theory Lens | Rising Action | 提出组织学习理论 | ✅ knot 即将 fully tied |
| Preview | Late Rising Action | 面板数据 + 方向性预览 | ✅ reader 想知道结果 |
| Contribution | Denouement Preview | Mechanism 贡献声明 | ✅ 回到 knot，承诺 resolution |

**阶段倒退检查**：Hook→Lit Turn 功能是否倒退？Hook 用 14 条生命建立 urgency，Lit Turn 转为文献回顾（功能似乎弱化）。但 Haunschild 的 Lit Turn 很短（1 段），且 immediately 指向文献盲区，所以功能仍在推进。

**架构注记（2026-07-27）**：Haunschild 2015 的 Hook（14 条生命 field 张力）+ Gap（学习理论不能处理修正-复发）是**双重张力交织**（twin-complication）的隐式使用——田野张力与理论张力互为表里。该架构已显式化为 `../hooks/22-twin-complication.md`（GBL Ch3 Turner 1976 原型），含双 resolution 纪律与删除检验；现象驱动论文在设计 Hook 时应先检查是否满足该架构的合同条件。

### Eilert et al. (2017) — CSR（Incommensurability）

| 段落 | 叙事阶段 | 功能 | knot 推进检查 |
|------|---------|------|-------------|
| Hook (数据) | Exposition | 温和数据开场 | ✅ 暗示 CSR 的 paradox |
| Lit Turn | Early Rising Action | 展示文献对立 | ✅ knot 显现：文献认为 CSR→好，但有反例 |
| Gap | Rising Action | 直接挑战"CSR 总是好的" | ✅ knot 更紧：挑战核心假设 |
| Stakes (嵌入 Gap) | Rising Action | 实践 + 理论 stakes | ✅ knot 更紧迫 |
| Theory Lens | Rising Action | 代理理论 + 行为理论冲突 | ✅ knot fully tied |
| Preview | Late Rising Action | 自然实验 + IV 策略 | ✅ reader 必须看结果 |
| Contribution | Denouement Preview | 直接挑战 CSR 核心假设 | ✅ 回到 knot，承诺 resolution |

**阶段倒退检查**：无。每个段落的功能都在推进 knot。
