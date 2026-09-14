# _shared（运行期共享件）

**定位**：运行期共享件的落点——各 skill 在**执行任务时**共同依赖的契约、引擎、schema 与指针白名单。当前内容：

- `pass-contract.md` — 审查输出契约（六字段 + 两条硬规则 + 四个 review 出口的消费方清单）。所有 `*-review` skill 的 PASS 输出以本文件为唯一事实源（原位于 `write-introduction/references/`，Batch 4 迁入）。
- `pointer-allowlist.txt` — `skill_pointer_check.py --strict` 的跨 skill 指针白名单。
- `feedback/` — 反馈引擎（Batch 5 已落地）：`record_feedback.py`（fingerprint 去重 + supersedes + 读写 registry 的共享引擎，schema 迁移 1.0.0→1.1.0 只在读取层）、`lint_language.py`（确定性语言锁扫描引擎）、`schema.json`（canonical schema 1.1.0 + 迁移映射声明）。write-methods / write-results / write-introduction 的 scripts/ 只留薄封装与各自词表/registry。

**与 `_governance/` 的边界**：

| | `_shared/`（运行期） | `_governance/`（维护期） |
|---|---|---|
| 读取时机 | 每次执行 skill 都可能被读取 | 仅在语料维护 / 回归检测时读取 |
| 内容性质 | 契约、引擎、schema、指针白名单 | 盲测基准、pruning 清单、治理脚本 |
| 判据 | 被 SKILL.md 的运行期步骤直接引用 | 被 distill-* / corpus_health_check 等维护流程引用 |

一条经验判据：**被 SKILL.md 的运行期步骤直接引用 → `_shared/`；只在维护 / 评审 / 回归流程中被引用 → `_governance/`**。
