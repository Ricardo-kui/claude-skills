#!/usr/bin/env python3
"""Create an Obsidian literature-note scaffold with stable metadata and layout."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import unicodedata
from datetime import date
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONFIG_PATH = SKILL_DIR / "config.json"


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


CONFIG = load_config()

COMMON_NOTE_DIRS = CONFIG.get(
    "notes_dir_candidates",
    ["literature", "literature_notes", "papers", "reading"],
)

DEFAULT_VAULT_ROOT = Path(CONFIG.get("vault_root", r"D:\Onedrive\Obsidian Vault"))
DEFAULT_ZOTERO_DB = Path(CONFIG.get("zotero_db", r"D:\同步文件\文献库\zotero.sqlite"))
DEFAULT_TAGS = ",".join(CONFIG.get("default_tags", ["source", "literature-note"]))


def to_ascii_token(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = re.sub(r"[^A-Za-z0-9]+", "", ascii_text)
    return ascii_text


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_authors(value: str | None) -> list[str]:
    if not value:
        return []
    normalized = re.sub(r"\s+(and|&)\s+", ";", value, flags=re.IGNORECASE)
    return [item.strip() for item in normalized.split(";") if item.strip()]


def safe_slug(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text).strip().lower()
    normalized = re.sub(r'[<>:"/\\|?*]+', " ", normalized)
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    normalized = normalized.strip("-. ")
    return normalized[:80] or "untitled-paper"


def normalize_lookup(text: str | None) -> str:
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKC", text).replace("\u00ad", "").casefold()
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = re.sub(r"[^\w]+", " ", normalized)
    return normalized.strip()


def first_author_key(authors: list[str]) -> str:
    if not authors:
        return ""
    first = authors[0]
    pieces = re.split(r"\s+", first.strip())
    token = pieces[-1] if pieces else first
    token = re.sub(r'[<>:"/\\|?*]+', "", token)
    return safe_slug(token)


def surname_token(author: str) -> str:
    pieces = re.split(r"\s+", author.strip())
    token = pieces[-1] if pieces else author
    cleaned = to_ascii_token(token)
    if not cleaned:
        cleaned = to_ascii_token(author) or "Author"
    return cleaned[:1].upper() + cleaned[1:]


def default_citekey(authors: list[str], year: str) -> str:
    clean_year = re.sub(r"[^0-9]", "", year or "")
    if not authors:
        return clean_year
    if len(authors) == 1:
        return f"{surname_token(authors[0])}{clean_year}"
    if len(authors) == 2:
        return f"{surname_token(authors[0])}{surname_token(authors[1])}{clean_year}"
    return f"{surname_token(authors[0])}EtAl{clean_year}"


def default_aliases(authors: list[str], year: str, citekey: str) -> list[str]:
    aliases: list[str] = []
    if citekey:
        aliases.append(citekey)
    clean_year = re.sub(r"[^0-9]", "", year or "")
    if authors and clean_year:
        if len(authors) == 1:
            aliases.append(f"{surname_token(authors[0])} ({clean_year})")
        elif len(authors) == 2:
            aliases.append(f"{surname_token(authors[0])} and {surname_token(authors[1])} ({clean_year})")
        else:
            aliases.append(f"{surname_token(authors[0])} et al. ({clean_year})")
    return aliases


def resolve_notes_dir(vault_root: str | None, notes_dir: str | None) -> Path:
    if notes_dir:
        return Path(notes_dir).expanduser()

    if vault_root:
        root = Path(vault_root).expanduser()
    else:
        root = DEFAULT_VAULT_ROOT

    for dirname in COMMON_NOTE_DIRS:
        candidate = root / dirname
        if candidate.exists():
            return candidate

    return root / "literature_notes"


def build_filename(title: str, authors: list[str], year: str, citekey: str | None) -> str:
    title_slug = safe_slug(title)

    if citekey:
        prefix = safe_slug(citekey)
    else:
        author_key = first_author_key(authors)
        if author_key and year:
            prefix = f"{author_key}{year}"
        elif year:
            prefix = safe_slug(year)
        else:
            prefix = ""

    if prefix:
        return f"{prefix}-{title_slug}.md"
    return f"{title_slug}.md"


def quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str], indent: int = 0) -> str:
    prefix = " " * indent
    if not values:
        return f"{prefix}[]"
    lines = [f"{prefix}- {quote(value)}" for value in values]
    return "\n".join(lines)


def markdown_link(label: str, target: str) -> str:
    if not target:
        return ""
    return f"[{label}]({target})"


def resolve_zotero_db(zotero_db: str | None) -> Path | None:
    if zotero_db:
        candidate = Path(zotero_db).expanduser()
    else:
        candidate = DEFAULT_ZOTERO_DB
    return candidate if candidate.exists() else None


def zotero_library_path(conn: sqlite3.Connection, library_id: int | None) -> str:
    if not library_id:
        return "library"
    row = conn.execute(
        "SELECT type FROM libraries WHERE libraryID = ?",
        (library_id,),
    ).fetchone()
    if not row or row[0] == "user":
        return "library"
    if row[0] == "group":
        group = conn.execute(
            "SELECT groupID FROM groups WHERE libraryID = ?",
            (library_id,),
        ).fetchone()
        if group:
            return f"groups/{group[0]}"
    return "library"


def build_zotero_bundle(
    conn: sqlite3.Connection,
    item_key: str | None,
    attachment_key: str | None,
    library_id: int | None,
) -> dict[str, str]:
    library_path = zotero_library_path(conn, library_id)
    return {
        "item_key": item_key or "",
        "attachment_key": attachment_key or "",
        "select_uri": f"zotero://select/{library_path}/items/{item_key}" if item_key else "",
        "pdf_uri": f"zotero://open-pdf/{library_path}/items/{attachment_key}" if attachment_key else "",
        "citation_key": "",
        "citation_key_source": "",
    }


def parse_bbt_citation_key(extra_value: str | None) -> str:
    if not extra_value:
        return ""
    patterns = [
        r"(?im)^\s*citation\s*key\s*:\s*(\S+)\s*$",
        r"(?im)^\s*bibtex\s*citation\s*key\s*:\s*(\S+)\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, extra_value)
        if match:
            return match.group(1).strip()
    return ""


def fetch_item_extra(
    conn: sqlite3.Connection,
    item_id: int,
) -> str:
    row = conn.execute(
        """
        SELECT v.value
        FROM itemData d
        JOIN fields f ON f.fieldID = d.fieldID
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE d.itemID = ?
          AND f.fieldName = 'extra'
        LIMIT 1
        """,
        (item_id,),
    ).fetchone()
    return row[0] if row else ""


def fetch_pdf_attachment_for_parent(
    conn: sqlite3.Connection,
    parent_item_id: int,
) -> tuple[str, str] | tuple[None, None]:
    row = conn.execute(
        """
        SELECT child.key, child.libraryID
        FROM itemAttachments att
        JOIN items child ON child.itemID = att.itemID
        WHERE att.parentItemID = ?
          AND att.contentType = 'application/pdf'
        ORDER BY child.itemID
        LIMIT 1
        """,
        (parent_item_id,),
    ).fetchone()
    if not row:
        return None, None
    return row[0], row[1]


def lookup_zotero_by_attachment(
    conn: sqlite3.Connection,
    pdf_path: str | None,
) -> dict[str, str] | None:
    if not pdf_path:
        return None
    basename = Path(pdf_path).name
    row = conn.execute(
        """
        SELECT parent.itemID, parent.key, child.key, parent.libraryID
        FROM itemAttachments att
        JOIN items child ON child.itemID = att.itemID
        LEFT JOIN items parent ON parent.itemID = att.parentItemID
        WHERE att.path = ?
           OR att.path LIKE ?
        ORDER BY child.itemID
        LIMIT 1
        """,
        (f"storage:{basename}", f"%{basename}%"),
    ).fetchone()
    if not row:
        return None
    parent_item_id, parent_key, child_key, library_id = row
    item_key = parent_key or child_key
    attachment_key = child_key
    bundle = build_zotero_bundle(conn, item_key, attachment_key, library_id)
    if parent_item_id:
        citation_key = parse_bbt_citation_key(fetch_item_extra(conn, parent_item_id))
        if citation_key:
            bundle["citation_key"] = citation_key
            bundle["citation_key_source"] = "zotero_bbt"
    return bundle


def lookup_zotero_item_by_doi(
    conn: sqlite3.Connection,
    doi: str | None,
) -> tuple[int, str, int] | None:
    if not doi:
        return None
    row = conn.execute(
        """
        SELECT i.itemID, i.key, i.libraryID
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID
        JOIN fields f ON f.fieldID = d.fieldID
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE f.fieldName = 'DOI'
          AND lower(trim(v.value)) = lower(trim(?))
        LIMIT 1
        """,
        (doi,),
    ).fetchone()
    return row if row else None


def lookup_zotero_item_by_title(
    conn: sqlite3.Connection,
    title: str | None,
) -> tuple[int, str, int] | None:
    if not title:
        return None
    normalized_title = normalize_lookup(title)
    if not normalized_title:
        return None
    exact_row = conn.execute(
        """
        SELECT i.itemID, i.key, i.libraryID
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID
        JOIN fields f ON f.fieldID = d.fieldID
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE f.fieldName = 'title'
          AND lower(v.value) = lower(?)
        LIMIT 1
        """,
        (title,),
    ).fetchone()
    if exact_row:
        return exact_row

    prefix = " ".join(normalized_title.split()[:6])
    rows = conn.execute(
        """
        SELECT i.itemID, i.key, i.libraryID, v.value
        FROM items i
        JOIN itemData d ON d.itemID = i.itemID
        JOIN fields f ON f.fieldID = d.fieldID
        JOIN itemDataValues v ON v.valueID = d.valueID
        WHERE f.fieldName = 'title'
          AND lower(v.value) LIKE ?
        LIMIT 200
        """,
        (f"%{prefix}%",),
    ).fetchall()
    for item_id, item_key, library_id, raw_title in rows:
        if normalize_lookup(raw_title) == normalized_title:
            return item_id, item_key, library_id
    return None


def resolve_zotero_links(
    doi: str | None,
    title: str | None,
    pdf_path: str | None,
    zotero_db: str | None,
    disable_lookup: bool,
) -> dict[str, str]:
    blank = {
        "item_key": "",
        "attachment_key": "",
        "select_uri": "",
        "pdf_uri": "",
        "citation_key": "",
        "citation_key_source": "",
    }
    if disable_lookup:
        return blank
    db_path = resolve_zotero_db(zotero_db)
    if not db_path:
        return blank

    conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    try:
        attachment_match = lookup_zotero_by_attachment(conn, pdf_path)
        if attachment_match:
            return attachment_match

        item_match = lookup_zotero_item_by_doi(conn, doi)
        if not item_match:
            item_match = lookup_zotero_item_by_title(conn, title)
        if not item_match:
            return blank

        item_id, item_key, library_id = item_match
        attachment_key, attachment_library_id = fetch_pdf_attachment_for_parent(conn, item_id)
        bundle = build_zotero_bundle(
            conn,
            item_key,
            attachment_key,
            attachment_library_id or library_id,
        )
        citation_key = parse_bbt_citation_key(fetch_item_extra(conn, item_id))
        if citation_key:
            bundle["citation_key"] = citation_key
            bundle["citation_key_source"] = "zotero_bbt"
        return bundle
    finally:
        conn.close()


def build_frontmatter(
    title: str,
    aliases: list[str],
    authors: list[str],
    year: str,
    journal: str,
    doi: str,
    url: str,
    citekey: str,
    citation_key: str,
    citation_key_source: str,
    pandoc_cite: str,
    zotero_item_key: str,
    zotero_attachment_key: str,
    zotero_select_uri: str,
    zotero_pdf_uri: str,
    reading_mode: str,
    source_type: str,
    reading_stage: str,
    status: str,
    tags: list[str],
    paper_kind: str,
    evidence_grade: str,
    reuse_level: str,
    confidence: str,
    verified: str,
    template: str,
) -> str:
    lines = [
        "---",
        'note_type: literature-note',
        f"title: {quote(title)}",
    ]

    if aliases:
        lines.extend(["aliases:", yaml_list(aliases, indent=2)])
    else:
        lines.append("aliases: []")

    lines.append(f"citekey: {quote(citekey)}")

    if authors:
        lines.extend(["authors:", yaml_list(authors, indent=2)])
    else:
        lines.append("authors: []")

    lines.extend(
        [
            f"year: {quote(year)}",
            f"journal: {quote(journal)}",
            f"doi: {quote(doi)}",
            f"url: {quote(url)}",
            f"citation_key: {quote(citation_key)}",
            f"citation_key_source: {quote(citation_key_source)}",
            f"pandoc_cite: {quote(pandoc_cite)}",
            f"zotero_item_key: {quote(zotero_item_key)}",
            f"zotero_attachment_key: {quote(zotero_attachment_key)}",
            f"zotero_select_uri: {quote(zotero_select_uri)}",
            f"zotero_pdf_uri: {quote(zotero_pdf_uri)}",
            f"paper_kind: {quote(paper_kind)}",
            f"reading_stage: {quote(reading_stage)}",
            f"evidence_grade: {quote(evidence_grade)}",
            f"reuse_level: {quote(reuse_level)}",
            "project_relevance:",
            '  - "{project-slug}"',
            "archive_only: false",
            f"status: {quote(status)}",
            f"created: {quote(str(date.today()))}",
            f"updated: {quote(str(date.today()))}",
            f"reading_mode: {quote(reading_mode)}",
            f"source_type: {quote(source_type)}",
        ]
    )

    if tags:
        lines.extend(["tags:", yaml_list(tags, indent=2)])
    else:
        lines.append("tags: []")

    lines.extend(
        [
            "projects:",
            '  - "{project-slug}"',
            "related: []",
            f"confidence: {quote(confidence)}",
            f"verified: {quote(verified)}",
            f"template: {quote(template)}",
        ]
    )

    lines.append("---")
    return "\n".join(lines)


def build_researcher_body(
    title: str,
    citekey: str,
    citation_key: str,
    citation_key_source: str,
    pandoc_cite: str,
    source_ref: str,
    zotero_item_key: str,
    zotero_attachment_key: str,
    zotero_select_uri: str,
    zotero_pdf_uri: str,
    doi: str,
) -> str:
    zotero_item_link = markdown_link("Open Zotero Item", zotero_select_uri)
    zotero_pdf_link = markdown_link("Open Zotero PDF", zotero_pdf_uri)
    return f"""# {title}

## Quick View

核验后写 150–250 词：puzzle 一句；核心发现；框架/机制名；主效应系数 + 方向 + 显著性；关键异质性或机制；对活跃项目的 1 句 relevance。不要复述摘要。

原文：[[path-style-wikilink-to-fulltext]]。

---

## §0. Reading Scope and Paper Type

- Paper type: empirical / theoretical / review / meta-analysis
- Reading stance: core / supporting / background
- Keep:
- Do not copy:
- Must add:

---

## §1. Research Question, Purpose, and Gap

- One-sentence RQ:
- Constructs in the RQ:
- Purpose type: explanatory / exploratory / descriptive
- Core puzzle: 真实现象或未解经验模式；若是 manufactured gap，在此点破
- Why care — practical:
- Why care — theoretical:
- Intuitive answer, and why it is not enough:
- Gap type: mechanism / boundary / comparison / measurement / identification
- Gap:
- Literature move: 如何推进这场对话，而不是再加一个 setting

---

## §2. Prior Research on This Question

- Conversation:
- Prior consensus:
- Unresolved: mechanism / boundary / comparison / measurement / identification
- **Strand 1 — [标签]**: 前人做了什么 → 缺了什么 → 本文如何填补
- **Strand 2 — [标签]**:

---

## §3. Theory, Constructs, and Claims

### 3a. Theoretical framework

理论框架名称 + 核心逻辑 + 为什么这个框架适合这个 RQ。不要发明论文未使用的理论标签。

Work test: 机制是否做了真实的因果/行为工作，还是主要靠理论标签和引用？

### 3b. Core constructs

- **Construct**:
  - Definition:
  - Origin: inherited / sharpened / newly introduced
  - Operationalization:
  - Role: IV / DV / mediator / moderator
- Relationship form: linear / moderated / mediated / sequential / recursive / comparative

### 3c. Hypothesis Logic

**H_main (标签): 一句话预测**

- 理论前提:
- 因果机制: A → B → C → Y（每步标注逻辑类型：signal / incentive / constraint / belief update / resource allocation / attention）
- 实证预测:
- 竞争性解释排除:
- 边界:

### 3d. Key claims (summary table)

| H | 预测 | 系数 | 显著性 | 逻辑链关键词 |
|---|------|------|--------|------------|
| H_main |  |  |  |  |

---

## §4. Research Design, Data, Measures, and Ethics

- Why this setting:
- Design:
- Sample:
- Comparison structure:
- DVs:
- Key IVs:
- Controls:
- Fixed effects / SE clustering:
- Identifying assumptions:
- Slippage (ideal test vs actual design):
- Key identification features:

Endogeneity（实证必填；概念文写 N/A（非实证））

- Threat: simultaneity / omitted variable / measurement error / selection / reverse causality
- Addressed?: yes / partial / no / not claimed
- Strategy: OLS+controls / FE / matching / DiD / RDD / IV / control function / other
- Residual threat:

若 IV：

- Endogenous regressor:
- Instrument(s): 名称、构造、variation 层级
- Why this instrument:
- Relevance（一阶段 F / KP 等）:
- Exclusion（作者论证 + 笔记是否买账）:
- Diagnostics:

若 control function：

- Endogenous regressor:
- CF source / excluded variable: 名称 + 构造（不得只写“用了 CF”）
- First stage / CF construction:
- Why this source:
- Diagnostics:

---

## §5. Findings, Validity, and Interpretation

- 主效应:
- 异质性/调节:
- 渠道/中介:
- 稳健性:
- Statistical vs substantive:
- Interpretive weight: association / conditional association / causal（不得高于 §4 Endogeneity 的 Addressed?）
- 内部效度:
- 外部效度:

---

## §6. Contribution, Critique, and Reuse

- Theoretical contribution:
- Empirical / methodological contribution:
- Earned vs claimed:
- Absence test: 若没有这篇，文献会少什么
- Boundary:
- My critique for <project>:
- Key citations to retain:

---

## §7. Codex-Required Sections

N/A（无需 Stata/复制层）

---

## §8. Project Handoff and Evidence Check

- Motivation / gap use:
- Theory / hypothesis use:
- Variables / measures:
- Reviewer defense use:
- Related / similar / opposing papers:
- My critique:
- Should create or update concept page:
- Should create or update argument card:
- Atomic deep-evidence page needed: yes / no

---

## §9. Metadata Notes

- Citation key: {citekey}
- Resolved citation key: {citation_key}
- Citation key source: {citation_key_source}
- Pandoc cite token: {pandoc_cite}
- DOI: {doi}
- Canonical source: [[{citekey}]]
- Source PDF / Markdown: {source_ref}
- Zotero item key: {zotero_item_key}
- Zotero attachment key: {zotero_attachment_key}
- Zotero item link: {zotero_item_link}
- Zotero PDF link: {zotero_pdf_link}
- Reading status: verified-from-fulltext-markdown / verified-from-pdf / stub
- Confidence:
- Key corrections from stub:
"""


def build_writer_body(
    title: str,
    citekey: str,
    citation_key: str,
    citation_key_source: str,
    pandoc_cite: str,
    source_ref: str,
    zotero_item_key: str,
    zotero_attachment_key: str,
    zotero_select_uri: str,
    zotero_pdf_uri: str,
) -> str:
    zotero_item_link = markdown_link("Open Zotero Item", zotero_select_uri)
    zotero_pdf_link = markdown_link("Open Zotero PDF", zotero_pdf_uri)
    return f"""# {title}

## Quick View

用一个短段落先交代这篇文章在写作上最值得借鉴的是什么，它的结构逻辑是否清晰易学，以及哪一部分最值得拿来当模板。

## 1. Overall Structure and Layout

写成 2-3 段：

第一段：
各节标题是什么，顺序如何，篇幅分布是否符合该领域常见写法。

第二段：
哪些内容放在正文，哪些放在 appendix，正文的信息分配是否高效。

第三段：
整体结构最大的优点和最大的问题分别是什么。

## 2. Introduction Strategy

写成 2-3 段：

第一段：
第一段从哪个抽象层次切入，用现象还是理论问题开篇。

第二段：
作者如何识别受众、建立重要性、从现象转入 literature，再把 gap 和 paper move 明确出来。

第三段：
摘要与引言如何分工，有没有明显重复或缺口。

## 3. Literature Review and Theory Construction

写成 2-3 段：

第一段：
文献综述与理论框架是分开写还是合并写，作者如何组织已有研究。

第二段：
作者如何在推进原创论点的同时回顾文献，引用是在支持解释还是替代解释。

第三段：
文章如何从“已有研究”切入“本文逻辑”，这个过渡是否顺滑。

## 4. Methods and Results Presentation

写成 2-3 段：

第一段：
方法部分如何交代 sample、measure、design 和 estimator，信息顺序是否自然。

第二段：
结果部分如何引导读者读表，是否避免了逐项念表。

第三段：
稳健性、附加分析和 appendix 的安排是否服务于叙事，而不是打断叙事。

## 5. Discussion and Conclusion Writing

写成 2-3 段：

第一段：
discussion / conclusion 如何平衡 finding summary、limitations、literature dialogue 和 future research。

第二段：
作者如何处理局限，是防御式还是引导式。

第三段：
结论是否越过了研究设计所能支持的边界。

## 6. Language and Rhetoric

写成 1-2 段：

第一段：
句式节奏、信号词使用、段落开头方式是否稳定而清楚。

第二段：
有没有特别值得摘录的定义句、贡献句、假设桥接句或结果解释句。

## 7. What I Should Borrow

写成 1-2 段：

第一段：
这篇文章最值得直接学习的 1-2 个具体技巧是什么。

第二段：
哪些写法只能服务这篇论文自身，不适合机械迁移。

## Metadata Notes
- Citation key: {citekey}
- Resolved citation key: {citation_key}
- Citation key source: {citation_key_source}
- Pandoc cite token: {pandoc_cite}
- Source file or link: {source_ref}
- Zotero item key: {zotero_item_key}
- Zotero attachment key: {zotero_attachment_key}
- Zotero item link: {zotero_item_link}
- Zotero PDF link: {zotero_pdf_link}
- Reading date:
- Related notes:
"""


def build_body(
    title: str,
    citekey: str,
    citation_key: str,
    citation_key_source: str,
    pandoc_cite: str,
    source_ref: str,
    zotero_item_key: str,
    zotero_attachment_key: str,
    zotero_select_uri: str,
    zotero_pdf_uri: str,
    reading_mode: str,
    doi: str = "",
) -> str:
    if reading_mode == "writer":
        return build_writer_body(
            title=title,
            citekey=citekey,
            citation_key=citation_key,
            citation_key_source=citation_key_source,
            pandoc_cite=pandoc_cite,
            source_ref=source_ref,
            zotero_item_key=zotero_item_key,
            zotero_attachment_key=zotero_attachment_key,
            zotero_select_uri=zotero_select_uri,
            zotero_pdf_uri=zotero_pdf_uri,
        )

    return build_researcher_body(
        title=title,
        citekey=citekey,
        citation_key=citation_key,
        citation_key_source=citation_key_source,
        pandoc_cite=pandoc_cite,
        source_ref=source_ref,
        zotero_item_key=zotero_item_key,
        zotero_attachment_key=zotero_attachment_key,
        zotero_select_uri=zotero_select_uri,
        zotero_pdf_uri=zotero_pdf_uri,
        doi=doi,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create an Obsidian literature-note scaffold."
    )
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--authors", help="Authors separated by ';' or 'and'")
    parser.add_argument("--year", default="", help="Publication year")
    parser.add_argument("--journal", default="", help="Journal or venue")
    parser.add_argument("--doi", default="", help="DOI")
    parser.add_argument("--url", default="", help="URL")
    parser.add_argument("--pdf-path", default="", help="Local PDF path for optional Zotero attachment lookup")
    parser.add_argument(
        "--markdown-path",
        default="",
        help="Authoritative full-text Markdown path; preferred substantive reading source",
    )
    parser.add_argument("--citekey", default="", help="Citation key")
    parser.add_argument("--zotero-db", help="Path to zotero.sqlite")
    parser.add_argument("--disable-zotero-lookup", action="store_true", help="Skip Zotero lookup")
    parser.add_argument(
        "--source-type",
        default="pdf",
        choices=["markdown", "pdf", "doi", "url", "title", "abstract", "note-upgrade", "comparison"],
        help="Primary source type for this note",
    )
    parser.add_argument(
        "--reading-stage",
        default=CONFIG.get("default_reading_stage", "close-read"),
        choices=["to-read", "browsed", "close-read"],
        help="Vault evidence-card reading_stage",
    )
    parser.add_argument(
        "--reading-mode",
        default="researcher",
        choices=["researcher", "writer"],
        help="Perspective represented by the note",
    )
    parser.add_argument(
        "--paper-kind",
        default="empirical",
        choices=["theoretical", "empirical", "review", "methods", "mixed"],
        help="Paper kind for evidence-card frontmatter",
    )
    parser.add_argument(
        "--evidence-grade",
        default="medium",
        choices=["low", "medium", "high"],
        help="Evidence grade",
    )
    parser.add_argument(
        "--reuse-level",
        default="medium",
        choices=["low", "medium", "high"],
        help="Reuse level for the user's project",
    )
    parser.add_argument(
        "--confidence",
        default="medium",
        choices=["seed", "low", "medium", "high"],
        help="Note confidence",
    )
    parser.add_argument(
        "--verified",
        default="",
        help="Verification stamp, e.g. '2026-08-29 — OvisOCR2 全文 Markdown'",
    )
    parser.add_argument(
        "--status",
        default=CONFIG.get("default_status", "developing"),
        choices=["triage", "developing", "citation_ready", "stub"],
        help="Evidence-card status",
    )
    parser.add_argument("--tags", default=DEFAULT_TAGS, help="Comma-separated tags")
    parser.add_argument("--vault-root", help="Obsidian vault root")
    parser.add_argument("--notes-dir", help="Explicit notes directory")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing file")
    parser.add_argument("--dry-run", action="store_true", help="Print path and content without writing")
    args = parser.parse_args()

    authors = parse_authors(args.authors)
    generated_citekey = args.citekey or default_citekey(authors, args.year)
    zotero = resolve_zotero_links(
        doi=args.doi,
        title=args.title,
        pdf_path=args.pdf_path,
        zotero_db=args.zotero_db,
        disable_lookup=args.disable_zotero_lookup,
    )
    citation_key = zotero.get("citation_key") or generated_citekey
    citation_key_source = zotero.get("citation_key_source") or ("manual_or_generated" if args.citekey else "generated")
    pandoc_cite = f"[@{citation_key}]" if citation_key else ""
    citekey = citation_key
    aliases = default_aliases(authors, args.year, citekey)
    tags = parse_csv(args.tags)
    notes_dir = resolve_notes_dir(args.vault_root, args.notes_dir)
    filename = build_filename(args.title, authors, args.year, citekey)
    output_path = notes_dir / filename

    template = "writer-note" if args.reading_mode == "writer" else "evidence-card"
    frontmatter = build_frontmatter(
        title=args.title,
        aliases=aliases,
        authors=authors,
        year=args.year,
        journal=args.journal,
        doi=args.doi,
        url=args.url,
        citekey=citekey,
        citation_key=citation_key,
        citation_key_source=citation_key_source,
        pandoc_cite=pandoc_cite,
        zotero_item_key=zotero["item_key"],
        zotero_attachment_key=zotero["attachment_key"],
        zotero_select_uri=zotero["select_uri"],
        zotero_pdf_uri=zotero["pdf_uri"],
        reading_mode=args.reading_mode,
        source_type=args.source_type,
        reading_stage=args.reading_stage,
        status=args.status,
        tags=tags,
        paper_kind=args.paper_kind,
        evidence_grade=args.evidence_grade,
        reuse_level=args.reuse_level,
        confidence=args.confidence,
        verified=args.verified,
        template=template,
    )
    source_ref = args.markdown_path or args.pdf_path or args.url or args.doi
    content = f"{frontmatter}\n\n{build_body(args.title, citekey, citation_key, citation_key_source, pandoc_cite, source_ref, zotero['item_key'], zotero['attachment_key'], zotero['select_uri'], zotero['pdf_uri'], args.reading_mode, doi=args.doi)}"

    if args.dry_run:
        print(output_path)
        print()
        print(content)
        return 0

    notes_dir.mkdir(parents=True, exist_ok=True)
    if output_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {output_path}")

    output_path.write_text(content, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
