# Corpus Taxonomy for write-theory（v1.4.0）

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 4 沉淀建议映射到 write-theory corpus 结构时加载。

---

## Corpus Taxonomy for write-theory（v1.4.0 新增）

本 skill 的终极目的不是产出报告，而是把验证过的模式沉淀到 `write-theory` 的语料库中。为避免沉淀时混乱，所有提取产物必须按以下 taxonomy 分类存放。

### 分类原则

1. **按功能粒度分层**：
   - `variants/`：整篇 Theory 的宏观结构（按构建类型）
   - `subprotocols/`：中观论证策略/模式（跨构建类型可复用）
   - `sentences/`：微观句式模板（填充式表达单元）

2. **按构建类型分桶**：
   - 同一模式若只在某构建类型中出现 → 写入该构建类型的 variant
   - 同一模式跨多个构建类型出现 → 写入 `subprotocols/` 并标注 `[跨类型]`

3. **按证据强度准入**：
   - 单篇论文出现 → 只入 Vault 参考注释
   - 2 篇同类型论文出现 → `subprotocols/` 作为可选变体
   - ≥3 篇跨期刊论文出现 → 可进入 `variants/` 或 `SKILL.md` 默认规则

### Taxonomy 映射表

| 提取产物 | 沉淀位置 | 文件名/路径 | 准入门槛 |
|---------|---------|------------|---------|
| 构建类型整体结构（T1–T6 模块序列、比例、节奏） | `corpus/variants/` | `A_construct_differentiation.md`<br>`B_mechanism_elaboration.md`<br>`C_hypothesis_tree.md`<br>`D_process_theory.md`<br>`E_moderation.md`<br>`F_competing_hypotheses.md`<br>`G_dialectical_opposition.md` | ≥2 篇该构建类型论文一致 |
| 假设论证微观动作（Anchor/Gap/Mechanism/Warrant/Prediction） | `corpus/subprotocols/` | `argumentation_patterns.md` | ≥2 篇论文出现同类动作序列 |
| **假设推导段落级模板（完整 Anchor→Mechanism→Warrant→Prediction）** | `corpus/subprotocols/` | `hypothesis_derivation_patterns.md` | ≥2 篇论文出现同类段落结构 |
| 论点-论据安排模式（Warrant-Embedded / Evidence-Contrast / Cumulative / Parallel） | `corpus/subprotocols/` | `arrangement_patterns.md` | ≥2 篇论文使用同模式 |
| 复杂假设段落组织（common trunk / dual branch / baseline→moderation） | `corpus/subprotocols/` | `hypothesis_organization_patterns.md` | ≥2 篇复杂假设论文一致 |
| 证据类型、证据功能、文献三要素句式 | `corpus/subprotocols/` | `evidence_patterns.md` | ≥2 篇论文出现同类证据策略 |
| 双边论证 high/low 句法 | `corpus/subprotocols/` | `bilateral_argumentation_templates.md` | ≥2 篇调节效应型论文一致 |
| Moderator 选择元框架 | `corpus/subprotocols/` | `moderator_selection_frameworks.md` | ≥2 篇多 moderator 论文一致 |
| Closure 策略（局部收束 / 嵌入框架总结 / Discussion 回补） | `corpus/subprotocols/` | `closure_strategies.md` | ≥3 篇管理学顶刊论文一致 |
| 识别策略理论嵌入（IV/DiD/RDD/生存分析） | `corpus/subprotocols/` | `identification_strategy_in_theory.md` | ≥2 篇制度冲击类论文一致 |
| 构念定义句式 | `corpus/sentences/` | `construct_definition.md` | ≥3 篇论文使用同类句式 |
| 理论视角引入句式 | `corpus/sentences/` | `theoretical_lens.md` | ≥3 篇论文使用同类句式 |
| 机制推演句式 | `corpus/sentences/` | `mechanism_chain.md` | ≥3 篇论文使用同类句式 |
| 调节假设句式 | `corpus/sentences/` | `moderation.md` | ≥3 篇论文使用同类句式 |
| 假设形式句式 | `corpus/sentences/` | `hypothesis_forms.md` | ≥3 篇论文使用同类句式 |
| 收束/过渡连接词句式 | `corpus/sentences/` | `closure.md`<br>`connectors.md` | ≥3 篇论文使用同类连接词 |

### 单篇蒸馏时的快速分类决策

对每个提取出的骨架/模式，按以下问题链决定去向：

```text
Q1: 该模式是否只适用于特定构建类型？
    ├── 是 → 进入 corpus/variants/[build_type].md
    └── 否 → Q2

Q2: 该模式是否涉及具体措辞/句法结构？
    ├── 是 → 进入 corpus/sentences/[function].md
    └── 否 → Q3

Q3: 该模式是否跨构建类型可复用？
    ├── 是 → 进入 corpus/subprotocols/[pattern_type].md
    └── 否/不确定 → 只入 Vault 参考注释
```

### Corpus Entry 标准格式

每个写入 corpus 的条目必须包含以下字段：

```markdown
<!-- 
pattern_id: [唯一标识]
build_type: [适用构建类型 / 跨类型]
source_papers: ["作者_年份_期刊", "作者_年份_期刊"]
confidence: [high / medium / low]
-->

### [Pattern Name]

**适用场景**: [一句话说明在什么情况下使用]
**排列模式**: [Warrant-Embedded / Parallel / 等]
**范文来源**: [论文引用]

**骨架**:
```
[可填充的句法结构]
```

**为什么有效**: [该模式的说服逻辑]
**注意事项**: [使用该模式时的风险和边界]
**反模式**: [什么情况下不该用]
```

---
