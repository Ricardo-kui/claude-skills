# Generation Protocol — 生成层协议（G1–G5）

> **单一事实源**：本文件是 leading word「底本」与「借句表」的唯一权威定义处。`SKILL.md`、`outline-protocol.md`、`render-rules.md` 只引用本协议，不复述其定义。
> **位置**：Phase 3 渲染之前、Phase 4 水位门之前。上游 = 大纲表（`outline-protocol.md`）；下游 = 水位门（`water-level-gate.md`）与审查契约（`pass-contract.md`）。
> **分工**：段落**论证角色**组装见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`；模块**渲染**检查见 `render-rules.md`；**句子表达**细节（五病 / AI 腔 / specificity / 节奏 / 术语密度）见 `corpus/storytelling/prose-craft-checklist.md` 与 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md`。本协议只写"如何把底本变成最终句子"的步骤与产物。

## 触发分支

**任何要产出最终句子的请求都走本协议**——含完整 Introduction、单模块、以及改稿（含"不够像范文"的返工）。触发不按篇幅判定；只请求诊断或大纲、不产出句子的请求不触发。

## 一、两个 leading word 的权威定义

### 底本（exemplar base）

底本 = 可 verbatim 借用的范文句骨架，附 `id` 与 `citekey`。唯一来源是骨架索引 `corpus/_skeleton/<module>.md`（路由见 `corpus/_skeleton/_index.md`）；`<module>` 取值见 SKILL.md Phase 3 语料指针表的「骨架」列。

- 每条底本都带状态列：`verbatim`（逐字底本）或 `模板`（填槽骨架）。**`模板` 不可当逐字底本**，借用时按填槽处理。
- 底本借用 = **只替换来源特异内容，骨架节奏与结构词保留**。
- `citekey` 继承自卡片，索引不改写卡片既有标注。遇到卡片自身标注与 citekey 冲突（例：`12-contrary-to-belief#1`）或 `未标注` 时，**保留状态列原样引用、不自行更正**，并在借句表备注登记该冲突。
- 底本状态为 EMERGING（单源）时，借句表该行加「单篇来源」标记，正文采用处保持该认知（不得当已验证惯例使用；三带判据见 registry/INDEX）。

### 借句表（exemplar-borrowing table）

借句表 = 每段一行的六列表，进输出合同：

| 段落 | 主导功能 | 底本 id | 借用骨架 | 替换清单 | 保留节奏 |
|---|---|---|---|---|---|
| P1 | … | `03-data-shock#3`（darby2025）或 `self-drafted` | 底本原句 / 模板骨架 | 专名/行业/样本/年份/数字 | 先现象后理论 |

- 底本 id 只能取自 `corpus/_skeleton/<module>.md`；无对应底本时填 `self-drafted`，并如实记录占比。
- 替换清单逐项列出被替换的来源特异内容（专名 / 行业 / 样本 / 年份 / 数字）。
- 保留节奏从三型中选一并写死：**先主张后限定 / 先对立后裁定 / 先现象后理论**。

> 上表为格式示意，不是可套用的段落清单。

## 二、G1 借句表

1. 按大纲表逐段启动：每段先落借句表行，再渲染该段正文（先借句表，后正文）。
2. 底本 id 只允许引用 `corpus/_skeleton/<module>.md` 的 id；形状包（`corpus/packs/`）只提供 id 引用，不复制 verbatim。
3. 无对应底本时填 `self-drafted`，并在表下记录其在全表占比（大纲表的 `self-drafted` 登记口径见 `outline-protocol.md` O3，不在此复述）。
4. 借句表进输出合同固定位置，作为 G2 落句的准入产物。

**完成判据（是/否）**
- 借句表出现在每次生成输出的固定位置？
- 每段一行的底本 id 非空（索引 id 或 `self-drafted`）？
- 全部底本 id 可在 `corpus/_skeleton/<module>.md` 定位？

## 三、G2 落句

固定顺序（逐级执行）：
1. 取底本骨架；
2. 替换来源特异内容（专名 / 行业 / 样本 / 年份 / 数字）；
3. 填本文构念与方向；
4. 校验原句节奏（先主张后限定 / 先对立后裁定 / 先现象后理论）是否保留。

错误顺序 = 先写通用正确句，再"让它像范文"。

**完成判据（是/否）**
- 借句表逐段有底本 id（索引 id 或 `self-drafted`）？
- 每段「保留节奏」栏已填，且取值属三型之一（先主张后限定 / 先对立后裁定 / 先现象后理论）？
- 每段「替换清单」栏非空，且来源特异内容已全部换成本文对象？

## 四、G3 边界翻译表

行 = 本项目实际锁定约束（**权威在项目态**：canonical `story` / `story.integrity` 的锁定边界清单；本表只是其语言化映射，权威声明见 `pass-contract.md` 的 `boundary_compliance`）。列 = 锁定约束 | 今日失败写法（事实记录）| 论文语言底本 | 底本状态 | 出现位置。

**取证范围**：骨架索引 verbatim 全量（口径见 `corpus/_skeleton/_index.md` 的「合计」行），按修辞功能检索（不止六篇范文）。找不到正面底本的行填 `self-drafted`，并在「待扩池登记」列出。登记方式：`_skill_design_feedback.yaml` 以 **slug 键**登记条目（无 `P2-*` 编号体系），登记字段为 `proposed_change.action`，取值 **`append_variant`**（语料变体需求）。

| 锁定约束 | 今日失败写法（事实记录） | 论文语言底本 | 底本状态 | 出现位置 |
|---|---|---|---|---|
| sign 不是贡献 | "The sign is the estimand, not the contribution."（`Introduction_0913_polished.md:28` / `_deepened.md:30`） | `self-drafted`（骨架索引 verbatim 全量无正面底本；口径见 `corpus/_skeleton/_index.md`；见待扩池登记） | self-drafted | Contribution 首句 |
| mixed evidence 集中披露 | 结果段与贡献段各披露一次（`_polished.md:32` 边界段 + :34 贡献段） | `01-general-theory-practice#1`（zhou2017）"empirical evidence is mixed on the effects of state ownership on innovation… To resolve the theoretical and empirical inconsistencies… we theorize…" | verbatim | Preview 一次集中披露 |
| recall count 非纯质量 | "the implication is equally bounded"（`_polished.md:34` / `_deepened.md:36`） | `corpus/packs/portfolio-governance.md` §P1 Hook（:19）模板底本（:25）——"…reflects [more than incidence]; it also records [conversion into public action]."（来源 archetype，非逐字底本） | 模板 | Preview / 边界句 |
| timing 仅作裁决 | "Supplementary adjudication remains nonexclusive"（`_polished.md:32` / `_deepened.md:34` / `_rewritten.md:29`） | `self-drafted`（骨架索引 verbatim 全量无正面底本；口径见 `corpus/_skeleton/_index.md`；见待扩池登记） | self-drafted | Preview 裁决句 |
| 不写因果 | "Annual serious recall counts are therefore governance outcomes. They show…"（`_polished.md:24` / `_deepened.md:26`） | `mechanism-preview#20`（ridge2013）"they may provide internal support to the mechanisms… as relevant explanations of the relationship…" | verbatim | 结果 / 边界句 |
| 不写质量收益 | "bounded scope conditions, not as evidence that common ownership is uniformly beneficial or harmful"（`_polished.md:34` / `_deepened.md:36`） | `theory-lens-driven-preview#3`（wowak_2020_female_directors_recalls，verbatim）"we do not theorize that adding female directors should influence all types of recalls equivalently; doing so might lead to the false implication that adding female directors worsens product quality." | verbatim | Preview / 贡献段 |

> **row「不写质量收益」换底本理由**：原底本 `robustness-preview#3` 的修辞功能是排除竞争行动者（null 结果支撑 board 而非 managers 定调），与「不写质量收益」不同层；`theory-lens-driven-preview#3`（同索引、同一论文 wowak_2020）先命名并否定一个质量维度误读，再改写为权变关系，与失败写法 `…not as evidence that common ownership is uniformly beneficial or harmful` 逐点对应。

### 待扩池登记

- **sign 不是贡献** → `self-drafted`。骨架索引 verbatim 全量（口径见 `corpus/_skeleton/_index.md`）无正面底本；登记为 `append_variant`（语料变体需求），进 `_skill_design_feedback.yaml` triage。
- **timing 仅作裁决** → `self-drafted`。同上；登记为 `append_variant`。

> 登记只记需求，不自拟句冒充底本；变体落地后回填本表 id。

> 防御文风类（"should not be presumed…"）与边界独立性类（"not independent contextual additions…"）不属任何锁定约束的语言化实例，已移入 `water-level-gate.md` §预算「防御堆叠的已核实实例」；本表每行只保留真正违反该约束的实例。

**完成判据（是/否）**
- 六行齐全？
- 每行「论文语言底本」栏标 id、「底本状态」栏标状态（`verbatim` / `模板` / `self-drafted`）？
- `self-drafted` 行已在「待扩池登记」注明白底缺失与登记去向？

> **镜像**：同一底本来源按**失败案例**组织的对照卡（失败句 × 底本 id × 差异字段）见 `../corpus/contrast-pairs/_index.md`；本表按约束类型组织，两目录互为镜像。

## 五、G4 机制语气库

可定位的底本（各自标来源行）与它们处理的机制类型：

| 语气底本 | 来源（文件:行 / 索引 id） | 处理的机制类型 |
|---|---|---|
| `we theorize` | `01-general-theory-practice#1`（zhou2017，`_skeleton/stakes.md`）；`02-actor-funnel#3`（darby2026，`_skeleton/transitions.md`） | 本文提出的构念—构念连接；把未观察机制写成作者的理论主张 |
| `we argue` | `06-paradigm-challenge#1`（gamache2023，`_skeleton/hooks.md`） | 对既有解读的纠偏与再框架；声明本文立场 |
| `may reflect` | **索引外底本**（无 `_skeleton/` 索引 id）——`gulati_2009_the_nature_of_partnering_experience_and_the_gain.sentences.md:491`（gulati_2009_the_nature_of_partnering_experience_and_the_gain，rhetoric-moves/sources） | 对已观察关联的替代解释；不把观察等同于机制 |
| `is consistent with` | **索引外底本**（无 `_skeleton/` 索引 id）——`fang_et_al_2025_rival_recall_ad_spend.sentences.md:75`（fang_et_al_2025，rhetoric-moves/sources）；`additional-analysis-embedding.md:42`（rhetoric-moves） | 证据与机制的相容性；补充分析作为裁决而不宣称确认 |
| `can change` | **索引外底本**（无 `_skeleton/` 索引 id）——`anand_mukherjee_2024_learning_from_failures_di.sentences.md:339`（anand_mukherjee_2024，rhetoric-moves/sources） | 条件/能力改变行为；机制起作用的能力面 |
| `can bundle` | **未定位底本**——骨架索引 verbatim 全量（口径见 `corpus/_skeleton/_index.md`）与 rhetoric-moves 正文均无该语气动词的 verbatim；`bundles of resources` 类命中的是名词短语，不构成机制语气底本 | （暂无） |

### 回归 case（必须写死）

原句：

> "Annual serious recall counts are therefore governance outcomes. They show…"

判定：**姿态不合格**。`are therefore` 把未观察的治理机制写成定义式断言，`They show…` 把观察事实直接当作机制证据——属上帝视角（定义式 `is/are` + 事实语气 `show`）。

改写示例（用本语气库）：

> "Annual serious recall counts may reflect how governance structures shape which known defects are converted into public action. These counts are consistent with a governance-channel account, in which ownership conditions can change the incentive to act on a known defect."

**完成判据（是/否）**
- 五个可定位底本各有来源行？
- `can bundle` 如实标"未定位底本"？
- 回归 case 判为姿态不合格并给出一条改写？

## 六、G5 完成判据汇总

对任一次生成，以下每条都能用"是 / 否"回答：

1. 借句表已产出，且每段底本 id 非空（索引 id 或 `self-drafted`）？
2. 全部底本 id 可在 `corpus/_skeleton/<module>.md` 定位？
3. G2 四步顺序在借句表"替换清单 / 保留节奏"栏可核对？
4. G3 六行齐全，每行「论文语言底本」栏标 id、「底本状态」栏标状态（`verbatim` / `模板` / `self-drafted`），`self-drafted` 行已登记去向？
5. G4 的机制语气选择在正文可指认，回归 case 已判 FAIL 并给出改写？
6. 底本覆盖率（见 `water-level-gate.md`）已计算并触发重写/修补分支？
