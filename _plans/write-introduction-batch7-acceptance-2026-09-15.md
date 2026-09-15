# write-introduction 验收补测记录（Batch 7 / D-07 后续最小补测，2026-09-15）

- 补测对象：第一轮方案（`write-introduction-optimization-2026-09-14.md`）§7 验收实验中 D-07 标记为未检验的两项——**d（5 条失败原句回归）**与 **h（重写门）**；同时作为第二轮方案 Batch 7「把 P0 项转成可重跑断言」的 intro 侧实测记录。
- 输入：`D:/Onedrive/01_研究 Research/01_活跃项目 Active/共同所有权 × 产品召回/writing/Introduction_0913_deepened_20260914.md`（中间态，frontmatter 自证 `exemplar_retrieval: no matching Introduction learning object returned by v0.4-lite`，即管线化之前、无底本 id 的草稿——重写门的理想输入）。
- 规则源：`water-level-gate.md` §一/二/三/四、`generation-protocol.md` G4 回归 case、`_shared/pass-contract.md` 硬规则、`corpus/_skill_design_feedback.yaml` 的 5 条 `channel=rule, risk=high` 回归条目。
- 执行方式：主会话执行。h/d 是门逻辑的机械应用（覆盖率计数 + 规则句比对 + 既定改写引用），不涉及生成侧范文暗示，D-07 的"新会话 + 污染控制"要求针对 fresh 生成路径，对本次两项不构成效度威胁；d 判定允许读 contrast-pairs 与登记层（其规则源），与 D-07 当次禁读不矛盾——目的不同（回归对照，非无提示生成）。

---

## h｜重写门（水门 §四）

**段落盘点**：草稿为 `architecture: JOM compact six-paragraph introduction`，6 段全部为论证型段落（P5 结果预览段含审计性句子，但整段承载"边界证据不整齐"的论证主张，计入分母；无 framing-only 段）。

**覆盖率实核**：草稿全文无任何底本 id 登记；抽样 3 个特征句回源核对 `corpus/_skeleton/*.md`，命中均为 0——
- "whose losses enter an owner's governance calculus" → 0 命中
- "competitive proximity and potency as bounded scope conditions" → 0 命中
- "has largely treated serious recalls as visible traces" → 0 命中

**门判定（按 §四输出）**：

| 项 | 取值 |
|---|---|
| 论证型段落 | 6 |
| 有底本 id 的论证型段落 | 0 |
| 底本覆盖率 | **0% < 80%** |
| 分支结论 | **回 G1 全量重写**（重落借句表、按底本重渲染）；句级修辞动作（L-Move）分支不适用 |
| 联动（pass-contract 硬规则 2） | 草稿无逐段 id 列表 → `exemplar_fidelity` 不得判 PASS，任何"未违规式 PASS"无效 |
| 重启产物要求 | 先落 O1–O3 大纲表（每段来源列非空可核）+ G1 借句表（每段一行，只引 `corpus/_skeleton/<module>.md` 索引 id 或 `self-drafted`），再按底本重渲染 |

**重启可执行性示例（P1 行，非本次生成产物）**：

| 段 | 主导功能 | 承载信息 | 来源（O3 枚举） |
|---|---|---|---|
| P1 | Hook→Tension：召回"可见痕迹"默认框架遗漏"缺陷生成→正式纠正行动"双边际 | 治理者集合未定；gap=Inadequacy | `routing:Inadequacy` + 张力底本候选 `03-structural-blindspot#1`（gamache2020） |

**h 结论**：✅ 通过——覆盖率触发 `<80%` 分支，门输出为全量重写要求而非句级修补，与 §7 判定项 h 的通过标准一致。

---

## d｜5 条失败原句回归（登记层 `channel=rule, risk=high` 固定回归集）

喂入草稿中 5 条原句**全部在场**（行号按 `_deepened_20260914.md`）。逐条按其 `rule_locator` 单一源判定并给出既定改写：

| # | 回归 id | 原句（草稿行） | 判定 | 单一源 | 改写（引用单一源既定转写/示例） |
|---|---|---|---|---|---|
| 1 | posture-godseye-recall-counts | "Annual serious recall counts are therefore governance outcomes. They show…"（:26） | **FAIL·姿态**（定义式 `are therefore` + 事实语气 `show`） | `generation-protocol.md` §五 G4 回归 case | "Annual serious recall counts may reflect how governance structures shape which known defects are converted into public action. These counts are consistent with a governance-channel account, in which ownership conditions can change the incentive to act on a known defect."（G4 逐字改写示例） |
| 2 | meta-language-sign-estimand | "The sign is the estimand, not the contribution."（:30） | **FAIL·元语言**（`estimand` 出方法语境外；JOM 元句容受=未核查→默认转论文语言） | `water-level-gate.md` §三 row 1 | "The direction of this association is not the contribution itself; the contribution is the mechanism through which it arises."（门内既定转写） |
| 3 | boundary-implication-equally-bounded | "…the implication is equally bounded."（:36） | **FAIL·预算**（mixed-evidence caveat 在 :34 已完整披露一次，:36 二次披露超"≤1"；收尾非肯定式范围句） | `water-level-gate.md` §二 | "These boundaries are scope conditions, not uniform effects."（肯定式范围句；mixed evidence 保留 :34 一次集中披露） |
| 4 | meta-language-adjudication-nonexclusive | "Supplementary adjudication remains nonexclusive:"（:34） | **FAIL·元语言**（`adjudication` / `nonexclusive`） | `water-level-gate.md` §三 row 4 | "Supplementary analyses provide diagnostic evidence:"（按 row 4 `supplementary evidence / diagnostic evidence` 转写） |
| 5 | generic-thesis-central-thesis | "Our central thesis is that greater common institutional ownership…is associated with fewer…"（:30） | **FAIL·具体性**（第一人称占位论点句，零理论信息，可原样放进任意论文） | `generation-protocol.md` G3 边界翻译表 + `contrast-pairs/04-generic-thesis-and-contributions.md` | "Although a large stake in the focal firm can accelerate correction (Darby et al. 2026), we show that ownership spanning product-market rivals changes the objective of external governance and is associated with fewer annual serious recall counts."（Although…we… 转换式，点明被转换的理论关系） |

**超出固定回归集的额外命中**（同一草稿，如实记录）：§三元语言 row 4 的 `bounded scope conditions`（:36）；§二防御堆叠两条已核实实例（:36 "should not be presumed…"、:32 "not independent contextual additions…"）亦全部在场——该草稿在预算维度的实际违规数高于固定回归集的 5 条。

**d 结论**：✅ 通过——5/5 判 FAIL 且改写均出自单一源既定文本（非临场自拟），与 §7 判定项 d 的通过标准一致。

---

## 汇总与诚实边界

| 判定项 | D-07（2026-09-14） | 本补测（2026-09-15） | 合计证据 |
|---|---|---|---|
| a 大纲表来源可核 | ✅ | — | D-07 |
| b blueprint 卡实际消费 | ✅ | — | D-07 |
| c 借句表 id 可定位 | ✅ | — | D-07 |
| **d 5 条回归** | ⚠ 仅间接 | **✅ 5/5 FAIL+改写** | 本补测 |
| e 预算 | ✅ | （额外命中佐证） | D-07 + 本补测 |
| f 元语言 | ✅ | — | D-07 |
| g 检索非空 | ✅ | 回归脚本 43/43 复跑全绿（同日 commit 14567d8） | D-07 + 复跑 |
| **h 重写门** | ✗ 未跑 | **✅ 0%→全量重写** | 本补测 |
| i 迁移完整性 | ✅ | — | D-07 |

- 按 §7 通过线（≥7/9 且 a/c/d/h 必过）：**9 个判定项现全部有通过证据**。
- 边界 1：h/d 为门逻辑触发测试（既成草稿为输入），不替代 fresh-session 完整生成验收；第二轮 Batch 7 的"每个 write-* skill 各跑一次真实生成（第二个项目）"仍未执行，仍是两轮方案共同的最大剩余缺口。
- 边界 2：改稿路径的完整 G1 重启（真的重落大纲表与借句表并重渲染全文）本次未执行——门已给出重启要求与可执行示例行；完整重启属于一次真实改稿任务，非验收补测范围。
- 边界 3：术语作用域提示——"Our central thesis is that" 在 `story-blueprints/v4/rhetoric-moves/mechanism-two-chain.md` 的信号词表中是**理论节**主题句信号；在 **Introduction 贡献段**语境它才是登记失败句（contrast-pairs 04）。信号短语按节取用，不构成两源矛盾。
- 回归集固化：5 条已登记于 `write-introduction/corpus/_skill_design_feedback.yaml`（`channel: rule` / `risk: high` / `regression_cases.positive` 带 prompt 与 invariants）；本报告为该回归集的首次实测记录，后续改动水位门 / G4 后可按同法重跑。
