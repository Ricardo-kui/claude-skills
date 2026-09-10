# _pi-config — pi 配置快照（2026-09-10 起）

> **快照性质：** 本目录是 pi 配置的版本化副本，权威文件仍在原路径。任一端修改后须手动同步回此处再 commit。

| 快照 | 权威路径 | 说明 |
|---|---|---|
| `AGENTS.md` | `~/.pi/agent/AGENTS.md` | 全局学术基线（任何 cwd 生效） |
| `AGENTS.override.md` | `C:\Users\admin\AGENTS.override.md` | 工作区层（home 目录会话细节与例外路由） |
| `settings.json` | `~/.pi/agent/settings.json` | 默认模型/thinking/扩展包（**不含** auth.json——密钥永不入库） |
| `filter-cursor-models.mjs` | `~/.pi/agent/filter-cursor-models.mjs` | Cursor 地区限制模型过滤脚本 |

同步纪律：claude-skills 仓库同时是 Claude Code 与 pi 的工作树，任一端编辑 skill 或配置后直接 commit+push，不手动拷贝目录。
