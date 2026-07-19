# Fine-Grained Profile 输出模板

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 3 结构化报告输出时加载并严格遵循。

---

# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 构建类型: [来自 Phase 0]
- 期刊/领域: [journal]
- Theory 字数: [N]
- 段落数: [N]
- 假设数: [N]
- 与 write-theory 模板对齐度: [高/中/低]

## Rising Action 定位（Pollock Ch02，v1.2.0 新增）

**Central Knot 继承**: [true/false] — "[knot_inheritance_statement]"
**叙事弧线连续性**: [一致/增强/倒退] — 与 Introduction narrative_arc 的对比
**角色一致性**:
- 主角: [protagonist_construct]（Theory 中出现 [N] 次）
- 配角: [supporting_construct1], [supporting_construct2]
- 缺失角色: [如有，列出 Introduction 承诺但 Theory 未定义的构念]
**Plot Emergence**: [自然/有风险] — [extraneous_storyline_risk 或 null]

## Prose Craft Profile（Pollock Ch03，v1.2.0 新增）

**Human Face 策略**:
- P1 场景: "[具体场景句]"
- 构念 illustration: [构念名] → "[例子内容]"
- Why-chain 微型场景: [步骤] → "[场景句]"

**Showing vs Telling 策略**:
- Stroke/Glide 比例: [N:N]
- Illustration 类型分布: [案例/数字/场景/具体研究]
- Showing 断裂点: [如有]

**Conversational Voice 策略**:
- 主动语态频率: [N] 次
- 被动语态位置: [P[段号]: "[原句]"]
- T6 收束句式: "[closure_phrase]"

## 制度冲击特殊适配（v1.2.0 新增，如适用）

**设计类型**: [IV / DiD / RDD / 生存分析 / 无]
**三层论证覆盖**:
- 外生性: [✓/✗] — "[论证句]"
- 机制: [✓/✗] — "[论证句]"
- 识别基础: [✓/✗] — "[论证句]"
**识别策略理论嵌入**: [IV排除限制/DiD平行趋势/RDD可比性/生存时间维度] — [✓/✗]
**Theory-Methods 识别链接**: [无缝/脱节]

## Module Coverage (T1–T6)
[Phase 1.5 输出]

## Distilled Skeletons
### T1 — Construct Definition ([策略])
[来自 Phase 2.2 的骨架列表]

### T2 — Theoretical Lens ([理论])
...

## Argumentation Micro-Moves Map（v1.4.0 新增）

[来自 Phase 2.1.6]

### H1 / P4
- **Anchor**: [起点句]
- **Gap/Puzzle**: [缺口句]
- **Mechanism Move**: [机制步骤]
- **Warrant**: [文献/理论支撑]
- **Prediction**: [假设收敛]
- **缺失动作**: [如有]

### H2 / P5
...

### 双边论证
- **Moderator**: [W]
- **High condition**: [论证句]
- **Low condition**: [论证句]
- **对称性**: [完整/仅单边/缺失]

### 替代解释排除
- **已识别竞争解释**: [list]
- **排除策略**: [theoretical_inconsistency / scope_condition / empirical_counter / mechanism_incommensurable]
- **位置**: [P段号]

## Argument-Evidence Arrangement Pattern（v1.4.0 新增）

[来自 Phase 2.1.7]

- **主要模式**: [Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel]
- **辅助模式**: [如有]
- **证据**: [具体段落位置与句式]
- **功能等价性**: [true/false]

### Concrete Illustration 分布
- **密度**: [每个步骤后 1 句 / 每 2 步 1 句 / 稀疏]
- **类型分布**: [案例 / 数字 / 场景 / 比喻]
- **缺失位置**: [步骤2, 步骤3]

### 复杂假设段落组织
- **Pattern**: [common_trunk → dual_branch / baseline_first → moderation_second / mediation_chain]
- **H1 位置**: [P4]
- **H2 位置**: [P5]
- **假设间关系**: [sequential / parallel / nested]

## Evidence Map（v1.4.0 新增）

[来自 Phase 2.1.8]

### 证据类型分布
- Empirical finding: [N] ([%])
- Theoretical argument: [N] ([%])
- Boundary condition: [N] ([%])
- Negative evidence: [N] ([%])
- Analogical evidence: [N] ([%])

### 证据功能分布
- support: [N]
- qualify: [N]
- contrast: [N]
- pave: [N]
- rebut: [N]

### 文献引用三要素完整率
- 完整: [N/%]
- 缺失 concrete finding: [N/%]
- 缺失 argument summary: [N/%]
- 缺失 link to mechanism: [N/%]

### 代表性三要素例句
- "[Author] (year) found that [concrete finding] — [argument summary]. This suggests that [mechanism step], because [theoretical reason]."

## Theory DNA
[来自 Phase 3 的量化指标，已包含微观动作、双边论证、证据类型/功能、约束对齐等新指标]

## Theory Logic Map
[来自 Phase 2.3]

## write-theory Constraint Alignment（v1.4.0 新增）

| 约束 | 检查项 | 状态 | 说明 |
|------|--------|------|------|
| C10 交互模式 | 调节假设是否明确 enhancing/buffering/antagonistic/existence/competing | ✓/✗/N/A | |
| C14 竞争假设收敛 | 竞争假设是否使用非 "Therefore" 信号 | ✓/✗/N/A | |
| C16 辩证对立对称 | 对立机制步骤数是否对称 | ✓/✗/N/A | |
| C17 真正方向反转 | 是否方向反转而非仅强度变化 | ✓/✗/N/A | |
| C18 Moderator 选择框架 | ≥2 moderators 是否有元框架 | ✓/✗/N/A | |
| C19 连续 IV 三点 | high/middle/low 行为差异是否论证 | ✓/✗/N/A | |
| C20 双边论证 | 调节/边界条件是否同时论证 high/low | ✓/✗/N/A | |

## Dorobantu 问题链覆盖度
| 问题 | 对应模块 | 覆盖度 |
|------|----------|--------|
| WHAT are the key constructs? | T1, T2 | ✓/△/✗ |
| HOW do constructs relate? | T3, T4 | ✓/△/✗ |
| WHY expect these relationships? | T3 | ✓/△/✗ |
| WHAT theoretical lens? | T2 | ✓/△/✗ |
| Are findings consistent? (理论内部) | T3, T5 | ✓/△/✗ |
| What is missing? (理论边界) | T5, T6 | ✓/△/✗ |

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新 why-chain 模式: ...
- 新构念关系组织方式: ...

## Narrative Style Profile
[来自 Phase 3 的多维度风格解剖]

**Tone**: [主语气]（证据："..."）
**Paragraph Rhythm**: [段落内部节奏模板]
**Module Ratio**: T1 [N%] / T2 [N%] / T3 [N%] / T4 [N%] / T5 [N%] / T6 [N%]
**Distinctive Features**:
- [特征1]: [原文例句]
- [特征2]: [原文例句]
**Avoids**:
- [回避写法1]: [功能解释]
- [回避写法2]: [功能解释]
**Quality Markers**:
- what_makes_effective: [为什么这个理论论证结构有效]
- strongest_aspect: [最值得模仿的1-2个技巧]
- weakest_aspect: [已知风险/审稿人可能攻击的理论薄弱点]

**Prose Craft 子维度**（v1.2.0 新增）:
- **Human Face 策略**: [actor 类型分布 + 代表性例句]
- **Showing 策略**: [illustration 类型分布 + 代表性例句]
- **Voice 策略**: [主动句式模板 + 被动语态位置]
- **Stroke/Glide 控制**: [比例 + 风险段落标记]

## Non-Transferable Facts
[仅适用于该论文的特定构念、理论视角、机制内容，不可迁移]

## Corpus Recommendations（v1.4.0 新增）

基于本篇论文的提取结果，按 Corpus Taxonomy 分类给出沉淀建议。

```yaml
corpus_recommendations:
  ready_for_corpus:
    - pattern_id: "[唯一标识，如 parallel_three_mechanisms]"
      pattern_name: "[人类可读名称]"
      source_paper: "[作者_年份_期刊]"
      corpus_path: "corpus/subprotocols/arrangement_patterns.md"
      section: "[建议写入的章节]"
      build_type: "[适用构建类型]"
      confidence: "high / medium / low"
      cross_paper_evidence: "[已验证的范文数 / 需要再积累的范文数]"
      rationale: "[为什么这个模式值得沉淀]"
      entry_preview: |
        ### [Pattern Name]
        [可直接写入 corpus 的 markdown 条目预览]
  needs_validation:
    - pattern_id: "[唯一标识]"
      pattern_name: "[名称]"
      source_paper: "[作者_年份_期刊]"
      corpus_path: "[目标路径]"
      note: "[为什么还需要验证 / 需要找什么类型的论文验证]"
  anti_patterns:
    - pattern_id: "[唯一标识]"
      pattern_name: "[名称]"
      source_paper: "[作者_年份_期刊]"
      reason: "[为什么不建议沉淀到 write-theory]"
      alternative: "[如果要实现类似功能，建议用什么替代]"
```

**记录原则**：
- 单篇论文出现的新颖模式 → 优先放入 `needs_validation`
- 与 write-theory 当前 Constraints 冲突的做法 → 放入 `anti_patterns`
- 过于论文特异的机制内容 → 不进入任何 corpus，只在 Non-Transferable Facts 记录

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-theory skill]
```

---
