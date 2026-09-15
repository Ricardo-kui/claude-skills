# Phase 4 — 技能更新指令生成（Skill Update Instructions）

> **写回前必跑预检（2026-08-20 起）**：候选骨架定稿后、读取任何语料前，运行
> `python ../distill-paper-exemplar/scripts/corpus_precheck.py --section <本节名> --citekey <citekey> --candidates <candidates.yaml>`
> 产出 writeback plan（选带判定 + jaccard/containment 查重 + registry 定点匹配 + insert_after 锚点）。
> **禁止为查重/选带/锚点定位而整读 corpus 或 `_evidence_registry.yaml`**（单个文件可达 54–257KB）——
> 一切以 plan 为准；仅当 plan 的 verdict 可疑时，才允许按 plan 标注的文件+行号定点核对。
>
> **产出格式（2026-09-14 起，单一契约源）**：candidates.yaml 与 writeback plan 的字段结构以
> `../../distill-paper-exemplar/references/l1-subagent-protocol.md` 的「子代理输出契约」与
> 「plan 条目字段契约」为准（执行器 v2：items: / name / dedup.verdict / anchor.file /
> block_text 全文内嵌 / index_note；骨架 block_text 只写这一遍，corpus_precheck 透传进
> plan，无需再写 blocks.yaml）。本 skill 不另立格式。
>
> **--auto-write**：默认仍需 gate ① 人审确认 plan 后写回；调用方显式传 `--auto-write`
> （或批量模式用户预先授权）时，可按 plan 直接写回 ADD/EXTEND 项（**SKIP 项永不写回**），
> 并在写回报告中标注 `auto-write: plan <plan路径>`。
>
> **写回执行权（2026-09-14 起）**：写回权在主循环——整篇编排模式（L1 子代理分发）下
> **子代理一律不得运行 corpus_writeback.py**，plan 产出即停，把 plan 路径交回主循环等待
> 批量 gate ①（四节攒齐一次呈审）；单节独立模式下由主会话在 gate ① 确认（或调用方显式
> `--auto-write` 授权）后调用写回执行器 `corpus_writeback.py`（先 dry-run 复核 diff 再
> `--apply`），不手改语料。

本阶段生成**受治理的 adoption instructions**。输出回答三个问题：
1. **改哪个文件** → 精确到 `write-methods/corpus/[设计类型].md`
2. **怎么改** → ADD / EXTEND / REPLACE / SKIP，含具体骨架和插入位置
3. **为什么** → 与当前 corpus 的差异 + 对 write-methods skill 的提升

## 输出定位（2026-09-14，旧格式退役）

本阶段产出 = writeback plan 候选，格式唯一以头部「产出格式」块为准（执行器 v2）。
历史 `skill_update_instructions` 字段族退役，映射：target_file/target_slot → v2 `anchor.file`
（含 target 提示）；insert_after → `anchor.after_heading`（主题匹配既有标题，禁默认文件尾）；
distinct_from → 并入 `index_note`；skeleton → `block_text` 全文内嵌；verbatim_anchor 遵守
`../../distill-paper-exemplar/references/anchor-rules.md`；reason → `index_note` 一句话特征。
反模式与诚实边界不写进 plan：入 PDM paper_weaknesses 与 story 卡 caveat，由主循环处置。

## 写入后操作（两段式：预览 → 确认 → 写入）

**原则：所有待写入内容必须先展示给用户评估，用户确认后才写入。不自动写入任何变体。**

### Step 1 — 写入预览（Preview）

Phase 4 输出的每条 `action != SKIP` 指令渲染为「待写入预览块」，随蒸馏报告一起输出：

```markdown
### 待写入 #N：[action] → [target_file] [slot]（[变体名]）
- **来源论文**: [Author Year (VENUE)——年份必填；wb 标记缺席时这是唯一 citekey 来源]
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

确认后的写入步骤不变：打开 `target_file` → 按 `insert_after` 插入 → 更新 `source_papers` / `variants_count` / `updated` → 对 `new_anti_patterns_for_skill` 写入「反模式」段落 → 更新 `INDEX.md` 表行和「已填充变体」计数 → **更新文件顶部「变体速查表」**（新变体行 + 槽位分布总览，`区别` 列直接取 `distinct_from`；速查表与正文变体必须同步，quality_check 会校验）。速查表行格式遵守 `../../distill-paper-exemplar/references/band-vocab.md` 路由行胶囊规范（只复述正文已有内容、要点 ≤4 条、压缩不得改变路由判断）。

**旧变体锚点回填**：`REPLACE`/`EXTEND` 触碰已有变体且该变体缺 `原始句锚点` 时，按上述锚点来源检索规则**顺带补锚点**（检索不到原文则标"待补"，不阻塞写入）。

### 评估清单（供用户参考）

- [ ] 骨架无机构名/政策名/数据库名残留（[placeholder] 泛化彻底）
- [ ] 与已有变体不重复（Phase 3 新颖度成立）
- [ ] 骨架填入实际内容后能产出顶刊风格段落（可生成性）
- [ ] **原始句锚点保留原文风味**（生成时可据此校准"顶刊味道"；锚点非复制源）
- [ ] 因果语言强度与设计类型匹配
- [ ] 符合你的写作习惯与当前论文需要

`core_candidate`、单篇证据或主骨架级修订只生成显式人工审核包——同样先展示后由用户决定；不得自动修改 SKILL.md、路由、强制槽位顺序、story schema 或 stage gate。

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

## Phase 4 收尾 — 骨架索引回填（2026-09-15 起）

写回只更新 corpus 与选材索引；写作期借句检索的底本来源是 `corpus/_skeleton/` 骨架子清单
（借句表底本 id 只取自骨架子清单），必须重建回填，否则新变体对写作期不可见：

```bash
python ~/.claude/skills/write-methods/scripts/build_indices.py
```

- plan 含 `new_file`（create_new_file）项：先在 `write-methods/scripts/build_indices.py`
  的 `FAMILIES` 轴表登记该文件再重建（`_shared/indexing/check_all.py` 的 Check-R 会拦截
  未登记新文件）。
- 收尾判据：`python ~/.claude/skills/_shared/indexing/check_all.py` 全绿（重建产物与
  corpus 同批提交）。

## Phase 4 收尾 — 回写后语料体检

回写完成后运行 skills 根目录的体检脚本：

```bash
PYTHONIOENCODING=utf-8 python ~/.claude/skills/corpus_health_check.py --type methods
```

- exit 0 = 正常；exit 1 = 存在 critique_heavy 类型——在输出中列出这些类型，作为下一轮蒸馏 REPLACE/EXTEND 的优先级依据。
- 脚本缺失或运行失败不阻断回写，但必须在输出中声明"体检未执行"，不得静默跳过。
