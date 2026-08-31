# Panel Review — 跨分支调解

改编自 ToC 论文 §3.5 与附录 C.5，加入 Edmans (2023) 的"可修复 vs 结构性"分诊与 Pollock Ch13 表13.1 的拒稿/修改标准。由编排者（主 agent）对全部存活条款逐条执行，一次调解同时持有六个视角，做分支内主持人做不到的跨类别推理。

## 输入

- 全部存活条款（含 branch、moderator 裁决、evidence_verified 状态）
- 稿件路径（Panel 需要时可回查原文）
- 已声明局限清单

## Panel Prompt（逐条执行）

```
You are a review PANEL representing all six skeptic perspectives on a
management manuscript under review at {journal}:
Identification & Inference, Construct & Measurement, Theory & Contribution,
Scope & External Validity, Alternative Explanation, and Contribution &
Journal-Fit (the desk-review gate).

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
 "final_category": "identification|construct|theory|scope|alternative|contribution",
 "final_severity": "minor|major",
 "fix_type": "revision_fixable|contribution_structural|delivery_only",
 "cross_category_concerns": ["..."],
 "reasoning": "..."}
```

## 裁决后处理

- `endorse` / `reclassify` / `downgrade`：进入最终报告，按 final_category 归类、final_severity 排序
- `merge`：保留更扎实的一条，另一条并入其 cross_category_concerns，报告合并计数
- `reject`：不进主表，留痕于统计区（含 reject 理由，供人工复核）
- `fix_type` 分诊（Edmans 2023 + Pollock Ch13 表13.1 的管理学化）：
  - `revision_fixable` → 进入修复优先级，路由到对应 *-review / write-* skill。表13.1 修改列的特征：可澄清、可补检验、可通过重构回应
  - `contribution_structural` → 单列"刊层风险"（见 output-format），路由 `research-gap-diagnosis`（重定位）或 `grill-the-claim`（重构贡献主张）。表13.1 拒稿列的特征：贡献潜力不可见、对话不可识别、构念效度不足且**很难补救**、逻辑不连贯无法聚合为可检验主张——此类条款**不进**修复优先级，打补丁解决不了门禁问题
  - `delivery_only` → 进 minor 表标注"→ pollock-qc"

## 严重度最终语义（Panel 校准基准）

- **major**：审稿人可以据此写出 reject 或 major-R&R 的核心理由——威胁核心 claim 的有效性、可信度，**或触发贡献门禁**（novelty=先验更新失败、importance 不足、期刊契合错位、net-value 问题只测一半）
- **minor**：真实但局部可修——补一个检验、改一处措辞、加一段边界条件讨论

**显式排序规则（top-K 选取）**：major 内部按 类别冲击先验 × evidence_strength × realism 排序——
1. 类别冲击先验（Pollock Ch13 表13.1 的拒稿列标准映射到分支）：理论贡献清晰性与对话可识别（theory / contribution 分支，表13.1 前两行）> 测量构念效度且难补救（construct 分支，表13.1"测量"行拒稿列）> 设计系统性偏差（identification）> 假设发展缺陷（theory）> 结果呈现与抽样（scope / construct）> 写作病（delivery_only）
2. 同类别内 substantial 证据 > moderate > weak（weak-evidence majors 默认 reject，见 debate-protocol 双轴规则）
3. structural（不可修订修复）在同严重度内优先列示——它改变作者的投稿决策，不只改变修订清单

期刊偏置：`--journal=OS|SMJ` 时理论增量与机制证据类条款从严；`MSOM` 时识别与运营情境类从严；`AMJ` 时构念清晰与情境嵌入类从严。contribution 分支的 fit 判据始终以 `--journal` 参数指定的期刊读者为准。偏置只影响升 severity 的判断方向，不改变裁决类型。

**反校准提醒（Pollock Ch12）**：单一来源的特质性意见（只有一位审稿人会提、编辑未点名）通常是 idiosyncratic 的；Panel 对只被一个分支以 weak 证据提出的条款保持怀疑——共同主题（多分支命中或证据扎实）才是 major 的常态来源。审稿人在方法上也会犯错（Ch12：作者侧的三分类 improves/neutral/hurts 提醒）——方法类条款要求 moderator 已过 realism 门才可入 major。
