#!/usr/bin/env python3
"""Skeleton status column vs registry authority audit — periodic, deterministic.

背景（2026-09-28，dewan2020 跑实证）：write-theory 骨架的 status 列曾因
build_indices.load_status_registry 的行扫描缺陷被跨条目错配——EMERGING 单源
变体在检索层被通胀为 VERIFIED，而台账对账 CLEAN。教训：**台账对账 CLEAN ≠
检索层正确**。本脚本把"骨架呈现的状态 == registry 权威值"变成可定期执行的
机器对账，不嵌入 check_all（蒸馏链路已重，本审计独立跑、零 LLM、只读）。

对账规则（逐行，权威域两分——2026-09-28 首跑修正）：
- 骨架行 id 去点号取 base（pattern key），查 registry 权威映射；
- base ∈ 映射 → 硬对账：骨架 status 必须等于权威值；未标注=骨架过期（FAIL）；
- base ∈ 映射且骨架声称值 ≠ 权威值 → FAIL（通胀/降级都算失真）；
- 骨架有值但 base ∉ 映射 → **unmapped（INFO 不阻塞）**：这些是旧 hash 锚定块
  （无 pattern_id），骨架 status 来自块内联声明回退渠道
  （build_indices.py:403-406 设计内行为），与骨架同源同次生成，不经 registry；
- 双方都无档 → unmapped（历史遗留属正常）。

适用范围：write-theory/corpus/_skeleton/*.md——四节中唯一带 status 列的骨架
（intro/methods/results 骨架无 status 列，不受此类失真影响）。

用法：
  python _shared/indexing/skeleton_status_audit.py
  python _shared/indexing/skeleton_status_audit.py --skeleton-dir <dir>   # 负样本/定向
exit 0 = 全部一致；exit 1 = 有失真（附 file:line 清单）。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "write-theory" / "scripts"))
from build_indices import load_status_registry  # noqa: E402

VALID = {"ROBUST", "VERIFIED", "EMERGING"}


def audit(skeleton_dir: Path, registry: dict[str, str]) -> tuple[int, list[str], int]:
    rows = 0
    mismatches: list[str] = []
    unmapped = 0
    for f in sorted(skeleton_dir.glob("*.md")):
        lines = f.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").split("\n")
        status_col: int | None = None
        id_col: int | None = None
        for ln, line in enumerate(lines, 1):
            cells = line.split("|")
            stripped = [c.strip() for c in cells]
            if line.lstrip().startswith("|") and "status" in stripped and "id" in stripped:
                # 表头行：定位 id 与 status 列索引（split 首元素为空串）
                id_col = stripped.index("id")
                status_col = stripped.index("status")
                continue
            if status_col is None or not line.lstrip().startswith("|"):
                continue
            if set(line.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
                continue  # 分隔行
            if len(cells) <= max(status_col, id_col):
                continue
            rid = cells[id_col].strip().strip("`")
            status = cells[status_col].strip()
            if not rid:
                continue
            rows += 1
            base = rid.split(".", 1)[0]
            if status == "未标注":
                if base in registry:
                    mismatches.append(
                        f"{f.name}:{ln} `{rid}` 未标注，但 registry 权威="
                        f"{registry[base]}（骨架过期？重建 build_indices.py）")
                else:
                    unmapped += 1
                continue
            if status not in VALID:
                mismatches.append(f"{f.name}:{ln} `{rid}` 非法 status 值：{status!r}")
                continue
            if base not in registry:
                # 映射覆盖域外：旧 hash 锚定块的 status 来自块内联回退渠道
                # （build_indices.py:403-406 设计内行为），不经 registry——计数不判失真
                unmapped += 1
                continue
            if registry[base] != status:
                mismatches.append(
                    f"{f.name}:{ln} `{rid}` 骨架={status} vs registry 权威="
                    f"{registry[base]}")
    return rows, mismatches, unmapped


def main() -> int:
    ap = argparse.ArgumentParser(description="骨架 status 列 vs registry 对账（定期，确定性）")
    ap.add_argument("--skeleton-dir", default=None,
                    help="默认 write-theory/corpus/_skeleton（唯一带 status 列的骨架）")
    args = ap.parse_args()
    skeleton_dir = Path(args.skeleton_dir) if args.skeleton_dir else \
        REPO / "write-theory" / "corpus" / "_skeleton"
    registry = load_status_registry()
    if not registry:
        print("[audit] registry 权威映射为空——解析失败或文件缺失")
        return 1
    rows, mismatches, unmapped = audit(skeleton_dir, registry)
    print(f"[audit] 骨架目录: {skeleton_dir}")
    print(f"[audit] 权威映射 keys={len(registry)}（patterns + source_papers.fragments，rank 取高）")
    print(f"[audit] 扫描条目行 {rows}，unmapped（双方无档，正常遗留）{unmapped}")
    if mismatches:
        print(f"[audit] FAIL — status 失真 {len(mismatches)} 行：")
        for m in mismatches:
            print(f"  - {m}")
        print("[audit] 修复路径：python write-theory/scripts/build_indices.py（重建派生视图）；"
              "若重建后仍失真，则 registry 或解析器有新缺陷，先查权威值再动检索层")
        return 1
    print("[audit] PASS — 骨架 status 列与 registry 权威逐行一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
