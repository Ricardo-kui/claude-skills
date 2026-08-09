# Hypothesis-Fulfillment Map — 假设-结果承诺兑现框架（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成 Results 骨架前**必建**：本 skill 的核心任务是**兑现 Theory 的假设承诺**。确保每个 Theory 假设都有对应的 Results 段落。

## 映射表

| 假设 | Theory 预测 | Methods 模型 | Results 槽位 | 兑现状态 | 备注 |
|------|-----------|-------------|------------|---------|------|
| H1 | [IV] (+) → [DV] | Model 2, Table 2 | R3 | pending | 主效应 |
| H2 | [Mediator] (+) → [DV] | Model 3, Table 2 | R3 | pending | 中介路径 |
| H3 | [IV] × [Mod] (+) → [DV] | Model 4, Table 2 | R3 + R4 | pending | 调节效应 |
| 非显著假设 | [IV] (-/ns) → [DV2] | Model 5, Table 3 | R3/R6 | pending | 不得跳过 |

## 兑现状态定义

- `pending` = Results 尚未生成或尚未填入实际系数
- `supported` = 系数方向与预测一致且统计显著
- `not_supported` = 系数不显著或与预测方向相反
- `partially_supported` = 部分条件支持（如调节效应在某些子样本显著）
- `exploratory` = 事后分析，不对应原始假设

## 假设-结果对齐检查点

1. **覆盖完整性**：Theory 中提出的每个假设都必须在 Results 中有对应段落（R3 或 R6）
2. **模型定位**：每个假设必须明确对应到具体的 Table 和 Model，避免"在结果中 somewhere"的模糊定位
3. **因果语言匹配**：Results 中使用的因果/关联语言必须与 Methods 中声明的 design strength 一致（见 SKILL.md 渲染节的因果词汇表）
4. **经济显著性**：每个显著假设的 R3 段落必须包含 Beat-3（幅度解释），使用具体数值基准
5. **非显著假设处理**：非显著假设不得跳过，必须使用 "Contrary to our prediction" / "providing no support" / "direction is consistent but not significant" 等规范句式

## 假设-结果偏离记录格式

```markdown
### 假设-结果偏离记录

| 偏离ID | 假设 | Theory 预测 | Results 实际 | 偏离类型 | 严重程度 | 修正建议 |
|--------|------|-----------|------------|---------|---------|---------|
| R1 | H2 | Mediation via routine updating | 中介效应不显著 | 机制失效 | 高 | 如实标记 unsupported；检查 M5 测量并更新 story resolution |
| R2 | H3 | 正向调节 | 交互项显著但方向为负 | 方向反转 | 高 | 标记 mixed/unsupported；回查 Theory 机制和 Methods 设定 |
```
