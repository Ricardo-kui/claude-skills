# Pass Contract — 审查输出契约（六字段）

> **单一事实源**：本契约定义 Introduction 审查输出的字段形状与举证要求。所有审查入口按本契约产出，不各自另定字段。
> **硬规则**：缺任一字段 = 审查未完成；只有"未违规"而无底本 id 的 PASS 无效。
> **路径基准**：本契约已从 `write-introduction/references/` 迁至 `_shared/`（Batch 4）。文中 `corpus/_skeleton/`、`water-level-gate.md`、`journal-fit.md`、`generation-protocol.md`（G3/G4）等仍按 `../write-introduction/` 解析——它们是 Introduction 域单一源，非共享件。

## 一、六个字段

| 字段 | 取值形式 | 举证要求 |
|---|---|---|
| `boundary_compliance` | 逐条锁定约束：`<约束名>: PASS / FAIL`，加一行总判 | 每条 FAIL 附原句；每条 PASS 附该约束在正文的落点句位。**锁定边界清单的权威在项目态**：canonical `story` / `story.integrity` 的锁定边界清单（如 unsupported_moves）是唯一权威；skill 不持有通用锁定约束清单。`generation-protocol.md` G3 表只是该清单的语言化映射，非权威本身。 |
| `exemplar_fidelity` | `PASS / FAIL` | **必须逐段列底本 id**（`corpus/_skeleton/<module>.md` 的 id，或明文 `self-drafted`）；无逐段 id 列表的 PASS 无效 |
| `posture` | `none / present` | `present` 附原句 + 应改用的机制语气（G4 语气库指针） |
| `defense_budget` | `within / exceeded`（附计数） | 三项计数逐项给数：同一 caveat 集中披露次数、贡献段限定句数、黄金段防御句数；另给形态要求判定：段落收尾是否为肯定式范围句（形态要求非计数项）。 |
| `meta_language` | `none / present` | `present` 附原句 + 论文语言替换；例外须指出 `journal-fit.md` 元句容受列的允许取值 |
| `expression` | `PASS / FAIL` | 逐项写"是否执行"：五病 / AI 腔 / specificity / 节奏 / 术语密度（单一源见 `water-level-gate.md` §五） |

> `exemplar_fidelity` 的 id 通过率即 `water-level-gate.md` 的底本覆盖率输入；`< 80%` 触发全量重写分支。

## 二、两条硬规则

1. **缺任一字段 = 审查未完成**。不产出"部分字段 + 默认通过"。
2. **只有"未违规"而无底本 id 的 PASS 无效**。`exemplar_fidelity` 为 PASS 时，逐段底本 id 列表必须非空且可在 `corpus/_skeleton/<module>.md` 定位；无法定位的 id 按 FAIL 处理。

## 三、消费方（四个 review 出口）

| 消费方 | 用法 |
|---|---|
| `intro-review` | 语言层审查按本契约六字段（唯一事实源）；节别增量：Introduction 的 Hook/Conversation/Problematization/Preview 逐字风格字段归其 QC 表，语言层字段由本契约承接 |
| `theory-review` | 语言层/契约承接：PASS 输出按本契约六字段；节别增量：why-chain 是否兑现 central knot |
| `methods-review` | 语言层/契约承接：PASS 输出按本契约六字段；节别增量：识别威胁三C（Completeness / Clarity / Credibility） |
| `results-review` | 语言层/契约承接：PASS 输出按本契约六字段；节别增量：双层支持判断（假设支持判定 + 稳健性 threat 组织） |

## 四、完成判据（是/否）

- 六字段全部有取值？
- 每个 FAIL / `present` / `exceeded` 都附原句与底本 id（或 `journal-fit.md` 允许取值）？
- `exemplar_fidelity` 的逐段 id 列表非空且可定位？
