# Story Architecture 核心字段（Pollock 2025 Ch02-Ch05）

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：生成 Phase 0 输出的 story_architecture 字段时加载。供下游 write-introduction theory_hints 消费。

---

# Story Architecture 核心字段（Pollock 2025 Ch02-Ch05，供下游 write-introduction theory_hints 消费）
phase_0_story_architecture:
  central_knot_statement: "[用一句话概括的 central knot。从 Gap 段包含转折信号词（However/Yet/Although/In contrast）且含具体理论/现象名称的句子推断；如无法推断则填 null]"
  protagonist_construct: "[主角构念名称。从 Theory Lens 或 Preview 中提取，必须是 Introduction 中出现 ≥2 次的构念；无法提取则填 null]"
  supporting_constructs:
    - "[配角1，如 mediator/moderator，上限3个]"
    - "[配角2]"
  daviss_index_types:
    - "[匹配的 Davis 类型1，如无法推断则留空列表]"
    - "[匹配的 Davis 类型2]"
  front_end_consistent: null  # Phase 3 如有 Title/Abstract 输入再判定 true/false
```

#### Story Architecture 字段推断规则

**central_knot_statement**：
- 来源：Gap 段中同时包含 (a) 转折信号词和 (b) 具体理论/现象名称的完整句子
- 质量标准：必须是"包含冲突"的一句话，不能是"我们研究X"或"用DID方法"
- 回退：无符合条件的句子 → `null`（允许 null，不阻塞输出）

**protagonist_construct**：
- 来源：Theory Lens 的核心 IV/DV；或 Preview 中的核心构念
- 质量标准：Introduction 全文出现 ≥2 次
- 回退：无法提取 → `null`

**supporting_constructs**：
- 来源：Theory Lens 中提及的 mediator/moderator/control 变量
- 上限：最多 3 个

**daviss_index_types**（推断规则，用户未直接回答时）：
| Hook/Gap 组合 | 推断的 Davis 类型 |
|--------------|------------------|
| 数据冲击 + 现实矛盾共识 | False Positive / False Negative |
| 范式挑战 + 理论失衡 | Order from Chaos / Chaos from Order |
| 构念混淆 + 隐含假设错误 | False Similarity / False Difference |
| 政策反效果 + 成本效益 | Unobserved Bad / Unobserved Dysfunction |
| 其他组合 | 不推断，留空列表 |

**front_end_consistent**：
- 需要 Title/Abstract 输入时才检查。若仅有 Introduction 文本 → 保持 `null`

---
