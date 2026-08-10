#!/usr/bin/env python3
"""
NotebookLM 学术文献流水线辅助脚本。

封装 notebooklm-py CLI，提供适合 Claude Code skill 调用的稳定接口：
- create: 创建 notebook 并返回 ID
- add-sources: 批量添加本地文件/URL sources
- wait: 等待 sources 处理完成
- ask-file: 从文件读取 prompt，提问并保存回答
- run: 端到端执行（create + add-sources + wait + ask + save output）

使用示例：
    python notebooklm_pipeline.py create "AI Adoption Review" --use
    python notebooklm_pipeline.py add-sources paper1.pdf paper2.md "https://example.com/article"
    python notebooklm_pipeline.py wait --timeout 300
    python notebooklm_pipeline.py ask-file prompt.md --output answer.md

端到端：
    python notebooklm_pipeline.py run \
        --title "AI Adoption Review" \
        --mode literature-review \
        --sources paper1.pdf paper2.md "https://example.com/article" \
        --prompt prompt.md \
        --output "D:\\OneDrive\\Obsidian Vault\\00 工作台\\NotebookLM 输出\\ai-adoption\\review.md"
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional


NOTEBOOKLM_BIN = "notebooklm"
# 可用环境变量 NOTEBOOKLM_OUTPUT_DIR 覆盖；默认指向本机 Obsidian Vault
DEFAULT_OUTPUT_DIR = Path(os.environ.get(
    "NOTEBOOKLM_OUTPUT_DIR",
    "D:/OneDrive/Obsidian Vault/00 工作台/NotebookLM 输出",
))


def run_cmd(args: List[str], capture: bool = True, timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    """运行 notebooklm CLI 命令，失败时打印 stderr 并退出。"""
    cmd = [NOTEBOOKLM_BIN] + args
    if not capture:
        result = subprocess.run(cmd)
        return result
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        print(f"[ERROR] command failed: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    return result


def create_notebook(title: str, use: bool = False) -> str:
    """创建 notebook，返回 notebook ID。"""
    args = ["create", title, "--json"]
    if use:
        args.append("--use")
    result = run_cmd(args)
    data = json.loads(result.stdout)
    # notebooklm create --json 输出格式需要实测；这里兼容两种可能
    notebook_id = data.get("id") or data.get("notebook_id") or data.get("notebook", {}).get("id")
    if not notebook_id:
        print("[ERROR] could not parse notebook ID from create output", file=sys.stderr)
        print(result.stdout, file=sys.stderr)
        sys.exit(1)
    return notebook_id


def set_current_notebook(notebook_id: str) -> None:
    run_cmd(["use", notebook_id], capture=False)


def add_source(content: str, source_type: Optional[str] = None, title: Optional[str] = None) -> dict:
    """添加一个 source，返回 source 元数据。"""
    args = ["source", "add", content, "--json"]
    if source_type:
        args.extend(["--type", source_type])
    if title:
        args.extend(["--title", title])
    result = run_cmd(args, timeout=120)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print("[WARN] could not parse source add output as JSON", file=sys.stderr)
        return {"raw": result.stdout}


def add_sources(paths: List[str]) -> List[dict]:
    """批量添加 sources，自动检测 URL/文件。"""
    added = []
    for p in paths:
        source_type = None
        title = None
        if p.startswith("http://") or p.startswith("https://"):
            source_type = "url"
        elif os.path.exists(p):
            source_type = "file"
            title = Path(p).stem
        else:
            print(f"[WARN] path does not exist, skipping: {p}", file=sys.stderr)
            continue
        print(f"[INFO] adding source: {p}")
        meta = add_source(p, source_type=source_type, title=title)
        added.append({"path": p, "meta": meta})
    return added


def wait_sources(timeout: int = 300, interval: int = 5) -> bool:
    """等待当前 notebook 的所有 sources 处理完成。"""
    # notebooklm source wait 需要 source_id；但我们可以轮询 source list
    deadline = time.time() + timeout
    while time.time() < deadline:
        result = run_cmd(["source", "list", "--json"])
        try:
            sources = json.loads(result.stdout)
        except json.JSONDecodeError:
            print("[WARN] could not parse source list, retrying...", file=sys.stderr)
            time.sleep(interval)
            continue

        if not sources:
            print("[INFO] no sources found, waiting...")
            time.sleep(interval)
            continue

        statuses = [s.get("status", "").lower() for s in sources]
        pending = [s for s in statuses if s not in ("ready", "failed")]
        failed = [s for s in sources if s.get("status", "").lower() == "failed"]

        if not pending:
            print(f"[INFO] all {len(sources)} sources finished processing")
            for f in failed:
                print(f"[WARN] source failed: {f.get('title', f.get('id', 'unknown'))}", file=sys.stderr)
            return len(failed) == 0

        print(f"[INFO] {len(pending)}/{len(sources)} sources still processing...")
        time.sleep(interval)

    print("[ERROR] timeout waiting for sources", file=sys.stderr)
    return False


def ask_notebook(prompt: str, timeout: int = 300) -> str:
    """向当前 notebook 提问，返回答案文本。"""
    result = run_cmd(["ask", prompt, "--json", "--yes"], timeout=timeout)
    try:
        data = json.loads(result.stdout)
        # 兼容可能的 JSON 结构
        if isinstance(data, dict):
            return data.get("answer") or data.get("response") or data.get("text") or json.dumps(data, ensure_ascii=False, indent=2)
        return result.stdout
    except json.JSONDecodeError:
        return result.stdout


def ask_file(prompt_file: str, output_file: Optional[str] = None, timeout: int = 300) -> str:
    """从文件读取 prompt，提问，可选保存到文件。"""
    prompt_path = Path(prompt_file)
    if not prompt_path.exists():
        print(f"[ERROR] prompt file not found: {prompt_file}", file=sys.stderr)
        sys.exit(1)
    prompt = prompt_path.read_text(encoding="utf-8")
    answer = ask_notebook(prompt, timeout=timeout)
    if output_file:
        Path(output_file).write_text(answer, encoding="utf-8")
        print(f"[INFO] answer saved to: {output_file}")
    return answer


def slugify(text: str) -> str:
    """生成文件路径友好的 slug。"""
    text = text.replace(" ", "-").lower()
    text = re.sub(r"[^a-z0-9\-]", "", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "notebooklm-output"


def build_frontmatter(title: str, mode: str, sources: List[str], notebook_id: str) -> str:
    """生成 Obsidian Markdown frontmatter。"""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    source_lines = "\n".join(f"  - \"{s}\"" for s in sources)
    return f"""---
title: "{title}"
date: {now}
source_notebook: "{notebook_id}"
mode: "{mode}"
sources:
{source_lines}
tags:
  - "notebooklm"
  - "{mode}"
---

"""


def cmd_create(args):
    notebook_id = create_notebook(args.title, use=args.use)
    print(notebook_id)


def cmd_use(args):
    set_current_notebook(args.notebook_id)


def cmd_add_sources(args):
    if args.notebook:
        set_current_notebook(args.notebook)
    added = add_sources(args.paths)
    print(json.dumps(added, ensure_ascii=False, indent=2))


def cmd_wait(args):
    ok = wait_sources(timeout=args.timeout, interval=args.interval)
    sys.exit(0 if ok else 1)


def cmd_ask_file(args):
    answer = ask_file(args.prompt_file, output_file=args.output, timeout=args.timeout)
    if not args.output:
        print(answer)


def cmd_run(args):
    """端到端执行：创建 notebook -> 添加 sources -> 等待 -> 提问 -> 保存。"""
    # 1. 创建 notebook
    notebook_id = create_notebook(args.title, use=True)
    print(f"[INFO] created notebook: {notebook_id}")

    # 2. 添加 sources
    if args.sources:
        add_sources(args.sources)

    # 3. 等待处理
    if not args.skip_wait:
        wait_sources(timeout=args.wait_timeout)

    # 4. 提问
    prompt = None
    if args.prompt:
        prompt = Path(args.prompt).read_text(encoding="utf-8")
    elif args.prompt_text:
        prompt = args.prompt_text
    else:
        print("[ERROR] --prompt or --prompt-text required for run mode", file=sys.stderr)
        sys.exit(1)

    answer = ask_notebook(prompt, timeout=args.ask_timeout)

    # 5. 保存结果
    output_path = None
    if args.output:
        output_path = Path(args.output)
    else:
        slug = slugify(args.title)
        mode_slug = args.mode or "analysis"
        output_path = DEFAULT_OUTPUT_DIR / slug / f"{mode_slug}_{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = build_frontmatter(args.title, args.mode or "analysis", args.sources or [], notebook_id)
    downstream = """
## 下游使用提示

本文件由 `notebooklm-pipeline` skill 自动生成，可直接作为以下 skill 的输入素材：
- `/write-introduction`：基于「文献综述与缺口识别」结果撰写 Introduction。
- `/write-theory`：基于「理论框架提取」结果构建 Theory & Hypotheses。
- `/write-methods` / `/write-results`：基于「方法-结果语料蒸馏」结果撰写 Methods/Results。
- `/distill-introduction-exemplar` / `/distill-theory-exemplar` / `/distill-methods-exemplar` / `/distill-results-exemplar`：对单篇范文做更精细的模块级蒸馏。

建议先通读全文，把关键 claim、gap、mechanism 用 Obsidian 高亮或注释标出，再调用下游 skill。
"""
    output_path.write_text(frontmatter + "\n" + answer + "\n\n" + downstream, encoding="utf-8")
    print(f"[INFO] output saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="NotebookLM academic paper pipeline helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create
    p_create = subparsers.add_parser("create", help="Create a new notebook")
    p_create.add_argument("title")
    p_create.add_argument("--use", action="store_true", help="Set as current notebook")
    p_create.set_defaults(func=cmd_create)

    # use
    p_use = subparsers.add_parser("use", help="Set current notebook")
    p_use.add_argument("notebook_id")
    p_use.set_defaults(func=cmd_use)

    # add-sources
    p_add = subparsers.add_parser("add-sources", help="Add sources to current notebook")
    p_add.add_argument("paths", nargs="+")
    p_add.add_argument("--notebook", help="Notebook ID (uses current if omitted)")
    p_add.set_defaults(func=cmd_add_sources)

    # wait
    p_wait = subparsers.add_parser("wait", help="Wait for all sources to be processed")
    p_wait.add_argument("--timeout", type=int, default=300)
    p_wait.add_argument("--interval", type=int, default=5)
    p_wait.set_defaults(func=cmd_wait)

    # ask-file
    p_ask = subparsers.add_parser("ask-file", help="Ask using prompt from file")
    p_ask.add_argument("prompt_file")
    p_ask.add_argument("--output", help="File to save answer")
    p_ask.add_argument("--timeout", type=int, default=300)
    p_ask.set_defaults(func=cmd_ask_file)

    # run
    p_run = subparsers.add_parser("run", help="End-to-end pipeline")
    p_run.add_argument("--title", required=True)
    p_run.add_argument("--mode", choices=["literature-review", "theory-extraction", "methods-results", "comprehensive"], default="literature-review")
    p_run.add_argument("--sources", nargs="+", default=[])
    p_run.add_argument("--prompt", help="Path to prompt file")
    p_run.add_argument("--prompt-text", help="Inline prompt text")
    p_run.add_argument("--output", help="Output markdown file path")
    p_run.add_argument("--skip-wait", action="store_true", help="Do not wait for source processing")
    p_run.add_argument("--wait-timeout", type=int, default=600)
    p_run.add_argument("--ask-timeout", type=int, default=600)
    p_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
