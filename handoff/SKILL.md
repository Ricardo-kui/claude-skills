---
name: handoff
description: 会话交接。把一个 session 的结论写成一份交接记录，供下一个 session 接续。写入位置为项目知识库（不是系统临时目录）。触发词：交接、handoff、写个交接文档、新会话继续、换个窗口接着做、收尾记录。
---

# handoff

`research-bootstrap` 的**写入端**。bootstrap 负责读入项目状态，本 skill 负责在会话结束时把本次新增的执行层信息落回项目。

## 1. 写入位置与命名

**位置**：`D:\OneDrive\Obsidian Vault\00 工作台\项目\<项目名>\00 Active\`

> **2026-09-11 修正**：旧版本规定写入**系统临时目录**且「不写进当前工作区」。该规定与实际用法完全相反——Vault 内 11 份真实交接稿全部落在项目目录，临时目录无任何产出。现改为写入项目目录。

**命名**：`session-handoff-YYYY-MM-DD.md`。同一天第二份加后缀 `-b`、第三份 `-c`。

**不再使用**的历史命名（存量文件不重命名，仅新文件遵守新规则）：`交接 - <主题> YYYYMMDD.md`、`YYYY-MM-DD_Session交接_<主题>.md`、`HANDOFF_SESSION_YYYYMMDD.md`。

## 2. 固定格式

```markdown
---
type: handoff
project: <注册表 id>
date: YYYY-MM-DD
supersedes: <上一份文件名> | none
session_focus: <一句话>
authority: detail-only
decision_authority: 00 Active/Decision Register - <项目名>.md
---

## 当前状态
（≤5 行。从 PROJECT_STATUS 与 Decision Register 派生，不新增信息）

## 下一步
（≤5 行）

## 执行细节（本层独有）
- 系数与模型输出：…
- 运行命令 / 路径：…
- 环境坑与运行怪癖：…

## 待签认项
- <起草但未签认的 design_lock / claims 字段>（无则写「无」）

## 证据完整性声明
```

**前两节必须在文件顶部且不超过 5 行**——这是为了让 `research-bootstrap` 能在只读前两节时就把状态接上，而不必全文加载。

## 3. 硬规则

1. **禁止复述决策**。决策内容属 Decision Register。这里只写 `D-20260911-02` 这样的**编号引用**，需要细节时由读者回查。
2. **引用而非复制**。不要粘贴 Decision Register 或 PROJECT_STATUS 的段落。文件级信息给路径，不给内容副本。
3. **只写本层独有的东西**：系数、命令、环境坑、未落盘的中间产物、当日踩到的坑。这些在 DR 与 PS 里都没有对应位置，是 handoff 存在的理由。
4. **脱敏**。不上传、不写入任何未公开数据或受保密约束的内容。
5. **待签认项不得标为已确认**。起草的高风险字段标 `status: draft`，并在「待签认项」列出。

## 4. 权威分层（三者不得互相覆盖）

| 层 | 载体 | 承载什么 | 寿命 |
|---|---|---|---|
| 决策权威 | `Decision Register` | 已锁决定、依据、被否决方案、不要复活 | 长 |
| 摘要投影 | `PROJECT_STATUS.md` | 当前阶段、焦点、下一步 | 中 |
| **执行细节** | **本 skill 的产出** | 系数、命令、环境坑、中间产物 | **短（随工具版本失效）** |
| 数据事实 | `FINDINGS.md` | 数据层事实 | 中 |

**同一信息只在一处维护。** 若发现某条决策同时出现在 handoff 与 DR，handoff 那一份是缺陷——改为编号引用。

## 5. 何时被读取

`research-bootstrap` 在读取链第 5 步读取**最近一份** handoff 的 `## 当前状态` 与 `## 下一步` 两节。其余分节（执行细节、待签认项）仅在以下情形按需读取：

- 用户明确要求继续实证执行；
- 用户问起某个系数、命令或环境问题；
- 排查「上次跑通了、这次跑不通」。

**不要整份注入。** 一份 handoff 可达 300+ 行，全文加载会挤占项目状态读取的预算。

## 6. 定稿前的自查

- [ ] frontmatter **六个**字段齐全（含 `authority: detail-only` 与 `decision_authority`），`project` 与注册表 id 逐字一致
- [ ] 文件写在项目 `00 Active/`，不在临时目录
- [ ] `## 当前状态` 与 `## 下一步` 各不超过 5 行且位于顶部
- [ ] 全文检索：是否复述了任何一条决策的内容？有则改为编号引用
- [ ] 「待签认项」已如实列出起草未审的内容

## 7. 归属声明：机器可判定的分层

`authority: detail-only` 与 `decision_authority: <DR 路径>` 不是装饰。它们的用途是让下游能**机器判定**这份文件是不是决策权威：

- `research-bootstrap` 读到 `authority: detail-only` → 只取 `## 当前状态` / `## 下一步`，**不采信其余内容为决策**；
- 存量交接稿缺这两个字段 → 视为**归属未声明**，只能按降级规则读开头 ≤20 行，且不得把其内容当作当前决策；
- 若某份 handoff 的正文与 `decision_authority` 指向的 DR 冲突，**以 DR 为准**，并把该冲突登记进分歧登记表。

## 8. 存量文件的归属补写（2026-09-11 已完成）

改造前已有的 11 份交接稿里有 7 份不符新命名与新分节约定。已为其**补写两个 frontmatter 字段**（`authority: detail-only` 与指向本项目 Decision Register 的 `decision_authority`），**正文一字未改**。

理由：它们是历史记录，改写会破坏证据链；而加两个归属字段即可让机器正确分层——成本最低、风险为零。这也与用户 2026-09-11 的裁定一致（历史欠账不应过度考虑，但不应让旧格式污染新分层）。

**存量文件本轮不做的事**：不重命名、不改正文、不删除、不拼接。

## 证据完整性声明

交接记录不是证据。它是对已发生工作的索引，所有事实性主张必须能追溯到 Decision Register、`empirical-state.yaml` 或 `outputs/` 中的实际产物。无法追溯的内容不得写入。
