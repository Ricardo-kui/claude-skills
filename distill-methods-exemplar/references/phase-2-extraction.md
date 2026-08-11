# Phase 2 — 深度提炼：段落功能、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

## 2.1 段落功能提炼

回答：这个段落完成了什么**说服动作**？

| 说服动作 | 示例 |
|----------|------|
| 合法性论证 | Setting 段落论证"为什么这个情境适合检验理论" |
| 可审计性 | 样本漏斗让审稿人可以复现样本选择 |
| 对齐性 | 变量操作化段落建立构念→假设→测量的映射 |
| 抗辩性 | Controls 段落预判竞争性解释并提前排除 |
| 可信性 | 识别策略段落让审稿人相信因果推断成立 |
| 导航性 | M10 段落预告 Results 的阅读顺序 |

## 2.2 表达骨架提炼（Expression Skeleton）

将具体措辞抽象为**可填充的句法结构**。这是最关键的输出。

**骨架格式**：
```text
[功能标签]: 论证 setting 合法性
[骨架]: [Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period].
[原始句锚点]: "This setting provides a natural laboratory for examining how firms' product portfolios shape competitive dynamics, for three reasons."（来源论文原句 1–2 句，15–40 tokens，风格参照用）
[可迁移性]: 高 — 出现在 12/28 篇范文中
[范式排他性]: 通用 setting 论证，不绑定特定设计
[设计变体]: DiD 版本替换首句为政策冲击描述；实验版本替换为"We test X using a Y experiment"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- **原始句锚点（verbatim anchor）**：来源论文中的 1–2 句原文（15–40 tokens），保留原味——骨架抽象负责"结构可迁移"，锚点负责"语言风味不丢失"。生成时以锚点校准"顶刊味道"，不逐字复制。选句标准：最能代表该变体叙事手法的句子（不是信息量最大的，而是最有"论文味"的）
- **锚点拼接硬规则（2026-08-09 审计教训）**：多句锚点必须保留省略号标记——**禁止跨段落/跨小节无声拼接**；同段删句也必须用 "..." 标注被删内容。读者会把锚点当连续引文，无声拼接会误导读者的因果链理解
- **锚点来源检索**（取原句/补锚点时）：优先本次蒸馏论文原文；其次按论文 id/作者/标题检索 Obsidian 知识库：
  - `D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\_parsed_texts\mvp30`（MVP30 解析文本，主力库，frontmatter 含 journal/author/year，正文为全文）
  - `D:\OneDrive\Obsidian Vault\Clippings`（网页剪藏）
  - `D:\OneDrive\Obsidian Vault\文献笔记库\01 导入\论文导入`（OvisOCR 论文导入）
  检索不到原文时锚点标记"待补"，不阻塞写入
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类设计所需）
- 设计变体（同类骨架在不同设计中的改写模式）
- **skill_gap**（相对于 write-methods 当前 corpus 的状态）：
  - `ADD`：当前 corpus **无**此类变体 → 新增到目标设计类型文件
  - `EXTEND`：当前 corpus **有**但本论文提供了额外维度 → 追加为变体
  - `REPLACE`：当前 corpus 的旧变体**质量不如**本论文 → 标记旧变体，建议替换
  - `SKIP`：与当前 corpus **高度重叠** → 不写入，仅在学习要点中记录
  - 每个骨架必须标注对应的 `目标文件`（如 `生存分析.md`）和 `目标槽位`（如 M7）

## 2.3 Validity Logic 提炼

提取该 Methods 如何处理三类 validity threat：

| Threat 类型 | 提炼问题 |
|-------------|----------|
| 内部效度 | 如何排除 omitted variable / reverse causality / simultaneity？识别策略是什么？ |
| 构造效度 | 如何论证 measure 捕捉了 construct？是否有效度检验链？ |
| 外部效度 | Setting 的 boundary 在哪里？是否讨论 generalizability 限制？ |

输出格式：
```yaml
phase_2_distillation:
  M1_setting:
    persuasive_action: "合法性论证"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (12/28)"
        paradigm_exclusivity: "通用"
        design_variants: ["DiD variant", "Experiment variant"]
    validity_logic:
      internal: "..."
      construct: "..."
      external: "..."
  # ... 其余槽位
```
