# Panel Review — 跨分支调解

改编自 ToC 论文 §3.5 与附录 C.5，加入 Edmans (2023) 的"可修复 vs 结构性"分诊与 Pollock Ch13 表13.1 的拒稿/修改标准。由**独立裁判模型**（阵容协议裁判槽，家族与全部分支隔离——跨分支调解不能由辩手家族自我复核）执行，编排者组装输入并派发（一次调用，逐条调解），裁判同时持有六个视角，做分支内主持人做不到的跨类别推理。裁判槽降级为编排者自审时（lineup-protocol §4.3），本协议原文嵌入编排者的 Panel 阶段。

## 输入（编排者组装进裁判模型 prompt）

- 全部存活条款（含 branch、moderator 裁决、evidence_verified 状态）
- 稿件路径（Panel 需要时可回查原文）
- 已声明局限清单

## Panel Prompt（逐条执行）

```
You are a review PANEL representing all six skeptic perspectives on a
management manuscript under review at {journal}:
Tension & Knot, Hook & Front-End Conversion, Conversation & Contribution
Claim, Characters & Storylines, Evidence Staging, and Promise & Payoff.

A category-specific skeptic produced the following claimed UNSTATED
weakness, which survived a four-stage debate (the authors' advocate could
not deflect it) and quote verification.

Your job is to cross-review:
1. Is the claim in the right category? (category drift check)
2. Is it materially subsumed by a concern another skeptic has also raised?
   (double-counting check — you see all branches' surviving claims)
3. Is the severity calibrated against the whole picture? (inflation check)
4. Was it in fact already stated or adequately handled by the authors?
   (novelty check — reject restatements of the acknowledged list)
5. Is it a substance concern or a delivery/craft concern? (delivery concerns
   are not rejected but rerouted: mark delivery_only=true)
6. Is it fixable by revision, or structural? (triage — Edmans: a paper may
   be rejected even if every issue is individually fixable, when the issue
   indicates a contribution-bar or framing problem too deep to converge)
   - revision_fixable: a test, measure, wording, or section can resolve it
     within the current framing
   - contribution_structural: resolving it requires reframing the question,
     changing the contribution claim, or switching outlets — not a patch

CLAIM UNDER REVIEW
Topic: {topic}
Branch (as claimed): {category}
Severity (as claimed): {severity}
Evidence quote: "{evidence_quote}" (section: {evidence_section})
Evidence verified against manuscript: {evidence_verified}
Revised description: {revised_description}
Authors' advocate response: {paper_response}
Moderator's rationale: {moderator_reasoning}

Output ONE verdict: endorse | reclassify | downgrade | merge | reject.
Additional rules:
- evidence_verified=false and no other verbatim passage independently
  supports the claim → reject (reason: ungrounded).
- A concern that is real but belongs to a different branch → reclassify.
- Two branches raising the same underlying issue → merge into the
  better-grounded one, record cross_category on both.
```

Output JSON:
```json
{"verdict": "endorse|reclassify|downgrade|merge|reject",
 "final_category": "knot|hook|conversation|characters|staging|payoff|<动态分支名>",
 "source_branch": "产生该条款的原分支（六固定名或 dynamic-N；reclassify 后仍保留溯源）",
 "final_severity": "minor|major",
 "fix_type": "revision_fixable|contribution_structural|delivery_only",
 "cross_category_concerns": ["..."],
 "reasoning": "..."}
```

动态分支条款的 final_category 规则：语义上能对应六固定类目的 reclassify 到固定类目（source_branch 保留动态分支名溯源）；对应不上的保留动态分支名，报告统计区单独计数。

## 裁决后处理

- `endorse` / `reclassify` / `downgrade`：进入最终报告，按 final_category 归类、final_severity 排序
- `merge`：保留更扎实的一条，另一条并入其 cross_category_concerns，报告合并计数
- `reject`：不进主表，留痕于统计区（含 reject 理由，供人工复核）
- `fix_type` 分诊（Edmans 2023 的可修/结构性 + Pollock Ch13 表13.1 的管理学化）：
  - `revision_fixable` → 进入修复优先级，路由到对应 *-review / write-* skill。表13.1 修改列的特征：可澄清、可补检验、可通过重构回应
  - `contribution_structural` → 单列“刊层风险”（见 output-format）：段落级补丁无法收敛的门禁问题——故事架构级失败（无可陈述的 knot、对话错位、预设答案、贡献主张换血）、或需重构问题/换刊（路由 `research-gap-diagnosis` / `grill-the-claim`；故事层另路由 `paper-story-contract` 重建故事契约）。表13.1 拒稿列的特征：贡献潜力不可见、对话不可识别、逻辑不连贯无法聚合为可检验主张——此类条款**不进**修复优先级
  - `delivery_only` → 进 minor 表标注“→ pollock-qc”

## 严重度最终语义（Panel 校准基准）

- **major**：审稿人可以据此写出 reject 或 major-R&R 的核心理由——故事架构层（无可陈述的 knot、预设答案、对话不可识别）、贡献门禁层（先验更新失败、单边 trade-off、受众错位）、或主张校准层（claim 超出设计/数字支持）的未声明弱点
- **minor**：真实但局部可修——补一个检验、改一处措辞、加一段边界条件讨论

**主张校准层的裁定基准（2026-09-23 用户裁定）**：claim 是否“超出设计/数字支持”以**主规格结果**为对照，不以稳健性/替代口径电池为对照——稳健性格与主规格不一致是观察性社会科学常态，不构成 major 来源；引言的总体支持陈述与理论解读是文体常规（范文：Darby 2026 JOM 引言全称宣告而 Table 6 多格 not-supported；military imprint LQ 结论全称重申而稳健性总表多格 Not support），要求**引言**加对冲、三档语言或竞争解释 qualifier 的条款直接 reject（feedback-registry `tcr_nohedge_front_20260923`）；本基准仅改变引言条款的裁定，Results/Discussion 的主张校准审查照旧；要求 supplementary 证据升位为并列结果的修复动作默认驳回（`tcr_supp_elevation_20260923`）。

**显式排序规则（top-K 选取）**：major 内部按 类别冲击先验 × evidence_strength × realism 排序——
1. 类别冲击先验（Pollock Ch13 表13.1 拒稿列标准映射到分支）：故事架构与贡献门禁（knot 无张力/预设答案；conversation 对话不可识别、先验更新失败——表13.1 前两行）> 人物与构念（characters 主角不清、构念未立）> 证据登台与主张校准（staging claim 超证、稳健性无名单）> 承诺兑现（payoff 承诺断裂、claim 跨节膨胀）> 读者转化（hook 前端失能）> 写作病（delivery_only）
2. 同类别内 substantial 证据 > moderate > weak（weak-evidence majors 默认 reject，见 debate-protocol 双轴规则）
3. structural（不可修订修复）在同严重度内优先列示——它改变作者的投稿决策，不只改变修订清单

期刊偏置：`AMJ` 时对话可识别与情境嵌入类条款从严；`SMJ` 时战略利害与新颖性（对战略对话的先验更新）从严；`OS` 时理论兴趣与反直觉性从严；`MSOM` 时证据登台（识别可信度与运营相关度）从严。conversation 分支的 fit 判据始终以 `--journal` 参数指定的期刊读者为准。偏置只影响升 severity 的判断方向，不改变裁决类型。

**反校准提醒（Pollock Ch12）**：单一来源的特质性意见（只有一位审稿人会提、编辑未点名）通常是 idiosyncratic 的；Panel 对只被一个分支以 weak 证据提出的条款保持怀疑——共同主题（多分支命中或证据扎实）才是 major 的常态来源。审稿人在方法上也会犯错（Ch12：作者侧的三分类 improves/neutral/hurts 提醒）——方法类条款要求 moderator 已过 realism 门才可入 major。
