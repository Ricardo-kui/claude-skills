# Post-Generation Checklist — 生成后自检清单（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成 Results 段落后**逐条核对**。

## Completeness
- [ ] R1：描述性统计 + 相关性 + 诊断（VIF/multicollinearity）导向
- [ ] R1.5（如适用）：复杂识别设计前是否报告 model-free evidence
- [ ] R2：表格导航解释 Model 1→2→3 的增量逻辑，每假设对应哪一列
- [ ] R3：每假设都有"方向 → 显著性 → 幅度 → 支持判断"四拍
- [ ] R4：交互项系数 + 简单斜率/AME + 图示引用；若显著则**强烈建议**警告主效应不可独立解释（若主效应已不显著可酌情省略）
- [ ] R5：经济显著性（one-SD change / 概率变化 / 基准对比 / cost-per-event）已报告
- [ ] R6：所有非显著/混合/意外发现都被报告（Inline 报告可接受，独立段落非必需），未跳过
- [ ] R7：稳健性按威胁组织（测量/模型/样本/时点/内生性/机制），或按 alternative strategy 组织（长短期/联立方程/外生事件/非线性），非机械列表
- [ ] R8：补充/事后分析与稳健性分开，明确标记为探索性
- [ ] R9（可选）：只做 Results 证据收束，说明 headline answer 与 unresolved questions

## Clarity
- [ ] 变量名与 Methods 完全一致
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号
- [ ] 表格引用指向用户实际表格编号

## Credibility
- [ ] 非显著假设被报告而非跳过
- [ ] 经济显著性与统计显著性同时出现
- [ ] 稳健性检验和补充分析有明确区分
- [ ] 交互效应有图示或简单斜率支持
- [ ] **预处理变异**：至少报告一种预处理稳健性检验（缺失数据/离群值/转换），或说明为何不必要（Yuan et al. 2026）
- [ ] **协变量变异**：若控制变量选择存在理论不确定性，已检验替代控制变量集的稳健性（Yuan et al. 2026）
- [ ] **脆弱性披露**：若任何稳健性检验产生不一致结果，已在正文（而非仅脚注）中如实报告（Yuan et al. 2026）
- [ ] **六维覆盖声明**：R7 开头或汇总表中已明确列出检验的稳健性维度，未检验维度已附排除理由（Yuan et al. 2026）
- [ ] **证据五问**（Booth Ch7）：正文数字与表格/输出逐位一致 / 无 some/most/many/often 类模糊量词替代数字 / 全部假设含非显著已报告（cherry-picking 禁令）/ 数据源与采集链可查 / 每表图有解释句（细则见 `references/evidence-standards.md`）
- [ ] **视觉证据**（Booth Ch13）：表图形式匹配表达效果 / 标题描述数据而非主题、不写含义解读 / 无截断纵轴等失真（伦理四规则，细则见 `references/visual-evidence.md`）

## 论证质量诊断
- [ ] **四拍完整性**：显著假设 方向→显著性→幅度→支持；非显著诚实缩减为2-3拍
- [ ] **稳健性按威胁组织**：每个 threat 一段（"One concern is..."），非按表格罗列
- [ ] **经济显著性嵌入**：1 SD → N unit change / N% / N-day，不只报 β 和 p
- [ ] **非显著诚实**：所有假设可追溯到明确声明，无跳过
- [ ] **因果语言自律**：OLS→"associated with", DiD→"effect of", 实验→"caused"
- [ ] **段落体裁适配**：Results 段落遵循审计体裁约定——假设重述-first / 表格导航-first 为合法段首，支持判断置段尾；通用段落规则（长度、coherence、体裁分型）见 `../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` §0.0/§0.2/§0.5；§0.1 PEEL/§0.3 claim-first/§0.6 Dunleavy 反模式为说服体裁专用，不适用于本 section

## 反向审查（可选但建议）

生成完成后，可使用 `/distill-results-exemplar` 对输出段落进行反向蒸馏审查，生成 Vault 参考注释，供人工判断：
- 槽位覆盖是否完整（R1–R9）
- 四拍节奏是否规范（方向→显著性→幅度→支持）
- 表达骨架是否可迁移（无具体系数/样本量残留）
- 因果语言强度是否与估计器类型匹配
- 稳健性检验是否按 threat 组织而非机械罗列
- 非显著假设是否被报告而非跳过

**注意**：反向审查产出存入 Vault，不自动修改本 skill 的骨架库。是否采纳为 skill 参考由人工决定。
