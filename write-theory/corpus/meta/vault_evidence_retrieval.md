# Vault 基线检索协议（Theory）

> 外置自 `write-theory/SKILL.md` Phase 1.2。执行条件：paper-state.yaml 中 `paper.vault` 节存在且至少有一个非 null 字段；无 vault 配置时静默跳过。

在确认理论路由后，从用户知识库拉取当前主题的理论证据。**本步骤为可选：无 vault 配置时静默跳过。**

**执行条件**：paper-state.yaml 中 `paper.vault` 节存在且至少有一个非 null 字段。

**检索流程**（三级回退，不阻塞）：

```
paper-state.yaml 中 paper.vault 是否有配置?
│
├── vault.section_evidence_map 非空 → 读取该文件
│   → 过滤到 "Theory" / "T" 行（按 Section 列或命题 ID 前缀匹配）
│   → 提取每行: 命题ID, citation key, Vault note path, 证据用途
│   → 如有 vault.war_room，补读 canonical handle buckets 和 rival mechanism layers
│   → 生成 "Vault Knowledge Brief (Theory)"
│
├── vault 路径存在但文件读不到 → 用 Obsidian MCP search_notes
│   以 paper.title 和 introduction.theory_hints.core_constructs 为关键词
│   搜索 Vault（限制 10 条）→ 提取 citation key 和 note path
│
└── 无 vault 配置或全部为 null → 静默跳过
```

**Theory Vault Knowledge Brief 输出格式**（所有内容来自 Vault）：

```markdown
## Vault 知识简报（Theory）

### 机制证据卡片（来自章节-证据映射 Theory rows）
| 命题ID | Citation Key | 证据用途 | Vault Note |
|--------|-------------|---------|-----------|
| [T1] | [@citekey] | [理论定义/机制核心/假设支撑] | [[note_path]] |
| ... | ... | ... | ... |

### Rival Mechanisms 需区分（来自项目作战室，如有）
- vs. [rival_mechanism_1]: [区分策略——从 war_room rival anchors 提取]
- vs. [rival_mechanism_2]: [区分策略]

### 概念锚点（来自章节-证据映射或概念库搜索）
- [[概念 - ...]]: [一句话概括与本文理论的关联]

### 证据完整度
- Vault 命中: N 条理论级证据
- [如命中数 < 3，提示 "证据映射中 Theory 条目较少，建议从 canonical notes 补读或扩展章节-证据映射"]
```

**使用方式**：Brief 中的 citation keys 作为 Phase 2-4 理论构建和假设推导的文献弹药——每条 hypotheses 的机制链应优先引用 Brief 中标注为"机制核心"或"假设支撑"的文献。Brief 不覆盖用户在 Introduction 中已确立的理论框架选择。

**通用性保证**：本步骤不假定 Vault 结构或文献内容。所有路径来自 paper-state.yaml 的 vault 字段，技能本身不含项目特定硬编码。