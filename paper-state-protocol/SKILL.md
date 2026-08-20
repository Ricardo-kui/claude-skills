---
disableModelInvocation: true
name: paper-state-protocol
description: "paper-state.yaml 协议 v1.2.0——write-* 技能族跨 Section 状态传递规范：在论文写作过程中持久化各 Section 的 metadata（theory_hints、构念、假设、变量、假设结果），使下游技能自动消费上游输出。触发词：paper-state、状态传递、跨 section 状态。"
whenToUse: "当需要创建、读取、更新或审计项目的 paper-state.yaml，让 write-introduction/write-theory/write-methods/write-results 之间自动传递 theory_hints、构念、假设、变量等写作链状态时使用。触发词：paper-state、paper-state.yaml、状态文件、跨 section 传递、上下游衔接、状态同步、写作状态持久化"
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

四段结构：`paper`（项目标识 + Vault 连接）→ `introduction`（theory_hints + contribution_contract）→ `theory`（constructs + hypotheses + mechanism_chains）→ `methods`（variables + hypothesis_variable_map）→ `results`（hypothesis_results + key_findings）+ `cross_section_alignment` 追踪。每段标注生产者/消费者；任何字段可为 `null`，下游回退交互式询问。

→ 完整权威 schema（逐字段注释）：`references/schema.md`

## 4. 工作流

| 时机 | 行为 |
|------|------|
| write-introduction 完成后 | 输出末尾追加 `introduction:` 片段（theory_hints + contribution_contract），用户复制或 `--paper-state` 自动填充 |
| write-theory 启动时 | Phase 0 检测 paper-state.yaml → 自动加载 theory_hints，跳过交互式类型诊断进入确认模式；文件缺失回退交互式询问（当前行为） |
| write-theory 完成后 | 输出追加 `theory:` 片段（variant + constructs + hypotheses + mechanism_chains） |
| write-methods 启动时 | Phase 0 自动读取 `theory.hypotheses` 和 `theory.constructs`，构建假设-变量映射表，不再要求用户手动输入假设列表 |
| write-results 启动时 | Phase 0 自动读取：`methods.estimator_family` → 推荐结果类型；`methods.hypothesis_variable_map` → 假设-结果对齐表；`theory.hypotheses` → Hypothesis-Result Fulfillment Map |

→ 各片段的完整 YAML 示例与启动检查输出：`references/workflow-fragments.md`

## 5. Vault 知识检索协议（LOOP 5: Vault → Write Evidence）

paper-state.yaml 解决 write-* 技能之间的 metadata 传递；**Vault 检索协议**解决写作时如何调取 Vault 中 1800+ 笔记的文献弹药——write-introduction 和 write-theory 的 Phase 0 在检查 paper-state.yaml 后执行三级回退检索（章节-证据映射 → 项目作战室/全文搜索 → 跳过不降级），产出 **Vault Knowledge Brief**（核心文献表 + Claim Cards + Rival Mechanisms + 概念锚点 + 证据完整度）。

Brief 纪律：检索摘要非全文复制（每条 ~1 行 + note link）；提供内容弹药，结构骨架仍由 template 提供；检索无结果时不编造。

→ 发现机制树、Brief 格式模板、Section 特化表、完整纪律：`references/vault-retrieval.md`

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
