<!-- write-methods 槽位骨架 M7补充：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M7 补充：调节效应检验选择（differential prediction vs. differential validity）

**上游接口**：本段承接 `/write-theory` 的假设形式决策矩阵。Theory 部分应已明确每个调节假设是 **differential prediction**（Z 改变 X→Y 的 slope/nature）还是 **differential validity**（Z 改变 X→Y 的 strength/correlation）。Methods 的任务是选择与之匹配的检验。

**检验-方法对应表**：

| Theory 概念类型 | 假设语言信号 | 推荐检验 | 解释对象 | 报告位置 |
|---|---|---|---|---|
| Differential prediction（同层，连续 Z） | "effect... is stronger/weaker/changes" | Moderated multiple regression：Y ~ X + Z + X×Z | 交互项系数（slope 变化） | M7 主模型 |
| Differential prediction（类别 Z） | "X relates to Y for A but not B" | 分组 OLS/FE/Logit，或 MMR 加 X×D_Z | 组间系数差异 | M7 主模型 |
| Differential validity（连续/类别 Z） | "correlation/strength... is greater/lesser" | Subgroup correlation comparison；Fisher z 转换后比较 | 组间相关系数差异 | M7 或 M8 |
| Cross-level differential prediction | "higher-level Z changes lower-level X→Y slope" | HLM / multilevel model with cross-level interaction | 跨层交互项系数 | M7 主模型 |
| Cross-level differential validity | "strength of lower-level X–Y correlation varies by higher-level Z" | Multigroup SEM 或 level-2 分组相关比较 | 跨层相关强度差异 | M7/M8 |

**differential prediction 填空段落**：
```text
Because H[X] predicts that [Z] changes the slope of the [X]→[Y] relationship (differential prediction), we estimate [model: e.g., OLS/FE/Logit] with the interaction term [X × Z]. A significant coefficient on [X × Z] indicates that the effect of [X] on [Y] differs across levels of [Z]. We interpret the interaction using [simple slopes / marginal effects at ±1 SD of Z / predicted values at low and high Z].
```

**differential validity 填空段落**：
```text
Because H[X] predicts that [Z] changes the strength of the [X]–[Y] correlation rather than its slope (differential validity), we follow Andersson, Cuervo-Cazurra, and Nielsen (2014) and split the sample by [Z]. We estimate the [X]–[Y] correlation separately for [group A] and [group B] and compare the coefficients using [Fisher z-test / χ² test for equality of correlations]. A significant difference in correlation strength supports H[X].
```

**跨层调节填空段落**：
```text
Because [Z] operates at the [level-2] level while [X] and [Y] are measured at the [level-1] level, we estimate a hierarchical linear model with a cross-level interaction [level-1 X × level-2 Z]. This specification allows the slope of [X]→[Y] to vary across [level-2 units] and tests whether [Z] explains part of that slope variance.
```

**QC 检查点**：
- [ ] Theory 假设中是否明确是 differential prediction 还是 differential validity？
- [ ] 所选检验是否与假设语言匹配？（slope 语言 → 交互项；strength/correlation 语言 → 分组相关比较）
- [ ] 是否区分了 cross-level direct effect 与 cross-level slope effect？
- [ ] 是否在 M7 中说明交互项/分组比较的解释策略（simple slopes、Fisher z 等）？

**常见反模式**：
- 声称 differential validity 却用 MMR 交互项系数解释；
- 用 subgroup regression 的系数差异代替 correlation 强度差异；
- 跨层调节未在 M7 中声明 focal unit 和 nesting structure；
- 调节假设改变 slope，但 Results 仅报告主效应方向，未解释交互形态。
