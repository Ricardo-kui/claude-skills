#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_blueprints.py — story-blueprints 语料校验器（schema v0.3）

对照 `../_schema.md` 逐份校验 blueprint，捕获数据层漂移：

  1. 文件头必填字段（id / paper / distilled_sections / source_records）
  2. Story 节完整性（one_liner / knot / characters / resolution_logic /
     five_acts / stakes / alternative_tellings / storytelling_tools）
  3. knot 字段齐全 + primary_type / compound_types 属于 knot 类型表
  4. resolution_logic 内联类型可识别（resolution 6 型）
  5. blueprints/ 文件 与 _index.md 1:1 同步（id、状态列）
  6. knot 主型计数 vs _schema 类型表「原型状态」列对账（WARN 级）

容忍：字段值含「待补」合法；vault_reports / paper_type / cross_paper_notes
为可选字段（单独统计采纳率，不作硬性要求）。

退出码：0 = 无 ERROR；1 = 存在 ERROR（WARN 不影响退出码）。

用法：
    python scripts/validate_blueprints.py            # 从 story-blueprints/ 运行
    python story-blueprints/scripts/validate_blueprints.py   # 从 skills 根运行
"""

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("缺少依赖 PyYAML：pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# 管道/重定向下保证 UTF-8 输出，规避 Windows GBK 崩溃
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parent.parent
BLUEPRINTS_DIR = ROOT / "blueprints"
INDEX_PATH = BLUEPRINTS_DIR / "_index.md"
SCHEMA_PATH = ROOT / "_schema.md"

REQUIRED_HEADER = ("id", "paper", "distilled_sections", "source_records")
REQUIRED_STORY = (
    "one_liner", "knot", "characters", "resolution_logic", "five_acts",
    "stakes", "alternative_tellings", "storytelling_tools",
)
KNOT_FIELDS = (
    "primary_type", "compound_types", "statement", "tied_at",
    "untied_at", "antagonist", "antagonist_built_by",
)
KNOT_TYPES = {
    "paradox", "irony-reversal", "paradigms-at-war", "consensus-puzzle",
    "counterevidence", "neglected-arena", "assumption-flip",
    "tangled-constructs", "half-domain-gap", "overlooked-alternative",
    "cross-domain-unification",
}
RESOLUTION_TYPES = (
    "arbitration", "revelation", "exploration", "unification",
    "dimension-split", "remedy",
)
PAPER_TYPES = ("quantitative", "qualitative", "theory")
SECTION_TYPES = {"intro", "theory", "methods", "results"}
INDEX_STATUS = {"ROBUST", "PARTIAL"}
CN_NUM = {"九": 9, "八": 8, "七": 7, "六": 6, "五": 5, "四": 4, "三": 3, "二": 2, "单": 1}
CONFLICT_MARKERS = (
    "？", "?", "vs", "versus",
    "但", "但是", "然而", "却", "反而", "相反", "反转", "翻转",
    "对立", "冲突", "矛盾", "张力", "悖论",
    "挑战", "争议", "推翻", "颠覆", "忽视", "忽略", "空白",
    "conventional wisdom", "no study", "under-researched",
    "→", "->", "——",
)


# ---------- 解析工具 ----------

def _split_sections(text: str) -> Dict[str, str]:
    """按 ## / ### 标题切分 markdown 为 {标题: 正文}。"""
    parts = re.split(r"^#{2,3}\s+(.+?)\s*$", text, flags=re.M)
    sections: Dict[str, str] = {}
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i].strip()] = parts[i + 1]
    return sections


def _yaml_block(text: str) -> Tuple[Optional[dict], Optional[str]]:
    """取 ```yaml 代码块并解析；返回 (data, error)。"""
    m = re.search(r"```(?:yaml)?\s*\n(.*?)```", text, re.DOTALL)
    if not m:
        return None, "未找到 yaml 代码块"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, f"yaml 解析失败: {e}"
    if not isinstance(data, dict):
        return None, "yaml 块不是映射"
    return data, None


def _has_conflict(statement: str) -> bool:
    """启发式：statement 应含冲突双方（问句 / 对立标记 / 足够长）。"""
    if len(statement) < 15:
        return False
    low = statement.lower()
    return any(m in low for m in CONFLICT_MARKERS)


def _has_section(sections: Dict[str, str], canonical: str) -> bool:
    """节是否存在；容忍标题带括号注解（如 storytelling_tools（Ch03））。"""
    return any(
        h == canonical or h.startswith(canonical + "（") or h.startswith(canonical + "(")
        for h in sections
    )


def _find_section(sections: Dict[str, str], canonical: str) -> str:
    """取节正文；标题带括号注解时同样命中。"""
    for head, body in sections.items():
        if head == canonical or head.startswith(canonical + "（") or head.startswith(canonical + "("):
            return body
    return ""


# ---------- 逐份校验 ----------

def _validate_file(path: Path, issues: List[Tuple[str, str, str]]) -> Optional[dict]:
    name = path.name
    text = path.read_text(encoding="utf-8")
    sections = _split_sections(text)

    # 文件头
    header_data, err = _yaml_block(_find_section(sections, "文件头"))
    if err:
        issues.append(("ERROR", name, f"文件头 {err}"))
        return None
    for key in REQUIRED_HEADER:
        if key not in header_data:
            issues.append(("ERROR", name, f"文件头缺必填字段 {key}"))
    bid = header_data.get("id", "")
    if not bid:
        issues.append(("ERROR", name, "id 为空"))

    paper_type = header_data.get("paper_type")
    if paper_type is not None and paper_type not in PAPER_TYPES:
        issues.append(("ERROR", name, f"paper_type 非法: {paper_type!r}"))

    ds = header_data.get("distilled_sections")
    if isinstance(ds, list):
        bad = [x for x in ds if x not in SECTION_TYPES]
        if bad:
            issues.append(("WARN", name, f"distilled_sections 含未知区段: {bad}"))

    # Story 节
    missing = [s for s in REQUIRED_STORY if not _has_section(sections, s)]
    if missing:
        issues.append(("ERROR", name, f"缺 Story 节: {missing}"))

    # knot
    primary_type = None
    knot_text = _find_section(sections, "knot")
    if len(re.findall(r"^\s*primary_type\s*:", knot_text, re.M)) > 1:
        issues.append(("WARN", name, "knot 节内 primary_type 出现多次"))
    knot_data, kerr = _yaml_block(knot_text)
    if kerr:
        issues.append(("ERROR", name, f"knot {kerr}"))
    elif knot_data is not None:
        # yaml 顶层可能嵌套在 `knot:` 下（与文件头平铺格式不同）
        if "knot" in knot_data and isinstance(knot_data["knot"], dict):
            knot_data = knot_data["knot"]
        for field in KNOT_FIELDS:
            if field not in knot_data:
                issues.append(("ERROR", name, f"knot 缺字段 {field}"))
        primary_type = knot_data.get("primary_type")
        if primary_type not in KNOT_TYPES:
            issues.append(("ERROR", name, f"knot.primary_type 不在类型表: {primary_type!r}"))
        ct = knot_data.get("compound_types") or []
        if isinstance(ct, str):
            ct = [ct]
        for c in ct:
            if c not in KNOT_TYPES:
                issues.append(("ERROR", name, f"knot.compound_types 含非法类型: {c!r}"))
        statement = knot_data.get("statement", "")
        if not _has_conflict(statement):
            issues.append(("WARN", name, "knot.statement 可能不含冲突双方（问句/对立标记）"))

    # resolution
    res_text = _find_section(sections, "resolution_logic")
    if res_text:
        m = re.search(r"`(" + "|".join(RESOLUTION_TYPES) + r")`", res_text) or \
            re.search(r"\b(" + "|".join(RESOLUTION_TYPES) + r")\b", res_text)
        if not m:
            issues.append(("WARN", name, f"resolution_logic 无法识别 6 型之一（当前文本前 40 字: {res_text[:40]!r}）"))

    return {
        "file": name,
        "id": bid,
        "primary_type": primary_type,
        "has_paper_type": paper_type is not None,
        "has_vault_reports": "vault_reports" in header_data,
        "has_cross_paper_notes": _has_section(sections, "cross_paper_notes"),
    }


# ---------- 索引同步 ----------

def _parse_index(path: Path) -> List[tuple]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*([a-z0-9_]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
        if not m:
            continue
        if m.group(1) == "id" and m.group(2).strip() == "论文":
            continue  # 表头行
        rows.append((m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)))
    return rows


# ---------- schema 类型表计数 ----------

def _parse_schema_counts(schema_text: str) -> Dict[str, Optional[int]]:
    """读 _schema.md knot 类型表第 3 列（原型状态）→ {类型: 声明计数或 None}。"""
    declared: Dict[str, Optional[int]] = {}
    for line in schema_text.splitlines():
        m = re.match(r"^\|\s*`([a-z-]+)`[^|]*\|\s*[^|]*?\|\s*([^|]*?)\s*\|", line)
        if not m:
            continue
        t, status = m.group(1), m.group(2).strip()
        for cn, num in CN_NUM.items():
            if f"{cn}原型" in status:
                declared[t] = num
                break
        else:
            if "compound-only" in status or "待建" in status or "未定" in status:
                declared[t] = 0
            else:
                declared[t] = None
    return declared


# ---------- 主流程 ----------

def main() -> int:
    issues: List[Tuple[str, str, str]] = []

    bp_files = sorted(p for p in BLUEPRINTS_DIR.glob("*.md") if p.name != "_index.md")
    if not bp_files:
        print("未在 blueprints/ 找到任何 blueprint 文件", file=sys.stderr)
        return 1

    records: List[dict] = []
    for path in bp_files:
        rec = _validate_file(path, issues)
        if rec:
            records.append(rec)

    # 索引同步
    index_rows = _parse_index(INDEX_PATH)
    index_ids = [r[0] for r in index_rows]
    id_to_files: Dict[str, List[str]] = {}
    for rec in records:
        id_to_files.setdefault(rec["id"], []).append(rec["file"])
    for idx_id in index_ids:
        files = id_to_files.get(idx_id, [])
        if not files:
            issues.append(("ERROR", "_index.md", f"索引行无对应文件: {idx_id}"))
        elif len(files) > 1:
            issues.append(("ERROR", "_index.md", f"索引 id {idx_id} 命中多个文件: {files}"))
    for rec in records:
        if rec["id"] not in index_ids:
            issues.append(("ERROR", rec["file"], f"blueprint id={rec['id']} 未收录进 _index.md"))
    for row in index_rows:
        if row[4] not in INDEX_STATUS:
            issues.append(("WARN", "_index.md", f"状态列非法: {row[0]} -> {row[4]!r}"))

    # 主型计数对账
    counts = Counter(r["primary_type"] for r in records if r["primary_type"])
    declared = _parse_schema_counts(SCHEMA_PATH.read_text(encoding="utf-8"))
    total = sum(counts.values())
    for t in sorted(set(KNOT_TYPES) | set(counts) | set(declared)):
        d, c = declared.get(t), counts.get(t, 0)
        if d is not None and d != c:
            issues.append(("WARN", "_schema.md", f"knot 主型计数对账: {t} 类型表声明 {d} / 实测 {c}"))

    # 可选字段采纳率
    n = len(records)
    n_pt = sum(1 for r in records if r["has_paper_type"])
    n_vr = sum(1 for r in records if r["has_vault_reports"])
    n_cp = sum(1 for r in records if r["has_cross_paper_notes"])

    # 输出
    errors = [i for i in issues if i[0] == "ERROR"]
    warns = [i for i in issues if i[0] == "WARN"]

    print("=" * 72)
    print("validate_blueprints.py — story-blueprints 语料校验（schema v0.3）")
    print("=" * 72)
    print(f"blueprint 文件: {n}  索引行: {len(index_rows)}")
    print(f"可选字段采纳率: paper_type {n_pt}/{n} | vault_reports {n_vr}/{n} | cross_paper_notes {n_cp}/{n}")
    print()
    print("knot 主型分布（primary_type 实测 / 类型表声明）:")
    for t in sorted(set(counts) | set(declared)):
        c = counts.get(t, 0)
        d = declared.get(t)
        if c or d is not None:
            flag = "" if d is None or d == c else f"  <- 表声明 {d}"
            print(f"  {t:<28} {c}{flag}")
    print(f"  合计 {total}（应与 blueprint 文件数一致）")
    print()

    if issues:
        for sev, name, msg in issues:
            print(f"  [{sev}] {name}: {msg}")
        print()

    print(f"汇总: ERROR {len(errors)} | WARN {len(warns)}")
    if errors:
        print("结论: 存在 ERROR（退出码 1）")
        return 1
    print("结论: 无 ERROR（退出码 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
