# _shared（运行期共享件）

**定位**：运行期共享件的落点——各 skill 在**执行任务时**共同依赖的契约、引擎、schema 与指针白名单。当前内容：

- `pass-contract.md` — 审查输出契约（六字段 + 两条硬规则 + 四个 review 出口的消费方清单）。所有 `*-review` skill 的 PASS 输出以本文件为唯一事实源（原位于 `write-introduction/references/`，Batch 4 迁入）。
- `pointer-allowlist.txt` — `skill_pointer_check.py --strict` 的跨 skill 指针白名单。
- `function-map.md` — 功能→语料载体地图（write-* 家族「按句子功能取范本」的跨节路由；各节功能系统异构即正典，本图只列轴名+唯一源指针+词汇/档位载体，不复述各节索引）。由 `check_all.py` function-map 节机器看守（指针可解析 + 索引目标非空）。
- `consumption-log.md` — 消耗登记单源（四个 write skill 成文后的 query_id/UID/草稿指纹关联、统一采用入口与原生登记兼容；各 SKILL.md 只留本 skill 固定值指针）。
- `feedback/` — 反馈引擎（Batch 5 已落地）：`record_feedback.py`（fingerprint 去重 + supersedes + 读写 registry 的共享引擎，schema 迁移 1.0.0→1.1.0 只在读取层）、`lint_language.py`（确定性语言锁扫描引擎）、`schema.json`（canonical schema 1.1.0 + 迁移映射声明）。write-methods / write-results / write-introduction 的 scripts/ 只留薄封装与各自词表/registry。
- `indexing/` — 骨架索引共享引擎（§9.2 已落地）：`indexing_engine.py`（write-theory / write-methods / write-results 三份 `scripts/build_indices.py` 的共享工具层 / Entry·Unparsed / materialize / verify 回源抽样 / 渲染原语 / 写盘 / CLI，唯一一份；各 skill 适配器只留目录轴、正则、槽位机制、模板文本与锚点校验）、`check_all.py`（**维护期回归门**：重生成 + blob 哈希逐字节比对 + SUMMARY 解析 + validator 串联；运行期写作路径不引用——对下表边界判据的显式例外，先例 `story-blueprints/tests/regression_retrieval.py`）。

**与 `_governance/` 的边界**：

写作期检索见 `exemplar-retrieval.md` 与 `indexing/retrieve.py`；`indexing/build_catalog.py` 从四节原生适配器生成可丢弃的缓存，默认落本机 `%LOCALAPPDATA%/claude-skills/corpus-index/<仓库路径哈希>/catalog.json`，不写入 skills 仓库。细功能的动作定义与例子唯一维护在源卡 `retrieval-move.definitions`，索引派生读取；宽功能名称与既有选择器桥接见 `indexing/retrieval-functions.json`。旧编号迁移记录见 `indexing/legacy-id-migration.json`。`check_all.py --worktree` 校验当前工作树的可重建性、来源绑定与检索回归。

蒸馏增量写回的登记、索引刷新、试查和清理统一见 `distillation-writeback-finalization.md`；四个单节蒸馏与整篇编排共用。

细功能补在现有范本块的 `retrieval-move` 元数据中，查询用 `--need` 表达具体动作，连续动作可用有序 `--action`。`applicability` 和 `sequence` 仍由源卡维护，`indexing/request_matching.py` 核对条件与同源原文顺序；排序依次比较功能、条件、内容、来源，未知适用性明标，主题近但动作不符的候选单列。真实写作走 `indexing/use_exemplar.py query → open → write/adopt`：实际操作自动登记返回、查看与采用，统一采用登记同时写 consumption。`query_id` 关联候选 UID/排名/版本，`use_id` 关联实际保存草稿及两类采用事件，重试修复漏登不重复计数。收到明确评价后用 `feedback` 校验实际采用与版本；候选评价、旧稿与新稿评价分别呈现，目标歧义保持未知。`show --query-id` 派生完整使用链；原 `log_exemplar.py` 入口兼容相同反馈校验。台账仅存关联、文件定位与指纹，写仓库外；维护继续用只读 `retrieve.py`，试运行用隔离台账。流程单源见 `exemplar-retrieval.md`。

每条候选的 `adaptation_card` 按原句/功能/骨架/替换部分/条件/来源上下文六栏支持改编，`retrieve.py --format cards` 可输出 Markdown。`indexing/adaptation_cards.py` 只派生展示；段落承接、推进及后续证据仍由源卡元数据维护，未标注的信息保持未知。格式与使用边界见 `exemplar-retrieval.md`。

write skills 的文件保留口径：`corpus/` 正文是语料与功能资产，`corpus/_skeleton/` 是可重建的运行索引，注册表/反馈账本是持久治理状态；这些均有长期用途。缓存、写回工作单、一次性候选、评测输出和备份落仓库外工作目录。`check_all.py` 的内部文件清洁门仅拦截明确的临时格式/文件名；`preview`、`draft-revision` 等正式功能或协议名称照常保留。

| | `_shared/`（运行期） | `_governance/`（维护期） |
|---|---|---|
| 读取时机 | 每次执行 skill 都可能被读取 | 仅在语料维护 / 回归检测时读取 |
| 内容性质 | 契约、引擎、schema、指针白名单 | 盲测基准、pruning 清单、治理脚本 |
| 判据 | 被 SKILL.md 的运行期步骤直接引用 | 被 distill-* / corpus_health_check 等维护流程引用 |

一条经验判据：**被 SKILL.md 的运行期步骤直接引用 → `_shared/`；只在维护 / 评审 / 回归流程中被引用 → `_governance/`**。
