#!/usr/bin/env python3
"""Save a literature note into the vault and append a memory log entry."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONFIG_PATH = SKILL_DIR / "config.json"


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


CONFIG = load_config()
DEFAULT_VAULT_ROOT = Path(CONFIG.get("vault_root", r"D:\Onedrive\Obsidian Vault"))
DEFAULT_NOTES_DIR = CONFIG.get("default_notes_dir", "literature")
BACKUP_ON_OVERWRITE = bool(CONFIG.get("backup_on_overwrite", True))
NOTE_LOGGING = CONFIG.get("note_logging", {})
DEFAULT_MEMORY_LOG = SKILL_DIR / NOTE_LOGGING.get("memory_log", "memory/notes_log.md")


def extract_frontmatter(content: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = match.group(1)
    result: dict = {}

    for field in ("title", "year", "journal", "citekey", "citation_key"):
        field_match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if field_match:
            result[field] = field_match.group(1).strip().strip('"').strip("'")

    for field in ("authors", "tags"):
        block = re.search(rf'^{field}:\s*\n((?:[ \t]+-[^\n]+\n?)*)', frontmatter, re.MULTILINE)
        if block:
            items = re.findall(r'^\s+-\s+"?([^"\n]+)"?', block.group(1), re.MULTILINE)
            result[field] = [item.strip() for item in items if item.strip()]

    return result


def format_log_entry(filename: str, output_path: Path, metadata: dict) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    citekey = metadata.get("citation_key") or metadata.get("citekey") or filename.removesuffix(".md")
    title = metadata.get("title", "—")
    year = metadata.get("year", "—")
    journal = metadata.get("journal", "—")

    authors = metadata.get("authors", [])
    author_labels = []
    for author in authors[:4]:
        author_labels.append(author.split(",")[0].strip())
    authors_str = ", ".join(author_labels) if author_labels else "—"
    if len(authors) > 4:
        authors_str += " et al."

    generic_tags = {"literature-note", "paper", "tool-note", "research-methodology", "writing-guide"}
    tags = metadata.get("tags", [])
    topics = [tag for tag in tags if tag.lower() not in generic_tags]
    topics_str = ", ".join(topics) if topics else "—"

    lines = [
        "",
        f"### {citekey} · {date_str}",
        f"- **title**: {title}",
        f"- **authors**: {authors_str}",
        f"- **year**: {year} · **journal**: {journal}",
        f"- **topics**: {topics_str}",
        f"- **file**: `{filename}`",
        f"- **path**: {output_path.as_posix()}",
    ]
    return "\n".join(lines) + "\n"


def resolve_output_dir(vault_root: Path, notes_dir: str) -> Path:
    if Path(notes_dir).is_absolute():
        return Path(notes_dir)
    return vault_root / notes_dir


def save_note(filename: str, content: str, vault_root: Path, notes_dir: str, log_enabled: bool) -> Path:
    output_dir = resolve_output_dir(vault_root, notes_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    if output_path.exists() and BACKUP_ON_OVERWRITE:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = output_path.with_name(output_path.stem + f".bak.{timestamp}" + output_path.suffix)
        shutil.copy2(output_path, backup_path)
        print(f"[backup] {backup_path.as_posix()}", file=sys.stderr)

    output_path.write_text(content, encoding="utf-8")
    print(f"[saved] {output_path.as_posix()}", file=sys.stderr)

    if log_enabled:
        metadata = extract_frontmatter(content)
        DEFAULT_MEMORY_LOG.parent.mkdir(parents=True, exist_ok=True)
        with DEFAULT_MEMORY_LOG.open("a", encoding="utf-8") as handle:
            handle.write(format_log_entry(filename, output_path, metadata))
        print(f"[logged] {DEFAULT_MEMORY_LOG.as_posix()}", file=sys.stderr)

    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Save a literature note into the configured Obsidian vault.")
    parser.add_argument("filename", help="Target markdown filename")
    parser.add_argument("--vault-root", default=str(DEFAULT_VAULT_ROOT), help="Override Obsidian vault root")
    parser.add_argument("--notes-dir", default=DEFAULT_NOTES_DIR, help="Relative or absolute notes directory")
    parser.add_argument("--no-log", action="store_true", help="Skip memory log append")
    args = parser.parse_args()

    content = sys.stdin.read()
    if not content.strip():
        print("ERROR: stdin is empty", file=sys.stderr)
        return 1

    output_path = save_note(
        filename=args.filename,
        content=content,
        vault_root=Path(args.vault_root),
        notes_dir=args.notes_dir,
        log_enabled=not args.no_log and NOTE_LOGGING.get("enabled", True),
    )
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(output_path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
