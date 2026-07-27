# Visual Evidence（视觉证据设计，Booth Ch13）

> 来源：Booth et al. 2024, *The Craft of Research*, Chapter 13 "Communicating Evidence Visually"。
> 验证状态：EMERGING——Booth 是通用学术写作书而非管理学语料；设计原则通用，**定量适配注**为本土化补充。
> 适用位置：write-results 的 R2（表格导航）、R4（交互效应图）、R7（稳健性汇总表 / 规格曲线图）涉及表图设计时必读。

## 1. 表还是图：形式匹配效果（§13.1–13.2）

| 数据形态 | 选择 | Booth 原文锚点 |
|---------|------|---------------|
| 数字少而简单 | **句子** | "readers can grasp them as easily in a sentence as in a table" |
| 离散精确值，读者需自行核对 | **表** | "emphasizes discrete numbers and requires readers to infer relationships or trends on their own" |
| 离散项目间对比，要冲击力 | **条形图** | "emphasizes contrasts among discrete items" |
| 时间/连续变化 | **线图** | "suggests continuous change over time" |

总规则（逐字）：**"Choose the form that achieves the effect you want, not the one that first comes to mind."**

定量适配：回归主结果→表（精确、可核对）；交互效应/条件效应→图（读者无法从交互项系数直观推出模式）；系数跨规格稳定性→规格曲线图（线图变体）。饼图在管理定量论文中基本不出现——一行禁令："Avoid using pie charts to convey quantitative data in any detail. For that, use bar charts."

## 2. 标题/图例纪律（§13.3.1）

- **位置**：表的 label 叫 *title*，置于表**上方** flush left；图的 label 叫 *legend/caption*，置于图**下方** flush left（与顶刊排版惯例一致）。
- **标题描述数据，不是泛泛主题**：
  - ❌ "Heads of households"
  - ✅ "Changes in one- and two-parent heads of households, 2005–2020"
- **标题不写背景信息或数据含义**（解读留给正文）：
  - ❌ "Weaker effects of counseling on depressed children before professionalization of staff, 2012–2022"
  - ✅ "Effect of counseling on depressed children, 2012–2022"
- 呈现相似数据的多个图表，标题必须互相区分（加样本/情境限定语）。
- **Frame 每个图表**：图表前一句解释如何解读 + 指出希望读者聚焦的位置（"Introduce the table or figure with a sentence that explains how to interpret it. Then highlight what you want readers to focus on."）——已内置在 R2 表格导航与 R4 图解读句骨架中，此处是通用纪律。

## 3. 简洁规则（§13.3.2）

- **只放与论点相关的数据**；为存档完整性提供的数据标注后移入 appendix。
- **禁双向深色网格线**（"Never use both horizontal and vertical dark lines"）；仅复杂表用浅灰线；多行表每第五行浅 shading。——与顶刊 **booktabs 三线表惯例收敛**（顶线/栏目线/底线，无竖线），Booth 规则是该惯例的读者心理学依据。
- 不用颜色/色阶**单独**标记对比（视觉障碍读者无法区分）——用图案/线型/标注叠加。
- 禁 3D 效果与象形柱（iconic bars）："Both look amateurish and can distort how readers judge values."
- 背景网格线仅在读者需要读精确值时使用，且用浅灰。

## 4. 表格细则（§13.4.1）

- 行列**按强调原则排序**，不默认字母序（"Do not automatically choose alphabetic order"）。
- 数字取整到相关精度。
- 合计置列底/行右，不置顶/左。

定量适配：回归表的"强调原则排序"= **列按模型演进排序**（baseline→full→interaction），行按 IV→moderator→controls→FE→N/R² 惯例——这就是 Booth 原则在回归表上的本土化形态。

## 5. 伦理四规则（§13.5，逐字）

> - "Do not manipulate a scale to magnify or reduce a contrast.
> - Do not use a figure whose image distorts values.
> - Do not make a table or figure unnecessarily complex or misleadingly simple.
> - If the table or figure supports a point, state it."

**重点应用场景**（本 skill 的高危区）：
- **R4 交互效应图**：截断纵轴会夸大两线斜率差异——披露纵轴范围；若从非零点起标，必须在 caption 或正文中明示。
- **R7 系数图/规格曲线**：CI 必须显示（不能只画点估计——既有 slot-R7 禁忌与此收敛）；纵轴截断会夸大或掩盖系数跨规格的波动。
- 双轴图暗示虚假相关、堆叠面积图排序误导——管理论文中罕见但出现即违规则 2。

**第四条是本 skill 的既有纪律**：图表支持论点就在正文中明言（R2/R4 骨架已内置"Thus, Hypothesis [x] is supported"收束）——图表不自证，论点不明言等于图表白做（联动 evidence-standards.md 第 5 问 "Clear and understandable"）。

## 与既有骨架的关系

- R2 表格导航模板（"Table [x] reports... Model [2] adds..."）= §2 frame 纪律的本土化实例
- R4 "Figure [x] plots the predicted values..." = §1 形式匹配（交互→图）+ §2 frame 纪律
- R7 规格曲线变体 = §1 线图变体 + §5 规则 3（显示 CI = 不 misleadingly simple）
- 本文件提供**通用原则层**，slot 文件提供**句式层**；冲突时以期刊排版要求为准
