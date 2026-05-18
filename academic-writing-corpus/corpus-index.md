# Academic Writing Corpus (MVP30-Derived)

> 基于 22 篇顶级管理学期刊论文（ASQ, SMJ, JM, Organization Science, IJRM 等）的叙事拆解而构建的功能句语料库。
> 所有例句均来自已解析论文的改写/模板化处理，仅供句法学习，不直接复制原文。

## 定位

这是一个**按修辞功能分类**的学术写作表达范本库，与 Pollock 系列 `write-*` skills 配合使用：
- `write-introduction`
- `write-theory`
- `write-methods` + `write-results`
- `write-discussion`

**使用方式**：
1. **直接查阅**：按功能类别找到所需表达，参考句法模板和例句。
2. **Skill 内引用**：各 skill 的 SKILL.md 或 references 文件通过相对路径引用本语料库的具体文件。
3. **模板化改写**：所有例句中的具体领域内容已替换为占位符 `[X]`, `[Y]`, `[MECHANISM]` 等，直接套用即可。

## 分类索引

### 1. Hooks（引言开头 hook，20 种）

| # | 文件名 | 功能描述 |
|---|--------|----------|
| 01 | `01-cross-disciplinary-analogy.md` | 跨学科类比 hook（生物学→天文学→社会科学） |
| 02 | `02-extreme-situation.md` | 极端情境/"Imagine..." hook |
| 03 | `03-data-shock.md` | 数据冲击 hook（咨询公司数据 + 巨额数字 + 权威引语） |
| 04 | `04-puzzle-paradox.md` | 谜题/悖论 hook（为什么 A 而同样条件的 B 不...） |
| 05 | `05-literature-consensus-blindspot.md` | 文献共识 + 盲点 hook |
| 06 | `06-paradigm-challenge.md` | 范式挑战 hook（共识说 X，但现实中 Y 持续存在） |
| 07 | `07-headline-news.md` | 头条新闻/当日事件对比 hook |
| 08 | `08-quotation-hook.md` | 权威引语 + 日常类比 hook |
| 09 | `09-evolving-social-issue.md` | 演变中的社会问题 hook |
| 10 | `10-practical-puzzle.md` | 实践难题/从业者困境 hook |
| 11 | `11-current-affairs-debate.md` | 时事/社会辩论 hook |
| 12 | `12-surprising-fact.md` | "Contrary to popular belief" 惊人事实 hook |
| 13 | `13-domain-gap.md` | 领域缺口/"surprising lack of research" hook |
| 14 | `14-cost-benefit-tension.md` | 成本-收益张力 hook |
| 15 | `15-classic-debate-constraint.md` | 经典辩论 + 约束放松 hook |
| 16 | `16-theory-contradiction-empirical-paradox.md` | 理论矛盾 + 经验悖论 hook |
| 17 | `17-phenomenon-market-evolution.md` | 现象驱动市场演变 hook |
| 18 | `18-authority-quotation-dilemma.md` | 权威引语 + 系统性困境 hook |
| 19 | `19-forward-looking-shift.md` | 前瞻性视角转移 hook |
| 20 | `20-counterintuitive-finding.md` | 反直觉发现挑战 hook |

### 2. Tensions（张力构建，10 种）

| # | 文件名 | 功能描述 |
|---|--------|----------|
| 01 | `01-despite-progress-unaddressed.md` | "Despite progress... largely unaddressed" |
| 02 | `02-implicit-assumption-wrong.md` | "The implicit assumption is wrong" |
| 03 | `03-structural-blindspot.md` | "Structural blind spot" |
| 04 | `04-reality-contradicts-consensus.md` | "Reality contradicts consensus" |
| 05 | `05-overlooked-alternative.md` | "Overlooked alternative strategy" |
| 06 | `06-forward-vs-backward-looking.md` | "Forward-looking vs backward-looking" |
| 07 | `07-same-policy-opposite-effects.md` | "Same policy, opposite effects" |
| 08 | `08-cost-vs-benefit.md` | "Cost vs benefit trade-off" |
| 09 | `09-resource-acquisition-vs-utilization.md` | "Resource acquisition vs utilization" |
| 10 | `10-constraint-vs-freedom.md` | "Constraint vs freedom" |

### 3. Stakes（ stakes 构建，6 种）

| # | 文件名 | 功能描述 |
|---|--------|----------|
| 01 | `01-resource-allocation-guidance.md` | 资源配置指导 stakes |
| 02 | `02-quantified-economic-loss.md` | 量化经济损失 stakes |
| 03 | `03-insidious-mechanism.md` | 隐性机制揭示 stakes |
| 04 | `04-public-health-safety.md` | 公共健康/安全 stakes |
| 05 | `05-firm-value-stock-market.md` | 企业价值/股价 stakes |
| 06 | `06-competitive-advantage.md` | 竞争优势/生存 stakes |

### 4. Transitions（过渡句，段落间桥梁）

- `hook-to-literature.md` — Hook 到文献综述的过渡
- `literature-to-gap.md` — 文献综述到 Gap 的过渡
- `gap-to-contribution.md` — Gap 到贡献声明的过渡
- `contribution-to-roadmap.md` — 贡献到文章结构的过渡
- `theory-to-hypothesis.md` — 理论论证到正式假设的过渡
- `results-to-implications.md` — 结果到启示的过渡

### 5. Mechanisms（理论机制表达）

- `dual-path-ability-motivation.md` — 二元路径（能力-动机）机制论证
- `opposing-forces.md` — 对立力量（正向 vs 负向）机制
- `problemistic-search.md` — 问题导向搜索与威胁刚性
- `context-reversal.md` — 情境反转机制
- `inverted-u-mechanism.md` — 倒 U 型机制论证

### 6. Hypotheses（假设推导句法）

- `main-effect.md` — 主效应假设句式
- `moderation-weakening.md` — 负向调节假设句式
- `moderation-strengthening.md` — 正向调节假设句式
- `mediation-chain.md` — 中介链假设句式
- `inverted-u-hypothesis.md` — 倒 U 型假设句式
- `difference-comparison.md` — 差异比较假设句式

### 7. Methods Narrative（方法论叙事）

- `sample-justification.md` — 样本选择的叙事辩护
- `model-selection.md` — 模型选择的比较叙事
- `endogeneity-defense.md` — 内生性处理的论证语法
- `instrumental-variable.md` — 工具变量外生性论证
- `robustness-threat-test.md` — 稳健性检验的"威胁-测试"叙事

### 8. Results Exposition（结果阐述）

- `coefficient-to-substantive.md` — 系数到实质意义的转化
- `interaction-marginal-effects.md` — 交互效应的边际效应叙事
- `economic-significance.md` — 经济显著性计算与表达
- `null-results.md` — 不显著结果的体面表达

### 9. Discussion Moves（讨论段落的修辞动作）

- `reversal-silver-lining.md` — 反转叙事（从负面中提取正面）
- `contribution-statement.md` — 贡献声明的三种句法
- `limitation-boundary-control.md` — 局限性的边界控制
- `future-research-derived.md` — 从实际局限推导未来研究
- `closing-elevation.md` — 结尾升华句法

## 文件格式规范

每个语料库文件统一使用以下结构：

```markdown
# [功能名称]

## 功能定义
一句话说明这个表达在论文中承担什么修辞功能。

## 句法模板
用占位符表示可替换成分的模板句。

## 例句（来自 MVP30）
每个例句标注来源论文类型（改写处理）。

## 使用场景
什么时候用这个表达， outlet 偏好（ASQ vs AMJ/SMJ）。

## 反模式
常见错误用法或应该避免的变体。

## 验证状态
- **跨论文复现**: [✓✓ ROBUST / ✓ VERIFIED / ⚠️ SINGLE-INSTANCE]
- **来源论文**: [Author Year (Journal)] × N
- **生成力**: [✓ GENERATIVE / 待验证 / ✗ NON-GENERATIVE]
- **排他性**: [高 / 中 / 低 / 通用]
- **期刊限制**: [无限制 / 不适用于 ASQ / 仅适用于 SMJ+AMJ]
- **收录状态**: [⭐ PREMIUM / ✓ STANDARD / 🔬 EXPERIMENTAL / 📋 REFERENCE / 📌 BASIC]

## 相关语料
链接到同一论文中配合使用的其他功能句。
```

---

## 质量基础设施

语料库的质量由三个参考文件保障：

| 文件 | 用途 | 何时读取 |
|------|------|---------|
| [`references/verification-standards.md`](references/verification-standards.md) | 三重验证入库标准 + 决策矩阵 + 回溯验证状态表 | 新增/修改 corpus 条目时 |
| [`references/quality-validation.md`](references/quality-validation.md) | 测试论文集 + 回归测试流程 + 季度质量评分卡 | 语料库更新后执行验证时 |
| [`references/honesty-boundaries.md`](references/honesty-boundaries.md) | 覆盖范围声明 + 样本偏差披露 + 使用建议 | 用户首次使用语料库时；生成写作建议时 |

### 当前质量状态

| 指标 | 数值 | 目标 |
|------|------|------|
| 已完成条目 | 42/67（63%） | ≥ 80% |
| 已验证条目 | 0/42（0%） | ≥ 50% |
| 条目收录状态 | 全部 `🔬 EXPERIMENTAL` | 90% 升级至 `✓ STANDARD`+ |

> ⚠️ **重要提醒**：当前语料库所有条目均为 `🔬 EXPERIMENTAL`（单论文观察，未经跨论文验证）。使用时请注意：模板可能过拟合单一论文的叙事结构，需结合具体论文进行判断。详见 [`references/honesty-boundaries.md`](references/honesty-boundaries.md)。

## 更新日志

- **2026-05-16 (Batch 2)**：完成第三阶段语料库空白填补——新增 mechanisms/ (5)、hypotheses/ (6)、methods-narrative/ (5)、results-exposition/ (4)、discussion-moves/ (5)，共 25 个条目，全部基于 MVP30 真实范文文本提取句法模板。已完成条目从 17/67 提升至 42/67 (63%)。
- **2026-05-16**：建立验证基础设施——新增 `references/verification-standards.md`、`references/quality-validation.md`、`references/honesty-boundaries.md`；扩展文件格式规范增加验证状态区块；标注所有现有条目的验证状态。
- **2026-05-15**：搭建语料库骨架，基于已拆解 5 篇论文填充第一批 hooks/tensions/stakes。
