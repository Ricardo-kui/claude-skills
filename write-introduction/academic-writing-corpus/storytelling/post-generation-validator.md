---
type: validator
canonical_id: "intro-post-generation-validator"
source: "Pollock 2025 Ch02-Ch05"
created: 2026-06-01
updated: 2026-08-03
version: 1.1.0
---

# Introduction 后生成验证器

在完整骨架或草稿生成后运行。验证器消费 canonical `story`，按实际功能序列检查，不假定 P1=Hook、P2=Literature Turn、P3=Tension，也不假定全文恰有八段。

## 输入与兼容

优先读取：

```yaml
story:
  central_knot: "..."
  characters:
    main: [...]
    supporting: [...]
  reader_shift:
    from: "..."
    to: "..."
```

只有 `story` 缺失时，才按 `paper-story-contract/references/schema.md` 将旧字段迁移为 provisional canonical block。验证结果只输出 canonical 字段，不写回 `central_knot_statement`、`protagonist_construct`、`supporting_constructs` 或 `narrative_arc`。

## 验证 1：Central Knot 与 P1 张力

### Central Knot

必须满足：

- `story.central_knot` 非空，是一个可理解的关系性张力，而不是 gap 清单；
- 能识别相互冲突的观察、预测、假设、行动目标或结果；
- 不要求机械出现 however/paradox/surprisingly 等信号词。

### P1

P1 前三句必须完成：

1. 给出具体事实、行为者、差异或反直觉现象；
2. 暗示或明示 `story.central_knot`；
3. 说明该现象给目标理论或文献主张制造什么 trouble。

仅写“X 很重要”、宏观趋势或长背景而未形成 theory trouble，判定为 ❌。Human Face 是期刊敏感的质量提示，不以专有名词数量作为二进制门槛。

## 验证 2：开篇前三段功能合同

先读取骨架声明的 `dominant_function`，再检查实际文本。模块合并时，检查功能是否真实完成，不因段号不同而失败。

| 开篇位置 | 主导功能 | 必须可回答的问题 | 允许合并 |
|---|---|---|---|
| P1 | 现象张力 | 哪里不对劲？为什么给理论制造 trouble？ | 可与 Literature Turn 合并 |
| P2 | 学术对话 | 目标受众已知什么、凭什么知道、现有解释会预测什么？ | 可在紧凑型中与 P1 或 P3 合并 |
| P3 | Problematization | 现有解释为何失败？理论后果是什么？本文往哪里回应？ | 可提前到 P2 |

判定：

- ✅ 三项功能均在前三段内完成；
- ⚠️ 功能存在但主导关系不清，或背景句超过前三段的 60%；
- ❌ P1 无张力，或前三段结束仍未出现 diagnostic failure + theoretical consequence。

篇幅阈值是启发式而非跨期刊硬标准：P1 通常不超过约 120 词，前三段通常不超过约 350 词；超限时结合期刊和段落功能判断，不自动失败。

## 验证 3：Literature Conversation 与引文角色

### Conversation 独立性

确认 `conversation_strategy` 是根据文献状态选择，而非由 `gap_type` 自动推出：

- Progressive：一个文献流形成累积推进；
- Synthesized：多个文献流可围绕共同问题重新组织；
- Non-Coherence：存在可核查的冲突命题、预测或证据。

非对角组合合法；只有歪曲文献以迁就 Gap 时才失败。

### 引文角色

逐条标记 citation role：

| 角色 | 句中必须还原 |
|---|---|
| Empirical | 方向、边界、样本或效应 |
| Theory/conceptual | 核心命题、假设或解释逻辑 |
| Review/meta | 共识、异质性或争议状态 |
| Construct | 定义、维度或区分 |
| Context/institution | 可核查事实及理论相关性 |

禁止：

- 范畴断言后堆叠多个无法还原支持内容的引文；
- 将理论、综述或情境来源伪写成方向性实证发现；
- 用被引量代替共识证据；
- 把研究对象不匹配的引文挂到目标命题上。

## 验证 4：叙事阶段与功能推进

阶段编码：

```text
Exposition=1
Early Rising Action=2
Rising Action=3
Late Rising Action=4
Denouement Preview=5
```

按实际段落的主导功能映射阶段：

| 功能 | 阶段 |
|---|---|
| Hook / phenomenon tension | Exposition |
| Literature Turn / early differentiation | Early Rising Action |
| Tension / Stakes / Theory Lens | Rising Action |
| RQ / Preview | Late Rising Action |
| Contribution / reader shift / contribution-embedded differentiation | Denouement Preview |

检测逻辑：

```python
previous = None
for paragraph in actual_paragraphs:
    current = stage_rank(paragraph.dominant_function)
    if previous is not None and current < previous:
        fail("narrative regression")
    if previous == current and not deepens_knot(paragraph):
        warn("same-stage plateau")
    previous = current
```

允许连续多个 Rising Action 段。Contribution 之后不得新增独立 Differentiation、Literature Turn 或 Tension 段；需要区分 closest prior work 时，将其嵌入早期对话或 Contribution。

## 验证 5：角色与 Story 对齐

从 `story.characters.main[*].name` 和 `story.characters.supporting[*].name` 读取角色：

- main characters 必须在开篇和回应预告中保持名称、层次和角色一致；
- supporting character 只有在表达 central knot 必要时才可进入 P1，不机械禁止；
- 控制变量、稳健性变量和方法细节不得占据前三段；
- 新 main character 必须先更新 story contract；新 supporting character 必须解释其功能。

仅凭关键词出现次数不能证明角色清晰；应检查构念是否承担稳定的叙事功能。

## 验证 6：JTBD、Four Moves 与前端一致性

### JTBD 六块

| Block | 检查 |
|---|---|
| Target audience | 是否锁定具体研究流或理论社群？ |
| Progress/challenges | 是否准确建立已知与仍存挑战？ |
| Gain/pain | 不解决问题的理论或实践后果是否具体？ |
| Proposed solution | Theory Lens/RQ 是否直接回应问题？ |
| Credibility | 理论依据、情境和证据能力是否匹配承诺？ |
| Implications | Contribution 是否回到受众并兑现 reader shift？ |

另做 `claim_fit_check`：理论承诺、研究设计、数据能力和因果措辞必须一致。

### Four Moves

检查 Significance、Literature situation、Problematization、Response foreshadow 是否完成；它们是功能，不是固定段数。

### Title/Abstract（条件检查）

用户提供 Title/Abstract 时，检查核心构念、central knot、reader shift 和认识论强度是否一致。未提供时标 N/A，不阻塞输出。

## 验证 7：段落与语言质量

每段只有一个主导修辞功能，但内部仍应包含 Point、Support/Warrant 和 Link。检查：

- 段首或第二句能识别 controlling idea；合法的短 transition-first 句不误判；
- 段末回扣本段功能或自然推进下一段；
- 长句、从句和名词化没有掩盖主张；
- 过渡可由语义承接、关键词链或显式信号实现，不要求每段以 However/Thus 开头；
- Contribution 可用 “We…”, “Our study…” 或明确主语的主动表达，不强制只用 We；
- 因果措辞匹配研究设计。

## 执行顺序与严重度

1. 验证 canonical story 与 P1 tension；失败则停止完整成稿，只返回修复后的前三段骨架。
2. 验证前三段合同和 literature conversation；失败则修复后再进入后半段。
3. 验证叙事阶段、角色、JTBD/Four Moves 和 claim fit。
4. 最后检查段落与语言质量。

严重度：

- ❌：故事或理论承诺错误，必须修复；
- ⚠️：表达、篇幅或期刊适配风险，可带警告输出；
- ✅：功能和证据均对齐。

## 输出格式

```markdown
### Introduction 自动验证结果

| 验证项 | 结果 | 文本证据 | 修复 |
|---|---|---|---|
| Canonical story + P1 tension | ✅/⚠️/❌ | [...] | [...] |
| 前三段功能合同 | ✅/⚠️/❌ | P1=... P2=... P3=... | [...] |
| Conversation + citation roles | ✅/⚠️/❌ | [...] | [...] |
| 叙事阶段推进 | ✅/⚠️/❌ | [实际阶段序列] | [...] |
| 角色对齐 | ✅/⚠️/❌ | [...] | [...] |
| JTBD + Four Moves + claim fit | ✅/⚠️/❌ | [...] | [...] |
| 段落与语言质量 | ✅/⚠️ | [...] | [...] |

**总体状态**：[通过 / 有警告 / 必须修复]
**优先修复**：[只列最高影响的一项]
```

## 下游接口

```yaml
validation_output:
  story_schema_version: 1
  central_knot: "[story.central_knot]"
  main_characters: ["..."]
  supporting_characters: ["..."]
  paragraph_functions:
    - {paragraph: P1, dominant_function: "phenomenon tension", stage: "Exposition"}
    - {paragraph: P2, dominant_function: "literature conversation", stage: "Early Rising Action"}
  knot_coverage:
    P1: true
    P2: true
  validation_status: "pass | warning | fail"
```

`write-theory` 应从 canonical `story` 读取 central knot 与 characters；本接口只传递验证结果，不建立平行 story schema。
