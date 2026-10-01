# 消耗登记（write-* 家族共用单源）

> **用途**：fitness 台账策展数据面（实际采用及窗口内未记录使用的条目）。不代表检索命中率或从未被检索。触发：每次成文（含常规交付）。**best-effort**：台账失败不阻塞已保存草稿交付；同一新采用记录可以重试修复漏登，不重复计数。

使用新检索 UID 的成文走 `exemplar-retrieval.md` 的 `use_exemplar.py query → open → write/adopt`：保存成功后同时登记 `adopted` 与 `consumption`，共用 `use_id`；已成功登记的版本不另记一次。多个检索或跨来源改编用 `uses` 分别绑定编号与 UID。由其他工具保存的草稿，成文后调用一次统一登记入口：

```
python -B _shared/indexing/use_exemplar.py adopt
```

（自各 skill 目录取相对路径 `../_shared/indexing/use_exemplar.py`。）

stdin JSON（固定 skill/section；其余取实际检索、已读源卡与已保存草稿，不存正文）：

```json
{"skill":"<write-introduction|write-theory|write-methods|write-results>","section":"<introduction|theory|methods|results>","project":"<实际项目>","uses":[{"query_id":"<实际检索编号>","source_uids":["<实际采用UID>"]}],"draft":{"path":"<已保存草稿的仓库外路径>","sha256":"<已保存文件的真实64位SHA256>","location":"<句段定位>"},"variants":[],"blueprint_cards":[],"note":""}
```

各 skill 固定值：write-introduction→`introduction`；write-theory→`theory`；write-methods→`methods`；write-results→`results`。

`corpus_files` 自动含实际采用 UID 的源卡；如另填，必须是已登记卡片。只有实际采用且 UID 对应的真实 wb 标记才填 `variants`，不要用骨架 ID 拼接标记。`source_uids` 汇总由 `uses` 派生；可兼容单次的顶层 `query_id/source_uids`，不能匿名登记新 UID。草稿文件须存在且指纹一致；查看过但未改编成文不登记。

旧命令 `python -B distill-paper-exemplar/scripts/fitness_ledger.py log-consumption` 仍可从 stdin 或 `--file` 读取同一对象，转到统一采用入口；支持 `--home` 隔离测试。直接按原生索引或蓝图写作、未使用新检索 UID 的登记继续用旧命令，填 `skill/section/project/corpus_files/variants/blueprint_cards/note`，不编造 `query_id`，以 `legacy_native` 单列。历史日志不改写、不倒填编号；读取时消歧旧别名，歧义项单列。

台账在 skills 外部，只记关联与草稿定位。返回/打开/采用/作者接受不能相互替代；作者评价只在真实反馈到达时登记，未回复保持未知。未记录使用不代表没有价值，未知条目年龄不以文件日期推断；不凭使用频率删除低频语料。
