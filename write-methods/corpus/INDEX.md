---
corpus: write-methods
description: Methods 填空骨架变体库，按设计类型组织。由 distill-methods-exemplar 手动写入验证通过的变体。
organization: by_design_type
design_types_count: 24
created: 2026-05-18
updated: 2026-08-23
---

# Methods Econometric Models Corpus

## 组织逻辑

按模型设计类型组织。每个文件包含：
1. **主骨架引用** — 指向 `references/slot-M*.md` 中对应设计类型的变体（按需加载规则见 `write-methods/SKILL.md` → 槽位骨架加载）
2. **累积变体** — 由 `distill-methods-exemplar` Phase 4 自动写入的验证通过变体

另：`micro-templates/` 子目录为 18 类句法级微模板（槽位映射与使用协议见其 `INDEX.md`），由 `write-methods` 在表达润色时按需选读。

## 选择优先（变体速查表）

> 每个设计类型文件顶部现已有「变体速查表」（2026-08-08 推广）：按槽位（M1–M10）分组 + 六列表（变体 | 适用场景 | 区别 | 状态 | 来源），是类型内变体选择的唯一入口。
> **状态词表（三档，2026-08-29 用户裁决统一，与 _evidence_registry.yaml 一致）**：ROBUST（≥5 论文跨子领域复现）> VERIFIED（≥3 论文复现，或用户专家审计单源）> EMERGING（1–2 论文单源/双源；原「可选变体」统一记作 EMERGING（可选））。LEGACY-DIAGNOSTIC 保留（工具诊断类）。召回/产品伤害危机主题论文（Darby 2023–2026、Mayo/Ball/Mills 2022 POMS、Ball 2018、Wowak 2020/2021 M&SOM、Wowak 2025 MS、Li/Bapuji 2025/2026 JSCM、Chen/Ganesan/Liu 2009 JM、Kashmiri 2017 JAMS、Liu & Shankar、Bendig、Hoffmann、Malik 2025 JOM、Eilert 2017 JM，及其他来源文本含 recall/召回/product-harm 的论文）的全部蒸馏成果，按用户 2026-08-29 裁决记单源 VERIFIED。旧五档状态词已废弃，速查表/legend/状态字段不再使用；下方 dated changelog 保留历史原词，不改写。
> 检索流程：SKILL 路由确定设计类型 → 打开类型文件读速查表 → 按槽位+状态定位候选 → 精读变体正文（骨架/诚实边界/跨 skill 对齐）。

## 设计类型索引

| 文件 | 设计类型 | 变体数 | 最后更新 |
|------|---------|--------|---------|
| [面板数据-OLS](面板数据-OLS.md) | 面板数据-OLS | 44 | 2026-08-13；变体 51：M1 制度冲击型三重理由 setting 论证（变异源/降噪/利害分工），ball_2018，gap HIGH；变体 52：M3 构念边界排除（排除替代结果类别+falsification DV 预告），ball_2018，gap HIGH；变体 53：M3/M5 severity-split DV 配对假设（无交互项调节实现），ball_2018，gap HIGH；变体 54：M2 lead-DV 滞后对齐+理论驱动双理由排除，ball_2018，gap HIGH；变体 55：M4 新颖测量 provenance 链（缺口→补全→能力声明），ball_2018，gap HIGH；变体 56：M1 监管在场但裁量权在厂商的设置辩护（wowak2020；变体 57：M2 同一现象双边际分渠道取数 + 多库交集报最终 N（wowak2020）；变体 58：M3 DV 观察窗对齐治理决策钟（wowak2020）；变体 59：M3/M7 证据架构服从决策拆分 — DV 按严重度分组 + 假设→符号方向预登记（wowak2020）；变体 60：M2.5 预测变量组内变异预展示为 FE 设计发证（wowak2020）；变体 61：M7 FE 去均值选择 + 时不变因素按设计吸收 + 组内系数解读协议（wowak2020）；变体 62：M6 求而不得的控制变量 — 因变异不足主动弃用并声明（wowak2020）；变体 63：二分交互四格哑变量拆分（乘积项不可用宣告 + base case 逻辑 + 判定标准前置），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 64：风险集排他型控制剔除（定义性互斥指标的反向剔除 + 风险集 because 从句），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 65：时间括弧控制+反向相关保守性声明（t/t+1/t–t+1 三窗封同期解释 + 控制负相关=偏误不利于假设），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 66：先前状态构念 PCA 合成控制（eigenvalue+scree 双判据 + cf. 惯例清单 + 分量分别入模稳健），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 67：完备性准则漏斗+总体代表性 t 检验（统一完备准则导出 N + 对未入样总体的双维 t 检验），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 68：M2 排除阈值双向代价论证 + 放宽阈值补充分析回环（含入→噪声偏差 / 排除→失样本，再用放宽阈值补充分析闭合），anand_mukherjee_2024；变体 69：M7 三步渐进模型设定叙事（Step1 控制→Step2 非假设的复制步→Step3 交互），把基线步辩护为与既有研究对齐，anand_mukherjee_2024；变体 70：M2 自维护档案比较性数据质量辩护（强制核订→官方发布→点名第三方库失效模式+权威锚），fini_jourdan_perkmann_2017，EMERGING——区别于变体41 可得性辩护与变体55 provenance 链；变体 71：M1 设置含义调查佐证链（双制度张力陈述+设置内调查证 actor 感知，封存污名化替代解读），fini_jourdan_perkmann_2017，EMERGING——EXTEND 变体41 的 Setting rationale 槽位，提供张力句背后的证据链；变体 72：同构替代目标控制（同一构念对同类替代目标重算入模，封堵'普遍信念/偏好'类替代解释），desjardine_li_shi_2025_amj，EMERGING；变体 73：共有制子集镜像调节（调节变量聚合域限定为与中介机构共有制相连的对手子集——聚合域本身携带传导理论），desjardine_li_shi_2025_amj，EMERGING；变体 74：M2 可得性损耗对比 + 范围限制保守检验声明（pfarrer2010 型，M2）——数据可得性损耗致全样本缩减为缩减样本做三属性 t 检验，承认差异显著后把 restriction of range 重构为 conservative test（偏误方向对假设不利）；与变体 67 分工：67 无差异→安心，本变体有差异→保守 reframe；变体 75：M6 1/n 衰减加权历史自控制 + 权重窗稳健性（pfarrer2010 型，M6）——学习/传染文献正当化 1/n 递减权重加总 prior 行为与资产水平，每项括号命名被堵机制（halo/habitual surprisers/guidance），15/10/5/3 年权重窗同结果收口；变体 76：M2 双名单合并 + 重叠率验证（pfarrer2010 型，M2/M4）——单源覆盖口径随年份漂移迫使合并，并集编码规则 + 重叠率（22/25）作合并决策的经验验证收口；区别于变体 16（多源合并求全+防重复计数）；变体 77：M8 操作化定义稳健性——未列表替代阈值段（pfarrer2010 型，M8）——To ensure that our definition of X did not drive results 点明被检对象是定义本身，in analyses not reported here 诚实披露未列表地位，替代定义 cf. 引用锚定 field 惯例，substantively the same 收口；区别于 robustness-foreshadowing 微模板（仅预告句）与非线性模型 变体 8（Results 三角组织）；变体 78：M6 冲突证据→无假设控制声明——冲突史三方位综述 + did not put forth specific hypotheses + 遵循先行研究纳入 + NP 预测符号登记 + 池化样本行业中位数归一 because，gulati_1999_network_location_and_learning_the_influence_of_n，VERIFIED (expert_audit_override 2026-09-05)；变体 79：备择解释具名→控制变量化→可检验判据+边界让步（Named-Alternative-as-Control，Gulati_1999_AJS 型）——控制变量段以竞争假说组织，控制变量携带预声明显著性判据，同时向 rival 机制让渡共存空间；变体 80：源清单生存者条件化修复——回收未存活事件单元+风险集合并（higgins_2003_OS；行业清单以存活为条件→主动回收同窗内经历事件但未存活到编表年的单元（改名/并购/清算）+非事件单元并成风险集；M2）；变体 81：第三方榜单阈值化突出名单→生涯纽带计数→团队规模标准化（higgins_2003_OS；榜单+出现阈值→突出机构名单报量级与稳定性→逐人计数→除以梯队规模引先例+每类基率句；M4）；变体 82：采纳标准指数 DV 四拍出处链（higgins_2003_OS；原始开发者+更新者→跨领域通行度引用→缺失计数 all-but-n→第三方验证的比替代更细粒度论证+量表端点与均值；M3）；变体 83：有界异质性指数双测量+零锚定+工作例翻译（higgins_2003_OS；HHI/Blau 指数与 0..K 计数并置→无相关属性=0 锚定→谱系等价声明→两个可复算工作例演示打分；M4）；变体 84：档案研究田野佐证组件（higgins_2003_OS；访谈对象不进估计样本→过程复杂度通报+测量接地+常驻专家通报人，多类场所枚举与受访者构成报告；M2）；变体 85：M1/M2 问卷前置田野与抽样框-受访者双核验（gulati_2007 ASQ；两阶段访谈塑工具+清单双路核验+独立资格核验；区别于变体84 不进样本的过程佐证田野），VERIFIED；变体 86：M2 问卷响应率-非应答 K-S-范围排除段级全链（gulati_2007 ASQ；先例锚定检验特征+unique partner 双口径；区别于 micro 层 K-S+Heckman 与 K-S+双层代表性句式链——本条为段级全链），VERIFIED；变体 87：M3/M4 量表双构念区分+旋转交叉验证+低 α 保守反驳链（gulati_2007 ASQ；衰减逻辑保守检验反驳为语料空白拍；区别于变体66 PCA 控制合成与 micro 六环链——本条是焦点构念开发+双构念区分剔除），VERIFIED；变体 88：M4 复合构念替代规格三段防御+spline 分解（gulati_2007 ASQ；先例锚定→偏误场景数值对分析+替代重跑稳健→不可行性边界声明；spline 语料零覆盖；区别于变体83 双测量并置——本条防御的是规格选择），VERIFIED） |
| [自然实验-DiD](自然实验-DiD.md) | 自然实验-DiD | 15 | 2026-08-23；变体 O（M8_judicial_shock_two_assumption，moon2026）、变体 P（M2_staggered_did_always_treated_hygiene，moon2026）；2026-08-29 fang2025 POM 新增 4 变体（不编号）：RDiT 识别策略选择论证（为什么用时间断点而非 DiD）、局部断点外部效度两理由预抗辩、控制变量按竞争性解释编号分组引入、受影响单元两步考虑集抽样；变体 O：监管冲击强度→二元编码辩护 + 连续指数稳健收口（M4），castellaneta_conti_kacperczyk2017_smj，EMERGING；变体 P：处理×条件交互的行业级调节变量操作化链（M5，joint effect 宣告→定义+时点→数据库双承诺→既定方法锚→比例型测度），castellaneta_conti_kacperczyk2017_smj，EMERGING；变体 Q：专有核心库 + 按构念补外部源 + 合并后最终样本（M2，DV 相对优势→三重排除→构念-数据库映射→多维最终 N），castellaneta_conti_kacperczyk2017_smj，EMERGING |
| [非线性模型](非线性模型.md) | 非线性模型 | 16 | 2026-08-12；变体 20：M7 计数面板诊断三重链（过度分散→序列相关检验与修正→Hausman FE 选择），anand_mukherjee_2024，递进式补齐变体 1 未覆盖的两类后续诊断 |
| [生存分析](生存分析.md) | 生存分析 | 22 | 2026-08-01 |
| [SEM](SEM.md) | SEM | 4 | 2026-05-18 |
| [实验](实验.md) | 实验 | 6 | 2026-08-03 |
| [多研究](多研究.md) | 多研究 | 10 | 2026-08-12 |
| [定性过程研究](定性过程研究.md) | 定性过程研究 | 6 | 2026-07-07 |
| [稀有结果](稀有结果.md) | 稀有结果 | 3 | 2026-08-13 |
| [实证对象构建](实证对象构建.md) | 实证对象构建 | 5 | 2026-07-30；变体 6：交易级单位升级宣告（gulati2005型）——Unlike-prior-aggregation 单句立层级贡献 + 下一句交付子记录数据结构（respondent→focal unit→两大供应商记录），gulati_lawrence_puranam_2005，VERIFIED，M2；变体 7：专家报告人资格核验三环链（gulati2005型）——组织提名→业务线外办公室独立核验→问卷内自除名+替补提名，封住角色错配静默偏差，gulati_lawrence_puranam_2005，VERIFIED，M2；变体 8：类别变量问卷自分类+行为性双印证项（gulati2005型）——问卷内嵌定义的自分类为主，percentage-sourced 与 expected duration 行为性旁证为辅，随即分布宣告，gulati_lawrence_puranam_2005，VERIFIED，M3/M4；变体 9：文本相似度聚类竞争组构建（法定披露文本→pairwise 相似度→聚类分档→类目固定/成员年度更新），desjardine_li_shi_2025_amj，EMERGING；变体 10：M3 「无标准操作化」声明 + 总体相对分位阈值（pfarrer2010 型，M3/M4）——承认 field 无标准操作化并枚举替代方案→点名各替代的 distortion→industry-year 相对分位定义 materiality→cutoff 从更宽总体（数据库全域 N 而非估计样本 n）计算使阈值外生于样本构成 |
| [事件历史+事件研究](事件历史+事件研究.md) | 事件历史+事件研究 | 13 | 2026-08-12；变体 16：多窗口三角化（长短窗两难显式化 + 对披露假设的窗口无关性声明 + 长窗永久性检验），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 17：污染效应规避型事件日选择（已文档化污染效应反向证明所选日期洁净 + 惯例页码声明 + 备择日期让步式稳健），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 18：ZW2004 漏斗+剔除后总体等价检验（KS 两样本检验封住 selection 死角；变体 19：ZW2004 实现窗→样本时钟链（测量窗决定回归起点+短窗理论/量化双轨辩护）；变体 20：ZW2004 证据驱动短主窗选择（调整速度证据+污染风险→短窗正向论证+长窗 thoroughness 交棒）；变体 21：ZW2004 事件窗污染控制块（混杂清单权威锚+虚拟变量收口，其余控制变量平铺）；变体 22：ZW2004 多期 CAR 汇归估计栈（subgroup→regression 升级+AR(1)+时间趋势双路防御）；变体 23：ZW2004 Methods 内 selection 最小预告（两方程一句话+结果等价收口）；变体 24：ZW2004 测量四拍（定义→模型公式→Intuitively 直觉翻译→统计修正）） |
| [同时方程](同时方程.md) | 同时方程 | 5 | 2026-08-13 |
| [IV-2SLS](IV-2SLS.md) | IV-2SLS | 14 | 2026-08-13 |
| [动态面板-GMM](动态面板-GMM.md) | 动态面板-GMM | 5 | 2026-08-13 |
| [匹配DiD-广义DiD](匹配DiD-广义DiD.md) | 匹配DiD-广义DiD | 1 | 2026-08-05 |
| [同伴效应-网络效应](同伴效应-网络效应.md) | 同伴效应-网络效应 | 4 | 2026-07-30；变体 5：M4 加权平均操作化的两单元数值反例辩护 + 备选加权稳健收口，carpenterwestphal2001，VERIFIED；变体 6：M4 构念区分对照对——「distinct from 频次计数」显式声明 + 多而弱连/少而强连假想对照 + 构念涵义收口（同一构念多侧面组织），gulati_1999_network_location_and_learning_the_influence_of_n，VERIFIED (expert_audit_override 2026-09-05)；变体 7：M4 构造选择×备选项枚举契约——开头一次预告全部构造选择 + First/Second/Third 逐条配对备选 + 自由参数由外部文献基准定参，gulati_1999_network_location_and_learning_the_influence_of_n，VERIFIED (expert_audit_override 2026-09-05)；变体 8：M4 间接联结路径长度分离（第三方联结嵌套于总任命→总量作控制使残差=3+ 联结效应 + 强度排序预登记：直接共同联结>长路径），gulati_westphal_1999，VERIFIED；变体 9：M4 操作化谱系 PCA 综合 + 设计层级适配（三既有操作化枚举→命名综合研究 PCA 还原→dyad 层级加总适配→极值语义解读收口），gulati_westphal_1999，VERIFIED；变体 10：描述性结构预分析×理论回扣（Structural Preanalysis with Theory Loopback，Gulati_1999_AJS 型）——把描述性网络分析升格为理论参照物检验，每项结构发现即时回读理论机制。；变体 11：风险集宽度辩护×递减稳健性阶梯（Risk-Set Breadth Defense，Gulati_1999_AJS 型）——宽风险集预设为无偏性要件，承认反向偏差并论证不可先验筛选，再以递减风险集做稳健性 triage。；变体 12：重叠消解式构念区分（Overlap-Eliminating Construct Discrimination，Gulati_1999_AJS 型）——两个同源构念的操作化在数据构造层互斥（重叠事件置零），区分做进测量而非论证。；变体 13：滞后网络×同期效应区分声明（Lagged-Network Temporal Separation，Gulati_1999_AJS 型）——模型段脚注一句把滞后协变量与同期内生反馈模型族切开，时间先例即识别主张。；变体 14：dyadic 非独立性×随机化检验（Dyadic Nonindependence Randomization Test，Gulati_1999_AJS 型）——同一行为者复现于多条 dyad 的相依威胁，用估计器内随机化置换给出免分布稳健性判据。；变体 15：随机 DV 基线证伪检验（Random-DV Baseline Falsification，Gulati_1999_AJS 型）——把理论赌注（模式非随机）转成显式零假设，随机分配 DV 作基线并预声明败局条件。 |
| [文本构念测量](文本构念测量.md) | 文本构念测量 | 16 | 2026-08-13；变体 18：形式/实质二分解耦验证链（构念定义即编码规则 + 三重行为验证 + 排除规则自带 because），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；2026-08-29 fang2025 POM 新增变体：算法标注构念三层效度链（算法性能→人机信度→一致性验证；变体 19：M3/M4 手工+自动组合分类 → 与主体自分类子集交叉验证报匹配率（效度锚在外部主体自归档），anand_mukherjee_2024；变体 20：ZW2004 异质编码团队保守信度检验（无规则手册+背景异质=信度下限证明）；变体 21：M4 媒体检索算法精确性——结构性噪音排除（pfarrer2010 型，M4）——出版物机制理由→自建 search algorithm 排除 false positive 与目录页/名录/行情表三类结构性噪音→产出 N 收口；与变体 30（provider relevancy score）、lunetal2026（GLLM 过滤）构成三条媒体精确性路线） |
| [PSM匹配面板](PSM匹配面板.md) | PSM匹配面板 | 4 | 2026-08-12 |
| [堆叠扩散Logit](堆叠扩散Logit.md) | 堆叠扩散Logit | 0 | 2026-05-18 |
| [多行为者设计](多行为者设计.md) | 多行为者设计 | 1 | 2026-07-08；变体 2：M8 个体→组级聚合辩护链（构念层次理论化→r_wg/ICC 双判据→聚合收口），westphal_bednar2005，VERIFIED；变体 3：M4 个体/组层同构测量+子群合并等价声明+去重口径注，carpenterwestphal2001，VERIFIED |
| [推断二元结果](推断二元结果.md) | 推断二元结果 | 1 | 2026-08-05 |
| [两阶段模型](两阶段模型.md) | 两阶段模型 | 11 | 2026-08-23；变体 12：控制变量威胁源分组 because 枚举+测量形态内联（gulati2005型）——First~Finally 每组一个威胁源一句 because，log/单条目/类别界测量形态随行声明，竞争理论解释单独成组，gulati_lawrence_puranam_2005，VERIFIED，M6；变体 13：三分模式内生选择→分模式 λ 修正切换回归（gulati2005型）——naïve 哑变量×交互回归拒绝链（would not be appropriate→attempts to account for→controls for 因果语言三段限位）+多项式 Logit 第一阶段分模式算 λ+排除变量不入第二阶段前瞻声明，gulati_lawrence_puranam_2005，VERIFIED，M7/M8 |
| [VARX-PVAR](VARX-PVAR.md) | VARX-PVAR | 8 | 2026-07-15 |
| [结构需求-state-space](结构需求-state-space.md) | 结构需求-state-space | 6 | 2026-08-05 |

## 写入规则

1. 仅 `distill-methods-exemplar` Phase 4 验证通过的变体可写入
2. 每个变体标注来源论文、验证状态、写入日期
3. 不覆盖现有变体，仅追加
4. 变体达到 3+ 时，考虑提升为 skill 主骨架

## 语料库质量状态

> ✅ **2026-08-13 更新（Lun–Zurbruegg–Mount–Cheong 2026 ETP，Gate ① HIGH only）**: EO × COO power × product life cycle；面板条件 logit + 稀有二元 + 文本构念。新增（均单篇 EMERGING，`section_variant`）：
>   - **稀有结果** 变体2–3（M2 监管暴露总体含从未事件单元；M3 extensive/intensive margin → 二元 DV）+ M7 反模式（industry+year FE 误称 TWFE）
>   - **文本构念测量** 变体16–17（GLLM 句级假阳性过滤 + industry-year 标准化；阶段概率加总为连续生命周期调节）
>   - **面板数据-OLS** 变体49（职能高管权力：有职位薪酬比，无职位编码为 0）
>   未改 SKILL.md 核心路由。配套 Results：Logit 变体19–23、三向交互变体4。
> ✅ **2026-08-12 更新（Chen–Ganesan–Liu 2009 JM，distill-methods-exemplar writeback，Gate ① 全部确认含 OPTIONAL Kenny）**: 多阶段召回事件研究栈（CPSC AR → 截面 → Kenny 中介 → Heckman 切换）。新增 5 变体（均单篇 EMERGING / 待第二篇交叉验证，`section_variant`）；SKIP 市场模型公式与 CAR 后截面基础结构：
>   - **事件历史+事件研究** 变体12（M1）：**监管情境多理由合法性**（禁泄事件日 + 字段可观测策略 + 品类广度 + 排除高频偏误业）
>   - **事件历史+事件研究** 变体13（M2/M8）：**威胁三联预筛选**（混杂日 / 泄漏剔除兼 AE ruling / 分类模糊）
>   - **事件历史+事件研究** 变体14（M4）：**零事故报告=proactive** 监管公告结构化字段策略二分
>   - **事件历史+事件研究** 变体15（M5，OPTIONAL）：**Kenny 中介**（probit 策略选择 + 截面 AR）
>   - **两阶段模型** 变体10（M8）：**Heckman 策略切换回归** — 无先验直接效应+主表确认型排除限制；λ=0 验证主截面
>   - 新增反模式：威胁筛选无逐步 N；多阶段栈仅出现在 Results；排除限制事后改口
>   未改 SKILL.md / PDM 根。

> ✅ **2026-08-12 更新（Fini–Jourdan–Perkmann 2017 AMJ，distill-methods-exemplar writeback，Gate ① 全部写入）**: Social valuation across multiple audiences（Minerva scientist panel + Poisson GMM）。核心识别叙事已由 非线性模型 变体16 覆盖（今日入库）；本轮补 4 变体 + 3 反模式（均单篇 EMERGING，`section_variant`）：
>   - **面板数据-OLS** 变体41（M1）：**数据可得性挑战→独特档案数据集设置辩护**（DV 部分 censored/未披露 → 自建档案；双制度张力情境）——区别于单行业（15/23）与单一中介机构（33）
>   - **面板数据-OLS** 变体42（M5）：**调节 dummy 外部效度链**（身份 proximity dummy 用 Tijssen 学科 U-I 强度 0.071/0.061/0.046/0.039 外部连续测量验证 + 访谈锚定）——band=gap，corpus 首个调节测量效度链
>   - **PSM匹配面板** 变体4（M8）：**CEM 确认性复制**（内生焦点变量自身作处理，匹配后重估同估计器）——区别于变体1/2 主分析与外生冲击位置
>   - **多研究** 变体10（M9）：**Explanatory Sequential 三步确认路线图**（量化主分析→匹配确认→访谈机制佐证）——单研究内递进，访谈仅作机制佐证
>   - **非线性模型** 变体16 EXTEND：**平方项/边界交互工具化增量**（Abadie 2003）
>   - 新增反模式：CEM 匹配只报 strata 不报平衡统计量（PSM匹配面板 M8）、"三威胁合并表述"（非线性模型 M7）、工具化平方项/交互 exclusion 未逐一论证（IV-2SLS M8）
>   均为单篇 EMERGING；未改 SKILL.md 核心路由。

> ✅ **2026-08-12 更新（Ridge–Hill–Ingram–Kolomeitsev–Worrell 2024 AMJ，whole-paper distillation 的 methods writeback）**: CEO paranoia × stakeholder engagement（earnings-call 文本构念 + Tobit/NB + RIR/2SRI）。新增 6 变体（均单篇 EMERGING，`section_variant`）：
>   - **文本构念测量** 变体14–15：**从零自定义词典九步效度链**（组件→专家 sort→演绎词典→学生 sort→PFA→nomological→stability）+ **earnings-call speaker-attribution 管线**（fuzzy-match + 手工核对 + firm-year 折叠）
>   - **两阶段模型** 变体8–9：**内生性"balancing act"诊断先行叙事**（RIR 数量化 N-to-overturn → 治愈第二 → naïve/cured 配对）+ **2SRI 治愈 + validation-measures 复用为 instruments**
>   - **面板数据-OLS** 变体39–40：**时间间隔一句声明（DV t+1 / IV t）** + **控制变量"双面 because"（对 DV 一条 + 对 IV 共变一条）**
>   - 新增反模式：非线性估计器单句选择无诊断链（非线性模型 M7）、理论检验型面板缺设置合法性（面板 M1）、行业/年度 dummy 替代 firm FE 未辩护 + 未声明聚类 SE（面板 M7）
>   均为单篇 EMERGING；未改 SKILL.md 核心路由。配套 Results 由同批 distillation 的 write-results worker 处理。

> ✅ **2026-08-05 更新（Zorn–Shropshire–Martin–Combs–Ketchen 2017 SMJ）**: S&P 1500 lone-insider boards + 2SLS。新增：
>   - **IV-2SLS** 变体12–13：industry leave-out 均值 IV（CEO 推动采纳内生性）+ 连续 DV 用 2SLS/FE、稀有二元放弃 FE 改聚类 Logit（IV-Probit 稳健性预告）
>   - **面板数据-OLS** 变体32：结构二元「kind rather than degree」相对 majority-independence 的构念辩护
>   - **稀有结果** 变体1（**首填**）：低事件率 → FE 丢样本 → 年份虚拟+单元聚类 Logit
>   均为单篇 EMERGING；未改 SKILL.md 核心路由。配套 Results：`../write-results/corpus/IV-2SLS.md` 变体8–10。

> ✅ **2026-08-05 更新（Castellaneta–Conti–Kacperczyk 2017 SMJ 蒸馏）**: 交错 UTSA + PE buyout 持有窗截面。新增：
>   - **自然实验-DiD** 变体8–13：dual-sale setting、持有窗处理+staggered 示例、IRR/ΔV≈DiD 一阶差分等价、entry/exit 年 FE 栈、政治经济外生性电池、±k 年日历安慰剂
>   - **匹配DiD-广义DiD** 变体1（**首填**）：CEM 匹配 ex-ante 价值+风险代理作为准实验稳健性
>   均为单篇 EMERGING；不将 IRR≈DiD 提升为现代面板 staggered-DiD 默认路由；未改 SKILL.md 核心。

> ✅ **2026-08-05 gap audit（Kim & Lee 2026 SMJ）**: Methods **无需新增**（多研究变体6 / 非线性变体10 / 文本构念变体12 已覆盖）；配套 Results 缺口补写见 `../write-results/corpus/`（OLS-FE 变体45–46）。

> ✅ **2026-08-05 更新（Liu & Shankar 2015 MS 蒸馏）**: **首次填充**设计类型 `结构需求-state-space`（BLP + Kalman + GMM，product-harm crises 需求侧动态）变体1–6；扩展 `面板数据-OLS` 变体29–31（severity 理论分类、媒体 relevancy 阈值、异频月聚合）、`两阶段模型` 变体7（价格 BLP-IV + 广告双端 CF + 跨品类媒体 IV）。均为单篇 EMERGING；与 survival/time-to-recall 召回家族分工，不修改核心路由。

> ✅ **2026-08-05 更新（Hoffmann et al. 2024 JM 重蒸馏）**: 修正既有 hoffmann2024 slot 变体中的两处事实错误（误写 firm FE / incidental parameters；原文为 year+industry FE + always-zero DV collinearity）。新增：
>   - **自然实验-DiD** 变体4–7：Marketing quasi-experiment 识别栈、无 firm FE 辩护、POST 共线性说明、裁量权/行业扩展漏斗
>   - **非线性模型** 变体15：Schmitz reduced-form 三阶交互 + staggered collinearity
>   - **文本构念测量** 变体13：validated dictionary 相对净得分 + 大规模语料辩护
>   - **推断二元结果** 变体1（首填）：裁量权边界子样本
>   - slot-M1/M2/M7/M8 EXPERIMENTAL 变体同步升级（paper_id: `hoffmann_cheong_phan_zurbruegg2024`）
>   均为单篇 EMERGING；未使用 Sun–Abraham 估计器，不提升为核心路由规则。

> ✅ **2026-08-04 更新（Lee–Park 2024）**: 非线性模型新增两条写作型变体：有界结果的“估计尺度—正式形状标准—可解释尺度”契约，以及“先声明几何对象、再直接比较条件转折点”的位置型曲线调节。Lee & Park 经用户专家审计为典型 U／倒 U 写作范文，两条变体均登记为 **VERIFIED**。同步加入术语与边界：quadratic vertex 不称 inflection point；二次项和交互项的符号不能替代端点斜率、内部转折点及直接差异检验。主 skill 路由不变。

> ✅ **2026-08-03 更新（Schumacher–Keck–Tang 2020）**: 面板数据-OLS 新增“任期早期构念形成窗与后续结果观察窗完全分离 + 媒体/期权方法异质双代理”变体；`executive-confidence-operationalization` 同步补入 M4 生成骨架与两条诚实边界：窗口分离不等于外生性，双代理同向不等于构念纯度。该变体为单篇 EMERGING reference，不提升为默认核心规则。

> ✅ **2026-08-03 更新（Kashmiri–Nicol–Arora 2017）**: `executive-confidence-operationalization` 增加“视觉显著性 + 传播显著性 + 相对现金/非现金薪酬”的 CEO narcissism 复合代理，并加入 succession-year exclusion、同一 CEO 跨期稳定性与同一企业继任 CEO 对照；`model-selection-comparison` 增加多结果 `measurement property → estimator → interpretation scale` 路由；M3 新增 product-harm crisis 与 recall timing/strategy/severity 的强制边界声明。均为单篇 EMERGING reference，不改变核心槽位。

> ✅ **2026-08-03 更新（Vidal–Mitchell 2015；Moon–Tuli–Mukherjee 2023）**: 非线性模型新增“随机效应面板 Poisson：分布诊断—estimand 对齐”变体；IV-2SLS 新增“同行 IV 距离梯度组合”变体；两阶段模型新增“多内生性威胁—修正方法配对账本”变体。均为 reference-level / EMERGING，不替代既有 Tobit、地理 IV 或单一控制函数变体。

> ✅ **2026-08-02 更新（Lee–Wu–Bednar, Organization Science）**: 首次填充自然实验-DiD：跨层级冲击映射与样本漏斗、有符号计数衍生 DV 的估计器选择、错位 DiD 三层诊断栈。第三项标记为 **LEGACY-DIAGNOSTIC**：Bacon 分解只诊断传统 TWFE，不替代 Callaway–Sant'Anna / Sun–Abraham 与平行趋势敏感性分析。

> ✅ **2026-05-20 更新**: 五篇产品召回论文 (Darby2026 JOM / Darby2025 JSCM / Eilert2017 JM / Darby2023 MSOM / Wowak2025 MS) 交叉验证完成。
>
> **设计家族**: 4篇生存分析(AFT+Weibull) + 1篇IV-2SLS(Lewbel heteroskedastic identified instrument)
> **核心骨架 (5/5 必现)**: Time-to-Recall操作化 (days from defect awareness to recall initiation)、firm+year FE
> **高频可选模块 (3-4/5)**: 控制变量分层because、复发事件处理、样本交集漏斗
> **双篇高价值 (2/5)**: 事件研究法、CEM匹配、CPH稳健性对比
> **单篇高价值 (1/5)**: 分布选择BIC比较、右删失处理、IV三层because论证链、mixed-effects机制分解、替代变量机制矩阵、CAR非参数检验双报告、信息泄露检验、Lewbel三步法、IV诊断链完整报告、政治意识形态操作化
>
> ✅ **2026-07-06 更新**: 蒸馏 Cutolo & Ferriani 2024 (JM) "How Narratives Can Help Atypical Actors Increase Market Appeal" 新增 4 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 文本构念测量 变体5：**复合文本指标构建**（多子维度 → 分别测量 → 平均合成）
>   - 文本构念测量 变体6：**类别相对文本常规性操作化**（LDA topic → category-average regression slope）
>   - 文本构念测量 变体7：**文本测量人工验证**（随机样本检查）
>   - 非线性模型 变体1：**计数模型选择**（负二项回归 + 过度分散诊断）
>   - 配套 write-results：count-model moderation translation、text-measure robustness bundle、composite text component disaggregation
>
> ✅ **2026-07-06 更新（续）**: 蒸馏 Falchetti, Cattani & Ferriani (SMJ) "Start with 'Why,' but only if you have to" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 多研究 变体1：**多研究实验项目总览**（研究梯度图：audience × stimulus × DV 变异矩阵）
>   - 多研究 变体2：**操纵检验 Pilot Study 段落**（嵌入主 Methods 的操纵验证）
>   - 实验 变体1：**单实验 Methods 标准段落**（被试→材料→操纵→测量）
>   - 配套 write-results：experimental ANOVA four-beat、Hayes PROCESS mediation reporting、cross-study synthesis
>
> ✅ **2026-07-07 更新**: 蒸馏 Lashley & Pollock 2020 (ASQ) "Waiting to Inhale" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁新设计类型「定性过程研究」：
>   - 定性过程研究 变体1：**现象与方法正当化**（limited understanding → inductive qualitative approach）
>   - 定性过程研究 变体2：**极端情境选择理由**（extreme situation + theoretical tensions visible + background stability）
>   - 定性过程研究 变体3：**多源数据角色分配**（observations / interviews / archives 各捕获什么）
>   - 定性过程研究 变体4：**过程阶段划分与编码进阶**（chronology → bracketing → open coding → axial coding → aggregate dimensions）
>   - 定性过程研究 变体5：**可信性机制组合**（triangulation + prolonged engagement + peer debriefing + secondary coding）
>   - 配套 write-results：process-model overview、front-stage/backstage contrast、side-stage negotiation、audience-specific success assessment
>
> **已填充变体**: 49个 (分布于 13个设计类型文件)
> **新设计类型解锁**: 实验、多研究实验、定性过程研究
>
> ✅ **2026-06-16 更新**: 蒸馏 Qiao, Hiatt & Sine (2026, SMJ) "dual imprinting" 新增 3 个高价值变体（均单篇、不可跨论文复现声明已标注）：
>   - 生存分析 变体6：**因 Cox 比例风险失败（Schoenfeld）→ piecewise exponential + 理论时段分割**（估计器由诊断驱动 + 分段由理论驱动）
>   - IV-2SLS 变体4：**外部自然事件（自然灾害）作工具变量 + 三因排除限制论证**（外生性 / 制度缝隙渠道 / 结果文献反推无直接渠道）
>   - PSM匹配面板 变体3：**Entropy Balancing (EBM)** — 重加权、保留全部观测，适用于处理组稀少/需保全样本的研究
>   - 配套 write-results：IV-2SLS 变体4（control-function 残差作非线性 DWH + 有限样本偏误诚实提示）、SEM-moderated-mediation（reverse-code + Wald 检验对立通道持续性差异）
>   - 配套 write-theory：mechanism_chain.md 新增"双重印记对立通道 + 效果持续性差异 + 底物匹配调节"骨架；write-introduction：theory-lens/05-maxim-contrast 变体B（单句历史名言作 foil）
>
> ✅ **2026-07-07 更新**: 蒸馏 Mayo, Ball & Mills (2022, POM) "CEO Tenure and Recall Risk Management" 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁复发事件风险模型子类型：
>   - 生存分析 变体7：**复发事件指数风险模型 + 连续递增时间 + 备选分布稳健性**
>   - 生存分析 变体8：**三分位离散化 IV（等样本量理由 + 同模型双向检验）**
>   - 生存分析 变体9：**Goldman-Huang 三步 CEO 被迫离职分类**（协议逐字引用+频次报告）
>   - 生存分析 变体10：**SEC 10-K 披露作为事件裁量权测量**（GAAP 重大性杠杆）
>   - 生存分析 变体11：**表格式控制变量辩护（"Potential Factor of Influence"列）**
>   - 生存分析 变体12：**CEM 匹配程序（双向处理、作为稳健性非主识别）**
>   - 配套 write-results：风险模型三拍+exp(β)−1百分比、交互效应简洁报告、分样本Wald χ²+null确证叙事、CEM双向ATE、替代机制交互检验+诚实收尾
>
> ✅ **2026-07-07 更新（续）**: 蒸馏 Haunschild, Polidoro & Chandler (2015, ORSC) 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 非线性模型 变体2：**负二项回归选择 — 竞争焦点 DV 的模型论证**（ZINB 排除 + e^β−1 预告）
>   - 非线性模型 变体3：**竞争焦点 DV 互控 — 排除伪 trade-off**（双向互控 + 无互控稳健性）
>   - 非线性模型 变体4：**替代测量构造效度三角 — 双层测量正当性**（广义vs特定响应区分）
>   - 配套 write-results：计数模型 变体7-9（主效应四拍+e^β−1、无显式交互项调节效应、跨测量复制）
>
> ✅ **2026-07-07 更新（续2）**: 蒸馏 Mannor, Wowak, Bartkus & Gomez-Mejia (2016, SMJ) 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 文本构念测量 变体8：**LIWC 双成分净得分 + face validity 引语锚定**
>   - 面板数据-OLS 变体6：**多通道精英/关键行为人招募**
>   - 面板数据-OLS 变体7：**嵌套横截面数据的聚类稳健标准误**
>   - 面板数据-OLS 变体8：**回顾性偏差三角检验**
>   - 配套 write-results：OLS-FE 变体8-10（主效应不显著但调节显著、单侧边际效应、ΔR²经济显著性）
>
> ✅ **2026-07-07 更新（续3）**: 蒸馏 Pfarrer, Pollock & Rindova (2010, AMJ) 新增 3 个高价值变体：
>   - 事件历史+事件研究 变体5：**事件窗口+市场模型+标准软件声明**
>   - 非线性模型 变体5：**RE 面板 Logit + odds-ratio 报告惯例**
>   - 非线性模型 变体6：**理想型二分化 + 复合媒体构念测量**
>   - 配套 write-results：Logit-Probit-Ordered-Probit 变体1-3（首次填充该结果类型）
>
> ✅ **2026-07-07 更新（续4）**: 蒸馏 Desai (2011, AMJ) 新增 3 个高价值变体：
>   - 非线性模型 变体7：**条件 FE 负二项 + 全零面板审计**
>   - 面板数据-OLS 变体9：**制度断点样本辩护**
>   - 配套 write-results：计数模型 变体10-11（负主效应+正交互条件反转、跨模型共线性说明）
>
> ✅ **2026-07-07 更新（续5）**: 蒸馏 Bamberger, Homburg & Wielgos (2021, JM) 新增 3 个高价值变体：
>   - 多研究 变体3：**混合方法多研究设计的情境+数据源衔接**
>   - 面板数据-OLS 变体10：**Hausman FE vs RE 检验**
>   - 配套 write-results：多研究 变体2（跨研究镜像首句）、SEM-moderated-mediation 变体2（不一致中介→抑制变量）、OLS-FE 变体11（边际显著 90% CI）
>
> > ✅ **2026-07-07 更新（续6）**: 蒸馏 Li, Chiu, Kong, Cropanzano & Ho (2026, JOM) "A Sensemaking Model of Investor Reactions to CEO Achievement Expression" 新增 6 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 面板数据-OLS 变体13：**RE 选择三重辩护 — 理论+Hausman+ICC**
>   - 面板数据-OLS 变体14：**全谱系控制变量 — 高because密度+RavenPack事件控制+CEO人格特质**
>   - 文本构念测量 变体10：**LIWC 默认字典效度链 — 效度引用+补充实验验证+区段聚焦理由**
>   - 实验 变体2：**开放式文本 RA 评分操纵检验 — 替代 traditional self-report**
>   - 多研究 变体4：**三研究递进设计论证 — 内部效度→概念复制→生态效度**
>   - 事件历史+事件研究 变体7：**三DV互补市场反应测量体系 — CAR+ATV+投资者文本情绪**
>   - 配套 write-results：实验变体3（被调节的中介五拍）、OLS-FE 变体13-15（交互百分比经济显著性/低基础率边际直方图/五威胁标签化稳健性）、多研究变体3（三研究递进结果叙事）、新建事件研究法文件

> ✅ **2026-07-07 更新（续7）**: 蒸馏 Ahmadi, Khanagha, Berchicci & Jansen (2017, JMS) "Are Managers Motivated to Explore in the Face of a New Technological Change?" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - 实验 变体3：**视频操纵 + 两阶段数据收集** — 替代纯文本vignette，T1特质/T2实验时间分离
>   - 实验 变体4：**双极量表选择辩护** — continuous vs orthogonal 测量论证
>   - 实验 变体5：**专业样本同质性辩护** — 单组织内同质管理者群体
>   - 配套 write-results：OLS-FE 变体16（7模型层次回归表导航）、三向交互 变体1（三向交互条件分解，首次填充）、多研究 变体4（跨研究差异嵌入Results讨论）

> ✅ **2026-07-08 更新**: 蒸馏 Cui, Yang & Vertinsky (SMJ) "Attacking your partners: Strategic alliances and competition between partners in product markets" 新增 10 个高价值变体（均单篇、待第二篇交叉验证声明已标注），解锁/填充 5 个设计类型：
>   - **同伴效应-网络效应**（首次填充）变体1-3：**degree centrality 差值**、**common ties 计数**、**ego network density via two-mode incidence transformation**
>   - **多行为者设计**（首次填充）变体1：**multiparty alliance 拆 dyad + 混淆控制**
>   - **面板数据-OLS** 变体15-18：**双重现象设置辩护**、**多源 alliance 交叉验证**、**多维行为 factor score**、**dyad FE + dyad 聚类 SE + 具体混淆源举例**
>   - **文本构念测量** 变体11：**手工 content analysis 编码规则 + 边界案例 + 焦点 actor 视角**
>   - **实证对象构建** 变体2：**FDA 监管产品竞争组构建**
>   - 新增反模式：调节效应论文 Methods 未报告交互项构造、手工内容分析未报告编码者间一致性
>
> ✅ **2026-07-08 更新**: 蒸馏 Chung, Low & Rust (2022, JAMS) "Executive confidence and myopic marketing management" 新增 5 个高价值变体（均单篇、待第二篇交叉验证声明已标注）：
>   - **面板数据-OLS** 变体19-21：**高管信心期权 moneyness 操作化**、**model-free evidence 预览**、**三向交互模型设定（mean-centering + 完整 lower-order terms + 聚类 SE）**
>   - **两阶段模型** 变体3：**Heckman 选择模型 + 同行 CMO prevalence 排他性限制（跨 segments 加权）**
>   - **IV-2SLS** 变体5：**DWH 检验 + Gaussian copula 内生性叙事**
>   - 配套微模板：executive-confidence-operationalization、interquartile-economic-significance、heckman-peer-prevalence-exclusion、alternative-dv-falsification
>
> ✅ **2026-07-22 更新**: 蒸馏 Ilicic & Brennan (2026, JM) "Political Ideology Shapes Consumer Responses to Addictive Products" 新增 2 个高价值变体（均单篇、待第二篇交叉验证声明已标注）——首次填充 consumer psychology 机制证明传统：
>   - 实验 变体6：**测量过程+操纵过程双设计 + rival accounts battery** — Spencer, Zanna & Fong (2005) 双过程收敛机制设计；一次研究测量 9+ 竞争中介并逐一排除 + 随机化中介呈现顺序（区别于 slot-R8 的 1-2 个替代中介结果报告）
>   - 多研究 变体5：**Empirical Plan 因果阶段化预告段** — foundation→effect→process→intervention 理论因果阶梯（区别于变体4 的方法论效度阶梯）；含 foundation pilot（现象建立型）+ "Having established... we next investigated whether..." 因果阶段转折句
>   - 配套 write-results：多研究 变体5（逐研究 Discussion 接力立项）、SEM-moderated-mediation（reverse-order mediation 仅作竞争排序敏感性检查；不能确认序列中介的时间或因果顺序）
>   - 配套 write-theory：hypothesis_forms（序列中介叙事打包式）、hypothesis_derivation_patterns（counterintuitive direction-reversal via mechanism substitution）

> ✅ **2026-07-22 更新**: 蒸馏 Kim & Lee (2026, SMJ) "Putting a Price on Mission" 新增 3 个高价值变体（均单篇、待第二篇交叉验证声明已标注）——empirical strategy / strategic human capital 风格（首篇多阶段决策管道 + WTP）：
>   - 多研究 变体6：**同一 IV 跨决策阶段管道** — 各阶段不同分析单元 + 条件性样本递减（attraction/selection/attrition，Schneider ASA）；区别变体1-5 的 cross-study 独立样本梯度
>   - 非线性模型 变体10：**revealed-preference WTP 三估计器系数比**（LPM/conditional logit/mixed logit，-beta_X/beta_price）；corpus 零命中 WTP/mixed logit；顺手修复 variants_count 重复键 typo
>   - 文本构念测量 变体12：**手工二元编码 + 多源聚合 + embedded/peripheral 构念边界**（区别变体11 的边界案例披露，本变体理论上限定构念范围到 core identity）
>   - 配套 write-results：OLS-FE 变体27（多阶段管道衰减 profile + 跨阶段对比句）、slot-R5（WTP 经济显著性双 benchmark）、slot-R6（Slough post-treatment selection 诚实边界）

> **已填充变体**: 120个 (分布于 14个设计类型文件；本轮 Bendig et al. 2024 +1：面板数据-OLS M7 +1)
> **新设计类型解锁**: 同伴效应-网络效应、多行为者设计

> ✅ **2026-08-04 更新（Bendig, Hensellek & Schulte 2024 ETP 蒸馏）**: 面板数据-OLS 变体28新增 **binary-panel GEE + all-zero panel retention + formal U-test chain**。该变体与既有 GEE 变体22构成“同估计器、不同选择理由”的对照：变体22服务于时不变 IV；变体28服务于保留始终无事件但焦点活动有变异的企业，并预先要求二次项、两端斜率、拐点与 Fieller 区间共同支持曲线。
>
> ✅ **2026-07-23 更新（sync from local backup）**: 从 pre-sync 备份补回两批本地蒸馏成果：
>   - **VARX-PVAR 设计类型接入**（Borah & Tellis 2016, JMR）：8 个 Methods 变体（行业情境 4-reason 辩护、品牌选择 + quasi-experiment、第三方 NLP 数据 + 人工匹配、算法准确率双重验证、VARX 框架 3-reason 辩护、Granger causality 外生性论证、VARX 方程规格、VARX 估计细节）。配套 `../write-results/corpus/VARX-PVAR.md`（7 个 Results 变体）。
>   - **Pupovac, Astvansh, Carrillat & Legoux (2026, POM) "Product Recall Contagion in the Supply Chain" 蒸馏**：补回 7 个 Methods 变体——事件历史+事件研究 变体 8/9/10、两阶段模型 变体 4/5、面板数据-OLS 变体 23/24；含 2 个新反模式（事件-企业多源匹配无每步 N 审计、控制变量全部外包至附录）。
>   - 注：面板数据-OLS 变体编号因远程 86f478d 已占用 22（GEE，Abdurakhmonov et al. 2026 JOM），本地原 22/23 续编为 23/24。
>
> ✅ **2026-07-25 更新（du_tsolmon2024 ORSC 蒸馏）**: 基于 Du & Tsolmon (2024, *Organization Science*) "Post-M&A Retention of Top Managers: The Role of Structural Knowledge"：
>   - **实证对象构建** 变体3：**连续相似度指数构建**（base unit 计数比率公式 1−|A−B|/(A+B) + 0.1 平滑零值 + 0-1 归一化 + identical/moderate/extreme 三数值示例 + binary 替代版本）
>   - **面板数据-OLS** 变体25：**DV 文献基准锚定**（retention rate 54.8% vs Hambrick & Cannella 55% / Krug & Hegarty 59.4%——均值与前人文献对比建立跨样本可比性）
>   - **面板数据-OLS** 变体16 EXTEND：**三层异质数据库漏斗 + 附录审计**（交易库→人员库→结构库 576K→15,773→2,941 + 附录 match rate + 初始vs最终样本变量对比）
>   - 可改进警示（反哺反模式）：0.1 平滑常数无 because/敏感性检验；相似度公式对称性未讨论
>   - 配套 Results 新增 6 变体见 `../write-results/corpus/OLS-FE.md` 变体 29-34

> ✅ **2026-07-30 更新（pollock2015 蒸馏）**: 基于 Pollock, Lee, Jin & Lashley (2015, *ASQ*) "(Un)Tangled"——新创 VC 企业 status↔reputation 共演，动态同时方程面板 + AB difference GMM。**首次填充 2 个设计类型** + 扩展 2 个，共 +8 变体（均单篇、待第二篇交叉验证）：
>   - **动态面板-GMM**（首次填充）变体1–4：**AB difference GMM 三源内生性统一处理**（LDV/同时性/异质性逐一列举→AB 作统一解）、**difference vs system GMM 选择**（young firms 远未稳态→放弃效率选一致性）、**工具变量滞后结构 per-sample 经验精调**（外生性类别定起始阶→Hansen J/diff-Sargan/AR(2) 三诊断逐变量精调，分样本各自精调）、**发展性调节无理论断点→多阈值分样本检验**（跨多个 age 阈值展示效应梯度）
>   - **同时方程**（首次填充）变体1–2：**动态同时双方程规格**（path dependence + simultaneity + FE 三特征显式映射到方程）、**堆叠非嵌套 Wald χ² 检验**（Weesie 1999 stack + vce(cluster) 恢复跨方程协方差，解决非嵌套系数比较难题——H1a/H1b 不对称方向检验的关键创新）
>   - **同伴效应-网络效应** 变体4：**Bonacich beta centrality 作 status 全局网络中心性测量**（区别 degree centrality 的局部结构；全数据库计算 + 移动窗口平滑 + 标准化跨构念比较）
>   - **实证对象构建** 变体4：**multi-item formative objective index + 跨年 rescaling 100 分制**（reputation 客观指标测量；形成性指标 + 排除理论需另用变量 + 年内排序保持/年际市场方差消除 + 标准化跨构念比较）
>   - 配套 write-results：见 OLS-FE.md（路径依赖 ρ 解释、分样本系数比较叙事、零结果 Monte Carlo 功效分析、partial support 叙事）
>   - 配套 write-theory：developmental reversal of reciprocal-causation asymmetry (H1a/H1b) + differential persistence / lagged-DV moderation (H2) 见 hypothesis_derivation_patterns.md

> ✅ **2026-07-30 更新（malshe2015 蒸馏）**: 基于 Malshe & Agarwal (2015, *JM*) "From Finance to Marketing"——5-方程 SUR/3SLS 系统（leverage↔advertising/R&D↔customer satisfaction↔firm value）。共 +3 变体（均单篇、待第二篇交叉验证）：
>   - **同时方程** 变体3：**辅助反向因果方程**（system 内增设 policy-variable 作 DV、下游变量滞后项作预测变量的方程，吸收"下游需求→政策变量"reverse-causal channel；区别变体1 的当期同时性）
>   - **同时方程** 变体4：**DWH 检验裁决"是否需要 IV"**（SUR 有效 vs 3SLS 一致；DWH 不显著→内生性不是问题→选 SUR）+ Hansen-Sargan 工具有效性——与"用 IV 处理内生性"常规叙事反向；与 `write-results/OLS-FE` 变体39（替代估计器失败佐证主估计器）互补
>   - **面板数据-OLS** 变体26：**跨库手工匹配（无共同标识符）+ 多源漏斗**（ACSI↔Compustat 无公用 firm ID → manually matched + 五库合并 + 限定上市 + 排除金融行业漏斗）
>   - 配套 write-results：OLS-FE 变体40-42（floodlight 符号反转交互双转折点、同时方程三条件中介+非对称支持、反直觉反向延迟到 Discussion）

> ✅ **2026-07-30 更新（zhou2017 蒸馏）**: 基于 Zhou, Gao & Zhao (2017, *ASQ*) "State Ownership and Firm Innovation in China"——双研究（new product ratio Tobit + patent Poisson）、institutional vs efficiency logics 整合。共 +3 Methods 变体（均单篇、待第二篇交叉验证）：
>   - **IV-2SLS** 变体10：**地理外生性工具变量（Frankel-Romer 型）**——用省会到大港口（香港/上海）的 Great Circle 物理距离作 institutional development 的 IV；区别自然灾害 IV（变体4）、Bartik（变体7）；配套第一阶段 F=144.12
>   - **多研究** 变体7：**同一理论模型跨 facet-DV 双研究复制**——Study 1 new product ratio（commercial, Tobit）+ Study 2 patent（fundamental, Poisson）；区别 cross-study 独立样本梯度（变体1-6）
>   - **非线性模型** 变体11：**Tobit corner-solution**——非负、零聚集 DV（R&D intensity、new product ratio）；区别负二项（count, 变体1）、面板 Logit（binary, 变体5）
>   - 配套 Intro：`03-non-coherence` 变体A 增"双层 non-coherence（理论对立+实证 mixed 三方向）+ facet-decomposition resolution"；Theory：`hypothesis_derivation_patterns` dual-logic 增"moderator-as-remedy（H3/H4：竞争/start-up 作 agency 低效的解药）"；Results：多研究 变体6（双研究核心收敛+样本解释的发散）、三向交互 变体3（线收敛=差距消除器）

> ✅ **2026-07-30 更新（pontikes2012 蒸馏）**: 基于 Pontikes (2012, *ASQ*) "Two Sides of the Same Coin"——software 行业 label ambiguity 跨受众评估。共 +1 Methods 变体（单篇、待第二篇交叉验证）：
>   - **实证对象构建** 变体5：**label-ambiguity 从共属重叠构建（fuzziness + leniency）**——fuzz = 1 − contrast；leniency = fuzz × ln(不同其他标签数)，区分"重叠到同一标签（仍 constraining）"vs"重叠到多标签（不 constraining）"；fuzzy-set grade of membership（部分归属 μ∈[0,1]）+ 加权聚合到 actor 层。构念是**标签属性**从成员共属网络结构推导，区别 Jaccard/计数比率/形成性指数。
>   - 配套 Intro：`tensions/04-reality-contradicts-consensus` 变体G（共识惩罚 vs 行为持续 + 修辞问 pivot）；Theory：audience-role dichotomy 增"two-stage complementary process reconciliation"（temporal staging 化解 VC/consumer 相反偏好的 irony）；Results：跨受众构念对比 变体1（首次填充——同一构念跨两类受众镜像相反效应 + 受众内 corporate-VC 反转）
>   - 注：发现 `write-theory/.../hypothesis_derivation_patterns.md` 中 audience-role dichotomy 模式**重复两次**（pre-existing duplication）——本次 two-stage 扩展通过 replace_all 同步写入两份，保持一致；建议日后 dedup。

> ✅ **2026-08-01 更新（darby2025 蒸馏）**: 基于 Darby, Wowak, Ketchen & Connelly (2025, *JSCM*) "An Agency Theory Perspective on Activist Investors and Supply Chain Failures"——recurrent-event AFT (Weibull) + frailty + PSM + CPH/marginal risk set 稳健性的生存分析。该论文（darby2025_activist_investors）已在 source_papers 中，本次蒸馏补齐**已登记来源但尚未提取为变体的方法学写法**（7 个新变体，均单篇、待第二篇交叉验证）：
>   - **生存分析** 变体16：**AFT 显式方程 + 双向固定效应嵌入**（M7）——变体1 是纯叙述引入，本变体补显式广义估计方程 Log(t_ijt)=β₀+βX+ΣFirm+ΣYear+u，使 FE 识别逻辑在数学层可见
>   - **生存分析** 变体17：**构念构建三步法 + fuzzy matching 多数据库链接**（M4）——13D/13D/A→13f 跨库实体链接，fuzzy score<0.95 手工核对 + conservative exclusion；区别变体14（止于 intersection）和变体8/10（单源构念）
>   - **生存分析** 变体18：**分样本调节设计（split-sample 替代交互项）**（M5）——分类调节变量（FDA Class I/II vs III）拆样本而非加交互项，理论理由=离散类别不可加性改变机制；与变体15（同模型交互）和变体8（同模型哑变量）形成对照族
>   - **生存分析** 变体19：**Threat-based 稳健性四威胁框架（生存分析专属）**（M8）——omitted（progressive controls+frailty）/ reverse（panelized FE+lagged IV）/ measurement（PSM）/ alternative estimators（CPH+marginal risk set）四威胁分节；语料库首个按威胁组织的完整稳健性架构
>   - **生存分析** 变体20：**Frailty 双层稳健性（recall-level + shared firm-level）**（M8）——Gamma frailty 两层独立报告，回应 event-level 与 firm-level 两种未观测异质性
>   - **生存分析** 变体21：**Marginal Risk Set 模型（Wei, Lin & Weissfeld 1989）**（M8）——作为复发事件处理的稳健性替代（stratification by event order），区别变体4/7（主模型复发事件处理）
>   - **生存分析** 变体22：**分析设计服务于理论构念——排除处理组以捕获"威胁而非实现"**（M7/M8）——语料库首个"样本定义=理论构念识别条件"的元层面骨架；适用于 spillover/contagion/anticipatory/deterrence 效应研究
>   - 配套 write-results：生存分析 变体15-19（"every day counts"经济显著性辩护、dummy-coding 方向翻译、分样本显著vs不显著对照、threat-based 四威胁报告、PSM ATE 天数翻译）；配套 write-theory：新增 `sentences/leitmotif-section-opener.md`（段首主导动机串联句）
