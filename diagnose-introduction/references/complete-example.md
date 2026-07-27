# Complete Introduction Diagnosis Example

Load this reference only when an end-to-end example is needed. Do not preload it
for routine diagnosis.

## Input

```text
/diagnose-introduction
研究描述：研究企业数字化转型如何影响创新绩效。现有文献主要讨论技术采纳的直接效应，但没有解释组织惯例更新这一中介机制。基于组织惯例理论，我们发现数字化转型通过促进组织惯例更新提升创新绩效。
--journal=SMJ
```

## Output

```markdown
## Introduction 诊断报告

### 1. Puzzle 诊断
- Puzzle：为什么相似的数字化投入产生不同的创新结果？
- 广度：合适
- Puzzle-Gap 层次：有层次
- 重要性：需要解释企业数字化转型结果的差异

### 2. 范文匹配
| 排名 | 范文 | 期刊 | 匹配理由 |
|---|---|---|---|
| 1 | Wu 2025 | SMJ | 机制缺口；从直接效应转向过程解释 |
| 2 | Malshe 2015 | JM | 跨文献桥接；多理由缺口论证 |

### 3. Gap / Problematization
- 类型：Incompleteness
- Conversation：Progressive Coherence
- 风险：如果不说明缺失机制造成的理论后果，贡献会显得增量化。

### 4. Makadok 贡献维度
- 维度：Mechanism
- 核心 lever：Why
- 声明骨架：We explain why digital transformation affects innovation by
  identifying organizational routine updating as the intervening mechanism.

### 5. Hook
- 推荐：Cold-start definition 或有来源的 trend data
- SMJ 风格：克制、专业；不使用无证据的戏剧性反例

### 6. Audience & RQ 质量 + JTBD 6-Block 交叉诊断

| Block | 诊断结果 | 具体性/对齐度 |
|-------|---------|--------------|
| 1. Target audience | 技术战略与组织理论学者 | — |
| 2. Progress/challenges | 技术采纳→创新绩效的直接效应语境已建立 | 已建立 |
| 3. Gain/pain | 不识别惯例更新机制，就无法解释数字化转型效果为何不同 | **高** |
| 4. Proposed solution | 组织惯例理论作为解释机制，与 gain/pain 直接对齐 | 对齐 |
| 5. Credibility | 组织惯例理论已交代；实证情境暗示方法可信度 | 已交代 |
| 6. Implications | 贡献回到技术战略与组织理论受众 | 回到受众 |

**Audience 清晰度判断**：高。受众具体（非"管理学学者"泛称）。
**RQ 质量判断**：高。RQ 内含 tension——相似数字化投入产生不同创新结果。
**Gain/Pain 具体性判断**：高。Gap 被表述为"无法解释差异化结果"的理论遗漏，而非 generic "few studies"。
**Claim fit 初步评估**：是。提出的机制与理论视角和实证发现一致，承诺可兑现。

### 7. GBL Four-Move 对齐
| Move | 状态 | 依据 |
|---|---|---|
| Significance | pass | 数字化转型结果差异是重要组织问题 |
| Literature situation | pass | 以 Progressive Coherence 组织技术采纳研究 |
| Problematization | pass | 明确识别机制层面的 Incompleteness |
| Response foreshadow | pass | 惯例更新直接回应机制缺口 |

总体状态：aligned
优先修复：在贡献预告中说明该机制如何改变现有解释。

### 8. 下一步
**直接调用写作 Skill**：
`/write-introduction Incompleteness Mechanism` + 粘贴上述研究描述。

**或查看范文详情**：读取 `references/corpus-patterns.md` 中 Wu 2025、Malshe 2015 条目，了解其 narrative 结构。
```

```yaml
diagnostic_schema_version: 2
gap_type: "Incompleteness"
gap_strength: "低"
conversation_strategy: "Progressive Coherence"
makadok_dimension: "Mechanism"
core_lever: "Why"
exemplar_paper: "Wu 2025"
exemplar_journal: "SMJ"
hook_strategy: "Cold-start definition"
target_journal: "SMJ"
risk: "必须说明缺失机制造成的理论后果"
puzzle: "为什么相似的数字化投入产生不同的创新结果？"
puzzle_broadness: "合适"
puzzle_gap_alignment: "有层次"
audience_clarity: "高"
rq_contains_tension: "是"
rq_quality: "高"
jtbd:
  target_audience: "技术战略与组织理论学者"
  gain_or_pain: "不识别惯例更新，就无法解释数字化转型效果为何不同"
  pain_specificity: "高"
  claim_fit: "是"
gbl_four_moves:
  significance: "pass"
  literature_situation: "pass"
  problematization: "pass"
  response_foreshadow: "pass"
  overall: "aligned"
  repair_priority: "说明该机制如何改变现有解释"
```
