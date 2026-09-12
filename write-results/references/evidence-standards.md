# Evidence Standards（证据五问审计，Booth Ch7）

> 来源：Booth et al. 2024, *The Craft of Research*, Chapter 7 "Assembling Reasons and Evidence"（§7.5）。
> 验证状态：EMERGING——Booth 是通用学术写作书而非管理学语料；五问本身通用，本文件的**定量映射列**为本土化适配。
> 适用位置：write-results 生成后自检（`../SKILL.md` Credibility 区）；Discussion 证据回顾时亦可参考。

## 核心区分：Evidence vs Reasons

Booth §7.2 的关键警告：

> "You don't get to decide whether your evidence is sufficient; your audience does. To count as evidence, a statement must report something they can be expected not to question, at least for the purposes of the argument. But if they do question it, what you think is hard evidence becomes for them only another reason."

定量映射：你的回归系数表只有**在审稿人接受你的测度、样本与识别假设时**才是证据；一旦他们质疑（"这个代理变量真的测了 X 吗？"），表格就降级为另一个需要防守的 reason。这就是为什么 Results 的证据标准不能只盯表格本身，还要管**报告链的可信度**（reports-of-reports：数据→清洗→估计→表格→正文转述，每一环都被你的 ethos 担保——competence + integrity）。

## 五问证据审计表

| # | Booth 标准（§7.5 逐字） | 定量映射（Results 层） | 失败信号 |
|---|------------------------|----------------------|---------|
| 1 | **Accurate** — 报告与证据本身一致（"If someone else were to redo your measurements, would they get the same numbers?"） | 正文转述的系数/p 值/N 与表格、估计输出**逐位一致**；表格与 do 文件输出一致 | 正文 β=0.15 表格 β=0.13；"mistakes in your evidence" 被审稿人读作**整体不可靠**的信号 |
| 2 | **Appropriately precise** — 精确度恰当（"Watch for words like *some, most, many, almost, often, usually, frequently, generally*... they can also fudge it"） | 小数位纪律（系数 2–3 位、SE 同位）；Results 散文中**禁用模糊量词**替代数字（除非量化真不可得的真限制）；报告效应量而非 "substantial" | "many firms" "often significant" "most models show"——Booth 警告这类 hedge 不是承认不确定性而是**掩饰没努力拿到精确数字** |
| 3 | **Sufficient and representative** — 充分且有代表性 | 完整模型序列（baseline→加控制→加交互）；**全部假设含非显著均报告**（联动 `../SKILL.md` 诚实边界 #7）；稳健性检验全维度披露（联动诚实边界 #11） | **Cherry-picking**："A related charge is that of *cherry-picking*, of presenting only those bits of evidence that support a reason and claim... one of the most devastating charges a researcher can face because it implies not just carelessness but dishonesty"——只报显著规格、只报一致的稳健性子集 |
| 4 | **Authoritative** — 来源有权威 | 数据源与采集链可查（数据库版本、样本构建规则、引用权威数据源）；二手数据的 reports-of-reports 链完整 | "data obtained from a proprietary database" 无版本无访问日期；关键测度无既有文献背书 |
| 5 | **Clear and understandable** — 清晰可理解（"if they can't understand how it supports your argument, then you might as well have offered no evidence at all"） | 每个表/图配一句解释句 + 焦点指引（R2 表格导航、R4 图的解读句）；数字不"speak for themselves" | 表格堆砌无导航；系数列出让读者自己找显著性 |

## 可疑证据的正面用法

Booth §7.5.1：

> "You can sometimes use even questionable evidence, *if you acknowledge its dubious quality*. In fact, if you point to evidence that seems to support your claim but then reject it as unreliable, you show yourself to be cautious, self-critical, and thus trustworthy."

定量映射：代理变量有缺陷时，**主动指出并说明为何仍可用**（或用它做稳健性再否定它），比假装它完美更建可信度。与 soundness 层的"承认但不回应"处置同源——见 `../../write-theory/corpus/subprotocols/reasoning_soundness_protocol.md` §4。

## 边界注

- Booth 在 Ch8 补充第六标准 **relevance**——已由 soundness 层 warrant 五测试覆盖（`reasoning_soundness_protocol.md` §2），本文件不重复。
- 精确度的"恰当"水平因领域而异（Booth §7.5.2: "What counts as appropriately precise differs by field"）——管理实证惯例：系数 2–3 位小数、p 值用阈值标记（* / ** / ***）或精确 p（两流派皆可，全表一致即可）。

## 段落论证文法接线（Booth Ch05，`_argument-grammar.md` v1.2）

> 五问审计管**证据内容**，本节管**证据的段落组织**。单一事实源 = `../../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`；本节只写 Results 侧的范围划定与特有拼贴信号。

- **范围划定**：解读型段落（finding claim + 系数/检验证据 + 幅度解释）是论证单元，按文法五问+拼贴自查；表格走读段（数字→表格的导航句群）为程序性报告，体裁豁免——对应 methods 侧的辩护段/程序段之分。
- **角色映射**：finding 句=claim（段首可指认）；系数/检验统计量=证据；幅度解释（经济显著性换算、与既有效应比较）=reason 性质 move。证据不替代 move——"β=−0.12, p<0.01" 本身不构成解读（五问审计 #5：数字不 speak for themselves）。
- **Results 特有拼贴信号**：**数值列队**（相邻句罗列系数、无 because/however 连接——拼贴#5 的 results 形态）；**无主 finding**（系数句不挂任何假设编号或 finding claim——#4/证据孤儿变体）；**稳健性错配**（稳健性检验与所回应的威胁失配——证据孤儿变体，联动 `robustness-diagnosis.md`）。
- **稳健性组织 = 方法世界的制度化 A&R**（Booth Ch09）：每个稳健性检验应能指认它回应的替代解释或效度威胁——results 侧形态是"换度量/换样本/换估计器，结论不变"，且该不变性回应一个**被指认的**威胁，不是无目的的检验堆叠。
