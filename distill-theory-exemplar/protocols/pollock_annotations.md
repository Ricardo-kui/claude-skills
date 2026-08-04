# Pollock 标注协议（Phase 0.5 Rising Action + Phase 0.75 Prose Craft）

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 0 分类完成后、Phase 1 模块映射前加载。

---

## Phase 0.5 — Rising Action 定位与 Central Knot 继承检查（Pollock Ch02，v1.2.0 新增）

Theory & Hypotheses 在整篇论文的 Five-Act 结构中属于 **Rising Action** 的后半段。蒸馏时必须检查 Theory 是否继承了 Introduction 建立的 Central Knot，并验证叙事连续性。

### 输入接口

如果输入包含 Introduction 文本或上游 `write-introduction` 输出的 `theory_hints` YAML 块，解析以下字段：
- `central_knot_statement`：如果存在且非 `null` → 作为 Theory 的叙事锚点
- `narrative_arc`：决定 Theory 的 rising action 强度
- `protagonist_construct` / `supporting_constructs`：作为角色定位初始值

### Central Knot 推断规则（当上游未提供时）

从 Theory 文本自身推断核心冲突：
- Incommensurability → "对立理论或证据之间的矛盾冲突"
- Inadequacy → "现有解释存在盲区或基于错误假设"
- Incompleteness → "遗漏了关键维度、机制或时点"
- 具体推断：从 T3 Mechanism Chain 的转折信号词或 T2 Theoretical Lens 的框架对立中提取

### Phase 0.5 诊断流程

按顺序检查以下叙事对齐项：

1. **Knot 继承检查**
   - Theory P1（T1/T2）是否明确或暗示地承接了 Introduction 的 central knot？
   - 标志："To resolve the paradox that [knot]..." / "To explain why [knot]..."
   - 如无 explicit 承接，检查是否 implicit 通过 Gap 文献的延续来承接

2. **Rising Action 强度检查**
   - 对比 Introduction 的 `narrative_arc` 与 Theory 的 rising action 强度
   - Theory 的 rising action 应 ≥ Introduction 的 closing energy，为 Results climax 蓄力
   - 检测：T1-T2 能量级是否低于 Introduction P7-P8 → 标记"叙事阶段倒退"

3. **Characters 一致性检查**
   - Theory 中的主角/配角是否与 Introduction 承诺的一致？
   - Introduction 承诺了 mediator M，但 Theory T1 未定义 M → 标记"角色缺失"
   - Introduction 的 protagonist 在 Theory 中出场次数 < 3 → 标记"主角淡出"

4. **Plot Emergence 检查**
   - 情节是否从构念互动中自然浮现，而非强加？
   - 检测：T3 的 why chain 是否从 T2 的理论框架自然推导而来？
   - T3 引入了新理论视角但未在 T2 铺垫 → 标记"extraneous storyline"

### 输出格式

```yaml
phase_0_5_rising_action:
  central_knot_inherited: true/false
  knot_inheritance_statement: "[Theory 中承接 knot 的具体句子]"
  knot_inheritance_location: "T1/T2/P[段号]"
  narrative_arc_continuity: "一致 / 增强 / 倒退"
  protagonist_consistent: true/false
  protagonist_presence_in_theory: "[N] 次提及"
  supporting_construct_consistent: true/false
  missing_promised_construct: "[如有，列出 Introduction 承诺但 Theory 未定义的构念]"
  plot_emergence_natural: true/false
  extraneous_storyline_risk: "[描述，如无则 null]"
```

---

## Phase 0.75 — Prose Craft 定位（Pollock Ch03，v1.2.0 新增）

Theory section 的 Rising Action 不仅需要功能推进，还需要 prose 层面的可读性。以下三个工具与 Phase 1-5 并行执行。

### 1. Human Face in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| P1 Knot Inheritance | 用 1 句具体场景说明"这个问题在现实世界中长什么样" | 记录具体场景句 |
| 新构念首次出现 | 构念抽象、易混淆或定义后仍不直观时可配正例/反例 | 记录例子承担的澄清功能；无例子不自动失败 |
| P5-PN Why-chain 关键步骤 | 每个 why-chain 关键步骤可配 1 个微型场景（1-2句） | 记录微型场景句 |

### 2. Showing vs Telling in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| Stroke 段落 | 推理负荷过高时用解释/例子帮助吸收，不设固定比例 | 记录 illustration 类型、位置与是否真正必要 |
| Glide 段落（30%） | 用比喻/类比解释抽象概念 | 记录比喻/类比句 |
| 连续无 showing | 不允许连续 2 个 stroke 句子无 showing | 标记断裂位置 |

### 3. Conversational Voice in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| P1 承接 | "To resolve the paradox that [knot], we argue that..." | 记录承接句式 |
| 假设推导 | "We argue that..." / "We hypothesize that..." | 记录主动语态频率 |
| T6 收束 | "In sum, we have argued that..." | 记录收束句式 |
| 禁止被动 | 无 "It is argued that..." / "It is hypothesized that..." | 标记被动语态位置 |

### Prose Craft 输出格式

```yaml
phase_0_75_prose_craft:
  human_face:
    p1_scene_present: true/false
    p1_scene_text: "[具体场景句]"
    construct_illustrations:
      - construct: "[构念名]"
        illustration: "[例子内容]"
        location: "T[模块] P[段号]"
    why_chain_scenes:
      - step: "[机制步骤]"
        scene: "[微型场景]"
        location: "P[段号]"
  showing_vs_telling:
    stroke_paragraphs: N
    glide_paragraphs: N
    stroke_glide_ratio: "N:N"
    illustration_types: ["案例", "数字", "场景", "具体研究"]
    showing_gaps: ["[断裂位置描述]"]
  conversational_voice:
    active_voice_count: N
    passive_voice_count: N
    passive_voice_locations: ["P[段号]: [原句]"]
    hypothesis_transition_phrases: ["Therefore, we hypothesize:", "Thus:"]
    closure_phrase: "[T6 收束句]"
```

---
