---
type: meta_routing
canonical_id: "theory-variant-routing"
source: "Pollock 2025 Ch06 + SKILL.md Phase 0"
created: 2026-06-01
version: 1.0.0
---

# Theory Variant 路由表

本文件定义从 Introduction 输出（Gap 类型、Makadok 维度、Tension 模板）到 Theory 构建变体的映射规则。

**调用方式**：`write-introduction` 在生成 `theory_hints` 时读取本文件，确定 `recommended_theory_variant` 和 `variant_confidence`。

**回退策略**：如果查询无匹配，`recommended_theory_variant` 设为 `null`，`variant_confidence` 设为 `null`，由 write-theory 的 Phase 0 交互式诊断处理。

---

## 一级路由：Gap × Makadok → Theory Variant

| Gap 类型 | Makadok 维度 | Theory 变体 | 变体代码 | 置信度 | 理由 |
|---------|-------------|------------|---------|--------|------|
| **Incompleteness** | Constructs | 构念辨析型 | A | medium | Incompleteness 常为构念遗漏，需先界定新构念 |
| Incompleteness | Mechanism | 机制推演型 | B | high | Incompleteness + Mechanism 是最常见组合 |
| Incompleteness | Boundary | 调节效应型 | E | medium | 边界条件遗漏 → 引入 moderator |
| Incompleteness | Level | 假设树型 | C | medium | 跨层遗漏 → 多层次假设体系 |
| Incompleteness | Mode | 质性过程理论型 | D | low | Incompleteness 较少触发过程理论 |
| Incompleteness | Question | 竞争假设型 | F | low | Incompleteness 较少直接挑战理论 |
| Incompleteness | Output | 机制推演型 | B | high | 输出维度遗漏 → 机制解释 |
| Incompleteness | Phenomenon | 机制推演型 | B | high | 新现象 → 机制解释 |
| **Inadequacy** | Constructs | 构念辨析型 | A | medium | 构念误置 → 需要重新界定 |
| Inadequacy | Mechanism | 机制推演型 | B | high | 机制误置 → 重新推导 why chain |
| Inadequacy | Boundary | 调节效应型 | E | high | 最经典组合：现有机制在特定边界下失效 |
| Inadequacy | Level | 假设树型 | C | medium | 层次误置 → 跨层假设 |
| Inadequacy | Mode | 竞争假设型 | F | medium | 模式误置 → 两种理论的竞争预测 |
| Inadequacy | Question | 竞争假设型 | F | medium | 问题误置 → 重新定义问题 |
| Inadequacy | Output | 机制推演型 | B | high | 输出误置 → 修正机制 |
| Inadequacy | Phenomenon | 机制推演型 | B | high | 现象误置 → 修正解释 |
| **Incommensurability** | Constructs | 构念辨析型 | A | high | 构念混淆 → 必须区分 |
| Incommensurability | Mechanism | 竞争假设型 | F | high | 理论冲突 → 竞争预测 |
| Incommensurability | Boundary | 调节效应型 | E | medium | 边界冲突 → 识别条件 |
| Incommensurability | Level | 假设树型 | C | high | 层次冲突 → 多层次竞争 |
| Incommensurability | Mode | 竞争假设型 | F | high | 模式冲突 → 两种理论竞争 |
| Incommensurability | Question | 竞争假设型 | F | high | 问题冲突 → 直接竞争 |
| Incommensurability | Output | 竞争假设型 | F | medium | 输出冲突 → 竞争解释 |
| Incommensurability | Phenomenon | 竞争假设型 | F | medium | 现象冲突 → 竞争解释 |

---

## 二级路由：Introduction 文本信号 → 子协议

当一级路由确定变体后，检查 Introduction 中的文本信号，进一步确定是否需要子协议。

### 变体 B（机制推演型）的子协议

| Introduction 信号 | 子协议 | 触发条件 |
|-------------------|--------|----------|
| `promised_mechanism_steps: 2` | B2 双轨并行 | 同一构念的两个维度产生相反/互补预测 |
| Preview 提及 "parallel mechanisms" | B2 双轨并行 | 明确提及双机制 |
| Contribution 提及 "multiple pathways" | B2 双轨并行 | 声称多路径机制 |

**B2 判定标准**：
- [ ] 是否存在两个不同的理论机制解释同一关系？
- [ ] 两个机制是否产生不同的可检验预测？
- [ ] 是否有至少一个调节变量区分两种机制？

### 变体 E（调节效应型）的子协议

| Introduction 信号 | 子协议 | 触发条件 |
|-------------------|--------|----------|
| `interaction_type: within` | E1 同层调节 | 调节变量与 IV/DV 在同一分析层级 |
| `interaction_type: cross` | E2 跨层调节 | 调节变量在更高/更低层级 |
| Preview 提及 "categorical moderator" | E1.1 分组调节 | 调节变量为分类变量 |

**E2 判定标准**：
- [ ] 是否明确声明了 focal unit of analysis？
- [ ] 是否说明了 nesting structure（如 firm within industry）？
- [ ] 跨层调节是否在 P1 就声明？

---

## 三级路由：Gap 能量级 → 机制深度要求

| Gap 能量级 | 要求的最小机制步数 | 假设结构要求 |
|-----------|-------------------|-------------|
| low (Incompleteness) | 2 步 | 主效应 + 中介（可选） |
| medium (Inadequacy) | 2-3 步 | 主效应 + 中介 或 主效应 + 调节 |
| high (Incommensurability) | 3-4 步 | 主效应 + 中介 + 调节 或 竞争假设对 |

**机制步数定义**：
- 1 步：X → Y（直接效应）
- 2 步：X → M → Y（中介）或 X × Z → Y（调节）
- 3 步：X → M1 → M2 → Y（链式中介）或 X → M → Y + X × Z → Y（中介+调节）
- 4 步：X → M1 → M2 → Y + X × Z → Y（完整机制+边界）

---

## 冲突处理

当一级路由和二级路由冲突时：

| 冲突场景 | 优先级规则 | 示例 |
|---------|-----------|------|
| 一级路由推荐 B，但文本信号暗示 B2 | 二级优先 | 变体 = B2，置信度降一级 |
| 一级路由推荐 E，但无 interaction_type | 默认 E1，置信度 = low | 在 Phase 0 诊断时确认 |
| Gap 类型 = Incommensurability，但 Makadok = Boundary | 以 Gap 为主，Makadok 为辅 | 变体 = E，但要求呈现理论冲突背景 |
| 多个文本信号指向不同子协议 | 以最先出现的信号为准 | 在提醒中标注备选方案 |

---

## 从 theory_hints 到变体的解析流程

```
theory_hints:
  gap_type: "Incompleteness"
  makadok_dimension: "Mechanism"
  tension_template: "01-despite-progress-unaddressed"
  promised_mechanism_steps: 2
  promised_mediation: true
  promised_boundary_conditions: false
```

**解析步骤**：
1. 查一级路由表：`Incompleteness` + `Mechanism` → `B`（机制推演型），置信度 `high`
2. 检查 `promised_mechanism_steps`：= 2 → 不需要 B2 子协议
3. 检查 `promised_mediation`：= true → 验证机制推演型是否含中介假设
4. 检查 `promised_boundary_conditions`：= false → 确认无调节假设
5. 输出：`recommended_theory_variant: "机制推演型"`，`variant_confidence: "high"`

**如果缺少关键字段**：
- `gap_type` 缺失 → 回退到 Phase 0 交互式诊断
- `makadok_dimension` 缺失 → 默认 `Mechanism`，置信度降为 `low`
- `tension_template` 缺失 → 忽略，不影响一级路由

---

## 与 write-theory Phase 0 的接口

write-introduction 将 `recommended_theory_variant` 写入 `theory_hints`，write-theory 在 Phase 0 解析：

```python
# 伪代码（概念性）
def phase0_diagnosis(theory_hints):
    variant = theory_hints.get('recommended_theory_variant')
    confidence = theory_hints.get('variant_confidence')
    
    if variant and confidence in ['high', 'medium']:
        return variant  # 直接使用推荐变体
    elif variant and confidence == 'low':
        return f"{variant}（建议确认）"  # 推荐但要求用户确认
    else:
        return interactive_diagnosis()  # 进入交互式诊断
```

---

## 更新日志

- **v1.0.0** (2026-06-01): 初始版本。基于 Pollock 2025 Ch06 的 Section Architecture 六因素表和 Gap 类型 × Makadok 交叉映射建立。包含一级路由（Gap × Makadok → Variant）、二级路由（文本信号 → 子协议）、三级路由（能量级 → 机制深度）。
