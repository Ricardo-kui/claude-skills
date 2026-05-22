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
