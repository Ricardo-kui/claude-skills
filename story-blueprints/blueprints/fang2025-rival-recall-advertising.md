# Story Blueprint — Fang, Astvansh, Tong, Lee & Guo (2025) POM

## 文件头

```yaml
id: fang2025
paper: "Fang, Astvansh, Tong, Lee & Guo (2025, POM) — How Do Brands Change Their Advertising Spending in Response to a Rival's Product Recall?"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：62 替代车型/31 周/308 地区、RDiT）
  story_arc: null
corpus_links:
  write-introduction: "机会/威胁双重解读（'opportunity to preempt sales... Conversely, they may interpret the recall as a threat'）+ Samsung 具名案例——路径待验证"
  write-methods: "RDiT（回归断点时间）+ 广告类型分解（price/quality/brand）——路径待验证"
  write-results: "威胁主导（−50%）+ 价格广告 +25%/质量广告 −71%——路径待验证"
```

## Story

### one_liner

> 直觉与媒体报道说召回是对手的机会（Samsung Note 7 后其他厂商 fierce advertising）——但实证显示**威胁解读主导**：替代品牌总体广告支出 −50%；细粒度分解暴露策略：价格广告 +25%（销售抢占）、质量广告 −71%（避免不利比较）、品牌广告不变；而降低广告是明智之举——召回提升替代品销量 +35.3%，广告支出反而削弱该溢出（比较效应）。

### knot

```yaml
knot:
  primary_type: consensus-puzzle         # 第六原型："召回=对手机会"共识 vs 威胁主导现实——广告类型条件（与 shipilov2020 同构的通俗共识翻转）
  compound_types: []                    # 机会/威胁双重解读是结构，非子类型
  statement: "共识——召回是对手的机会（媒体叙事：Samsung Note 7 后'other phone makers started advertising fiercely'；
              Toyota 召回后 GM 巨额激励）；实证——威胁解读主导：替代品牌总体广告 −50%（避免不利比较）；
              但细粒度暴露局部机会：价格广告 +25%（销售抢占）、质量广告 −71%、品牌广告不变——机会/威胁并存于广告类型"
  tied_at:
    - "Intro：Samsung Note 7（2016——其他厂商 fierce advertising——机会共识）+ Toyota 加速踏板（2010——GM 激励——'Ironically, some of GM's brands... used the same accelerator pedal'）→ 机会/威胁双重解读"
    - "Theory：三种响应策略（销售抢占→价格广告/回避→品牌广告/质量信号→质量广告）"
  untied_at:
    - "Theory H1-H3：三广告类型调整"
    - "Results：总体 −50% + 价格 +25%/质量 −71%/品牌不变"
  antagonist: "'召回=对手机会'的共识（媒体叙事——Samsung 案例——趁机抢市场的直觉）"
  antagonist_built_by:
    - "Samsung Note 7 案例（'other phone makers started advertising fiercely to seize Samsung's loss of sales'——机会共识的媒体叙事）"
    - "GM 激励的 irony（'some of GM's brands that were heavily advertised... used the same accelerator pedal that Toyota used'——机会策略的隐患）"
    - "机会/威胁双重解读排布（'A brand manager can interpret... as an opportunity... Conversely, they may interpret... as a threat'）"
```

### characters

```yaml
characters:
  protagonist: [rival's recall（X——Sagitar 召回）, substitute brand's ad spending（DV——总体 + 三类型分解）]
  supporting:
    - "威胁解读（主导——避免不利比较——'unfavorable comparisons between their brand and the recalling brand'）"
    - "机会解读（局部——销售抢占——价格广告 +25%）"
    - "广告类型分解（price +25%/quality −71%/brand 不变——细粒度策略）"
    - "positive spillover（召回提升替代品销量 +35.3%——广告削弱之 −23.1%/单位）"
  ensemble: [62 替代车型/31 周/308 地区/591,976 obs、RDiT、Sagitar 召回、Samsung/Toyota/GM 具名案例]
```

### resolution_logic

`revelation` 揭幕（揭幕威胁解读的主导地位 + 广告类型的局部机会——细粒度策略地图 + 溢出机制的明智降广告）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Samsung Note 7（其他厂商 fierce advertising——机会共识）→ Toyota 召回（GM 激励——'Ironically... used the same accelerator pedal'）→ 机会/威胁双重解读"
  rising_action: "三种响应策略理论（抢占→价格广告/回避→品牌广告/信号→质量广告）+ Methods（62 替代车型/31 周/308 地区、RDiT、广告类型分解）"
  climax: "Results——威胁主导揭晓：替代品牌总体广告 −50%（'threat interpretation dominates the opportunity interpretation'——机会共识被翻）"
  falling_action:
    - "细粒度策略揭晓（价格广告 +25%——销售抢占；质量广告 −71%——避免不利比较；品牌广告不变——无品牌回避）"
    - "溢出机制（召回提升替代品销量 +35.3%——广告削弱该溢出 −23.1%/单位——'by lowering its total ad spending, a substitute brand prevents unfavorable comparisons'——降广告是明智之举）"
    - "异质性（直接替代品更视威胁——降低价格/质量广告可见度；同制造商替代品 guilty by association——加大质量广告）"
    - "稳健性五重 + 复制（另一召回事件）"
  denouement: "Discussion——威胁解读的主导（召回不是对手的机会而是比较陷阱）；广告类型作为策略信号（'the substitute's strategy can be discerned through the type of its advertising creatives'）；
              溢出机制的竞争含义（降广告获利的反直觉）"
```

### stakes

```yaml
stakes:
  theoretical: "'召回=对手机会'共识未检验——机会/威胁双重解读的实证缺失；广告类型作为竞争策略信号"
  practical: "替代品牌的广告决策（威胁解读主导——降广告获利）；质量感知管理（避免不利比较）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 机会共识版——召回=对手机会（媒体叙事——Samsung 后 fierce advertising——趁机抢市场）"
  - "讲法B: 传染威胁版——召回传染对手（水平传染——Zavyalova/Borah & Tellis——负面视角）"
  - "讲法C: 制造商策略版——召回企业的回应（recall 企业自身——Chen et al. 策略——非替代品）"
  - "本文: 威胁主导揭幕版——总体 −50% + 广告类型细粒度（'threat dominates' + 价格/质量/品牌分解 + 降广告获利）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Samsung Galaxy Note 7（2016——其他厂商 fierce advertising——机会共识的具名案例）；Toyota 加速踏板（2010——GM 激励——'Ironically, some of GM's brands... used the same accelerator pedal that Toyota used'——irony 细节）；Sagitar 召回（主分析情境）"
  rhetorical_question: "标题即问句（'How Do Brands Change Their Advertising Spending...?'——标题问句家族第 6 例——'How' 型问句——新变体）"
  pacing_notes: "Samsung 机会共识→GM irony→双重解读→三策略理论；climax=威胁主导揭晓（−50%——机会共识被翻）；falling action 三类型+溢出机制+异质性+复制"
  showing_telling: "'Ironically'（GM 同踏板 irony——机会策略的隐患细节）；广告类型分解（策略的细粒度信号）；'unfavorable comparisons'（比较陷阱意象）"
  voice: "POM 实证口吻；'Ironically'（irony 标记）；'pay off'（策略回报——'suppressing total ad spending pays off'）"
```

### cross_paper_notes

- **consensus-puzzle 六原型（机会/威胁共识条件化）**：pontikes/cutolo/gamache/kundro/han2020/**fang2025**——"召回=对手机会"共识被威胁主导部分翻转 + 广告类型条件。
- **recall 现象域十六讲法**（对手反应维度 +1——竞争侧）。
- **与 pupovac2025 的 Astvansh 系连接**（共同作者——recall 传染/竞争家族网络）。
- **与 shipilov2020 的对照（信号解读共识翻转家族）**：shipilov（正面报道也驱动——负面偏好翻转）；fang（机会共识被威胁主导翻转——机会偏好翻转）。
- **标题问句家族第 6 例**（'How' 型问句——新变体）。
- **判别器记录**：consensus-puzzle 判定基于"召回=对手机会"强共识（媒体叙事——Samsung 案例）vs 威胁主导证据 + 广告类型条件（被忽略的异质性）。
