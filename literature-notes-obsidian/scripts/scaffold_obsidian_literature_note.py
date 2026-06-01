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


COMMON_NOTE_DIRS = [
    "literature",
    "literature_notes",
    "papers",
    "reading",
]

DEFAULT_VAULT_ROOT = Path(r"D:\Onedrive\Obsidian Vault")
DEFAULT_ZOTERO_DB = Path(r"C:\Users\admin\Zotero\zotero.sqlite")


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
) -> str:
    lines = ["---", f"title: {quote(title)}"]

    if aliases:
        lines.extend(["aliases:", yaml_list(aliases, indent=2)])
    else:
        lines.append("aliases: []")

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
            f"citekey: {quote(citekey)}",
            f"citation_key: {quote(citation_key)}",
            f"citation_key_source: {quote(citation_key_source)}",
            f"pandoc_cite: {quote(pandoc_cite)}",
            f"zotero_item_key: {quote(zotero_item_key)}",
            f"zotero_attachment_key: {quote(zotero_attachment_key)}",
            f"zotero_select_uri: {quote(zotero_select_uri)}",
            f"zotero_pdf_uri: {quote(zotero_pdf_uri)}",
            'note_type: "literature-note"',
            f"reading_mode: {quote(reading_mode)}",
            f"source_type: {quote(source_type)}",
            f"reading_stage: {quote(reading_stage)}",
            f"status: {quote(status)}",
            f"created: {quote(str(date.today()))}",
        ]
    )

    if tags:
        lines.extend(["tags:", yaml_list(tags, indent=2)])
    else:
        lines.append("tags: []")

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
) -> str:
    zotero_item_link = markdown_link("Open Zotero Item", zotero_select_uri)
    zotero_pdf_link = markdown_link("Open Zotero PDF", zotero_pdf_uri)
    return f"""# {title}

## Quick View

用一个短段落先交代这篇文章最重要的判断：它到底在说什么，值不值得深读，它最有价值的地方在哪里，以及证据强度大致如何。

## 1. Research Purpose and Research Gap

写成 2-4 段，而不是拆成零碎 bullet。必须明确回答：

第一段：
这篇文章研究的现象、问题或谜题是什么，为什么这件事值得关心。

第二段：
这篇文章参与的是哪场文献讨论。作者把自己放进了哪些 literatures、对话或争论里。

第三段：
已有文献没有回答什么。这里不要只写“文献很少研究”，而要写清楚究竟遗漏了什么机制、边界条件、比较关系、测量、或因果判断。

第四段：
为什么这些未回答的问题重要，以及作者如何利用已有文献把研究问题和独特贡献推出来。

## 2. Theory, Argument, and Hypothesis Logic

写成 2-4 段。

如果是实证论文：
解释核心构念、理论视角、机制链条、以及假设如何被一步一步“挣出来”。

如果是假设不明显、甚至没有正式假设的理论论文：
解释作者的概念工作、逻辑推进、论证结构和主张之间的连接。

无论哪种情况，都要说明：
- 理论逻辑最强的地方在哪里
- 哪一步有跳跃或偷换
- 作者如何从文献综述转入自己的解释

如果论文在正式假设前先整合多条理论传统，可加一个小节 `理论前提与框架整合`，说明作者如何让这些理论互补，而不是并排堆放。

如果论文按理论块组织假设，可在本节下使用分组小标题。每个假设或核心主张尽量区分：
- `HOW`：假设本身，即变量、方向、效应类型
- `WHY`：支撑该关系的机制。若机制可枚举，可用短 bullet 写出多个渠道，最后点出共同依托的上位理论

最后补一段整体理论评估：
- 多组假设是否共享一个连贯的上位逻辑，还是有“拼接感”
- 哪个假设组最有说服力，哪个最薄弱，为什么

## 3. Variables, Measures, and Empirical Strategy

如果论文是实证研究，写成 2-4 段：

第一段：
交代 setting、sample、data source，以及研究设计大致是什么。

第二段：
解释核心变量是如何被操作化的。区分理论构念和实际 measure，判断 proxy 是否贴切。

第三段：
解释文章依赖的识别或比较逻辑是什么。写清楚 variation 从哪里来，关键识别假设是什么，最主要的威胁是什么。

第四段：
概括主要结果与作者如何解释这些结果，并判断这种解释是否超出了设计所能支持的强度。

如果论文是理论或概念性论文，没有实证部分，则明确写一句：
`本文为理论/概念性文章，无正式变量测量和因果识别设计；应重点评估其概念界定、论证链条与理论贡献。`

## 4. Contribution, Limits, and My Judgment

写成 2-3 段：

第一段：
这篇文章的理论贡献、经验贡献或方法贡献到底是什么。

第二段：
这篇文章的局限、边界条件、以及最容易被攻击的地方是什么。

第三段：
我自己的总体判断：这篇文章好在哪里，如果没有它会少什么，它对我将来的 research 有什么帮助。

## 5. Writing Deconstruction

### 5.1 Introduction Craft

用一个短段落说明它的前端是怎么写的：
hook 怎么开，文献讨论怎么转，gap 句子如何落地，paper move 如何显出来。

然后写一句：
`Transferable rule for $write-social-science-introduction: ...`

### 5.2 Theory and Hypotheses Craft

用一个短段落说明它如何引入构念、铺机制、把文献支持变成 why 逻辑、以及如何把假设写得“像是被挣出来的”。

然后写一句：
`Transferable rule for $write-theory-and-hypotheses: ...`

### 5.3 Methods and Results Craft

用一个短段落说明它如何写 sample、measure、identification、results、interaction、robustness，尤其是如何避免念表和过度因果语言。

然后写一句：
`Transferable rule for $write-methods-and-results: ...`

## 6. Writing Transfer Candidate

只有在这篇文章真的写得特别好而且模式可泛化时才填写。简短写明：

- target skill
- source passage or paragraph
- why it works
- generalized rule
- confidence

## 7. Metadata Notes
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
    parser.add_argument("--pdf-path", default="", help="Local PDF path for Zotero attachment lookup")
    parser.add_argument("--citekey", default="", help="Citation key")
    parser.add_argument("--zotero-db", help="Path to zotero.sqlite")
    parser.add_argument("--disable-zotero-lookup", action="store_true", help="Skip Zotero lookup")
    parser.add_argument(
        "--source-type",
        default="pdf",
        choices=["pdf", "doi", "url", "title", "abstract", "note-upgrade", "comparison"],
        help="Primary source type for this note",
    )
    parser.add_argument(
        "--reading-stage",
        default="purposeful",
        choices=["triage", "purposeful", "constructive"],
        help="Reading depth represented by the note",
    )
    parser.add_argument(
        "--reading-mode",
        default="researcher",
        choices=["researcher", "writer"],
        help="Perspective represented by the note",
    )
    parser.add_argument(
        "--status",
        default="reading",
        choices=["to-read", "reading", "done"],
        help="Note status",
    )
    parser.add_argument("--tags", default="literature-note,paper", help="Comma-separated tags")
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
    )
    source_ref = args.pdf_path or args.url or args.doi
    content = f"{frontmatter}\n\n{build_body(args.title, citekey, citation_key, citation_key_source, pandoc_cite, source_ref, zotero['item_key'], zotero['attachment_key'], zotero['select_uri'], zotero['pdf_uri'], args.reading_mode)}"

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
