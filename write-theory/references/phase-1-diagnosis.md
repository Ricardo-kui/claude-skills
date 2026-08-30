# Phase 1: theory diagnosis

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 1: 类型诊断（自动）

来自 paper-state.yaml:
- Gap 类型: [gap_type]
- Makadok 维度: [makadok_dimension]
- Introduction 推荐: [recommended_theory_variant]
- 承诺假设数: [promised_hypothesis_count]
- Central Knot: "[story.central_knot]"

→ 默认路由: **[recommended_theory_variant]**
→ variant 文件: `corpus/variants/[variant_filename]`  # 变体名→文件名映射见下表；下游 step 3 直接用此文件名加载
→ 理由: [gap_type] × [makadok_dimension] → [路由理由——由 routing_table.md 查询]

**变体名 → variant 文件名映射**（step 3 加载用）：

| 变体名 | variant 文件 |
|--------|-------------|
| A 构念辨析型 | `A_construct_differentiation.md` |
| B 机制推演型 | `B_mechanism_elaboration.md` |
| C 假设树型 | `C_hypothesis_tree.md` |
| D 质性过程理论型 | `D_process_theory.md` |
| E 调节效应型 | `E_moderation.md` |
| F 竞争假设型 | `F_competing_hypotheses.md` |
| G 辩证对立型 | `G_dialectical_opposition.md` |

是否确认此路由？或需调整为其他变体？
```

**交互式诊断树**（三级回退均未命中时）：

```
你的理论构建方式是什么？
│
├── 核心贡献是区分两个易混淆的构念 → [A] 构念辨析型
├── 核心贡献是解释 X 如何影响 Y 的因果/过程机制 → [B] 机制推演型
│   └── 同一构念的两个维度产生相反/互补预测 → [B2] 双轨并行
├── 核心贡献是多层次/多条件的假设体系 → [C] 假设树型
├── 核心贡献是揭示动态过程和时间演化 → [D] 质性过程理论型
├── 核心贡献是识别 boundary condition / contingency → [E] 调节效应型
│   ├── X, Y, Z 在同一层级 → [E1] 同层调节
│   ├── Z 在更高/更低层级 → [E2] 跨层调节
│   └── Moderator 为分类变量 → [E1.1] 分组调节
├── 核心贡献是裁决两种对立理论的竞争预测 → [F] 竞争假设型
└── 核心贡献是同一构念/现象对不同受众产生相反效果 → [G] 辩证对立型
    └── 两类受众是同一层面的不同角色 → [G1] 水平辩证
    └── 两类受众是不同层面的决策者 → [G2] 跨层辩证
```

**如果检测到上游 Introduction 输出**：先查 `../corpus/meta/routing_table.md` 给出默认推荐，再进入确认。

**1.2 Vault 基线检索**（可选——仅在 paper-state.yaml 有 vault 配置时执行）

从用户知识库拉取当前主题的理论证据，生成 Vault Knowledge Brief 作为 Phase 2-4 理论构建的文献弹药。**执行条件**：paper-state.yaml 中 `paper.vault` 节存在且至少有一个非 null 字段；无 vault 配置时静默跳过。三级回退检索流程、Brief 输出格式与通用性保证见 `../corpus/meta/vault_evidence_retrieval.md`。

**1.3 Rising Action 定位**（Pollock 2025 Ch02）

**制度冲击检测**（自动判断，无需用户输入）：

在 Phase 1.3 诊断之前，自动检测是否需要激活 Phase 2.3（制度冲击类研究的 Theory Lens 特殊适配）：

```
检查以下信号（任一满足即激活 Phase 2.3）：
├── 上游 `theory_hints` 中的 `identification` 字段包含 IV / DiD / RDD / natural experiment / quasi-experiment
├── 上游 `theory_hints` 中的 `empirical_setting` 描述涉及政策变化、法律冲击、制度差异、州级差异
├── 用户输入的研究描述中出现：staggered adoption / policy shock / regulatory change / law change / institutional reform / eligibility threshold
└── 以上均不满足 → 跳过 Phase 2.3，按标准 Theory Lens 流程执行
```

**检测输出**：
- 如果激活 Phase 2.3 → 在输出结构中插入 Phase 2.3 块，并标记"制度冲击适配已激活"
- 如果跳过 → 不输出 Phase 2.3 相关内容，保持流程简洁

Theory & Hypotheses 在整篇论文的 Five-Act 结构中属于 **Rising Action** 的后半段。

**前置检查**（优先从 canonical `story`，其次从 `theory_hints` 解析）：
- `story.central_knot`：Theory 的叙事锚点。
- `story.protagonist` / `story.characters`：角色定位初始值。
- `story.storylines[*].id`：每个假设的强制绑定目标。
- legacy `central_knot_statement` / `protagonist_construct` / `narrative_arc` 只按 `intake-and-story-gate.md` 迁移读取，不再输出旧字段。

**Central Knot 推断规则（当 `story.central_knot` 缺失时，仅生成 provisional 诊断）**：
- Incommensurability → 推断为"对立理论或证据之间的矛盾冲突"
- Inadequacy → 推断为"现有解释存在盲区或基于错误假设"
- Incompleteness → 推断为"遗漏了关键维度、机制或时点"
- 具体推断：从 Tension 模板的 `[gap statement]` 句法签名中提取核心冲突，或从用户提供的 Gap 描述中识别转折信号词（"However"/"Yet"/"Although"/"In contrast"）后的核心主张

**Incommensurability 二级诊断（仅该 gap 激活）**：读取 `incommensurability-resolution-routes.md`，先提取 L0 stable reasoning kernel，并验证 X/Y/层级/时间/estimand 可比和方向冲突真实，再定位 R1（X 分类）、R2（Y 分类）、R3（对立机制）或 R4（情境调节）。输出 `primary_route`、可选 `secondary_route`、置信度、最接近替代路线、`unclassified_residual`、`adjudicating_prediction` 与 architecture necessity。R1–R4 优先于粗粒度 Gap×Makadok 默认路由，但不自动决定 A–G、H 数量或模型形式。

推断出的 Central Knot 只能用于 local-only 诊断，标记为 provisional；在用户确认并形成 canonical story 前，不写入 paper-state。

按顺序读取以下语料库文件：

1. **Rising Action 协议**
   读取 `../corpus/storytelling/rising-action-protocol.md`
   → 确认从 Introduction 继承的 Central Knot 在此继续被 tie

2. **Plot Emergence 检查**
   读取 `../corpus/storytelling/plot-emergence-check.md`
   → 验证情节是否从构念互动中自然浮现，而非强加

3. **Knot 连续性检查**
   读取 `../corpus/storytelling/knot-continuity-check.md`
   → 验证 Theory 的每个段落都让 knot 更紧，无 extraneous storyline

**诊断结果输出**：narrative risk 标记附加到 Phase 4 QC 清单。

**1.4 Prose Craft 定位**（Pollock 2025 Ch03；以下三个工具与 Phase 2-5 并行执行）

Theory section 的 Rising Action 不仅需要功能推进，还需要 prose 层面的可读性。
按任务读取 `../../write-introduction/corpus/storytelling/prose-craft-checklist.md` 的相关节：段落架构用 §0，例证需求用 §2，声音用 §3，节奏用 §4，过度/不足声明用 §5.6–5.7。不要为一般 Theory 任务加载整份清单。

**新增**：段落级 architecture 检查（PEEL/PEAL、paragraph length、topic sentence placement、coherence）参见 `../../write-introduction/corpus/storytelling/prose-craft-checklist.md` §0；句子级 transition 信号词参见 `../../write-introduction/corpus/micro-templates/transition-signals.md`。

#### Human Face in Theory（按需使用）
- **Knot Inheritance**：当 knot 抽象或跨域时，可用 1 句具体场景说明"这个问题在现实世界中长什么样"
  - 句式："To resolve the tension that [knot], consider what happens when [Company] tried to [action]..."
- **Knot Deepening**：新构念抽象、易混淆或无法由定义直接想象时，配正例/反例
  - 例："We define [construct] as [definition] (Author, Year). A [concrete instantiation], for example, might [observable behavior]..."
- **Knot Tying**：why-chain 跨层、反直觉或负荷较高的步骤可配 1 个微型场景（1-2句）
  - 例："Because [actors with trait X] prioritize [goal A] over [goal B], they may [observable behavior] when [condition]. Consider how [Company] [specific action]..."

#### Showing vs Telling in Theory
- **Stroke**：负责推进推理；若连续推理造成读者无法模拟过程，再补解释、例子或反事实。
- **Glide**：负责定义澄清、文献定位和边界说明，但不能变成引用停滞。
- Pollock Ch03 只给定性判据；本 skill 不设置固定比例或“每 N 句必须举例”的硬门槛。

#### Conversational Voice in Theory
- **P1**：用 "To resolve the paradox that [knot], we argue that..." 承接
- **假设推导**：用 "We argue that..." / "We hypothesize that..." 引出每个假设
- **禁止**："It is argued that..." / "It is hypothesized that..." / "The literature suggests that..."（无主语被动）

---
