# story-blueprints 指针分诊与基准 D 落地验收（2026-09-15）

> 承接 `write-star-optimization-round2-2026-09-14.md` §6 的开放项「story-blueprints 76 处指针待分诊」。
> 本文件是**验收记录**（做了什么、实测数字、被驳回的口径、残余风险），不是方案书。

## 0. 结论摘要

- 开放项已闭环：`story-blueprints` 从「完全不进校验器」变为**一等校验对象**（新增基准 D = 仓库根 + `SHARED_ROOTS`），其 117 处指针在 **strict 与非 strict 两种模式下均 `missing=0`**。
- 「76 处」是**计数口径产物，不是断链数**（见 §1）。真实断链在修完机制后为 **0**，其余是写法/基准问题 + 6 条仓库外资产。
- 全落地分 5 枚可独立回滚的 commit（§3），**两个批次各经一轮独立复核**（§5）：`0 P0 / 0 P1`，全库 `OK→MISSING = 0`（两种模式），三套下游门禁逐字节不变。
- 未处理项集中在 §7（有意保留）与 §8（残余风险，含一条既有假 OK 与三条机制化建议）。

## 1. 前提更正：「76」的来历

上一会话报告的「76 处」用当前扫描器**在两种提交状态下都复现不出**（`bfdb670` 与 `268081c` 的 strict missing 均为 70）。穷举计数口径后定位：

| 口径 | 报出行数 | distinct target 串 | 涉及文件 |
|---|---|---|---|
| rel 非 strict（**= 76 的唯一来源**） | 101 | **76** | 24 |
| rel strict | 70 | 50 | 18 |
| abs 非 strict | 85 | 64 | 21 |
| abs strict | 70 | 54 | 17 |

即 **76 = 「MISSING 行 + NO-BASELINE 行」去掉重复 target 串后的个数**（35 + 41，两集无交集），不是断链数。
该口径还建立在一个**驱动 bug** 上：临时驱动传相对路径 `Path("story-blueprints")`，而 `skill_root_of()` 用绝对 `ROOT` 做 `cur.parent == ROOT` 等值比较 → 永远不成立 → 回退到仓库根，凭空多出 16 条 MISSING。真实脚本（`main()` 用 `rglob` 返回绝对路径）不受影响，但**任何用相对路径自建驱动的复核都会失真**——这条已写进 §8 的复现纪律。

## 2. 改动前的真实基线（真实脚本，绝对路径）

| 命令 | checked | missing | whitelisted | 说明 |
|---|---|---|---|---|
| `--strict --whitelist … story-blueprints` | 117 | **61** | 9 | 61 条里含大量「语义正确但基准解析错」与「裸文件名」 |
| `--strict --whitelist …`（全库） | 7775 | 1411 | 271 | 快照环境实测 1412（差 1 为仓库外指针 artifact，非行为差异） |
| `--strict --whitelist … <9 skill>` | 4948 | 0 | **183** | 门禁本体是绿的，代价是 183 次白名单豁免 |

加基准 D 后（内容未改）：`story-blueprints` `missing 61→36`、`whitelisted 9→3`、`resolvedD=31`；9 skill `whitelisted 183→119`（64 行**从豁免变成真解析成功**）。

## 3. 落地内容（5 枚本任务 commit）

| # | commit | 文件 | 内容 |
|---|---|---|---|
| A | `9ac480a` | `skill_pointer_check.py`、`_shared/pointer-allowlist.txt` | 基准 D（仓库根）+ 影子守卫 + `SHARED_ROOTS=("story-blueprints",)` + `skill_root_of()` 入口 `.resolve()` + `resolvedD=` 可观测 + 删 25 条 stale key + docstring 基准表 |
| B | `79fca24` | 10 个 `story-blueprints/**/*.md`、白名单 | 26 行正文指针修复（裸名补全 / 跨 skill 显式 `../<sibling>/…`）+ 6 条仓库外白名单 |
| C | `e0d953c` | `skill_pointer_check.py` | 影子守卫上溯至 `skill_root` 且改用 `.exists()`，封堵嵌套影子与文件型影子的 false-pass |
| D | `1702607` | 9 个 md、白名单 | 默认（非 strict）模式 18 条归零 + `scripts/README.md:26` 教学句自洽 + 白名单理由口径同步 |
| E | `b3cc4f3` | `skill_pointer_check.py`、`scripts/README.md` | `classify(…, md=None)` 回退精确恢复 pre-C `.is_dir()`；L9「上一级」措辞改为「仓库内 …, 相对本目录即 `../../../scripts/`」 |

另有 5 枚**并发写者** commit（`5765bce`/`1f41fe0`/`34873c3`/`4dd8195`/`4c240eb`，write-* 索引脚本重构 + `_shared/indexing/`），非本任务产物。

### 三层机制改动各自的角色

1. **基准 D = 仓库根**：裸 `sibling/…` 的语义真身是仓库根，不是 skill 目录。依据是机器可读真值——`story-blueprints/scripts/retrieve_exemplars.py` 用 `Path(__file__).resolve().parents[1].parent / "distill-paper-exemplar" / "scripts"` 解析跨 skill 脚本目录，正是 `_immediate-exemplar-protocol.md:5` 那条裸指针的真身。
2. **影子守卫**：D 只在「首段是 ROOT 直属目录 **且** 从文件自身目录上溯到 `skill_root` 的任一层都不存在同名条目」时生效，因此原本判 C-OK 的行不可能被 D 覆盖 → `OK→MISSING` **构造上不可能**（另有实测对账佐证）。库内真实影子样例：`staggered-did/stata/`、`humanizer/.claude-plugin/`。
3. **共享根显式常量**：ROOT 下另有 12 个无 `SKILL.md` 目录（合计 746 目标 / 593 MISSING），全纳入会让默认门禁被噪声淹没；`story-blueprints` 是唯一含大量跨 skill 指针的共享根。要加谁，谁举证。

## 4. 验收数字（最终态，commit E）

```
python skill_pointer_check.py --whitelist _shared/pointer-allowlist.txt story-blueprints
python skill_pointer_check.py --strict --whitelist _shared/pointer-allowlist.txt story-blueprints   # 两者均 exit 0
→ checked=118 resolvedA=51 resolvedB=0 resolvedC=30 resolvedD=31 missing=0 whitelisted=6
  unresolved_no_baseline=0 unresolved_missing_file=0

# 9 skill 门禁（相对改动前：missing 0→0，whitelisted 183→119，新增 resolvedD=64）
→ checked=4948 resolvedA=483 resolvedB=305 resolvedC=3977 resolvedD=64 missing=0 whitelisted=119

# 全库默认跑（strict）
→ checked=7893 missing=1353 whitelisted=206 resolvedD=160
```

对账（逐行 `(file, line, target) → status` 迁移）：

| 迁移 | strict | 非 strict |
|---|---|---|
| `OK → MISSING` | **0** | **0** |
| `WHITELIST → MISSING` | **0** | **0** |
| `MISSING → OK`（A 批） | 57 | 57 |
| `WHITELIST → OK`（A 批） | 72 | 72 |
| `MISSING(no_baseline) → OK`（D 批） | — | 18 |
| 新增 MISSING | **0 条** | **0 条** |

下游门禁（pre/post **逐字节相同**）：`tests/regression_retrieval.py` → `ALL REGRESSION ASSERTIONS PASSED`（43 fixtures 非空，exit 0）；`scripts/validate_blueprints_v4.py` → `v0.4-lite cards: 78 | invalid: 0`（exit 0）；`scripts/validate_blueprints.py` → 既有 `ERROR 1`（`_index.md: 索引行无对应文件: lun2026`）+ `WARN 1`（`_schema.md` half-domain-gap 计数），exit 1，**无新增**。

## 5. 独立复核（两轮，均 fresh-context reviewer）

| 轮 | 对象 | 裁定 | 独立复现的关键点 |
|---|---|---|---|
| 1 | A、B | COMMENT / **push 放行**，0 P0 0 P1，3 个 P2 | N1–N4 四组数字零差异；`OK→MISSING=0`；三套门禁 md5 相同；影子守卫两个 false-pass 反例可执行复现 |
| 2 | C、D | **APPROVE**，0 P0 0 P1 | 自建 mini-repo（嵌套影子 / 文件型影子 / junction 影子 / 空 seg / `md=None` 矩阵 36 组）；C-only old-vs-new 在 live 上**逐字节相同**；D 的唯一效果 = 恰好 18 条 `no_baseline→OK`，0 新增 MISSING |

### 被复核驳回的口径（本记录不沿用）

1. 「25 条白名单 key 改前零命中」**错**：改前（旧脚本 + 旧白名单）它们合计命中 71 行（最大 `write-methods/SKILL.md` 27 次）。它们是**打上基准 D 之后**才变成零命中——删除仍正确且零回归，但「stale」必须表述为「相对新基准陈旧」。
2. `blueprints/desjardine2022-rising-tide.md:112` 的 Vault 全路径出处是**同文件 `vault_reports.theory`（L12）**，不是 `corpus_links`。
3. B 批「27 处」实为 **26 行 / 34 个指针 span**；D 批「18 行」实为 **16 行 / 19 occurrences**（18 条 MISSING 修复 + 1 条 P2-3 重标注）。

### 两处语义裁定（复核独立背书）

1. `v4/rhetoric-moves/_index.md:43` 的裸 `SKILL.md` → 改指**本文件的动作分类表**。依据：`polish/SKILL.md:12` 原文「识别动作读 `story-blueprints/v4/rhetoric-moves/_index.md` 动作分类表，按草稿的修辞功能自动匹配」，而 `polish/SKILL.md` 本身**没有任何表格**；`v4/rhetoric-moves/SKILL.md` 不存在（真死链）。残留瑕疵（P3）：该行现在读作「在 `_index.md` 里说见 `_index.md`」，同文件平行句用的是「本文件动作表」。
2. `desjardine2022-rising-tide.md:112` 的 Vault 全路径：复核逐条 `-e` 实测真身存在（同批 4 个 Vault key 亦全部存在），路径与 `vault_reports.theory` **逐字相同**，无猜测成分。该处是「⚠️ vault 勘误」注记而非可执行指针。

## 6. 白名单政策（本批确立，是后续所有批次的判据）

- **enter**（三条，均要求「本仓库不可能有该文件」）：真身在仓库外（Vault / 工作区根相对 / 插件缓存）；已删除资产的历史声明；运行时生成物。
- **not-enter**（三条禁令）：目标在仓库内可确定存在（必须改正文）；**裸文件名**（key 是全局扁平命名空间，一处豁免全库失守——实测裸 key 命中 `SKILL.md` 34 次、`_index.md` 10 次）；改基准后零命中的 stale key（本批删了 25 条）。
- 理由措辞模板：`<target> | <类别>：<真身位置>；<为何本仓库不可能有>`。
- **联动规则（写死）**：key = 改写前的精确 target 串，改正文必须同 commit 改 key，否则旧串会变成「未来同字面断链的静默豁免」。

## 7. 有意保留未改

- `story-blueprints/README.md:20–22`、`v4/rhetoric-moves/scripts/README.md:5/9/13–16/30` 等处残留的裸仓库根写法（基准 D 兜底，两模式都 OK）。裁定：**新增/重写一律显式 `../<sibling>/…`，存量不做全库批量规范化**（与 round2 方案 L16/L104 的既有裁定一致）。
- `scripts/README.md` 中「演示不同基准下同一指针解析成什么」的示例串（进白名单，不改）——改了会破坏该文档的解释功能。
- 围栏代码块内的 canonical 调用串（校验器按约定跳过）。
- 60 份卡的 YAML front-matter / `corpus_links` 数据字段、`v4/catalog.json`、`references/tag-normalization.yaml`：**禁改**（是 `retrieve_exemplars.py` / `validate_blueprints*.py` 的数据输入）。

## 8. 残余风险与后续建议

| 级别 | 项 | 建议 |
|---|---|---|
| P3（既有，非本批引入） | strict 下目标串 `/` 解析到文件系统根 `C:/` 并报 OK，库内 7 行（`officecli/SKILL.md:239,328`、`stata/packages/tabout.md:239`、`stata/references/{basics-getting-started.md:237,date-time-functions.md:82,variables-operators.md:73,97}`） | 把 `/`、`./`、`../` 一类纯分隔串判为非路径或 no_baseline |
| 机制 | 白名单**无 staleness 护栏**，25 条 stale key 就是这么攒出来的 | 加 `--check-whitelist-staleness`（任何 key 零命中即 exit 1） |
| 机制 | 校验器**没有任何测试**，「零回归」全靠人工 A/B 重跑 | 把 pre/post 全量输出规范化为 `(file, target, rule, status)` 快照入库做 golden fixture；并接 CI/pre-commit |
| 机制 | 默认跑（全库）纳入 sbp 后 `checked +117`，其中 6 条外部目标仍需豁免 | 若 CI 以默认跑为必绿门禁，需先决定 sbp 的 6 条是否允许长期豁免 |
| 度量纪律 | 用 `git archive` 建基准会**严重失真**（`.gitignore` 首行 `*` 忽略大量真实目录与 junction，实测 `checked=6292` vs 真值 7775） | 复核一律用 `tar` 工作树快照或 `git show <rev>:<path>`；且**驱动必须传绝对路径**（见 §1） |
| 噪声 | 扫描吃到 `baoyu-translate/scripts/node_modules/**` 的第三方 README（+7 行 / +4 MISSING） | 排除 `node_modules/` |
| 范围外 | 全库 strict 仍有 1353 条既有 MISSING（主体在 story-blueprints 之外的 skill） | 另立批次，不要混入指针基础设施改动 |
| 范围外 | `validate_blueprints.py` 长期红灯（`lun2026` 索引行），使「退出码」信号失效 | 该 RED 应单独清理，否则后续只能靠逐字节比对判新增 |

## 9. 复现命令

```bash
cd C:/Users/admin/.claude/skills

# 目标态：story-blueprints 双模式归零
python skill_pointer_check.py --strict --whitelist _shared/pointer-allowlist.txt story-blueprints
python skill_pointer_check.py          --whitelist _shared/pointer-allowlist.txt story-blueprints

# 门禁本体 + 全库
python skill_pointer_check.py --strict --whitelist _shared/pointer-allowlist.txt \
  write-introduction write-theory write-methods write-results write-section \
  intro-review theory-review methods-review results-review
python skill_pointer_check.py --strict --whitelist _shared/pointer-allowlist.txt

# 下游
python story-blueprints/tests/regression_retrieval.py
python story-blueprints/scripts/validate_blueprints_v4.py
python story-blueprints/scripts/validate_blueprints.py
```

---

**验收结论**：开放项闭环；`0 P0 / 0 P1`；两种模式 `OK→MISSING = 0`、新增 MISSING = 0；三套下游门禁逐字节不变。回滚顺序：E → D → C → B → A（D 批依赖 A 的基准 D，先回 B 会把 25 条已删 key 变成真断链）。
