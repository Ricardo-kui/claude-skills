# write-* 技能剪枝清单（2026-09-06，供裁决定夺）

> **目标**：技能可靠地把草稿送到 80 分，让作者的编辑杠杆最大化。
> **判定标准**：①生成期上下文最小化（SKILL.md 每次必载）；②审查职责归专职 review 技能；③no-op 删除；④单一事实源；⑤零触发机制待数据淘汰。
> **处置档位**：**P0** 安全剪（纯减常驻行数、零行为变化，可批量执行）｜**P1** 需逐项裁定（职责再分配/语义统一/删文件）｜**P2** 待数据（跑 2–3 篇真实草稿后回填）。
> **盘点来源**：四代理全量扫描 write-introduction（15 references/13 corpus 子目录）、write-theory（8 references/17 subprotocols）、write-methods（24 references/25 设计类型）、write-results（28 references/24 corpus 文件），全部指针实测无断链（孤儿与 stale 见 E 节）。

---

## A. 跨技能合并（P0，最大单笔收益）

| ID | 位置 | 现状 | 处置 | 护栏 |
|----|------|------|------|------|
| A1 | intro L39-48 + theory L35-43 + **methods L105-113 + results L98-106**（四节同构 ≈90–95%；retrieve_exemplars.py 已四节接线） | 四份四步流程逐句同义，常驻 ~35 行 | 下沉为 story-blueprints 侧单一协议文件（retrieve_exemplars.py 调用协议），四 SKILL.md 各留 3 行差异项（section 名 / learning block 路径 / 触发时机） | 调用参数与跳过条件必须在协议文件完整保留 |
| A2 | intro L92 尾半句+L104、theory L113、theory output-format.md L89 | 润色纪律句 4 处同义复述；_polish-protocol 自称单一事实源 | 各留一句指针 | — |
| A3 | intro 纪律节（4 bullet）+ theory 批评登记（9 行） | 核心规则逐字同构（revise/reject+1、去重首插 8 条） | 各压 ≤3 行 bullet；theory 差异项"只登记变体产出质量"保留 | 见 G3：critique.per_file 至今为 null，机制零使用 |
| A4 | intro L104、theory L122-124 | 原文锚点规则复述（_polish-protocol 已载全文） | 删复述留指针 | — |
| A5 | intro L79、theory L27 + _polish-protocol + _argument-grammar | "语料优先改编/角色先于风格"四重表述（含 2026-09-06 新增条款） | SKILL.md 各压一句指向 _argument-grammar + _polish-protocol | — |
| A6 | theory L136-138 | Evidence-driven evolution 门控复述（design-feedback-loop.md 已载全文） | 留指针，删"授权/风险/双回归"复述 | — |
| A7 | methods SKILL.md L127-135 词汇表、results SKILL.md L119、results claim-calibration 互指行、双方 post-generation-checklist/anti-patterns 各一行 | 因果语言强制词汇表 **≥5 处**复述 | 正典唯一化：`write-methods/corpus/micro-templates/causal-hedging.md`（151 行最全，intro 两处已指它）为单一源；各处留一行指针 | causal-hedging.md 本体禁动（多技能单一源） |
| A8 | methods/references/paper-state-schema.md（复制品）、results/references/paper-state-schema.md（58 行） | 复述 paper-state-protocol v1.2.0 schema | 改为指针 + 本技能特有字段说明；输出合同字段名保留 | 字段/CLI 签名勿改（results 护栏④） |

## B. write-theory SKILL.md（P0 缩行 / P1 职责）

| ID | 位置 | 现状 | 处置 | 护栏 |
|----|------|------|------|------|
| B1 | Hard constraints #11 / #16 行内 | cue-activation carve-out 与 Incommensurability 两阶段门控的例外全文在行内，所指文件（bilateral_argumentation_templates / incommensurability-resolution-routes）已载全文 | 行内各缩一句，例外下沉 | 所指文件确已载全文（agent 已核对） |
| B2 | #1 / #8 / #15 | 环节计数、Closure 例外、conditionality 细则与所指文件三处重复 | 行内缩为一句 | — |
| B3 | #5（主角≤3）、#13 后半（Lit Support=argument 总结） | "细则位置"列自认审查侧；theory-review Step1/Step2 已覆盖 | 生成侧留一行+审查侧标注（AUDIT-IN-WRITER） | — |
| B4 | Selection rules（9 条英文） | B0/B1、conditionality、Incommensurability 判断在 routing_table / phase-3 / routes 文件已有第二三份 | 每条压"变体名+一句触发"；判断细则唯一源 = routing_table | routing_table 确含全部判据（已核对） |
| B5 | 反模式速查（8 行） | 与 corpus/_index.md 反模式节全量对应；Workflow step1 已强制读 _index | 压 3 行高频 + 指针 | — |
| B6 | Resource loading 元解释段 | "本节是加载总则……两者一致"纯自我关系说明（NO-OP 引文在案）；其余句与 Workflow step1 重复 | 删元解释段，整节缩两行 | — |
| B7 | phase-3-hypothesis-derivation.md 段落 QC 表 | 末 5 项复述 reasoning_soundness_protocol §1/3/4/5/7；前 8 项与 paragraph_layout §3 十二项重叠 | QC 表压成两个指针；soundness 双份 checklist 留 phase-4 复核版 | — |
| B8 | — | **不剪**：Incommensurability / conditionality / figure-path / storyline_id 类条目（theory-review 不查，生成侧必须自持） | KEEP | — |

## C. write-introduction SKILL.md（P0/P1）

| ID | 位置 | 现状 | 处置 | 档位 |
|----|------|------|------|------|
| C1 | Phase 4 Gate 2 JTBD 六模块表 | 与 intro-review Step 1 JTBD 表几乎同表（同 6 block 同判据） | 推荐降级为"渲染自检一行 + 审查归 intro-review"（表对渲染时 utility 排序仍有引导，不整删） | P1 |
| C2 | Phase 2 第 6 条异议预判 vs quality-gates §4 | 同一含义两处展开（2026-09-06 新增） | Phase 2 条压一行（生成时机+指针 §4） | P0 |
| C3 | Phase 0 门控矩阵内联 | theory 已走 intake-and-story-gate.md 下沉模式（省 4 行），intro 全内联 | 可选同模式下沉；**前置条件 = C4** | P1 |
| C4 | 两技能 stage 词表 | **语义分歧 bug**：intro preparing=只出骨架，theory preparing=diagnosis only；intro 用 provisional，theory 用 blocking | 统一为 paper-state-protocol 词表（先裁定词表归属），再做 C3 | P1（先办） |
| C5 | L79"已核实事实与用户裁定优先"、L90 分工元话语 | no-op 嫌疑（成本低） | 待定/压缩 | P2 |
| C6 | anti-patterns 21 条生成期逐条扫描 | 长尾反模式稀释生成注意力 | 生成期保留 5 条高频（稻草人/弱缺口/缺 Stakes/过度承诺/未回应显见异议），其余归 intro-review 扫描 | P1 |

## H. write-methods（SKILL.md 182 行，四件套最大）

| ID | 位置 | 现状 | 处置 | 档位 |
|----|------|------|------|------|
| H1 | L105-113 即时范文学习对象 | 与 theory 版 ≈90% 同文 | 并入 A1 四技能批次 | P0 |
| H2 | L127-135 因果语言强制词汇表 | 整表复述 causal-hedging.md（151 行更全） | 并入 A7 | P0 |
| H3 | L64-79 槽位目录表 + L86-99 路由加载表 | SKILL.md 内部二表 80% 重合，且复述 slot 文件头 | 合一（文件列+加载时机+输出形式），砍输出形式列 | P0 |
| H4 | Phase -1（L33-43）复述 draft-revision-protocol、使用反馈闭环（L156-162）复述 feedback-protocol、纪律段（L171-179）复述 boundaries 第6/7/8条 | 协议层复述 | 各留 2-3 行硬规则 + 指针 | P0 |
| H5 | paper-state-schema.md | schema 复制品 | 并入 A8 | P0 |
| H6 | 前置检查 L27-31、Role 元解释 L11、纪律段同句重复两遍（L175≈L177）、6 处完成判据多为前文重述 | NO-OP | 删/缩 | P0 |
| H7 | validation-protocol.md Gate2/5 | 与 robustness-menu / post-generation-checklist 重复 | 合并进 checklist | P1 |
| H8 | methods-review 承接边界 | 三C（样本漏斗/变量操作化/控制逻辑/分析方法）review 已覆盖；**行为/契约项 review 不查**（越级动词合规、Methods–Results 边界与稳健性归属、placeholder/机构名残留、语态纪律、revision 约束、M2.5/M7/M9 槽位结构、Bad Control） | post-generation-checklist 与三C去重后保留；行为型项留 writer，三C 项标注"审查侧 methods-review" | P1 |
| H9 | SKILL.md 23 设计类型清单 | STALE：漏列 结构需求-state-space（INDEX 已有 6 变体） | 删清单改指 corpus/INDEX.md | P0 |
| H10 | REVERSE-VALIDATION-GUARDED | slot-M*.md 命名（M2_5 / M7-supplement 正则解析）、"**通用填空段落**:"+fenced 代码块格式（无代码块的"待补"变体会被静默漏解析）、design_type_map.json 硬编码中文设计类型名 | **冻结**：改名/改格式/改设计类型名前必须先跑反向验证；corpus/[设计类型].md 与 micro-templates 管线不读（自由度高，但跨技能入站密集——write-intro/results/theory/distill 多处指入），只增不删 | 护栏 |

## I. write-results（SKILL.md 162 行）

| ID | 位置 | 现状 | 处置 | 档位 |
|----|------|------|------|------|
| I1 | L98-106 即时范文学习对象 | 与 intro/theory 同构 ≈95% | 并入 A1 | P0 |
| I2 | L47-51 前置检查节 | 逐字复述 Phase -1 完成判据与 Phase 0 | 整节删（NO-OP） | P0 |
| I3 | L63-73 与 L80-91 双 R1-R9 表 | SKILL.md 内部二表 80% 重合（注：R1-R9 定义未在 SKILL/corpus 两处重复，此项干净） | 合并为单表 | P0 |
| I4 | L119 因果词汇表 | ≥5 处复述之一 | 并入 A7 | P0 |
| I5 | L155 诚实边界摘要 | 逐字复述 boundaries.md 第3/6/7/8/9条（该文件 86 入站引用，全体系最高——本体禁动） | 压为指针+一句"设计排他性与非显著报告不可违反" | P0 |
| I6 | L21 优先级阶梯 | 与 draft-revision-protocol §1 七级源层次同构 | SKILL.md 留指针 | P0 |
| I7 | references/example-skeleton.md | 与 slot-R2/R3/R4/R9 通用段落 70%+ 逐字重合（历史下沉遗留） | 删或缩为"见 slot-R*"一行 | P1 |
| I8 | references/output-metadata-template.md | 首行自注"已废弃"，正文仍留整套 JSON | 删（入站仅 governance 1 处） | P1 |
| I9 | corpus/_pilot_r2_index.yaml | STALE：sha256 钉在 OLS-FE 旧版、expected 46 变体现为 85，试点未毕业 | 与治理方确认后删除或重钉 | P2 |
| I10 | story-resolution.md vs hypothesis-fulfillment-map.md | 判据词表（stable/qualified/mixed/unresolved）70% 重合 | 留 fulfillment-map（有外部消费）；story-resolution 缩为 storyline 映射表+指针 | P1 |
| I11 | corpus/_evidence_registry.yaml meta 悬空指针 | 指"write-results SKILL.md 批评登记"节——**不存在**；distill-results-exemplar selection-gate 依赖该登记 | SKILL.md L139-145 补分工声明（feedback-registry=修订规则 / corpus registry=语料精炼信号），修复悬空名；results 反馈双件套含 supersedes 厚于 intro/theory 版，**不**并入 A3 批次 | P0（bug 修复） |
| I12 | L45 调用方式 19 类型枚举（与 design-branches、INDEX 三处枚举）、L162 脚注与 Role 重复 | 弱重复 | 留 3 例+指针；删脚注 | P0 |
| I13 | results-review 承接边界 | review 不查双层 verdict、claim-calibration L 层匹配、Yuan 六维、Booth 证据五问/视觉证据、语言锁与 active rules 回归 | post-generation-checklist / anti-patterns / claim-calibration / validation-protocol 属**承重件不可外推** | 护栏 |
| I14 | REVERSE-VALIDATION-GUARDED | slot-R1..R9 文件名与 9 槽数量（解析器 glob+计数）、INDEX.md 变体数同步契约（distill Phase 4）、_evidence_registry schema/usage_stats（selection-gate 消费）、CLI 参数签名 | **冻结** | 护栏 |

## D. 审查职责再分配（P1，双向原则）

- **D1 移出（writer→review）**：JTBD 表（C1）、theory #5/#13b（B3）、反模式长尾（C6）、phase-3 QC 前八项复述（B7）。
- **D2 反向补强（先立岗再拆防）**：intro-review 目前**不查**首尾句/异议预判/论证文法五问/claim_fit 三扩展/能量阶梯。**每剪一道 writer 侧防线，必须先把对应检查加进 review 侧**，否则失防。theory 侧同理核对 conditionality/figure-path（当前 review 不查，故 B8 留守）。
- **D3 留守生成侧**：paper-state 片段正确性、EMERGING 标注、evidence placeholder（review 不查，属生成合同）。

## E. 孤儿与登记缺口

| ID | 对象 | 现状 | 处置 | 档位 |
|----|------|------|------|------|
| E1 | write-theory/corpus/storytelling/_index.md | 零入站引用（4 个 storytelling 文件由 phase-1 直接指名加载） | 删除候选；删前全库 grep 二次验证 | P1 |
| E2 | corpus/subprotocols/process_transition_operators.md | D 型硬加载但未入 _index 子协议表、未入 registry | **补录**（不是删） | P0 |
| E3 | product_safety_construct_lexicon.md | 领域专属（产品召回）语料，疑似项目残留 | 核实后移出 corpus 归项目目录 | P2 |
| E4 | methods corpus/_slot_micro_template_bindings.yaml + validate_bindings.py | 全库零外部引用（仅互引，SKILL.md 也不提）——真孤儿对 | 确认蒸馏 writeback 历史用途后删 | P1 |
| E5 | results output-metadata-template.md（自注已废弃）、example-skeleton.md（与 slot 70% 重合） | STALE/DUPLICATION | 删除（见 I7/I8） | P1 |
| E6 | empirical-writeup / empirical-pipeline-stata 引用技能名 `write-methods-and-results` | **不存在的技能名**——对方侧 stale 指针 | 修对方指针为 write-methods / write-results | P0（bug） |

## F. 不剪清单（护栏）

1. 立场 4 条（intro L11-16）——全篇取向的 leading words。
2. Phase 2 路由/开篇功能合同/能量阶梯——gap→结构映射是核心资产。
3. Phase 3 模块→corpus 指针表——无表则 114 个语料文件不可导航。
4. 输出合同、paper-state-schema——下游技能显式消费。
5. Hard constraints 表结构——只缩行，不拆表。
6. Gate 3 首尾句 / Gate 4 异议预判 / Gate 5 论证文法——review 未立岗前不动（走 D2 流程）。
7. 全部语料文件本体——按需加载，非常驻成本。
8. _argument-grammar、语料角色标注、reasoning_soundness_protocol、paragraph_layout——承重新层。
9. journal-fit、intake-and-story-gate 等 11–39 行薄文件——薄而必要。
10. **反向验证护栏全集**（methods/results）：slot-*.md 文件命名与格式（通用填空段落标记+fenced 代码块）、design_type_map.json 类型名、_evidence_registry schema/usage_stats、INDEX 变体数同步契约、CLI 参数签名——动前动后各跑一次 reverse_validation_pipeline。
11. causal-hedging.md（多技能单一源）、boundaries.md（86 入站引用）——本体禁动，只删他处复述。
12. results feedback 双件套（feedback-protocol + registry.json）与 hypothesis-fulfillment-map.md——有外部消费与 distill 依赖，不并入压缩批次。

## G. 数据淘汰流程（P2）

0. **前置（methods/results 专属）**：任何触碰 slot 文件、设计类型名、registry/INDEX 的 P0/P1 项，执行前后各跑一次 `reverse_validation_pipeline`（槽位解析 X/9、X/10 覆盖报告不变才可落盘）。
1. 选 2–3 篇真实在写论文（建议含 1 篇 Incommensurability 路线）跑 write→review 全链路。
2. 逐 gate 记录：触发次数 / 抓到问题数 / 修复动作 → 回填 `_skill_design_feedback.yaml`（通道活跃，已有 141 条）。
3. 一轮后淘汰零触发零拦截的 gate；同时裁决批评登记机制去留（critique.per_file 仍为 null 则降级为 review 侧动作）。
4. 顺带验证：Phase 1.5 范文命中率、vault 检索失败率、Gate 4/5 的实际拦截率。

## 执行日志

**2026-09-06 P1 已执行完毕**（B3/B4/B5、C1/C3/C4/C6、D 标注、E1/E4/E5）：

- **C4 词表统一**：intro 是四件套中唯一偏离 stage-gates 权威词表的技能（把 preparing 用成了出骨架）——已对齐：`preparing`=只做诊断、`blocking`=可出占位符骨架、`refining/finishing`=confirmed+Intro 附加门；权威源 = `../paper-story-contract/references/stage-gates.md`。润色行的"preparing 跳过"同步改为"blocking 只出骨架时跳过"。
- **C3 门控下沉**：新建 `write-introduction/references/intake-and-story-gate.md`（模式/Story Intake/阶段行为表/local bypass），SKILL.md Phase 0 保留 5 行概述。
- **B3**：theory #13 补审查侧标注（theory-review Step 2）；#5 原已标注。
- **B4**：Selection rules 9 条压为变体名+一句触发，判断细则唯一源 = routing_table（B0/B1、conditionality、R1–R4、"对立机制≠U/倒U"均已核实在该表）；E 型 within/cross-level 细则指向 E_moderation.md。
- **B5**：反模式速查 8 行→3 行高频+指针（8 条已逐一核实 _index 反模式速查全有对应）。
- **C1**：quality-gates Gate 2 加审查归属注（正式审计归 intro-review Step 1 + deep L4，本表为渲染自检对照）。
- **C6**：anti-patterns.md 重构为两档——§1 生成期高频 5 项（稻草人/弱缺口/缺 Stakes/过度承诺/未回应显见异议）、§2 长尾 16 项；**D2 先立岗**：intro-review Step 2 新增"反模式长尾扫描"承接 §2；SKILL.md Phase 4 同步。
- **E1**：theory storytelling/_index.md 删除（grep 零入站）。**E4**：methods _slot_micro_template_bindings.yaml + validate_bindings.py 删除（writeback 脚本零引用，纯自包含 QA 对）。**E5**：results output-metadata-template.md（自注已废弃）+ example-skeleton.md（与 slot 70% 重合）删除；SKILL.md 输出合同改为"slot-R* 为正典"。注：validate_write_results.py 的 FORBIDDEN 清单本就含 output-metadata-template（防复活守卫），删除与校验器意图一致。
- 实测：SKILL.md 四件套 506 → 504 行（P1 以职责再分配与单一事实源为主，行数收益小）；**references 净删 5 个文件**（~1050 行 on-demand 层）；validate_write_methods/results 复跑双 PASSED；已删文件零悬空引用。
- **遗留**：`write-discussion-and-conclusion`（不存在的技能名）仍在 empirical-writeup SKILL L19 与 writeup-matrix L8 被引用——Discussion 路由（discussion-review vs 未来 write-discussion）待用户裁定后修。

**2026-09-06 P0 已执行完毕**（A1–A8、B1/B2/B6/B7、C2、H1–H6/H9、I1–I6/I11/I12、E2(_index 部分)/E6）：

- 实测：四 SKILL.md 595 → 506 行（intro 107→102 / theory 144→126 / methods 182→138 / results 162→140，-89 ≈ 15%）；phase-3 -11 行；`validate_write_methods.py` 与 `validate_write_results.py` 双双 PASSED；slot 文件与 design_type_map/registry schema 零改动（G0 未触发，mtime 核验）。
- 新建：`story-blueprints/v4/rhetoric-moves/_immediate-exemplar-protocol.md`（四节共用协议）。
- **偏差记录**：① A8 降级——两份 paper-state-schema.md 实为技能专属输出片段模板（字段=输出合同），非协议复制品；改为补权威 schema 指针，内容保留。② E2 的 registry 补录缓办——process_transition_operators 无蒸馏来源可溯源，待 D 型蒸馏时由写回器首登记；`corpus/_index.md` D 型行已补录。③ I12 的版本脚注保留（Yuan 框架溯源，1 行成本）。④ A2 中 theory output-format 的润色纪律句压缩为指针。
- **待办**：P1（B3/B4/B5、C1/C3/C6、D 职责再分配、E1/E4/E5 删除项）待用户逐项裁定；C4 词表统一需先拍板以 paper-state-protocol 为准；P2 待真实草稿数据。

## 预期收益

- theory SKILL.md 144 → ~105 行（-35~40）；intro SKILL.md 107 → ~90 行（-15~20）；**methods SKILL.md 182 → ~125 行（-50~57）；results SKILL.md 162 → ~115 行（-45~47）**；phase-3 约 -30 行。
- 四技能生成期常驻上下文合计净减 **~150 行（约 25%）**，零行为损失（P0 项）。
- references 净删 3–4 个文件（methods bindings 孤儿对、results output-metadata-template、example-skeleton），缩 3–4 个（story-resolution、validation-protocol、paper-state-schema ×2）。
- 修复 3 个 bug：两技能 stage 词表语义分歧（C4）、results corpus registry 悬空指针（I11）、empirical-writeup/pipeline-stata 的不存在技能名（E6）。
- P1 项完成后，write-* 与 review 栈职责边界清晰：write 管生成形状，review 管合规；methods/results 因 review 侧承接面窄，writer 侧保留的合规件多于 intro/theory（H8/I13 已划界）。
