# Complete Example — 端到端对辩示例

虚构稿件与虚构对手（教学用途，非真实论文），展示 Step 0 产物、一个节点的辩论全程、叶子判定与报告核心段。每轮真实对辩参照此例的字段完整度与判定密度。

---

## 输入

```
/tod-debate "D:\Projects\recall-focus\manuscript.md" --journal=JOM
```

论文A（虚构）：CEO regulatory focus 与召回时点，awareness-to-recall 天数，Cox 模型 + 非竞争执行度变化的 staggered DiD 稳健性。

## Step 0 产物（节选）

- 对手提名：R1 `[@darby2025]`（activist investors 与召回时点，同 DV 家族、不同 IV 与理论）——用户确认；R2 提名被否（同方法但时距定义不同构，留作旗标）
- 维度派生来源：`产品召回\03 前因与驱动`（clock-start、发起方两维度）、`产品召回\05 概念`（regulatory focus）、`论证卡库\03 Method Cards`（识别维度）
- 简报卡：`论证卡 - 时间动态影响流动决策与效能`（定向 persona 的构念系统）
- 等价旗标：literature 笔记中 R1 被标"与稿件共用 NHTSA 数据与 awareness 起点"——开辩即重点核

## Root 自辩（persona A 主张节选，英文原文）

```json
{"claim_id": "A1", "title": "CEO regulatory focus as an antecedent of recall timing",
 "description": "First to theorize and test executive-level regulatory focus as a determinant of how quickly firms recall, beyond firm-level incentives.",
 "taxonomy": "construct-operationalization",
 "evidence_quotes": [{"quote": "We introduce CEO regulatory focus as an executive-level antecedent of recall speed, distinct from governance and litigation incentives.", "section": "Introduction"}]}
```

persona B（R1）对应主张 B1：股东行动主义压力缩短召回时距（`identification-variation`）。

## 节点辩论（子题"who moves the clock: executive psychology vs. external pressure"，节选）

**Present（A）**：行动者层级不同——activist pressure 是外部治理通道，A1 是执行者认知通道，两者对同一 DV 的解释可以分离……（引文：Theory 节机制段）

**Respond（B）**：A 的机制证据只有交互项（prevention focus × 高可见度召回），没有区分"认知通道"与"压力感知通道"的中介证据；clarifying question: 稿件能否排除 activist 在场本身改变 CEO focus 测量的解读？

**Revise（A）**：接受证据缺口，收窄主张——A1 的成立范围是"外部压力通道之外的残余变异"，margin 是行动者层级与构念（regulatory focus）本身。

## 叶子判定（moderator，含门禁留痕）

```json
{"claims": ["A1", "B1"], "verdict": "unique",
 "margin": null,
 "evidence_A": ["We introduce CEO regulatory focus as an executive-level antecedent..."],
 "evidence_B": ["Activist investors shorten the time between defect awareness and recall."],
 "positioning_implication": "定位句可写执行者认知通道与外部治理通道互补；但 intro 不得声称机制已分离。"},
{"claims": ["A3", "B2"], "verdict": "incremental",
 "margin": "R1 已建 awareness-to-recall 的行动主义解释；稿件新增同一 DV 上的执行者层级调节，margin 为 cross-level moderation，非新基线。",
 "gate_fired": "equivalence",
 "...": "（同冲击窗口 + 同 DV 家族 + 同数据源触发等价门禁，路径终止于此判定）"}
```

## 报告核心段（节选）

```markdown
## 一、贡献定位表

| # | 子贡献 | 判定 | A 证据 | B 证据 | 含义 |
|---|--------|------|--------|--------|------|
| 2 | awareness-to-recall 的解释 | incremental | 交互项引文 | R1 主效应引文 | 定位句写 cross-level 调节，不写新基线；防守：收窄措辞即可 |
| 1 | CEO regulatory focus 构念 | unique | Intro 引文 | — | 互补通道表述可用；机制分离的主张删除 |

## 三、等价风险区

- 开辩前旗标：与 R1 共用 NHTSA 数据与 awareness 起点（literature 笔记）
- 实锤：无 equivalent 判定；incremental 行 #2 是最近接点（margin 已写明）
- pairwise 提醒：第三者查重 → research-gap-diagnosis
```

---

## 给运行者的对照点

- 每条主张带分类学标签与逐字引文；判定对象是主张对，论文级结论由定位表汇总
- incremental 行的 margin 一句话写明增量与证据；equivalent 门禁触发时路径终止于显式判定
- 定位表行序：最危险的（incremental/equivalent）在上，unique 在下
- 判定与引文是英文原文，转述与含义是中文——报告双语分工的样板
