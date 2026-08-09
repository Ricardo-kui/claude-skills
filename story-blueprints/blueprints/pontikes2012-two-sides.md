# Story Blueprint — Pontikes (2012) ASQ

## 文件头

```yaml
id: pontikes2012
paper: "Pontikes (2012, ASQ) — Two Sides of the Same Coin（software 行业 1990–2002）"
distilled_sections: [intro, theory, methods, results]
source_records: [project-mvp30-pontikes2012-two-sides]
corpus_links:
  write-introduction: "tensions/04-reality-contradicts-consensus 变体G（共识惩罚 vs 行为持续 + 修辞问 pivot）；变体E（双受众对立评价型）"
  write-theory: "hypothesis_derivation_patterns audience-role dichotomy（镜像 H1a/H2a）；two-stage complementary process reconciliation（temporal staging）"
  write-methods: "实证对象构建 变体5（label-ambiguity 从共属重叠构建：fuzziness + leniency；fuzzy-set grade of membership）"
  write-results: "跨受众构念对比 变体1（同一构念跨受众镜像相反效应 + 受众内反转）"
```

## Story

### one_liner

> 同一个标签（类别模糊），两类受众给出相反的判决：消费者市场把它当缺陷惩罚，风投市场把它当灵活性奖励。共识说"模糊该罚"，行为却说"模糊还在用"——谜底不在标签本身，而在看它的人；两类受众一个早期筛选、一个后期评估，时间上互补分工。

### knot

```yaml
knot:
  primary_type: irony-reversal
  compound_types: [consensus-puzzle]
  statement: "label ambiguity 对 consumer（market-taker）与 VC（market-maker）两类受众产生镜像相反评价——同一构念对两类受众有相反意义，不是'证据 mixed'"
  tied_at:
    - "Intro P1–P2：'A consensus is building'（模糊受惩罚，三情境加固）→ 'Despite this'（组织仍持续用模糊标签）→ 修辞问 'how does [this] come to be?' → 预告 'The answer may lie in different audiences'"
    - "Theory：audience-role dichotomy（同一构念的双重身份设定）+ 镜像假设 H1a/H2a"
  untied_at:
    - "Theory：two-stage reconciliation 首现（时间分工化解相反偏好）"
    - "Results：镜像系数揭晓（同一 IV，consumer 惩罚 / VC 奖励）"
    - "Results：受众内子群反转（corporate VC 符号回负）确证"
  antagonist: "学术共识本身——'单一受众'的共识（ambiguity 被惩罚）不是错的，而是只看了一面；共识的完整性就是反派，行为持续是它漏掉的破绽"
  antagonist_built_by:
    - "三情境加固：共识不是断言而是'堆积的证据'（惩罚在 3 个情境重复出现），加固越强，'行为持续'的张力越大"
    - "修辞问 pivot：'how does this come to be?' 把共识推下神坛——共识与行为冲突必然意味着共识不完整"
```

### characters

```yaml
characters:
  protagonist: [label ambiguity (X), 两类受众的评价 (Y)]
  supporting:
    - "audience 角色二分（market-taker / market-maker）：配角其实是'双面镜'，把主角照成两个相反的角色"
    - "corporate VC（受众内异质性，Results 的反转工具）"
  ensemble: [软件行业情境、标签共属网络、控制变量]
```

### resolution_logic

`revelation` 揭幕——**换视角**：不是修正测量、不是选边，而是展示"同一构念的第二张脸"。再加 `temporal staging`（VC 早期筛选模糊创新者、consumer 后期评估存活者）把"相反"重释为"互补"，irony 转化为分工。研究者是揭幕者：读者以为认识这个标签，其实只见过一面。

### five_acts

```yaml
five_acts:
  exposition: "Intro：共识惩罚（三情境）→ 行为持续 → 修辞问 pivot → 'answer may lie in different audiences'（knot 与解法方向同时预告）"
  rising_action: "Theory：audience-role dichotomy 设定两面；镜像假设 H1a/H2a 把张力结构化；two-stage reconciliation 首次化解；Methods：把'模糊'从共属网络结构测出来（fuzziness + leniency，fuzzy-set μ∈[0,1]）——arena 本身是'测量对象'"
  climax: "Results 主表：同一 IV 双独立模型镜像系数（consumer −101.5*** inverse rank vs VC +1.476*** funding；同图双线）——两行数字并置即全部故事"
  falling_action:
    - "受众内异质性反转：corporate VC 作 market-taker 符号反转回负 → 排除'受众身份混淆'的替代解释，镜像更硬"
    - "各受众分别经济显著性（不是只报符号）"
  denouement: "Discussion：two-stage 时间互补分工（早期筛选/后期评估）；回到开头修辞问——'how does this come to be?' 的答案是受众，不是标签"
```

### stakes

```yaml
stakes:
  theoretical: "类别理论/受众研究的核心争议：同一类别属性对不同受众是否同义？共识默认'惩罚'单面答案，忽略会让整个类别-评价理论对创新者行为失明"
  practical: "创新者为何坚持用模糊标签（行为持续的现象本身就是 stakes）；'分类清晰'是否总是策略美德——对谁而言？"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 单面惩罚故事 — '类别模糊损害市场评价，共识已确立'（共识版；也是本文要驳的版本）"
  - "讲法B: 无差异 null 故事 — '模糊对评价无系统影响'（gap-filling 版：更细测量再验一次）"
  - "讲法C: 悲剧/代价故事 — '模糊是创新者的困境：必须模糊以取悦 VC、必须清晰以取悦市场，两难'（irony 但导向冲突而非互补）"
  - "本文: 揭幕+互补版 — 同一标签两副面孔（镜像），再以时间分工把 irony 转成互补。选择理由：镜像发现（−/+ 并置）比任一单面结论信息量更大；two-stage 把'矛盾'转化为'分工'，使理论贡献从'发现反例'升为'重新解释结构'"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "软件行业具名标签作现象角色（2026-08-09 原文核实）：'document management'、'computer-aided design'、'enterprise software'、'data mining'、'e-business applications'——模糊标签本身是 actor（'行为持续'的具体形态）"
  rhetorical_question: "'how does an ambiguous classification structure like the software industry's come to be?' 是整篇的 pivot——把共识与行为的矛盾转成读者的好奇心；'The answer may lie in different audiences' 紧接给出悬念方向"
  pacing_notes: "intro 前半是慢速加固（三情境堆积共识），修辞问处急转（pivot），Theory 快速结构化（镜像假设），climax 即主表双线；falling action 短而硬（一个反转排除一类替代解释）"
  showing_telling: "同图双线（consumer/VC 两条相反斜率）=showing 核心；镜像系数并置（−101.5 vs +1.476）=telling 的表格化"
  voice: "Abstract 第一人称单数 I（'I suggest this depends on the audience'）+ 正文 we 混合（已核实 2026-08-09）"
```
