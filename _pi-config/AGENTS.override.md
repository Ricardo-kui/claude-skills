# Pi Workspace Layer — C:\Users\admin（本机事实与例外路由）

全局学术基线与本机工作台事实见 `C:\Users\admin\.pi\agent\AGENTS.md`（任何 cwd 生效）。本层只补 home 目录会话需要的本机细节；学术规则一律在全局层，不在本层重复，也不维护与 skill descriptions 平行的分发清单。

## 文档导入解析器（详细路由）

- 统一入口：`C:\Users\admin\.local\bin\paper-import.cmd "PDF完整路径"`。页数/类型分诊：`python D:\AI\OvisOCR2\diagnose_pdf.py "PDF路径"`。
- ≤80 页普通论文 → OvisOCR2（质量优先：文本/扫描/旧字体/双栏/表格/公式/图）；>80 页或保守识别图书 → MinerU HighAccuracy。显式控制：`-UseOvis` / `-UseMinerU` / `-Fast` / `-NoTidy` / `-NoRelocateTables` / `-LinkImages`（旧版每篇一 images/ 文件夹布局）。
- 两条路径均执行 `python D:\AI\OvisOCR2\pdf_ocr_tidy.py` 文档级整理（唯一排版阶段，不加兄弟脚本）；默认输出单文件 flat `.md` + base64 内嵌图，落 `D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入`。
- 质量升级触发：不可读扫描、缺图、表重建差、多栏乱序、公式丢失。默认不双管线并行（避免重复 Obsidian 笔记）。
- 中文路径兜底：`opendataloader-pdf` 无输出时立即改用 `markitdown`。

## Office / 转换工具

- `.docx/.xlsx/.pptx` 读写编辑 → `officecli`（`C:\Users\admin\AppData\Local\OfficeCLI\officecli.exe`，v1.0.145+）：`view text|outline|annotated` 读，`get`/`query` 查（多步编辑优先稳定 `@paraId`/`@id` 路径），`set`/`add`/`remove`/`batch` 改（batch 原子），`validate` / `view issues` 查。`--find` + 格式属性自动拆 run。markitdown 兜底；python-docx/openpyxl 仅当 officecli DOM 层表达不了操作时用。
- `markitdown` / `opendataloader-pdf` 位于 `C:\Users\admin\AppData\Roaming\Python\Python312\Scripts\`。

## Stata 运行时（本机细节）

- `stata-mp` shim 在 `C:\Users\admin\.local\bin`；exe `C:\Program Files\StataNow19\StataMP-64.exe`。
- `stata-cli` 在 PATH；始终带 `--compact --max-tokens 20000`；长脚本写 .do 后 `stata-cli --compact do file.do`；查状态 `stata-cli data` / `vars` / `return` / `matrix`（JSON）；频繁调用先 `stata-cli daemon start` 保活。
- `staggered_did` 已装至 StataNow19 PERSONAL（仓库 `C:\Users\admin\staggered-did`）；`JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-21.0.10.7-hotspot`。

## Vault Protocol（文献综合类任务）

- 顺序：preflight → 项目 `PROJECT_STATUS.md` → `Decision Register`（含 rejected/superseded）→ fresh `Context Packet`（stale 先对账再当现状用）→ 匹配 skill → `index.md` / Tier 1（≤15 篇）→ Tier 2（≤10 篇，仅 Tier 1 不足时）→ Archive（仅显式要求）。
- 排除读取：`_codex_tools/`、`.smart-env/`、`.obsidian/`、`.trash/`、`Template/`、`模板/`、`wechat/`、`xhs/`、`inbox/`、`meeting_notes/`、`文献笔记库/01 导入/`（例外：`01 导入/论文导入/` 全文 MD 是权威源层）及 `_backup_` 目录。
- 输出：文献用 `[@citekey]`、笔记用 `[[note_id]]`，附证据完整性声明；综合 3+ 篇时建议回写。

## 例外路由（仅列与默认路由冲突的少数条目）

- 全稿 QC / 投稿前审查 → `paper-review`（唯一入口；`--narrative` 只跑叙事层）；实质红队单查 / desk-reject 风险专项 → `toc-review`；两篇论文新颖性对辩 → `tod-debate`。
- Discussion 生成不再路由（`write-discussion` 已退役归档）。
- 其余任务按 skill descriptions 自动路由。
