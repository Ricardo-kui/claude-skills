# Assumption-Challenging 假设挑战诊断（Alvesson & Sandberg 2013）

> 来源：Alvesson & Sandberg (2013) *Constructing Research Questions: Doing Interesting Research*——五类可问题化假设（Ch01/Ch05）、六步法（Ch05）、mystery construction（Ch08）。配套：2010 *Organization* 文章笔记（gap-spotting vs problematization 三模式）。
> **何时加载**：diagnose-introduction 在 Gap 类型诊断之后、Makadok 贡献维度之前加载——判断"你的研究挑战的是哪一类假设"以及"挑战的洞见 × 惊异性"。
> **与 GBL 的关系**：GBL 三型问题化（Incomplete / Inadequate / Incommensurate）回答"缺口是什么类型"；本文件回答"挑战的是哪一层假设"——两者正交，同时输出。G-L working thesis 四模型（misperception / gap / modification / new understanding）可作 thesis 层交叉验证。
> **与故事层的接口**：story-frame-menu Step A 问题 9（前提可疑 → assumption-flip）用本文件五类假设扩展；讲法汇编家族 10 按五类组织。

## 五类可问题化假设

| 类型 | 含义 | 挑战的洞见来源 | 典型句式 | 风险/跑道 |
|------|------|--------------|---------|----------|
| **in-house** | 某一特定研究传统内部的假设（该传统内被当常识） | 传统内部的矛盾或未检视前提 | "research in this tradition assumes [X]" | 低风险、贡献小而精 |
| **root metaphor** | 支撑整个研究领域的根本隐喻/意象（如"组织是机器"） | 隐喻适用范围的边界 | "the metaphor of [X] has channeled inquiry away from…" | 中高风险、需隐喻替代物 |
| **paradigm** | 学科范式的核心假设（理性选择、均衡等） | 范式间可通约性问题 | "even [mainstream paradigm] takes [Y] for granted" | 高风险、需充分理论跑道 |
| **ideology** | 政治/道德/意识形态预设（效率至上、市场天然等） | 价值前提的可争议性 | "implicitly endorsing [value premise]" | 中风险、需价值立场的自反性 |
| **field** | 整个领域跨传统普遍共享的假设 | 领域级盲区（被所有传统共同默认） | "scholars across this field assume [Z]" | 中高风险、贡献最大但需最强论证 |

> **范围越广不必然越有价值**——关键是挑战的**洞见（insight）**与**惊异性（surprisingness）**。挑战 in-house 假设安全但可能琐碎；挑战 paradigm/root metaphor 贡献大但"挑战落空"风险高（假设其实成立则退化为 Incompleteness）。

## 六步法（problematization 生成流程）

1. **界定文献域**（identify a literature domain）——与 GBL Move 2 的对话对象一致
2. **阐明其假设**（identify underlying assumptions）——用五类假设逐层扫描
3. **评估假设**（evaluate the assumptions）——哪些值得挑战？按洞见 × 惊异性排序
4. **构造替代性假设基础**（develop alternative assumption ground）——新研究问题由此长出
5. **考虑目标受众**（relate to audiences）——⚠️ 最常被跳过的步：替代性基础对目标期刊/读者是否"可被重新理解"
6. **评估前景**（evaluate the alternative ground against the audience）——能否产生有前景的问题 + 可执行设计

## Mystery Construction（第二条路径——与文献问题化互补）

研究问题也可以从**经验材料**出发：识别反常/矛盾/未解之处（mystery），再寻求解释（Alvesson & Kärreman 2007 系）：

| 路径 | 起点 | 终点 | 互补用法 |
|------|------|------|---------|
| 文献问题化 | 文献假设 → 构造替代基础 | 新问题 | 提供"为什么现在"的时机论证 |
| mystery construction | 经验反常/矛盾 → 解释性追问 | 新问题 | 提供"值得挑战"的证据锚（challenge 的落地） |

**组合信号**：当研究描述里有"现象很奇怪但文献没解释"（而非"文献错了"）→ mystery 路径；当有"文献的前提可疑"→ 问题化路径；顶刊常见两者叠加（mystery 作 hook/evidence，问题化作 gap）。

## 三书交叉验证表（GBL 三型问题化 × G-L working thesis 四模型 × Alvesson 五类假设）

> G-L Ch06 的 working thesis 四模型（misperception / gap in knowledge / modification of accepted view / new understanding）是**论文层面**的主张形态；GBL 三型是**文献关系层面**的缺口类型；Alvesson 五类是**假设层面**的挑战对象——三层正交，同一次诊断应三层齐备。

| G-L working thesis 模型 | GBL 缺口类型 | Alvesson 假设类型（典型） | 叙事形态 |
|------------------------|-------------|--------------------------|---------|
| misperception（共识误解） | Inadequacy（implicit assumption wrong） | field / ideology | 挑战共识前提——assumption-flip 家族 |
| gap in knowledge（知识缺口） | Incompleteness | （无假设挑战，标 none） | 填空型——标准 progressive |
| modification of accepted view（修正既有观点） | Inadequacy（refinement） | in-house | 局部修正——常规 Inadequacy |
| new understanding（全新理解） | Incommensurability / 重新框定 | root-metaphor / paradigm | 范式级翻转——最高能量 |

**用法**：诊断时先定 GBL 三型（现有 Step 3），再定 thesis 模型（本表第一列），再定假设类型（五类）——三者不一致时是诊断信号（如 GBL=Inadequacy 但 thesis=gap-in-knowledge → 可能是错配，需重审问题陈述）。

## 诊断输出块（供下游 write-introduction / story-frame-menu 消费）

```yaml
assumption_challenging:
  challenged_assumption_type: "in-house | root-metaphor | paradigm | ideology | field | none"
  challenged_assumption_statement: "[被挑战的假设一句话；type=none 时填 null]"
  alternative_ground: "[替代性假设基础一句话]"
  insight_surprisingness: "high | medium | low"    # 洞见 × 惊异性综合评估
  target_audience_fit: "high | medium | low"       # 六步法第 5 步：替代基础对目标期刊读者的可接受度
  mystery_anchor: "[经验反常/矛盾锚点或 null——mystery 路径证据]"
  thesis_crosscheck: "[G-L working thesis 映射：misperception | gap-in-knowledge | modification | new-understanding | null]"
  risk_notes: "[挑战落空风险：假设其实成立 / 范围过广缺跑道 / 替代基础不可执行]"
```

## 与 story-frame-menu 的接口

- **Step A 问题 9**（前提可疑 → assumption-flip）命中后，用五类假设定位"挑战的是哪一类"：
  - `field` 类（跨传统共享）→ assumption-flip 的深层版（可能升级为 overlooked-alternative 的领域级变体）
  - `in-house` 类（单一传统内部）→ assumption-flip 的常规版（02-implicit-assumption-wrong 家族）
  - `root-metaphor` / `paradigm` 类 → 风险最高，story-frame-menu 前提风险清单须提示"需论证跑道"
- **讲法汇编家族 10**（前提推翻）：按五类假设组织实例（当前无蒸馏实例；军事×薪酬手稿挑战的 uniform imprint 前提 = field 类候选）。
