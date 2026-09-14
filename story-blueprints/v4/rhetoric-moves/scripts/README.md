# scripts/ — 本目录为占位，脚本不在此处

## 这是什么

`story-blueprints/v4/rhetoric-moves/scripts/` 是一个**空目录占位**。rhetoric-moves 层（修辞动作与润色协议）没有自己的脚本。若按本目录路径调用脚本会得到“文件不存在”，从而误判为“检索不可用”。

## 脚本真实位置

rhetoric-moves 相关脚本位于上一级 `story-blueprints/scripts/`：

| 脚本 | 路径 | 作用 |
|---|---|---|
| `retrieve_exemplars.py` | `story-blueprints/scripts/retrieve_exemplars.py` | 从 v0.4-lite 卡 catalog 检索即时范文学习对象（1 主 + 1 对照） |
| `build_catalog_v4.py` | `story-blueprints/scripts/build_catalog_v4.py` | 生成 v4 catalog |
| `validate_blueprints_v4.py` | `story-blueprints/scripts/validate_blueprints_v4.py` | 校验 v4 blueprint 卡 |
| `validate_blueprints.py` | `story-blueprints/scripts/validate_blueprints.py` | 校验 blueprint 卡 |

## 调用路径

单一事实源的调用写法见 `../_immediate-exemplar-protocol.md` §步骤 2：

```
py ../story-blueprints/scripts/retrieve_exemplars.py --request <临时 JSON>
```

该相对路径以**调用方 skill 目录**为基准。例如从 `write-introduction/` 目录调用时，`../story-blueprints/scripts/` 解析为 `skills/story-blueprints/scripts/`。从本目录（`story-blueprints/v4/rhetoric-moves/scripts/`）出发时，正确路径是 `../../../scripts/retrieve_exemplars.py`。

## 维护约定

- 新增 rhetoric-moves 脚本时，直接放入 `story-blueprints/scripts/`，并在 `../_immediate-exemplar-protocol.md` 或相应协议文件登记调用路径。
- 本目录保留为空目录加本 README，作为路径说明锚点。
