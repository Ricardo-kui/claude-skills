# Phrasebank 索引 — Morley 2021 措辞变化库（auxiliary 语言实现层）
> 论证角色标注：critique-phrases=A&R 材料；hedging-strength=Claim 强度校准（Booth Ch06 hedge）；其余为跨角色措辞变体库；总文法见 填位规则见 `_argument-grammar.md`（story-blueprints/v4/rhetoric-moves/）

本索引组织 `phrasebank/` 下全部文件。**层级定位**：auxiliary——顶刊蒸馏模板与各 write skill 的 slot 骨架决定**说什么**；phrasebank 只在其措辞反复使用时提供**怎么换个说法**与**强度校准**。

> **调用入口**：各 write skill 的"措辞润色阶段"（write-introduction Phase 4 / write-theory 措辞润色 / write-methods & write-results 默认润色）默认查本目录。先读本索引定位，再开对应文件。

---

## 文件清单（按功能）

| 文件 | 功能 | 适用 section | Morley 源章 | 触发场景 |
|------|------|-------------|------------|---------|
| [`hedging-strength.md`](hedging-strength.md) | **hedging 强度阶梯**（5 档情态动词 + 认识论句式 + Discussion 解释非显著场景） | 全 section（Discussion/Theory 最频） | Ch.07 Being Cautious | 校准声明的认识论强度——避免越级（过度声明）或过度弱化（稀释贡献） |
| [`critique-phrases.md`](critique-phrases.md) | **单研究/单理论方法学批判**（指出方法/数据/理论局限 + 建设性批判） | Introduction（Literature Turn）/ Theory（竞争机制）/ Discussion | Ch.08 Being Critical | 为 problematize 句、竞争理论处理提供批判措辞（**必须配具体研究+局限**） |
| [`methods-process.md`](methods-process.md) | **过程描述变化**（sequence words / infinitive of purpose / using+instrument / 统计程序动词） | Methods（M2-M7 过程描述） | Ch.03 Describing Methods | Methods 句子级措辞变化，防同质化 |
| [`quantities-trends.md`](quantities-trends.md) | **数值与趋势描述**（描述统计转述 / 事件研究趋势） | Results（R1 描述统计 / R5 经济显著性 / R7 趋势） | Ch.13 Quantities + Ch.12 Trends | Results 数值转述与图形趋势描述 |

---

## 调用规则（每次必读）

1. **调用顺序**：顶刊模板/slot 骨架 → 本目录变化库 → claim-strength QC。骨架空白处优先用顶刊模板，phrasebank 不填补结构缺口。
2. 每个位置最多取 **2–3 个候选**；同一段落不连续堆叠两个以上 phrasebank 句式。
3. **必须替换占位符**并具体化（构念、数据源、程序细节、具体研究）。
4. **Specificity gate**：替换后的句子若仍可不加修改放进任何论文 → 不合格，加入具体 actor / construct / context。
5. claim strength 列是语气上限；涉及因果的遵守 `../../../write-methods/corpus/micro-templates/causal-hedging.md` 设计家族词汇表。
6. **退役规则**：某功能一旦被顶刊蒸馏语料覆盖（经 distill-* 验证），对应条目从本目录删除。本目录不计入 MVP30 paper_count。

---

## 与其他表达资产的关系（避免重复查）

phrasebank 是 **auxiliary 措辞层**，与以下资产分工：

| 资产 | 层级 | 职责 | 位置 |
|------|------|------|------|
| **顶刊 slot 骨架** | 主结构 | 决定每段说什么（hook/tension/四拍等） | 各 write skill 的 `references/slot-*.md` + `corpus/` |
| **micro-templates** | 句法层 | 关键句位的句式变体（because 从句、漏斗节奏等） | `../../write-methods/corpus/micro-templates/` |
| **phrasebank（本目录）** | 措辞层 | 同一功能的换说法 + 强度校准 | 本目录 |
| **prose-pathology** | 病理层 | 五病诊断 + 修复（fat suit 等） | `../../../pollock-qc/references/prose-pathology.md` |
| **hedging 判别** | 校验层 | 过度/不足声明的判别规则（§5.6/§5.7） | `../storytelling/prose-craft-checklist.md` |

**hedging-strength 与 prose-craft-checklist 的闭环**：hedging-strength 提供"选哪档强度短语"，prose-craft-checklist §5.6（Overclaiming）/§5.7（Defensive prose）提供"判别是否过强/过弱"。先选（hedging-strength）→ 再校验（§5.6/§5.7）。
