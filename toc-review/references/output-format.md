# Output Format — 红队审查报告模板

报告语言：中文叙述 + 英文证据引文原文。落盘到 `--out` 或稿件同目录 `<稿件名>-toc-review-<YYYYMMDD>.md`。

分支名中英映射（报告正文用中文）：knot→张力与结　hook→读者转化　conversation→对话与贡献　characters→人物与故事线　staging→证据登台　payoff→承诺兑现。

---

```markdown
# ToC 红队审查报告 — {稿件名}

- 目标期刊：{journal}　审查日期：{date}
- 分支：knot / hook / conversation / characters / staging / payoff（{focus} 模式）＋ 动态分支 {n_dynamic} 条（{dynamic-1、dynamic-2 名称或“无”，派生理由见统计区末）
- 节点统计：辩论 {n_nodes} 个节点 → 存活 {n_surviving} / 被驳回 {n_deflected} / 撤回 {n_withdrawn}
- 模型阵容：lineup = {balanced|cheap|max|single|manual}；degraded = {false|partial|true（原因）}
  
  | 槽位 | 角色 | 模型（provider/id） | 家族 | 档位 |
  |---|---|---|---|---|
  | branch-{name} | 辩手 | {provider/id} | {家族} | {mid/cheap/high} |
  | ... | | | | |
  | referee | Panel 裁判 | {provider/id 或 orchestrator} | {家族} | {high} |
  
  运行时重派：{无 | 槽位→替代模型（原因）}
- Panel 处置：endorse {a} / reclassify {b} / downgrade {c} / merge {d} / reject {e}
- 证据核验：{n_verified}/{n_surviving} 引文字面命中稿件
- 定位：本报告提取**未声明**弱点（已声明局限 {n_acknowledged} 条已列为禁猎区，其中 {n_deflection} 条判定为 deflection-suspect）

## 〇、叙事骨架总评（Step 0 故事契约提取）

红队分支发现之前，先把稿件的叙事骨架摆出来——多数单条弱点同根于骨架层，这一区让报告读者先看整体再看条款：

- **knot 一句话陈述**：{编排在 Step 0 用一句话写出稿件试图解开的中心张力；写不出时明确说“无法在一句话内陈述”，这本身即 knot 分支的候选证据}
- **五幕映射**：

| 幕 | 稿件位置 | 完成度判断 |
|---|---------|----------|
| Exposition | {节次} | {铺陈背景/人物/knot 是否完成} |
| Rising action | {节次} | {理论与方法是否把结打紧} |
| Climax | {节次} | {Results 开头是否标志性转折} |
| Falling action | {节次} | {主结果/稳健性/意外发现是否解结} |
| Denouement | {节次} | {讨论是否回到开头承诺} |

- **人物 casting**：主角 {核心构念}；配角 {调节/中介}；群演 {控制/情境}；{主角是否可辨认、配角是否推动主线}
- **骨架层诊断一句**：{把骨架层最严重的断裂点用一句话点出，并与下方 Major 条款建立指回（“M1/M3 与此同根”）}

## 一、Major 弱点（按修复优先级排序）

### M{序号}　[{final_category}] {topic 一句话}

- **严重度**：major（Panel 裁决：{verdict}）　**分支**：{branch}　**证据核验**：{evidence_verified}　**证据强度**：{evidence_strength}　**realism**：{fixable/structural}　**修复类型**：{fix_type}
- **质疑**：{revised_description 中文转述}
- **证据引文**："{evidence_quote}"（{evidence_section}）
- **作者辩护方的回应**：{paper_response 摘要，含 acknowledges 状态}
- **为何仍然成立**：{moderator_reasoning + panel_reasoning 合并，一两句}
- **修复动作**：{具体可执行的动作：补什么检验/改什么措辞/加什么边界}
- **下游路由**：{skill 名称与调用方式}

（每条 major 重复此块。无 major 时写"本次未发现 major 级未声明弱点"并列出最接近的 minor。）

## 二、刊层风险总评（contribution_structural 条款）

Panel 判为 contribution_structural 的条款单列——它们不是补丁问题，而是贡献主张或期刊选择问题（Edmans 2023：即使每个问题 individually 可修，门禁层的裂缝会让论文在审稿循环中无法收敛）：

| # | 门禁风险 | 证据要点 | 含义：重构问题/换刊/补定位 | 路由 |
|---|---------|---------|---------------------------|------|

无此类条款时写"未发现结构性刊层风险"。总评一句话：这篇稿子在 {journal} 的最大门禁风险是什么（若 contribution 分支有存活 major，此处必写）。

## 三、Minor 弱点（简表）

| # | 类别 | 弱点 | 证据位置 | 修复动作 | 路由 |
|---|------|------|---------|---------|------|
| m1 | | 一句话 | section | 一句话 | skill |

## 四、被驳回与撤回记录（留痕，供人工复核）

| 节点 | 质疑摘要 | 驳回/撤回原因 |
|------|---------|--------------|

Panel reject 的条款在此注明 reject 理由（ungrounded / 已声明复述 / 其他）。

## 五、修复优先级 Top {3-5}

1. **{最高优先级动作}** → {skill}
2. ...

优先级依据：major 数量 × 对核心 claim 的威胁程度 × 修复成本。**只含 revision_fixable 条款**——contribution_structural 条款留在刊层风险区，不与补丁类动作混排。

## 六、边界声明

本报告是弱点候选清单而非结论（方法源在其基准上精度约 40%）：每条已附辩护方回应供快速人工裁决；未被发现的弱点中约四成需要后续文献知识（跨论文定位批评请用 research-gap-diagnosis）。纯交付层条款已标注 → pollock-qc，不计入实质优先级。
```

---

## 编译规则

- major 条款完整记录（辩护方回应必须保留——它是人工裁决"这条我认不认"的最快依据）
- 合并条款（merge）只出现一次，cross_category_concerns 注明另一分支
- contribution_structural 条款只进"刊层风险总评"，不进修复优先级；delivery_only 条款进 minor 表并标注 → pollock-qc
- evidence_verified=false 的条款不得以 major 进入报告（SKILL.md 约束）
- 空集分支（如 knot 支全部撤回）在统计区注明 branch_note，这是信息而非失败
- 报告结尾不加客套总结，最后一节就是边界声明
