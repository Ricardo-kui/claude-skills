# Phase 4 — 技能更新指令生成（Skill Update Instructions）

> **写回前必跑预检（2026-08-20 起）**：候选骨架定稿后、读取任何语料前，运行
> `python ../distill-paper-exemplar/scripts/corpus_precheck.py --section <本节名> --citekey <citekey> --candidates <candidates.yaml>`
> 产出 writeback plan（选带判定 + jaccard/containment 查重 + registry 定点匹配 + insert_after 锚点）。
> **禁止为查重/选带/锚点定位而整读 corpus 或 `_evidence_registry.yaml`**（单个文件可达 54–257KB）——
> 一切以 plan 为准；仅当 plan 的 verdict 可疑时，才允许按 plan 标注的文件+行号定点核对。
>
> candidates.yaml 格式：
> ```yaml
> candidates:
>   - name: <skeleton_id>
>     target: "<目标文件或目录提示，如 OLS-FE.md / tensions>"
>     skeleton_text: "<骨架模板文本（查重输入）>"
>     keywords: ["<registry 匹配关键词，可选>"]
> ```
>
> **--auto-write**：默认仍需 gate ① 人审确认 plan 后写回；调用方显式传 `--auto-write`
> （或批量模式用户预先授权）时，可按 plan 直接写回 ADD/EXTEND 项（**SKIP 项永不写回**），
> 并在写回报告中标注 `auto-write: plan <plan路径>`。
>
> **整篇编排模式（distill-paper-exemplar 分发）下**：plan 产出即停，把 plan 路径交回
> 主循环等待批量 gate ①（四节攒齐一次呈审），不要自行进入写回；单节模式随产随审。
>
> **写回执行（gate ① 确认后，2026-08-20 起）**：用确定性执行器，不手改语料——
> `python ../distill-paper-exemplar/scripts/corpus_writeback.py --plan <plan> --paper <citekey> --journal <刊名> --gap <Gap类型>`（block_text/index_note 已在 candidates.yaml 写一遍并透传进 plan，无需 blocks.yaml）
> 默认 dry-run 打印全部 diff 供复核，`--apply` 才落盘（插块自动续 `{NEXT}` 编号、
> _index 行注、registry 计数、SKIP 拒绝）。gate ① 改判锚点文件时在 blocks.yaml 加
> `file:` 覆盖。完整 blocks.yaml 格式见
> `../../distill-introduction-exemplar/references/phase-4-validation-writeback.md` 头部。

本阶段生成**受治理的 adoption instructions**。输出回答三个问题：
1. **改哪个文件** → 精确到 `write-methods/econometric-models/[设计类型].md`
2. **怎么改** → ADD / EXTEND / REPLACE / SKIP，含具体骨架和插入位置
3. **为什么** → 与当前 corpus 的差异 + 对 write-methods skill 的提升

## skill_update_instructions 格式

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

## 写入后操作（两段式：预览 → 确认 → 写入）

**原则：所有待写入内容必须先展示给用户评估，用户确认后才写入。不自动写入任何变体。**

### Step 1 — 写入预览（Preview）

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

### Step 2 — 评估确认（Gate）

用户明确表态后才执行写入。默认确认粒度：
- **单篇模式**：逐个确认——用户可指出哪条不写、哪条需修改（修改后重新展示）。
- **批量模式（--batch）**：一次确认写入全部 `ADD/EXTEND`；`REPLACE` 仍逐个确认（替换是破坏性动作）。
- 用户说"全部写入"即跳过剩余逐个确认。

确认后的写入步骤不变：打开 `target_file` → 按 `insert_after` 插入 → 更新 `source_papers` / `variants_count` / `updated` → 对 `new_anti_patterns_for_skill` 写入「反模式」段落 → 更新 `INDEX.md` 表行和「已填充变体」计数 → **更新文件顶部「变体速查表」**（新变体行 + 槽位分布总览，`区别` 列直接取 `distinct_from`；速查表与正文变体必须同步，quality_check 会校验）。

**旧变体锚点回填**：`REPLACE`/`EXTEND` 触碰已有变体且该变体缺 `原始句锚点` 时，按上述锚点来源检索规则**顺带补锚点**（检索不到原文则标"待补"，不阻塞写入）。

### 评估清单（供用户参考）

- [ ] 骨架无机构名/政策名/数据库名残留（[placeholder] 泛化彻底）
- [ ] 与已有变体不重复（Phase 3 新颖度成立）
- [ ] 骨架填入实际内容后能产出顶刊风格段落（可生成性）
- [ ] **原始句锚点保留原文风味**（生成时可据此校准"顶刊味道"；锚点非复制源）
- [ ] 因果语言强度与设计类型匹配
- [ ] 符合你的写作习惯与当前论文需要

`core_candidate`、单篇证据，或任何 `skill_main_skeleton_update` 只生成显式人工审核包——同样先展示后由用户决定；不得自动修改 SKILL.md、路由、强制槽位顺序、story schema 或 stage gate。

## 批评登记（critique-driven stats）

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

## Phase 4 收尾 — 回写后语料体检

回写完成后运行 skills 根目录的体检脚本：

```bash
PYTHONIOENCODING=utf-8 python ~/.claude/skills/corpus_health_check.py --type methods
```

- exit 0 = 正常；exit 1 = 存在 critique_heavy 类型——在输出中列出这些类型，作为下一轮蒸馏 REPLACE/EXTEND 的优先级依据。
- 脚本缺失或运行失败不阻断回写，但必须在输出中声明"体检未执行"，不得静默跳过。
