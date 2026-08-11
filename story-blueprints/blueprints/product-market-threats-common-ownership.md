# Story Blueprint — Kini, Lee & Shen (2024) Management Science

## 文件头

```yaml
id: product_market_threats
paper: "Kini, Lee & Shen (2024, MgmtSci) — Common Institutional Ownership and Product Market Threats"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（共同所有权/07 原文）→ ROBUST
source_records: [parsed full text（共同所有权/07 原文）]
vault_reports:
  intro: null（共同所有权文件夹原文回读）
  methods_results: null（全文回读：DiD——金融机构并购外生冲击、Hoberg-Phillips fluidity）
  story_arc: null
corpus_links:
  write-introduction: "market power vs efficiency 两假说（'This view, however, neglects the welfare-promoting externalities'——看漏效率面）+ fluidity 新维度——路径待验证"
```

## Story

### one_liner

> 共同所有权的市场力量假说（反竞争——quasi-monopoly 租金）主导关注——但"this view, however, neglects the welfare-promoting externalities"——本文用产品市场 fluidity（10-K 文本竞争指标）检验净效应：平均而言共同所有权**促进**产品市场动态（效率假说胜——知识溢出）——但在准垄断倾向的行业中抑制竞争——"一刀切"限制共同所有权的政策在强溢出行业有害。

### knot

```yaml
knot:
  primary_type: overlooked-alternative  # 第九原型：共同所有权效率面被看漏（'This view, however, neglects the welfare-promoting externalities'）
  compound_types: []                    # 两假说净效应是裁决，非子类型
  statement: "共同所有权的市场力量假说（反竞争——'quasi-monopoly rents'——主流：Azar et al.）vs 效率假说（知识溢出——
              'welfare-promoting externalities'——'This view, however, neglects...'——被看漏）——fluidity 新维度检验净效应：
              平均而言共同所有权→产品市场动态↑（效率胜——溢出环境）；准垄断倾向行业→竞争↓——'one-size-fits-all regulatory policy
              limiting common ownership may be harmful in industries with strong spillover opportunities'"
  tied_at:
    - "Intro：市场力量假说（'common owners may pursue anticompetitive strategies to achieve quasi-monopoly rents'）→ 'This view, however, neglects the welfare-promoting externalities'（看漏效率面）→ 两假说联合分析需要"
    - "Theory：两假说净效应（溢出的'rat race' vs 市场力量激励——countervailing forces）"
  untied_at:
    - "Theory H1-H3：共同所有权→fluidity + 行业异质性"
    - "Results：平均效率胜 + 准垄断行业抑制 + DiD 外生冲击"
  antagonist: "共同所有权的市场力量视角（'market power hypothesis'——Azar et al. 主流——效率面被 neglect）"
  antagonist_built_by:
    - "'This view, however, neglects the welfare-promoting externalities'（看漏声明——原文锚）"
    - "两假说排布（market power vs efficiency——countervailing forces——'a holistic view... can be achieved by studying strategic variables beyond price and quantity'）"
    - "fluidity 新维度（Hoberg-Phillips 10-K 文本竞争指标——'capture competitive risk or threats'——超越价格/数量的新战场）"
```

### characters

```yaml
characters:
  protagonist: [common ownership（X）, product market fluidity（DV——竞争/威胁）]
  supporting:
    - "效率假说机制（知识溢出——'rat race'——产品创新加速——'common owners... promote investments in technologies with strong spillover effects'）"
    - "市场力量假说机制（quasi-monopoly——'tacit collusion between cross-held competitors'）"
    - "行业异质性（溢出环境 vs 准垄断倾向——净效应的条件）"
    - "金融机构并购（外生冲击——DiD 识别）"
  ensemble: [美国上市公司、fluidity（Hoberg-Phillips 10-K 文本指标）、DiD（金融机构并购）、多共同所有权测量（MHHID/Cross/GGL）]
```

### resolution_logic

`revelation` 揭幕（揭幕共同所有权的效率面——fluidity 新维度 + 行业条件化——"净效应"地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：市场力量假说（'quasi-monopoly rents'——主流）→ 'This view, however, neglects the welfare-promoting externalities'（看漏效率面）→ 两假说联合分析需要 → fluidity 新维度引入"
  rising_action: "两假说净效应理论（溢出的'rat race' vs 市场力量激励——countervailing forces）+ Methods（fluidity 10-K 文本指标、DiD——金融机构并购外生冲击、多共同所有权测量）"
  climax: "Results——净效应揭晓：共同所有权→fluidity↑（'greater product market fluidity'——'spurs dynamism in product spaces rather than tacit collusion'——效率假说平均胜出）"
  falling_action:
    - "溢出环境条件（'especially true in economic environments in which it is easier to take advantage of knowledge spillovers'）"
    - "准垄断行业抑制（'common ownership can also inhibit product market competition and dynamism, especially in industries more prone to quasi-monopoly outcomes'——双面完整）"
    - "政策含义（'one-size-fits-all regulatory policy limiting common ownership may be harmful in industries with strong spillover opportunities'——政策地图）"
  denouement: "Discussion——共同所有权的净产品市场效应（市场力量与效率的联合分析——'a holistic view'）；
              政策异质性（一刀切限制的行业危害）；fluidity 作为竞争测量的新维度"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权效率面被看漏——'This view, however, neglects the welfare-promoting externalities'——价格/数量之外的新维度"
  practical: "监管政策（一刀切限制的行业危害——强溢出行业）；产品市场动态（创新/投资）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 市场力量版——共同所有权反竞争（Azar et al. 主流——markup 研究——'market power hypothesis'）"
  - "讲法B: 价格边际版——共同所有权与 markup（既有实证——'positive relation... can represent support for either hypothesis'——不可区分）"
  - "讲法C: 治理版——共同所有权治理效应（治理文献——不接产品市场竞争）"
  - "本文: 效率面揭幕版——fluidity 新维度（'neglects the welfare-promoting externalities'——净效应 + 行业条件化）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（fluidity 文本指标——10-K 描述变化）；'rat race'（溢出竞争意象——产品空间内的追逐）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "市场力量假说→'neglects' 声明→两假说→fluidity 引入→DiD；climax=效率胜出揭晓；falling action 双条件+政策地图"
  showing_telling: "'This view, however, neglects'（看漏声明——反转点）；'rat race'（溢出竞争意象）；'fluidity'（流动/动荡——竞争的新维度意象）；'vibrations'（产品空间震动——fluidity 定义）"
  voice: "MgmtSci 金融实证口吻；'neglects'（看漏强调）；'one-size-fits-all... may be harmful'（政策警示）"
```

### cross_paper_notes

- **overlooked-alternative 八原型（共同所有权效率面家族）**：desjardine2022/anton2025/**product_market_threats**——'This view, however, neglects'（原文锚）与 anton2025 的 'much less work' 同款——共同所有权亮面/效率面家族三篇（CSR/创新/竞争）。
- **共同所有权家族七篇成型**。
- **与 anton2025 的对照**：anton（创新投入/产出——溢出促进创新）；PMT（产品市场竞争——fluidity——溢出促进竞争）——溢出的双后果（创新/竞争）。
- **判别器记录**：overlooked-alternative 判定基于效率面被看漏（'neglects the welfare-promoting externalities'——原文锚）。
