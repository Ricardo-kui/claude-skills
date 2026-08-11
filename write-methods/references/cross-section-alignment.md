# Cross-Section Alignment — 对齐检查 1/2 与偏离记录（从 SKILL.md 下沉，v0.1）

> 由 write-methods 生成骨架后**执行**。本 skill 的输出必须与上游 Skill 的承诺严格对齐。

## 对齐检查 1：Introduction ↔ Methods（I6 Preview ↔ M7/M8）

| Introduction 承诺（I6 Preview） | Methods 兑现（M7/M8） | 检查问题 | 失败信号 |
|-------------------------------|---------------------|---------|---------|
| "Drawing on... we argue that..." | M7 的 estimator 和 model specification | Theory 承诺的机制是否在模型中被正确设定？ | M7 缺少 mediator 方程或交互项 |
| "Using [data] and [methods]" | M2 数据来源 + M7 估计方法 | 数据和方法是否与 Preview 一致？ | 数据来源或估计方法与 Preview 不符 |
| "We account for [identification concern]" | M8 识别策略 / 效度检验 | Preview 中提到的识别关切是否在 M8 中被处理？ | M8 缺失 Preview 承诺的检验 |

## 对齐检查 2：Theory ↔ Methods（假设列表 ↔ M3-M6 变量操作化）

| Theory 假设 | Methods 变量 | 检查问题 | 失败信号 |
|------------|-------------|---------|---------|
| H1: [IV] → [DV] | M4 自变量 + M3 因变量 | IV 和 DV 的操作化是否与假设中的构念一致？ | 构念名与变量名不一致 |
| H2: [Mediator] 中介 | M5 中介变量 | 中介变量是否被正确测量和纳入模型？ | M5 缺失中介变量或测量方式不符 |
| H3: [Moderator] 调节 | M5 调节变量 + M7/M7补充 检验选择 | 调节变量是否被操作化？检验方法是否与 Theory 的 differential prediction / differential validity 声明一致？ | M7 缺少交互项（prediction）或 M7补充 缺少分组相关比较（validity） |
| 控制逻辑 | M6 控制变量 | 每个控制变量是否对应 Theory 中的竞争性解释？ | M6 出现与 Theory 无关的控制变量 |

## 对齐偏离记录格式

```markdown
### Cross-Section 对齐偏离记录

| 偏离ID | 上游承诺 | 本段实际内容 | 偏离类型 | 严重程度 | 修正建议 |
|--------|---------|------------|---------|---------|---------|
| D1 | I6 Preview: "We use IV to address endogeneity" | M7 使用 OLS/FE，未提及 IV | 识别策略缺失 | 高 | 在 M7 中添加 2SLS 或在 I6 中删除 IV 承诺 |
| D2 | Theory H2: Mediation via routine updating | M5 未包含 routine updating 变量 | 机制变量缺失 | 高 | 补充 M5 中介变量段 |
```
