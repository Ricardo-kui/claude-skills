#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill_pointer_check.py — 全库 skill 相对路径存在性校验（标准库实现）。

四条解析基准（覆盖历史上出现的四类写法，各自可解释）：

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

  基准 D（仓库根 / repository root）
      - 以 ROOT 直属目录名开头、且当前 skill 下没有同名子目录的写法
        （如 `story-blueprints/...`、`write-theory/...` 这类「仓库根相对」写法）
      解析：相对 **仓库根 ROOT**。
      「影子守卫」：若当前 skill 下也存在同名子目录（`<skill_root>/<seg>/`），
      则即使 ROOT 下同名目录存在，仍判基准 C（相对本 skill 目录），避免把
      skill 内部同名子目录误解析到仓库根。

书写约定裁定（2026-09-15）：新增 / 重写的跨 skill 指针一律显式写成
`../<sibling>/...`（走基准 C，无歧义）；不得在新增 / 重写中引入裸
`sibling/...`。既有裸写法存量由基准 D 兜底，不做全库批量规范化。

排除项：围栏代码块（``` / ~~~ 之间）内的行、http/https/mailto 等协议、纯锚点、
含空格的短语、含通配/占位符的模板串。

输出：按 skill 分组，每行
    file:line | 目标 | 命中基准 A/B/C | 解析后路径 | OK/MISSING
末尾汇总 `checked / resolvedA / resolvedB / resolvedC / resolvedD / missing`；MISSING 再分两桶：
    unresolved_no_baseline  三条基准都不成立（基准选择问题）
    unresolved_missing_file 命中了基准但目标文件确实不存在（真断链）
存在 MISSING 时 exit code 1。

用法：
    python skill_pointer_check.py                       # 全部含 SKILL.md 的 skill
    python skill_pointer_check.py write-theory write-results
    python skill_pointer_check.py --missing-only        # 只打印 MISSING 行
    python skill_pointer_check.py --limit 6             # 每个 skill 最多打印 N 行
    python skill_pointer_check.py --strict              # 严格基准：其余写法按 C
    python skill_pointer_check.py --whitelist _shared/pointer-allowlist.txt
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
# 仓库根直属、无 SKILL.md 的共享资源目录：纳入默认扫描，目标按基准 D 解析
SHARED_ROOTS = ("story-blueprints",)

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

    该谓词同时是基准 D 的判据：ROOT 下存在同名目录（且当前 skill 下无同名子目录）
    时，裸 `sibling/...` 写法按基准 D 相对仓库根解析（影子守卫见 classify()）。
    """
    if seg in (".", "..") or not seg:
        return False
    return (ROOT / seg).is_dir()


def skill_root_of(md: Path) -> Path:
    """向上找到最近的含 SKILL.md 的祖先目录。

    找不到时回退到「ROOT 直属子目录」作为 skill 目录（覆盖 story-blueprints
    这类无 SKILL.md 的共享资源目录），再回退到 ROOT。
    """
    md = Path(md).resolve()
    cur = md.parent
    top = None
    while cur != cur.parent:
        if (cur / "SKILL.md").is_file():
            return cur
        if cur.parent == ROOT:
            top = cur
        if cur == ROOT:
            break
        cur = cur.parent
    return top or ROOT


def classify(target: str, strict: bool = False, skill_root: Path | None = None) -> str | None:
    """按写法判定命中的基准：'A' / 'B' / 'C' / 'D' / None（各基准都不成立）。

    strict=True 时把「其余」写法按 C（skill 目录）解析，不再产生 None。
    skill_root 用于影子守卫：当前 skill 下有同名子目录时，裸 `seg/...` 不判 D。
    """
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
    if (ROOT / seg).is_dir() and (skill_root is None or not (skill_root / seg).is_dir()):
        return "D"
    return "C" if strict else None


def resolve(rule: str, target: str, md: Path, skill_root: Path) -> Path:
    if rule == "A":
        return (md.parent / target).resolve()
    if rule == "B":
        return (skill_root / "corpus" / target).resolve()
    if rule == "D":
        return (ROOT / target).resolve()
    return (skill_root / target).resolve()


def load_whitelist(path: str | None) -> set[str]:
    """读取白名单：每行 `target | 理由`；忽略空行与 `#` 注释。

    key 取 ` | ` 之前的精确 target 串，与 MISSING 行的 target 做等值匹配。
    """
    if not path:
        return set()
    keys: set[str] = set()
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return keys
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        key = s.split(" | ", 1)[0].strip()
        if key:
            keys.add(key)
    return keys


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
    return [d for d in sorted(ROOT.iterdir()) if d.is_dir() and (d / "SKILL.md").is_file()] + [
        ROOT / n for n in SHARED_ROOTS if (ROOT / n).is_dir() and not (ROOT / n / "SKILL.md").is_file()
    ]


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
    ap.add_argument("--strict", action="store_true", help="严格基准：其余写法按 C（skill 目录）解析")
    ap.add_argument("--whitelist", default=None, help="白名单文件（每行 `target | 理由`）")
    args = ap.parse_args(argv)
    whitelist = load_whitelist(args.whitelist)

    if args.skills:
        targets = []
        for name in args.skills:
            d = ROOT / name
            if not d.is_dir():
                ap.error(f"skill 目录不存在: {name}")
            targets.append(d)
    else:
        targets = find_skills()

    checked = missing = whitelisted = 0
    rules_ok = {"A": 0, "B": 0, "C": 0, "D": 0}
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
                rule = classify(target, args.strict, skill_root)
                checked += 1
                if rule is None:
                    status, path, bucket = "MISSING", None, "no_baseline"
                else:
                    path = resolve(rule, target, md, skill_root)
                    if path.exists():
                        rules_ok[rule] += 1
                        status, bucket = "OK", None
                    else:
                        status, path, bucket = "MISSING", path, "file_absent"
                if status == "MISSING" and target in whitelist:
                    status, path, bucket = "WHITELIST", None, None
                    whitelisted += 1
                if bucket == "no_baseline":
                    missing += 1
                    no_baseline += 1
                elif bucket == "file_absent":
                    missing += 1
                    file_absent += 1
                if args.missing_only and status in ("OK", "WHITELIST"):
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
        f"resolvedC={rules_ok['C']} resolvedD={rules_ok['D']} missing={missing} whitelisted={whitelisted}"
    )
    print(f"  unresolved_no_baseline={no_baseline} unresolved_missing_file={file_absent}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
