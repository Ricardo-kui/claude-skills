# L1 子代理分发协议（2026-08-22 起）

L1 的四个分节蒸馏在**子代理**里跑，主循环只收紧凑摘要。分节 skill 的 phase 参考
文件（7–24KB/个 × 5–7 个）、语料索引与切片只进子代理上下文；主上下文只背 SKILL.md +
PDM + 各节摘要，实测可降主上下文 fresh input 约 60%（此前四节全部载荷累积在同一窗口，
cache_read 是 fresh input 的 3.5 倍）。

## 子代理提示词模板

```
<skill 名> <切片路径> --output-format=json --pdm <pdm路径>
按该 skill 的 phase 流程蒸馏。输出契约：
1. 把 section JSON 写入 <pdm>/sections/<section>.json，feedback 写入
   <pdm>/feedback/<section>.feedback.yaml（skill 无该基础设施时注明缺失）
2. 写回候选停在 writeback plan 产出。plan 条目必须是执行器 v2 schema：
   items: 下每项含 name / dedup.verdict / anchor.file / block_text（全文内嵌，
   {NEXT} 作变体号占位）/ index_note（带 {NEXT}）。缺 block_text 或 index_note
   的条目在子代理内自查补齐后再返回——主循环不返工。
   **子代理一律不得运行 corpus_writeback.py**（写回权收归主循环；gate ① 批量
   呈审或已授权的 --auto-write 直写均由主循环执行）
3. 最终回复只允许 ≤20 行紧凑摘要：
   - identity: gap_type / theory_building_type / design_family / estimator_family
   - band: gap|薄弱|quiet + 一句依据
   - writeback_candidates: 每个候选一行（action + target + 变体名）
   - feedback_path / section_json_path
   - 任何 flag
不得把 phase 报告全文、DNA profile 或语料文件内容贴进回复。
```

固化依据（2026-08-29 五连跑教训）：discipline 2 的前半句根治
"plan 到达主循环才发现无 block_text → 全 SKIP → SendMessage 重发"的返工环
（每次 5–10 分钟）；后半句根治"残项手补子代理为验证而重跑写回器 → 12 块
重复插入"的事故。

各工具的子代理机制：

| 工具 | 分发机制 |
|---|---|
| Claude Code | `Task` 工具（subagent_type: general-purpose），prompt 用上方模板 |
| Codex / Kimi Code | 各节 `agents/openai.yaml` 定义的子代理（default_prompt 已含 PDM 输出契约） |
| Cursor / Zcode | 按其各自的子代理/task 机制，prompt 用上方模板 |

## 主循环纪律

- 主循环**只读**：PDM 根文件、各节 `sections/<section>.json`、子代理的 ≤20 行摘要。
- **验收以盘面为准（2026-09-12 固化）**：子代理是否完成只按盘面产物判定——`sections/<section>.json` 存在且非空、`identity` 字段齐、`feedback/<section>.feedback.yaml` 在（无该基础设施时见其注明）、写回候选停在 plan。≤20 行摘要只用于汇报与合并，**不作为完成依据**；摘要与盘面冲突时以盘面为准（runbook 教训：`_meta` 谎报 produced 不可信）。
- **失败必须显式记录**：子代理死亡 / 超时 / 产物缺失一律视为该节未完成，在 PDM 注明根因一行并在最终报告呈报；主循环不得代其宣布 verified，也不得静默跳过（判定失败绝不当作可以停止）。
- 读 `sections/<section>.json` 时校验 `identity` 字段非空；空或缺文件 → 该节视为未完成，只重发该节（不整链路重跑）。
- 主循环**不得打开**：任何分节 skill 的 references/、protocols/、语料索引
  （_index / INDEX / _evidence_registry / routing 表）、论文切片——这些只在子代理里读。
- 合并：每节完成后主循环把摘要中的 identity/band 写入 PDM 该节条目、更新 `status`；
  JSON 文件由子代理写入，主循环不代写。
- **写回执行输出纪律（2026-09-13，Lu 跑）**：`corpus_writeback.py --apply` 每份 plan
  只调用**一次**，输出 `tee <plan>.apply.log` 后再检查——两次调用（一数数一抓错）曾把
  apply#1 的启动失败与 apply#2 的静默全量完成混成一个"计数 0 但盘面全对"的谜团；
  成败判定以盘面 + verify_writeback 为准，不以输出计数为准。
- 中断续跑：以 PDM 各节 `status` 为断点，只重发未完成节，不整链路重跑。

## JSON 修复路径（不重发原文，2026-09-12）

`sections/<section>.json` 存在但 `json.loads` 失败、或 identity 字段缺失/为空时，先走修复
而非整节重发：派一个最小修复子代理，prompt 只含 (a) 损坏文件的完整原文（通常几十 KB，
远小于切片），(b) 精确的解析/校验错误清单，(c) 指令——只修 JSON 语法与字段结构，不改任何
蒸馏内容、不新增语义，**禁止重读切片/语料/参考文件**；修复后写回同一路径并回传 ≤5 行确认。
修复子代理同样不得运行 corpus_writeback.py。仅当文件整体缺失或内容实质错误（identity 与
盘面/切片明显矛盾）时才按重试上限整节重发。固化依据：pi-distill repairer 契约（修复只带
坏响应+校验错误，不重发工具输出）——一次修复远省于整节重发（约 0.5–1.5M tokens），且不产生
第二次蒸馏漂移。

## 节奏与限流

- **发射金丝雀（2026-09-13，Lu 跑后固化）**：任一波次并行发射前，先发射一个微型探针
  代理（prompt 仅"回复 OK 两字"）验证发射通道健康；探针失败（captcha verify failed /
  Model request failed 等瞬态家族）→ 当天该篇全程串行，不烧大发射（Lu 跑：首波 4M 级
  并行双败于发射层，浪费 ~25 分钟 + ~2M token + 一次用户体感故障；同日串行四连发零失败）。
  探针成功则按 2+2 正常并行。
- 默认 **2+2 波次并行**（2026-08-29 起，Fang 五连跑验证）：第一波 intro+theory
  （短切片）同时分发，完成后再发第二波 methods+results（长切片）。实测零限流，
  L1 总耗时 ~11 min（串行 ~25 min）。`--serial` 显式回退串行；**4 个全并行仍然禁止**
  （实测触发账户限流，整批作废重发，重试开销 30–40%）。
- 波次内两个子代理并行返回后，主循环合并 identity/band 再发下一波。
- **瞬态失败降级（2026-08-29 v2）**：Agent 发射报 `captcha verify failed` / `Model
  request failed` 等瞬态错误时——先等 20 秒查 PDM 盘面（防"后台实际完成"，见
  runbook 超时代理教训），确认无产物后**串行**逐个重发，不再并行重试（Anand 篇
  实测：2 并行双败、串行重发一次成功）。
- **重试上限（2026-09-12 固化）**：同一节累计重发 ≤2 次（含瞬态降级重发）；达上限即
  停止该节重发并在最终报告呈报根因与已有盘面（如有），由用户裁决是否续跑——不无限爬梯。
- 子代理内仍按分节 skill 自己的 phase 纪律按需加载参考文件（不预读全部 phase）。
- Windows 本机注意：脚本调用一律用 `py`，不用 `python`（WindowsApps 占位 stub）。

## plan 条目字段契约（执行器 v2，2026-08-29 固化）

- ADD/EXTEND：`name` / `dedup.verdict` / `anchor.file` / `block_text`（全文内嵌，
  `{NEXT}` 占位）/ `index_note`（带 `{NEXT}`）。
- **写回定锚纪律（2026-09-12）**：定锚前先跑
  `py ../distill-paper-exemplar/scripts/corpus_query.py outline --section <section> --file <目标相对路径>`
  取目标文件标题树（行号 + 全部层级标题）——`after_heading` 必须指向**主题匹配的既有标题**，
  禁止默认文件尾；目标文件标题族与其主流不同（如 E_moderation 用 `## EN.` 家族）时，
  block_text 标题与 index_note 直接写**显式已解析标号**（如 `## E13.`），不用 `{NEXT}`。
- **block_text 禁止预嵌 `<!-- wb:... -->` 标记**——执行器在块尾自动追加溯源标记，
  预嵌 = 同块双标记（verify V2 FAIL；2026-09-12 Ridge 跑 15 项全中，修复耗一轮主循环手术）。
- **registry 自动同步（2026-09-12）**：theory plan 项必须带 `registry_dimension`
  （Mechanism/Boundary/Constructs/Mode/Level/Question 之一）——执行器据此自动创建论文条目并追加
  tfr 片段（缺该字段的项仍落残项，手工同步是退路不是默认）；theory plan 顶层建议带
  `paper_meta: {title, year, theory_build_type}`（display_name/年份用，缺省回退 CLI
  `--paper-title/--paper-year`）；results 由执行器按 `rN_` 前缀自动追加估计器槽位
  skeleton_variants 与 batch_history；methods/intro 沿用 paper-append 路径（空壳条目现在会
  自动创建 papers 列表与 slots_covered）。
- **create_new_file**（gate ① 裁决新建 canonical 模块时）：上述字段 + `new_file`
  （相对 corpus_root 的新路径）/ `module_description`（1–2 句功能描述，进模块
  frontmatter 与功能描述节）/ `template_of`（可选，同语料 sibling 文件名，决定
  frontmatter 键序与分区结构）；执行器自动生成模块脚手架（变体 A、适用/禁忌
  从 block 字段提取）、加 _index 行、registry 留给残项同步 pass。
