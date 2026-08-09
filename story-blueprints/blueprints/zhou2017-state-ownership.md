# Story Blueprint — Zhou, Gao & Zhao (2017) ASQ

## 文件头

```yaml
id: zhou2017
paper: "Zhou, Gao & Zhao (2017, ASQ) — State Ownership and Firm Innovation in China: An Integrated View of Institutional and Efficiency Logics"
distilled_sections: [intro, theory, methods, results]
source_records: [project-mvp30-zhou2017-state-ownership]
corpus_links:
  write-introduction: "literature-turns/03-non-coherence 变体A（双层 non-coherence 完整架构）；tensions/04-reality-contradicts-consensus 变体F（宏观事实反证）"
  write-theory: "hypothesis_derivation_patterns dual-logic integration（H1a+H1b→H1c 倒U）；moderator-as-remedy 扩展（H3 竞争 / H4 start-up）"
  write-methods: "IV-2SLS 变体10（地理外生性 IV）；多研究 变体7（facet-DV 双研究复制）；非线性模型 变体11（Tobit corner-solution）"
  write-results: "多研究 变体6（双研究收敛+发散+样本解释）；三向交互 变体3（线收敛=差距消除器）"
```

## Story

### one_liner

> 两套互相打架的理论（制度逻辑说国有产权给资源所以促进创新，效率逻辑说双重代理所以抑制创新），各有实证支持、各持一半真相；把"创新"拆成资源获取与资源利用两个层面后，谁都不是全错——整合出倒 U。

### knot

```yaml
knot:
  primary_type: paradigms-at-war
  compound_types: [counterevidence]
  statement: "state ownership → firm innovation 到底是促进还是抑制？institutional logic 与 efficiency logic 对同一关系推出相反预测，实证三方向（正/负/null）各有人支持"
  tied_at:
    - "Intro literature turn：双层 non-coherence（①理论层对立 + ②实证层三方向 mixed，各引具体研究）"
    - "Intro ③：dying-dinosaurs→dynamic-dynamos 现实反证（理论预测 vs 宏观量化事实，Fortune Global 500 统计）"
    - "Theory：H1a（输入逻辑）+ H1b（效率逻辑）平行建立"
  untied_at:
    - "Theory：H1c 倒U（facet 整合首现解法）"
    - "Results：双研究主结果（倒U 收敛）"
    - "Results：三向交互线收敛（竞争关闭 SOE/非 SOE 效率差）"
  antagonist: "文献内两派理论——各持一个 facet 且互不兼容，谁都不能全对"
  antagonist_built_by:
    - "双层 non-coherence 排布：理论对立 → 实证 mixed → 宏观反证，三级递进把'冲突'升级为'必须裁决'"
    - "反证用聚合事实而非个别研究（区别变体A/B），让冲突带上现实性 stakes"
```

### characters

```yaml
characters:
  protagonist: [state ownership (X), firm innovation (Y)]
  supporting:
    - "竞争强度（H3）：外部治理 monitor，作 H1b 低效机制的'解药'"
    - "start-up（H4）：生存压力纪律，同上"
  ensemble: [控制变量、制度情境、行业与年份]
```

### resolution_logic

`arbitration` 仲裁——**facet-decomposition**：两个逻辑各管一个 facet（institutional→资源获取 / efficiency→资源利用），分解后再整合出非单调（倒U）。研究者是"拆地测绘的仲裁者"，不是选边者。

### five_acts

```yaml
five_acts:
  exposition: "Intro：国有产权创新之争背景；两派逻辑与三方向 mixed 证据登台；宏观反证把冲突钉死；facade 预告解法"
  rising_action: "Theory：H1a 输入逻辑 + H1b 效率逻辑平行建立张力 → H1c 倒U（整合首现）；H3/H4 moderator-as-remedy 蓄积条件化；Methods：双研究 arena（Tobit 新产品比率 / Poisson 专利）、地理 IV 处理内生性"
  climax: "Results 开头：倒U 主结果揭晓（H1b/H1c/H3 双研究收敛）"
  falling_action:
    - "H1a/H2 在 Study 2（上市企业）发散 → 发散即 study-level 边界发现（不是失败）"
    - "三向交互'线收敛'图解：高竞争下 SOE 与非 SOE 效率差收敛（gap closer）"
    - "稳健性/替代测量（按 Results 分工惯例）"
  denouement: "Discussion：两逻辑各管一 facet 的整合视角收口；回归开头'谁对'之争——都对一半；政策含义（何时国有产权有益创新）"
```

### stakes

```yaml
stakes:
  theoretical: "两套成熟逻辑（制度/效率）对同一关系给出相反预测且各有证据——不解决则文献无法回答'state ownership 到底怎么影响创新'，更无法指导理论综合"
  practical: "国企改革与创新政策的直接分歧（中国情境）；'什么时候国有产权促进创新'是政策制定者的真问题"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: efficiency-only 负面故事 — '双重代理下国有产权必然损害创新'（效率派文献的讲法；prediction=负）"
  - "讲法B: institutional-only 正面故事 — '国有产权解锁 R&D 资源，促进创新'（制度派文献的讲法；prediction=正）"
  - "讲法C: mixed-evidence 折中 — '文献结果不一致，我们再用更好的数据测一次'（gap-filling 版，无理论整合）"
  - "本文: 仲裁整合版 — 两派不是谁对谁错而是各管一个 facet，分解后整合出倒U。选择理由：与 mixed 证据相容（每派在其 facet 内成立）、产生非单调新预测、回避'选边'的不可裁决性"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "宏观聚合事实作'现实'角色（2026-08-09 原文核实）：China 106 家公司入 2015 Fortune Global 500——2006 的 4 倍、约 2/3 是 SOE（dying dinosaurs→dynamic dynamos 反证的具体数字）；无个别 actor（有意选择：反证用宏观事实而非个案）"
  rhetorical_question: "未见（已核实 2026-08-09：intro 无问句）"
  pacing_notes: "双研究序列制造两轮 rising/falling 起伏（Pollock 多研究节奏）：Study 1 commercial（Tobit）→ Study 2 fundamental（Poisson），核心收敛、边缘发散；climax 落在首轮主结果，发散与线收敛作 falling action 的反转与收口"
  showing_telling: "三向交互'线收敛'图解（showing：两条线在竞争高处汇合=差距被关闭）；倒U 图形化预测"
  voice: "we theorize/we propose 中性学术语态（已核实 2026-08-09）"
```
