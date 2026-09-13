# Registry 派生视图：分区地图、派生规则与透传契约

> S2 交付物（2026-09-13）。上游计划：`C:\Users\huawei\.claude\distill-work\PLAN-registry-derived-views.md`。
> 工具：`distill-paper-exemplar/scripts/rebuild_views.py`（派生重建 + --check 对账）；
> `partition_registry_surgery.py`（S2 一次性分区手术，含幂等守卫，勿重跑）。

## 0. 总纲

块即 truth：全库 338 处 `<!-- wb:<citekey>:<item> -->` 单行 HTML 注释（块尾、每块 ≤1、无多源合写）是语料块与 registry 足迹的 join key。四份 `_evidence_registry.yaml` 的 DERIVED 字段本质是块扫描的派生视图；执行器停止"读计数→+1→写回"类累加（S6 落地）；verify 收敛为漂移检测器。

## 1. 分区标记与段结构（S2 已落地）

标记行（顶格，单行注释）：

```
# === DERIVED: rebuilt by rebuild_views.py — do not hand-edit ===
# === AUTHORED ===
```

- 标记按段类型**交替**出现；文件首段（无标记前）属 AUTHORED；`split_partitions()` 返回有序 `(kind, text)` 段列表。
- `--apply`（S6）只重写 DERIVED 段；AUTHORED 段字节级透传；段内**按键透传**（keyed carry-through）字段见 §3。
- 四库当前段结构（物理键序，仅列首键）：

| corpus | 段序列 |
|---|---|
| write-introduction | A(meta) → D(evidence) → A(phrasebank) → D(paper_index) → A(critique + **status_overrides**) |
| write-theory | D(meta) → A(status_rules) → D(source_papers, patterns, summary_by_dimension) → A(honesty_boundaries, next_batch_targets, unattributed_corpus, critique + **status_overrides**) |
| write-methods | D(meta, evidence) → A(**status_overrides**) |
| write-results | D(meta) → A(status_rules, global_anti_patterns, global_honesty_boundaries) → D(estimators) → A(batch_history + **status_overrides**) |

- 保守硬约束全部保持：四 registry 路径与既有顶层键不变、`id:` 键行保留（precheck 分块锚，post-surgery 计数 0/4/0/409 与术前一致）、CRLF 保持（手术采用字节级读写，`Path.read_text()` 的 universal-newline 翻译是已踩坑点）、YAML 合法。

## 2. status_overrides（用户裁定显式优先）

ladder 成文：`distill-theory-exemplar/references/phase-4-validation-writeback.md` L232-238 —— 1–2 来源 EMERGING / 3+ VERIFIED / 5+ 且跨 2 子域 ROBUST（Incommensurability 晋升限制见该文）。

派生规则：**derived status = ladder(n_sources) ⊕ status_overrides（本节显式优先）**。键为 registry 路径（不含尾随 `.status`）；value = `{status, basis}`。rebuild `--check` 命中 override 即 match（note 携带 basis 摘录）；registry 值与本节冲突 → novel 漂移。

各库收拢量（S2 机械提取，凭据原文逐字保留）：results 191（`verification_basis` 字段）、theory 33（patterns 携带 VERIFIED@≤2，basis 标注"pre-partition carried"）、intro 16、methods 13（`user_designation`）。已知具名裁定：召回域单源 VERIFIED（2026-08-29）、Westphal 系单源 VERIFIED（2026-09-06）、Gulati 系单源 VERIFIED（2026-09-05/06 点名）。

## 3. 按键透传契约（S6 --apply 的 AUTHORED 保护）

DERIVED 段内并非全部字段可再生——rebuild 重生成段时，下列字段**按键从上一版文件原样携带**（键不稳定/丢失 → 记 orphan 漂移，绝不静默丢弃）：

| 段 | 派生（regenerate） | 透传（carry by key） |
|---|---|---|
| intro evidence.<module>.<entry> | paper_count, papers[], gap_distribution | status, generativity, exclusivity, common_failures, validation_history |
| intro paper_index | citekey 键集 | gap 值（writeback --gap 不在块内） |
| intro meta | —（整段 AUTHORED 携带） | — |
| theory source_papers.<paper> | fragments 成员（type/title/home_files 由块派生） | display_name, journal, year, subfield, gap_type, theory_build_type, source_tier；fragment 内 makadok_dimension, note, status（S4 迁入块） |
| theory patterns.<pid> | source_count, source_papers, home_file, status | description |
| theory summary_by_dimension | 全量（fragments makadok_dimension 再聚合） | — |
| methods evidence.by_design_type.<key> | papers[], paper_count, slots_covered | common_failures, validation_history, note |
| methods evidence.by_source_paper.<paper> | design_types 反查 | journal, title, status, verification_basis, note |
| results meta | batches_processed=len(batch_history), total_papers_indexed=distinct sources | schema_version, registry_type, last_updated, last_batch_id, usage_stats_schema, subfields |
| results estimators.<ek> | slots.*.skeleton_variants 成员 + id/corpus_path/sources/paper_count/status | display_name, usage_stats, forced_slots, high_risk_missing, cross_slot_patterns, anti_patterns, honesty_boundaries；variant 内 verification_basis, paradigm_exclusivity, transferability, rhythm_tags, notes, subfield_distribution |
| results batch_history | —（整段 AUTHORED；append-only 账本） | — |

不变量：tfr 编号永不重编（append-only id issuance 是执行器唯一保留的"新号分配权"，非计数累加）；batch_history / last_updated 的追加语义不动。

## 4. wb-meta 格式（S4 起，tfr 亲笔字段的块内归宿）

```markdown
<!-- wb:<citekey>:<item> -->
<!-- wb-meta: dim=Boundary status=EMERGING gap=Incompleteness tbt="机制推演型" -->
```

- 与 wb 标记**分立两行**（V2 校验不受影响）；单行、紧凑空格分隔 KV、值可双引号（含空格/中文）、grep 可命中（`wb-meta: dim=`）。
- 键集（开放）：`dim`（makadok_dimension 七维）、`status`（ladder 词）、`gap`（Incompleteness/Inadequacy/Incommensurability）、`tbt`（theory_build_type）。
- `rebuild_views.parse_wb_meta()` / `WB_META_RE` 已实现并有单测；扫描器已捕获 `Block.wb_meta`。

## 5. 块解析规则（S1 实证定案）

- 块界：`^#{2,4} ` （与执行器 `BLOCK_HEAD` 一致）。
- theory frontmatter 三态归属（计划 §3.2 陷阱）：① 本块内任一 wb item 与 `pattern_id` 模糊匹配（归一化后互含或词交过半）→ 本块；② 否则本块内有位于注释之后的 wb 标记 → 本块；③ 否则若下一块的 wb item 模糊匹配 → 下一块；④ 否则本块。
- 槽位派生只用 wb item 前缀（`m2_… → M2`、`r4_… → R4`）——与执行器写路径一致；`**槽位**` 行是块内散文不作 registry 输入。
- 状态信号：frontmatter `status:` 首词 / `**验证状态**` 行首词。
- 文件头 YAML 仅作参考（已知失真：匹配DiD variants_count 等以正文块扫描为准）。

## 6. 别名解析（双键体系）

`AliasIndex(primary=registry 键, secondary=wb citekey)`：registry 侧大小写不敏感精确命中 → primary 词交最佳（同年 + 核心词，平票拒绝）→ secondary 精确/最佳 → unresolved（入裁决单）。**永不猜测**——真歧义实例：两篇 2018 Ball（ball_anastasov…_smj / ball_shah_donohue…_jom）。

## 7. 对账基线与漂移分类

`--check` 产出三类判定（match / drift / unattributable）+ 七类裁决（expected_legacy_gap / expected_dual_key / expected_status_override / expected_stale_block_status / expected_counter_drift / expected_authored_passthrough / novel）。S2 后基线：match 977 / drift 278 / unattributable 1379 / **novel 184**（真实漂移候选，S6 rebuild 结构性消灭的清单）。报告与裁决单：`~/.claude/distill-work/rebuild_views/`。

## 8. S6 前的运行边界

`rebuild_views.py --apply` 现阶段一律拒绝（exit 3）：S2 分区已就位，但派生段重生成 + 按键透传的写入路径属 S6 交付，写路径双跑（S4）前不得触碰 registry。
