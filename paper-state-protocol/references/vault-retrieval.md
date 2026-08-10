# Vault 知识检索协议（§5，LOOP 5: Vault → Write Evidence）

## 发现机制（三级回退）

write-introduction 和 write-theory 的 Phase 0 在检查 paper-state.yaml 后，执行 Vault 检索：

```
paper-state.yaml 中有 vault.section_evidence_map?
│
├── YES → 读 章节-证据映射
│   → 按 Section 过滤相关行（如 write-theory → filter "Theory" + "T" rows）
│   → 提取: citation key, 命题, Vault note path, 证据用途
│   → 生成 "Vault Knowledge Brief"（结构化文献摘要）
│
├── YES 路径存在但文件不可读 → 继续下一级
│
├── paper-state.yaml 中有 paper.vault.war_room?
│   → 读项目作战室 → 找 canonical handle buckets 和文献分组
│   → fallback：Vault 全文搜索 paper.title 或 core_constructs
│
└── 全部不可用 → 跳过 Vault 检索（当前行为，不降级）
```

## Vault Knowledge Brief 格式

检索后在 Phase 0 诊断输出中附加以下简报：

```markdown
## Vault 知识简报（[Section]）

### 核心文献（来自 章节-证据映射）
| 命题 | Citation Key | 证据用途 | Vault Note |
|------|-------------|---------|-----------|
| T1 | @JohnsonEtAl2015 | 理论定义 / 机制核心 | [[johnsonetal2015...]] |
| T2 | @YoonEtAl2012 | 微观过程 / H1 机制支撑 | [[yoonetal2012...]] |

### 机制 Claim Cards（来自 论证卡库）
- [[Claim - ...]]: [一句话概括——来自 Vault 论证卡库，与本文理论假设相关的 claim card]
- [[Claim - ...]]: [同上]

### Rival Mechanisms 需区分
- vs. [rival_mechanism_1]: [区分策略——从 war_room rival anchors 提取]
- vs. [rival_mechanism_2]: [区分策略]

### 概念锚点（来自 概念库/）
- [[概念 - ...]]: [一句话概括与本文理论的关联]
- [[概念 - ...]]: [同上]

### 证据完整度
- Vault 检索命中: [N] 篇 canonical notes + [M] 条 claim cards
- 建议补读: [列出可能从 Tier 1 补读的关键文献]
```

## Section 特化

| Section | Vault 检索重点 | 关键 Vault 资产 |
|---------|---------------|----------------|
| **Introduction** | Hook 数据点、Gap 锚定文献、Literature Turn 引文簇 | 章节-证据映射 Introduction rows、项目领域文献地图（如有）、gap anchors |
| **Theory** | 机制证据卡片、Rival mechanism 区分、概念定义、边界条件文献 | 章节-证据映射 Theory rows、论证卡库 Claim Cards、canonical notes、概念库/ |
| **Methods** | 识别策略先例、变量操作化参照、关键变量防守文献 | 章节-证据映射 Methods rows、数据集/变量 note |
| **Results** | 贡献定位锚点、rival explanation 区分文献 | 章节-证据映射 Results/Discussion rows |

## 纪律

- Vault Knowledge Brief 是**检索摘要**，不是全文复制。每条 ~1 行概括 + Vault note link
- 用户阅读 Brief 后可说 "读那 3 篇" 来展开深读
- Brief 不替代 template 生成——它提供的是**内容弹药**，template 提供的是**结构骨架**
- 若 Vault 检索无结果（项目太新、笔记未建），不在 Brief 中编造
- 检索到但 paper-state.yaml 中未列的 citation key → 标注为 "Vault 候选，待确认是否纳入"
