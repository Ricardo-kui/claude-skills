# Vault 基线检索协议（Theory）

> 外置自 `write-theory/SKILL.md` Phase 1.2。执行条件：paper-state.yaml 中 `paper.vault` 节存在且至少有一个非 null 字段；无 vault 配置时静默跳过。

**回退树与总纪律以 `../paper-state-protocol/references/vault-retrieval.md` 为唯一权威**——三级回退（章节-证据映射 → 作战室/全文搜索 → 静默跳过）、Brief 纪律、Section 特化总表均见该文件。本文件只登记 Theory 侧差异，不重复定义回退树。

## Theory 侧差异

- **执行时点**：Phase 1.2（确认理论路由后），非 Phase 0；本步骤为可选，无 vault 配置时静默跳过，不阻塞。
- **行过滤**：读取 `vault.section_evidence_map` 后只过滤 "Theory" / "T" 行（按 Section 列或命题 ID 前缀匹配）；如有 `vault.war_room`，补读 canonical handle buckets 和 rival mechanism layers。
- **回退搜索关键词**：映射文件不可读时，以 `paper.title` 和 `introduction.theory_hints.core_constructs` 为关键词搜索（限制 10 条）。

## Theory Vault Knowledge Brief 输出格式（列差异）

相对 protocol 通用 Brief，Theory 版以「机制证据卡片」表为核心列结构，其余块（Rival Mechanisms、概念锚点、证据完整度）沿用 protocol 格式：

```markdown
## Vault 知识简报（Theory）

### 机制证据卡片（来自章节-证据映射 Theory rows）
| 命题ID | Citation Key | 证据用途 | Vault Note |
|--------|-------------|---------|-----------|
| [T1] | [@citekey] | [理论定义/机制核心/假设支撑] | [[note_path]] |
| ... | ... | ... | ... |

### Rival Mechanisms 需区分（来自项目作战室，如有）
- vs. [rival_mechanism_1]: [区分策略——从 war_room rival anchors 提取]

### 概念锚点（来自章节-证据映射或概念库搜索）
- [[概念 - ...]]: [一句话概括与本文理论的关联]

### 证据完整度
- Vault 命中: N 条理论级证据
- [如命中数 < 3，提示 "证据映射中 Theory 条目较少，建议从 canonical notes 补读或扩展章节-证据映射"]
```

**使用方式**：Brief 中的 citation keys 作为 Phase 2-4 理论构建和假设推导的文献弹药——每条 hypotheses 的机制链应优先引用 Brief 中标注为"机制核心"或"假设支撑"的文献。Brief 不覆盖用户在 Introduction 中已确立的理论框架选择。

**通用性保证**：本步骤不假定 Vault 结构或文献内容。所有路径来自 paper-state.yaml 的 vault 字段，技能本身不含项目特定硬编码。
