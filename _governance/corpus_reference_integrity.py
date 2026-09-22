#!/usr/bin/env python3
"""语料引用完整性门：校验语料树内的文件路径引用是否可达。

问题背景
--------
2026-09-20 发现：`story-blueprints/v4/blueprints/` 的卡片在
`reading_scope.source_records` 里以 `"Sentence archive: <路径>"` 引用
`v4/rhetoric-moves/sources/*.sentences.md`。该 sources 目录经历一次批量
backfill（126 候选 / 112 新增 / 8 个旧键被替换删除），**引用侧没跟着改名**，
产生 5 处死指针。能潜伏至今的原因是：**这个技能完全不在任何一致性门内**
（``check_all.py`` 的 SKILLS 列表只有 write-results / write-methods / write-theory；
``corpus_registry_reconcile.py`` 只覆盖四节的注册表对账）。

本脚本补的正是这个面：**「语料文档内部的路径引用 ↔ 磁盘实况」**。

对账口径
--------
1. **显式路径引用**：扫描每个技能树下的 ``*.md`` / ``*.yaml`` / ``*.json``，
   抽取形如 `<...>/sources/<file>.sentences.md` 之类**带目录分隔符的相对/仓内路径**，
   解析到仓库根后 `Test-Path`。

2. **别名式引用（sources 目录内）**：语料卡片常写「Sentence archive: <name>.sentences.md」
   这类**裸文件名 + 省略号占位**（如 `higgins_2003_...ppe.sentences.md`）。
   对**明确声明了归档目录**（如 story-blueprints 的
   `v4/rhetoric-moves/sources/`）的技能，把裸名解析为该目录下同名文件。

3. **省略号占位检出**：引用里含 `...` 的，一律单列为 `PLACEHOLDER`（不是 MISSING）——
   它表示「这条引用从未被验证过」，性质与普通断链不同，需人工补全。

刻意不检查的东西（重要，避免误报）
----------------------------------
- **PDM 引用**（`*.pdm/...`、`*.pdm.yaml`）：``story-blueprints/_schema.md`` 定义
  ``source_records: [<memory 文件名或蒸馏记录>]`` —— 是**蒸馏溯源记录名**，不是可解析路径。
  全库 94 处 PDM 引用而 ``.claude/skills`` 下不存在任何 ``.pdm`` 目录，属**设计使然**。
  本脚本按 ``PDM_RE`` 显式排除。是否把 PDM 变成可解析指针是独立议题。
- **Obsidian vault 绝对路径**（``D:\\Onedrive\\...``）：指向仓库外的用户笔记库，
  不在本门职责内，按 ``EXTERNAL_RE`` 排除。

退出码
------
0 = 无 FAIL；1 = 有 FAIL（断链或占位）；2 = 环境错误。

用法
----
    python _governance/corpus_reference_integrity.py [--skill <name>]... [--json] [--quiet]

只读：本脚本永不写盘。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------- 常量 ----

# 需要扫描的技能（语料树所在处）。新增技能时在此登记。
DEFAULT_SKILLS = [
    "write-introduction",
    "write-theory",
    "write-methods",
    "write-results",
    "story-blueprints",
    "_shared",
]

# 「裸文件名 → 归档目录」映射。
#
# 语料卡常写「`<name>.sentences.md:488`（..., rhetoric-moves/sources）」
# 这种**裸文件名 + 归档说明**形式。注意：归档目录可能属于**另一个技能**
# （如 write-introduction 的 generation-protocol.md 引用 story-blueprints 的
# rhetoric-moves/sources）——2026-09-20 实测确认，所以解析必须跨技能。
#
# 映射按「归档说明里出现的标识串」索引，全局可用。
BARE_NAME_ROOTS = {
    # 归档说明串 -> 相对 REPO 的目录
    "rhetoric-moves/sources": "story-blueprints/v4/rhetoric-moves/sources",
    "rhetoric-moves": "story-blueprints/v4/rhetoric-moves",
}

# 技能 → 该技能内裸名引用的默认归档目录（无显式归档说明时兜底）
SKILL_DEFAULT_ARCHIVE = {
    "story-blueprints": "story-blueprints/v4/rhetoric-moves/sources",
}

# 扫这些扩展名
SCAN_EXTS = {".md", ".yaml", ".yml", ".json"}

# 引用行特征：出现这些词的行走「引用候选」通道
REF_HINT = re.compile(
    r"(?:Sentence\s+archive|Sentence\s+inventory|sentence\s+archive"
    r"|句子库存|句子库|语料来源|见\s*sources/)",
    re.IGNORECASE,
)

# 仓内相对路径（含 `/` 或 `\`，以已知语料扩展名或目录结尾）
PATHLIKE = re.compile(
    r"(?P<p>(?:[A-Za-z0-9_\-\.]+[/\\])+[A-Za-z0-9_\-\.]+\.(?:md|ya?ml|json))"
)

# 裸文件名 + .sentences.md（可含 `...` 省略占位），可带 `:NNN` 行号
BARE_SENTENCES = re.compile(
    r"(?P<n>[A-Za-z0-9_\-\.]*\.\.\.[A-Za-z0-9_\-\.]*|[A-Za-z0-9_\-]+)"
    r"\.sentences\.md(?::(?P<ln>\d+))?"
)

# 显式路径 + 行号
PATH_WITH_LN = re.compile(
    r"(?P<p>(?:[A-Za-z0-9_\-\.]+[/\\])+[A-Za-z0-9_\-\.]+\.sentences\.md):(?P<ln>\d+)"
)

# 排除：PDM 溯源记录名（非路径）
PDM_RE = re.compile(r"\.pdm[/\\]|\.pdm\.ya?ml|_pdm\b", re.IGNORECASE)
# 排除：仓库外绝对路径（Obsidian vault 等）
EXTERNAL_RE = re.compile(r"^[A-Za-z]:[/\\]|^\\\\|^/mnt/|^/Users/|^/home/")
# 排除：明显的模板/示例占位
TEMPLATE_RE = re.compile(r"<[^>]+>|\{[^}]+\}|YYYY-MM-DD|xxxx", re.IGNORECASE)


class Result:
    def __init__(self) -> None:
        self.rows: list[dict] = []
        self.checked = 0
        self.line_checked = 0
        self.line_map: list[tuple] = []

    def add(self, kind: str, path: Path, line: int, ref: str, note: str = "") -> None:
        self.rows.append({
            "kind": kind,
            "file": str(path.relative_to(REPO)).replace("\\", "/"),
            "line": line,
            "ref": ref,
            "note": note,
        })


def _iter_files(skill: str):
    root = REPO / skill
    if not root.is_dir():
        return
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in SCAN_EXTS:
            continue
        # 跳过明显的非语料目录，减少噪声（仍可 --include-all 关闭）
        rel = p.relative_to(root).as_posix()
        if rel.startswith(("_governance/", "node_modules/", ".git/")):
            continue
        yield p


def _resolve_in_repo(ref: str) -> Path | None:
    """把仓内相对路径解析为磁盘路径（容忍前缀冗余）。"""
    r = ref.replace("\\", "/").strip().strip('"\'`')
    if not r or EXTERNAL_RE.search(r):
        return None
    # 去掉可能的 ./ 前缀
    while r.startswith("./"):
        r = r[2:]
    cand = REPO / r
    if cand.exists():
        return cand
    # 容忍「技能名前缀缺失」：逐段删前缀再试
    parts = r.split("/")
    for i in range(1, len(parts)):
        c2 = REPO / "/".join(parts[i:])
        if c2.exists():
            return c2
    return None


def _archive_index() -> dict[str, dict[str, Path]]:
    """为每个已知归档目录建「文件名 -> 路径」索引（跨技能全局可用）。"""
    idx: dict[str, dict[str, Path]] = {}
    for tag, rel in BARE_NAME_ROOTS.items():
        d = REPO / rel
        if not d.is_dir():
            continue
        files: dict[str, Path] = {}
        for f in d.iterdir():
            if f.is_file():
                files.setdefault(f.name, f)
        idx[tag] = files
    return idx


def check_skill(skill: str, res: Result, archives: dict[str, dict[str, Path]]) -> None:
    # 该技能无显式归档说明时的兜底归档
    default_tag: str | None = None
    dflt = SKILL_DEFAULT_ARCHIVE.get(skill)
    if dflt:
        for tag, rel in BARE_NAME_ROOTS.items():
            if rel == dflt:
                default_tag = tag
                break

    for path in _iter_files(skill):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            # 只审「引用特征行」与「含 .sentences.md 的行」
            if not (REF_HINT.search(line) or ".sentences.md" in line):
                continue
            if TEMPLATE_RE.search(line) and ".sentences.md" not in line:
                continue

            # --- 1. 显式路径引用 ---
            hit_path = False
            for m in PATHLIKE.finditer(line):
                ref = m.group("p")
                if PDM_RE.search(ref):
                    continue  # PDM 是溯源记录名，不是路径
                hit_path = True
                res.checked += 1
                if "..." in ref:
                    res.add("PLACEHOLDER", path, lineno, ref,
                            "路径含省略号占位——该引用从未被验证")
                elif _resolve_in_repo(ref) is None:
                    res.add("MISSING", path, lineno, ref, "显式路径不可达")

            # --- 2. 裸文件名 .sentences.md ---
            if not archives:
                continue
            # 本行提到的归档目录：优先取「显式说明」里的，其次取技能兜底
            tags_here = [t for t in archives if t in line]
            if not tags_here and default_tag:
                tags_here = [default_tag]
            if not tags_here:
                continue
            for m in BARE_SENTENCES.finditer(line):
                name = m.group("n") + ".sentences.md"
                # 若该行已有显式路径命中同一个名字，跳过（避免重复计）
                if hit_path and "/" in line and name in line:
                    continue
                res.checked += 1
                if "..." in name:
                    res.add("PLACEHOLDER", path, lineno, name,
                            "省略号占位——需补全真实文件名")
                    continue
                target = None
                for t in tags_here:
                    if name in archives[t]:
                        target = archives[t][name]
                        break
                if target is None:
                    res.add("MISSING", path, lineno, name,
                            f"归档目录下无此文件（查过: {', '.join(tags_here)}）")
                    continue
                # 行号校验：`:NNN` 指向的句子是否仍存在（改档会漂移）
                claimed = m.group("ln")
                if claimed and target.suffix.lower() == ".md":
                    total = len(target.read_text(encoding="utf-8",
                                                errors="replace").splitlines())
                    res.line_checked += 1
                    n = int(claimed)
                    if n < 1 or n > total:
                        res.add("LINE_OOB", path, lineno, f"{name}:{claimed}",
                                f"行号超出文件总行数 {total}（改档后漂移）")
                    else:
                        res.line_map.append(
                            (str(path.relative_to(REPO)).replace("\\", "/"),
                             lineno, name, n, total))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skill", action="append", default=None,
                    help="仅扫描指定技能（可重复）")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出")
    ap.add_argument("--quiet", action="store_true", help="只打印结论行")
    args = ap.parse_args(argv)

    skills = args.skill or DEFAULT_SKILLS
    res = Result()
    archives = _archive_index()
    for s in skills:
        check_skill(s, res, archives)

    findings = res.rows
    if args.json:
        print(json.dumps({"checked": res.checked,
                          "line_checked": res.line_checked,
                          "findings": findings},
                         ensure_ascii=False, indent=2))
    else:
        if not args.quiet:
            print(f"repo = {REPO}")
            print(f"skills = {', '.join(skills)}")
            print(f"checked refs = {res.checked}"
                  f" (line-numbered = {res.line_checked})")
            print()
        if findings:
            for f in findings:
                print(f"[{f['kind']}] {f['file']}:{f['line']}")
                print(f"    ref: {f['ref']}")
                if f["note"]:
                    print(f"    note: {f['note']}")
        print()
        if findings:
            n_miss = sum(1 for f in findings if f["kind"] == "MISSING")
            n_ph = sum(1 for f in findings if f["kind"] == "PLACEHOLDER")
            n_oob = sum(1 for f in findings if f["kind"] == "LINE_OOB")
            print(f"REFERENCE INTEGRITY FAILED ({len(findings)}): "
                  f"MISSING={n_miss} PLACEHOLDER={n_ph} LINE_OOB={n_oob}")
            return 1
        print(f"ALL REFERENCE CHECKS PASSED "
              f"({res.checked} refs, {res.line_checked} line-numbered)")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
