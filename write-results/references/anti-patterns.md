# Anti-Patterns — Results 常见反模式（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成段落前**先生效**——以下错误在 Results 中高频出现，生成前主动排查。

- **跳过不显著假设**：只报告显著结果，省略 null/mixed findings，造成发表偏误
- **系数即解释**：只报 "β = 0.15, p < 0.05"，不翻译为实质含义；或在线性模型外直接比较系数大小
- **交互显著后仍独立解释主效应**：未提醒用户 "when interaction is significant, main effects cannot be interpreted independently"（强烈建议，但部分顶刊若主效应本身不显著可省略）
- **稳健性机械罗列**：按 "Table 3 用 Tobit, Table 4 换样本" 组织，而非按威胁（内生性/测量/模型/样本）组织
- **经济显著性缺失**：只报统计显著性，不报 one-SD change 对应的幅度或基准对比
- **因果语言越级**：面板数据/OLS 结果用 "caused" "led to"，超出 design strength 许可
- **事后分析未标记为探索性**：把 post hoc 机制检验包装成 confirmatory
- **表格导航缺失**：直接跳入主效应，未解释 Model 1→2→3 的增量逻辑
- **设计排他性混淆**：为非 DiD 设计使用平行趋势语言；为非 IV 设计要求第一阶段/排他性约束检验；为非匹配设计要求重叠支撑检验
- **稳健性包装成因果识别**：把安慰剂检验、模型替换等 robustness check 称为 "causal identification"，超出其回应的 threat 类型
- **batch 同质化**：不同估计器（Logit/Probit/生存分析）使用 OLS 的 ritual 和句式，未按估计器特性调整解释策略（如 Logit 直接比较系数大小）
- **稳健性检验只报告 confirmatory 结果**：当某些稳健性检验结果不一致时，只在脚注中轻描淡写或选择性只报告一致的子集。应在正文和汇总表中同时披露 divergent findings，并框定为边界条件/测量敏感性（Yuan et al. 2026 JOM, Section D）
- **预处理选择不透明**：不在任何地方报告缺失数据处理方式、离群值阈值、变量转换策略，使得读者无法评估预处理选择对结论的影响（Yuan et al. 2026 JOM, REC B3.4）
- **协变量选择无理论辩护**：控制变量的增删仅基于统计显著性而非理论依据，或未在正文/附录中为控制变量集的选择提供 DAG/理论论证（Yuan et al. 2026 JOM, REC B3.3）
