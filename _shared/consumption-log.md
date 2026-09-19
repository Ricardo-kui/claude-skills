# 消耗登记（write-* 家族共用单源）

> **用途**：fitness 台账策展数据面（检索命中率、从未被检索变体）。**best-effort**：失败不阻塞交付，漏登可接受，不重登。触发：每次成文（含无批评的常规交付）。

命令（各 skill 成文后执行一次）：

```
py distill-paper-exemplar/scripts/fitness_ledger.py log-consumption
```

（自各 skill 目录取相对路径 `../distill-paper-exemplar/scripts/fitness_ledger.py`。）

stdin JSON（`skill`/`section` 用本 skill 固定值，其余按当次实况填）：

```json
{"skill": "<write-introduction|write-theory|write-methods|write-results>", "section": "<introduction|theory|methods|results>", "project": "<项目>", "corpus_files": ["<实际读过的 corpus 文件>"], "variants": ["<!-- wb:citekey:item -->"], "blueprint_cards": ["<实际采用的蓝图卡 id>"], "note": ""}
```

各 skill 固定值：write-introduction→`introduction`；write-theory→`theory`；write-methods→`methods`；write-results→`results`。
