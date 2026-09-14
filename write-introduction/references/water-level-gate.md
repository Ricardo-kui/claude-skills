# Water-Level Gate — 水位门（表达质量线）

> **位置**：Phase 4，排在 `quality-gates.md`（结构/功能合规）之后。本门与合规**并列且不可互替**：合规 PASS 不蕴含水位 PASS，水位取值独立于合规结论。
> **审查契约**：本门产出的字段格式与举证要求见 `pass-contract.md`（单一事实源）；本门只定义四项检查内容与重写门。
> **不重复表达细节**：五病的定义与例证单一源 = `../pollock-qc/references/prose-pathology.md`；其余表达细节（AI 腔 / specificity / 节奏 / 术语密度）的定义与修复见 `corpus/storytelling/prose-craft-checklist.md` §0 与 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §5。本门只核对"是否执行"，并要求把执行证据写进举证字段。
> **触发分支（与 `generation-protocol.md` 对称）**：本门适用于任何要产出最终句子的请求——含完整 Introduction、单模块与改稿（含"不够像范文"的返工）；只请求诊断或大纲、不产出句子时不触发。

**水位** = 表达质量线，指一段文字作为顶刊论文语言的完成度（姿态、防御预算、元语言、底本覆盖）。它与"合规"是两个独立维度：合规问"是否违反锁定边界"，水位问"是否写到了范文的表达质量"。两者都有取值才算审查完成。

## 一、§姿态（posture）

**姿态** = 作者对"自己知道什么、机制是否被观察"的站位，两端为上帝视角（不合格）与机制语气（合格）。机制语气的动词/句式表及其机制类型定义归 `generation-protocol.md` G4「机制语气库」（`we theorize` / `we argue` / `may reflect` / `is consistent with` / `can change` 等）；本门不复制该表。

触发句式清单（出现即核查）：

- 定义式断言：`X is Y`、`X is the Y`；
- 事实语气归属：`X shows / demonstrates / reflects / proves Y`；
- 心智状态直断：`owners want / seek / intend…`、`investors perceive…`；
- 因果直断：`because it changes the objective…`、`X are therefore Y`。

修复方向：按 `generation-protocol.md` G4「机制语气库」选与机制类型匹配的底本动词并声明作者立场。G4 回归 case 逐字指针：`generation-protocol.md` §五「回归 case」——原句 `Annual serious recall counts are therefore governance outcomes. They show…` 判姿态不合格。

**完成判据（是/否）**：正文每处触发句式都已改为机制语气，或在举证字段写明保留理由？

## 二、§预算（defense budget）

**预算** = 防御性限定在全篇的**计数上限**。

**计数项**（逐条可数）：

1. 同一 caveat 全篇**集中披露 ≤1 次**（mixed evidence / measure sensitivity / inference sensitivity 只在一处完整陈述）；
2. 贡献段限定句 **≤1**；
3. 黄金段（Hook / Theory Lens / Contribution）**无防御句**。

**形态要求**（非计数项，不计入上列三项）：段落收尾用**肯定式范围句**（如 "These boundaries are scope conditions, not uniform effects."）。

**防御堆叠的已核实实例**（从 G3 事实记录移入本门，不属任何锁定约束）：

- "Fewer serious recall counts should not be presumed to represent a safety improvement."（`Introduction_0913_polished.md:34` / `_deepened.md:36`）
- "These are separately testable boundaries within one internalization framework, not independent contextual additions or components of a three-way condition."（`_polished.md:30` / `_deepened.md:32` / `_rewritten.md:27`）

**完成判据（是/否）**：三项计数均在预算内、段落收尾为肯定式范围句？超预算或防御堆叠处附原句与底本 id？

**扩展病理判定**：Overclaiming（确定性过高）与 Defensive prose（确定性过低 / 防御姿态）的判定归本节防御预算字段与 §一 姿态字段；两条的条目定义见 `corpus/storytelling/prose-craft-checklist.md` §6。

## 三、§元语言（meta-language）

管理语言默认转成论文语言，**除非目标期刊画像允许**（与 `journal-fit.md` 的「元句容受」列对齐；该列取值决定本项例外是否成立）。

| 管理语言 | 论文语言 | 今日实例 |
|---|---|---|
| `the sign is the estimand, not the contribution` | The direction of this association is not the contribution itself; the contribution is the mechanism through which it arises. | G3 row 1 |
| `nonexclusive adjudication` | supplementary evidence / diagnostic evidence | G3 row 4 |
| `locked` / `contribution boundary` | the scope we commit to / the bounds of the claim | 全文 |
| `bounded scope conditions`（成堆） | scope conditions / conditions under which the relationship has more force | 边界段收尾 |
| `estimand` / `adjudication`（方法语境外） | association / diagnostic test | Preview |

例外前提：`journal-fit.md` 元句容受列为「允许」时，本项相应放松；列为 `未核查` / `<待证据回填>` 时按默认（转论文语言）处理。

**完成判据（是/否）**：正文无未声明的元语言泄漏，或泄漏处已由目标期刊画像显式允许？

## 四、§底本覆盖率与重写门

**底本覆盖率** = 有底本 id 的**论证型段落**占全部论证型段落的比例（论证型段落定义见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`；framing 段不计入分母）。

- `< 80%` → **回 G1 全量重写**（重落借句表、按底本重渲染）；句级修辞动作留给 `≥ 80%` 分支；
- `≥ 80%` → 进 L-Move 句级修辞动作（L-Move 的层定义见 `library-contract.md`；动作清单见 `../story-blueprints/v4/rhetoric-moves/_index.md`）。

**完成判据（是/否）**：覆盖率已计算并写入举证字段？分支结论（全量重写 / 句级修补）与阈值一致？

## 五、表达细节的核对方式

水位门不重新定义表达细节，只核对是否执行：

| 表达项 | 单一源 | 核对方式（写入举证字段） |
|---|---|---|
| 五病 | `../pollock-qc/references/prose-pathology.md`（五病的定义与例证唯一源） | 逐项写"已执行 / 未命中"，命中处附原句 |
| AI 腔 | `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §5 与 §AI 腔速查表 | 写"已对照 X 项" |
| specificity | `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §write-* 共用纪律 | 写"句子能否原样放进任意论文"的判定 |
| 节奏 / 术语密度 | `corpus/storytelling/prose-craft-checklist.md` §0、§4 | 写"长短句交替 / 构念术语统一"判定 |
