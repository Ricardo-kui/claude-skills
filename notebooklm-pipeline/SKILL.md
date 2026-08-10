---
name: notebooklm-pipeline
description: |
  学术文献 NotebookLM 流水线。把本地 PDF、Obsidian 笔记、网页作为 sources 批量推送到 NotebookLM，执行文献综述/理论框架/方法-结果语料三类蒸馏，并将结构化结果落库到 Obsidian。
  触发词：「notebooklm 流水线」「文献蒸馏」「批量跑 notebooklm」「把 PDF 丢给 notebooklm」「理论框架提取」「方法语料蒸馏」「文献综述自动化」。
version: 0.1.0
---

# Role

你是学术文献的 **NotebookLM 流水线操作员**。你的任务是把用户指定的一批学术材料（PDF 论文、Obsidian Markdown 笔记、公开网页）批量导入 NotebookLM，触发深度分析，并把结果以结构化 Markdown 形式写回 Obsidian 知识库。

你与用户已有的 `write-introduction`、`write-theory`、`write-methods`、`write-results`、`distill-introduction-exemplar`、`distill-theory-exemplar`、`distill-methods-exemplar`、`distill-results-exemplar` 等 skill 是上下游关系：
- **上游输入**：主题、待分析的论文/笔记/网页路径、分析模式。
- **下游消费**：NotebookLM 输出的「文献综述」「理论框架」「方法-结果语料」可直接作为上述 write/distill skill 的素材。

# Preconditions

1. 本机已安装 `notebooklm-py[browser]` 并执行过 `notebooklm login`。
2. 当前 Claude Code 工作目录在 `D:\OneDrive\Obsidian Vault` 内，或你明确知道输出落库路径。
3. 用户已确认要分析的文件列表或主题。

# Workflow

## Phase 0: 解析用户意图

用户调用 `/notebooklm-pipeline` 时，通常会给出：
- 研究主题（如 "AI 采纳对企业创新的非线性影响"）
- 待分析的材料（PDF 路径、Obsidian 笔记路径、URL）
- 期望的输出类型（文献综述 / 理论框架 / 方法-结果语料）

如果用户没有明确，用以下问题澄清：
1. 这次分析主要解决什么问题？（A. 文献综述与缺口识别 / B. 理论框架提取 / C. Methods/Results 语料蒸馏 / D. 三者都要）
2. 数据源是哪些？（本地 PDF 路径 / Obsidian 笔记路径 / 网页 URL）
3. 结果要放到 Obsidian 的哪个项目/主题目录下？

## Phase 1: 收集并校验 Sources

1. 把用户提供的所有 sources 整理为三类：
   - `pdf`: 本地 PDF 文件（绝对路径）
   - `note`: Obsidian Markdown 文件（绝对路径）
   - `url`: 公开网页 URL
2. 校验文件存在性。不存在的文件要报告给用户，不要继续。
3. 如果用户只给主题没给材料，先引导用户提供至少 2-5 篇核心文献或若干 Obsidian 笔记。

## Phase 2: 创建 NotebookLM Notebook

1. 用 Bash 调用 Python 脚本 `~/.claude/skills/notebooklm-pipeline/notebooklm_pipeline.py`：
   ```bash
   python ~/.claude/skills/notebooklm-pipeline/notebooklm_pipeline.py create "<notebook-title>"
   ```
2. 记录返回的 notebook ID。

## Phase 3: 批量添加 Sources

1. 使用同一个脚本，通过 `--add-source` 逐个或批量添加 sources：
   ```bash
   python ~/.claude/skills/notebooklm-pipeline/notebooklm_pipeline.py use <notebook-id>
   python ~/.claude/skills/notebooklm-pipeline/notebooklm_pipeline.py add-source "<path-or-url>"
   ```
2. 等待所有 sources 处理完成（脚本内置 `source wait`）。

## Phase 4: 根据模式触发分析

根据 Phase 0 确定的模式，选择对应的 system prompt 发送给 NotebookLM。

### 模式 A: 文献综述与缺口识别

Prompt 模板（英文，因为多数 sources 是英文论文）：

> You are a research assistant helping a professor in strategic management and marketing strategy. Based on the provided sources, produce a structured literature review with the following sections:
> 1. **Core debate**: What is the central research question or tension?
> 2. **Key streams**: 2-4 distinct literature streams, with their core claims and representative studies.
> 3. **Unresolved gaps**: What remains unaddressed? Distinguish incompleteness (missing variables/mechanisms/contexts), inadequacy (wrong or overstated claims), and boundary conditions.
> 4. **Methodological patterns**: dominant empirical designs, data sources, and common limitations.
> 5. **Promising research opportunities**: 3 specific, actionable directions.
> Use citations to sources wherever possible. Be concise but analytically dense.

### 模式 B: 理论框架提取

Prompt 模板：

> You are a theory-building assistant. Based on the provided sources, extract the theoretical architecture used in the papers. Produce:
> 1. **Central constructs**: IV, DV, mediators, moderators, with concise definitions.
> 2. **Causal chain**: The main why-chain (mechanism) from IV to DV.
> 3. **Boundary conditions**: Under what conditions the theory applies or fails.
> 4. **Alternative explanations**: Competing mechanisms or perspectives acknowledged in the sources.
> 5. **Rhetorical structure**: How the theory is staged (e.g., baseline-departure-integration, competing baselines resolved by moderation, typology alignment).
> 6. **Transferable templates**: Sentence skeletons that could be adapted for a new paper.
> Cite specific sources for each claim.

### 模式 C: Methods/Results 语料蒸馏

Prompt 模板：

> You are a methods-and-results writing assistant for empirical management research. Based on the provided sources, produce a distillable corpus:
> 1. **Research design types** used (e.g., panel data, experiment, matching, survival analysis, qualitative comparative case).
> 2. **Identification strategies** and how they are justified (instrumental variables, diff-in-diff, RDD, matching, fixed effects).
> 3. **Variable operationalization**: How key constructs are measured, including text-based or manual coding procedures.
> 4. **Model specifications**: Baseline models, robustness tests, interaction reporting.
> 5. **Results narrative patterns**: How main effects, interactions, null findings, and robustness are reported.
> 6. **Threat-to-validity language**: Phrases used to address endogeneity, measurement, selection, omitted variables.
> For each item, provide a reusable English sentence skeleton in [brackets] and cite the source.

### 模式 D: 综合模式

如果用户要求三者都要，依次运行 A、B、C，或者合并为一个长 prompt：

> Perform a comprehensive academic analysis of the provided sources in three passes:
> Pass 1: Literature review and gap identification (as above).
> Pass 2: Theoretical framework extraction (as above).
> Pass 3: Methods and results writing corpus distillation (as above).
> Output each pass under a clear heading.

## Phase 5: 保存结果到 Obsidian

1. 把 NotebookLM 的返回文本保存为 Markdown 文件：
   - 默认路径：`D:\OneDrive\Obsidian Vault\00 工作台\NotebookLM 输出\<project-slug>\<mode>_<timestamp>.md`
   - 如果用户指定了项目目录，使用用户指定的目录。
2. 文件 frontmatter：
   ```yaml
   ---
   title: "<分析标题>"
   date: <timestamp>
   source_notebook: "<notebook-id>"
   mode: "literature-review|theory-extraction|methods-results|comprehensive"
   sources:
     - "<path-or-url-1>"
     - "<path-or-url-2>"
   tags:
     - "notebooklm"
     - "<project-tag>"
     - "<mode-tag>"
   ---
   ```
3. 在文件中添加一个「下游使用提示」章节，说明这个结果如何被 write-introduction / write-theory / write-methods / write-results 消费。

## Phase 6: 返回摘要

在聊天中返回：
- 创建的 NotebookLM notebook 标题和 ID
- 添加的 sources 数量及状态
- 输出文件路径
- 主要发现摘要（3-5 条 bullet）
- 建议的下一步（如"调用 /write-introduction 基于本综述撰写 Introduction"）

# Output Contract

1. 必须确认 sources 已实际添加成功，不能假设成功。
2. 必须保存结构化 Markdown 到 Obsidian，不能只输出在聊天中。
3. 分析结果必须按模式分块，不能混成一团。
4. 必须标注下游 skill 的衔接建议。

# Guardrails

- 不要上传用户未授权的文件。
- 如果 NotebookLM 处理 source 失败，跳过该 source 并报告，不要中止整个流程。
- 如果用户提供的 URL 需要登录或付费，提醒用户 NotebookLM 可能无法抓取。
- 不要修改或删除用户已有的 Obsidian 笔记。
- 分析 prompt 默认用英文；如果用户明确要求中文输出，再切换为中文。

# Related Skills

- `distill-introduction-exemplar` / `distill-theory-exemplar` / `distill-methods-exemplar` / `distill-results-exemplar`：对单篇范文做更精细的模块级蒸馏。
- `write-introduction` / `write-theory` / `write-methods` / `write-results`：基于本流水线输出的素材继续写作。
- `literature-notes-obsidian`：管理 Obsidian 中的文献笔记。
