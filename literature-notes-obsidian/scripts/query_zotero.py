#!/usr/bin/env python3
"""Query Zotero metadata for literature-note workflows."""

from __future__ import annotations

import json
import os
import re
import shutil
import sqlite3
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONFIG_PATH = SKILL_DIR / "config.json"
CACHE_DIR = SKILL_DIR / "cache"
CACHE_DB = CACHE_DIR / "zotero_cache.sqlite"
CACHE_MTIME_FILE = CACHE_DIR / "zotero_cache.mtime"


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


CONFIG = load_config()
ZOTERO_DB = Path(CONFIG.get("zotero_db", r"D:\同步文件\文献库\zotero.sqlite"))
ZOTERO_STORAGE = Path(CONFIG.get("zotero_storage", r"D:\同步文件\文献库\storage"))


def source_mtime() -> float:
    mtime = ZOTERO_DB.stat().st_mtime
    wal = Path(f"{ZOTERO_DB}-wal")
    if wal.exists():
        mtime = max(mtime, wal.stat().st_mtime)
    return mtime


def read_cached_mtime() -> float:
    try:
        return float(CACHE_MTIME_FILE.read_text(encoding="utf-8").strip())
    except Exception:
        return 0.0


def write_cached_mtime(mtime: float) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_MTIME_FILE.write_text(str(mtime), encoding="utf-8")


def get_db_path() -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    current_mtime = source_mtime()
    cached_mtime = read_cached_mtime()

    if CACHE_DB.exists() and current_mtime == cached_mtime:
        print("[zotero] using cached sqlite copy", file=sys.stderr)
        return CACHE_DB

    print("[zotero] refreshing sqlite cache", file=sys.stderr)
    tmp = CACHE_DB.with_suffix(".tmp")
    shutil.copy2(ZOTERO_DB, tmp)

    for ext in ("-wal", "-shm"):
        src = Path(f"{ZOTERO_DB}{ext}")
        dst = Path(f"{tmp}{ext}")
        if src.exists():
            shutil.copy2(src, dst)

    os.replace(tmp, CACHE_DB)
    for ext in ("-wal", "-shm"):
        tmp_sidecar = Path(f"{tmp}{ext}")
        cache_sidecar = Path(f"{CACHE_DB}{ext}")
        if tmp_sidecar.exists():
            os.replace(tmp_sidecar, cache_sidecar)
        elif cache_sidecar.exists():
            cache_sidecar.unlink()

    write_cached_mtime(current_mtime)
    return CACHE_DB


def resolve_attachment_path(raw_path: str, attachment_key: str) -> str:
    if not raw_path:
        return ""
    if raw_path.startswith("storage:"):
        filename = raw_path[len("storage:") :]
        return str((ZOTERO_STORAGE / attachment_key / filename).as_posix())
    return raw_path.replace("\\", "/")


def parse_citekey(extra_value: str) -> str:
    if not extra_value:
        return ""
    match = re.search(r"(?im)^\s*(citation|bibtex citation)\s*key\s*:\s*(\S+)\s*$", extra_value)
    return match.group(2).strip() if match else ""


def sanitize_name(value: str) -> str:
    return re.sub(r"[^A-Za-z]", "", value or "")


def generate_citekey(authors: list[dict], year: str) -> str:
    if not authors:
        return f"Unknown{year}"
    first = sanitize_name(authors[0].get("lastName", "")) or "Unknown"
    if len(authors) == 1:
        return f"{first}{year}"
    if len(authors) == 2:
        second = sanitize_name(authors[1].get("lastName", ""))
        return f"{first}{second}{year}"
    return f"{first}EtAl{year}"


def query_by_title(keyword: str) -> dict:
    if not ZOTERO_DB.exists():
        return {"error": f"Zotero DB not found: {ZOTERO_DB}"}

    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT i.itemID, i.key AS item_key, it.typeName
            FROM items i
            JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
            JOIN itemData data_title ON i.itemID = data_title.itemID
            JOIN fields f ON data_title.fieldID = f.fieldID
            JOIN itemDataValues v ON data_title.valueID = v.valueID
            WHERE f.fieldName = 'title'
              AND v.value LIKE ?
              AND it.typeName IN (
                'journalArticle',
                'conferencePaper',
                'preprint',
                'thesis',
                'bookSection',
                'book'
              )
            ORDER BY i.itemID DESC
            LIMIT 5
            """,
            (f"%{keyword}%",),
        )
        rows = cur.fetchall()
        if not rows:
            return {"error": f"No Zotero items found matching: {keyword}"}

        item = rows[0]
        item_id = item["itemID"]
        item_key = item["item_key"]

        cur.execute(
            """
            SELECT f.fieldName, v.value
            FROM itemData d
            JOIN fields f ON d.fieldID = f.fieldID
            JOIN itemDataValues v ON d.valueID = v.valueID
            WHERE d.itemID = ?
            """,
            (item_id,),
        )
        fields = dict(cur.fetchall())

        cur.execute(
            """
            SELECT c.firstName, c.lastName, ct.creatorType
            FROM itemCreators ic
            JOIN creators c ON ic.creatorID = c.creatorID
            JOIN creatorTypes ct ON ic.creatorTypeID = ct.creatorTypeID
            WHERE ic.itemID = ?
            ORDER BY ic.orderIndex
            """,
            (item_id,),
        )
        authors = [
            {
                "firstName": row["firstName"] or "",
                "lastName": row["lastName"] or "",
                "type": row["creatorType"],
            }
            for row in cur.fetchall()
        ]

        cur.execute(
            """
            SELECT child.key AS attachment_key, att.path, att.contentType
            FROM itemAttachments att
            JOIN items child ON att.itemID = child.itemID
            WHERE att.parentItemID = ?
              AND (att.contentType = 'application/pdf' OR att.path LIKE '%.pdf')
            ORDER BY child.itemID DESC
            LIMIT 1
            """,
            (item_id,),
        )
        attachment = cur.fetchone()
        attachment_key = attachment["attachment_key"] if attachment else ""
        pdf_path = resolve_attachment_path(attachment["path"] if attachment else "", attachment_key)

        citekey = parse_citekey(fields.get("extra", ""))
        year = (fields.get("date", "") or "")[:4]
        if not citekey:
            citekey = generate_citekey(authors, year)

        return {
            "item_key": item_key,
            "attachment_key": attachment_key,
            "citekey": citekey,
            "citation_key_source": "zotero_bbt" if fields.get("extra") and parse_citekey(fields.get("extra", "")) else "generated",
            "title": fields.get("title", ""),
            "abstract": fields.get("abstractNote", ""),
            "year": year,
            "journal": fields.get("publicationTitle", ""),
            "doi": fields.get("DOI", ""),
            "volume": fields.get("volume", ""),
            "issue": fields.get("issue", ""),
            "pages": fields.get("pages", ""),
            "authors": authors,
            "pdf_path": pdf_path,
            "zotero_select_uri": f"zotero://select/library/items/{item_key}",
            "zotero_pdf_uri": f"zotero://open-pdf/library/items/{attachment_key}" if attachment_key else "",
        }
    finally:
        conn.close()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: query_zotero.py <title_keyword>", file=sys.stderr)
        return 1

    result = query_by_title(sys.argv[1])
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
