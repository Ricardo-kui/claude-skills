# write-* 技能剪枝清单（2026-09-06，供裁决定夺）

> **目标**：技能可靠地把草稿送到 80 分，让作者的编辑杠杆最大化。
> **判定标准**：①生成期上下文最小化（SKILL.md 每次必载）；②审查职责归专职 review 技能；③no-op 删除；④单一事实源；⑤零触发机制待数据淘汰。
> **处置档位**：**P0** 安全剪（纯减常驻行数、零行为变化，可批量执行）｜**P1** 需逐项裁定（职责再分配/语义统一/删文件）｜**P2** 待数据（跑 2–3 篇真实草稿后回填）。
> **盘点来源**：双代理全量扫描 write-introduction（15 references/13 corpus 子目录/114 语料文件）与 write-theory（8 references/17 subprotocols/8 sentences/7 variants），全部指针实测无断链。

---

## A. 跨技能合并（P0，最大单笔收益）

| ID | 位置 | 现状 | 处置 | 护栏 |
|----|------|------|------|------|
| A1 | intro SKILL.md L39-48「Phase 1.5」+ theory SKILL.md L35-43「即时范文学习对象」 | 两段四步流程逐句同义（theory 自标"与 intro 同构"），常驻 ~17 行双份 | 下沉为 story-blueprints 侧单一协议文件（retrieve_exemplars.py 调用协议），两 SKILL.md 各留 3 行差异项（section 名 / learning block 路径 / 触发时机） | 调用参数与跳过条件必须在协议文件完整保留 |
| A2 | intro L92 尾半句+L104、theory L113、theory output-format.md L89 | 润色纪律句 4 处同义复述；_polish-protocol 自称单一事实源 | 各留一句指针 | — |
| A3 | intro 纪律节（4 bullet）+ theory 批评登记（9 行） | 核心规则逐字同构（revise/reject+1、去重首插 8 条） | 各压 ≤3 行 bullet；theory 差异项"只登记变体产出质量"保留 | 见 G3：critique.per_file 至今为 null，机制零使用 |
| A4 | intro L104、theory L122-124 | 原文锚点规则复述（_polish-protocol 已载全文） | 删复述留指针 | — |
| A5 | intro L79、theory L27 + _polish-protocol + _argument-grammar | "语料优先改编/角色先于风格"四重表述（含 2026-09-06 新增条款） | SKILL.md 各压一句指向 _argument-grammar + _polish-protocol | — |
| A6 | theory L136-138 | Evidence-driven evolution 门控复述（design-feedback-loop.md 已载全文） | 留指针，删"授权/风险/双回归"复述 | — |

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

## G. 数据淘汰流程（P2）

1. 选 2–3 篇真实在写论文（建议含 1 篇 Incommensurability 路线）跑 write→review 全链路。
2. 逐 gate 记录：触发次数 / 抓到问题数 / 修复动作 → 回填 `_skill_design_feedback.yaml`（通道活跃，已有 141 条）。
3. 一轮后淘汰零触发零拦截的 gate；同时裁决批评登记机制去留（critique.per_file 仍为 null 则降级为 review 侧动作）。
4. 顺带验证：Phase 1.5 范文命中率、vault 检索失败率、Gate 4/5 的实际拦截率。

## 预期收益

- theory SKILL.md 144 → ~105 行（-35~40）；intro SKILL.md 107 → ~90 行（-15~20）；phase-3 约 -30 行。
- 生成期常驻上下文净减 ~25%（P0 项），零行为损失。
- P1 项完成后，write-* 与 review 栈职责边界清晰：write 管生成形状，review 管合规。
