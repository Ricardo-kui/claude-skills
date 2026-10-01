# 写作期范本检索

逐句、逐段决定要完成的功能，再检索；输入研究内容，已知的设计/证据限制单独传入。保留各节原生分类，不用一个统一标签替代 Hook、A–G、M/R 槽位。

细功能先用一句话说明“当前句子要完成什么动作”，再填写内容与设计条件。`--list-functions` 的细功能包含定义、适用条件、相邻动作的区别、正例与误匹配例，并附权威卡片位置；检索结果的 `function_contract/function_contracts` 也返回这些判据。连续动作可在 `need` 中按“然后/随后/接着/→”表达，或按顺序填写 `actions`。只有宽功能能确定时保留宽查询，功能推断的不确定性在结果中单列。

细功能唯一维护在现有卡片源块的 `retrieval-move.definitions`，`catalog.function_definitions` 是可重建视图。`positive_example.kind/cue/why` 指向同块已有原句或模板的短锚点，不另存范文全文；`template` 正例只证明表达结构已有模板，完整原文仍缺时继续报告缺口。`mismatch_example` 明标 `illustrative`，用于判别动作，不当作论文摘录。新增动作定义不改变语料的 VERIFIED/EMERGING 状态。

首批覆盖文献解释缺口/解释冲突/共同前提、动机/局部链条/条件增强、三类稳健性、未支持裁决/解释限定/混合发现，以及首轮复核暴露的构念比较、注意力透镜、竞争预测、让步回应、完整机制和收益成本权衡。Methods 补样本连接、二元测量、组内变异限制和控制理由；连续动作检索另补“承认并定位内生性风险”和“移交具体缓解设计”，定义仍在现有 DiD 卡片，Heckman/IV 源块仅引用 ID。来源排序复核另补“报告实际估计的间接效应”，避免历史条件计数式完全中介声明顶替现代间接效应结果句；LEGACY 范本保留原有状态，只在明确的历史用途下核对适用性。

维护时在一个已有源块中声明完整定义，其他合适源块只在 `functions` 中引用其 ID。定义须包含 `id/label/section/refines/definition/use_when/neighbors/positive_example/mismatch_example/aliases`；新 ID 由源卡派生，既有 ID 的词法选择器留在 `retrieval-functions.json`，语义与别名读取源卡。构建器核验唯一权威块、相邻 ID、父功能和正例锚点。新增细功能只匹配已标注其 ID 的源块，覆盖不足时补现有卡片。细动作查询例：`--function intro.gap_shared_assumption`；也可用 `--function theory.mechanism --need "连接两个机制环节"`。

补标已有范本或登记新增蒸馏时，为新标签填写同一对象中的 `function_evidence:{"已引用的功能ID":{"kind":"verbatim","cue":"同块已有原句的短锚点","why":"此处实际完成该动作的理由"}}`；仅模板提供支持时用 `kind:"template"`，不能冒称原文。构建器核验字段及锚点确属同一源块、同一种摘录。标签按实际动作判定，标题和主题相似不构成完整支持；原句只完成部分动作时同时填写 `function_support` 的 `partial`。既有未填锚点的标注保持兼容，后续逐步核验。

逐条核查原句完整完成动作后，显式填写 `function_support:{"功能ID":"complete"}`。同块 `function_evidence` 的原句锚点实际命中时，功能判断采用该标注依据，不要求范文使用旧词法规则列出的连接词；`expression_check_basis` 明示 `authored_original_evidence`。只有标签、锚点缺失、仅模板支持或标为部分支持时，仍执行旧表达与原文同源检查，不把模板补成原文。来源可靠性与适用条件继续分别核对。

标注应位于本块来源与 pattern 元数据之后、下一个独立源块之前；有嵌套子变体时不得把父卡标注放进子变体的范围。保留原句、模板、原生编号及来源状态，补足具体句段角色和必要条件。覆盖统计分别看显式源块、完整/部分支持、模板缺原句和来源键，不能把同一论文的不同表达形式算成多个独立来源，也不为达到数量目标给相邻动作加完整标签。

结果收尾若要保留混合发现与主张上限，使用 `results.mixed_closure`；它与检验报告中的 `results.mixed_synthesis` 区分。当前源卡提供跨阶段对比形式，只有当前稿件确有多阶段证据时才借用；不能用一致强支持的总结句替代，也不能移植机制衰减解释。

在 skills 仓库根运行（从 skill 目录运行时使用 `../_shared/indexing/retrieve.py`）：

```powershell
python -B _shared/indexing/retrieve.py "共同所有权 产品召回" --function methods.sample --top 3
python -B _shared/indexing/use_exemplar.py query "地位 声誉" --function theory.definition --need "沿同一维度区分声誉" --project "当前项目"
python -B _shared/indexing/retrieve.py "女性 高管 战略更新" --function results.interaction --design "OLS" --top 3
python -B _shared/indexing/retrieve.py "产品召回" --function methods.identification --need "承认内生性风险，然后解释设计如何缓解风险" --conditions-file request-conditions.json
python -B _shared/indexing/retrieve.py "产品召回" --action methods.endogeneity_risk --action methods.design_mitigation --conditions-file request-conditions.json
python -B _shared/indexing/retrieve.py "产品召回" --action methods.endogeneity_risk --action methods.design_mitigation --conditions-file request-conditions.json --format cards --out adaptation-cards.md
python -B _shared/indexing/retrieve.py --list-functions
python -B _shared/indexing/retrieve.py --batch queries.json --out candidates.json
```

真实写作查询由代理使用 `use_exemplar.py query`，填写 `--need`（当前句段具体要完成的动作）与 `--project`；此入口自动登记返回事件，参数与 `retrieve.py` 一致。维护与基准继续使用只读 `retrieve.py`；兼容入口 `retrieve.py --record-use` 仍可用，试运行必须指定仓库外的隔离 `--home`。`--function` 接受列出的 ID 或中英功能名称；`--need` 可把原生功能族细化到已有细功能，例如构念定义→沿共同维度区分构念。未提供 function 时先从 need、再从 query 推断；单动作无法推断时保留内容查询。连续请求中某一步无法识别则返回 `unresolved_action_sequence` 与未识别的文本，不静默丢掉第二步；代理核对定义后填写有序 `--action` 或另拆需求。已有一个细功能本身定义了组合动作，且各分句都解析到它时，仍使用该完整功能契约。`--section` 限定来源章节；`--out <路径>` 保存到项目工作目录或外部临时目录。

`--section` 指来源库，不是当前草稿所在节；跨节借句按所需功能的来源节查询，使用时核对当前章节角色。来源的 `source_key_kind` 分单键、多键、引用字符串及缺失；多键/引用字符串仍须消歧，不能当作已确认的单篇 DOI/citekey。`status_basis` 显示原生/卡片状态、明确用户 override 或现有 status policy 的依据；不按单源条目自动推定低等级。

结构化条件用 `--conditions-file`、`--conditions-json` 或批量项 `conditions` 传入，字段为 `design/evidence/claim_scope/facts`。前三级接受字符串或字符串列表；`facts` 是具名的布尔值或字符串，只填当前项目已确认的事实，不从提问中的关键词补造。以下文件例子对应 DiD 风险移交范本：

```json
{"design":"did","evidence":"quasi_experimental","claim_scope":"causal_with_assumptions","facts":{"plausibly_exogenous_shock":true}}
```

源卡 `retrieval_move.applicability` 的 `design/evidence/claim_scope` 声明允许值，`required_facts` 声明必须核对的事实。`use_when` 是功能层面的文字条件，`applicability` 是该范本形式的可执行条件；例如非显著解释可以有多种限定理由，本卡的小样本形式要求 `small_sample:true`。某一类未标注或请求事实缺失保持 `unknown`，完全未检查为 `not_checked`；明确不符为 `incompatible`，在主题排序前排除。全部所涉检查有依据且相容才为 `compatible`。这只确认已声明条件，仍需核对文字条件和当前设计本身。

已使用的规范值包括 `did/iv_2sls/heckman/logit_probit`（依赖具体设计的范本）、`observational/quasi_experimental/null_result/mixed_findings`（证据性质）、`association/causal_with_assumptions/limited_conclusion/hypothesis_support/measurement_robustness`（论断范围）。允许值以源卡声明为准；`causal` 不自动等同于依赖识别假设的因果主张。范本只有在句式依赖设计时才把设计列为限制，不能仅按来源文件的估计器给所有句式设限。

`--design` 保留既有词法硬筛选，并将已识别的整个设计名用于结构化比较；源块有设计声明时按声明检查，未标注时词法命中也保持条件未知。`--evidence` 保留证据特征词法硬筛选，结构化证据性质放在 `conditions.evidence`。`--require-content` 要求至少命中一个内容概念；`--status VERIFIED` 按现有状态筛选（可重复），默认不过滤单源或未评级条目。

多句/多段起草优先批量查询：`queries.json` 是对象列表，每项含 `id/query/function/need`，其余可填 `actions/conditions/section/design/evidence/status/require_content/top/supplement_top/query_id`。一批共用一次目录校验，每项生成独立检索编号；也可在 Python 中先 `load_catalog()`，再将结果传给多次 `search(..., catalog=data, actions=[...], conditions={...})`。当前已登记库存由原生解析器决定，新增文件仍须进入该节的解析清单。

每条主候选与补充候选都有派生的 `adaptation_card`，按下列六栏呈现。默认 JSON 保留原有字段；`--format cards` 把同一对象输出为 Markdown，支持单次及批量检索。输出仍放项目目录或仓库外，不新增范本库。

| 栏目 | 内容与改编边界 |
|---|---|
| 原句或原段落（`original`） | 原摘录、UID 和卡片来源键；连续动作在档案中确认顺序时附真实完整段落，跨段分开呈现。缺原句明确写缺失，模板单列。 |
| 完成的功能（`function`） | 动作定义及其支持程度；句段位置、承接、推进、后接与后续证据要求。部分支持、别名推断和补充候选继续明标。 |
| 关键表达骨架（`skeleton`） | 同一源块已有模板与可学动作，保留模板 UID；标为蒸馏骨架，不能作为论文原句引用。宽于当前动作的骨架只借适用部分。 |
| 可替换部分（`substitution`） | 槽位的逻辑角色与填写边界、论证步骤提示、源卡不可移植项。数值与检验信息取当前分析；方向和判断重新核对；设计与条件不能仅换名称。 |
| 适用条件（`applicability`） | 结构化条件检查、源卡文字条件、动作的 `use_when`。未知保持未知，已声明条件相容不等于设计可信度已验证。 |
| 来源与上下文（`source_context`） | 每条摘录的原有状态、来源键类型、档案匹配状态、真实段落位置及前后文。与适用条件分栏，档案定位不等于原始 PDF 或书目核验。 |

先读原句，再核对动作与承接关系，然后选择骨架和替换内容；提交改编前核对条件与来源。`[基线]`、`[事件分段1]` 等论证提示单列为 `structural_markers`，不当作变量槽位。参数、函数与系数先确认表示模型设定还是实际估计值，不能仅因出现“系数”就要求填实证数值。槽位角色由保守规则辅助识别，无法确定的标为 `requires_review`，不得据此认为所有括号内容都能任意替换。

段落角色只读取源卡已写的 `position/prerequisite/advances/next/next_evidence`；没有标注时明确为未知或未单独标注，不从功能名、来源文件名或相邻卡片补造。`next` 说明后续交接，`next_evidence` 说明当前稿件还须提供的证据，两者分别显示。卡片对句段的角色标注与档案的实际章节/段号分别保留。骨架覆盖整段但当前动作只需要其中一部分时，在同一源块补 `skeleton_span:{"functions":["本块动作ID"],"start":"已有模板中的唯一起始锚点","end_before":"可选的结束前锚点"}`；构建器核验锚点能唯一定位同块模板的有序范围。仅当当前需求动作落在此范围内才截取已有文字，其他动作与宽查询保留完整模板及 UID。缺模板时显示未定位，不改写或跨块拼接。

旧 `skeleton_span` 未填动作列表时，范围沿用该源块的 `functions`；不扩展到其他动作。改编卡的 `function.actions[].support.state` 显示已标注、部分支持、推断或未匹配；`selector_satisfied` 表示本次功能检查通过，`expression_check_basis` 区分原句标注依据与旧词法规则，不能仅凭检查通过认定动作完整。原句优先显示顺序锚点，其次显示本块 `function_evidence` 所指摘录，再使用定义正例和同块回退；未选中的同块原句仍保留 UID，但不抢占当前动作的展示位置。

原有字段仍包括原句、同块模板、原生功能、来源 citekey、验证状态、UID、卡片路径与行号、源块全文、适用条件、不可移植项和可学动作。`context/preceding_context/following_context` 是**蒸馏卡片上下文**。每条原句的 `source_context` 单列在本地 `.sentences.md` 档案中逐字或排版归一化匹配的原文段落、章节、段号、路径/行号和前后段落；省略号分段匹配会明确标注。改编卡的 `source_context.excerpt_sources[].paragraph_windows` 提取该摘录在实际段落内的前后文本，并保留省略与位置歧义；前后段另外给出定位，不混作同段前后句。

档案匹配状态分为 `matched`、`citation_discrepancy`（键的作者/年份字符串有差异）、`ambiguous_paragraph`（段落不唯一）、`ambiguous`（档案不唯一）、`not_found`。键差异可能是别名、发表年份或误归源，不能直接认定书目错误；档案定位不等于PDF核验。缺失/歧义不补造上下文。状态不等同于摘录与当前任务适配程度；用户认可的单源 VERIFIED 保持有效。

分层检索按“需求解析→功能匹配→适用条件检查→内容相关度排序→来源与上下文支持”执行。排序为功能准确度、条件相容程度、内容分数（含标题命中）、来源与上下文支持的字典序，主题分数不能抵消更高的功能层级或更明确的条件匹配。已标注完整动作优先于词法推断和部分动作；已核对的相容条件优先于缺标注的候选。`specific_move/native_family/partial_move/content_only` 区分具体动作、宽功能族、部分支持和仅内容命中；`function_matching.uncertain` 明标别名解析、词法匹配和部分动作的不确定性。`condition_check` 与 `source_support` 分别呈现适用性和来源依据。`content_matches` 列出实际命中的内容词，零命中只表示同功能异主题候选。

`candidates` 是主候选，`supplementary_candidates` 单列主题相关但动作不符、动作不全或顺序未确认的补充项；这些不计作成功匹配，主候选为空仍为 `no_fit`。明确条件冲突的项也不能进入补充项。`--supplement-top` 默认最多2条，0关闭；两组候选的 `rank` 按展示顺序连续编号。

连续动作要求同一源块、同一篇原文中的有序锚点，`retrieval_move.sequence` 每步含 `function/kind/cue`，且引用 `functions` 中已登记的动作。运行时按请求顺序检查 cue，不跨卡片或跨论文拼接，不用模板补齐原文动作。同一摘录暂缺单篇来源键时保留明确的来源待确认状态；只有一个摘录自身包含全部动作才可保留顺序。`function_matching.sequence.archive_order` 另核对真实档案段落顺序：能定位时返回段落行号与单段/跨段状态，档案顺序冲突不能进入主候选。档案缺失、歧义或省略号继续保留，源卡的顺序标注不能替代原文上下文。

改编卡由 `indexing/adaptation_cards.py` 从本次候选派生，不改变检索排序、原生编号或验证状态。旧 `replaceable_slots` 保留兼容，新改编应读取含角色和边界的 `adaptation_card.substitution`。给新范本补细功能时，在现有源块的来源/pattern_id 元数据**之后**写 `<!-- retrieval-move: {"functions":["已登记的功能ID"],"position":"句段位置","prerequisite":"成立前提","advances":"此句推动的论证","next":"后续交接","next_evidence":["后文所需证据"]} -->`；可在同一对象中补 `applicability/sequence`。段落角色字段可选，缺信息不补猜；填写时字符串与证据列表必须非空。只有部分原文动作时用 `function_support:{"功能ID":"partial"}`，不得标成完整动作。构建器核验条件结构、动作登记、同块锚点及顺序；保留原生分类，索引派生读取，不另存摘录副本。

从 top 3 中读取原句及上下文，比较功能、论证关系、适用条件和证据强度；挑选可改编项，再替换研究内容。只换变量名不足以构成改编。不得把原句的数值、因果强度、制度事实、研究设计或支持判断带入用户稿。若条件未标注，在当前输入中自行核对；若缺原文、功能不符或没有可用候选，报告具体缺口并回查该节原生索引，不强行仿写。需要多个来源合成时逐项保留来源。

返回、打开、采用、作者接受是不同状态，只记录实际发生的状态。原句/模板 ID 不得伪造为 wb item。基准与试运行不写真实使用台账。

每次查询返回独立 `query_id`、原始需求和检索/语料版本指纹；批量项的 `id` 是任务标签，不替代检索编号。主候选与补充候选都关联本次编号和排名，外部台账仅存 UID、候选角色、文件定位与指纹，不存原句、模板或改编正文副本。`returned_recorded` 显示登记是否成功；失败仍交付检索结果，后续登记须先补实际返回记录。Python API 的 `search()` 保持只读，真实使用时调用 `record_returned(result, catalog, home=...)`。默认台账由既有 `fitness_ledger.ledger_home()` 决定，位于 skills 外部。

按以下顺序执行实际操作，由代理代办，不要求作者操作台账：

1. `use_exemplar.py query ...` 返回候选并自动记 `returned`。保留本次 `query_id`，批量各项分别保留。
2. 改编前执行 `python -B _shared/indexing/use_exemplar.py open`，stdin 为 `{"query_id":"<本次编号>","source_uids":["<实际选看UID>"]}`。它实际读取源卡及可定位的本地原文段落、前后文，再自动记 `opened`；只看检索卡片不算打开原文。来源缺失仍只读取已有卡片并明标档案缺口，不声称读过 PDF。可一次选看多个 UID。
3. 保存改编稿时执行 `python -B _shared/indexing/use_exemplar.py write`，stdin 为下述对象。写入成功并核对文件指纹后，自动记各次检索的 `adopted` 和一条 `consumption`，共用 `use_id`。失败写入不登记采用。已保存同内容的重试只修复漏登，不重复写正文或计数。

```json
{"skill":"write-methods","section":"methods","project":"<实际项目>","uses":[{"query_id":"<本次编号>","source_uids":["<实际采用UID>"]}],"draft":{"path":"<仓库外项目草稿.md>","mode":"create","text":"<实际改编稿>","location":"<句段定位>"}}
```

`write` 保存 UTF-8 文本，默认 `create`；修改已有稿件用 `replace` 或 `append`，必须填读取原稿得到的 `expected_sha256`，防止覆盖后来修改。`append` 的 `text` 只含新增文字并自带所需换行。采用多次检索或多个来源时，在 `uses` 中逐项填编号与实际 UID；草稿所属 skill/section 不限定范本的来源节。草稿与输入工作单均放项目目录，不放 skills 或台账目录。

使用 Word、OfficeCLI 等原生写作工具时，先成功保存，再执行 `use_exemplar.py adopt`；stdin 与上例相同，但 `draft` 改为 `{"path":"<实际草稿文件>","sha256":"<已保存文件的真实64位SHA256>","location":"<句段定位>"}`，不传正文。此入口核对文件存在与指纹，再执行同一采用登记。成文登记规则见 `consumption-log.md`；已经由 `write/adopt` 登记的版本不另做一次消耗登记。新采用须有本次候选与实际文件读取记录，语料改变则重新检索；历史手动观察保留，不补造缺失步骤。

事件须关联已登记检索，UID 必须属于本次候选；编号不可绑定不同需求、版本或候选。日志失败不阻塞已保存草稿交付，返回结果分别显示 `adopted_recorded/consumption_recorded`；保留同一草稿、编号和 UID 重试即可修复单边漏登。同一观察重试不重复计数。`use_exemplar.py show --query-id <编号>` 或 `log_exemplar.py --query-id <编号>` 按编号只读展示排名、实际查看、采用稿件、时间顺序、各 UID 作者状态和拒绝原因，不推断未发生的步骤。

4. 后续收到对范本匹配或已交付改编稿的明确评价时，代理执行 `python -B _shared/indexing/use_exemplar.py feedback`，stdin 填实际反馈与当次关联。`log_exemplar.py` 的原入口仍可用并执行同一校验。作者无需填写编号；代理从实际检索与采用记录中读取编号、UID 和 `use_id`。

```json
{"query_id":"<实际检索编号>","use_id":"<实际采用编号>","source_uids":["<本版本实际采用UID>"],"feedback_scope":"adoption","state":"rejected","actor":"author","feedback":"<作者实际原话>","reason_code":"condition_mismatch","reason":"<原话指出的具体设计或证据条件差异>"}
```

作者接受用 `state:"author_accepted"` 并保留原话，不需要编造拒绝原因。反馈分三种目标：`adoption` 评价具体改编版本，校验本次 UID、`use_id/adoption_event_id` 和登记的草稿指纹；`candidate` 评价范本本身，不等同于接受随后写出的草稿；`query` 用空 UID 登记检索级缺口。未指定目标时，唯一实际采用可以自动关联；存在多个可评价版本时必须从实际上下文明确目标，不能按最新版本猜测。无法确认的版本保持未知，保留真实原话在项目的待关联记录中，并简短确认目标。

`feedback` 只登记实际 `author_accepted/rejected`，不补造返回、查看或采用。作者评价须含 `actor:"author"` 和 `feedback` 原话；代理判断用 `actor:"agent"`。工作指令、对本系统的验收或没有回复，都不算稿件作者接受。同次检索其他 UID、其他检索、同 UID 的新稿版本均不继承该项评价。晚到的旧稿评价绑定当时保存的指纹，不以当前磁盘内容覆盖；`show` 的 `adoptions` 逐版呈现，顶层作者状态对应最近登记的采用。候选评价与未明确版本的历史反馈另外保留，历史日志不改写、不猜测关联。`feedback_recorded` 显示登记是否成功；失败不登记已接受，代理仍先按真实反馈修正文稿，并保留原关联重试。

弃用事件 `rejected` 必须包含 `reason_code` 与具体 `reason`：`function_mismatch`（功能）、`condition_mismatch`（设计/证据条件）、`adaptation_difficulty`（改编）、`source_unclear`（来源）、`corpus_gap`（缺语料）、`content_distance`（内容距离）、`redundant`（重复）、`other`。`log_exemplar.py --list-reasons` 查看对应修正位置。反馈事件不把返回/打开自动计为 consumption；后续评价仍能绑定当时返回的 UID 和版本，即使条目已退出当前目录。可执行修订规则与语料维护继续走各 skill 既有批评通道，使用记录及原话留在外部台账。低频或未登记使用本身不构成删除语料的依据。

`catalog.json` 是四个原生解析器生成的派生缓存，默认存入 `%LOCALAPPDATA%/claude-skills/corpus-index/<仓库路径哈希>/`，不进入 skills 仓库；可删除，下一次查询自动重建。非 Windows 环境使用 `~/.cache/`。改卡片、解析器、排除/override 或注册表后检索会校验依赖并刷新，新增已登记的卡片也会刷新。维护时运行 `python -B _shared/indexing/build_catalog.py` 和 `python -B _shared/indexing/check_all.py --worktree`；前者的 `--check` 在无缓存时仅验证内存重建，有缓存时比较一致性；后者检查当前修改，不要求先暂存到 Git。`legacy-id-migration.json` 是冻结旧索引的必要迁移记录，旧编号有歧义时必须用源文件与摘录哈希消歧。
