# Post-Generation Checklist — 生成后自检清单（从 SKILL.md 下沉，v0.1）

> 由 write-results 生成 Results 段落后**逐条核对**。

## Completeness
- [ ] Revision-first：若存在当前草稿，已读取正文、修订记录/Decision Register、当前 Methods 与指定表格源；未用旧稿或摘要替代
- [ ] R1：描述性统计 + 相关性 + 诊断（VIF/multicollinearity）导向
- [ ] R1.5（如适用）：复杂识别设计前是否报告 model-free evidence
- [ ] R2：表格导航解释 Model 1→2→3 的增量逻辑，每假设对应哪一列
- [ ] R3：每假设都有"方向 → 显著性 → 幅度 → 支持判断"四拍
- [ ] R4：交互项系数 + 简单斜率/AME + 图示引用；若显著则**强烈建议**警告主效应不可独立解释（若主效应已不显著可酌情省略）
- [ ] R5：经济显著性（one-SD change / 概率变化 / 基准对比 / cost-per-event）已报告
- [ ] R6：所有非显著/混合/意外发现都被报告（Inline 报告可接受，独立段落非必需），未跳过
- [ ] R7：selection 与 endogeneity 分开；内生性按来源组织；其余稳健性按测量/样本/时点/规格等具体问题组织，非机械列表
- [ ] R8：补充/事后分析与稳健性分开，明确标记为探索性
- [ ] R9（可选）：只做 Results 证据收束，说明 headline answer 与 unresolved questions
- [ ] 假设顺序：基准结果按锁定的 H1→H2→H3 顺序报告；理论锚点只影响强调和解释深度
- [ ] 证据阶段：样本选择、内生性、机制/替代解释、异质性和其他稳健性按所解决的问题归位

## Clarity
- [ ] 变量名与 Methods 完全一致
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号
- [ ] 表格引用指向用户实际表格编号
- [ ] 含两个以上分析的章节使用问题导向的小标题；标题不只写工具名
- [ ] 每个补充分析说明问题如何发生、影响哪个推断、该检验为何能诊断，而非只写泛化 concern
- [ ] 每段只有一个证据功能，句间形成 problem→evidence→implication 链，不像逐项日志
- [ ] 用户语言锁全部通过；`model/modeled/modelled/modeling/modelling` 未作动词（除非用户明确允许）
- [ ] 事实直陈：方向、显著性/不确定性、幅度和限制直接呈现；无“诚实披露/为了透明/并不把它表述为”等元报告 wrapper
- [ ] active feedback 中的 voice benchmark 已落实；`supersedes` 指向的旧建议没有因历史记录或 corpus 命中而复活
- [ ] `lint_results_language.py` 已对正文运行并通过；若文件含修订记录，扫描边界没有把历史反例混入正文

## Credibility
- [ ] 非显著假设被报告而非跳过
- [ ] 经济显著性与统计显著性同时出现
- [ ] 稳健性检验和补充分析有明确区分
- [ ] 交互效应有图示或简单斜率支持
- [ ] **预处理变异**：至少报告一种预处理稳健性检验（缺失数据/离群值/转换），或说明为何不必要（Yuan et al. 2026）
- [ ] **协变量变异**：若控制变量选择存在理论不确定性，已检验替代控制变量集的稳健性（Yuan et al. 2026）
- [ ] **脆弱性披露**：若任何稳健性检验产生不一致结果，已在正文（而非仅脚注）中如实报告（Yuan et al. 2026）
- [ ] **双重判断**：每个假设均区分 baseline verdict 与 overall evidence；基准支持不被写成所有检验一致
- [ ] **六维覆盖声明**：R7 开头或汇总表中已明确列出检验的稳健性维度，未检验维度已附排除理由（Yuan et al. 2026）
- [ ] **证据五问**（Booth Ch7）：正文数字与表格/输出逐位一致 / 无 some/most/many/often 类模糊量词替代数字 / 全部假设含非显著已报告（cherry-picking 禁令）/ 数据源与采集链可查 / 每表图有解释句（细则见 `references/evidence-standards.md`）
- [ ] **视觉证据**（Booth Ch13）：表图形式匹配表达效果 / 标题描述数据而非主题、不写含义解读 / 无截断纵轴等失真（伦理四规则，细则见 `references/visual-evidence.md`）

## 论证质量诊断
- [ ] **四拍完整性**：显著假设 方向→显著性→幅度→支持；非显著诚实缩减为2-3拍
- [ ] **稳健性按威胁组织**：每个 threat 一段；`One concern is...` 后已解释具体数据路径、受影响推断、诊断逻辑和残余边界
- [ ] **经济显著性嵌入**：1 SD → N unit change / N% / N-day，不只报 β 和 p
- [ ] **非显著诚实**：所有假设可追溯到明确声明，无跳过
- [ ] **因果语言自律**：OLS→"associated with", DiD→"effect of", 实验→"caused"
- [ ] **段落体裁适配**：Results 段落遵循审计体裁约定——前两句提供假设或问题锚点，句法不机械同构；支持判断只出现一次。通用段落规则（长度、coherence、体裁分型）见 `../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` §0.0/§0.2/§0.5；§0.1 PEEL/§0.3 claim-first/§0.6 Dunleavy 反模式为说服体裁专用，不适用于本 section
- [ ] **反馈回归**：`feedback-registry.json` 中与 skill/project/section/estimator 匹配的 active rules 已逐条通过

## 独立审查（可选但建议）

生成完成后，可使用 `/results-review` 对当前草稿做第二遍独立审查，重点检查：
- 槽位覆盖是否完整（R1–R9）
- 四项证据功能是否完整（方向→不确定性→幅度→基准判断），且未固化成四个同构句
- 问题—检验—证据—结论是否闭合
- 因果语言强度是否与估计器类型匹配
- 稳健性检验是否按 threat 组织而非机械罗列
- 非显著假设是否被报告而非跳过

**注意**：`distill-results-exemplar` 只处理已发表范文和 corpus 维护，不承担当前草稿验证。
