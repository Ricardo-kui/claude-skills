# Story Blueprint — Toh & Pyun (2023) SMJ

## 文件头

```yaml
id: toh2023
paper: "Toh & Pyun (2023, SMJ) — Risky Business: How Standardization as Coordination Tool in Ecosystems Impacts Firm-Level Uncertainty"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [project_mvp30_toh_pyun_smj, vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/toh2023_risky_business_standardization_smj_narrative.md + fine_grained/batch_2026-05-26/toh_pyun_smj_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-05-26/toh_pyun_smj_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/toh2023_risky_business_methods_narrative.md + results/toh2023_risky_business_results_narrative.md + deep_distillation/papers/toh2023_..._deep_profile.md + fine_grained/batch_06_darby2024_toh2023/toh2023_risky_business_fine_methods_results.md"
  story_arc: null
corpus_links:
  write-introduction: "Rhetorical Question Tension pivot（firm-level? 层次跳跃问句）——路径待验证；_evidence_registry.yaml（toh 条目）"
  write-theory: "corpus/sentences/mechanism_chain.md、construct_definition.md、hypothesis_forms.md、closure.md（假设树型 Y-shaped：common trunk → H1/H2 双路径 → H3-H5 分支）"
  write-methods: "隐含波动率测量（stock option implied volatility）——路径待验证"
  write-results: "路径待验证"
```

## Story

### one_liner

> 标准化被当作生态系统的协调解药（降低协调不确定性），但企业层面看它把企业劈成两类：标准所有者更安稳（隐含波动率 ↓3.2%），非所有者反而更不确定（↑18%）——同一把工具，两面不同的刀；非所有者的风险还取决于强对手与自身互补资产。

### knot

```yaml
knot:
  primary_type: irony-reversal   # 第三原型（pontikes2012 受众分裂 / desjardine2023 反果 / 本文类别分裂）
  compound_types: [consensus-puzzle]   # 共识"标准化降低不确定性"只在平均层面成立（Model 1 验证）——被无条件化
  statement: "文献共识——标准化降低生态系统协调不确定性（'The hope is that...'）；但企业层面看，同一工具对两类主体相反：标准所有者不确定性下降、非所有者上升——第三类不确定性（价值攫取）被文献忽略"
  tied_at:
    - "Intro P2-P3：共识建立 → 层次跳跃修辞问（'does it necessarily reduce uncertainty at the firm-level?'）"
    - "Intro P4：异质性论点（standard-owner vs non-standard-owner）"
  untied_at:
    - "Theory H1/H2：双路径镜像预测"
    - "Results Model 2：−3.2% vs +18% 镜像兑现；H3-H5 条件化"
  antagonist: "文献共识——标准化=协调解药的无条件化预期（ecosystem-level 镜头遮蔽 firm-level）"
  antagonist_built_by:
    - "'Past research suggests... The hope is that...' 温和共识建立"
    - "层次跳跃修辞问（However, even as... does it necessarily...）"
    - "双重强调缺口（'As far as we know, this crucial issue has not been examined'）"
```

### characters

```yaml
characters:
  protagonist: [standardization（X——SEP 披露：own/non-own 双暴露）, firm-level uncertainty（DV——隐含波动率）]
  supporting:
    - "standard-owner vs non-standard-owner（irony 的分裂面）"
    - "strong rivals（H3——互补区强敌加重非所有者风险）"
    - "complementary technologies（H4——互补技术缓冲）"
    - "production assets（H5——生产资产缓冲）"
    - "value-appropriation uncertainty（第三类不确定性——被忽略的维度）"
  ensemble: [SSO 标准制定、ICT 生态系统 1996-2010、股票期权隐含波动率、IBM/Nokia/Sony（具名案例）]
```

### resolution_logic

`revelation` 揭幕（换镜头——从 ecosystem-level 镜头切到 firm-level 镜头，展示同一工具的镜像效应）+ 条件化（谁最受伤：强敌环伺、互补资产薄弱者）。研究者是镜头切换师：先给平均效应特写，再切近景露出分裂。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：协调挑战→共识（标准化缓解协调不确定性）→层次跳跃修辞问（firm-level?）→第三类不确定性（价值攫取）引入"
  rising_action: "Intro P4-P6（异质性论点+5 假设预览+贡献）+ Theory（2.1-2.4：ecosystem→firm 层级递进、所有者/非所有者双机制链）+ Methods（SSO 数据、SEP 披露测量、隐含波动率 DV、RE 模型）"
  climax: "Results Model 2——镜像揭晓：Standards Own 降低不确定性（t=−2.40, p=.017，全模型 −0.032/↓3.2%）vs Standards Non-Own 升高不确定性（t=1.99→2.93，↑18%）——Model 1 平均效应（t=−1.99）被劈成两半"
  falling_action:
    - "H3-H5 条件化：强对手加重（1.747, t=2.64）/ 互补技术缓冲（−0.988, t=−2.92）/ 生产资产缓冲（−0.080, t=−3.40）——谁更受伤的完整地图"
    - "具名案例（showing）：IBM 2004 无线通信标准轮（无 SEP 但 44% 数据互补专利——波动率 36.7→19.8%）、Nokia 1999（388 vs 21 互补专利——48.5→45.4%）、Sony 2005（PPE $31.6B vs $11B——29.6→20.3%）——'绕开价值攫取的非常规者'"
    - "稳健性：robust SE / Swamy-Arora / AR(1) + H3-H5 分样本（H4 略弱）+ 8 项附加分析（测量比较、选择问题、替代解释排除）"
  denouement: "Discussion——回到开头：'standardization... creates uncertainty for other non-standard-owner firms'；层别分离呼吁（ecosystem ≠ firm 不确定性不重合）；标准化从协调工具重读为价值攫取战略工具；'generative growth' 担忧收口（不确定性排除小专业厂商——民主生态增长的反向风险）"
```

### stakes

```yaml
stakes:
  theoretical: "协调类不确定性被充分研究，价值攫取类（第三形式）被忽略——层别分离（ecosystem/firm）是领域盲区"
  practical: "非标准所有者（尤其小专业厂商）参与生态的意愿被不确定性抑制——'democratic and inclusive' 生态增长面临反向风险"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 平均效应版——标准化降低不确定性（文献共识；Model 1 确实成立——但掩盖分裂）"
  - "讲法B: 所有者视角版——标准所有者的价值攫取优势（Miller & Toh 2022 已做——本文明确 depart）"
  - "讲法C: 协调成本版——生态治理机制比较（合同 vs 层级 vs 标准——协调文献主流）"
  - "本文: 类别分裂镜像版——同一工具对 owner/non-owner 相反效应 + 第三类不确定性概念创新——选择理由：平均效应掩盖分裂；做第二序效应（不确定性）而非第一序（价值捕获）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "IBM/Nokia/Sony 具名案例（Results 4.3 末——'绕开价值攫取的非常规者'三连：波动率具体轨迹 36.7→19.8%、48.5→45.4%、29.6→20.3%）"
  rhetorical_question: "Intro P3 层次跳跃修辞问（'does it necessarily reduce uncertainty at the firm-level?'——Tension pivot）；Discussion 收口反问（'Does this lead to the exclusion of smaller, specialist-firms...?'——generative growth 担忧）"
  pacing_notes: "8 段紧凑 Intro（共识→转折→概念创新→预览）；Theory 层级递进（ecosystem→firm）；climax=Model 2 镜像并置；falling action 具名案例作'反面证明'插曲"
  showing_telling: "镜像数字并置（−3.2% vs +18%）；'The hope is that'（期望与现实的落差暗示）；具名企业波动率轨迹作 showing"
  voice: "主动语态；克制谦逊（'We do not claim to have studied this here'——战略意图讨论的自限）"
```

### cross_paper_notes

- **irony-reversal 三原型**：pontikes2012（同一构念两受众相反——受众分裂）↔ desjardine2023（监督反果——行动反果）↔ toh2023（标准化对两类企业相反——类别分裂）——"同一 X 劈开两类 Y"三种形态。
- **与 pontikes2012 同 compound（+consensus-puzzle）**：共识只在平均层面成立（toh Model 1 / pontikes 单面惩罚）——"平均效应掩盖分裂"家族。
- **与 wu2025 对照（外部工具家族）**：wu2025 制度冲击改变行为（DiD）、toh2023 协调工具改变不确定性分配——同一"外部工具"两种故事。
- **层次跳跃叙述引擎**：toh2023 修辞问（firm-level?）与 singh2023 Should-be-Yet 同属"镜头移动"族。
