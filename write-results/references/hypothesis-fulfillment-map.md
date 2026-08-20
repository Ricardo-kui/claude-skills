# Hypothesis-Fulfillment Map — 假设-结果承诺兑现框架（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成 Results 骨架前**必建**：本 skill 的核心任务是**兑现 Theory 的假设承诺**。确保每个 Theory 假设都有对应的 Results 段落。

## 映射表

| 假设 | Theory 预测 | Methods 模型 | Results 槽位 | Baseline verdict | Overall evidence | 备注 |
|------|-----------|-------------|------------|------------------|------------------|------|
| H1 | [IV] (+) → [DV] | Model 2, Table 2 | R3 | pending | pending | 主效应 |
| H2 | [Mediator] (+) → [DV] | Model 3, Table 2 | R3 | pending | pending | 中介路径 |
| H3 | [IV] × [Mod] (+) → [DV] | Model 4, Table 2 | R3 + R4 | pending | pending | 调节效应 |
| 非显著假设 | [IV] (-/ns) → [DV2] | Model 5, Table 3 | R3/R6 | pending | pending | 不得跳过 |

## 双层状态定义

`baseline_verdict`：

- `pending` = 尚未填入指定基准结果
- `supported` = 指定基准估计方向与预测一致且达到预设推断标准
- `not_supported` = 基准估计不显著或方向相反
- `partially_supported` = 基准检验只在预设条件/部分路径成立

`overall_evidence`：

- `stable` = 关键选择、内生性、测量和规格检查在方向、显著性与量级上基本一致
- `qualified` = 主模式仍在，但存在明确的样本、测量、时期、估计位置或显著性边界
- `mixed` = 关键检查翻号、失显著或彼此冲突，无法用单一边界概括
- `unresolved` = 证据不足以判断稳定性
- `not_applicable` = 探索性分析，不对应原始假设

## 假设-结果对齐检查点

1. **覆盖完整性**：Theory 中提出的每个假设都必须在 Results 中有对应段落（R3 或 R6）
2. **模型定位**：每个假设必须明确对应到具体的 Table 和 Model，避免"在结果中 somewhere"的模糊定位
3. **因果语言匹配**：Results 中使用的因果/关联语言必须与 Methods 中声明的 design strength 一致（见 SKILL.md 渲染节的因果词汇表）
4. **经济显著性**：每个显著假设的 R3 段落必须包含 Beat-3（幅度解释），使用具体数值基准
5. **非显著假设处理**：非显著假设不得跳过，必须使用 "Contrary to our prediction" / "providing no support" / "direction is consistent but not significant" 等规范句式
6. **稳定性分离**：不得从 baseline `supported` 直接推导 overall `stable`；需要根据关键补充检验填写 `qualified/mixed/unresolved`

## 假设-结果偏离记录格式

```markdown
### 假设-结果偏离记录

| 偏离ID | 假设 | Theory 预测 | Results 实际 | 偏离类型 | 严重程度 | 修正建议 |
|--------|------|-----------|------------|---------|---------|---------|
| R1 | H2 | Mediation via routine updating | 中介效应不显著 | 机制失效 | 高 | 如实标记 unsupported；检查 M5 测量并更新 story resolution |
| R2 | H3 | 正向调节 | 交互项显著但方向为负 | 方向反转 | 高 | 标记 mixed/unsupported；回查 Theory 机制和 Methods 设定 |
```
