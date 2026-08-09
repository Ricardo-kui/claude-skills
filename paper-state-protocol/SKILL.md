---
name: paper-state-protocol
description: |
  paper-state.yaml 协议 v1.2.0 — write-* 技能族跨 Section 状态传递协议。
  在论文写作过程中持久化各 Section 的 metadata，使下游技能能自动消费上游输出，
  代替当前"用户手动复制 theory_hints YAML"的断裂。
version: 1.2.0
---

# paper-state.yaml — Write-* 跨 Section 状态传递协议

## 1. 设计问题

当前 4 个 write-* 技能（Introduction/Theory/Methods/Results）各自声明了
下游接口，但实际传输依赖用户手动复制。写 Introduction 时输出的 theory_hints
YAML 到了写 Theory 时需要用户回忆并重新输入。

**paper-state.yaml 是整个飞轮的脊椎**——一个轻量状态文件，每个 write-* 技能
在启动时读取，在完成时写入。一次创建，四个 section 共享。

## 1.1 权威边界（避免双头权威）

本文件不是论文状态的唯一权威。以下字段各有唯一权威来源，本文件不重复定义：

- **canonical `story`**（theme question、central knot、characters、storylines、
  stage、evidence state）：以 `paper-story-contract/references/schema.md` 为
  唯一权威。本协议中的 `introduction.theory_hints.central_knot_statement`
  为 **legacy 字段**——新项目直接写 canonical `story`；旧项目已有该字段时，
  按 schema.md 迁移并标记 `provisional`。
- **诊断输出接口**（`diagnostic_schema_version`、`gbl_four_moves` 等）：以
  `diagnose-introduction/SKILL.md` 的「输出接口契约」为准。这些字段是
  Skill 间传输格式，**不写入** paper-state.yaml。
- 本文件的权威范围：四个 Section 的 status / output_path / theory_hints /
  constructs / hypotheses / variables / hypothesis_results 等**写作链
  metadata**，以及 §5 的 Vault 检索协议。

## 2. 文件位置与发现

| 优先级 | 发现方式 |
|--------|---------|
| 1 | `--paper-state=<path>` 命令行参数 |
| 2 | 当前工作目录下的 `paper-state.yaml` |
| 3 | 项目根目录下的 `paper-state.yaml` |
| 4 | 未找到 → 技能正常执行，手动收集上游信息（当前行为，不降级） |

**建议约定**：每个论文项目在自己的输出目录放一个 `paper-state.yaml`，
如 `outputs/ceo-rf-recall/paper-state.yaml`。

## 3. Schema

```yaml
# ============================================================
# paper-state.yaml v1.2.0
# ============================================================
# 字段按 section 分组。每个 section 的核心作用是：
#   上游 section 完成后填充自己的 metadata
#   下游 section 启动时读取上游 metadata
#   人工也可以随时手动编辑（YAML 可读）
# 注意：canonical story 字段以 paper-story-contract/references/schema.md 为准（见 §1.1）

paper:
  id: "ceo-regulatory-focus-recall-timing"   # 唯一标识，kebab-case
  title: "CEO Regulatory Focus and Time to Recall"  # 论文标题
  target_journal: "AMJ"                       # 目标期刊（影响 Hook 风格、结构等）
  created: 2026-07-08
  updated: 2026-07-08

  # --- Vault 知识库连接（供 write-* Phase 0 Vault 检索步骤使用）---
  vault:
    war_room: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/项目作战室 - CEO regulatory focus × time to recall.md"
    section_evidence_map: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/章节-证据映射 - CEO regulatory focus × time to recall.md"
    evidence_pack: "00 工作台/项目/CEO regulatory focus × time to recall/00 Active/文献证据包 - CEO regulatory focus × time to recall.md"
    claim_cards_tag: "CEO regulatory focus × time to recall"   # 论证卡库中与此项目关联的 tag
    # 以上路径均为 Vault 内相对路径。若项目不在此层级结构或使用不同文件名，修改即可。
    # 若项目尚未建立这些资产，字段为 null，write-* 回退到 Vault 全文搜索（较慢但仍有价值）。

# ============================================================
# Section 1: Introduction
# 生产者: write-introduction / diagnose-introduction
# 消费者: write-theory (Phase 0), paper-review/pollock-qc (承诺-兑现对齐)
# ============================================================
introduction:
  status: drafted               # pending | drafted | reviewed | final
  output_path: "outputs/intro_v3.md"
  updated: 2026-07-05

  # --- theory_hints: 供 write-theory Phase 0 自动读取 ---
  theory_hints:
    gap_type: "Inadequacy"                   # Incompleteness | Inadequacy | Incommensurability
    makadok_dimension: "Mechanism"           # Constructs | Mechanism | Boundary | Phenomenon | Level | Mode | Question | Output
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    central_knot_statement: "While prior work assumes firms respond to product failures uniformly, we argue that CEO regulatory focus systematically shapes when—not just whether—firms initiate recalls."  # legacy 字段：新项目用 canonical story（见 §1.1）
    narrative_arc: "moderate_rise"           # gentle_rise | moderate_rise | sharp_rise
    core_constructs: ["CEO regulatory focus", "time to recall"]

  # --- contribution_contract: 供 paper-review/pollock-qc 承诺-兑现对齐 ---
  contribution_contract:
    - claim: "We explain why CEO regulatory focus affects time to recall by identifying two timing-error weighting mechanisms."
      makadok_dimension: "Mechanism"
    - claim: "We introduce regulatory focus as a novel predictor of recall timing, extending the literature beyond governance and operational antecedents."
      makadok_dimension: "Constructs"

# ============================================================
# Section 2: Theory & Hypotheses
# 生产者: write-theory
# 消费者: write-methods (变量对齐), write-results (假设-结果对齐), paper-review/discussion-review (已有草稿的理论贡献锚点)
# ============================================================
theory:
  status: pending               # pending | drafted | reviewed | final
  output_path: null
  depends_on: ["introduction"]   # 上游 section 必须 completed 才能启动
  updated: null

  theory_variant: null           # 从 write-theory Phase 0 输出
  institutional_background_included: false

  # --- constructs: 供 write-methods M1-M4 变量操作化 ---
  constructs:
    independent: null            # 如 "CEO promotion focus"
    dependent: null              # 如 "time to recall (days)"
    mediator: null               # 如 "weighting of error type I vs II"
    moderator: null              # 如无可为 null
    controls: []                 # 理论驱动的控制变量

  # --- hypotheses: 供 write-methods 假设-变量映射 + write-results 假设-结果对齐 ---
  hypotheses:
    - id: "H1"
      storyline_id: "S1"         # 对齐 story.storylines[*].id（paper-story-contract 定义的 Section Extension，write-methods/write-results 消费）
      statement: null            # "CEO promotion focus is negatively associated with time to recall."
      type: "main"               # main | mediation | moderation | competition
      iv: null
      dv: null
      predicted_direction: "negative"
    # - id: "H2"
    #   statement: null
    #   type: "main"
    #   iv: null
    #   dv: null
    #   predicted_direction: "positive"

  # --- mechanism_chains: 供 paper-review/discussion-review 检查理论贡献兑现 ---
  mechanism_chains: []

# ============================================================
# Section 3: Methods
# 生产者: write-methods
# 消费者: write-results (模型规格、变量名)
# ============================================================
methods:
  status: pending
  output_path: null
  depends_on: ["theory"]
  updated: null

  design_type: null              # 面板数据/OLS | 自然实验/DiD | 生存分析 | ...
  estimator_family: null         # OLS | FE | Logit | Cox | DiD | IV/2SLS | ...
  sample:
    source: null                 # 数据来源描述
    n_observations: null
    n_firms: null
    time_window: null
    inclusion_criteria: []

  # --- variables: 供 write-results 槽位报告 ---
  variables:
    dv: null                      # 因变量名（如 time_to_recall_days）
    iv: null                      # 核心自变量名（如 ceo_promotion_focus）
    mediator: null                # 中介变量名
    moderator: null               # 调节变量名
    controls: []                  # 控制变量列表
    fixed_effects: []             # 固定效应（如 firm, year）

  # --- hypothesis_variable_map: 供 write-results R3 槽位 ---
  hypothesis_variable_map:
    H1: {predictor: null, outcome: null, model: null}
    # H2: {predictor: null, outcome: null, model: null}

  # --- results_preview: Methods M10 段的预告（供 write-results 预期管理）---
  results_preview: null

# ============================================================
# Section 4: Results
# 生产者: write-results
# 消费者: paper-review/pollock-qc；如用户已有 Discussion 草稿，可供 discussion-review 检查主要发现与意外发现是否被正确解释
# ============================================================
results:
  status: pending
  output_path: null
  depends_on: ["methods"]
  updated: null

  estimator_family: null          # 确认的估计器

  # --- hypothesis_results: 供 Results story_resolution 与全稿审查 ---
  hypothesis_results:
    H1: {direction: null, significant: null, supported: null}
    # H2: {direction: null, significant: null, supported: null}

  # --- key_findings: 供全稿审查；已有 Discussion 草稿时供 discussion-review 对照 ---
  key_findings: []
  unexpected_findings: []         # 意外/反直觉发现

# ============================================================
# Discussion — 仅保留兼容占位；标准化写作链不生成 Discussion
# ============================================================
# discussion:
#   status: skipped
#   ...

# ============================================================
# 跨 Section 对齐追踪
# ============================================================
cross_section_alignment:
  intro_theory:
    status: unchecked             # unchecked | checked_ok | checked_conflict
    checked_at: null
    notes: null
  theory_methods:
    status: unchecked
    checked_at: null
    notes: null
  methods_results:
    status: unchecked
    checked_at: null
    notes: null
  intro_discussion:
    status: skipped               # Discussion 暂不激活
    checked_at: null
    notes: null
```

## 4. 工作流

### 4.1 write-introduction 完成后

用户在 write-introduction 输出末尾收到以下追加块：

```yaml
# --- paper-state.yaml 片段（复制到你的 paper-state.yaml）---
introduction:
  status: drafted
  output_path: "outputs/intro_v3.md"
  theory_hints:
    gap_type: "Inadequacy"
    makadok_dimension: "Mechanism"
    tension_template: "06-theoretical-imbalance"
    recommended_theory_variant: "机制推演型 (B)"
    promised_hypothesis_count: 2
    promised_boundary_conditions: false
    promised_mechanism_steps: 2
    central_knot_statement: "..."
    narrative_arc: "moderate_rise"
    core_constructs: ["CEO regulatory focus", "time to recall"]
  contribution_contract:
    - claim: "..."
      makadok_dimension: "Mechanism"
```

用户复制到 paper-state.yaml 中（或用 `--paper-state` 参数指向该文件时自动填充）。

### 4.2 write-theory 启动时

Phase 0 增加自动检查：

```
[paper-state.yaml] 检测到 paper-state.yaml
  → introduction.status = drafted
  → 自动加载 theory_hints:
      gap_type: Inadequacy
      recommended_theory_variant: 机制推演型 (B)
      promised_hypothesis_count: 2
  → 跳过交互式类型诊断，直接进入确认模式
  → 默认推荐: 机制推演型 (B)
  → 用户只需确认或调整
```

如果 paper-state.yaml 不存在：回退到交互式询问（当前行为）。

### 4.3 write-theory 完成后

输出追加 paper-state.yaml 片段：

```yaml
theory:
  status: drafted
  output_path: "outputs/theory_v2.md"
  theory_variant: "机制推演型 (B)"
  constructs:
    independent: "CEO promotion focus"
    dependent: "time to recall (days)"
    mediator: "weighting of timing error type I (premature recall)"
    moderator: null
    controls: ["firm size", "ROA", "leverage", "board independence"]
  hypotheses:
    - id: "H1"
      storyline_id: "S1"
      statement: "CEO promotion focus is negatively associated with time to recall."
      type: "main"
      predicted_direction: "negative"
    - id: "H2"
      storyline_id: "S1"
      statement: "CEO prevention focus is positively associated with time to recall."
      type: "main"
      predicted_direction: "positive"
  mechanism_chains:
    - "promotion focus → sensitivity to opportunity costs of delay → overweighting type I error (premature recall) → shorter time to recall"
    - "prevention focus → sensitivity to reputational costs of error → overweighting type II error (delayed recall) → longer time to recall"
```

### 4.4 write-methods 启动时

Phase 0 自动从 paper-state.yaml 读取 `theory.hypotheses` 和 `theory.constructs`，
构建假设-变量映射表，不再要求用户手动输入假设列表。

### 4.5 write-results 启动时

Phase 0 自动从 paper-state.yaml 读取：
- `methods.estimator_family` → 推荐结果类型
- `methods.hypothesis_variable_map` → 构建假设-结果对齐表
- `theory.hypotheses` → 建立 Hypothesis-Result Fulfillment Map

## 5. Vault 知识检索协议（LOOP 5: Vault → Write Evidence）

### 5.1 设计问题

paper-state.yaml 解决的是 write-* 技能之间的 metadata 传递，但不解决**写作时如何调取 Vault 中 1800+ 笔记的文献弹药**。

当前用户在写 Theory 时需要手动回忆：哪个 Claim Card 支持这条机制？哪篇 canonical 笔记有理论桥接？哪个 rival mechanism 需要区分？

**Vault 检索协议**让 write-* 技能在启动时自动从 Vault 拉取当前 Section 相关的文献资产。

### 5.2 发现机制（三级回退）

write-introduction 和 write-theory 的 Phase 0 在检查 paper-state.yaml 后，执行 Vault 检索：

```
paper-state.yaml 中有 vault.section_evidence_map?
│
├── YES → 读 章节-证据映射
│   → 按 Section 过滤相关行（如 write-theory → filter "Theory" + "T" rows）
│   → 提取: citation key, 命题, Vault note path, 证据用途
│   → 生成 "Vault Knowledge Brief"（结构化文献摘要）
│
├── YES 路径存在但文件不可读 → 继续下一级
│
├── paper-state.yaml 中有 paper.vault.war_room?
│   → 读项目作战室 → 找 canonical handle buckets 和文献分组
│   → fallback：Vault 全文搜索 paper.title 或 core_constructs
│
└── 全部不可用 → 跳过 Vault 检索（当前行为，不降级）
```

### 5.3 Vault Knowledge Brief 格式

检索后在 Phase 0 诊断输出中附加以下简报：

```markdown
## Vault 知识简报（[Section]）

### 核心文献（来自 章节-证据映射）
| 命题 | Citation Key | 证据用途 | Vault Note |
|------|-------------|---------|-----------|
| T1 | @JohnsonEtAl2015 | 理论定义 / 机制核心 | [[johnsonetal2015...]] |
| T2 | @YoonEtAl2012 | 微观过程 / H1 机制支撑 | [[yoonetal2012...]] |

### 机制 Claim Cards（来自 论证卡库）
- [[Claim - ...]]: [一句话概括——来自 Vault 论证卡库，与本文理论假设相关的 claim card]
- [[Claim - ...]]: [同上]

### Rival Mechanisms 需区分
- vs. [rival_mechanism_1]: [区分策略——从 war_room rival anchors 提取]
- vs. [rival_mechanism_2]: [区分策略]

### 概念锚点（来自 概念库/）
- [[概念 - ...]]: [一句话概括与本文理论的关联]
- [[概念 - ...]]: [同上]

### 证据完整度
- Vault 检索命中: [N] 篇 canonical notes + [M] 条 claim cards
- 建议补读: [列出可能从 Tier 1 补读的关键文献]
```

### 5.4 Section 特化

| Section | Vault 检索重点 | 关键 Vault 资产 |
|---------|---------------|----------------|
| **Introduction** | Hook 数据点、Gap 锚定文献、Literature Turn 引文簇 | 章节-证据映射 Introduction rows、项目领域文献地图（如有）、gap anchors |
| **Theory** | 机制证据卡片、Rival mechanism 区分、概念定义、边界条件文献 | 章节-证据映射 Theory rows、论证卡库 Claim Cards、canonical notes、概念库/ |
| **Methods** | 识别策略先例、变量操作化参照、关键变量防守文献 | 章节-证据映射 Methods rows、数据集/变量 note |
| **Results** | 贡献定位锚点、rival explanation 区分文献 | 章节-证据映射 Results/Discussion rows |

### 5.5 纪律

- Vault Knowledge Brief 是**检索摘要**，不是全文复制。每条 ~1 行概括 + Vault note link
- 用户阅读 Brief 后可说 "读那 3 篇" 来展开深读
- Brief 不替代 template 生成——它提供的是**内容弹药**，template 提供的是**结构骨架**
- 若 Vault 检索无结果（项目太新、笔记未建），不在 Brief 中编造
- 检索到但 paper-state.yaml 中未列的 citation key → 标注为 "Vault 候选，待确认是否纳入"

## 6. 版本兼容

- v1.2.0 `theory.hypotheses[*]` 新增 `storyline_id` 字段（对齐
  `paper-story-contract/references/schema.md` 定义的 Section Extension
  `theory.hypotheses[*].storyline_id`，供 write-methods / write-results 消费）。
  此前该字段被 write-theory 输出但未在权威 schema 登记，造成双头权威风险
- v1.1.0 新增 Vault 知识检索协议（§5）；明确权威边界（§1.1）：canonical
  `story` 归 `paper-story-contract/references/schema.md`，诊断接口字段归
  `diagnose-introduction/SKILL.md`，本文件只管写作链 metadata
- v1.0.0 覆盖 Introduction → Theory → Methods → Results 四段
- Discussion 字段在 schema 中保留但标记 `skipped`；标准化 Pollock 写作链不生成 Discussion，已有草稿只进入 `discussion-review`
- 各 `metadata` 和 `theory_hints` 字段跟随对应 write-* 技能版本演进
- 向后兼容：任何字段可为 `null`，下游技能检测到 `null` 时回退到交互式询问

## 7. 纪律

- paper-state.yaml **只记录 metadata，不替代各 section 的完整输出**
- 每个 section 的输出路径记录在 `output_path`，全文存在对应文件中
- paper-state.yaml 随时可手动编辑（YAML 纯文本）
- 建议和 section 文件一起做版本管理（Git）
- cross_section_alignment 在每次运行对齐检查后更新
