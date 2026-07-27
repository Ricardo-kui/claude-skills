# Revision Roadmap 与回复信骨架模板

本文件支撑 revision-coach 模式 A 的 Step 7 输出。

## 一、Revision Roadmap(主输出)

```markdown
## Revision Roadmap

### 概述
- 决定类型:[Major Revision / Minor Revision / Revise & Resubmit]
- 意见总数:[N]
- 按类型:[N] Major / [N] Minor / [N] Editorial / [N] Positive
- 预计工作量:[Light / Moderate / Substantial / Fundamental]

### P1: Must Fix(最先改)
| # | 意见转述 | 审稿人 | 类型 | 节 | 建议动作 | 兑现证据位置 |
|---|---|---|---|---|---|---|
| 1 | [一句话] | R1 | Major | Methods | [做什么] | [new_table / methods_paragraph…] |

### P2: Should Fix(P1 之后)
| # | 意见转述 | 审稿人 | 类型 | 节 | 建议动作 | 兑现证据位置 |

### P3: Consider(有余力再做)
| # | 意见转述 | 审稿人 | 类型 | 节 | 建议动作 |

### Positive(回复信致谢)
| # | 意见 | 审稿人 |

### 跨审稿人共性问题(高优先)
[多名审稿人同时提出的点,提示这是必须正面回应的]

### 建议修改顺序
1. [先改某节,因为……]
2. [再改某节,因为……]
3. [最后统一处理 editorial]
```

"兑现证据位置"列来自 `comment-parsing.md` Step 3.5 的承诺拆解——让作者一眼看到"每条要求最终落在稿件的哪个具体物上",也为模式 B 体检埋好核对点。

## 二、Response-to-Reviewers 骨架(回复信)

```markdown
Dear Editor and Reviewers,

Thank you for the constructive feedback on our manuscript "[Title]" (Manuscript ID: [XXX]).
We have revised the manuscript following your comments. Below we respond to each point.
All changes are marked in [tracked changes / colored text] in the revised manuscript; page/line references refer to the revised version.

## Response to the Editor

### Editor Point E-1: [parsed summary]
**Editor's comment:** "[verbatim]"
**Response:** [PLACEHOLDER — 作者填写]
**Changes made:** [PLACEHOLDER — 指向具体页/行/表]

## Response to Reviewer 1

### Comment R1-1: [parsed summary]
**Reviewer's comment:** "[verbatim]"
**Response:** [PLACEHOLDER]
**Changes made:** [PLACEHOLDER — page/line/table]

### Comment R1-2: ……

## Response to Reviewer 2
……

## (可选)审稿人之间存在分歧的点
[列出 R1 与 R2 相左之处,及作者的取舍理由]
```

**骨架填写纪律**:
- 每条审稿意见对应**一个独立回复块**,先引原文、再回应、再指改动位置——三段缺一不可。
- "Changes made" 必须指向稿件真实位置(页/行/表/图);若该条是"仅致谢/无需改稿"(acknowledgment_only),明确写"No manuscript change required; addressed in this response"。
- 实证类要求(重跑、换识别、加稳健性):在回复里写"Conducted as requested; see new Table X / Appendix Y",且**该表格必须真实存在**——若尚未跑,标 `[PENDING — 需 causal-analysis/stata 执行]`,不要编结果。
- push back(礼貌不同意)时:先复述并肯定审稿人关切 → 给出理由(理论/数据/文献)→ 说明你做了什么折中(如加入稳健性或脚注讨论)。不要直接否定。

## 三、可选:修改追踪表

若作者要跟踪进度,可生成预填好的追踪表(每条已解析意见一行):

| concern_id | 审稿人 | 意见转述 | 优先级 | 责任节 | 兑现证据 | 状态 | 备注 |
|---|---|---|---|---|---|---|---|
| R1-1 | R1 | … | P1 | Methods | new_table | ☐ todo | |

状态值:`todo` / `in_progress` / `done` / `pushback` / `acked_only`。

## 四、工作量估计

| 等级 | 标准 | 典型周期 |
|---|---|---|
| Light | 0–2 Major,<5 Minor,多为 editorial | 1–3 天 |
| Moderate | 3–5 Major,5–10 Minor | 1–2 周 |
| Substantial | >5 Major,或需补数据/分析 | 2–4 周 |
| Fundamental | 需重构或新增研究 | 4 周以上(考虑重投) |

实证类 Major(要重跑回归/换识别)按 Substantial 起估,并提示作者尽早把这部分排进 `causal-analysis` / `stata` 线。
