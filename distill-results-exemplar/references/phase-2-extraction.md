# Phase 2 — 深度提炼：段落节奏、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

## 2.1 段落节奏提炼（Rhythm Distillation）

Results 不是静态描述，而是**节奏化的证据展演**。提炼每个槽位的节奏模式。

### R3 主假设检验四拍节奏

```text
[拍1-方向]: Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome].
[拍2-显著性]: As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]).
[拍3-幅度]: Substantively, a [one-SD] increase in [predictor] is associated with a [Y-unit] [increase/decrease] in [outcome].
[拍4-判断]: Thus, Hypothesis [x] is supported.
```

提炼任务：
- 该论文是否严格遵循四拍？是否有变体（如拍3嵌入拍2、拍5添加经济显著性）？
- 非线性模型的四拍如何调整（系数→边际效应→概率变化→支持判断）？
- 非显著结果的四拍如何调整（方向→不显著→不解释幅度→不支持）？

### R7 稳健性检验节奏

```text
[威胁定位]: One concern is that our findings depend on [specific threat].
[检验动作]: To address this concern, we re-estimate our models using [method].
[结果]: The results are substantively unchanged.
[结论]: reducing concerns that [threat] drives the findings.
```

提炼任务：
- 稳健性是否按 threat 组织，还是按表格机械罗列？
- 每个稳健性检验是否对应明确的 threat？
- "unchanged" 的表述强度（consistent / qualitatively similar / unchanged）

## 2.2 表达骨架提炼（Expression Skeleton）

**骨架格式**：
```text
[功能标签]: 主假设检验四拍（OLS/FE 版）
[骨架]: Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p < [threshold], 95% CI [[lower], [upper]]). The R² increases from [value] to [value] when [predictor] is added, indicating that [predictor] explains an additional [value]% of the variance in [outcome]. Thus, Hypothesis [x] is supported.
[可迁移性]: 高 — 出现在 15/28 篇范文中
[范式排他性]: OLS/FE 专用，Logit 版本需替换为边际效应
[设计变体]: 
  - DiD: 替换 "Model [y]" 为 "Model [y] provides the baseline DiD estimate"
  - IV: 拆分为第一阶段→第二阶段两段
  - 实验: 替换为 t-test 格式
[节奏标记]: [方向][显著性+系数][幅度解释][支持判断]
[原始句锚点]: "Substantively, a one-standard-deviation increase in [predictor] translates into a [Y-unit] change in [outcome], or roughly [value]% of its standard deviation."（来源论文原句 1–2 句，15–40 tokens，风格参照用）
[skill_gap]: ADD / EXTEND / REPLACE / SKIP
[目标文件]: "OLS-FE.md / 生存分析.md / ..."
[目标槽位]: "R3 / R4 / R7 / ..."
```

**原始句锚点要求**：每个骨架必须附带来源论文中的 1–2 句原文（15–40 tokens），保留原味——骨架抽象负责"节奏可迁移"，锚点负责"语言风味不丢失"。生成时以锚点校准"顶刊味道"，不逐字复制。选句标准：最能代表该变体节奏/措辞手法的句子（如 R3 的幅度翻译句、R7 的 threat 定位句）。

**锚点拼接硬规则（2026-08-09 审计教训）**：多句锚点必须保留省略号标记——**禁止跨段落/跨研究小节无声拼接**（如 Study 1 段与 Study 2 段不得直接并置）；同段删句也必须用 "..." 标注。读者会把锚点当连续引文，无声拼接会误导读者的因果链理解。

**锚点来源检索**（取原句/补锚点时）：优先本次蒸馏论文原文；其次按论文 id/作者/标题检索 Obsidian 知识库：
- `D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\_parsed_texts\mvp30`（MVP30 解析文本，主力库，frontmatter 含 journal/author/year，正文为全文）
- `D:\OneDrive\Obsidian Vault\Clippings`（网页剪藏）
- `D:\OneDrive\Obsidian Vault\文献笔记库\01 导入\论文导入`（OvisOCR 论文导入）
检索不到原文时锚点标记"待补"，不阻塞写入。

**skill_gap 标准**：
- `ADD`：当前 write-results corpus **无**此类骨架 → 新增到目标文件
- `EXTEND`：当前 **有**但本论文提供了额外维度（如新的交互报告节奏）→ 追加为变体
- `REPLACE`：当前旧变体质量不如本论文（如缺少 CI）→ 标记替换
- `SKIP`：与当前 corpus 高度重叠 → 不写入，仅在学习要点中记录
- 每个骨架必须标注 `目标文件`（如 `OLS-FE.md`）和 `目标槽位`（如 R3）

## 2.3 Validity Logic 提炼

提取该 Results 如何处理三类证据可信性问题：

| 可信性问题 | 提炼问题 |
|------------|----------|
| 统计结论效度 | 是否同时报告统计显著性和经济显著性？是否报告置信区间？ |
| 内部效度 | 稳健性检验是否真正回应了 identification threat？还是 placebo 堆砌？ |
| 构造效度 | 测量替代检验的结果是否与主效应一致？ |
