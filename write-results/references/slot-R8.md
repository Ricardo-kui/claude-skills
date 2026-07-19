<!-- write-results 槽位骨架 R8：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R8. 补充 / 事后 / 机制分析

**通用填空段落**：

```text
We conducted supplemental analyses to examine [mechanism/boundary/alternative explanation]. This analysis helps assess whether [interpretation] rather than [alternative] explains the results. The results are [consistent with the proposed mechanism / provide a boundary condition / offer an exploratory extension]. These findings should be interpreted as [confirmatory/exploratory] evidence for [claim].
```

**机制检验专用**： ✓ STANDARD（8-10 篇含机制检验范文复现）
```text
We tested [mediation/moderated mediation] using [method] with [bootstrap samples]. The interaction predicted [mediator], and [mediator] predicted [outcome]. The indirect effect through [mediator] was [status] for [condition] but [status] for [comparison], and the difference between indirect effects was [status]. Because [alternative mechanisms] could also explain the pattern, we included [rival mediators] in the model. The focal mechanism [remained/did not remain] while the alternative mechanisms [did/did not] account for the effect.
```

**替代机制排除专用**（多机制竞争检验）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加竞争机制说明
```text
To examine whether [focal mechanism] rather than [alternative mechanism A] or [alternative mechanism B] explains the [predictor → outcome] relationship, we estimate [model] including [focal mediator], [alternative mediator A], and [alternative mediator B] simultaneously. Column [a] shows that [focal mediator] is [status] while [alternative A] is [status]. Column [b] adds [alternative B]; the coefficient on [focal mediator] [remains stable / attenuates], whereas [alternative B] is [status]. This pattern suggests that [focal mechanism] is the primary channel through which [predictor] affects [outcome], although we cannot rule out [remaining alternative] entirely.
```

**假设验证 / Corroborating Evidence 专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R8 段落
```text
We conducted supplemental analyses to verify [theoretical assumption]. Using [alternative data source / proxy], we examine whether [assumption] holds in our context. The results [support / do not support] the assumption that [theoretical claim]. Because [proxy] is an imperfect measure of [construct], these findings should be interpreted as [supportive / suggestive] rather than definitive evidence.
```

**MCMC / 模拟中介专用**（当使用贝叶斯模拟检验中介时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加模拟说明
```text
We used MCMC simulation with [N, e.g., 20,000] draws to test whether [mediator] mediates the relationship between [predictor] and [outcome]. The results indicate [partial / full / no] mediation for [condition] but [status] for [comparison]. A moderated mediation analysis confirms that the indirect effect is significantly moderated by [moderator]. These findings should be interpreted as [exploratory / suggestive] evidence for the mediating role of [mediator].
```

**辅助方程闭合专用（同时方程）**：
```text
Finally, Table [x], Column [y] reports the results for [auxiliary equation], which we included in Methods to address [reverse-path concern]. The pattern is consistent with the idea that [reverse path] is accounted for, while remaining secondary to the main hypothesis tests.
```
