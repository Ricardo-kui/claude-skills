# Story Blueprint — Shipilov, Greve & Rowley (2020) SMJ

## 文件头

```yaml
id: shipilov2020
paper: "Shipilov, Greve & Rowley (2020, SMJ) — Is All Publicity Good Publicity? The Impact of Direct and Indirect Media Pressure on the Adoption of Governance Practices"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/shipilov2020_publicity_good_smj_narrative.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/shipilov2020_publicity_good_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_09_gamache2020_shipilov2020/...（四报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "标题俗语问句 Hook（Is all publicity good publicity?）——路径待验证"
  write-methods: "DiD 三向交互 + CEM 匹配 + 条件数控制——路径待验证"
  write-results: "被拒假设的反直觉报告（H1b/H2b 正面同样驱动）——路径待验证"
```

## Story

### one_liner

> 媒体压力文献默认"只有负面报道才推动企业变革"（正面报道让企业安于现状），本文用加拿大金融危机 DiD 证明：正负面报道同样驱动治理改革——负面是批评应对，正面是议程认同（fad）；效应还通过董事网络间接传播——"Is all publicity good publicity?" 答案是：是的，只要报道带着情绪。

### knot

```yaml
knot:
  primary_type: assumption-flip        # 第二原型（valence 单边假设家族——负面偏好前提翻转）
  compound_types: [consensus-puzzle]   # 文献预测"正面→抵制"被证据证伪（延伸预测被拒）
  statement: "媒体-行动文献共识——企业厌恶治理变革，只在负面报道压力下改变、正面报道下抵制（'resist changes when
              coverage is positive'）；但数据显示正面报道同样（甚至更强）驱动采纳——情绪化报道（不论正负）都有
              议程设置效应，且通过董事网络扩散"
  tied_at:
    - "标题（Is all publicity good publicity?——俗语问句即 knot）"
    - "Intro P2：核心矛盾（replicate-then-flip 预告——'While we follow the same logic... we find the opposite effects'）"
  untied_at:
    - "Theory H1b/H2b：延伸预测（正面→抵制——自设立靶）"
    - "Results Model 6-9/15-18：正面报道→采纳（被拒假设的反直觉兑现）"
  antagonist: "媒体-行动文献的负面偏好共识（Baumeister 负面偏差——只有负面才推动变革）"
  antagonist_built_by:
    - "标题俗语问句（直接挑战日常共识）"
    - "'While we follow the same logic... and replicate... we find the opposite effects'（先复现后翻转）"
    - "自设 H1b/H2b 立靶（延伸预测被现实拒绝）"
```

### characters

```yaml
characters:
  protagonist: [media coverage（X——own/interlock × positive/negative 四流）, board reform adoption（DV）]
  supporting:
    - "direct vs indirect coverage（直接报道 vs 董事网络间接报道——双通道）"
    - "financial crisis 2007-08（外生冲击——DiD 识别）"
    - "board interlocks（扩散管道——problem 与 solution 同时扩散）"
    - "fad/agenda-setting（新机制——正面报道的驱动逻辑）"
  ensemble: [TSX 加拿大上市公司、78 匹配公司/16 处理、CEM 匹配、subprime crisis]
```

### resolution_logic

`revelation` 揭幕（replicate-then-flip——先复现负面效应，再翻出"正面同样有效"的第二张脸 + 网络间接通道）——不推翻负面效应，揭示"情绪化议程设置"的补充机制（负面=批评应对、正面=议程认同）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：多利益相关者背景 → 核心矛盾预告（负面驱动已知；正面也驱动——反直觉）"
  rising_action: "Intro P3-P5（网络视角缺口 + DiD 识别 + 理论解释预览）+ Theory（1.1-1.2 直接/间接覆盖机制）+ Methods（TSX 面板、CEM、DiD 三向交互、2007/2008 年度分解）"
  climax: "Results Model 2/3——H1a 支持（负面自有报道→采纳：β=3.55, p=.002 [2007]；2.66, p=.036 [2008]）；
           Model 6/7——H1b 被拒（正面自有报道同样→采纳：β=1.46, p=.002 [2008]）——反直觉揭晓：
           'the stronger is the positive coverage, the more likely is the firm to adopt'"
  falling_action:
    - "H2a 支持（负面间接报道→采纳：1.72, p=.03；1.87, p=.005——董事网络传播）"
    - "H2b 被拒（正面间接报道也→采纳：0.36, p=.02；0.56, p=.00——fad 经网络扩散）"
    - "post hoc 语气差分析（tone 正差值→采纳：1.69, p=.002 [2008]——正面压倒负面时更强）——Baumeister 负面偏差被反转"
    - "稳健性：clogit FE + 条件数控制 + 附录内生性检验"
  denouement: "Discussion——回到开头：'Is all publicity good publicity?' 的答案——'media is influential whenever
               it expresses an emotionally laden viewpoint'（情感化报道即影响——中性报道无效；范围限定：principal-agent 议题）；
               双机制收口（负面=批评应对、正面=议程认同/fad）；扩散研究升级（practice 扩散→problem/discussion
               扩散的两步过程——记者影响一个董事会、董事带进另一个）；制度理论含义（媒体压力必须情绪化+定向）"
```

### stakes

```yaml
stakes:
  theoretical: "媒体影响机制被窄化为'负面批评驱动'——议程设置/情感化报道被忽视；扩散研究只做了 solution 扩散未做 problem 扩散"
  practical: "董事会改革采纳的触发机制；利益相关者/媒体如何有效施压（必须情绪化+定向——中性报道无效）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 负面驱动版——只有负面报道推动变革（媒体-行动文献主流；Baumeister 负面偏差）"
  - "讲法B: 单企业视角版——只做企业自身报道的影响（忽略网络间接通道）"
  - "讲法C: 制度压力清单版——把媒体作为众多制度压力之一（制度理论传统——换框架无增量）"
  - "本文: 正负面同效+网络扩散版——replicate-then-flip（先复现负面，翻出正面）+ 双通道；标题俗语问句作 knot 载体"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（TSX 78 公司——加拿大经济支柱企业集体角色）；金融危机外生冲击作场景"
  rhetorical_question: "标题即修辞问（'Is all publicity good publicity?'——俗语挑战——全文 knot 的载体）"
  pacing_notes: "replicate-then-flip 节奏（先 H1a/H2a 复现预期，再 H1b/H2b 翻出反直觉）；DiD 年度分解分年精确报告
                 （负面自有效应 2007 更强 [3.55 vs 2.66]、正面/间接效应 2008 更强——原文总结差异 2008 更显著）；
                 falling action 从被拒假设转出新机制（fad）"
  showing_telling: "标题俗语问句（呼应 'no such thing as bad publicity'——与 pfarrer2010 Discussion 打破同一俗语对照）；
                    图 1/2/3 边际效应图（正负面斜率对比）"
  voice: "主动语态；'While we follow the same logic... we find the opposite effects'（诚实复现-翻转口吻）"
```

### cross_paper_notes

- **valence 单边假设翻转家族（assumption-flip 第二原型）**：paruchuri2020（负面事件→正面溢出——效价方向反转）↔ shipilov2020（正面报道也有效——负面偏好反转）——"极性单边假设"的两种挑战。
- **与 pfarrer2010 俗语对照对**：pfarrer Discussion 打破 'no such thing as bad publicity'（visibility 无益）；shipilov 标题问 'Is all publicity good publicity?' 并答"是"——同一俗语空间的两端。
- **cross-domain-unification 观察排除记录**：shipilov2020 曾被列为观察候选（Synthesized 综合对话），判定为 valence 单边假设挑战而非跨域统一——排除在案，继续观察。
- **识别策略家族 +1**：DiD + CEM（shipilov2020）与 wu2025（制度冲击 DiD）对照——同设计不同故事。
- **判别器记录**：assumption-flip 判定基于贡献维度=机制（议程设置——Mechanism）；文献"正面→抵制"预测被证伪的 consensus-puzzle 形态归 compound。
