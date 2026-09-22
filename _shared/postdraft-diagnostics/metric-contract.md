# Metric Contract v1 — Post-Draft Claim–Design Mismatch Diagnostics

**status**: frozen for pilot (Step 2–3) · v1.0.0 · 2026-09-20
**owner**: 写作侧诊断层（write-* 家族共用）
**wordlists**: [wordlists-v1.json](wordlists-v1.json)（机器可读，同版本冻结）

---

## 1. 范围与定位

诊断**草稿中因果语言强度与设计证据强度错配**的句子。它是一个 post-draft 异常诊断层，不是评分器，不是门禁。

- **诊断对象**：write-* 出稿或真实论文草稿的 Results / Methods(M7–M8) / Discussion 主段。
- **不做**：句子改写、自动回写、质量总分、通过/失败判定、AI 概率估计。
- **与 pass-contract 的关系**：明确不接 `_shared/pass-contract.md`（六字段审查契约属于另一层）。本层输出仅作为观察项供人裁决。

## 2. 输入

| 输入 | 来源 | 说明 |
|---|---|---|
| 草稿文本 | 调用方 | 按 section 标注的段落-句子序列（用与句档相同的切句器） |
| 设计元数据 | 调用方从 Design Packet / Analysis Manifest 提供 | `--design <family>`（七族之一）；v1 不自动猜测设计 |
| 识别诊断状态 | 草稿内检索 | identification_markers 命中与否（不验证诊断质量，只看是否报告过） |

设计族七类：`ols_fe_panel_hlm` / `did_natural_experiment` / `iv_2sls` / `nonlinear` / `survival` / `experiment` / `unknown`。设计族与 write-methods corpus 设计类型的映射见 wordlists `design_allowance.label`。

## 3. 判定流程（每句）

```
1. 假设句？→ hypothesis_markers 命中 → 豁免（假设不是 claim）
2. 提取动词档位：T_ASSOC / T_DIRECTIONAL / T_CAUSAL_EFFECT / T_MECHANISM / T_DEFINITIVE
3. 取该 section × design family 的允许/条件/禁止表
4. 档位 ∈ forbidden → OVERCLAIM
   档位 ∈ conditional 且草稿内无对应 identification_markers → CONDITION_MISSING + OVERCLAIM
5. Results 主效应句：tentative 弱化命中且句中含已验证主效应语境 → UNDERCLAIM
   （claim-calibration「勿过度回缩」条款：设计直接检验/替代解释已处理/L 层匹配时不弱化）
6. Discussion 机制外推句：无 tentative 修饰的 T_MECHANISM/T_DEFINITIVE → OVERCLAIM(discussion)
```

每条 flag 附：句子原文、位置（节/段/句序）、档位判定、设计允许档、依据规则（词表条目或条款 id）、修改**方向**（非改写文本）。

## 4. 词表与规则来源

- `write-methods/corpus/micro-templates/causal-hedging.md` — 设计家族动词表（允许/禁止/条件）
- `write-results/references/claim-calibration.md` — Claim Ladder（L1–L7）、过度声明动词表、勿过度回缩五条件
- 试探性表达（Discussion/Theory 合法档）与 hedging-strength.md 的极弱/弱档一致（Morley Phrasebank 07，source_tier: auxiliary——被顶刊蒸馏覆盖时按其退役规则更新）

## 5. 参考模式（reference modes）

- **house_style**：rhetoric-moves 批句档锚定集（Gulati/Westphal 系；批跑后键名以 `_backfill_manifest_2026-09-20.json` 的 key_equivalences 为准）。
- **field_norm**：现有 124 句档仅作**观察性参考**。不构成规范性基准；规范性使用前须完成 section×design 分层覆盖率审计（每 cell n≥5）。n<5 的 cell 只报 insufficient reference coverage。
- v1 的判定是规则型（词表×条件矩阵），不依赖分布基线；分布型指标全部推迟（§7）。

## 6. 禁止清单（硬约束）

1. 无综合分数
2. 无 pass/fail 门禁
3. 不自动改写
4. 不自动回写 corpus / feedback-registry
5. 不做 AI 概率包装
6. n<5 参考格只报 insufficient coverage，不报 percentile

## 7. v1 明确不做（推迟到 v2）

- 句长极端异常定位（p10/p50/p90）
- eligible-unit rationale coverage（because/as/since/given）
- hedge 强度错配与堆叠

推迟原因：分布型指标依赖 field_norm 覆盖率审计，且句长指标需对句档来源重切（preprocess 历史切句偏差已在 2026-09-20 修复，但 per-section 基线尚未建立）。

## 8. 试点判据（分阶段口径，v1.2.3 起生效；替代原「12 份盲审」单一口径）

单位说明：阶段③的单位是「节/版本」（一次 Results/Methods/Discussion 修订即一个使用事件），不是项目；不设最低草稿数量门槛。

| 阶段 | 判据 | 状态与实测 |
|---|---|---|
| ① 负对照（范文地板） | 已发表顶刊范文 flag 密度收敛到噪声地板，每条残差可归类 | ✅ 完成：Results 专项 1.49/千句（8 条残差全部归类），全量 2.1/千句 |
| ② 违规探针（合成变异） | recall ≥ 0.80；对照孪生 0 污染；PASS 期望探针零误报 | ✅ 完成：56 探针裁定后 recall 41/42=0.976（唯一 miss 为已接受的跨句语境限制），0 污染，PASS 特异度 4/4 |
| ③ 机会主义真实使用（每次写/改 Results、Methods M7-M8、Discussion 顺手跑 shadow） | 裁定一致性：每条 flag 人工裁定，误报→守卫修复后地板回归；行为判据：不诱导观察性设计升级因果主张（0 例）；审稿人出现机械迎合信号即停 | 🔄 进行中：使用事件 1 次（共同所有权×产品召回），2 条 flag 均误报并已修复，人工反查确认非漏检 |
| ④ 升级判定（长期） | 累计 ≥ 50 条真实裁定后查：precision ≥ 0.85；≥ 25% 使用事件发生作者认可的具体修改；每篇复核 ≤ 10 分钟 | ⏳ 未达标（累计裁定 2/50） |

停止判据（任何阶段生效）：审稿人（或 write-* 出稿）出现机械迎合行为信号（缩句/补 because/堆 hedge 换「像范文」）即停，回炉契约。地板警戒线：Results 密度回升超 3.0（误报回归）或全量低于 1.0（过度抑制）。

## 9. 变更控制

- 契约与词表同版本冻结；任何修改升版本号，旧版 supersede 记录在案（Decision Register）。
- 词表变更依据只能来自：(a) 范文语料证据（corpus 变体新增）；(b) 试点盲审 precision/recall 数据；(c) 用户裁定。不接受从通用去 AI 清单导入（registry 规则 wmf_b8fd3ab66c50541c）。
- **誊录保真修订（2026-09-20，Step 2 验证中发现，不升版本）**：① T_CAUSAL_EFFECT `affects` → `affects?`（单复数誊录遗漏）；② T_ASSOC 补 `predicts?`（causal-hedging OLS 允许组原有，v1 提取时漏录）；③ 结果标记补 `p < 0.01` 型模式。三处均为对已引源的忠实还原，非语义变更；回归 fixture 见 `tests/README.md`。
- **v1.2.3（2026-09-20，recall 探针阶段②完成 + 大小写缺陷族修复）**：探针集 56 个（七类变异 × 对照孪生，`tests/probe_gen.py` + `tests/probe_run.py`），首轮裁定 10 条变异未制造真违规（NOT_A_VIOLATION，留痕于 manifest）；真缺陷修复：STAT_HARD/UNDERCLAIM 前件大小写不敏感（Table/Column 大写形态此前逃逸，与 v1.2.1 cond_ok 同族第二例）、STAT_HARD += standard deviation(s)、ECON_DIAGNOSTIC += mis-specif（7 篇范文先例）。实绩：recall 0.976（唯一 miss = 跨句语境，v1 接受的限制）、PASS 特异度 4/4、改判一致性 10/10、0 污染。地板精确回基：Results 8/5381=1.49，全量 20/9432=2.1，synth 4/2/4。探针设计语义注记：M3（we reveal）与 M4（modal 剥离）变异在 124 范文实测中零自然出现，探针仅验证工具响应性，不代表范文分布。用户授权契约文本决策权（m01277），试点判据改为分阶段口径（见 §8）。
- **v1.2.2（2026-09-20，首次真实草稿使用事件）**：共同所有权×产品召回项目三份未打磨稿（Results 87 句 / Methods 6 句 / Introduction 范围外）。首跑 2 flag → 全部裁定为守卫覆盖型误报 → 修复（bootstrap produces a similar result；root cause 空格版）。人工反查全稿因果句确认 0 flag 为真实结论而非漏检：作者 Results 主张校准已达范文地板水平。地板无回归（Results 1.5 / 全量 2.1 / synth 4-2-4）。阶段③累计：1 次使用事件，2 条裁定，精度改进闭环首跑。
- **v1.2.1（2026-09-20，Results 专项地板校准，R7-R9 三轮）**：用户裁定 Results/Methods 高度模板化、优先专项对照校准（m01034）。91 篇 × 5381 results 句负对照 18.9→10.8→5.9→**1.5 flag/千句**；全量 41 篇地板稳定 2.2；synth 回归 4/2/4 恒稳。关键修复：hypothesis 单复数拼写缺陷（`hypotheses?` 从未匹配过单数，正则排写错误）；cond_ok 大小写不敏感；数字-单位窗口 `[^.]`→`[^;]`（小数点阻断单位匹配）；条件档补充 modal_guard 抑制；新增 15+ 语义守卫（RIVAL_EXPL/GIVEN_PREMISE/ROBUST_TO/CONSTRUCT_DEF/EXAMINE_WHETHER/引号-斜体-数学环境位置判定等）。残差 8 条全部分类为 X（历史事实）/S（切句伪影）/L（理论散文）/P（人工复核级），不再追求归零。基线 fixture：`tests/floor_results_v1.2.1_results.json`；判读警戒：Results 密度回升超 3.0 或全量低于 1.0（过度抑制）。
- **v1.1（2026-09-20，Step 2.5 地板测试第一轮裁定）**：tentative 删 `consistent with`（范文通用短语）；identification_markers 9→16（+hansen j/sargan/overidentif/durbin-wu/endogeneity test|concern/control function/granger）；T_DEFINITIVE causes 加 granger- 与 root- 排除；ols_fe/nonlinear 的 T_DIRECTIONAL 由 forbidden 改 conditional（范文证伪原设）；切句器修 roman-numeral 标题归档。
- **v1.2.0（2026-09-20，Step 2.5 地板测试五轮裁定后冻结）**：负对照 41 篇范文 9,350 句，flag 密度 21.8→2.9/千句。修订全部以具体范文句为锚：① 名词用法护栏（causes/drives 后接 of|for|underlying|behind|and effect、increases|decreases 后接 in、prove oneself）；② T_MECHANISM 收窄（删裸名词 `the mechanism`；`works by` 限 process/mechanism/channel/effect 主语）；③ 护栏族新增：文献综述句（literature has shown/prior studies have/papers have argued）、not consistent with the view that（被驳主张）、非显著语境（insignificant/nonsignificant——非显著句必须 hedge，UNDERCLAIM 不罚）、methods 程序动词（response bias/measurement error）、统计量随附的 caused/led to（事件研究惯例）；④ RESULT_MARKERS 补 results/findings 动词形态（含副词间隔与三单）；⑤ discussion 举报句豁免（we found/our finding/the effect was mediated）；⑥ 假设句 predict(ed/ing)。残差 27 条四类：历史/制度事实句、文献/理论散文、切句/表注伪影、体裁惯例（SEM 论 moderation/mediation）——句级正则不可再分，属噪声地板，由 Step 3 人工裁定消化。证据：`tests/floor_test_v1.2.0_results.json`。
- v2 启动条件：field_norm 覆盖率审计完成 + 试点判据通过。
