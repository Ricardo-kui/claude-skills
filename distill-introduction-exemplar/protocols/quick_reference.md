# Introduction 蒸馏快速参考

> **何时使用**: 当完整 SKILL.md 因上下文压缩不可用时，Read 本文件并按此协议执行蒸馏。本文件是 SKILL.md Phase 0-3 的精简版。
> **目标**: 确保格式一致的 Fine-Grained Profile，即使完整 skill 指令不可用。

---

## 0. 输出文件命名与路径

```
Vault路径: D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\narrative_analysis\introduction\mvp30\fine_grained\batch_2026-05-24\
文件命名: {author_lowercase}_{year}_{journal}_distilled_introduction.md
```

---

## 1. Phase 0 — Gap × Contribution 分类（必须包含证据链）

### Gap 判断（三选一）

| Gap | 标志性语言 | 关键词 |
|-----|-----------|--------|
| **Incompleteness** | "Yet little research investigates" / "remains unclear" / "few studies have examined" | 遗漏 |
| **Inadequacy** | "prior research has treated X as Y, but this view overlooks" / "the implicit assumption that... may be incorrect" | 假设错误 |
| **Incommensurability** | "A consensus is building that... Yet counter-evidence suggests" / "Two theoretical perspectives offer incompatible predictions" | 理论矛盾 |

### 输出格式（必须严格遵循）
```text
[Gap 判定]: [类型]
[标志性语言证据]:
  - "具体句1" (段落位置)
[判定理由]: 一句话
[反证排除]:
  - 非 [另一类型]: 理由
[置信度]: 高 / 中 / 低
```

### Contribution 维度（Makadok 8选N）
Constructs / Mechanism / Boundary / Phenomenon / Level / Mode / Question / Output

---

## 2. Phase 1 — 功能模块映射

### 7 个标准模块（标注 located: true/false + paragraph_range）

| 模块 | 功能 | 识别标志词 |
|------|------|-----------|
| Hook | 建立兴趣 | 前1-2段；呈现 paradox/trend/anecdote/debate |
| Literature Turn | 建立对话 | "Prior research has..." / "Scholars have examined..." |
| Tension | 呈现 Gap | "Yet" / "However" / "Despite" / "little research" |
| Stakes | So what? | 理论/现象/实践后果；可能嵌入 Tension |
| Theory Lens | 引入解释视角 | "Drawing on..." / "We argue that..." / "We theorize" |
| Preview | 预告方法/发现 | 样本描述、模型、发现方向、效应量 |
| Contribution | 贡献声明 | "We contribute by..." / "This study advances..." |

### 输出：标记 actual_module_sequence + deviation_from_standard

---

## 3. Phase 2 — 表达骨架提炼

### 每个模块提炼：
1. **Persuasive Action**: 该模块完成了什么说服动作？
2. **Expression Skeleton**: 用 `[占位符]` 抽象句法结构
3. **Transferability**: 高/中/低 + 跨论文出现频次证据
4. **Gap 变体**: 该骨架在其他 Gap 类型中的改写方式（如有）

### 新建 Tension 的判断标准：
- 标志性句式在现有 16 个 tension 模板中**无匹配** → 新建 `{NN}-{description}.md`
- 如匹配现有模板但有变体 → 更新现有文件的变体部分

---

## 4. Phase 3 — Introduction DNA

### 必须包含的量化指标：
| 指标 | 计算 |
|------|------|
| 模块密度 | 总字数 / 模块数 |
| Hook-to-Puzzle 距离 | Hook 首句到首次 puzzle 陈述的句数 |
| Tension 深度 | 0-3: (a) 具体文献批评 (b) 理论后果 (c) 反例/矛盾 |
| Stakes 具体性 | 高/中/低 |
| Transition 链完整性 | 0-6（7模块间6个过渡点） |
| Makadok 可见性 | 0-8 |

### Narrative Style Profile（必须包含）：
- **Tone**: 主语气 + 次语气，附证据句
- **Paragraph Rhythm**: 段落节奏描述
- **Distinctive Features**: 该论文特有的叙事标记（至少3条）
- **Quality Markers**: strongest_aspect / weakest_aspect

---

## 5. 跨 Section 对齐检查

| 检查项 | 问题 |
|--------|------|
| Theory Lens ↔ Introduction | Introduction 承诺的理论是否在 Theory 中兑现？ |
| Contribution ↔ Hypotheses | Contribution 声明的维度是否对应实际假设？ |
| Preview ↔ Results | Preview 的发现方向是否与 Results 一致？ |

如仅处理 Introduction（无完整论文），全部标记为 N/A。

---

## 6. 关键反模式

- ❌ 仅基于 "few studies" 判定 Incompleteness——必须检查是否有隐式假设批评（→Inadequacy）
- ❌ 骨架中嵌入具体机构名/政策名/行业术语——必须用 [占位符] 泛化
- ❌ 缺少证据链（[标志性语言证据] + [反证排除]）——Phase 0 必须包含
- ❌ Contribution 维度与 Gap 类型逻辑矛盾（Incommensurability × Phenomenon 几乎不可能）
- ❌ Tension 选择与 Gap 类型不匹配（如 Incompleteness 使用了 "implicit assumption wrong"）
- ❌ 忘记标注 deviation_from_standard

---

## 7. 蒸馏后动作

1. 保存报告到 Vault fine_grained 目录
2. 检查是否有**新骨架**需要注册到 `write-introduction` 语料库
3. 如发现新 tension/hook → 输出 `PROPOSE_ROUTING_CHANGE` 或 `ADD_REFERENCE` 审核计划；不得直接创建 corpus 文件、修改 `_evidence_registry.yaml` 或修改 `SKILL.md`
