# Story Blueprint — Gamache, Neville, Bundy & Short (2020) SMJ

## 文件头

```yaml
id: gamache2020
paper: "Gamache, Neville, Bundy & Short (2020, SMJ) — Serving Differently: CEO Regulatory Focus and Firm Stakeholder Strategy（DOI 10.1002/smj.3134）"
distilled_sections: [intro, theory, methods, results]   # methods/results 来自 batch_09 细蒸馏（fine_grained）
source_records: [project-mvp30-gamache-etal2020, 00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_09_gamache2020_shipilov2020/gamache2020_regulatory_focus_stakeholder_fine_methods_results.md]
corpus_links:
  write-introduction: "tensions/01-despite-progress-unaddressed 变体N（三层递进 Incompleteness）；Stakes 嵌入 Tension（'This omission is critical, as...'）"
  write-theory: "corpus/sentences/mechanism_chain.md（宽度型三理由并行架构：'Additionally... Finally...'）；Ruling Out Alternatives T2 修辞策略"
  write-methods: "batch_09 细蒸馏范式：多 outcome 样本分裂 / outcome family 作理论图 / 文本测量构念效度辩护 / GEE vs Tobit 估计器拆分 / 威胁族控制组织"
  write-results: "模块化假设段节奏（expectation→model→coefficient→interpretation→magnitude/bounded non-support）；2SRI 内生性；替代测量按威胁分组；探索性跨域测试"
```

## Story

### one_liner

> 同一个 CEO 心理引擎（regulatory focus 的双系统：promotion / prevention）驱动两个文献从不放在一起看的战略域（governance 型与 social 型利益相关者战略）——不是两个域各有一串不同的原因，而是一双原因同时决定两个域怎么"服务得不一样"（2×2 对称映射）。

### knot

```yaml
knot:
  primary_type: cross-domain-unification   # 跨域统一型（新类型候选：两个分离研究域由同一机制统一解释）
  compound_types: []   # 内层 mild Inadequacy（分域研究的惯例）是成因，不是独立子结构
  statement: "CEO 的 regulatory focus 如何影响 firm stakeholder strategy？governance 与 social 两类战略被文献分域研究、各自罗列驱动因素——同一个心理构念的双系统能否统一解释两个域？"
  tied_at:
    - "Intro P1：无独立 Hook，冷启动——Hook 与 Lit_Turn 合并（通过文献建立重要性，与 Pfarrer 2010 同型）"
    - "Intro：Stakes 嵌入 Tension（'This omission is critical, as...'，Gap→Stakes 在 Tension 段内完成）"
    - "Theory：Theory Lens 跨两段（P3 = IV 侧 regulatory focus 理论；P4 = DV 侧 governance vs social 概念化），两段由不同文献流支撑"
  untied_at:
    - "Theory：2×2 对称映射（dual regulatory focus → dual strategy types）"
    - "Results：四个模块化假设段（2 CEO 构念 × 2 outcome family）"
  antagonist: "分域研究的惯例（governance 与 social 战略被分开研究、驱动因素清单分离）+ 读者的两个直觉替代预测（T2 明确列出并逐一拒绝）——反派是'领域的分工惯性'和'读者想当然'"
  antagonist_built_by:
    - "Ruling Out Alternatives 修辞：T2 过渡段列出两个直觉上合理的替代预测并拒绝，再展示正确预测——先立靶（读者直觉）再推翻（suspense 装置）"
    - "冷启动文献铺陈：不靠案例/人面，靠文献自身的张力建立'两个域从未被统一'的代价"
```

### characters

```yaml
characters:
  protagonist: [CEO regulatory focus (X，双系统 promotion/prevention 是双主角), stakeholder strategy (Y，governance/social 双 outcome family)]
  supporting:
    - "governance 型 / social 型 outcome family 分裂：DV 概念化把主角切成两面"
    - "proactive engagement（连续，GEE）vs receptivity to activism（有界，Tobit）：同一构念的两种可观测形态，估计器拆分与其对应"
  ensemble: [威胁族控制（firm capacity / prior stakeholder pressure / external pressure / industry / persistence / CEO attributes）、文本测量字典]
```

### resolution_logic

`unification` 统一（新解法性格候选）——**同一机制统一两个分离研究域**：2×2 对称映射（双构念 × 双域）+ estimator split 让两个 outcome family 各得其所。研究者是"发现共同引擎"的工程师：两个域的文献各有一张零件清单，本文证明共用一台发动机。辅以 ruling-out-alternatives（先证伪读者的直觉预测再给出正解）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：无 Hook 冷启动（P1 合并 Hook+Lit_Turn）；Theory Lens 跨两段（IV 理论 + DV 概念化）；三层递进 Incompleteness Tension；'This omission is critical' 把 gap 升为 stakes；'First... also complement to...' 双轨贡献（refinement + paradigm-level complement）"
  rising_action: "Theory：2×2 对称并行架构（每个假设 3 个独立平行理论理由，'Additionally... Finally...' 标准节奏）；T2 Ruling Out Alternatives（立靶→拒绝→正解）；Methods：样本按 outcome family 分裂（proactive 全面板 / receptivity 条件样本）；regulatory focus 从年报文本间接测量 + 效度辩护（'为什么文本是可追踪的痕迹'）；威胁族控制；GEE/Tobit 估计器拆分；滞后 + 聚类 SE"
  climax: "Results 主结果：四个模块化假设段落（expectation→model→coefficient→interpretation→magnitude）——2×2 的四个格逐格揭晓"
  falling_action:
    - "H4 弱支持（p=.104）当场不救：'bounded non-support' 直接报告，解释推迟到 Discussion（claim discipline）——克制本身是 falling action 的可信度动作"
    - "2SRI 内生性 + 样本选择检验（robustness-by-threat）"
    - "替代测量：两个 outcome family 各自换构面再验（按测量威胁分组而非附录清单）"
    - "探索性跨域测试：理论可行但未假设的关系，明确 label 为 exploratory"
  denouement: "Discussion：H4 弱支持的根因定位（其论证与 H3 高度重叠）；'服务得不一样'的统一图景收口——同一引擎、两种服务方式"
```

### stakes

```yaml
stakes:
  theoretical: "governance 与 social 两类 stakeholder strategy 被文献分域研究（各有驱动因素清单），心理动机视角从未统一——缺了 '同一个 CEO 为什么在两个域服务得不一样' 的解释"
  practical: "董事会/任命者的 CEO 选聘：promotion/prevention focus 会系统性地塑造企业在 governance 与 social 两类战略上的姿态（服务方式）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 直觉替代预测 1（T2 拒绝的第一个）— 读者会想当然的版本，被显式推翻"
  - "讲法B: 直觉替代预测 2（T2 拒绝的第二个）— 同上"
  - "讲法C: 单域故事 — 只做 governance 或只做 social 战略（分域文献的惯例；半张图）"
  - "本文: 跨域统一 — 2×2 对称映射（双系统 × 双域）。选择理由：与分域惯例正面碰撞（'服务得不一样'标题即承诺）；2×2 产生四格预测而非两域各一；ruling-out-alternatives 把读者的直觉变成剧情反转"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "无 Hook 冷启动——反向选择：不靠具体人面开场，靠文献张力（与 Pfarrer 2010 同型；模板里 human_face 在此篇是'战略缺席'而非缺陷；已核实 2026-08-09：P1 纯文献开场）"
  rhetorical_question: "未见（已核实 2026-08-09）"
  pacing_notes: "Theory 每个假设三理由平行（'Additionally... Finally...'）制造匀速推进的节奏；T2 立靶-推翻是唯一一次戏剧性变速；Results 四段模块化重复——Pollock 'Clarity' 原则：平行假设用重复不是冗余；falling action 的克制（弱支持不救）让全篇节奏收束而非补救"
  showing_telling: "未见图解性 showing（待补——2×2 映射以表格呈现）"
  voice: "we argue/we demonstrate 中性学术语态（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Malshe 2015（跨域故事家族）**：同是"跨域"故事，机制相反——Malshe = 半区空白（half-domain-gap，一个域的一半没人做）；本文 = 全域统一（cross-domain-unification，两个域共用一台引擎）。对照价值：跨域不只有"补空"一种讲法。
- **与 Zhao-Ding & Gaba（对称双轨家族）**：那篇是同一构念的对称反向双轨机制（X 的两面驱动相反方向）；本文是双构念 × 双域的正交 2×2——同形不同义，路由时不可混用。
- **与 Pfarrer 2010**：无 Hook 冷启动同型（另一篇 Incompleteness 冷启动原型）。
