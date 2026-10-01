# 蒸馏写回收尾（四节共用）

单节独立蒸馏及整篇编排写回后都执行本协议；只产候选、未写回时不执行。沿用已获得的写回授权。本协议负责登记、检索可见性和终验，不改变各节提炼与适配判断。

1. **登记新文件**。plan 含 `new_file` 时，将文件加入对应 `write-*/scripts/build_indices.py` 的解析轴：Methods/Results 用 `FAMILIES`；Theory 用 `VARIANT_FILES`、`SUBPROTOCOL_FILES` 或 `SENTENCE_FILES`。Introduction 在现有 `MODULES` 目录内自动扫描；新增模块目录须先进入 `MODULES`。Methods 的 `micro-templates/` 是独立 INDEX 路由资产，不充当设计类型文件。
2. **核验写回与注册表**。使用本次 plan 和 citekey 运行 `distill-paper-exemplar/scripts/verify_writeback.py --plan <plan路径> --paper <citekey>`。其终检包含注册表派生字段 dry-run；修复失败及相关残项后继续，保持用户状态裁定。plan 与残项留在本次工作目录，供收尾审计读取。
3. **重建并检查检索**。从 skills 仓库根执行下列命令；`<section>` 为实际写回的 `introduction/theory/methods/results`。写回多节时逐节重建骨架，检索缓存和总门各执行一次。

   ```powershell
   python -B write-<section>/scripts/build_indices.py --verify
   python -B _shared/indexing/build_catalog.py
   python -B _shared/indexing/check_all.py --worktree
   ```

   总门检查当前工作树，完成写回不依赖 Git 暂存或提交。Methods 新设计类型文件漏登记（含子目录）及失效登记均会失败；Theory/Results 的内容覆盖检查沿用原生规则。检索缓存默认落本机缓存目录，位置见 [范本检索协议](exemplar-retrieval.md)。
4. **补标并试查新增资产**。逐源块判断是否完成已登记细功能；符合时在权威卡片的 `retrieval-move.functions` 引用已有 ID，按 [范本检索协议](exemplar-retrieval.md) 补同块证据锚点、支持程度、句段角色与必要条件。只完成部分动作时明标 `partial`，没有充分依据时不加标签。确需新细功能时在单一源块补 `definitions`，让索引派生读取；不在 `retrieval-functions.json` 复制定义，该文件保留既有词法入口。用一项本次新增的内容＋功能需求运行 `python -B _shared/indexing/retrieve.py "<内容>" --function <功能ID> --top 3`，打开候选核对新增原句/模板、UID、来源与适用条件；标签变更后重做第 3 步。无匹配、来源未定位或条件缺失如实记录，结构总门通过不代替范本适配判断。
5. **呈报后清理**。汇总本次新增/扩展位置、终验、试查及未解决项，再按原有单节/整篇规则清理工作目录和字节码缓存。保留语料、原文档案、状态记录与必要迁移记录；常规运行不在 skills 仓库保存完整候选JSON、一次性评测或运行日志。节内既有语料体检仍按该节规则执行。
