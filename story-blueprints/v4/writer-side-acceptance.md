# v0.4-lite 首轮写作侧验收（检索脚本修复后复测）

> **本版状态**：检索脚本语义修正 + Tier fallback + 标签归一 + 退化 tier 护栏 + `--explain` 落地后复测（方案 §P1-4 / Batch 3）。
> **口径**：以下 Case A/B/C 的预期一律改写为**本机实测行为**（命令见文末）。原 `writer-side-abstain` 期望空结果已过时；`writer-side-fini` 经标签归一后重新命中 Fini。
> **契约口径**：`story-blueprints/references/retrieval-contract.md` 的 **1 primary + 1 contrast 上限**与**每结果四要素**（matching reason / one learnable move / one non-transferable condition / one comparison question）保持不动；脚本产前三项，第四项 comparison question 由消费 skill 按 `v4/rhetoric-moves/_immediate-exemplar-protocol.md` step 3 产出。

## 验收范围

本验收测试 `write-introduction` 的 Phase 1.5：研究描述经人工 story gate 形成当前调用的临时检索请求，再由 `retrieve_exemplars.py` 执行严格匹配。它**不**测试、也不声称存在一个自动从自然语言抽取 `validated_conditions` 的分类器；条件确认仍属于写作技能的理论诊断责任。

每个通过的案例都必须满足两项：

1. 返回的学习对象与该次 story gate 已确认的结构相符；
2. 推荐不将范文改写成当前项目的强制 story frame，并清楚给出不可照搬条件。

## 字段语义（`--explain` 与每结果字段）

| 字段 | 含义 |
|---|---|
| `tier` | 产出该结果的 fallback 档位（一次运行内取第一个非空档，故同次结果同档）：`1` = `suitable=="yes"` + 严格相关（request 带 `retrieval_signals` 时要求 signals 交集，否则要求 `narrative_dynamics` / `theoretical_problem_form` 命中）；`2a` = 去掉 signals 要求、保留 tag 命中；`2b` = 再把 `suitable` 放宽到 `partial`；`2c` = 再丢掉 tag 要求，只按 `outlet` 或 `paper_type` 同类候选。若某档的全部候选同时 `theoretical_problem_form` 命中为空且 `unmet_conditions≥1`，该档被标 `degenerate=true, skipped=true` 且不锁定结果，检索继续下探。 |
| `relaxed` | 相对 tier 1 累计放宽的规则：`1`=[]；`2a`=[`retrieval_signals`]；`2b`=[`retrieval_signals`,`suitable<=partial`]；`2c` 再加 `relevance>=outlet+paper_type`。 |
| `signals_hit` | 该卡实际命中的三类标签交集：`retrieval_signals` / `narrative_dynamics`（=request 的 `story_needs`）/ `theoretical_problem_form`。两侧标签先过 `references/tag-normalization.yaml` 归一，再求精确交集；无 embedding/语义/子串匹配。 |
| `validation` | `known` = request 的 `validated_conditions` 非空；`unknown` = 该字段为空/缺省。`unknown` 表示「未声明已验证条件」，**不表示卡没有 requires**——requires 全部按未验证计入 `unmet_conditions` 作排序罚分。 |
| `unmet_conditions` | 卡 `section_learning.<section>.requires` 中未被 request `validated_conditions` 覆盖的条件。它是**排序罚分（每条 −15）**，不是硬门；卡仍可入选并带此标注。 |
| `low_confidence` | 仅当四档都只产生退化候选、不得不回退到最后一个退化档时为 `true`，并附 `low_confidence_reason`；正常命中为 `false`。 |
| `no_match` | 四档全空时的原因串；`--explain` 另给 `gate_eliminations`（cautionary_case / suitable_not_yes_tier1 / relevance_no_match_tier1）与 `requires_unmet_but_ranked`。 |

## Case A — Zhou 型：同一过程内的真实理论冲突

### 研究描述

某研究考察企业在进入新的数字生态系统后是否更可能实现持续创新。资源获取逻辑认为，生态系统嵌入带来互补资源与信息，因而应促进创新；资源利用逻辑认为，嵌入带来协调、依赖与路径锁定，因而会抑制创新。两套逻辑均针对同一焦点关系，且现有证据相互矛盾。研究不是把两组企业、两个结果或两个时间段分别交给不同理论，而是主张两种机制分别作用于同一创新过程中的资源获得与资源整合环节，并可推出一个联合预测。

### Story gate

- 主 gap：Incommensurability + Confusion。
- 已验证：`genuine-theory-conflict`、`same-causal-process-facets`。
- 未验证：不同结果过程、跨受众评价、机制悖论或理论适用域转移。

### 临时请求与实测行为

- Request：`tests/fixtures/writer-side-zhou-request.json`
- 实测返回 2 条（仍与 story gate 相符）：
  1. `zhou2017` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=known`，`unmet_conditions=[]`；`signals_hit.narrative_dynamics=[clarify-theme, establish-genuine-tension, theory-as-rising-action]`、`theoretical_problem_form=[competing-explanations, mixed-evidence]`。
  2. `ridge2013` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=known`，`unmet_conditions=[theory-domain-shift]`；`signals_hit.theoretical_problem_form=[competing-explanations, mixed-evidence]`。

### 写作端应显示的推荐（不变）

**学习对象：Zhou (2017)**（`ridge2013` 为对照对象；两者均需附四要素）

- 匹配理由：当前研究已确认两种既有解释对同一关系形成真实冲突，并且它们可落在同一过程的可区分 facet。
- 学习动作：先让两种解释各自以独立机制成立，再说明它们如何共同导出单一逻辑无法得到的联合预测。
- 不可照搬：只有当两个 facet 可被理论化并被证据区分时才可采用；不能把「文献结论混杂」或一个二次项当作冲突整合。`ridge2013` 的不可照搬条件即其 `unmet_conditions=[theory-domain-shift]`。
- 对照问题：本研究的两个机制是否真的属于同一因果过程，而非两个不同 outcome process？

**判定：通过。** 推荐学习结构而未指定研究必须采用 Zhou 的曲线、情境或贡献。

## Case B — Fini 型：跨受众的部分不可通约（标签归一后实测恢复 Fini）

### 研究描述

某研究考察独立纪录片制作人获得流媒体平台采购后，是否更容易得到电影节评审资助。电影节评审能将平台采购视为制作与项目执行能力的可观察线索；但当平台采购累积到很高程度时，它也可能让评审怀疑制作人是否仍符合艺术电影共同体期待的创作身份。两类受众并非完全无共同标准：平台认可仍有能力信息；冲突在于艺术共同体的身份规范与平台商业成功所传达的身份意义不完全对齐。研究可观察平台采购、电影节资助和艺术共同体的既有认证。

### Story gate

- 主 gap：Inadequacy；既有同行间社会评价传递理论的边界被错误外推到外部受众。
- 已验证：`cross-audience-valuation`、`shared-ability-baseline`、`identity-criteria-misalignment`。
- 未验证：同一 X–Y 的两套竞争理论、两个独立 outcome process、或一般性的多中介悖论。

### 临时请求与实测行为

- Request：`tests/fixtures/writer-side-fini-request.json`
- 标签归一：请求侧 `theoretical_problem_form=cross-audience-partial-incommensurability` 经 `references/tag-normalization.yaml` 归一到卡侧 `cross-audience-partial-criterion-overlap`；两侧再求精确交集（无 embedding/语义/子串）。
- 实测返回 2 条（**主学习对象恢复为 Fini**）：
  1. `fini2017-social-valuation` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=known`，`unmet_conditions=[]`，`score=70`；`signals_hit.theoretical_problem_form=[cross-audience-partial-criterion-overlap]`、`narrative_dynamics=[]`、`retrieval_signals=[]`。
  2. `chen2009` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=known`，`unmet_conditions=[dual-literature-intersection]`，`score=55`；`signals_hit.theoretical_problem_form=[cross-audience-partial-criterion-overlap]`。
- `zhou2017` 现排在 `fini2017` 之后（`score=45`，两条 unmet），受 1+1 上限不再返回。

### 写作端应显示的推荐（按实测恢复）

**学习对象：Fini (2017)**（`chen2009` 为对照对象；两者均需附四要素）

- 匹配理由：归一后的 `cross-audience-partial-criterion-overlap` 让 fini 卡在 tier 1 以 `suitable=yes` + `paper_type` 同型 + `published`/`complete` 直接命中，`unmet_conditions=[]`。
- 学习动作：把「同一可观察信号被两类受众分别读作能力与身份」的双重读法前置，让理论透镜分解机械地生成倒 U 预览与通道匹配调节，而非断言预测。
- 不可照搬：本项目若没有「外部评价—能力相关性—身份规范不对齐」三件套，则不能套用 Fini 的倒 U 与通道匹配结构；`chen2009` 的不可照搬条件即其 `unmet_conditions=[dual-literature-intersection]`。
- 对照问题：本研究的平台采购是否真的同时携带能力信息与身份信号，还是只改变信息量而非身份意义？

**判定：通过。** 归一映射恢复了 story gate 已确认的跨受众结构匹配；`low_confidence=False`。

## Case C — 弃权由 story gate 承担（`validation=unknown` 语义）

### 研究描述

某研究考察 CEO 的国际经历如何影响企业绿色创新。现有研究重视高管认知和外部制度压力，但较少讨论国际经历如何改变 CEO 对跨国监管信息的注意与解释。作者计划检验 CEO 国际经历、监管注意和绿色专利之间的关系，并收集多个控制变量和一个可能的调节变量。

### Story gate

- 主 gap：Incompleteness。
- 没有证实理论对同一关系的真实冲突；没有外部评价经焦点受众转译的结构；没有两条反向机制共同重定向同一过程；没有不同结果过程。
- 因此 `validated_conditions: []`。按现行语义这只表示**未声明已验证条件** → `validation=unknown`，**不表示必须弃权**，也不表示卡没有 `requires`。

### 临时请求与实测行为

- Request：`tests/fixtures/writer-side-abstain-request.json`
- 实测返回 2 条（**脚本不弃权**）：
  1. `moon2026-trade-secret-protection-advertising` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=unknown`，`unmet_conditions=[]`，`score=70`；`signals_hit.theoretical_problem_form=[incompleteness]`。
  2. `zhou2017` — `tier=1`，`relaxed=[]`，`suitable=yes`，`validation=unknown`，`unmet_conditions=[genuine-theory-conflict, same-causal-process-facets]`，`score=25`；`signals_hit.narrative_dynamics=[clarify-theme]`。

### 写作端应显示的推荐（弃权判定在写作端）

- `validation=unknown` 只说明本次调用未声明已验证条件；它**不等于**「必须弃权」。脚本继续返回候选（`moon2026` 无 requires、`zhou2017` 带两条 unmet），弃权不再由空结果承载。
- 本 case 的弃权依据是 **story gate 自身**：它已明示没有可证实条件、也没有与返回卡同构的结构。写作端应据此显示「当前库无适合的 Introduction 学习对象，继续按项目自身理论诊断构建」，而不把 `moon2026` / `zhou2017` 当作匹配推荐。
- **不得**把 `validated_conditions=[]` 重新定义为「必须弃权」的门；也**不得**将 `moon2026`（贸易秘密 × 广告）作为本项目的学习对象。

**判定：通过（判定责任在 story gate + 写作端）。** 脚本层面不弃权，弃权由 story gate 显式判定承担；下游不得把非空结果误当推荐。

## 补充实测

- `cross-audience-valuation-introduction-request.json`：与 fini 打同一归一标签，实测 `fini2017-social-valuation` — `tier=1`，`score=70`，`unmet_conditions=[]`；`chen2009` 紧随（`score=55`，`unmet=[dual-literature-intersection]`）。
- `distinct-outcomes-introduction-request.json`：实测 `wowak2025` — `tier=2b`，`relaxed=[retrieval_signals, suitable<=partial]`，`suitable=partial`，`validation=known`，`unmet_conditions=[]`，`score=50`，`signals_hit.theoretical_problem_form=[cross-literature-gap]`；`gate_eliminations` 显示 tier 1 / 2a 候选为 0、2b 候选为 1。
- 退化 tier 护栏实测：`vertical-screening-request.json` 的 tier 2a 唯一候选同时 `theoretical_problem_form` 命中为空且 `unmet_conditions≥1`，`tier_attempts` 标 `degenerate=true, skipped=true`，检索继续下探，tier 2b 以 `pupovac2025`（tpf 命中）入选；未出现 `low_confidence`。
- 回归脚本：`python tests/regression_retrieval.py` → `ALL REGRESSION ASSERTIONS PASSED`（R1 fini 主推 fini2017；R2 abstain 非空且 `validation=unknown`；R3 distinct-outcomes 走 2b；R4 全量 fixture 0 空结果）。
- 全量 fixture 回归：本机 `tests/fixtures/*-request.json` 共 **43** 个，实跑 **0 空结果**。（任务书所记「45 个」与本机实测不符；以本机 43 为准。）

## 已知限制（如实登记，不作为已通过项）

1. **标签词表仍稀疏（`cross-audience-*` 首组已归一，其余未覆盖）**。`tag-normalization.yaml` 首批只归一了跨受众评价家族；其他请求侧标签若与卡侧词面不匹配仍会落空。触发条件：请求标签在卡侧无同形词且不在归一表内（例如未来出现新的结构别名）。预期收益：每补齐一组已确认别名，就减少一次「仅靠 `story_needs` 命中语义泛化卡」的降级。当前状态：Case B / cross-audience fixture 已由首组归一修复，`low_confidence=False`。
2. **`tier2a` 仅在 request 带 `retrieval_signals` 时才有别于 tier1**。tier 1 在无 signals 时已回退到 `narrative_dynamics` / `theoretical_problem_form` 命中；此时 tier 2a（=去掉 signals 要求、保留 tag 命中）与 tier 1 的准入集合相同。对无 signals 的请求，该档空转，真正放宽只从 2b 起。触发条件：request 缺 `retrieval_signals`。预期收益：修复后 `--explain` 的 `tier_attempts` 不再于 1 与 2a 重复计数同一批候选，2a 的候选数才可当作放宽证据。

## Backlog（登记；已实现项与未完成项分开）

- **T1｜`requires` + `theoretical_problem_form` 作 tier 资格护栏**：触发条件 = 某 tier 全部候选同时 `theoretical_problem_form` 命中为空且 `unmet_conditions≥1`；预期收益 = 不放行语义泛化命中，继续下探更强档位。**已实现**（退化 tier 护栏 + `low_confidence` 标注）。
- **T2｜标签词表归一（`cross-audience-*` 系列）**：触发条件 = 同一结构在 request 与卡侧存在 ≥2 组词面不匹配的已知别名；预期收益 = 消解限制 ① 的具体实例，恢复 Fini 型结构匹配。**首组已实现**（`references/tag-normalization.yaml`，4 个 surface）；**未完成**：词表其余别名待补，见限制 1。
- **T3｜`tier2a` 与 `tier1` 在无 signals 请求下的空转去重**：触发条件 = request 缺 `retrieval_signals`；预期收益 = `--explain` 不再把同一批候选在 1 与 2a 重复计数，见限制 2。**未实现**。

## 结论

修复后的脚本在字段可审计性上达标（`tier` / `relaxed` / `signals_hit` / `validation` / `unmet_conditions` / `low_confidence` 齐全，空结果附原因）。**Case A、Case B 均构成完整通过**（Case B 由标签归一恢复 Fini 主推）；**Case C** 的弃权责任在 story gate + 写作端，`validation=unknown` 不再被当作弃权门。限制 1（词表其余别名）与限制 2（2a 空转）仍登记未完成。该验收只支持 Introduction 的试点继续使用；Theory、Methods、Results 不因此自动接入。

## 复现命令

```bash
cd story-blueprints
python scripts/retrieve_exemplars.py --request tests/fixtures/writer-side-zhou-request.json --explain
python scripts/retrieve_exemplars.py --request tests/fixtures/writer-side-fini-request.json --explain
python scripts/retrieve_exemplars.py --request tests/fixtures/writer-side-abstain-request.json --explain
python scripts/retrieve_exemplars.py --request tests/fixtures/cross-audience-valuation-introduction-request.json --explain
python scripts/retrieve_exemplars.py --request tests/fixtures/distinct-outcomes-introduction-request.json --explain
python tests/regression_retrieval.py
```
