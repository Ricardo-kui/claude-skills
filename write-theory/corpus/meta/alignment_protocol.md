# 跨 Section 对齐协议（Introduction ↔ Theory）

本协议定义 Introduction 和 Theory 之间必须保持一致的关键接口点。

**调用方式**：write-theory 在生成任何输出前，必须执行此对齐检查并作为输出的一部分呈现。

---

## 对齐维度

### 维度 1：Gap → Theory 构建类型一致性

| 检查项 | Introduction 信号 | Theory 必须满足 | 失败模式 |
|--------|-------------------|-----------------|----------|
| Gap 能量匹配 | Incommensurability 使用 Tension `06-theoretical-imbalance` | Theory 必须包含竞争机制或竞争假设 | Theory 只给单一机制，无对立论证 |
| Gap 叙事兑现 | Intro 声称"两种理论矛盾" | Theory 必须呈现两种理论路径 | Theory 只呈现一种理论视角 |
| 构念承诺 | Intro Preview 提及构念 A/B 的区分 | T1 必须界定这两个构念 | Theory 未界定或只界定一个 |

### 维度 2：Makadok 贡献声明 → Theory 模块覆盖

| Makadok 声明 | Introduction 句式（I7） | Theory 必须出现的模块 | 缺失即违约 |
|--------------|------------------------|----------------------|------------|
| Constructs | "We clarify [construct] by distinguishing [A] from [B]..." | T1（双构念界定）+ T3（区分维度推演） | T1 只定义一个构念 |
| Mechanism | "We explain why [X] affects [Y] by identifying [mechanism]..." | T3（≥2步机制链）+ T4（中介假设） | T3 单步跳跃 / T4 无中介假设 |
| Boundary | "We show that [relationship] depends on [moderator]..." | T5（调节机制）或 T3 嵌入边界 | 无调节假设 |
| Level | "We bridge [level A] and [level B]..." | T3（跨层机制：composition/emergence） | 无跨层论证 |
| Mode | "We reveal how [process] unfolds over time..." | T3（阶段序列+过渡条件） | 无时间/阶段标记 |

### 维度 3：Theory Preview → Theory 实际假设数

| Introduction 承诺 | 检测位置 | Theory 兑现标准 |
|-------------------|----------|-----------------|
| "we develop and test [N] hypotheses" | P5-P6 Preview | Theory 中假设数 = N |
| "we theorize a mediated relationship" | P5-P6 Theory Lens | Theory 必须含中介假设（H1:X→M, H2:M→Y 或 formal mediation） |
| "we identify boundary conditions" | P5-P6 / P7 Contribution | Theory 必须含至少一个调节假设 |
| "we propose competing predictions" | P5-P6 / P3 Gap | Theory 必须含 H1a/H1b 竞争假设对 |

### 维度 4：理论视角一致性

| 检查项 | Introduction 来源 | Theory 来源 | 不一致风险 |
|--------|-------------------|-------------|------------|
| T2 Theoretical Lens | P5 "Drawing on [theory]..." | T2 "Drawing on [theory]..." | 两处的理论名称必须一致 |
| 核心构念 | P5-P6 Preview 中提到的构念 | T1 中定义的构念 | 名称、scope、层次必须一致 |
| 关系方向 | P5 "[X] enhances [Y] through [M]" | T3 机制推演 + T4 假设方向 | 方向相反即严重错误 |

### 维度 5：Narrative Continuity（Pollock Ch02）

| 检查项 | Introduction 信号 | Theory 状态 | 结论 |
|--------|-------------------|-------------|------|
| Knot 继承 | `central_knot_statement` | P1 是否提及/暗示 knot | ✅/⚠️/❌ |
| 角色一致性 | `protagonist_construct` | 主角是否与 Theory 的核心 DV 一致 | ✅/⚠️/❌ |
| 叙事阶段连续性 | `narrative_arc` | Introduction 的 Denouement Preview 是否在 Theory 中被承接为 Rising Action | ✅/⚠️/❌ |
| Rising Action 完整 | `narrative_arc` | Theory 是否有 Knot Deepening + Tying 阶段 | ✅/⚠️/❌ |
| Plot 自然浮现 | — | 假设推导是否从构念互动中自然浮现 | ✅/⚠️/❌ |
| Extraneous Storyline | — | 是否有与 knot 无关的理论段落 | ✅/⚠️/❌ |
| Davis 有趣性 | `daviss_index_types` | Theory 的机制是否支撑 Introduction 承诺的有趣性 | ✅/⚠️/❌ |

**Narrative Continuity 详细检查**：

1. **Knot 继承检查**：
   - Introduction 的 `central_knot_statement` 是否在 Theory P1 中被明确承接？
   - 如果 Introduction 说"好公司为什么做坏事"，Theory P1 是否以"To resolve this paradox..."开头？
   - 如果 P1 未提及 knot → ⚠️ "Theory 开头未承接 Introduction 的 knot"

2. **角色一致性检查**：
   - Introduction 的 `protagonist_construct` 是否与 Theory 的核心 DV 一致？
   - Introduction 的 `supporting_constructs` 是否在 Theory 中以配角身份出现？
   - 如果 Theory 引入了 Introduction 未提及的新主角 → ⚠️ "新主角未在 Introduction 中预告"

3. **叙事阶段连续性检查**：
   - Introduction 的最后一个段落（Contribution）的叙事阶段是 Denouement Preview
   - Theory 的第一个段落（P1）的叙事阶段应是 Knot Inheritance（承接）
   - 检查：Theory P1 是否明确提及或暗示了 Introduction 的 central knot？
   - 如果 P1 未提及 knot → ⚠️ "Theory 开头未承接 Introduction 的 knot"
   - Theory 的叙事阶段应遵循：Knot Inheritance → Knot Deepening → Knot Tying → Knot Fully Tied
   - 如果某段落的叙事功能弱于前一段（如 Knot Deepening 后回到 Knot Inheritance）→ ⚠️ "叙事阶段倒退"

4. **Rising Action 完整性检查**：
   - Theory 是否有 Knot Deepening（P2-P4：构念定义、文献对话）？
   - Theory 是否有 Knot Tying（P5-PN：假设推导）？
   - Theory 是否有 Knot Fully Tied（T6 Closure）？
   - 如果缺少任一阶段 → ⚠️ "Rising Action 不完整"

5. **Plot Emergence 检查**：
   - 每个假设推导是否从构念定义中自然浮现？
   - 如果为了得到假设而重新定义构念 → ⚠️ "Plot 先于 Story"
   - 修复：回到构念定义，确保构念先于假设存在

6. **Extraneous Storyline 检查**：
   - 每个 Theory 段落是否服务于 central knot？
   - 如果某段落与 knot 无直接联系 → ⚠️ "Extraneous storyline"
   - 修复：删除、降级为控制变量、或移至附录/未来研究

7. **Davis 有趣性支撑检查**：
   - Introduction 承诺的 Davis 类型（如 False Similarity）是否在 Theory 中得到支撑？
   - 如果 Theory 的机制无法支撑该有趣性类型 → ⚠️ "Theory 无法兑现 Introduction 承诺的有趣性"

---

## 对齐检查输出格式

write-theory 必须在输出中强制包含以下块：

```markdown
### 跨 Section 对齐检查

| 维度 | 检查项 | Introduction 信号 | Theory 状态 | 结论 |
|------|--------|-------------------|-------------|------|
| Gap→Type | 能量匹配 | [Gap类型] + [Tension] | [构建类型] | ✅/⚠️/❌ |
| Makadok→Module | 贡献兑现 | [Makadok维度] | [模块覆盖] | ✅/⚠️/❌ |
| Preview→H | 假设数 | "[N] hypotheses" | [实际N个] | ✅/⚠️/❌ |
| Lens→Lens | 理论一致性 | "[theory]" | "[theory]" | ✅/❌ |

**必须修复的不一致**：
- [ ] [具体不一致项1]
- [ ] [具体不一致项2]
```

---

## 常见跨 Section 断裂模式

| 断裂模式 | 表现 | 修复策略 |
|----------|------|----------|
| **预告过度** | Intro 声称"4个假设"，Theory 只推导了3个 | 补回缺失假设，或修改 Intro Preview |
| **理论漂移** | Intro 用制度理论开场，Theory 用 RBV 推演机制 | 统一理论视角，或 Intro 增加理论整合说明 |
| **方向反转** | Intro Preview 说"正向影响"，Theory 假设为负 | 检查 T3 机制链，通常机制推演有误 |
| **Gap 降级** | Intro 用 Incommensurability（高能量），Theory 只做了 Incompleteness 式补充 | Theory 必须呈现对立论证，不能回避矛盾 |
| **构念失踪** | Intro 提到 moderator Z，Theory 未定义 Z | T1 必须定义所有主角+配角 |
