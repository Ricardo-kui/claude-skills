#!/usr/bin/env python3
"""Extract markdown text from PDFs using the local literature-note routing rules."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONFIG_PATH = SKILL_DIR / "config.json"


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


CONFIG = load_config()
PDF_CONFIG = CONFIG.get("pdf_extraction", {})
MIN_CONTENT_LENGTH = int(PDF_CONFIG.get("min_content_length", 200))


def has_non_ascii(path: Path) -> bool:
    try:
        str(path).encode("ascii")
        return False
    except UnicodeEncodeError:
        return True


def has_substance(text: str) -> bool:
    return len((text or "").strip()) >= MIN_CONTENT_LENGTH


def run_command(args: list[str]) -> tuple[int, str, str]:
    env = dict(os.environ)
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    completed = subprocess.run(
        args,
        capture_output=True,
        check=False,
        env=env,
    )
    stdout = (completed.stdout or b"").decode("utf-8", errors="replace")
    stderr = (completed.stderr or b"").decode("utf-8", errors="replace")
    return completed.returncode, stdout, stderr


def read_with_odl(pdf_path: Path, hybrid: bool = False) -> str | None:
    command = ["opendataloader-pdf", "-q"]
    if hybrid:
        command.extend(["--hybrid", "docling-fast", "--hybrid-mode", "full", "--hybrid-fallback"])
    else:
        command.extend(["--hybrid", "off"])
    command.extend(["-f", "markdown", "--to-stdout", str(pdf_path)])

    code, stdout, stderr = run_command(command)
    if code == 0 and has_substance(stdout):
        print(f"[read_pdf] {'hybrid ODL' if hybrid else 'ODL'} succeeded", file=sys.stderr)
        return stdout

    if stderr.strip():
        print(stderr.strip(), file=sys.stderr)
    print(
        f"[read_pdf] {'hybrid ODL' if hybrid else 'ODL'} produced insufficient output",
        file=sys.stderr,
    )
    return None


def read_with_markitdown(pdf_path: Path) -> str | None:
    code, stdout, stderr = run_command(["markitdown", str(pdf_path)])
    if code == 0 and has_substance(stdout):
        print("[read_pdf] markitdown succeeded", file=sys.stderr)
        return stdout

    if stderr.strip():
        print(stderr.strip(), file=sys.stderr)
    print("[read_pdf] markitdown produced insufficient output", file=sys.stderr)
    return None


def read_pdf(pdf_path: Path, force_markitdown: bool, force_hybrid: bool) -> str:
    if not pdf_path.exists():
        raise SystemExit(f"ERROR: File not found: {pdf_path}")

    if force_markitdown:
        text = read_with_markitdown(pdf_path)
        if text is None:
            raise SystemExit("ERROR: markitdown failed to extract substantive text")
        return text

    if force_hybrid:
        text = read_with_odl(pdf_path, hybrid=True)
        if text is None:
            raise SystemExit(
                "ERROR: hybrid ODL failed; if the hybrid backend is not running, start opendataloader-pdf-hybrid on 127.0.0.1:5002"
            )
        return text

    text = read_with_odl(pdf_path, hybrid=False)
    if text is not None:
        return text

    if has_non_ascii(pdf_path) and PDF_CONFIG.get("respect_non_ascii_windows_fallback", True):
        markitdown_text = read_with_markitdown(pdf_path)
        if markitdown_text is not None:
            return markitdown_text

        temp_dir = Path(tempfile.mkdtemp(prefix="literature-note-ascii-"))
        ascii_copy = temp_dir / "paper.pdf"
        try:
            shutil.copy2(pdf_path, ascii_copy)
            text = read_with_odl(ascii_copy, hybrid=True)
            if text is not None:
                return text
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
    else:
        text = read_with_odl(pdf_path, hybrid=True)
        if text is not None:
            return text

        markitdown_text = read_with_markitdown(pdf_path)
        if markitdown_text is not None:
            return markitdown_text

    raise SystemExit(
        "ERROR: no extractor returned substantive text. Try starting opendataloader-pdf-hybrid or rerun with --force-markitdown."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract PDF text to markdown using local CLI tools.")
    parser.add_argument("pdf_path", help="Local PDF path")
    parser.add_argument("--force-markitdown", action="store_true", help="Skip ODL and use markitdown only")
    parser.add_argument("--force-hybrid", action="store_true", help="Skip standard ODL and use hybrid ODL only")
    args = parser.parse_args()

    text = read_pdf(
        pdf_path=Path(args.pdf_path),
        force_markitdown=args.force_markitdown,
        force_hybrid=args.force_hybrid,
    )
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
