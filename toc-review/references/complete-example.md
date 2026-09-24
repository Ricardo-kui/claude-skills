# Complete Example — 端到端输入输出示例

虚构稿件（教学用途，非真实论文），展示分支辩论全程、Panel 裁决与报告片段。每轮真实运行参照此例的字段完整度与转述密度。示例主支选 knot（新分类学的旗舰支），并在 Panel 段展示 staging 支挂载的推断弹药轨迹。

---

## 输入

```
/toc-review "D:\Projects\recall-focus\manuscript.md" --journal=AMJ
```

虚构稿件概要：CEO regulatory focus 与召回时点（time-to-recall），1995–2018 美国制造业召回面板，Cox 模型 + 交叠 DiD 补充。

## Step 0 产物（节选）

章节表：Introduction / Theory & Hypotheses / Methods / Results / Discussion / Limitations。

已声明局限清单（禁猎区）：

| # | 已声明内容 | 位置 | 标注 |
|---|---|---|---|
| 1 | 单一国家样本限制外推 | Limitations ¶1 | — |
| 2 | regulatory focus 测量依赖文本编码 | Limitations ¶2 | — |
| 3 | 机制检验不足 | Limitations ¶3 | [deflection-suspect]：原文"future research should unpack the psychological mechanism"——外包给未来研究，conversation 支可打 |

事实卡：RQ = CEO regulatory focus 如何影响召回时点；IV = promotion/prevention focus（股东信文本编码）；DV = awareness-to-recall 天数；数据 = NHTSA 1995–2018；识别 = Cox 基线 + staggered DiD 稳健性；期刊 = AMJ。

故事契约（三件套，只描述不断案）：

- **knot 陈述**："预防型关注的 CEO 应更早发现问题并召回——但同一警觉也可能让他们更早暴露于监管 scrutiny，加速与迟疑在同一心理特质内对撞。"（能写出，但引言未将其作为张力陈述，见 knot 支）
- **五幕映射**：Exposition = Intro ¶1–4（行业背景铺陈，knot 未现）；Rising = Intro ¶5–Theory 末（H1–H3 逐步打结）；Climax = Results 表 3 段；Falling = 稳健性＋DiD 补充；Denouement = Discussion 前两段（回到警觉悖论）＋Limitations。
- **人物 casting**：主角 = regulatory focus（IV 构念）× recall timing（DV 构念）；配角 = regulatory scrutiny（调节）、crisis severity（中介）；群演 = firm size、industry、CEO tenure。

动态分支派生（1 条）：`dynamic-1`（exposition 悬置——五幕断裂派生：knot 到 Rising 中段才出现，Exposition 四段无张力事件，Ch02 标准）。派生理由记入报告统计区。

## Step 1 分支返回（knot 支，节选）

```json
{
  "branch": "knot",
  "nodes": [
    {
      "node_id": "root",
      "topic": "knot-suspended-until-rising-action",
      "claim": {
        "topic": "prescribed-answer-opening",
        "description": "The Introduction resolves its own tension in paragraph 5: it states that prevention-focused CEOs recall earlier 'because they attend to threats sooner', leaving the scrutiny-countervailing force unstated until the hypotheses. The knot never operates as a knot; the paper reads as filling a gap rather than resolving a conflict.",
        "evidence_quote": "We argue that prevention-focused chief executives identify product defects earlier and therefore initiate recalls sooner.",
        "evidence_section": "Introduction, ¶5",
        "severity_guess": "major"
      },
      "advocate": {
        "acknowledges": false,
        "response": "Paragraph 6 does acknowledge that 'recalls expose firms to regulatory and reputational consequences', which readers can assemble into the countervailing force; the tension is present, just economically stated.",
        "citation_quote": "Recalls, however, are not costless: they invite regulatory scrutiny and signal quality problems to consumers."
      },
      "revision": {
        "revised_description": "The raw material of the knot exists (¶6 cost sentence), but it is deployed as a caveat, not as an opposing force: no paragraph stages the two forces against each other, and the RQ paragraph follows the resolution rather than the conflict.",
        "concedes": false
      },
      "moderator": {
        "verdict": "valid",
        "severity": "major",
        "evidence_strength": "substantial",
        "realism": "fixable",
        "should_expand": true,
        "expansion_prompts": [
          "Does the abstract's one-line summary preserve any tension, or does it also resolve it?"
        ],
        "reasoning": "The rebuttal downgraded the claim from 'no tension material' to 'tension material present but never staged as conflict'. That is exactly the Pollock knot failure mode; severity holds at major, evidence upgraded to substantial because both quotes are on the page. Expand once: check whether the abstract repeats the prescribed answer."
      },
      "expanded_from": null
    },
    {
      "node_id": "root-a",
      "topic": "abstract-prescribed-answer",
      "claim": {
        "topic": "abstract-prescribed-answer",
        "description": "The abstract states the finding direction and the mechanism in a single sentence with no competing force, so the first-time reader's question is never opened.",
        "evidence_quote": "Prevention-focused CEOs initiate recalls sooner because they attend to threats earlier.",
        "evidence_section": "Abstract",
        "severity_guess": "minor"
      },
      "advocate": {
        "acknowledges": true,
        "response": "Abstracts conventionally state findings; suspense in an abstract is not the standard.",
        "citation_quote": null
      },
      "revision": {
        "revised_description": "Concede the convention point; the residual issue is that the abstract's framing sentence forecloses the paradox the Discussion returns to ('an ambivalent guardianship'), creating a framing mismatch rather than a missing tension.",
        "concedes": true
      },
      "moderator": {
        "verdict": "valid",
        "severity": "minor",
        "evidence_strength": "moderate",
        "realism": "fixable",
        "should_expand": false,
        "reasoning": "Advocate's convention rebuttal lands; what survives is a framing mismatch between abstract and Discussion, worth a minor with a one-line fix."
      },
      "expanded_from": "root"
    }
  ],
  "surviving": ["root", "root-a"],
  "branch_note": "Schulz guardrail applied: no node flags the Introduction for 'spoiling results' — the branch attacks the missing conflict, not the presence of previews."
}
```

注意此例展示的三种裁决轨迹：root 存活且证据升级（辩护把"没有张力素材"收窄为"素材未结成张力"，反而坐实 knot 失败模式）、child 从 expansion_prompt 生长且在辩护后降级（major→minor）、branch_note 记录校准护栏的运用。

## Step 2 核验输出（summary 行）

```
verified 9/11 quotes, 0 empty quotes skipped
```

两条未命中的处理：一条改引文后重跑命中；一条（characters 支）无独立原文支撑，Panel reject（reason: ungrounded）。

## Step 3 Panel 裁决（节选）

```json
{"verdict": "endorse",
 "source_branch": "knot",
 "final_category": "knot",
 "final_severity": "major",
 "fix_type": "contribution_structural",
 "cross_category_concerns": [],
 "reasoning": "Story-architecture-level failure under Table 13.1: no staged conflict means no study the reader is waiting for. The fix is architectural (re-open the knot in Exposition and let the RQ follow the conflict), not a patch; route to paper-story-contract, not to line editing."}
```

staging 支的推断弹药轨迹（挂载模式）：staging 支质疑 DiD 稳健性用未修正 TWFE，辩护方指出主推断在 Cox、DiD 只是辅助；moderator 降级为 minor、Panel downgrade 保留（fix_type: revision_fixable，路由 staggered-did 重估）——推断信号经 staging 支进入，严重度按其在故事中的实际工作量校准。

merge 示例：conversation 支与 payoff 支都打了"单行业设定 + 无行业限定的普遍表述"，Panel 将 conversation 版并入 payoff 版（后者引用了 abstract 原文），cross_category_concerns 标注两支。

## Step 4 报告片段（节选）

报告头部统计区（含阵容透明度块，lineup-protocol §6 模板）：

```markdown
# ToC 红队审查报告 — CEO Regulatory Focus 与召回时点（虚构稿）

- 目标期刊：AMJ　审查日期：2026-09-22
- 分支：knot / hook / conversation / characters / staging / payoff（all 模式）＋ 动态分支 1 条（dynamic-1：exposition 悬置——五幕断裂派生）
- 节点统计：辩论 9 个节点 → 存活 5 / 被驳回 3 / 撤回 1
- 模型阵容：lineup = balanced；degraded = partial（5 个非裁判家族 < 6 个辩手槽位，payoff 复用 GLM 异档）

  | 槽位 | 角色 | 模型（provider/id） | 家族 | 档位 |
  |---|---|---|---|---|
  | knot | 辩手 | deepseek/deepseek-v4-pro | DeepSeek | mid |
  | hook | 辩手 | zai-coding-cn/glm-5.3 | GLM | mid |
  | conversation | 辩手 | openai-codex/gpt-5.6-terra | GPT | mid |
  | characters | 辩手 | github-copilot/grok-4.6 | Grok | mid |
  | staging | 辩手 | kimi-coding/k3 | Kimi | mid |
  | payoff | 辩手 | zai-coding-cn/glm-5.3-highspeed | GLM | mid（家族复用，异档不可用时同档异模） |
  | dynamic-1 | 辩手 | deepseek/deepseek-flash | DeepSeek | cheap（家族复用取异档） |
  | referee | Panel 裁判 | github-copilot/claude-opus-5 | Claude | high |

  运行时重派：hook 槽首进模型派发验证失败，按 fallback 链重派 zai-coding-cn/glm-5.3-flash 成功（留痕）
- Panel 处置：endorse 3 / reclassify 0 / downgrade 1 / merge 1 / reject 1
- 证据核验：5/5 引文字面命中稿件
- 定位：本报告提取未声明弱点（已声明局限 3 条已列为禁猎区，其中 1 条判定为 deflection-suspect）
```

叙事骨架总评区（〇区，报告正文第一区）：

```markdown
## 〇、叙事骨架总评

**中心 knot（一句话）**：预防型关注的 CEO 更早发现问题并召回——但同一警觉也让他们更早暴露于监管 scrutiny；加速与迟疑在同一特质内对撞。
**可一句话陈述**：是（但稿内未以此张力开场，见 M1）。

| 幕 | 对应节次 | 完成度 |
|---|---|---|
| Exposition | Intro ¶1–4 | △ 行业背景充分但 knot 未现 |
| Rising action | Intro ¶5–Theory 末 | ✓ H1–H3 逐步打结 |
| Climax | Results 表 3 段 | ✓ |
| Falling action | 稳健性＋DiD 补充 | ✓ 解结节奏偏平（全部同向） |
| Denouement | Discussion 前两段＋Limitations | ✓ 回到警觉悖论，但该悖论在 Exposition 未埋 |

**人物 casting**：主角 = regulatory focus × recall timing；配角 = regulatory scrutiny（调节）、crisis severity（中介）；群演 = firm size、industry、CEO tenure。casting 无异常，主角未超三个。

**骨架层诊断**：故事骨架五幕齐备、人物清爽，唯一断点是 knot 的时序错位——张力素材在 ¶6 以让步状语存在，却在 Denouement 才被承认为悖论（"an ambivalent guardianship"）。这解释了 M1（knot 支 major）与 M3（payoff 支 framing mismatch）的同根因。
```

后续报告体示例：

```markdown
### M1　[张力与结] 引言在 ¶5 自答其题：knot 以让步状语存在、从未以对抗力登台

- **严重度**：major（Panel 裁决：endorse）　**分支**：knot　**证据核验**：true　**修复类型**：contribution_structural（故事架构级）
- **质疑**：¶5 直接宣告结论方向（"identify product defects earlier and therefore initiate recalls sooner"），对冲力（监管 scrutiny）只在 ¶6 作为成本让步出现且再未回环；RQ 段落跟在解决方案之后，读者从无需要研究回答的问题
- **证据引文**："We argue that prevention-focused chief executives identify product defects earlier and therefore initiate recalls sooner."（Introduction, ¶5）
- **作者辩护方的回应**：¶6 "Recalls, however, are not costless: they invite regulatory scrutiny and signal quality problems to consumers."（acknowledges: false）
- **为何仍然成立**：张力素材在场≠张力被结成；全文无一段把两股力摆到对方面前，Denouement 的"ambivalent guardianship"证明作者自己知道悖论存在——它只是来晚了
- **修复动作**：把 ¶6 的对冲力升格为 ¶1–2 的开场张力；RQ 移到张力陈述之后；abstract 措辞留悬念钩（路由 paper-story-contract 重建故事契约，write-introduction 落地）
- **下游路由**：paper-story-contract / write-introduction

## 二、刊层风险总评（contribution_structural 条款）

| # | 门禁风险 | 证据要点 | 含义 | 路由 |
|---|---------|---------|------|------|
| 1 | knot 时序错位：张力在结尾才被承认 | ¶5 预设答案 + ¶6 让步状语 + Discussion "ambivalent guardianship" | 故事架构级重排（AMJ：读者问题从未被打开） | paper-story-contract |
| 2 | 泛化措辞 vs 单行业样本 | Abstract 无限定表述 + Methods 制造业样本 | 收窄措辞或补定位论证 | research-gap-diagnosis |

总评：本稿在 AMJ 的最大门禁风险是故事架构层——证据登台与人物 casting 均达标，但中心张力从未真正开打，读者的第一个问题在第五段就被回答了。
```

---

## 给运行者的对照点

- 辩论记录四阶段字段齐全，advocate 的回应保留原文引用
- 存活条款的质疑转述是中文、引文是英文原文
- deflection-suspect 的局限（机制外包）被 conversation 支合法命中，已声明的 1、2 条无人复述
- knot 支的 Schulz 护栏可见：攻击的是"冲突未结成"，不是"结果预告剧透"（branch_note 留痕）
- moderator 降级（child major→minor）与 Panel 再校准（staging 支 downgrade）的双层路径可见
- 推断类弹药（未修正 TWFE）从 staging 支进入，按其在故事中的实际工作量（Discussion 引用其做佐证）定级，未升级为全稿门禁
- merge 条款只出现一次，另一支在 cross_category_concerns 留名
- contribution_structural 条款进刊层风险区，修复优先级里只有 revision_fixable
- 〇区叙事骨架总评与 M1/M3 互相指回，故事契约三件套（knot 陈述/五幕映射/人物 casting）齐备
