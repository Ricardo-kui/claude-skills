---
type: index
canonical_id: "literature-turns-index"
status: ✓ STANDARD
created: 2026-05-20
description: Literature Turn 三种策略的路由图、速查表和跨 skill 接口说明
---

# Literature Turns 索引 — 从 Hook 到学术对话的过渡策略

## 概述

Literature Turn（P2-P3）的核心功能是将 Hook 建立的注意力转化为学术对话。这不是文献综述，而是"将 Hook 中的张力重新框定为学术问题"。这个过渡的质量决定读者是否感觉 Hook 是"营销噱头"还是"真正的学术贡献起点"。

三种策略对应三种 Gap 类型，各有不同的文献诊断和修辞逻辑。

---

## 策略速查

| 策略 | 文件 | Gap 类型 | 能量 | 核心逻辑 | 文献诊断 |
|------|------|---------|------|---------|---------|
| **Progressive Coherence** | `01-progressive-coherence.md` | Incompleteness | 低–中 | "已有进展，但遗漏了 C" | 单一传统充分发展，自然留下空白 |
| **Synthesized Coherence** | `02-synthesized-coherence.md` | Inadequacy | 中 | "多个传统各自合理，但在交汇处集体盲区" | 多个传统各自正确，但互不知晓 |
| **Non-Coherence** | `03-non-coherence.md` | Incommensurability | 高 | "两个理论不能同时正确——除非重新理解" | 两个理论都有证据，但预测相反 |

---

## 路由决策树

```
用户的研究对已有文献的主要诊断是什么？
│
├─ "已有文献做了 A 和 B，但漏了 C"
│   → Gap: Incompleteness
│   → 策略: Progressive Coherence
│   → 关键句式: "Although research has... little attention has been paid to..."
│   → 搭配 Hook: 03-data-shock, 10-practical-puzzle, 02-epigraph-quote-pivot (低/中能量)
│   → 搭配 Tension: 01-despite-progress-unaddressed
│
├─ "多个文献流各自抓到了现象的一部分，但都没看到全貌"
│   → Gap: Inadequacy
│   → 策略: Synthesized Coherence
│   → 关键句式: "Two streams... developed largely in parallel... leaving [intersection] underexplored"
│   → 搭配 Hook: 05-literature-consensus-blindspot, 04-puzzle-paradox, 19-forward-looking-shift
│   → 搭配 Tension: 02-implicit-assumption-wrong, 03-structural-blindspot
│
└─ "两个理论分别预测相反结果，各自都有证据——它们不能同时正确"
│   → Gap: Incommensurability
│   → 策略: Non-Coherence
│   → 关键句式: "These perspectives offer incompatible predictions about [outcome]"
│   → 搭配 Hook: 06-paradigm-challenge, 17-classic-debate-constraint, 18-theory-contradiction-empirical-paradox
│   → 搭配 Tension: 04-reality-contradicts-consensus, 06-theoretical-imbalance
```

---

## 三策略对比矩阵

| 维度 | Progressive Coherence | Synthesized Coherence | Non-Coherence |
|------|----------------------|----------------------|---------------|
| **Gap 能量** | 低–中 | 中 | 高 |
| **文献流数量** | 1 个主流 | 2+ 个独立 | 2 个对立 |
| **文献态度** | "你们做得好" | "你们各自对了一部分" | "你们不能都对" |
| **核心隐喻** | 地图空白 | 盲人摸象 | 两军对垒 |
| **解决方案** | 填补空白 | 连接盲区 | 超越对立 |
| **典型 Hook** | data-shock, practical-puzzle | consensus-blindspot, forward-looking-shift | paradigm-challenge, classic-debate-constraint |
| **典型 Tension** | despite-progress-unaddressed | implicit-assumption-wrong, structural-blindspot | reality-contradicts-consensus, theoretical-imbalance |
| **变体数量** | 5 (A–E) | 5 (A–E) | 5 (A–E) |
| **反模式风险** | 弱缺口（没有解释为什么遗漏重要） | 虚假合成（两个"传统"实为同一流派变体） | 稻草人（一方被描绘得极其愚蠢） |

---

## 期刊偏好

| 期刊 | 首选策略 | 可接受策略 | 避免策略 |
|------|---------|-----------|---------|
| **ASQ** | Non-Coherence | Synthesized Coherence | Progressive Coherence（能量过低） |
| **ASR** | Non-Coherence | Synthesized Coherence | Progressive Coherence |
| **SMJ** | Synthesized Coherence | Progressive Coherence, Non-Coherence | — |
| **AMJ** | Synthesized Coherence | Non-Coherence, Progressive Coherence | — |
| **OS** | Synthesized Coherence | Non-Coherence | Progressive Coherence（需要更强的结构性缺口） |
| **JM/JMR** | Progressive Coherence | Synthesized Coherence | Non-Coherence（不典型） |
| **JOM** | Progressive Coherence | Synthesized Coherence | Non-Coherence |
| **MS** | Progressive Coherence | Synthesized Coherence | Non-Coherence |

---

## 跨 Skill 接口

### 上游（Hook → Literature Turn）

Hook 的类型直接约束可用的 Literature Turn 策略。参见 `hooks/_index.md` 的必须配对表。

### 下游（Literature Turn → Tension）

Literature Turn 的收尾句（"However, what remains unclear is..." / "leaving [gap] underexplored" / "These incompatible predictions cannot be simultaneously true"）必须自然过渡到 Tension 段。关键规则：

- **Progressive Coherence 收尾** → 使用 `01-despite-progress-unaddressed` 或 `08-cost-vs-benefit`
- **Synthesized Coherence 收尾** → 使用 `02-implicit-assumption-wrong` 或 `03-structural-blindspot`
- **Non-Coherence 收尾** → 使用 `04-reality-contradicts-consensus` 或 `06-theoretical-imbalance`

### 下游（Literature Turn → write-theory）

Literature Turn 的策略选择影响 write-theory 的推荐变体：

| Literature Turn | 推荐 Theory 变体 |
|----------------|-----------------|
| Progressive Coherence | 假设树型、机制推演型 |
| Synthesized Coherence | 构念辨析型、调节效应型 |
| Non-Coherence | 竞争假设型、质性过程理论型 |

---

## 文件结构

```
literature-turns/
├── _index.md                          ← 本文件（路由图 + 速查表）
├── 01-progressive-coherence.md        ← Progressive Coherence (5 variants)
├── 02-synthesized-coherence.md        ← Synthesized Coherence (5 variants)
├── 03-non-coherence.md                ← Non-Coherence (5 variants)
├── literature-turn-templates.md       ← 快速参考卡（三种策略的核心模板精简版）
└── table-embedded-review.md           ← 表格嵌入型文献回顾
```

---

## 新增 Literature Turn（待分类）

- table-embedded-review.md — Systematic literature table embedded in Introduction

---

## 更新日志

- **2026-05-20**: 创建索引文件；扩充 03-non-coherence 至 5 变体 + 关键技巧；扩充 02-synthesized-coherence 至 5 变体 + 升级动作表 + 对比表
- **2026-05-19**: 从 literature-turn-templates.md 拆分出 3 个独立文件，各自扩至 3-4 变体
- **2026-05-18**: 创建 literature-turn-templates.md（初始版本，含三种策略的合并模板）
