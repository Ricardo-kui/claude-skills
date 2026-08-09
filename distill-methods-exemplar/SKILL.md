---
name: distill-methods-exemplar
description: |
  Methods 范文蒸馏 meta-skill。输入单篇或批量论文的 Methods 文本，输出结构化提炼报告：段落骨架、表达 DNA、可迁移范式、不可迁移边界、以及 write-methods 更新建议。
  核心原则：提炼 HOW they argue, not WHAT they said。不复制句子，只提取可跨论文复现的论证组织方式。

  三层目标：
  1. **学习顶刊写作叙述手法** — 理解 Methods 如何组织证据、处理 validity threat、完成说服
  2. **完善 write-methods skill** — DNA 量化和跨论文验证反哺主骨架和路由逻辑
  3. **丰富 econometric-models** — 验证通过的变体写入 write-methods 内部 corpus，corpus 是学习成果的沉淀

  下游：`write-methods` (v3.0.0+) 检测到蒸馏请求时自动路由到本 skill。
  触发词：「蒸馏 methods」「methods 范文分析」「拆解 methods」「提取 methods 模板」「处理新论文 methods」「methods 骨架提炼」。
  **消歧**：用户未指定 section（只说"分析这篇论文""蒸馏一下"）时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。
  **反向边界**：Methods 写作用 `write-methods`；审查已有 Methods 草稿用 `methods-review`；全稿 QC 用 `pollock-qc`。本 skill 只蒸馏范文，不生成写作、不做 QC。
---

# Role

你是 Methods 范文的**结构化蒸馏器**。基于 nuwa-skill 的流水线逻辑和 Pollock 2025 Ch07，将单篇或批量论文的 Methods 转化为可复用、可验证、可入库的写作资产。

**你的工作是三层递进**：
1. **学习顶刊叙述手法**（Phase 0–2）：设计分类 → 槽位映射 → 表达式骨架 + Validity Logic——回答"这篇论文的 Methods 是怎么说服审稿人的？"
2. **量化和跨论文对比**（Phase 3–4）：Methods DNA 指标 + 与已有 corpus 交叉验证——回答"这个写法是独特的还是已经在 corpus 里了？"
3. **沉淀到 corpus**（Phase 4–5）：仅将验证通过且真正新增的变体写入 `write-methods/econometric-models/[设计类型].md`——corpus 是学习成果，不是目标本身

核心原则：
- **How > What**：提炼段落如何组织证据、如何处理 validity threat、如何完成说服，而非复制具体措辞。
- **范式排他性**：只提取某类方法设计**特别需要**的组织方式，而非所有文章都有的通用废话。

## Phase 0.5 — Story-Fidelity Gate

加载 `../paper-story-contract/references/distillation-gate.md` 并输出 `story_fidelity`。Methods 的 section role 是 `empirical_arena`：模式必须帮助测试 promised resolution 或提高可信度，不因其“像故事”而采用。单篇模式不能改变核心规则；ritual 只能记录为 `ritual_only`；与 story-to-design mapping 冲突的模式标记为 `reject`。
- **可生成性**：每个提炼出的骨架必须能直接指导一篇新论文写出段落。

## 调用方式

```
/distill-methods-exemplar <输入路径或文本> [--batch] [--design-filter=面板数据/DiD/实验/...] [--output-format=markdown/json]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--design-filter]`（可选）: 只处理特定设计类型的论文
- `[--output-format]`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果省略输入**，进入交互式询问后执行蒸馏。

---

## Phase 0 — 论文类型与设计分类

在读取正文前，先判断这篇论文 Methods 的**设计范式**，决定后续槽位检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| 数据形态 | 面板数据 / 截面数据 / 实验 / 多研究 / 质性→量化 |
| 识别策略 | OLS/FE / 自然实验/DiD / IV/2SLS / RDD / 匹配 / 实验随机化 |
| 估计器 | 线性 / Logit/Probit / 生存分析 / 计数模型 / SEM / GMM / Tobit |
| 特殊结构 | 多行为者 / 网络效应 / 文本构念 / 堆叠扩散 / 同时方程 |
| 因果强度 | 描述性 / 预测性 / 因果识别（quasi-experimental）/ 实验因果 |

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_design_profile:
  data_architecture: "面板数据 / 截面 / 实验 / ..."
  identification_strategy: "OLS+FE / DiD / IV / ..."
  estimator_family: "线性 / 非线性 / 生存 / ..."
  special_structure: "无 / 匹配DiD / 文本构念 / ..."
  causal_ambition: "描述 / 预测 / 准实验因果 / 实验因果"
```

---

## Phase 0.75 — 选材 Gate（批评驱动，Skill-SP 启发）

在进入 Phase 1 深读前，用 `write-methods/econometric-models/_evidence_registry.yaml` 中该设计类型的 `validation_history` 判断**这篇论文值不值得深蒸馏、优先级多高**。批评由 Claude 在 write-methods 会话中自动登记，也可用 `_update_registry.py --record-critique` 批量补登（见 Phase 4.5 批评登记）。

### 三带判定（依据 registry meta.usage_stats_schema）

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap**（未覆盖） | `slots_covered` 相对本文档覆盖存在缺口（静态，不依赖登记） | **HIGH**：ADD 候选，优先深读 |
| **critique_heavy**（批评密集） | `revise + reject >= 2` | **HIGH**：REPLACE/EXTEND 候选，优先对比已有变体质量；`common_revise_reasons` 是精炼的直接依据 |
| **quiet**（无批评） | 其余情况 | MEDIUM：正常蒸馏 |

**明确不做的**：不按使用频率/accepted_rate 淘汰或降级变体——语料是长期写作资产，频繁使用且好用应提升路由权重，而非降级（Skill-SP 语义修正，见 registry `non_signals`）。

### 执行规则

- **单篇论文（用户明确指定蒸馏）**：不拒绝，但必须输出带判定供 Phase 3 新颖度判断参考。
- **批量模式（--batch）**：按带排序（gap/critique_heavy → quiet），优先深读 HIGH 档；资源不足时 quiet 档仅做 Phase 1 粗标注，不进入 Phase 2 深提炼。
- **重复闸门**：Phase 2.2 得出骨架后，若与已有变体（corpus 或 registry）高度重叠（jaccard ≥ 0.33 或同源模式），按 SKIP 处理——不为重复模式新增变体（对应 Skill-SP `find_duplicate_skill` 语义）。

### 输出格式

```yaml
phase_0_75_selection_gate:
  design_type: "生存分析"
  band: "gap | critique_heavy | quiet"
  evidence:
    revise: 1
    reject: 0
    last_critique: "2026-06-01"
    critique_reasons: ["复发事件独立性假设的边界说明不充分"]
  priority: "HIGH | MEDIUM"
  rationale: "1 句话：为什么这篇论文处于该带"
```

### 趋同批评聚合检查（meta-skill 轻量版）

若该设计类型 `common_revise_reasons` 中**同一原因出现 ≥2 次**（趋同批评），在 Phase 0.75 输出中追加聚合检查块：

```yaml
phase_0_75_convergent_critique_check:
  design_type: "生存分析"
  convergent_patterns:
    - pattern: "复发事件独立性假设的边界说明不充分"
      count: 2
      last_critique: "2026-08-08"
  aggregation_suggestion: "该模式是否应升级为主骨架级修订（REPLACE 主骨架段落或增加警告行）——由本次蒸馏证据决定，仍走预览-确认 gate"
```

- **批评计数 < 2 时静默**——不输出该块，不预建机制。
- 若本次蒸馏的骨架恰好与该模式相关：Phase 4 的 `skill_update_instructions` 应包含主骨架级修订候选（`skill_main_skeleton_update`），同样先预览后确认。
- 若本次蒸馏的骨架与批评模式无关：聚合建议标记为"待后续蒸馏验证"，不强行修订。

---

## Phase 1 — Methods 文本读取与粗粒度解构

读取 Methods 全文，按叙事槽位目录（M1–M10）进行**粗粒度标注**。标注时只定位段落功能，不做深入分析。

### 槽位映射表（与 write-methods 对齐）

| 槽位 | 功能 | 粗粒度标注任务 |
|------|------|----------------|
| M1 | 研究情境 / 实证背景 | 定位 setting 段落，提取 3 个理由的论证结构 |
| M2 | 数据来源与样本漏斗 | 定位样本描述，标记起始 N → 每步排除 → 最终 N |
| M3 | 因变量操作化 | 定位 DV 定义段落，标记构念→操作化→来源→方向 |
| M4 | 自变量 / 核心预测变量 | 定位每预测变量段落，标记与假设的对应关系 |
| M5 | 调节/中介/机制变量 | 定位边界/机制变量，标记交互项说明 |
| M6 | 控制变量与竞争性解释 | 定位 controls 段落，标记每个变量的 because 逻辑 |
| M7 | 模型规格与估计方法 | 定位 estimator 段落，标记公式+文字+诊断 |
| M8 | 识别策略 / 效度 / 诊断检验 | 定位 identification 段落，标记假设+检验+位置 |
| M9 | 多研究 / 实验程序 | 如适用，标记研究间衔接结构 |
| M10 | Methods→Results 过渡（可选） | 定位 transition 段落，标记 Results 预告结构。顶刊实证论文中约 70% 缺失，若缺失不严重惩罚覆盖率 |

### 输出格式

```yaml
phase_1_slot_map:
  M1:
    quality: "✅ 强 / ⚠️ 可改进 / ❌ 缺失"
    paragraph_range: "[第X段–第Y段]"
    setting_claims: ["理由1", "理由2", "理由3"]
    learn_worth: "值得学/不值得学/反模式 — 1句话原因"
  M2:
    quality: "✅ 强 / ⚠️ 可改进 / ❌ 缺失"
    funnel_steps: ["起始", "排除1", "排除2", "最终"]
    has_numbers: true/false
    learn_worth: "值得学/不值得学/反模式 — 1句话原因"
  # ... 其余槽位
```
**quality 标记标准**：
- ✅ 强：该槽位的处理方式是同类设计中的典范，可提炼为骨架
- ⚠️ 可改进：该槽位存在但组织方式有改进空间，可作为反模式记录
- ❌ 缺失：该设计类型的强制槽位完全缺失

**learn_worth**：1 句话判断该槽位对完善 write-methods skill 的价值——"值得学"意味着可提炼新骨架，"反模式"意味着应加入 skill 的警告列表，"不值得学"意味着与已有 corpus 高度重叠。

---

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照设计类型，检查 Methods 是否覆盖了该类设计**必须出现**的槽位。

### 设计类型强制槽位表

| 设计类型 | 强制槽位 | 缺失即高风险 |
|----------|----------|--------------|
| 面板数据/OLS | M1, M2, M3, M4, M6, M7, M10 | M7 缺诊断、M6 缺 because |
| 自然实验/DiD | M1, M2, M7, M8 | M8 缺平行趋势、M2 缺处理/对照描述 |
| IV/2SLS | M4, M7, M8 | M8 缺排他性约束、M7 缺第一阶段说明 |
| 实验 | M1, M2, M6, M7, M8 | M8 缺操纵检验、M2 缺随机化说明 |
| 匹配DiD | M2, M7, M8 | M2 缺匹配后平衡、M8 缺重叠支撑 |
| 文本构念 | M3/M4, M7, M8 | M3/M4 缺效度链、M8 缺与人工程度相关性 |
| 同伴效应/网络效应 | M4, M7, M8 | M4 缺反射性问题处理、M8 缺 falsification |
| 动态面板/GMM | M7, M8 | M7 缺 Nickell bias 说明、M8 缺过度识别 |
| 同时方程 | M1, M4, M7, M8 | M7 缺 order/rank 条件、M8 缺方程特定诊断 |
| 稀有结果 | M2, M3, M7 | M2 缺抽样策略说明、M7 未解释稀有结果对幅度的影响 |
| 实证对象构建 | M2, M3/M4, M7 | M2 缺从原始痕迹到分析变量的构建步骤、M3/M4 缺 face validity 论证 |
| 事件历史+事件研究 | M2, M3, M7 | M2 缺过程时钟定义、M3 未分过程/市场双时钟 DV、M7 缺分布选择依据 |
| PSM匹配面板 | M2, M7, M8 | M2 缺匹配步骤与共同支撑域、M8 缺匹配后平衡检验 |
| 多行为者设计 | M2, M3, M7 | M2 缺多数据源匹配逻辑、M3 未区分主/辅行为者结果 |
| 推断二元结果 | M3, M4, M7, M8 | M3 缺从信号到状态的推断逻辑、M8 缺分类准确性验证 |
| IV + 非线性 (Tobit/Poisson/生存) | M4, M7, M8 | M8 缺排他性约束与第一阶段说明、M7 未解释非线性估计器选择依据 |

### 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["M1", "M2", ...]
    present_slots: ["M1", "M2", ...]
    missing_slots: ["M8"]
    coverage_verdict: "完整 / 轻微缺口 / 严重缺失"  # 替代数字百分比——覆盖率 80% 但论证平庸不如 60% 但每个槽位都是典范
  special_design_markers:
    detected: ["IV", "匹配"]
    properly_addressed: ["M7 第一阶段"]
    inadequately_addressed: ["M8 排他性约束仅一句话"]
  source_sufficiency:
    sample_funnel_auditable: true/false
    diagnostic_tests_named: true/false
    robustness_location_specified: true/false
  contradictions_or_gaps: ["M7 声称用 FE 但未报告 Hausman", "M8 说检验在 Results 但 Results 未出现"]
  information_poverty_dimensions: ["未报告 VIF 值", "未说明标准误聚类层级"]
  skill_implication:
    - slot: "M2"
      implication: "无漏斗计数 → 建议在面板数据-OLS 变体 X 的警告中标注'多数据库合并可省略漏斗，但需报告交集后 N'"
    - slot: "M7"
      implication: "分布选择仅一句话 → 建议在生存分析 M7 主骨架中增加参数分布选择的最小论证要求"
```

---

## Phase 2 — 深度提炼：段落功能、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

### 2.1 段落功能提炼

回答：这个段落完成了什么**说服动作**？

| 说服动作 | 示例 |
|----------|------|
| 合法性论证 | Setting 段落论证"为什么这个情境适合检验理论" |
| 可审计性 | 样本漏斗让审稿人可以复现样本选择 |
| 对齐性 | 变量操作化段落建立构念→假设→测量的映射 |
| 抗辩性 | Controls 段落预判竞争性解释并提前排除 |
| 可信性 | 识别策略段落让审稿人相信因果推断成立 |
| 导航性 | M10 段落预告 Results 的阅读顺序 |

### 2.2 表达骨架提炼（Expression Skeleton）

将具体措辞抽象为**可填充的句法结构**。这是最关键的输出。

**骨架格式**：
```text
[功能标签]: 论证 setting 合法性
[骨架]: [Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period].
[原始句锚点]: "This setting provides a natural laboratory for examining how firms' product portfolios shape competitive dynamics, for three reasons."（来源论文原句 1–2 句，15–40 tokens，风格参照用）
[可迁移性]: 高 — 出现在 12/28 篇范文中
[范式排他性]: 通用 setting 论证，不绑定特定设计
[设计变体]: DiD 版本替换首句为政策冲击描述；实验版本替换为"We test X using a Y experiment"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- **原始句锚点（verbatim anchor）**：来源论文中的 1–2 句原文（15–40 tokens），保留原味——骨架抽象负责"结构可迁移"，锚点负责"语言风味不丢失"。生成时以锚点校准"顶刊味道"，不逐字复制。选句标准：最能代表该变体叙事手法的句子（不是信息量最大的，而是最有"论文味"的）
- **锚点拼接硬规则（2026-08-09 审计教训）**：多句锚点必须保留省略号标记——**禁止跨段落/跨小节无声拼接**；同段删句也必须用 "..." 标注被删内容。读者会把锚点当连续引文，无声拼接会误导读者的因果链理解
- **锚点来源检索**（取原句/补锚点时）：优先本次蒸馏论文原文；其次按论文 id/作者/标题检索 Obsidian 知识库：
  - `D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\_parsed_texts\mvp30`（MVP30 解析文本，主力库，frontmatter 含 journal/author/year，正文为全文）
  - `D:\OneDrive\Obsidian Vault\Clippings`（网页剪藏）
  - `D:\OneDrive\Obsidian Vault\文献笔记库\01 导入\论文导入`（OvisOCR 论文导入）
  检索不到原文时锚点标记"待补"，不阻塞写入
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类设计所需）
- 设计变体（同类骨架在不同设计中的改写模式）
- **skill_gap**（相对于 write-methods 当前 corpus 的状态）：
  - `ADD`：当前 corpus **无**此类变体 → 新增到目标设计类型文件
  - `EXTEND`：当前 corpus **有**但本论文提供了额外维度 → 追加为变体
  - `REPLACE`：当前 corpus 的旧变体**质量不如**本论文 → 标记旧变体，建议替换
  - `SKIP`：与当前 corpus **高度重叠** → 不写入，仅在学习要点中记录
  - 每个骨架必须标注对应的 `目标文件`（如 `生存分析.md`）和 `目标槽位`（如 M7）

### 2.3 Validity Logic 提炼

提取该 Methods 如何处理三类 validity threat：

| Threat 类型 | 提炼问题 |
|-------------|----------|
| 内部效度 | 如何排除 omitted variable / reverse causality / simultaneity？识别策略是什么？ |
| 构造效度 | 如何论证 measure 捕捉了 construct？是否有效度检验链？ |
| 外部效度 | Setting 的 boundary 在哪里？是否讨论 generalizability 限制？ |

输出格式：
```yaml
phase_2_distillation:
  M1_setting:
    persuasive_action: "合法性论证"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (12/28)"
        paradigm_exclusivity: "通用"
        design_variants: ["DiD variant", "Experiment variant"]
    validity_logic:
      internal: "..."
      construct: "..."
      external: "..."
  # ... 其余槽位
```

---

## Phase 3 — 论证手法诊断

不量化机械指标（句数、对齐密度），而是诊断这篇 Methods 在论证上的强弱之处。

### 诊断维度

| 维度 | 诊断问题 | 输出 |
|------|---------|------|
| **because 密度** | 控制变量/样本排除中有多少附带了 because 理由？ | 定性判断 + 对 skill 模板的启示 |
| **因果语言自律** | "effect of" vs "associated with" 的分布是否匹配设计强度？ | 越级/一致/过于保守 |
| **审计链完整性** | 样本漏斗是否可让审稿人复现？ | 完整/可改进/不可审计 |
| **时间逻辑清晰度** | t-1 / contemporaneous / event window 标记是否明确？ | 清晰/模糊 |
| **新颖度**（替代旧的对齐度） | 这篇 Methods 的论证组织方式与 write-methods 当前模板**有多少不同**？不同才值得学 | 高度新颖 / 部分新颖 / 与模板一致 |

每个诊断维度输出时附带 skill 对比：
```
[定性判断] → 与 write-methods 当前模板的关系 → [skill 改进方向]
```

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 设计分类: [来自 Phase 0]
- 期刊: [journal]
- 新颖度: 这篇 Methods 的论证组织与现有模板的差异程度

## Slot Coverage (M1–M10) — 含 quality + learn_worth
[Phase 1 输出]

## 值得学的骨架（skill_gap != SKIP）
[来自 Phase 2.2 — 仅列出真正新增的]

## 论证手法诊断
[Phase 3 诊断维度]

## Validity Logic Map
[来自 Phase 2.3]

## 不可迁移的事实
[论文特有的数据库名、行业背景、样本量——仅当判断骨架可迁移性时需要参考]
```

---

## Phase 4 — 技能更新指令生成（Skill Update Instructions）

本阶段生成**受治理的 adoption instructions**。输出回答三个问题：
1. **改哪个文件** → 精确到 `write-methods/econometric-models/[设计类型].md`
2. **怎么改** → ADD / EXTEND / REPLACE / SKIP，含具体骨架和插入位置
3. **为什么** → 与当前 corpus 的差异 + 对 write-methods skill 的提升

### skill_update_instructions 格式

```yaml
phase_4_skill_update_instructions:
  - action: "ADD"           # ADD / EXTEND / REPLACE / SKIP
    story_fidelity_classification: "section_variant"
    target_file: "生存分析.md"  # write-methods/econometric-models/ 下的文件名
    target_slot: "M7"
    insert_after: "变体 6（piecewise exponential）"  # 语义定位——描述该插入在哪个已有变体之后，不硬编码数字
    distinct_from: "变体 6（piecewise exponential）— 本变体是 Cox-type 参数风险模型（continuous-time），变体 6 是 AFT 框架（piecewise）"  # ADD/EXTEND 必填：与最近变体的一句差异，写入速查表「区别」列
    skeleton: "..."
    verbatim_anchor: "We estimate a gap-time model that allows the hazard to depend on the time elapsed since the previous recall, in line with prior work on recurrent events."  # 来源论文原句 1–2 句，15–40 tokens，风格参照
    reason: "当前 生存分析 M7 变体1-6 全部是 AFT+Weibull 框架——缺少指数/参数风险模型的复发事件处理。本论文填补了这一缺口，且包含了 gap-time vs continuous-time 的显式论证。"
    source_paper: "Mayo_Ball_Mills_2022_POM"

  - action: "SKIP"
    target_file: "生存分析.md"
    target_slot: "M7"
    reason: "AFT+Weibull 段落与已有变体1（4/4 复现）高度重叠——不构成新的叙事模式。"

  - action: "EXTEND"
    target_file: "面板数据-OLS.md"
    target_slot: "M2"
    insert_after: "变体 8（回顾性偏差三角检验）"
    distinct_from: "变体 8（回顾性偏差三角检验）— 本变体是多库交集→直接报最终 N（省略逐步排除），变体 8 是逐步排除漏斗"
    skeleton: "..."
    reason: "当前 面板数据-OLS M2 变体默认要求逐步排除漏斗。本论文展示了一种替代模式（多数据库交集→直接报告最终 N），需作为可选变体加入。"

  - action: "REPLACE"
    target_file: "计数模型.md"
    target_slot: "R3"
    replace_variant: "变体 1（Cutolo 负二项四拍）"  # 描述要替换的变体
    replacement_skeleton: "..."
    verbatim_anchor: "Across models, the positive effect of advertising on recall counts remains consistent, with an incident-rate ratio of [x] (p < .01)."  # REPLACE 时同时提供新锚点
    reason: "当前变体的拍数不够完整——本论文的四拍节奏更完整（假设提醒→双DV方向→百分比翻译→支持判断）。"

  new_anti_patterns_for_skill:
    - target_file: "面板数据-OLS.md"
      slot: "M2"
      pattern: "无漏斗计数——多数据库合并但未说明交集前后的 N 差异"
      evidence: "本文仅说'the intersection resulted in N=2932'——无法审计数据损失"

  new_honesty_boundaries_for_skill:
    - target_file: "生存分析.md"
      boundary: "复发事件 AFT 模型假设事件间独立（同一 firm 的两次召回无关联）。若理论预测事件间存在依赖，需额外使用 frailty/shared frailty 模型或报告稳健性检验。"

  skill_main_skeleton_update:
    - target_file: "生存分析.md"
      update: "M7 主骨架增加一行：'若处理组/控制组存在系统性差异，应在估计前使用 CEM 预处理数据（参见变体13）。'"
```

### 写入后操作（两段式：预览 → 确认 → 写入）

**原则：所有待写入内容必须先展示给用户评估，用户确认后才写入。不自动写入任何变体。**

#### Step 1 — 写入预览（Preview）

Phase 4 输出的每条 `action != SKIP` 指令渲染为「待写入预览块」，随蒸馏报告一起输出：

```markdown
### 待写入 #N：[action] → [target_file] [slot]（[变体名]）
- **来源论文**: [source_paper]
- **插入位置**: [insert_after]
- **区别于**: [distinct_from——确认与最近变体的一句区分是否准确]
- **理由**: [reason]
- **原始句锚点**: [verbatim_anchor 原句展示——风格参照，评估风味是否地道]
- **骨架全文**:
  [skeleton 逐字展示，不摘要]
- **评估要点**: [该变体应满足的标准，如"无机构名残留"、"填入实际内容后可生成顶刊风格段落"]
```

- 预览块必须展示**骨架全文**，不是摘要。
- `REPLACE` 额外给出「旧变体 vs 新变体」并排对比，标注被替换变体名。

#### Step 2 — 评估确认（Gate）

用户明确表态后才执行写入。默认确认粒度：
- **单篇模式**：逐个确认——用户可指出哪条不写、哪条需修改（修改后重新展示）。
- **批量模式（--batch）**：一次确认写入全部 `ADD/EXTEND`；`REPLACE` 仍逐个确认（替换是破坏性动作）。
- 用户说"全部写入"即跳过剩余逐个确认。

确认后的写入步骤不变：打开 `target_file` → 按 `insert_after` 插入 → 更新 `source_papers` / `variants_count` / `updated` → 对 `new_anti_patterns_for_skill` 写入「反模式」段落 → 更新 `INDEX.md` 表行和「已填充变体」计数 → **更新文件顶部「变体速查表」**（新变体行 + 槽位分布总览，`区别` 列直接取 `distinct_from`；速查表与正文变体必须同步，quality_check 会校验）。

**旧变体锚点回填**：`REPLACE`/`EXTEND` 触碰已有变体且该变体缺 `原始句锚点` 时，按上述锚点来源检索规则**顺带补锚点**（检索不到原文则标"待补"，不阻塞写入）。

#### 评估清单（供用户参考）

- [ ] 骨架无机构名/政策名/数据库名残留（[placeholder] 泛化彻底）
- [ ] 与已有变体不重复（Phase 3 新颖度成立）
- [ ] 骨架填入实际内容后能产出顶刊风格段落（可生成性）
- [ ] **原始句锚点保留原文风味**（生成时可据此校准"顶刊味道"；锚点非复制源）
- [ ] 因果语言强度与设计类型匹配
- [ ] 符合你的写作习惯与当前论文需要

`core_candidate`、单篇证据，或任何 `skill_main_skeleton_update` 只生成显式人工审核包——同样先展示后由用户决定；不得自动修改 SKILL.md、路由、强制槽位顺序、story schema 或 stage gate。

### 批评登记（critique-driven stats）

登记来源 = **Claude 在 write-methods 会话中自动捕获用户批评**（见 write-methods SKILL.md 批评登记），用户零动作；批量补登可用：

```bash
python _update_registry.py --record-critique critiques.yaml
```

`critiques.yaml` 格式：

```yaml
critique_updates:
  - design_type: "生存分析"
    verdict: "revise"    # revise=需大改 / reject=被弃用重写
    reason: "复发事件独立性假设的边界说明不充分"   # 进入 common_revise_reasons，精炼直接依据
    date: "YYYY-MM-DD"   # 可选，默认今天
```

- 脚本累加 `revise/reject`、更新 `last_critique`、去重追加 `common_revise_reasons`（最多 8 条），输出信号（quiet/critique_heavy）供下一轮 Phase 0.75 选材。
- 不登记满意信号、不设淘汰逻辑——语义见 registry `meta.usage_stats_schema`。

---

## Phase 5 — 质量验证、QC 输出、技能版本影响

生成最终的蒸馏质量报告，确保产出物可以安全进入 Skill 更新流程。

### QC Checklist

- [ ] **Completeness**: 所有强制槽位（根据设计类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊做法泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的段落
- [ ] **Substance not Verbatim**: 具体事实已泛化为 [placeholder]；论证结构和过渡句式可保留原貌
- [ ] **Fact Boundary**: 所有不可迁移事实已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与设计类型匹配
- [ ] **Skill Update Audit**: Phase 4 的每个 `ADD/EXTEND/REPLACE` 指令都有明确的目标文件和插入位置
- [ ] **Story Fidelity Audit**: 每个 adoption 指令都有 classification；单篇论文未改变核心规则

### skill_version_impact（新增）

每个 `ADD/EXTEND/REPLACE` 行动必须附带版本影响评估：

```yaml
phase_5_skill_version_impact:
  write_methods:
    current_version: "3.0.0"
    suggested_version: "3.1.0"  # 或 "3.0.0"（仅 minor 时不变）
    bump_reason: "ADD 6 个变体 / EXTEND 2 个变体 / 新增 1 个主骨架警告"
    changed_files:
      - "生存分析.md: +2 变体 (13-14)"
      - "面板数据-OLS.md: +1 变体 (9)"
      - "INDEX.md: 更新表行和计数"
    main_skeleton_updates:
      - "生存分析 M7: 增加 CEM 预处理建议行"
      - "面板数据-OLS M2: 增加多数据库合并替代方案注释"
  distill_methods:
    current_version: "1.1.0"
    suggested_version: "1.1.0"  # 本次蒸馏未发现 skill 自身协议需修改
```

### 最终输出物清单

1. **Phase 4 Skill Update Instructions**（候选技能更新指令——随待写入预览块输出，经用户确认后执行）
2. **Expression Skeletons**（仅含 `skill_gap != SKIP` 的骨架）
3. **Validity Logic Map**（该设计类型的 threat 处理模式）
4. **Methods DNA with Skill Comparison**（DNA 指标 + skill 对比解读）
5. **Skill Version Impact**（版本号建议 + 变更文件清单）
6. **学习要点**（3-5 条：这篇论文最值得学的叙事手法 + 为什么有效）
7. **可改进之处**（这篇顶刊论文 Methods 仍然可以做得更好的地方——反哺 skill 的警告列表）
8. **QC Result**（通过/需修正/拒绝入库）

---

## 红线

- 骨架用 [placeholder] 泛化具体内容（变量名、数据库名、系数值）；但关键的论证连接词（"because" "however" "in contrast"）和叙事结构短语（"for three reasons" "to address this concern"）可保留——这些正是要学的手法
- causal language 强度匹配设计类型（OLS→"associated with", DiD→"effect of", 实验→"increases"）
- 骨架中不编造统计量；原文薄弱处如实记录
- 不同设计类型分桶处理，不跨范式套用

## 与下游 Skill 的接口

- **`write-methods`** — Phase 4 `skill_update_instructions` 直接指定写入文件和插入位置
- **`methods-review`** — Phase 1.5 槽位覆盖检查可复用

---
*基于 Pollock 2025 Ch07、MVP30 范文语料库构建。版本 1.8.0（Phase 0.75 批评驱动选材 + 趋同批评聚合检查 + Phase 4.5 批评登记 + 写入预览-确认两段式 + 变体原始句锚点与 Obsidian 知识库回填 + distinct_from 字段与速查表维护）。*
