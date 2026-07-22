<!-- write-methods 槽位骨架 M10：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M10. Methods 到 Results 的过渡

**通用填空段落**：

```text
The Results section first reports [main tests] and then examines [validity/robustness checks]. Because [measure/design] raises [concern], we address this issue in supplemental analyses using [test]. The model requires interpreting [marginal effects/predicted values], which we report after the coefficient estimates. We assess the plausibility of [identification assumption] through [event-study/placebo/diagnostic] tests.
```

**六维稳健性预览变体**（v3.0.0 新增 — 基于 Yuan et al. 2026 JOM 六维框架）：

当 Methods 中已记录了替代测量、替代控制变量集或预处理策略时，M10 可增加对其的预览（仅声明存在、不预览结果）：

```text
[Standard M10 content as above.] To assess the robustness of our findings, we report a series of sensitivity analyses in the Results section. These address [measurement concerns] through [alternative operationalizations of key constructs], [covariate sensitivity] through [alternative control-variable specifications], [preprocessing choices] by comparing results across [alternative missing-data/imputation/outlier-treatment approaches], and [statistical specification concerns] through [alternative estimators/model specifications]. When multiple justifiable analytical alternatives exist for a given decision, we compare results across (at least) two feasible alternatives to provide evidence about the stability of the findings (Yuan, Den Hartog, Liu, De Hoogh, Sun, Zhao, Riisla, & Belschak, 2026).
```

> **M10 预览约束**（不变）:
> - 只声明稳健性检验的**存在和类型**，不预览系数、p 值或结论
> - 稳健性检验的完整写作属于 Results R7，不可在 Methods 中提前展开
> - 若某些维度的稳健性检验因不可行而排除，应在 M10 中简要说明（如 "subsampling variation tests were not feasible given the limited sample size per subgroup"）
