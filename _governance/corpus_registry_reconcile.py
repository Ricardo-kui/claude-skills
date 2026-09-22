#!/usr/bin/env python3
"""write-* 语料对账门：以 corpus/ 实况为准，对账四节资产与注册表。

定位
----
维护期对账门（与 ``_shared/indexing/check_all.py`` 同类：运行期写作路径不引用）。
check_all.py 覆盖的是「骨架索引 ↔ corpus」，且 SKILLS 列表只有 write-results /
write-methods / write-theory；本脚本补的是它没有的那个面：
**「注册表/治理台账 ↔ corpus」**，并把 write-introduction 纳入。

对账口径
--------
以 corpus/ 目录的实际文件为唯一事实源（`discover_assets` 直接 rglob 扫盘），
反向检查登记侧的三类偏差：

- MISSING_IN_REGISTRY  corpus 有、注册表无  → 新蒸馏漏登记
- GHOST_IN_REGISTRY   注册表有、corpus 无  → 重命名收尾未清旧键
- NAME_DRIFT          文件 stem 与 canonical_id 不一致 → 检索键错位的温床

另做两项结构检查（intro）：

- NUMBER_COLLISION    同模块内数字前缀撞车 → 按 id 取件会静默取错
- GOVERNANCE_DEAD     治理台账加载失败 → 整条治理链路停摆（含路由外键与快照校验）

退出码
------
0 = 无 FAIL；1 = 有 FAIL；2 = 环境错误（缺依赖 / 路径不可达）。

用法
----
    python _governance/corpus_registry_reconcile.py [--skill <name>]... [--json]

依赖
----
pyyaml。若当前解释器缺 pyyaml，请用受管 venv 解释器运行。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GOV_INTRO_SCRIPTS = REPO / "_governance" / "write-introduction" / "scripts"

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - 环境问题，附明确指引
    print(
        "环境错误：缺少 pyyaml。请用受管 venv 运行，例如\n"
        r"  C:\Users\admin\.workbuddy\binaries\python\envs\default\Scripts\python.exe",
        file=sys.stderr,
    )
    raise SystemExit(2)


def _load_intro_catalog():
    """导入 intro 资产目录模块（有 __main__ 守卫，导入安全）。"""
    import importlib.util

    p = GOV_INTRO_SCRIPTS / "introduction_asset_catalog.py"
    name = "gov_intro_catalog"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


class Result:
    def __init__(self, skill: str) -> None:
        self.skill = skill
        self.rows: list[dict] = []

    def add(self, kind: str, message: str, detail: object = None) -> None:
        self.rows.append({"skill": self.skill, "kind": kind, "message": message, "detail": detail})

    @property
    def fails(self) -> list[dict]:
        return self.rows


def reconcile_intro(res: Result) -> None:
    """write-introduction：实况发现 + 注册表对账 + 治理台账健康。"""
    skill_root = REPO / "write-introduction"
    corpus = skill_root / "corpus"
    registry_path = corpus / "_evidence_registry.yaml"
    if not registry_path.exists():
        res.add("ERROR", f"注册表缺失: {registry_path}")
        return

    cat = _load_intro_catalog()
    parents, variants, _ = cat.discover_assets(corpus)
    res.add("INFO", f"实况发现 parent={len(parents)} variant={len(variants)}")

    # --- 治理台账健康：不得因单条记录拖垮整条链路 ---
    try:
        gp, gv, _ = cat.load_catalog(corpus, registry_path)
        res.add("INFO", f"治理台账加载成功 parent={len(gp)} variant={len(gv)}")
    except Exception as exc:  # noqa: BLE001 - 需要报出任意加载失败
        res.add(
            "GOVERNANCE_DEAD",
            f"治理台账加载失败，快照/路由外键/审计全线停摆: {type(exc).__name__}: {exc}",
            detail={"recover": "对照 load_catalog 迁移分支与 status_overrides 裁定通道的名字口径"},
        )

    # --- 登记侧对账 ---
    reg = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    ev = reg.get("evidence", {}) or {}
    for dirname, regkey in cat.KNOWN_MODULES.items():
        actual_ids = {p["canonical_id"] for p in parents if p["module"] == dirname}
        reg_ids = set(ev.get(regkey, {}) or {})
        if not actual_ids and not reg_ids:
            continue
        missing = sorted(actual_ids - reg_ids)
        ghost = sorted(reg_ids - actual_ids)
        if missing:
            res.add(
                "MISSING_IN_REGISTRY",
                f"{dirname}: {len(missing)}/{len(actual_ids)} 个资产在 evidence.{regkey} 段无登记",
                detail=missing,
            )
        if ghost:
            res.add(
                "GHOST_IN_REGISTRY",
                f"{dirname}: evidence.{regkey} 段有 {len(ghost)} 个 corpus 中不存在的键",
                detail=ghost,
            )

    # --- 命名漂移 ---
    # _index.md 是固定文件名，canonical_id 与 stem 天然不同，不构成改名残留，
    # 因此漂移检查只针对以 canonical_id 命名的卡片文件。
    drift = [
        {"file": p["source_file"], "stem": Path(p["source_file"]).stem, "canonical_id": p["canonical_id"]}
        for p in parents
        if Path(p["source_file"]).stem != p["canonical_id"]
        and Path(p["source_file"]).name != "_index.md"
    ]
    if drift:
        res.add("NAME_DRIFT", f"{len(drift)} 个文件的 stem 与 canonical_id 不一致（检索键错位风险）", detail=drift)

    # --- 编号撞车 ---
    buckets: dict[tuple[str, str], list[str]] = {}
    for p in parents:
        num = p["canonical_id"].split("-", 1)[0]
        buckets.setdefault((p["module"], num), []).append(p["canonical_id"])
    collisions = [
        {"module": m, "prefix": n, "ids": sorted(v)}
        for (m, n), v in buckets.items()
        if len(v) > 1 and n.isdigit()
    ]
    if collisions:
        res.add("NUMBER_COLLISION", f"{len(collisions)} 处数字前缀撞车（按 id 取件会静默取错）", detail=collisions)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skill", action="append", help="限定技能名（可重复）；缺省跑已接入的全部")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出")
    args = ap.parse_args(argv)

    res = Result("write-introduction")
    if not args.skill or "write-introduction" in args.skill:
        reconcile_intro(res)

    if args.json:
        print(json.dumps({"rows": res.rows}, ensure_ascii=False, indent=2))
    else:
        print(f"repo = {REPO}\n")
        for row in res.rows:
            print(f"[{row['kind']}] {row['message']}")
            if row["detail"] is not None:
                d = row["detail"]
                if isinstance(d, list):
                    for item in d:
                        print(f"    - {item if not isinstance(item, dict) else json.dumps(item, ensure_ascii=False)}")
                elif isinstance(d, dict):
                    for k, v in d.items():
                        print(f"    {k}: {v}")
        hard = [r for r in res.rows if r["kind"] not in {"INFO"}]
        print(f"\n{'RECONCILE FAILED' if hard else 'RECONCILE CLEAN'} ({len(hard)} findings)")
    return 1 if any(r["kind"] not in {"INFO"} for r in res.rows) else 0


if __name__ == "__main__":
    sys.exit(main())
