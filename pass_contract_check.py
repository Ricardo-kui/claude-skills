#!/usr/bin/env python3
"""Pass-contract 字段对齐门（round2 方案 Batch 7 的第 4 条 P0 断言）。

断言四个 review 出口（intro/theory/methods/results-review）与
``_shared/pass-contract.md`` 保持机读可核的对齐：

  C1 contract-defines-six  契约 §一 表格定义的恰好是六个规范字段（冻结集，
                           无缺失、无多出、无重名）
  C2 hard-rule-present     强制条款「缺任一字段 = 审查未完成」在契约中在位
  C3 consumer-registered   契约 §三 消费方表登记了全部四个出口（新增出口
                           须先登记再引用）
  C4 per-exit alignment    每个出口 SKILL.md：
                           - 指向 ``_shared/pass-contract.md`` 单一源；
                           - 声明「节别增量」（只许节别增量，不许另立字段）；
                           - 无本地字段定义（定义式行 `` `field`：… `` 视为
                             第二事实源；指回 pass-contract 的指针行豁免）；
                           - 无漂移拼写（kebab 化 / 英式变体）。

退出码：0 = 全部通过；1 = 任一 FAIL。维护期门：可单跑，亦由
``_shared/indexing/check_all.py`` 在维护期一并执行。

用法:
    python pass_contract_check.py            # 全部断言
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
CONTRACT = REPO / "_shared" / "pass-contract.md"

CANONICAL = ("boundary_compliance", "exemplar_fidelity", "posture",
             "defense_budget", "meta_language", "expression")
EXITS = ("intro-review", "theory-review", "methods-review", "results-review")
DRIFT_SPELLINGS = ("defence_budget", "exemplar-fidelity", "defense-budget",
                   "meta-language", "boundary-compliance")

SECTION_FIELDS = re.compile(r"^## 一、六个字段\s*$", re.M)
SECTION_CONSUMERS = re.compile(r"^## 三、消费方（四个 review 出口）\s*$", re.M)
SECTION_NEXT = re.compile(r"^## ", re.M)
TABLE_FIELD_ROW = re.compile(r"^\|\s*`([a-z_]+)`\s*\|", re.M)
DEFINITION_LINE = re.compile(r"^[-*•]?\s*`([a-z_]+)`\s*[:：](.*)$")


def _slice(text: str, start: re.Pattern) -> str:
    m = start.search(text)
    if m is None:
        return ""
    nxt = SECTION_NEXT.search(text, m.end())
    return text[m.end(): nxt.start() if nxt else len(text)]


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    failures: list[str] = []
    n_pass = 0

    def check(cond: bool, detail: str) -> None:
        nonlocal n_pass
        if cond:
            n_pass += 1
            print(f"  [PASS] {detail}")
        else:
            failures.append(detail)
            print(f"  [FAIL] {detail}")

    print("== pass-contract ==")

    if not CONTRACT.is_file():
        check(False, f"契约文件存在: {CONTRACT}")
        print(f"PASS {n_pass} / FAIL {len(failures)}")
        return 1
    text = CONTRACT.read_text(encoding="utf-8")

    # C1 六字段冻结集
    fields = TABLE_FIELD_ROW.findall(_slice(text, SECTION_FIELDS))
    missing = [f for f in CANONICAL if f not in fields]
    extra = [f for f in fields if f not in CANONICAL]
    dup = len(fields) != len(set(fields))
    check(not missing and not extra and not dup and len(fields) == len(CANONICAL),
          f"契约 §一 定义恰好六个规范字段（got {len(fields)}; 缺 {missing or '无'}; "
          f"多 {extra or '无'}; 重名 {'有' if dup else '无'}）")

    # C2 强制条款在位
    check(bool(re.search(r"缺任一字段\s*=\s*审查未完成", text)),
          "硬规则「缺任一字段 = 审查未完成」在位")

    # C3 消费方表登记
    consumers = _slice(text, SECTION_CONSUMERS)
    unregistered = [e for e in EXITS if f"`{e}`" not in consumers]
    check(not unregistered,
          f"契约 §三 登记全部四个出口（未登记: {unregistered or '无'}）")

    # C4 每出口对齐
    for exit_name in EXITS:
        skill_md = REPO / exit_name / "SKILL.md"
        if not skill_md.is_file():
            check(False, f"{exit_name}: SKILL.md 存在")
            continue
        t = skill_md.read_text(encoding="utf-8")
        problems: list[str] = []
        if "_shared/pass-contract.md" not in t:
            problems.append("缺 _shared/pass-contract.md 指针")
        if "节别增量" not in t:
            problems.append("缺「节别增量」声明")
        local_defs = sorted({
            m.group(1) for line in t.splitlines()
            if (m := DEFINITION_LINE.match(line.strip()))
            and m.group(1) in CANONICAL
            and "pass-contract" not in m.group(2)
        })
        if local_defs:
            problems.append(f"本地定义规范字段: {local_defs}（应只留指针）")
        drift = [tok for tok in DRIFT_SPELLINGS if f"`{tok}`" in t]
        if drift:
            problems.append(f"漂移拼写: {drift}")
        check(not problems,
              f"{exit_name}: 指针 + 节别增量 + 免本地定义 + 免漂移拼写"
              + ("" if not problems else f" —— {'; '.join(problems)}"))

    print(f"PASS {n_pass} / FAIL {len(failures)}")
    if failures:
        print("PASS-CONTRACT GATE FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("ALL PASS-CONTRACT CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
