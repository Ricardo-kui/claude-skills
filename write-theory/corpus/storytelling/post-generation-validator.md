---
type: validator
canonical_id: "theory-post-generation-validator"
source: "Pollock 2025 Ch02-Ch06"
created: 2026-06-01
version: 1.0.0
---

# Theory 后生成验证器

## 触发条件

在 `write-theory` 输出完整的 Theory & Hypotheses 骨架后，**必须**运行本验证器。验证不通过时，输出 ⚠️ 警告并给出修复指令；严重失败（❌）时，拒绝输出并要求修复。

**前置输入**：`write-introduction` 验证器的输出（`central_knot_statement`、`protagonist_construct`、`narrative_stage_sequence`、`knot_coverage`）。如果上游验证未通过，本验证器优先报告上游问题。

---

## 验证 1：Knot 继承（二进制）

**问题**：Theory P1 是否承接了 Introduction 的 central knot？

**判断标准**（必须满足至少 1 条）：
- [ ] Theory P1 包含 `central_knot_statement` 的 ≥1 个关键词
- [ ] Theory P1 包含明确的 knot 承接信号词："To resolve..."/"Building on..."/"To address..."/"为了解释..."/"为了解决..."
- [ ] Theory P1 的 `protagonist_construct` 与 Introduction 的 `protagonist_construct` 一致

**关键词匹配算法**：
```
keywords = extract_noun_phrases(introduction.central_knot_statement)
P1_text = theory.paragraph_1

match_count = sum(1 for kw in keywords if kw in P1_text)
if match_count >= 1:
    mark "关键词匹配"
elif any(signal in P1_text for signal in ["To resolve", "Building on", "To address", "为了解释", "为了解决"]):
    mark "信号词匹配"
elif theory.protagonist_construct == introduction.protagonist_construct:
    mark "主角一致"
else:
    mark "FAIL"
```

**输出**：
- ✅ **PASS**：Theory P1 继承了 Introduction 的 knot
  - **证据**：`P1 包含关键词 "[关键词]" / 信号词 "[信号词]" / 主角 "[主角]"`
- ❌ **FAIL**：Theory P1 未继承 knot
  - **修复指令**：在 P1 开头添加 `"To resolve the tension that [knot 简化版], we theorize that..."`

---

## 验证 2：叙事阶段完整性（四阶段检查）

**问题**：Theory 是否完整经历了 Knot Inheritance → Deepening → Tying → Fully Tied？

**阶段判定**（每段必须满足至少 1 条标准）：

| 阶段 | 段落位置 | 判定标准（满足任一） |
|------|---------|---------------------|
| **Knot Inheritance** | P1 | 包含 knot 承接信号词 + 主角构念定义 |
| **Knot Deepening** | P2-P4 | 包含构念定义段落 + 文献对话段落 + 理论透镜引入 |
| **Knot Tying** | P5-P(N-1) | 包含假设推导段落（why chain + hypothesis statement） |
| **Knot Fully Tied** | P(N) = T6 Closure | 包含总结信号词（"In sum"/"Together"/"In conclusion"）+ 所有假设的回顾 |

**四阶段完整性检查**：
- [ ] P1 被判定为 Knot Inheritance
- [ ] 存在至少 1 段被判定为 Knot Deepening
- [ ] 存在至少 1 段被判定为 Knot Tying
- [ ] 最后一段被判定为 Knot Fully Tied
- [ ] 阶段顺序：Inheritance → Deepening → Tying → Fully Tied（无倒退）

**阶段倒退检测**：
```
stages = ["Inheritance", "Deepening", "Tying", "Fully Tied"]
for i in range(1, len(stages)):
    if stages[i] < stages[i-1]:
        mark "阶段倒退"
```

**输出**：
- ✅ **PASS**：四阶段完整且顺序正确
- ⚠️ **WARNING**：缺少某个阶段或阶段顺序不完整
  - 缺少 Deepening → 补充构念定义或文献对话段落
  - 缺少 Tying → 补充假设推导段落
  - 缺少 Fully Tied → 添加 T6 Closure 段落
- ❌ **FAIL**：阶段倒退（如 Deepening 后回到 Inheritance）
  - **修复指令**：调整段落顺序，确保阶段单调推进

---

## 验证 3：Plot Emergence（逐假设检查）

**问题**：每个假设是否从构念定义中自然浮现，而非被强加？

**Plot 先于 Story 的检测标准**（满足任一即标记 ⚠️）：
- [ ] 假设推导段落中出现了**未在 P2-P4 构念定义段落中定义的构念**
- [ ] 假设中的构念名称与 P2-P4 的定义中的构念名称不一致（如定义用 X，假设用 X'）
- [ ] 假设推导段落包含"为了解释...""为了得到..."等目的论表述（暗示先确定假设方向再构造理论）
- [ ] 同一个构念在 P2-P4 和 P5-PN 中的定义/scope 不一致

**检测算法**：
```
# 提取 P2-P4 中定义的所有构念
defined_constructs = extract_defined_constructs(P2-P4)

# 检查每个假设推导段落
for paragraph in P5-P(N-1):
    used_constructs = extract_constructs(paragraph)
    undefined = used_constructs - defined_constructs
    if len(undefined) > 0:
        mark "未定义构念: {undefined}"
    
    if any(phrase in paragraph for phrase in ["为了解释", "为了得到", "为了验证"]):
        mark "目的论表述"
    
    for construct in used_constructs:
        if definition_in_P2_P4(construct) != usage_in_paragraph(construct):
            mark "构念定义不一致: {construct}"
```

**输出**：
- ✅ **PASS**：所有假设中的构念均在 P2-P4 中定义，无目的论表述，无定义不一致
- ⚠️ **WARNING**：N 个假设存在 Plot 先于 Story 风险
  - **修复指令**：
    - 未定义构念 → 在 P2-P4 中补充定义，或将该构念降级为控制变量
    - 目的论表述 → 改为因果推理句式（"Because X leads to Y..."）
    - 定义不一致 → 统一构念定义
- ❌ **FAIL**：≥2 个假设严重违背 Plot Emergence（构念未定义 + 目的论 + 定义不一致）
  - **修复指令**：回到 P2-P4 重新梳理构念定义，确保所有假设构念都先定义后推导

---

## 验证 4：Extraneous Storyline（逐段检查）

**问题**：每个段落是否服务于 central knot？

**逐段判断标准**（满足任一即算"服务于 knot"）：
- [ ] 段落包含 `central_knot_statement` 的 ≥1 个关键词
- [ ] 段落包含主角构念（`protagonist_construct`）
- [ ] 段落包含配角构念（`supporting_constructs`）
- [ ] 段落包含 why chain 推理（"Consequently"/"This leads to"/"Thus"）
- [ ] 段落包含假设陈述（"We hypothesize"/"H1:"）
- [ ] 段落包含 T6 总结信号词（"In sum"/"Together"）

**Extraneous 判定**：如果段落不满足以上任何一条 → 标记为 Extraneous

**检测算法**：
```
keywords = extract_noun_phrases(introduction.central_knot_statement)
protagonist = introduction.protagonist_construct
supporting = introduction.supporting_constructs

for i, paragraph in enumerate(theory.paragraphs):
    serves_knot = False
    
    if any(kw in paragraph for kw in keywords):
        serves_knot = True
    elif protagonist in paragraph:
        serves_knot = True
    elif any(s in paragraph for s in supporting):
        serves_knot = True
    elif any(signal in paragraph for signal in ["Consequently", "This leads to", "Thus", "We hypothesize", "In sum", "Together"]):
        serves_knot = True
    
    if not serves_knot:
        mark f"P{i+1} 可能为 Extraneous"
```

**输出**：
- ✅ **PASS**：所有段落服务于 knot
- ⚠️ **WARNING**：N 个段落可能为 Extraneous
  - **修复指令**：
    - 如果段落是文献综述但与 knot 无直接联系 → 压缩或删除
    - 如果段落讨论理论背景但与假设推导无关 → 移至附录或脚注
    - 如果段落是控制变量讨论 → 移至 Methods
- ❌ **FAIL**：≥2 个段落完全与 knot 无关
  - **修复指令**：删除无关段落，或将其中构念降级为控制变量

---

## 验证 5：角色一致性（跨 Section 检查）

**问题**：Theory 中的角色是否与 Introduction 一致？

**检查项**（二进制）：
- [ ] Theory 的核心 DV/IV 与 Introduction 的 `protagonist_construct` 一致
- [ ] Theory 中的调节/中介变量与 Introduction 的 `supporting_constructs` 一致（±1 个容忍）
- [ ] Theory 未引入 Introduction 未提及的新"主角"（核心构念）

**新主角检测**：
```
theory_protagonists = extract_core_constructs(theory)
intro_protagonist = introduction.protagonist_construct

new_protagonists = theory_protagonists - {intro_protagonist}
if len(new_protagonists) > 0:
    mark "新主角未在 Introduction 中预告: {new_protagonists}"
```

**输出**：
- ✅ **PASS**：角色一致
- ⚠️ **WARNING**：新配角 ±1 个容忍范围内
  - **修复指令**：确认新配角是否必要；如必要，在 Introduction Preview 中补充预告
- ❌ **FAIL**：新主角未在 Introduction 中预告
  - **修复指令**：
    - 如果新主角是 knot 的核心 → 回到 Introduction 补充预告
    - 如果新主角不是核心 → 降级为配角或控制变量

---

## 验证执行流程

```
Step 1: 检查上游验证状态
    └── introduction.validation_status == "fail" → ❌ 停止，报告上游问题
    └── introduction.validation_status == "warning" → ⚠️ 继续，标注上游警告
    └── introduction.validation_status == "pass" → ✅ 继续

Step 2: 运行验证 1（Knot 继承）
    └── ❌ FAIL → 停止输出，给出 P1 修复指令
    └── ✅ PASS → 继续

Step 3: 运行验证 2（叙事阶段完整性）
    └── ❌ FAIL → 停止输出，给出阶段修复指令
    └── ⚠️ WARNING → 继续输出，标注阶段问题
    └── ✅ PASS → 继续

Step 4: 运行验证 3（Plot Emergence）
    └── ❌ FAIL → 停止输出，给出假设重构指令
    └── ⚠️ WARNING → 继续输出，标注 Plot 风险
    └── ✅ PASS → 继续

Step 5: 运行验证 4（Extraneous Storyline）
    └── ❌ FAIL → 停止输出，给出段落删除/降级指令
    └── ⚠️ WARNING → 继续输出，标注无关段落
    └── ✅ PASS → 继续

Step 6: 运行验证 5（角色一致性）
    └── ❌ FAIL → 停止输出，给出角色对齐指令
    └── ⚠️ WARNING → 继续输出，标注角色差异
    └── ✅ PASS → 继续

Step 7: 运行验证 6（Prose Craft 层）
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注 prose 问题
    └── ✅ PASS → 继续

Step 8: 运行验证 7（Ch04 病理层）
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注病理问题
    └── ✅ PASS → 继续

Step 9: 汇总输出
    - 输出验证结果表
    - 如果有 ❌ → 输出"修复指令"并要求用户修复后重新生成
    - 如果无 ❌ 但有 ⚠️ → 输出骨架 + 警告 + 修复建议
    - 如果全部 ✅ → 输出骨架 + "Theory 叙事层验证通过"
```

---

## 输出格式

```markdown
### Theory 叙事层自动验证结果

**上游输入**：
- `central_knot_statement`: "[句子]"
- `protagonist_construct`: "[构念]"
- `supporting_constructs`: ["构念1", "构念2"]

| 验证项 | 结果 | 证据 | 修复指令 |
|--------|------|------|---------|
| Knot 继承 | ✅/⚠️/❌ | P1 包含 "[关键词/信号词]" | [如有] |
| 叙事阶段完整性 | ✅/⚠️/❌ | [阶段序列] | [如有] |
| Plot Emergence | ✅/⚠️/❌ | [假设检查详情] | [如有] |
| Extraneous Storyline | ✅/⚠️/❌ | [无关段落列表] | [如有] |
| 角色一致性 | ✅/⚠️/❌ | [角色对比] | [如有] |
| Prose Craft 层 | ✅/⚠️ | [Human Face / Showing / Voice 检查结果] | [如有] |
| Ch04 病理层 | ✅/⚠️ | [Burying the lead / Stuffing / Read my mind 检查结果] | [如有] |

**结论**：[全部通过 / 有警告 / 需修复]
```

---

## 与 Introduction 验证器的接口

本验证器消费 `write-introduction` 验证器的输出：

```yaml
validation_input:
  central_knot_statement: "[Introduction 验证后的 knot]"
  protagonist_construct: "[Introduction 验证后的主角]"
  supporting_constructs: ["[配角1]", "[配角2]"]
  narrative_stage_sequence:
    - P1: "Exposition"
    - P2: "Early Rising Action"
    - ...
  validation_status: "[pass / warning / fail]"
```

如果 `validation_status == "fail"`，本验证器直接输出：
> "上游 Introduction 验证未通过，请先修复 Introduction 的 narrative continuity 问题。"

---

## 跨 Section 联合验证

当 Introduction 和 Theory 都验证通过后，可以运行**跨 Section 联合验证**：

| 联合检查项 | Introduction 状态 | Theory 状态 | 联合结论 |
|-----------|------------------|------------|---------|
| Knot 连续性 | ✅ 已诊断 | ✅ 已继承 | ✅ 连续 |
| 角色连续性 | ✅ 已定位 | ✅ 一致 | ✅ 连续 |
| 叙事阶段连续性 | ✅ Exposition→Denouement Preview | ✅ Inheritance→Fully Tied | ✅ 连续 |
| Plot 自然浮现 | — | ✅ 无强加 | ✅ 自然 |
| Extraneous 检测 | — | ✅ 无无关 | ✅ 紧凑 |

**联合输出**：
```markdown
### 跨 Section 叙事连续性验证

| 检查维度 | Introduction | Theory | 联合结论 |
|---------|-------------|--------|---------|
| Knot 连续性 | ✅ | ✅ | ✅ |
| 角色连续性 | ✅ | ✅ | ✅ |
| 叙事阶段 | ✅ | ✅ | ✅ |
| Plot Emergence | — | ✅ | ✅ |
| Extraneous | — | ✅ | ✅ |

**整体评估**：✅ 叙事层验证全部通过。Introduction 和 Theory 在 narrative continuity 上一致。
```

---

## 验证 6：Prose Craft 层（Pollock Ch03）

### 6a: Human Face 检查
- [ ] P1 包含 >=1 个具体场景或 actor？
- [ ] P2-P4 每个新构念有 >=1 个具体例子？
- 检测：提取各段落中的专有名词；P1 专有名词 = 0 → ⚠️ "Theory P1 缺少 Human Face"

### 6b: Showing vs Telling 检查
- [ ] 无连续 2 句纯抽象推理？
- [ ] 每个假设推导段落有 >=1 个 concrete illustration 或比喻？
- 检测：扫描假设推导段落，标记纯抽象句子（无数字/无案例/无比喻）

### 6c: Conversational Voice 检查
- [ ] 无 "It is argued that" / "It is hypothesized that" / "The literature suggests that"？
- [ ] T6 Closure 以 "We" 开头？
- [ ] 无 inflated symbolism？
- 检测：正则匹配禁用词表

---

## 验证 7：Ch04 病理层（Pollock Ch04）

### 7a: Burying the lead 检查
- [ ] 各假设推导段段首句在 15 词内说出核心判断？
- [ ] 段首句不是元评论（"本节讨论..." / "接下来..."）？
- **检测**：提取各假设推导段段首句，统计词数；检查是否含元评论关键词（"discuss" / "examine" / "接下来" / "本节" / "本文"）；检查是否含核心判断信号词（"argue" / "show" / "hypothesize" / "challenge" / "extend"）
- 如果段首句 > 15 词且无核心判断信号 → ⚠️ "Theory 段首句可能埋没导语"
- 如果段首句含元评论关键词 → ⚠️ "段首句为元评论，需重写为核心判断句"
- **修复指令**：重写段首句为"主语 + 主动动词 + 方向/预测"；元评论移至段尾

### 7b: Sentence stuffing 检查
- [ ] 无单句 > 30 词？
- [ ] 无单句含 > 2 个从属连词？
- [ ] 无单段 > 200 词且只有 1-2 句？
- **检测**：按标点分割句子，统计每句词数；统计每句从属连词数量（which/that/because/although/while/whereas）；统计每段句子数
- 如果存在单句 > 30 词 → ⚠️ "存在 Sentence stuffing: [句子前 10 词]..."
- 如果存在单句 > 2 个从属连词 → ⚠️ "句子从句过多，建议拆分"
- 如果存在单段 > 200 词且 ≤2 句 → ⚠️ "段落句子过长，需拆分"
- **修复指令**：拆分为 2-3 短句；将非限制性定语从句独立成句；删除不必要的括号插入语

### 7c: Read my mind 检查
- [ ] why chain 中每个因果步骤间有 explicit transition？
- [ ] 无"显然" / "不难发现" / "as is well known"？
- [ ] 构念首次出现后用于推理前已有定义？
- **检测**：扫描假设推导段中相邻推理步骤间的 transition 信号词（"Consequently" / "Thus" / "Therefore" / "This leads to" / "As a result" / "Thereby"）；全文扫描"显然"类表述；检查构念定义顺序
- 如果 why chain 中 transition 覆盖率 < 50% → ⚠️ "因果推理缺少过渡，存在 Read my mind 风险"
- 如果全文含"显然"类表述 → ⚠️ "删除'显然'类表述，替换为具体推理"
- 如果假设推导段中出现未在 P2-P4 定义的构念 → ⚠️ "新构念未定义即用于推理"
- **修复指令**：在缺失 transition 的步骤间添加信号词；补充 why chain 中间步骤；删除所有暗示读者已知的表述；确保所有推理用构念先定义后使用
