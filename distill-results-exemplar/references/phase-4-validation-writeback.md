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

本阶段生成**受治理的 adoption instructions**，回答三个问题：
1. **改哪个文件** → 精确到 `write-results/econometric-models/[结果类型].md`
2. **怎么改** → ADD / EXTEND / REPLACE / SKIP，含具体骨架和插入位置
3. **为什么** → 与当前 corpus 的差异 + 对 write-results skill 的提升

## skill_update_instructions 格式

```yaml
phase_4_skill_update_instructions:
  - action: "ADD"
    story_fidelity_classification: "section_variant"
    target_file: "生存分析.md"
    target_slot: "R3"
    insert_after: "变体 5（事件研究 CAR 第二阶段）"  # 语义定位
    distinct_from: "变体 5（事件研究 CAR 第二阶段）— 本变体是 exp(β)−1 百分比三拍，变体 5 是 exponentiated beta 双拍"  # ADD/EXTEND 必填：与最近变体的一句差异，写入速查表「区别」列
    skeleton: "..."
    verbatim_anchor: "The hazard ratio of [x] indicates that a one-unit increase in [predictor] is associated with a [value]% decrease in the rate of [event] (p < .01)."  # 来源论文原句 1–2 句，15–40 tokens，风格参照
    reason: "当前 生存分析 R3 变体1-5 全部是 AFT 的 exponentiated beta 解释。本论文展示了指数风险模型的 exp(β)−1 百分比三拍节奏，填补了参数风险模型 R3 的空白。"
    source_paper: "Mayo_Ball_Mills_2022_POM"

  new_anti_patterns_for_skill:
    - target_file: "OLS-FE.md"
      slot: "R7"
      pattern: "稳健性按表格机械罗列而不按威胁组织"

  new_honesty_boundaries_for_skill:
    - target_file: "计数模型.md"
      boundary: "分样本 H3 的 null-in-one-subgroup 只有在分样本基于理论驱动时才可解释为确证性证据"

  skill_main_skeleton_update: []
```

## 写入后操作（两段式：预览 → 确认 → 写入）

**原则：所有待写入内容必须先展示给用户评估，用户确认后才写入。不自动写入任何变体。**

### Step 1 — 写入预览（Preview）

Phase 4 输出的每条 `action != SKIP` 指令渲染为「待写入预览块」，随蒸馏报告一起输出：

```markdown
### 待写入 #N：[action] → [target_file] [slot]（[skeleton_id]）
- **来源论文**: [source_paper]
- **插入位置**: [insert_after / 同 slot 变体列表中的位置]
- **区别于**: [distinct_from——确认与最近变体的一句区分是否准确]
- **理由**: [reason]
- **原始句锚点**: [verbatim_anchor 原句展示——风格参照，评估风味是否地道]
- **骨架全文**:
  [skeleton 逐字展示，不摘要]
- **评估要点**: [该变体应满足的标准，如"四拍完整"、"无系数残留"、"填入实际结果后可产出顶刊风格段落"]
```

- 预览块必须展示**骨架全文**，不是摘要。
- `REPLACE` 额外给出「旧变体 vs 新变体」并排对比，标注被替换的 skeleton_id。

### Step 2 — 评估确认（Gate）

用户明确表态后才执行写入。默认确认粒度：
- **单篇模式**：逐个确认——用户可指出哪条不写、哪条需修改（修改后重新展示）。
- **批量模式（--batch）**：一次确认写入全部 `ADD/EXTEND`；`REPLACE` 仍逐个确认（替换是破坏性动作）。
- 用户说"全部写入"即跳过剩余逐个确认。

确认后的写入步骤不变：按 Phase 4 指令执行写入并更新索引、计数，**并同步更新目标文件顶部「变体速查表」**（新变体行 + 槽位分布总览，`区别` 列直接取 `distinct_from`；速查表与正文变体必须同步，quality_check 会校验）。

**旧变体锚点回填**：`REPLACE`/`EXTEND` 触碰已有变体且该变体缺 `原始句锚点` 时，按上述锚点来源检索规则**顺带补锚点**（检索不到原文则标"待补"，不阻塞写入）。

### 评估清单（供用户参考）

- [ ] 骨架无具体系数/p 值/表格编号残留（[placeholder] 泛化彻底）
- [ ] 与已有变体不重复（Phase 3 新颖度成立）
- [ ] 四拍节奏完整（方向→显著性→幅度→支持判断）
- [ ] **原始句锚点保留原文风味**（生成时可据此校准"顶刊味道"；锚点非复制源）
- [ ] 非显著假设的句式处理符合你的报告习惯
- [ ] 符合你的写作习惯与当前论文需要

`core_candidate`、单篇证据及任何核心骨架、路由、强制槽位顺序、story schema 或 stage gate 变更只生成显式人工审核包——同样先展示后由用户决定，不自动执行。

## 批评登记（critique-driven stats）

登记来源 = **Claude 在 write-results 会话中自动捕获用户批评**（见 write-results SKILL.md 批评登记），用户零动作；批量补登可用：

```bash
python _update_registry.py --record-critique critiques.yaml
```

`critiques.yaml` 格式：

```yaml
critique_updates:
  - estimator_family: "OLS_FE"   # registry estimators 中的键名
    verdict: "revise"            # revise=需大改 / reject=被弃用重写
    reason: "R3 经济显著性段落缺少幅度翻译"   # 进入 common_revise_reasons，精炼直接依据
    date: "YYYY-MM-DD"           # 可选，默认今天
```

- 脚本累加 `revise/reject`、更新 `last_critique`、去重追加 `common_revise_reasons`（最多 8 条），输出信号（quiet/critique_heavy）供下一轮 Phase 0.75 选材。
- 不登记满意信号、不设淘汰逻辑——语义见 registry `meta.usage_stats_schema`。

## Phase 4 收尾 — 回写后语料体检

回写完成后运行 skills 根目录的体检脚本：

```bash
PYTHONIOENCODING=utf-8 python ~/.claude/skills/corpus_health_check.py --type results
```

- exit 0 = 正常；exit 1 = 存在 critique_heavy 类型——在输出中列出这些类型，作为下一轮蒸馏 REPLACE/EXTEND 的优先级依据。
- 脚本缺失或运行失败不阻断回写，但必须在输出中声明"体检未执行"，不得静默跳过。
