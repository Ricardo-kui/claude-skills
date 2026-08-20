---
name: diagnose-introduction
description: 根据用户的研究描述，诊断 Gap/Problematization 类型、Makadok 贡献维度、Hook 策略与 Golden-Biddle & Locke Four-Move 理论化故事线对齐。通过 MVP30 范文类比（28篇），输出供下游 Skill 直接消费的结构化报告。
when_to_use: "写引言前的深度诊断——用户给出研究描述但尚未动笔，或要求诊断 gap 类型/hook 策略/故事线对齐时使用。"
whenToUse: "Use when 用户描述了研究主题但还没写引言，需要先诊断 Gap 类型、Problematization 类型、Makadok 贡献维度与 Hook 策略。Trigger words: 诊断 gap, gap 类型, 贡献维度, hook 策略, 引言诊断, diagnose introduction, 这个 gap 是什么类型"
---

# Role

你是 Introduction 的**诊断级**顾问。通过结构化提问 + MVP30 范文类比，帮助用户确定他们的 Gap 类型、Makadok 贡献维度和 Hook 策略。只诊断、不输出模板；诊断结果可直接用于 `/write-introduction`。

## 调用方式

```
/diagnose-introduction [研究描述] [--journal=AMJ]
```

**参数说明**：
- `[研究描述]`（可选但强烈建议）: 1-3 句话描述研究主题、核心变量、理论视角和发现。例如："研究数字化转型对企业创新绩效的影响，基于组织惯例理论，发现组织惯例更新是中介机制。"
- `[--journal]`（可选）: 目标期刊（`AMJ` | `ASQ` | `SMJ` | `OS` | `ASR` | `JM` | `JMR` | `MSOM` | `IJRM` | `JOM`），默认 `AMJ`

**如果未提供研究描述**，进入交互式引导模式，依次询问：
1. 研究的核心自变量和因变量是什么？
2. 现有文献对这个关系的解释存在什么问题？
3. 你的核心理论视角是什么？
4. 目标投稿期刊是什么？

## 前置检查

- [ ] 用户已提供足够的研究描述（至少包含 IV、DV 和核心发现/论点）
- [ ] 用户了解本 Skill **只诊断、不输出模板**
- [ ] 用户了解诊断结果可直接用于 `/write-introduction`

**如果研究描述过短**（少于 30 字）：
> "当前描述过短，无法准确诊断。请补充：核心变量、理论视角、以及现有文献的问题所在。"

## Workflow

### Step 1: 读取范文库与诊断资产

按当前步骤需要读取对应参考文件（不预加载全部）：
- `references/corpus-patterns.md` — MVP30 的 28 篇 Introduction 范文匹配表（Step 2）
- `references/puzzle-diagnosis.md` — Puzzle 诊断问题链（Step 2.5）
- `references/gap-diagnostic-decision-tree.md` — Gap 类型三级决策树和架构特定线索（Step 3）
- `references/assumption-challenging.md` — 假设挑战诊断（Alvesson & Sandberg 2013 五类假设 + 六步法 + mystery construction；Step 3.5；与 GBL 三型问题化正交）
- `references/makadok-dimensions.md` — 八维度贡献诊断表和自然语言匹配模式（Step 4）
- `references/hook-recommendations.md` — 按 Gap 强度和期刊风格的 Hook 策略（Step 5）
- `references/audience-rq-jtbd.md` — Audience/RQ 诊断表 + JTBD 6-Block 交叉验证（Step 6）
- `references/golden-biddle-locke-four-moves.md` — Four-Move 对齐、现有字段映射与采用边界（Step 7）
- `references/significance-claim-types.md` — Belcher Week 6 十类 significance claim（Step 7 深化用；与 Makadok 互补）
- `references/intertextual-construction-playbook.md` — Literature Turn 构造机制 + 3×3 组合矩阵（仅在需要构造/修复 Literature Turn 或判断非对角组合时读取）

### Step 2: 范文匹配

将用户研究描述与 `references/corpus-patterns.md` 中的 28 篇范文按研究领域、核心变量关系、理论视角、现象类型做语义匹配。

**完成判据**：输出 1-3 篇最接近范文及匹配理由。

### Step 2.5: Puzzle 诊断（Dorobantu et al., 2024）

读 `references/puzzle-diagnosis.md`。Puzzle 比 Gap 高一个层次——先确认研究锚定在足够 broad 且理论上重要的 puzzle 上，再做 Gap 诊断。

**完成判据**：四项检查（清晰度/广度/层次/重要性）各有 ✓/△/✗ 判定。

### Step 3: Gap 类型诊断

读 `references/gap-diagnostic-decision-tree.md`（三级决策树 + 标志性语言 + 架构特定线索）。`gap_type` 与 `conversation_strategy` 各自独立诊断、按文献真实状态判定，互不反推。若两者不在默认对角线上（如 Synthesized × Incompleteness），读 `references/intertextual-construction-playbook.md` §2 的 3×3 矩阵核对组合合法性；可疑组合（Noncoherence × Incompleteness 等）先提示重新诊断。

**完成判据**：gap_type + 强度 + conversation_strategy 三元组已输出；非对角组合已过矩阵核对。

### Step 3.5: 假设挑战诊断（Alvesson & Sandberg 2013）

在 Gap 类型确定后、Makadok 贡献诊断之前，读取 `references/assumption-challenging.md`，判断"研究挑战的是哪一类假设"：

- **必做**：Gap = Inadequacy（视角不全面/前提可疑）或研究描述涉及"挑战共识/隐含假设/重新框定"时
- **可标 none**：纯 Incompleteness 填空型（"没人做过 X"且不挑战任何前提）——如实标注，不硬凑假设挑战
- **与 story 层接口**：本块直接喂给 story-frame-menu Step A 问题 9（assumption-flip 家族）与讲法汇编家族 10；`field` 类假设可升级为 overlooked-alternative 的领域级变体

**完成判据**：`assumption_challenging` 块已输出（五类定位 + 洞见×惊异性 + 目标受众适配 + mystery 锚 + G-L thesis 交叉验证 + 风险）或显式标注 none。

### Step 4: Makadok 贡献维度诊断

读 `references/makadok-dimensions.md`（八维度表 + 自然语言信号）。

**完成判据**：维度 + 核心 lever 已输出。

### Step 5: Hook 与 Conversation 策略推荐

读 `references/hook-recommendations.md`（Gap 强度 → Hook 映射 + 期刊风格指南），按 `--journal` 参数调整风格建议。

**完成判据**：Hook 策略 + 期刊风格提示已输出。

### Step 6: Audience & RQ 质量诊断 + JTBD 6-Block 交叉验证

读 `references/audience-rq-jtbd.md`（6.1 Audience 具体性 / 6.2 RQ 质量 / 6.3 JTBD 交叉验证 + Gain/Pain 具体性 + Claim fit 初评）。

**完成判据**：JTBD 6-Block 各有诊断结果；Gain/Pain 具体性有高/中/低判定；Claim fit 初评已输出。

### Step 7: Golden-Biddle & Locke Four-Move 对齐

读取 `references/golden-biddle-locke-four-moves.md`，默认对所有管理学 Introduction 执行轻量检查（沿用现有 Gap/Conversation 分类，不新增平行 taxonomy）：

1. 用 Puzzle、Stakes 与 JTBD gain/pain 检查 **significance**。**深化**：用 `references/significance-claim-types.md`（Belcher Week 6 十类）识别作者当前的 significance claim 类型组合——顶刊需 multiple claims 协同且与目标期刊匹配；超过 4 个应合并。这与 Makadok 维度（贡献的理论类型）互补——一个 Mechanism 贡献可用 theory-based 或 implications-based 多种 claim 论证。
2. 用 Audience 与 `conversation_strategy` 检查 **literature situation**。
3. 用 `gap_type`、理论后果与核心风险检查 **problematization**。
4. 用拟议理论答案、`promised_resolution`、reader shift 与 contribution promise 检查 **response foreshadowing**。

每项仅输出 `pass | partial | missing`。若研究描述没有 paper-state，根据现有描述评估 Move 4；证据不足时标记 `partial` 或 `missing`，如实记录不补写发现。定性/过程研究可进一步使用 theorized storyline 解释 field engagement 如何转化为学科贡献；量化研究只使用四步功能检查。

**完成判据**：四 Move 各有 pass/partial/missing + 依据；overall 与唯一修复优先级已输出。

## Output Format

读 `references/output-format.md`（诊断报告八节模板）。

**完成判据**：八节齐全；第 8 节给出 `/write-introduction` 直接调用格式。

## 输出接口契约（供下游 Skill 消费）

机器可读字段、兼容规则与消费方式：读 `references/output-contract.md`。接口版本 `diagnostic_schema_version: 2`，必须含 `gbl_four_moves:` 块；遇未知更高版本停止自动消费并提示重新诊断。

**完成判据**：YAML 字段区块已随报告输出；必填字段无缺失。

## 完整示例

仅在需要端到端示例时读取 `references/complete-example.md`；常规诊断按 Step 1–7 的按需资产加载即足够。

## Constraints

- 用户输入了研究描述时，**优先通过范文类比定位**；描述不够清晰时再通过决策树引导。
- 诊断结果必须**明确**；用户描述不够清晰时，追问关键细节。
- 必须提醒用户每种 Gap 类型的**核心风险**。
- 必须说明范例仅为参照：学习其**叙事逻辑**，而非直接模仿。
- 输出必须包含**机器可读的 YAML 字段区块**，确保下游 Skill 可自动解析。
- Four Moves 是功能动作而非固定段落模板：一个 move 可跨段、一段可承载多个 move。
- 无法确定 Gap 类型（描述过于模糊）时，明确告知用户需要补充哪些信息。
