# 候选主线枚举（Preparing 阶段，动笔前）

> 用途：在锁定 `central_knot` 之前，先发散出 2–4 条候选故事主线，再按证据强度收敛。产出的"候选"是**项目自身的**故事变体，不是范文故事类型；本步骤不选择 story frame、不加载 exemplar、不推荐 blueprint。
> 来源：抽取改写自 good-story (Rimagination) `SKILL.md` 的 Quick Workflow Step 2–3；与管理实证情境对齐，并遵守本 skill 的反范文纪律。
> 适用：Preparing 阶段已允许的"competing formulations"（见 `stage-gates.md`）。knot 已明确、无争议时可跳过。

## 何时用

- 结果多但主线散：同一批证据能讲出几种故事，读者会带走不同的新认识。
- 用户能说出"我在做什么"但说不出"这篇文章让读者改变什么"。
- audit 模式下，现有 `central_knot` 的证据张力不足，或与多个候选结果的证据权重冲突。

## 三个叙事角色（全部来自项目材料）

| 角色 | 定义 | 从哪取 | 不可用来源 |
|---|---|---|---|
| 主角 protagonist | 被解释的现象、机制、构念或方法 | 研究问题、Theory 的 focal construct | 范文的主角类型 |
| 障碍 antagonist | 瓶颈、矛盾、教条、缺失机制、噪声证据、尺度壁垒 | 文献冲突、Knot 真实性检查、机制不完备处 | "little is known" 类空洞缺口 |
| 转折 turn | 哪条证据改变读者原本能相信的判断 | 实际结果中的 surprise / 澄清性发现 | 预设结局 |

## 程序

1. **证据盘点**（Preparing 已允许）：列出最强主张、数据集、方法、对照、负结果、限制、目标读者。区分直接证据 / 解释 / 推测 / 背景。
2. **每个分析映射当前叙事职责**：它推动哪个判断，还是只是"我们接着做了 X"。
3. **起草 2–4 条候选主线**：每条一句话线——障碍是什么 → 转折证据是什么 → 读者被改变什么。逐条写出，先不评判。
4. **排序**，按三条标准独立评估：
   - **证据链强度**：每条转折都有直接证据支撑，证据阶梯成立（每个结果让下一主张更可信）；
   - **诚实后果**：结论范围 = 证据范围，不过度外推；
   - **可复述性**：一句话能带走，不需要多句解释。
5. **降级候选**（以下任一即降级，不必等到写完）：编年史逻辑（按做实验顺序而非读者推理）、隐藏假设、过多并列贡献（多个"同等重要"）、目标读者是证据满足不了的读者。
6. **收敛**：选中最强但不过界的一条，把它的转折喂给 `central_knot`、推进路径喂给 `storylines`、读者前后变化喂给 `reader_shift`。写入 schema 时全部标 `status: provisional`，直到 integrity gate 确认（`story-integrity-gate.md`）。

## 输出（Story Intake 增加一节）

```markdown
## 候选主线
| # | 障碍 | 转折证据 | 读者改变 | 排序理由 |
|---|---|---|---|---|
| C1 | ... | ... | ... | ... |
```
并列淘汰理由与最终选定线。若全部候选都违反证据边界，回到 Story Intake 报告（BLOCKED），不强行选定。

## 边界

- 候选必须来自项目自己的材料：不借用 exemplar 的 protagonist/antagonist/turn，不引入 `story_frame`、`resolution_type`、`exemplar_blueprint`。
- 排序不得为了"更有故事性"抬高弱证据；**weakest honest story 优先于 most dramatic story**。
- 本步骤只产生候选与选择，不产出正文 prose。
- 选定主线对 schema 的写入仍需通过 integrity gate 的 theme_grounding / knot_authenticity / payoff_feasibility 检查。
