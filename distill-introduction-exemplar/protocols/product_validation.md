# Phase 6 — 成品验证模式（Product Validation Mode）

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：用户请求验证已写出的 Introduction 成品（--validate）时加载。

---

## Phase 6 — 成品验证模式（Product Validation Mode）

本阶段是 **write-introduction → 用户写作 → distill 成品验证** 闭环的核心。用户在 `/write-introduction` 输出段落骨架并完成写作后，将写出的 Introduction 回传给本 skill 进行验证。

### 调用方式

```
/distill-introduction-exemplar --validate <用户写出的Introduction全文> --reference-metadata <write-introduction输出的段落功能地图> [--output-format=markdown/json]
```

**参数说明**：
- `--validate`（必填）: 标记进入成品验证模式（区别于默认的范文蒸馏模式）
- `<用户写出的Introduction全文>`（必填）: 用户根据 write-introduction 段落骨架写出的 Introduction
- `--reference-metadata`（必填）: write-introduction 输出中的段落功能地图——即每个段落的模块类型分配（如 P1=paradigm-challenge Hook, P2=Non-Coherence Literature Turn, ...）。纯文本格式即可，无需 JSON
- `--output-format`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果没有提供 `--reference-metadata`**：进入简化验证模式，仅执行通用 Introduction QC（不检查与组装方案的对齐）。

### 验证框架：五维检查（v2.1.0 更新）

成品验证从五个维度评估用户写出的 Introduction，与 write-introduction v3.4.0 的三层自检（功能层 / 叙事层 / Prose QC 层）对齐：

```
┌─────────────────────────────────────────────────────────────┐
│  维度1: 组装方案兑现 (Assembly Fidelity) — 功能层            │
│  维度2: 承诺兑现 (Promise Fulfillment) — 功能层              │
│  维度3: 叙事流连续性 (Narrative Flow) — 叙事层               │
│  维度4: 骨架生成力 (Skeleton Generativity) — 功能层          │
│  维度5: Prose Craft QC — Prose 层（v2.1.0 新增）             │
└─────────────────────────────────────────────────────────────┘
```

---

#### 维度1 — 组装方案兑现检查（Assembly Fidelity）

将用户写出的 Introduction 与 `write-introduction` 的段落功能地图逐段对比，检查：

| 检查项 | 问题 | 通过标准 | 失败信号 |
|--------|------|---------|---------|
| **模块覆盖** | 用户是否使用了推荐模块？ | ≥80% 的推荐模块有对应段落 | 多个推荐模块完全缺失 |
| **模块偏离** | 用户是否引入了未推荐的模块？ | 新增模块功能互补，不冲突 | 新增模块与推荐模块互斥 |
| **必须配对** | 必须配对的模块是否成对出现？ | 所有 mandatory 配对 satisfied=true | 如 paradigm-challenge Hook 无 reality-contradicts-consensus Tension |
| **互斥检查** | 是否违反了互斥规则？ | 无 mutual_exclusion_violations | 如 data-shock Hook + quantified-economic-loss Stakes 同现 |
| **段落数偏离** | 实际段落数与推荐布局是否一致？ | ±1 段内为正常 | 偏差 ≥2 段需说明 |

**偏离度矩阵输出格式**：

```markdown
### 组装方案偏离矩阵

| 段落 | 推荐模块 | 实际内容 | 偏离类型 | 偏离度 | 建议 |
|------|---------|---------|---------|--------|------|
| P1 | `06-paradigm-challenge` | 使用了数据冲击开场 | 模块替换 | 高 | Incommensurability 需要高能量 Hook，data-shock 能量不足 |
| P3 | `04-reality-contradicts-consensus` | 未出现现实与共识的矛盾 | 模块缺失 | 高 | 必须配对断裂，需补充反例支撑 |
| P5 | `opposing-forces` (Mechanism) | 使用了对立力量机制预览 | 完全兑现 | 无 | — |
```

---

#### 维度2 — 承诺兑现检查（Promise Fulfillment）

基于 Dorobantu et al. (2024) 的问题链和 Makadok 贡献框架，检查 Introduction 的"承诺"是否可被全文兑现：

| 检查项 | 对应模块 | 验证问题 | 失败后果 |
|--------|---------|---------|---------|
| **Hook→Puzzle 兑现** | Hook | Hook 是否让读者意识到 "这里有问题"？首段末或第二段初是否出现 Puzzle 陈述？ | Hook 沦为装饰，读者不知为何重要 |
| **Gap→Stakes 兑现** | Tension→Stakes | Gap 建立后是否立即解释 "So what?"？ Stakes 是否具体（量化/理论成本/实践后果）？ | 审稿人质疑增量贡献 |
| **Theory→Gap 回应** | Theory Lens→Tension | 理论视角是否直接回应了 Gap 提出的问题？关键词是否有重叠？ | "理论引入与 gap 脱节" |
| **Contribution→Preview 对齐** | Contribution→Preview | 贡献声明中的发现是否被 Preview 暗示？ | 过度承诺或承诺不足 |
| **Makadok 可见性** | Contribution | 贡献声明是否清晰对应 Makadok 八维度之一？ | 贡献模糊，Discussion 无处兑现 |
| **Four Questions** | Preview, Contribution | 四问（What/Why/Show/Move）是否全部回答？ | 读者不清楚论文要做什么 |

**承诺兑现评分**：

```yaml
promise_fulfillment:
  hook_to_puzzle: {score: 3, max: 3, note: "P1末明确出现 puzzle 陈述"}
  gap_to_stakes: {score: 2, max: 3, note: "Stakes 存在但偏 generic（'theoretically important'）"}
  theory_to_gap: {score: 3, max: 3, note: "Drawing on... 直接回应了 tension 的 mechanism gap"}
  contribution_to_preview: {score: 2, max: 3, note: "Preview 暗示了正向关系，但 Contribution 声称的是边界条件"}
  makadok_visibility: {score: 3, max: 3, note: "'We identify... as a key contingency' = Boundary 维度清晰可见"}
  four_questions: {score: 4, max: 4, note: "全部回答"}
  overall_fulfillment_rate: "85%"
```

---

#### 维度3 — 叙事流连续性检查（Narrative Flow）

检查段落间的 Transition 是否自然，叙事能量是否守恒：

| 过渡点 | 检查问题 | 能量守恒规则 |
|--------|---------|-------------|
| Hook → Literature Turn | 从现象到学术对话的过渡是否平滑？ | 高能量 Hook 后需要适度降温 |
| Literature Turn → Tension | 从共识到缺口的转折是否足够锐利？ | 不能渐进式减弱，需要认知断裂 |
| Tension → Stakes | 从缺口到重要性的升级是否令人信服？ | 裂缝必须升级为"危机" |
| Stakes → Theory Lens | 从重要性到新视角的过渡是否自然？ | 读者需要感到 "啊，原来可以这样看" |
| Theory Lens → Preview | 从理论到实证的过渡是否可信？ | 理论承诺必须让读者相信"你能回答" |
| Preview → Contribution | 从发现预告到贡献声明的收束是否有力？ | 贡献是契约，Preview 是证据预告 |

**Transition 链评分**：0-6 分（7 个模块间 6 个过渡点），每个过渡点：
- 2 分 = 有过渡句且功能明确
- 1 分 = 有过渡意图但不够清晰
- 0 分 = 无过渡，段落间跳跃

---

#### 维度4 — 骨架生成力验证（Skeleton Generativity）

这是闭环的**核心增值环节**：验证 `write-introduction` 推荐的骨架在用户实际写作中是否保留了说服动作。

**验证流程**：

1. **骨架匹配**
   - 将用户写出的段落与推荐模块的骨架进行对比
   - 标记骨架中的关键功能短语是否被保留或改写

2. **说服动作保留检查**
   - 原始骨架的说服动作是什么？（兴趣锚定 / 张力制造 / 重要性升级 / 框架引入...）
   - 用户填充后的段落是否完成了相同的说服动作？
   - 如果说服动作丢失或变形，标记为 "骨架失效"

3. **过度填充检查**
   - 用户是否在骨架中塞入了过多领域细节，导致骨架变形？
   - 是否存在 "骨架膨胀"（一个模块的功能被拆分到多个段落，导致叙事稀释）？

4. **Gap 类型 fidelity 检查**
   - 用户填充后的标志性语言是否与原始推荐的 Gap 类型匹配？
   - 例如：推荐 Incommensurability 骨架，用户写成了 "few studies have examined" → 能量降级警告

**生成力验证报告格式**：

```markdown
### 骨架生成力验证

| 段落 | 推荐模块 | 骨架关键短语保留 | 说服动作保留 | 过度填充风险 | 生成力评级 |
|------|---------|----------------|-------------|-------------|-----------|
| P1 | `06-paradigm-challenge` | "Conventional wisdom holds..." ✓ | 共识挑战 ✓ | 低 | VALIDATED |
| P3 | `04-reality-contradicts-consensus` | "Yet [counter-evidence]" ⚠️ 改写为 "some studies found" | 张力减弱（反例→渐进缺口） | 中 | REVISE |
| P5 | `opposing-forces` | "Drawing on... we argue..." ✗ 未出现 | 框架引入 ✗ | 高 | REJECT |
```

---

#### 维度5 — Prose Craft QC（v2.1.0 新增）

验证用户写出的 Introduction 是否符合 write-introduction v3.4.0 的 Prose Craft 标准（Pollock Ch03）：

| 检查项 | 模块 | 通过标准 | 失败信号 | 严重度 |
|--------|------|---------|---------|--------|
| **Human Face** | P1 Hook | >=1 个具体 actor（人名/公司名/机构名） | "many firms" / "some scholars" | 高 |
| **Consensus 有脸** | P1 Hook / P2 Lit Turn | 引用具体论文时用作者名 | "many scholars have argued" | 中 |
| **反例有脸** | P3 Tension | 具体案例或数字，非 "some studies found" | 模糊反例 | 高 |
| **Major construct 首次出现配 illustration** | P3-P6 | 每个核心构念首次出现后跟 1 个例子/数字/场景 | 连续 2+ 句纯抽象 | 中 |
| **Gap statement 配场景** | P3 Tension | 解释遗漏原因后跟 1 个"如果不解决会怎样"的场景 | 只有 "few studies have examined" | 高 |
| **无被动语态** | P3 Gap / P5-P6 Theory Lens / P7-P8 Contribution | 无 "It is argued that" / "It is shown that" | 出现无主语被动 | 高 |
| **Contribution 主动语态** | P7-P8 Contribution | "We extend/refine/reconcile..." | "This study contributes by..." | 中 |
| **无 inflated symbolism** | 全文 | 无 "paradigm shift" / "fundamentally transforms" | 过度包装词汇 | 中 |
| **Fat Suit 控制** | P1-P3 | P1 ≤ 120 词；前 3 段 ≤ 350 词；背景占比 ≤ 60% | P1 > 120 词 | 中 |
| **Burying the Lead** | 全文每段 | 段首句 15 词内说出核心判断；段首句不是元评论 | 段首句为元评论/纯过渡 | 高 |
| **Sentence Stuffing** | 全文 | 单句 ≤ 30 词；单句从属连词 ≤ 2 个；单段 >150 词需 ≥3 句 | 单句 > 30 词或 >2 从句 | 中 |
| **Read my Mind** | 全文 | 每段与前一段有 explicit transition；无"显然"/"不难发现"；因果无跳跃 | A 直接跳到 C 无 B | 高 |
| **Pompous Prose** | 全文 | 无 unnecessary nominalization；无 "utilize""leverage"；不过度正式化 | "the transformation of" / "in the event that" | 低 |

**Prose Craft 偏离矩阵输出格式**：

```markdown
### Prose Craft 偏离矩阵

| 检查项 | 推荐标准 | 实际表现 | 偏离类型 | 严重度 | 建议 |
|--------|---------|---------|---------|--------|------|
| Human Face | P1 >=1 actor | "Many firms fail to..." 无具体公司 | 无人脸 | 高 | 补充 1 个具体公司名或案例 |
| 无被动语态 | P3/P5/P7 无 "It is argued" | P5: "It is argued that CEO overconfidence..." | 机器声 | 高 | 改为 "We argue that CEO overconfidence..." |
| Fat Suit | P1 ≤ 120 词 | P1 = 145 词 | 膨胀 | 中 | 压缩背景，将行业统计移到 Lit Turn |
| Burying the Lead | 段首句 15 词内核心判断 | P3 段首句: "In the context of digital transformation..." (12词无核心判断) | 埋藏 | 高 | 重写为 "Digital transformation's innovation effects depend on organizational routine updating." |
```

---

### 综合验证报告输出

成品验证的最终输出是一份综合报告，供用户决定是否修正、如何修正。

```markdown
# Introduction 成品验证报告

## 基本信息
- **验证模式**: Product Validation（基于 write-introduction 段落功能地图）
- **参考组装方案**: Combo 8（Incommensurability × Mechanism）
- **实际段落数**: 7（推荐 8，偏差 -1）
- **总字数**: 520（推荐 550，偏差 -30）

## 五维评分卡（v2.1.0 更新）

| 维度 | 得分 | 满分 | 评级 | 关键发现 |
|------|------|------|------|---------|
| 组装方案兑现 | 65% | 100% | △ | P1 模块替换（能量降级），P3 必须配对断裂 |
| 承诺兑现 | 85% | 100% | ✓ | Stakes 偏 generic，Contribution-Preview 轻微错位 |
| 叙事流连续性 | 5/6 | 6 | ✓ | Tension→Stakes 过渡较弱 |
| 骨架生成力 | 2 VALIDATED / 1 REVISE / 1 REJECT | — | △ | P5 骨架失效，需重新选择机制预览模块 |
| Prose Craft QC | 8/13 | 13 | △ | P5 被动语态；P1 无人脸；P3 段首句埋藏核心判断 |
| **综合评级** | — | — | **CONDITIONALLY ACCEPT** | 需修正后重新验证 |

## 优先修正清单（按审稿人攻击概率排序）

1. **[高] P3 必须配对断裂**: `06-paradigm-challenge` 未配对 `04-reality-contradicts-consensus`
   - 当前：P3 使用 "some studies found" 渐进式缺口
   - 建议：改用 "A consensus is building that... Yet [counter-evidence]" 高能量张力
   - 若不修正：审稿人质疑 "挑战共识的证据不足"

2. **[高] P5 骨架失效**: 推荐的 `opposing-forces` 机制预览未被使用
   - 当前：P5 只有方法描述，无机制预览
   - 建议：补充 "We argue that X creates performative tension—a misalignment between..."
   - 若不修正：Theory 部分的理论承诺无处锚定

3. **[中] Stakes 具体性不足**: "This is theoretically important" 过于 generic
   - 建议：替换为具体理论成本或量化后果

4. **[低] 段落数偏少**: 实际 7 段 vs 推荐 8 段
   - 建议：检查是否遗漏了独立的 Identification strategy 段

## 验证后动作建议

- **若修正 ≤2 项**：可直接定稿
- **若修正 3-4 项**：建议修正后再次运行 `--validate`
- **若需更换核心模块**（如 P1 Hook 类型或 Gap 类型）：建议重新运行 `/write-introduction` 生成新组装方案

## 验证反馈自动回写（增量累积，无需等待 10+ 次）

> **此节替代旧的"人工汇总"流程。** 每次 `--validate` 运行后，验证结果**立即**回写到 `_evidence_registry.yaml`。不再需要等待 10+ 次验证后人工检查——每次验证都在累积数据，模式随数据增长自动浮现。

### 自动回写步骤

1. **提取验证数据**：从 Phase 6 五维评分卡的骨架生成力验证（维度4）和 Prose Craft QC（维度5）中提取每个模板的 verdict：
   - VALIDATED → 模板在此次使用中生效
   - REVISE → 模板部分生效，有修正建议
   - REJECT → 模板在此次使用中失效

2. **更新注册表**：使用 Read 工具读取 `corpus/_evidence_registry.yaml`，定位到每个被评估模板的 `validation_history` 块，使用 Edit 工具做以下增量更新：
   - `total_runs: N` → `total_runs: N+1`
   - `validated: N` → `validated: N+1`（VALIDATED）/ `revise: N` → `revise: N+1`（REVISE）/ `reject: N` → `reject: N+1`（REJECT）
   - 如果 verdict = REVISE 或 REJECT：在 `common_revise_reasons` 列表中追加新的修正建议字符串
   - **操作方式**：对每个模板，使用 Edit 工具做精确的 `old_string` → `new_string` 替换，只改数字和追加列表项，不动其他内容

3. **模式自动检测**：更新注册表后，检查每个模板的 `common_revise_reasons`：
   - 相同或高度相似的修正建议出现 **≥2 次** → 自动提升为 `common_failures`
   - 相似度判断：两个修正建议的核心动作相同（如都在建议"补充具体 Stakes"）

4. **写入注册表**：将更新后的 `_evidence_registry.yaml` 写回文件

### validation_feedback 硬化输出块

在 Phase 6 验证报告末尾，**必须附加**以下结构化 YAML 块。此块可直接被 `_update_registry.py` 消费：

```yaml
validation_feedback:
  validate_date: "YYYY-MM-DD"
  combo: "[Gap×Contribution 组合]"
  target_journal: "[如有]"

  per_template_results:
    - canonical_id: "06-paradigm-challenge"
      module: "hooks"
      verdict: "VALIDATED / REVISE / REJECT"
      reason: "[简短说明，如：用户改写为 'some studies found'，能量从高降为中]"
      revise_suggestion: "[如 REVISE：建议改用变体 E pontikes2012 双段式，先建立不可辩驳的共识再揭示反常]"

    - canonical_id: "04-reality-contradicts-consensus"
      module: "tensions"
      verdict: "REVISE"
      reason: "用户未包含反例支撑，Tension 退化为渐进式缺口"
      revise_suggestion: "补充 2-3 个跨 context 的反例证据"

    - canonical_id: "01-general-theory-practice"
      module: "stakes"
      verdict: "VALIDATED"
      reason: "Stakes 具体化成功——用户使用了量化经济损失"

  prose_craft_results:
    total_checks: 13
    passed: N
    failed: N
    high_severity_failures:
      - check: "Human Face"
        location: "P1 Hook"
        issue: "无具体 actor"
        suggestion: "补充 1 个具体公司名或案例"
      - check: "无被动语态"
        location: "P5 Theory Lens"
        issue: "It is argued that"
        suggestion: "改为 We argue that"
    fat_suit_index: {p1_words: N, first_three_paragraphs_words: N, background_ratio: "N%"}
    burying_the_lead_score: "[N]% 段首句合格"
    sentence_stuffing_count: N

  overall_validation:
    total_templates_assessed: N
    validated_count: N
    revise_count: N
    reject_count: N
    skeleton_generativity_rate: "[validated/total]"
    prose_craft_pass_rate: "[passed/total_checks]"
```

**validation_feedback 字段说明**：

| 字段 | 用途 | 消费方 |
|------|------|--------|
| `per_template_results[].verdict` | 单次验证中每个模板的生效/失效判定 | 写入 `_evidence_registry.yaml` validation_history |
| `per_template_results[].revise_suggestion` | 具体修正建议文本 | 写入 `validation_history.common_revise_reasons`，≥2 次相似 → 提升为 `common_failures` |
| `overall_validation.skeleton_generativity_rate` | 本次验证的整体骨架生效比例 | 跟踪 write-introduction 模板质量趋势 |

### 增量累积 vs 旧的人工汇总

| | 旧设计 | 新设计 |
|---|--------|--------|
| **触发门槛** | 10+ 次验证后人工检查 | 每次验证自动回写 |
| **数据更新** | 人工读取 Vault 报告 → 手动编辑 YAML | LLM 在 Phase 6 末尾直接读写 `_evidence_registry.yaml` |
| **模式检测** | 人工识别 patterns | 自动检测：≥2 次相同 revise_reason → 提升为 common_failure |
| **适用性** | 需要多用户/大规模数据积累 | 单人单次验证即有反馈——随使用次数增加逐渐精确 |
| **数据安全** | 无风险（不写注册表） | 追加式更新——不删除已有数据，仅累积 |

### Phase 6 的两层定位（更新）

Phase 6 不是单一功能，而是服务于两个时间尺度的需求：

| 层级 | 触发 | 产出 | 数据流向 | 目的 |
|------|------|------|---------|------|
| **即时 QC** | 每次 `--validate` | 五维评分 + 优先修正清单 | 直接给用户 | 写作辅助——发现偏离、承诺未兑现 |
| **增量累积反馈** | 每次 `--validate`（自动） | validation_history 更新 + 模式检测 | `_evidence_registry.yaml` → write-introduction 渲染阶段消费 | 语料库维护——模板的 common_failures 随使用自动增长；≥2 次同因失效即标记 |

**即时 QC 告诉用户"这次哪里写得不对"。增量累积反馈告诉系统"这个模板在真实使用中反复出什么问题"。** 两者在同一次 `--validate` 中完成，不需要额外步骤。当前 `validation_history` 全为 0 只是因为循环从未运行过——此修复使其在每次验证后自动更新。
```

---
