#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill_pointer_check.py — 全库 skill 相对路径存在性校验（标准库实现）。

三条解析基准（覆盖历史上出现的三类写法，各自可解释）：

  基准 A（文件自身目录 / file directory）
      - 裸文件名（目标不含 `/`，如 `hooks.md`）
      - 以 `./` / `../` 开头、且二级段不是其他 skill 的路径
        （如同级或父级的自 skill 路径 `../packs/`、`../hooks/22-*.md`）
      解析：相对**该文件自身所在目录**。

  基准 B（语料内部模块 / <skill>/corpus/）
      - 一级段属于语料内部模块名（hooks / tensions / stakes / literature-turns /
        theory-lens / previews / research-questions / contributions / transitions /
        differentiation / phrasebank / micro-templates / _skeleton / packs /
        contrast-pairs / storytelling / variants / subprotocols / sentences / meta）
      解析：相对 **<skill>/corpus/**。
      依据：write-introduction/references/render-rules.md:4 的既有声明。

  基准 C（skill 目录 = SKILL.md 所在目录 / skill directory）
      - 以 `corpus/` / `references/` / `scripts/` 开头
      - 至其他兄弟目录的指针 `../<sibling>/...`（含无 SKILL.md 的共享资源
        目录，如 `story-blueprints`）
      解析：相对 **该文件所属 skill 目录**（不是文件所在目录）。

排除项：围栏代码块（``` / ~~~ 之间）内的行、http/https/mailto 等协议、纯锚点、
含空格的短语、含通配/占位符的模板串。

输出：按 skill 分组，每行
    file:line | 目标 | 命中基准 A/B/C | 解析后路径 | OK/MISSING
末尾汇总 `checked / resolvedA / resolvedB / resolvedC / missing`；MISSING 再分两桶：
    unresolved_no_baseline  三条基准都不成立（基准选择问题）
    unresolved_missing_file 命中了基准但目标文件确实不存在（真断链）
存在 MISSING 时 exit code 1。

用法：
    python skill_pointer_check.py                       # 全部含 SKILL.md 的 skill
    python skill_pointer_check.py write-theory write-results
    python skill_pointer_check.py --missing-only        # 只打印 MISSING 行
    python skill_pointer_check.py --limit 6             # 每个 skill 最多打印 N 行
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# markdown 链接：[](path) / [](<path>) / [](path "title")
LINK_RE = re.compile(r"\]\(\s*<?([^)\n>]+?)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
# 行内反引号（不含换行）
BACKTICK_RE = re.compile(r"`([^`\n]+)`")

# 语料内部模块名（基准 B 的一级段）；依据 render-rules.md:4
CORPUS_MODULES = {
    "hooks", "tensions", "stakes", "literature-turns", "theory-lens", "previews",
    "research-questions", "contributions", "transitions", "differentiation",
    "phrasebank", "micro-templates", "_skeleton", "packs", "contrast-pairs",
    "storytelling", "variants", "subprotocols", "sentences", "meta",
}
# skill 目录基准的显式前缀（基准 C）
SKILL_PREFIXES = {"corpus", "references", "scripts"}

# 行尾可剥除的标点（ASCII + 全角）
TRAILING_PUNCT = (
    ".,;:!?)]}>\u2019\u201d'"
    "\u3002\uff0c\u3001\uff1b\uff1a\uff01\uff1f\uff09\u3011\u300b\u300d\u2026\u00b7"
)
# 中文标点：出现在路径里即判为非路径（自然语言）
CJK_PUNCT = set(
    "\u3002\uff0c\u3001\uff1b\uff1a\uff01\uff1f\uff08\uff09\u3010\u3011\u300a\u300b"
    "\u300c\u300d\u300e\u300f\u201c\u201d\u2018\u2019\u2026\u2014\uff5e\u00b7"
)
# 通配 / 占位符 / 代码字符：命中即判为非具体路径模板
BAD_CHARS = set("[]{}<>*?|=\"'`^")

# 包装对（成对出现时剥除）
WRAPS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    "\uff08": "\uff09",
    "\u3010": "\u3011",
    "\u300a": "\u300b",
    "\u300c": "\u300d",
    "\u201c": "\u201d",
    "\u2018": "\u2019",
}

KNOWN_EXT = {
    ".md", ".markdown", ".txt", ".rst", ".py", ".pyi", ".sh", ".ps1", ".js",
    ".ts", ".json", ".jsonl", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".csv", ".tsv", ".sql", ".ipynb", ".do", ".ado",
}

SCHEMES = (
    "http://", "https://", "mailto:", "ftp://", "ftps://", "tel:", "data:",
    "javascript:", "file://",
)


def normalize(raw: str) -> str | None:
    """把原始捕获串规整为待解析的相对路径；不合格返回 None。"""
    s = raw.strip()
    if not s:
        return None
    # <path> 尖括号包裹
    if len(s) >= 2 and s[0] == "<" and s[-1] == ">":
        s = s[1:-1].strip()

    low = s.lower()
    if any(low.startswith(p) for p in SCHEMES) or "://" in s:
        return None
    if s.startswith("#"):  # 纯锚点
        return None
    if re.search(r"\s", s):  # 含空格的自然是自然语言
        return None

    # 剥掉 #锚点 后缀
    s = s.split("#", 1)[0].strip()
    # 剥掉成对包装
    while len(s) >= 2 and s[0] in WRAPS and s[-1] == WRAPS[s[0]]:
        s = s[1:-1].strip()
    # 剥掉行尾标点
    s = s.rstrip(TRAILING_PUNCT).strip()
    if not s:
        return None

    if any(ch in CJK_PUNCT for ch in s):
        return None
    if any(ch in BAD_CHARS for ch in s):
        return None

    has_slash = "/" in s or "\\" in s
    if not has_slash and Path(s).suffix.lower() not in KNOWN_EXT:
        # 既无目录分隔、又无已知扩展名（如 `is/are`、`show/demonstrate`）→ 非路径
        return None
    s = s.replace("\\", "/")

    # 末段必须是已知扩展名的文件，或以 `/` 结尾的目录；否则视为自然语言/占位
    last = s.rsplit("/", 1)[-1]
    if not s.endswith("/") and Path(last).suffix.lower() not in KNOWN_EXT:
        return None
    if s.endswith("//") or "//" in s:
        return None

    return s


def is_sibling_skill(seg: str) -> bool:
    """ROOT 下是否存在同名兄弟目录（skill 或共享资源目录，如 story-blueprints）。

    判定放宽为「ROOT 下同名目录」：`../hooks/` 等自 skill 语料模块不在 ROOT 下，
    仍落到基准 A；只有 `../<sibling>/`（含无 SKILL.md 的共享目录）才落到基准 C。
    """
    if seg in (".", "..") or not seg:
        return False
    return (ROOT / seg).is_dir()


def skill_root_of(md: Path) -> Path:
    """向上找到最近的含 SKILL.md 的祖先目录；找不到返回 ROOT。"""
    cur = md.parent
    while cur != cur.parent:
        if (cur / "SKILL.md").is_file():
            return cur
        if cur == ROOT:
            break
        cur = cur.parent
    return ROOT


def classify(target: str) -> str | None:
    """按写法判定命中的基准：'A' / 'B' / 'C' / None（三基准都不成立）。"""
    if target.startswith("../"):
        seg = target[3:].split("/", 1)[0]
        if is_sibling_skill(seg):
            return "C"
        return "A"
    if target.startswith("./"):
        return "A"
    if "/" not in target:
        return "A"
    seg = target.split("/", 1)[0]
    if seg in CORPUS_MODULES:
        return "B"
    if seg in SKILL_PREFIXES:
        return "C"
    return None


def resolve(rule: str, target: str, md: Path, skill_root: Path) -> Path:
    if rule == "A":
        return (md.parent / target).resolve()
    if rule == "B":
        return (skill_root / "corpus" / target).resolve()
    return (skill_root / target).resolve()


def extract(text: str):
    """产出 (line_no, target)；跳过围栏代码块内的行。"""
    out = []
    in_fence = False
    fence_char = None
    for line_no, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if m:
            ch = m.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = ch
            elif ch == fence_char:
                in_fence = False
                fence_char = None
            continue
        if in_fence:
            continue
        seen = set()
        for m in LINK_RE.finditer(line):
            t = normalize(m.group(1))
            if t and t not in seen:
                seen.add(t)
                out.append((line_no, t))
        for m in BACKTICK_RE.finditer(line):
            t = normalize(m.group(1))
            if t and t not in seen:
                seen.add(t)
                out.append((line_no, t))
    return out


def find_skills() -> list[Path]:
    return [d for d in sorted(ROOT.iterdir()) if d.is_dir() and (d / "SKILL.md").is_file()]


def main(argv=None) -> int:
    # 保证 CJK / 全角路径输出不受 Windows 区域编码影响
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description="skill 相对路径存在性校验")
    ap.add_argument("skills", nargs="*", help="限定 skill 目录名（默认全部含 SKILL.md 的目录）")
    ap.add_argument("--missing-only", action="store_true", help="只打印 MISSING 行")
    ap.add_argument("--limit", type=int, default=0, help="每个 skill 最多打印 N 行（0=全部）")
    args = ap.parse_args(argv)

    if args.skills:
        targets = []
        for name in args.skills:
            d = ROOT / name
            if not d.is_dir():
                ap.error(f"skill 目录不存在: {name}")
            targets.append(d)
    else:
        targets = find_skills()

    checked = missing = 0
    rules_ok = {"A": 0, "B": 0, "C": 0}
    no_baseline = 0
    file_absent = 0
    for skill in targets:
        lines = []
        for md in sorted(skill.rglob("*.md")):
            try:
                text = md.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                text = md.read_text(encoding="utf-8", errors="replace")
            skill_root = skill_root_of(md)
            for line_no, target in extract(text):
                rule = classify(target)
                checked += 1
                if rule is None:
                    missing += 1
                    no_baseline += 1
                    status, path = "MISSING", None
                else:
                    path = resolve(rule, target, md, skill_root)
                    if path.exists():
                        rules_ok[rule] += 1
                        status = "OK"
                    else:
                        missing += 1
                        file_absent += 1
                        status = "MISSING"
                if status == "OK" and args.missing_only:
                    continue
                rel = md.resolve().relative_to(ROOT) if ROOT in md.resolve().parents else md
                rel_s = str(rel).replace("\\", "/")
                path_s = str(path).replace("\\", "/") if path is not None else "-"
                rule_s = rule if rule is not None else "-"
                lines.append(f"{rel_s}:{line_no} | {target} | {rule_s} | {path_s} | {status}")
        if lines:
            if not args.missing_only:
                print(f"=== {skill.name} ===")
            if args.limit and len(lines) > args.limit:
                shown = lines[: args.limit]
                print("\n".join(shown))
                print(f"... ({len(lines) - args.limit} more lines omitted)")
            else:
                print("\n".join(lines))
    print("-" * 72)
    print(
        f"checked={checked} resolvedA={rules_ok['A']} resolvedB={rules_ok['B']} "
        f"resolvedC={rules_ok['C']} missing={missing}"
    )
    print(f"  unresolved_no_baseline={no_baseline} unresolved_missing_file={file_absent}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
