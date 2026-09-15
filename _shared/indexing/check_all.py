#!/usr/bin/env python3
"""维护期漂移门：三个 write-* 骨架索引的「重生成 == 已提交内容」回归检查。

门语义（先读再用）
------------------
对 write-results / write-methods / write-theory 依序执行：

1. 运行 ``python scripts/build_indices.py --verify``（会重写 ``corpus/_skeleton/``，
   与手工重建同一效果），断言 exit 0 且 SUMMARY 行 ``mismatch=0 anchor_miss=0``；
2. **blob 哈希门**：``git hash-object``（工作树）逐文件比对 ``git rev-parse :path``
   （已提交索引）——全部相等即「生成物与提交内容逐字节一致」。不用
   ``git status``：autocrlf 下 LF 工作树文件会出现内容相同却报 M 的幻影；
3. 串联 ``validate_write_methods.py`` / ``validate_write_results.py``（exit 0）。

判定纪律：corpus 未变时，本门 FAIL = 引擎/适配器漂移（查 git diff 即见）；
corpus 变更后 FAIL = 重建产物尚未随 corpus 一起提交，是纪律提示而非误报。

用法
----
    python _shared/indexing/check_all.py [--skip-validators]

在仓库任意位置可用（脚本自定位仓库根）。本文件是**维护期回归门**，
运行期写作路径不引用它（``_shared/README.md`` 边界判据的显式例外，
先例：``story-blueprints/tests/regression_retrieval.py``）。
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SKILLS = ["write-results", "write-methods", "write-theory"]

failures: list[str] = []


def check(cond: bool, message: str) -> None:
    print(f"  [{'PASS]' if cond else '[FAIL]'} {message}")
    if not cond:
        failures.append(message)


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=env)


def parse_summary(stdout: str) -> dict[str, str]:
    for line in reversed(stdout.splitlines()):
        if line.startswith("SUMMARY "):
            kv: dict[str, str] = {}
            for tok in line.split()[1:]:
                if "=" in tok:
                    k, v = tok.split("=", 1)
                    kv[k] = v
            return kv
    return {}


def blob_gate(skill: str) -> None:
    """工作树 vs 已提交索引的逐文件 blob 哈希比对（免疫行尾幻影）。"""
    skel = REPO / skill / "corpus" / "_skeleton"
    drift: list[str] = []
    n = 0
    for p in sorted(skel.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(REPO).as_posix()
        wt = run(["git", "hash-object", str(p)], REPO).stdout.strip()
        idx = run(["git", "rev-parse", f":{rel}"], REPO)
        if idx.returncode != 0:
            drift.append(f"UNTRACKED {rel}")
            continue
        n += 1
        if idx.stdout.strip() != wt:
            drift.append(f"DIFF {rel}")
    for rel in run(["git", "ls-files", f"{skill}/corpus/_skeleton"], REPO).stdout.split():
        if not (REPO / rel).exists():
            drift.append(f"MISSING {rel}")
    detail = "" if not drift else f"；漂移 {len(drift)} 处: {drift[:5]}"
    check(not drift, f"{skill}: {n} 个生成物与提交内容逐字节一致{detail}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-validators", action="store_true",
                    help="跳过 validate_write_methods / validate_write_results 串联")
    args = ap.parse_args(argv)

    print(f"repo = {REPO}")
    for skill in SKILLS:
        print(f"\n== {skill} ==")
        r = run([sys.executable, "scripts/build_indices.py", "--verify"],
                REPO / skill)
        check(r.returncode == 0,
              f"{skill}: build_indices --verify exit 0 (got {r.returncode})")
        kv = parse_summary(r.stdout or "")
        check(kv.get("mismatch") == "0",
              f"{skill}: verbatim 回源 mismatch=0 (got {kv.get('mismatch', '无 SUMMARY 行')})")
        check(kv.get("anchor_miss") == "0",
              f"{skill}: anchor_miss=0 (got {kv.get('anchor_miss', '无 SUMMARY 行')})")
        if r.returncode != 0 or kv.get("mismatch") not in (None, "0"):
            tail = (r.stdout or "")[-1500:]
            print("  --- 诊断输出（末 1500 字符）---")
            for ln in tail.splitlines():
                print(f"  | {ln}")
            err = (r.stderr or "")[-800:]
            if err.strip():
                print(f"  stderr: {err}")
        blob_gate(skill)

    if not args.skip_validators:
        print("\n== validators ==")
        r = run([sys.executable, "scripts/validate_write_methods.py"],
                REPO / "write-methods")
        check(r.returncode == 0, f"validate_write_methods.py exit 0 (got {r.returncode})")
        r = run([sys.executable, "scripts/validate_write_results.py"],
                REPO / "write-results")
        check(r.returncode == 0, f"validate_write_results.py exit 0 (got {r.returncode})")

    print()
    if failures:
        print(f"INDEX DRIFT GATE FAILED ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("ALL INDEX DRIFT CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
