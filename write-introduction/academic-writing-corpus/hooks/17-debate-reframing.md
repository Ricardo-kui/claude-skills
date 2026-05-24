---
type: canonical_reference
canonical_id: "17-debate-reframing"
status: EXPERIMENTAL
hook_type: Debate (Reframing)
cross_paper: SINGLE-INSTANCE
generativity: ADAPTABLE
exclusivity: HIGH
source_papers:
  - park_lange_jeon (SMJ): "A long-standing debate... Rather than attempting to settle that disagreement... our interest lies in how these perspectives manifest in practice."
created: 2026-05-24
source: Extracted from MVP30 batch_2026-05-24
---

# 17-debate-reframing — 辩论重构型 Hook

## 功能定义

开场呈现一个领域内的经典学术辩论（两个视角/学派），但不试图裁决辩论，而是将问题重构为可实证检验的实践问题——"如果约束条件改变，行为者会怎么做？" 此 Hook 在辩论双方之间保持中立，利用辩论的 relevance 而不陷入任何一方。

## 适用场景

- 研究领域存在经典、尚未解决的学术辩论（stakeholder vs shareholder, exploration vs exploitation, agency vs stewardship）
- 作者不希望偏袒辩论的任何一方（避免引发对立审稿人）
- 贡献是实证性的——揭示 "在实践中实际发生了什么" 而非 "谁的理论正确"
- 目标期刊接受理论辩论作为背景语境（SMJ/OS/AMJ 都适用）

---

## 句法模板

```
"A long-standing debate in [field] centers on two perspectives: the [Perspective A view], 
which emphasizes [value A], and the [Perspective B view], which focuses on [value B] 
([citations]). Even as [one perspective] is gaining traction in the academic literature 
([citations]) and in the business press ([examples]), disagreement persists between 
advocates of [Perspective A] and those of [Perspective B] ([citations]). Rather than 
attempting to settle that disagreement here as a theoretical or philosophical matter, 
our interest lies in how these perspectives manifest in practice. Specifically, 
realizing that [actors] shape their [decisions/strategies] over time in response to 
various [pressures/constraints], we explore what they might do if certain constraints 
were relaxed, allowing them greater flexibility in decision-making ([citations]). This 
leads to a key question: [reframed empirical RQ]. Insight into such [preferences/behaviors] 
could help [audience] realize how [mechanism] would need to be constrained or enabled 
to achieve a desired orientation toward [outcome]."
```

**来源**: park_lange_jeon (SMJ), P1

**关键要素**:
- "A long-standing debate in [field] centers on..." — 呈现辩论
- "Rather than attempting to settle that disagreement here as a theoretical or philosophical matter" — **pivot 句**（精华所在）
- "our interest lies in how these perspectives manifest in practice" — 重构方向
- "what they might do if certain constraints were relaxed" — 实证问题框架
- Pivot 必须出现在 Hook 内部（不能拖延到 Literature Turn）

---

## 组装规则

### 必须配对
- 与 **Incompleteness** Gap: "尚未探索的实证现象" 是自然配对
- 与 **Mechanism** 或 **Phenomenon** Contribution: 解释实践中的 "how" 或记录 "what actually happens"

### 反模式提醒
- **真实辩论要求**: 辩论必须在文献中真实存在（有对立引用），不能是作者构造的 "pseudo-debate"
- **不要偷偷偏袒**: pivot 后不能暗示 "我们证明了 Perspective A 是对的" — 这会破坏 Hook 的承诺
- **辩论不能是 straw man**: 不能把一方描述为明显错误（这样就不需要 "rather than settling" 了）
- **必须在 Introduction 前 3 句内引入**: 长期辩论是读者的已知信息，不要花太长篇幅解释

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| SMJ | ⭐⭐⭐⭐⭐ | SMJ 偏好辩论驱动的 Hook |
| AMJ | ⭐⭐⭐⭐☆ | 可用，但 AMJ 期望更现象驱动的开场 |
| OS | ⭐⭐⭐⭐☆ | 辩论 Hook + 实证 pivot 是 OS 的舒适区 |
| ASQ | ⭐⭐⭐☆☆ | 可用，但 ASQ 偏好更理论驱动的框架 |

---

## 相关语料

- 与 `tensions/01-despite-progress-unaddressed.md` (Incompleteness) 配对使用
- 与 `tensions/14-debate-unresolved.md` (Inadequacy) 区分：后者将辩论未解决作为 gap 本身，本 Hook 将辩论作为语境
