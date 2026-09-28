---
type: canonical_preview
canonical_id: "context-agent-justification"
status: VERIFIED
function: "Preview 家族的情境辩护型：在引言内论证经验场域（执法/监管/认证类权威代理）与理论构念的操作对应，并用含命名外生冲击的样本窗口为调节变量变异提供双重可得性论证。"
generativity: ADAPTABLE
exclusivity: MEDIUM
created: 2026-09-28
source: "corpus_writeback.py create_new_file（gate ① 裁决新建模块）"
---

# context-agent-justification — Preview 家族的情境辩护型：在引言内论证经验场域（执法/监管/认证类权威代理）与理论构念的操作对应，并用含命名外生冲击的样本窗口为调节变量变异提供双重可得性论证。

## 功能描述
Preview 家族的情境辩护型：在引言内论证经验场域（执法/监管/认证类权威代理）与理论构念的操作对应，并用含命名外生冲击的样本窗口为调节变量变异提供双重可得性论证。


## 适用场景
- 以执法/监管/认证类权威机构为经验场域的研究（证券监管、产品召回监管、认证机构、审查机构）；样本窗口内恰好有研究者不可操纵的命名外生冲击提供调节变异时首选；Incompleteness × Mechanism/Boundary；AMJ/SMJ archival 研究的引言第三/四段


## 验证状态
### 单源验证
- 新建文件：context-agent-justification.md | 变体 A：执法代理操作映射+冲击窗口辩护型——情境宣告→代理选择理由→理论 DV 操作映射→含命名外生冲击的样本窗口→筛选逻辑+适当性收束（dewan2020，AMJ，EMERGING）
- 待第二篇跨论文复现后升 ROBUST


## 句法模板
### 变体 A：执法代理操作映射 + 冲击窗口辩护型（dewan2020 型）

> 论证角色：A&R（用"理论动作 ↔ 可观测行动"的操作映射与外生冲击窗口共同论证经验场域的适当性，为假设检验预置可信度）

**模板**:
> "We test our arguments in the context of [authority agent] actions against [targets] alleged of [violation]. We focus on [agent] as the focal [theoretical role] because [jurisdiction rationale]. A [agent action] is [operational definition mapping onto the theoretical DV] ([citations]). We examined [outcome] against [sample] from [year] through [year], a period that saw [N] major [exogenous shocks of the moderator's type]. [Measurement screen: the event that forms the sample detects alleged violations, whereas the DV reflects the authority's adjudicated decision]. The importance of [agent action] as [theoretical act] and the occurrence of [shocks] make [context] an appropriate empirical context for testing our theoretical arguments."

**来源**: dewan_jensen_2020 (AMJ), P3

**原文锚定**:
> "We examined the likelihood of enforcement action against firms accused of securities fraud (identified through class action lawsuits) from 2006 through 2011, a period that saw two major corporate scandals – the stock options backdating scandal of 2006-2007 and the subprime mortgage scandal of 2007-2009." / "The importance of SEC enforcement action as labeling of misconduct and the occurrence of two scandals in the period under consideration make SEC enforcement action an appropriate empirical context for testing our theoretical arguments."

**关键特征**:
- 五步结构：情境宣告 → 代理选择理由（jurisdiction/authority）→ 操作映射（理论 DV ↔ 具体行动）→ 含命名外生冲击的样本窗口 → 筛选逻辑+适当性收束
- 操作映射把理论语言逐字绑定到可观测行动（labeling of misconduct ↔ enforcement action），在 Methods 之前先保护 DV 的构念效度
- 筛选句区分"构成样本的事件"（class action = detection/allegation screen）与"结果变量"（enforcement = adjudicated labeling），预防"用检测当结局"的测量混淆
- 适当性收束 = 双重可得性论证：理论动作（labeling）在场域中高频且后果重大 + 调节变量（scandal）的天然变异恰好落在样本窗口内——两个条件合取，缺一不可

**适用**: 以执法/监管/认证类权威机构为经验场域的研究（证券监管、产品召回监管、认证机构、审查机构）；样本窗口内恰好有研究者不可操纵的命名外生冲击提供调节变异时首选；Incompleteness × Mechanism/Boundary；AMJ/SMJ archival 研究的引言第三/四段

**禁忌**: 外生冲击必须是窗口内真实发生的命名事件，不能许诺"准实验"却只给行业 dummy；操作映射两侧要一一对应，若理论 DV 与代理行动存在系统偏差（如和解不等于有罪认定），须在 Methods 补充分离检验；适当性收束句不要重复罗列前文全部理由，只保留双重可得性两条


## 组装规则
### 互斥

- 外生冲击必须是窗口内真实发生的命名事件，不能许诺"准实验"却只给行业 dummy；操作映射两侧要一一对应，若理论 DV 与代理行动存在系统偏差（如和解不等于有罪认定），须在 Methods 补充分离检验；适当性收束句不要重复罗列前文全部理由，只保留双重可得性两条

<!-- wb:dewan_2020_catching_the_big_fish_the_role_of_scandals_in_mak:preview_context_agent_justification -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
