---
type: validator
canonical_id: "intro-post-generation-validator"
source: "Pollock 2025 Ch02-Ch05"
created: 2026-06-01
version: 1.0.0
---

# Introduction 后生成验证器

## 触发条件

在 `write-introduction` 输出完整的 Introduction 骨架后，**必须**运行本验证器。验证不通过时，输出 ⚠️ 警告并给出修复指令；严重失败（❌）时，拒绝输出并要求修复。

---

## 验证 1：Central Knot 存在性（二进制）

**问题**：`central_knot_statement` 是否被成功诊断？

**判断标准**（必须全部满足）：
- [ ] `central_knot_statement` 字段不为 `null`
- [ ] `central_knot_statement` 是一个完整句子（包含主语和谓语）
- [ ] `central_knot_statement` 包含至少一个冲突信号词：**"然而"/"但是"/"尽管"/" paradoxically"/" surprisingly"/" contrary to"**（中文或英文）

**输出**：
- ✅ **PASS**：central knot 已诊断，`central_knot_statement = "[具体句子]"`
- ❌ **FAIL**：central knot 缺失或不合格
  - **修复指令**：返回 Central Knot 诊断步骤，要求用户用一句话回答"你的研究要解开的核心张力/悖论/挑战是什么？"

---

## 验证 2：Central Knot 贯穿性（逐段检查）

**问题**：每个段落是否提及或暗示了 central knot？

**逐段判断**（每段必须满足至少 1 条）：

| 段落 | 提及标准（满足任一即算） | 暗示标准（满足任一即算） |
|------|------------------------|------------------------|
| **P1 Hook** | 直接引用 `central_knot_statement` 的关键词 | 使用 paradox/tension/puzzle 类词汇 |
| **P2 Lit Turn** | 直接引用 `central_knot_statement` 的关键词 | 描述文献的"盲区"/"局限性"/"矛盾" |
| **P3 Gap** | 直接引用 `central_knot_statement` 的关键词 | 使用 "However"/"Yet"/"Although" 引出遗漏 |
| **P4 Stakes** | 直接引用 `central_knot_statement` 的关键词 | 描述"不解决 [knot] 的后果" |
| **P5-P6 Preview** | 直接引用 `central_knot_statement` 的关键词 | 说明"为了检验 [knot]，我们..." |
| **P7-P8 Contribution** | 直接引用 `central_knot_statement` 的关键词 | 承诺"我们解释/解决/挑战 [knot]" |

**关键词提取**：从 `central_knot_statement` 中提取名词短语（去掉动词和虚词）。例如：
- "好公司为什么做坏事" → 关键词 = {"好公司", "坏事"}
- "数字化转型失败的系统模式" → 关键词 = {"数字化转型", "失败", "系统模式"}

**判断算法**：
```
for each paragraph P1-P8:
    keywords = extract_noun_phrases(central_knot_statement)
    if any(keyword in paragraph):
        mark "提及"
    elif any(paradox_word in paragraph) or any(limitation_word in paragraph):
        mark "暗示"
    else:
        mark "MISSING" → ⚠️ 警告
```

**输出**：
- ✅ **PASS**：所有段落至少满足"提及"或"暗示"
- ⚠️ **WARNING**：N 个段落缺失 knot 关联
  - **修复指令**：在缺失段落中添加 `central_knot_statement` 的关键词或 paradox/limitation 类词汇
- ❌ **FAIL**：≥3 个段落完全缺失（无关键词、无 paradox/limitation 词汇）
  - **修复指令**：重写缺失段落，确保每段都与 central knot 相关

---

## 验证 3：叙事阶段顺序（逐段推进检查）

**问题**：段落是否按叙事阶段顺序推进？

**阶段映射表**（来自 `_routing_tables.yaml`）：
| 模块 | 阶段 |
|------|------|
| Hook | Exposition |
| Lit Turn | Early Rising Action |
| Gap | Rising Action |
| Stakes | Rising Action |
| Theory Lens | Rising Action |
| Preview | Late Rising Action |
| Contribution | Denouement Preview |

**阶段顺序规则**：
```
Exposition → Early Rising Action → Rising Action → Late Rising Action → Denouement Preview
```

**阶段倒退检测**（二进制）：
- 段落 i 的阶段编码 ≤ 段落 i-1 的阶段编码 → ❌ **FAIL**
- 阶段编码：Exposition=1, Early Rising Action=2, Rising Action=3, Late Rising Action=4, Denouement Preview=5

**特殊情况处理**：
- 如果模块被跳过（如跳过 Stakes）→ 不检查该模块的阶段，只检查相邻存在的模块
- 如果 Contribution 在 Preview 之前 → ❌ **FAIL**（过早 denouement）

**输出**：
- ✅ **PASS**：阶段单调递增
- ❌ **FAIL**：阶段倒退
  - **修复指令**：
    - 如果是 Exposition → Rising Action 倒退（Lit Turn 功能弱于 Hook）→ 加强 Lit Turn，展示共识局限性
    - 如果是 Rising Action → Denouement Preview 过早 → 调整段落顺序，确保 Preview 在 Contribution 之前

---

## 验证 4：角色定位清晰度

**问题**：主角和配角是否清晰定位？

**检查项**（二进制）：
- [ ] `protagonist_construct` 不为 `null`
- [ ] 主角构念在 Introduction 中出现次数 ≥ 2
- [ ] `supporting_constructs` 列表长度 ≤ 3
- [ ] 配角构念**不出现在** P1 Hook 中（Hook 只出现主角暗示）
- [ ] 群演构念（控制变量）**不出现在**前 3 段中

**判断算法**：
```
protagonist = theory_hints.protagonist_construct
supporting = theory_hints.supporting_constructs

# 检查 1：主角出现次数
protagonist_count = count_occurrences(protagonist, P1-P8)
if protagonist_count < 2 → ❌ FAIL

# 检查 2：配角数量
if len(supporting) > 3 → ⚠️ WARNING

# 检查 3：配角不出现在 Hook
for construct in supporting:
    if construct in P1_Hook → ❌ FAIL

# 检查 4：群演不出现在前 3 段
control_vars = extract_control_variables(P1-P3)
if len(control_vars) > 0 → ⚠️ WARNING
```

**输出**：
- ✅ **PASS**：所有检查项通过
- ⚠️ **WARNING**：配角 >3 个 或 前 3 段有控制变量
  - **修复指令**：将多余配角降级为控制变量，或将控制变量移到 Methods
- ❌ **FAIL**：主角出现 <2 次 或 配角出现在 Hook 中
  - **修复指令**：在 Gap/Stakes 中增加主角出现；将 Hook 中的配角删除

---

## 验证 5：前端一致性（条件检查）

**问题**：Title/Abstract/Introduction 是否一致？

**前提**：如果用户提供 Title 或 Abstract，则进行检查；如果未提供 → 跳过并提示用户补全

**检查项**：
- [ ] Title 包含 `central_knot_statement` 的 ≥1 个关键词
- [ ] Abstract 包含 `central_knot_statement` 的 ≥1 个关键词
- [ ] Title 长度 ≤ 20 个单词（避免堆砌）
- [ ] Abstract 包含：研究问题、理论域、主要发现方向、有趣性暗示

**输出**：
- ✅ **PASS**：所有提供的前端组件一致
- ⚠️ **WARNING**：Title/Abstract 与 Introduction 的关键词不一致
  - **修复指令**：统一术语，确保 Title/Abstract/Introduction 使用相同的核心构念名称
- ❌ **FAIL**：Title/Abstract 与 central knot 完全无关
  - **修复指令**：重写 Title/Abstract，使其与 Introduction 的 central knot 对齐

---

## 验证执行流程

```
Step 1: 运行验证 1（Central Knot 存在性）
    └── ❌ FAIL → 停止输出，返回 Central Knot 诊断
    └── ✅ PASS → 继续

Step 2: 运行验证 2（Central Knot 贯穿性）
    └── ❌ FAIL → 停止输出，给出缺失段落的修复指令
    └── ⚠️ WARNING → 继续输出，但在"提醒"中标注缺失段落
    └── ✅ PASS → 继续

Step 3: 运行验证 3（叙事阶段顺序）
    └── ❌ FAIL → 停止输出，给出段落顺序修复指令
    └── ✅ PASS → 继续

Step 4: 运行验证 4（角色定位）
    └── ❌ FAIL → 停止输出，给出角色修复指令
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注角色问题
    └── ✅ PASS → 继续

Step 5: 运行验证 5（前端一致性，条件性）
    └── ❌ FAIL → 继续输出（不阻止），在"提醒"中强烈建议重写 Title/Abstract
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注不一致
    └── ✅ PASS → 继续

Step 6: 运行验证 6（Prose Craft 层）
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注 prose 问题
    └── ✅ PASS → 继续

Step 7: 运行验证 7（Ch04 病理层）
    └── ⚠️ WARNING → 继续输出，在"提醒"中标注病理问题
    └── ✅ PASS → 继续

Step 8: 汇总输出
    - 输出验证结果表（✅/⚠️/❌）
    - 如果有 ❌ → 输出"修复指令"并要求用户修复后重新生成
    - 如果无 ❌ 但有 ⚠️ → 输出骨架 + 警告 + 修复建议
    - 如果全部 ✅ → 输出骨架 + "叙事层验证通过"
```

---

## 输出格式

```markdown
### 叙事层自动验证结果

| 验证项 | 结果 | 证据 | 修复指令 |
|--------|------|------|---------|
| Central Knot 存在性 | ✅/⚠️/❌ | [具体句子或 null] | [如有] |
| Central Knot 贯穿性 | ✅/⚠️/❌ | P1✓ P2✓ P3✗... | [如有] |
| 叙事阶段顺序 | ✅/⚠️/❌ | [阶段序列] | [如有] |
| 角色定位 | ✅/⚠️/❌ | 主角=[X] 配角=[Y,Z] | [如有] |
| 前端一致性 | ✅/⚠️/❌/N/A | [比较结果] | [如有] |
| Prose Craft 层 | ✅/⚠️ | [Human Face / Showing / Voice 检查结果] | [如有] |
| Ch04 病理层 | ✅/⚠️ | [Fat suit / Burying the lead / Stuffing / Read my mind / Pompous prose] | [如有] |

**结论**：[全部通过 / 有警告 / 需修复]
```

---

## 验证 6：Prose Craft 层（Pollock Ch03）

### 6a: Human Face 检查
- [ ] P1 Hook 包含 >=1 个具体 actor？
- 检测：提取 Hook 段落中的专有名词（大写单词），排除常见虚词（"The", "However", "Although"）
- 如果专有名词数量 = 0 → ⚠️ "Hook 缺少 Human Face"

### 6b: Showing vs Telling 检查
- [ ] `[anomaly / counter-evidence]` 槽位包含具体数字或案例？
- [ ] 无连续 2 句纯抽象描述？
- 检测：扫描相邻句子，如果连续 2 句都包含抽象名词（"understanding", "importance", "role"）且无数字/引语/案例 → ⚠️ "纯告知段落"

### 6c: Conversational Voice 检查
- [ ] 无 "It is argued that" / "It is shown that" / "It is hypothesized that"？
- [ ] 无 "paradigm shift" / "fundamentally transforms"？
- [ ] Contribution 用 "We" 开头？
- 检测：正则匹配禁用词表；检查 Contribution 首句是否以 "We" 开头

---

## 验证 7：Ch04 病理层（Pollock Ch04）

### 7a: Fat suit 检查
- [ ] P1 Hook 词数 ≤ 120？
- [ ] 前 3 段总词数 ≤ 350？
- **检测**：统计 P1 词数；统计 P1+P2+P3 总词数；扫描 P1-P3 中背景信息句（历史、定义、共识描述）vs 问题/张力句的比例
- 如果 P1 > 120 → ⚠️ "P1 可能存在 Fat suit"
- 如果 P1-P3 背景占比 > 60% → ⚠️ "前 3 段铺垫过度，核心问题出现太晚"
- **修复指令**：将 P1 中超出 80 词的背景信息移至 P2 Lit Turn；确保 P1 前 3 句出现核心 paradox/tension

### 7b: Burying the lead 检查
- [ ] 每段段首句在 15 词内说出核心判断？
- [ ] 段首句不是元评论（"本节讨论..." / "接下来..."）？
- **检测**：提取每段段首句，统计词数；检查段首句是否含元评论关键词（"discuss" / "examine" / "接下来" / "本节" / "本文"）
- 如果段首句 > 15 词且无核心判断信号（"argue" / "show" / "find" / "challenge" / "extend"）→ ⚠️ "段首句可能埋没导语"
- 如果段首句含元评论关键词 → ⚠️ "段首句为元评论，核心判断可能被埋没"
- **修复指令**：重写段首句为"主语 + 主动动词 + 方向/发现"；将元评论移至段尾或删除

### 7c: Sentence stuffing 检查
- [ ] 无单句 > 30 词？
- [ ] 无单句含 > 2 个从属连词？
- [ ] 无单段 > 150 词且只有 1-2 句？
- **检测**：按标点（.!?）分割句子，统计每句词数；统计每句中从属连词数量（which/that/because/although/while/whereas）；统计每段句子数
- 如果存在单句 > 30 词 → ⚠️ "存在 Sentence stuffing: [句子前 10 词]..."
- 如果存在单句 > 2 个从属连词 → ⚠️ "句子从句过多，建议拆分"
- 如果存在单段 > 150 词且 ≤2 句 → ⚠️ "段落句子过长，需拆分"
- **修复指令**：将长句拆分为 2-3 短句；将非限制性定语从句独立成句；删除不必要的括号插入语

### 7d: Read my mind 检查
- [ ] 每段与前一段有 explicit transition？
- [ ] 无"显然" / "不难发现" / "as is well known"？
- [ ] 因果推理无跳跃（A→B→C，而非 A→C）？
- **检测**：扫描段落首句是否含 transition 信号词（"However" / "Consequently" / "Thus" / "Therefore" / "In contrast" / "Building on" / "Turning to"）；全文扫描"显然"类表述；扫描假设推导段中因果步骤的完整性
- 如果段落数 ≥3 且段落间 transition 信号词覆盖率 < 50% → ⚠️ "段落间过渡不足，存在 Read my mind 风险"
- 如果全文含"显然"类表述 → ⚠️ "删除'显然'类表述，替换为具体推理"
- **修复指令**：在缺失 transition 的段首添加信号词；补充 why chain 中间步骤；删除所有暗示读者已知的表述

### 7e: Pompous prose 检查
- [ ] 无 unnecessary nominalization（"the transformation of" → "transforms"）？
- [ ] 无过度正式化短语（"in the event that" → "if"）？
- **检测**：扫描常见 nominalization 模式（"the [名词] of" 结构，其中名词可由动词替代：transformation→transform, applicability→applies, realization→realizes）；扫描过度正式化短语（"in the event that" / "due to the fact that" / "for the purpose of" / "with respect to" / "in the context of"）
- 如果 nominalization 出现 ≥3 次 → ⚠️ "存在过多 nominalization，建议改回动词形式"
- 如果过度正式化短语出现 ≥2 次 → ⚠️ "存在过度正式化表达，建议降级"
- **修复指令**：用降级词表替换（见 `prose-craft-checklist.md` 5.5 节降级词表）；将 nominalization 改回动词；Read-aloud test 检测是否像法律文件

---

## 与 write-theory 验证器的接口

本验证器的输出（特别是 `central_knot_statement` 和叙事阶段序列）作为 **输入** 传递给 write-theory 的验证器。write-theory 的验证器将检查：
- Theory P1 是否包含 `central_knot_statement` 的关键词
- Theory 的叙事阶段序列是否从 Knot Inheritance 开始
- 是否存在叙事阶段倒退

接口字段：
```yaml
validation_output:
  central_knot_statement: "[验证后的 knot 句子]"
  protagonist_construct: "[验证后的主角]"
  narrative_stage_sequence:
    - P1: "Exposition"
    - P2: "Early Rising Action"
    - ...
  knot_coverage:
    P1: true
    P2: true
    P3: false  # 如果缺失
    ...
  validation_status: "[pass / warning / fail]"
```
