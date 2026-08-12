---
type: routing
canonical_id: "theory-variant-routing"
source: "Gap × contribution lever × theory task"
created: 2026-06-01
updated: 2026-08-04
version: 2.2.0
---

# Theory Variant 路由表

本表把 Introduction 的 gap、贡献杠杆与实际理论任务映射到 Theory 构建变体。它是诊断辅助，不是机械生成器：**变量数量、模型复杂度与理论深度不是同一件事**。

## 输入与回退

优先读取 canonical `story`、Introduction contribution contract、`gap_type`、`makadok_dimension`（或等价 contribution lever）和明确承诺的理论任务。

- 缺 `gap_type`：回到 Phase 1 诊断。
- 缺贡献维度：诊断构念、机制、边界、层次、模式、问题、输出或现象中哪一项实际改变；**不得默认 Mechanism**。
- 缺失或冲突的信息：输出 `recommended_theory_variant: null` 或低置信建议，并列出待确认项；不发明中介或 moderator。

## 一级路由：Gap × 贡献杠杆

| Gap 类型 | 贡献杠杆 | 首选变体 | 代码 | 置信度 | 核心理论任务 |
|---------|---------|---------|------|--------|-------------|
| Incompleteness | Constructs | 构念辨析 | A | medium | 界定遗漏构念及其增量解释力 |
| Incompleteness | Mechanism | 机制推演 | B | high | 补足从前提到结果的过程解释 |
| Incompleteness | Boundary | 调节/条件化 | E | medium | 说明何时、对谁、为何不同 |
| Incompleteness | Level | 假设树/跨层 | C | medium | 连接遗漏层级，明确跨层作用 |
| Incompleteness | Mode | 过程理论 | D | low | 若遗漏的是阶段、顺序或演化方式 |
| Incompleteness | Question | 竞争假设 | F | low | 仅当遗漏问题产生真实对立预测 |
| Incompleteness | Output / Phenomenon | 机制推演 | B | medium | 解释新结果或新现象，必要时转 A/D |
| Inadequacy | Constructs | 构念辨析 | A | medium | 指出原构念化的失败点并修正 |
| Inadequacy | Mechanism | 机制推演 | B | high | 呈现既有机制为何不足及替代机制的可区分预测 |
| Inadequacy | Boundary | 调节/条件化 | E | high | 说明现有解释在哪一条件下失效或反转 |
| Inadequacy | Level | 假设树/跨层 | C | medium | 修正层次错置或跨层遗漏 |
| Inadequacy | Mode / Question | 竞争假设 | F | medium | 让旧逻辑与修正逻辑产生可裁决预测 |
| Inadequacy | Output / Phenomenon | 机制推演 | B | medium | 修正错误解释；若核心是过程顺序则转 D |
| Incommensurability | Constructs / Outputs | 构念辨析或假设树 | A / C | medium | 先定位是 X 分类（R1）还是 Y 分类（R2），再决定构念重定义或成组预测 |
| Incommensurability | Mechanism / Mode | 辩证对立或双轨机制 | G / B | high | 对称推导对立机制（R3）及其组合规则；实证裁决时可调用 F |
| Incommensurability | Boundary | 调节/条件化 | E | high | 用理论化情境（R4）解释两套预测何时各自成立，并双边推导 |
| Incommensurability | Question | 竞争假设 | F | high | 将两个强版本逻辑转为可直接裁决的预测 |
| Incommensurability | Level | 假设树/跨层 | C | high | 明确理论在不同层级的预测与连接规则 |
| Incommensurability | Output / Phenomenon | 竞争假设 | F | medium | 比较解释；若可综合则以 B/E 为主、F 为子协议 |

一级路由只给候选主架构。实际稿件可在一个主架构下调用多个子协议，但不得把多个变体简单堆叠为复杂模型；变量数量、假设编号和可估计模型不是路由依据。

### Incommensurability 专属优先路由

主 Gap 为 Incommensurability 时，先读 `../../references/incommensurability-resolution-routes.md`，提取 L0 stable reasoning kernel 后再判定 R1–R4；本表的 Gap × 贡献杠杆只作 architecture compatibility check。冲突位于 X→R1，位于 Y→R2，位于固定关系中的对立机制→R3，位于情境 W→R4。真实性门控首先只要求各研究共享理论对象或可辩护的高阶结果族，并清楚映射其下位成员；只有进入 R3/R4 的正式假设推理，才固定具体 X、Y、分析层级、时间范围与估计对象。一个项目保留一个主路由，至多一个次路由；允许低置信与 `unclassified_residual`。R1–R4 只规定必须完成的推理任务，不规定 A–G、H 数量或模型形式。

## 二级路由：理论任务 → 子协议

### B2 双轨机制

在判断 B2 前，先区分：B0 是理论过程解释（可只检验 X→Y），B1 是正式中介（M 为构念且设计检验间接效应）。出现多个过程动作不自动触发 B1。

仅当以下两项同时成立时触发：

- 存在两条概念上不同的过程路径，而非同一路径的同义改写；
- 两条路径产生不同的可检验预测、时间轨迹、结果维度或条件反应。

`promised_mechanism_steps: 2` **不触发** B2；这是推理深度提示，不是“两条机制”的证据。调节变量也不是 B2 的必要条件。

### E 条件化与调节

触发前先执行 conditionality gate：

1. 核心机制是否可在声明 scope 内稳定运作？
2. 候选条件是否改变暴露、注意、能力、动机、解释或约束中的至少一项？
3. 该变化是否导出方向、强度、形状或有效性上的明确差异？

若第 2–3 项没有机制依据，不选 E；若有依据且无稳定无条件预测，条件关系应成为主预测，而非“主效应之后再加一个 moderator”。

| 信号 | 子协议 | 必须确认 |
|------|--------|----------|
| `interaction_type: within` | 同层调节 | 条件与 focal relation 在同一层级 |
| `interaction_type: cross` | 跨层调节 | focal unit、nesting 与跨层传递机制 |
| categorical moderator | 分组调节 | 类别改变机制而非仅切样本 |
| 两套理论在不同条件下成立 | 竞争基线裁决 | 条件能够区分理论预测 |
| IV 是特质/倾向，moderator 是特质相关 cue（low 态=主效应默认基线，cue 激活对立表现型） | **E11 Trait-Activation Dual-Manifestation Cue-Switch**（EMERGING，单源；仅作 `section_variant`） | 两表现型同属一个行为连续谱两端；cue 是"默认失效"证据而非一般情境；假设用 Mitigation via Manifestation-Switch 句式（`sentences/moderation.md`） |

### C 假设树

只有多个预测共享同一理论 trunk 且分支之间存在递进或条件关系时选择 C。四个彼此独立的假设不是“树”。

## 三级路由：Claim burden → reasoning burden

理论负担由主张性质决定，不由 mediator/moderator 数量决定。

| Gap | 最低论证负担 | 不要求的东西 |
|-----|-------------|--------------|
| Incompleteness | 完整说明缺失前提/过程如何改变预测，并指出补充后的理论后果 | 不强制中介 |
| Inadequacy | 公平呈现既有机制或假设，定位失败环节，提出修正/替代逻辑，并给出至少一个可区分预测 | 不强制“主效应+调节” |
| Incommensurability | 以强版本呈现双方逻辑，说明不可同时成立之处，并给出裁决或条件化方案 | 不强制 3–4 步或复杂模型 |

### 机制深度定义

机制深度按**有内容的推理移动**计算，例如：

`制度信号改变行动者注意 → 注意改变信息解释 → 解释改变选择`。

这可以对应无中介的 X→Y 模型，也可以对应中介模型。反之，X→M→Y 若只是重述变量关系而没有行动者过程，并不构成深机制。

## 冲突处理

1. 以确认后的 contribution contract 和论文实际理论任务为最高优先级。
2. Introduction hint 是建议，不得覆盖 Theory 中更具体的诊断；不一致时回写/提示契约修订。
3. 多个信号并存时，选择一个主架构，再列必要子协议及各自承担的任务；不得按“最先出现的信号”裁决。
4. Incommensurability 不自动选择 F：R1/R2 可用 A/C，R3 可用 G/B，R4 可用 E；只有研究任务是直接裁决竞争理论时才以 F 为主。
5. 置信度 low 或关键信息缺失时，输出诊断问题，不使用默认 Mechanism/E1 填空。
6. 选择复杂 L2 架构前执行 necessity check：若一个更简单的 differential/conditional proposition 能表达同一贡献，不复制来源论文的多分支、中介、调节或曲线模型。

## 解析示例

```yaml
theory_hints:
  gap_type: Inadequacy
  makadok_dimension: Mechanism
  promised_mechanism_steps: 2
  promised_mediation: false
  promised_boundary_conditions: true
```

解析：

1. Inadequacy × Mechanism → 主架构 B。
2. `steps: 2` 只表示至少两个推理移动，不触发 B2。
3. 对 boundary promise 执行 conditionality gate；若条件改变已识别机制，调用 E 子协议。
4. 若无稳定无条件效应，输出“B 主架构 + 条件关系为主预测”，而非强制 H1 主效应。

## 与 Phase 1 的接口

```python
def diagnose_theory_variant(theory_hints, contribution_contract):
    if not theory_hints.get("gap_type"):
        return interactive_diagnosis()
    lever = theory_hints.get("makadok_dimension") or diagnose_contribution_lever(contribution_contract)
    if not lever:
        return {"recommended_theory_variant": None, "confidence": None}
    primary = route(theory_hints["gap_type"], lever)
    return apply_task_checks(primary, theory_hints, contribution_contract)
```

## 更新日志

- **v2.2.0** (2026-08-04): 为 Incommensurability 增加 L0–L3 抽象层级与 architecture necessity check；R1–R4 只规定推理任务，不再隐含 H 数量、A–G 变体或模型形式。
- **v2.1.0** (2026-08-04): 新增 Incommensurability R1–R4 专属路由；取消由 Makadok 维度机械选择解决方案；加入对立机制≠自动 U/倒U、同号调节≠自动 Incommensurability 的边界。
- **v2.0.0** (2026-08-03): 将“Gap 能量级→变量/路径数量”改为“claim burden→reasoning burden”；增加 conditionality gate；修正 B2 冲突规则；取消缺失贡献维度时默认 Mechanism；冲突按理论任务而非首个文本信号裁决。
- **v1.0.0** (2026-06-01): 初始 Gap × Makadok 路由。
