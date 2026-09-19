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
4. **覆盖对账**（theory/results）：(a) 登记检查——corpus 内容文件必须登记在适配器
   解析清单（FAMILIES/VARIANT_FILES 等），新蒸馏文件漏登记即 FAIL；(b) 变体覆盖——
   每个变体标题必须有索引条目或 _unparsed 记录；(c) 围栏覆盖——含 [槽位] 的围栏块数
   ≤ 该文件模板条目数（E_moderation 型 H2 模板静默漏抽的自动拦截）。
5. **function-map 门**：`_shared/function-map.md`（功能→语料载体地图）的全部本仓
   指针可解析，且骨架/索引目标有表格数据行——「按句子功能取范本」的非空性由此
   被机器看守（地图即 fixtures 源）。

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
import re
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


# ------------------------------------------------------- 覆盖对账门 ----

def _load_adapter(skill: str):
    """导入适配器模块（main 有 __main__ 守卫，导入安全），取解析清单与正则。"""
    import importlib.util
    p = REPO / skill / "scripts" / "build_indices.py"
    name = f"adapter_{skill}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _fence_stats(lines: list[str]) -> tuple[int, int]:
    """(围栏块总数, 含 [..] 的围栏块数)。"""
    tot = bracket = in_f = 0
    has_b = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("```"):
            if in_f:
                tot += 1
                bracket += 1 if has_b else 0
                in_f, has_b = False, False
            else:
                in_f, has_b = True, False
            continue
        if in_f and "[" in s and "]" in s:
            has_b = True
    return tot, bracket


def function_map_gate(fail) -> None:
    """`_shared/function-map.md` 的指针可解析 + 索引/骨架目标非空（地图即 fixtures 源）。

    地图是 write-* 家族「按句子功能取范本」的跨节路由（ad-hoc 查询入口）。门语义：
    (a) 图内全部本仓路径（反引号内、首段为 skill/共享目录名）必须存在；
    (b) 指向 corpus/_skeleton/ 与 corpus 索引（INDEX/_index）的目标必须有表格数据行
        ——即「该功能轴当前有非空范本库存」，功能检索非空由此被机器看守。
    """
    map_path = REPO / "_shared" / "function-map.md"
    if not map_path.is_file():
        fail("_shared/function-map.md 缺失（功能→语料载体地图）")
        return
    text = map_path.read_text(encoding="utf-8")
    roots = {"write-introduction", "write-theory", "write-methods",
             "write-results", "_shared", "distill-paper-exemplar",
             "story-blueprints"}
    targets: list[str] = []
    for m in re.finditer(r"`([a-zA-Z0-9_\-./]+\.(?:md|py|yaml))`", text):
        t = m.group(1)
        if t.split("/")[0] in roots and t not in targets:
            targets.append(t)
    if not targets:
        fail("function-map 未解析到任何本仓指针（格式漂移？）")
        return
    for t in targets:
        p = REPO / t
        if not p.exists():
            fail(f"function-map 指针不可解析: {t}")
            continue
        if "/_skeleton/" in t or t.endswith(("corpus/INDEX.md", "/_index.md")):
            rows = [ln for ln in p.read_text(encoding="utf-8").splitlines()
                    if ln.startswith("|")]
            if len(rows) < 3:
                fail(f"function-map 索引目标无表格数据行: {t}")


def coverage_gate(fail) -> None:
    """theory/results 的登记/变体/围栏三重覆盖对账。"""
    # 覆盖豁免清单：未登记但有意的文件（协议/骨架文档，非模式库语料）。
    # 是否应升级入索引属语料扩展决策——改动此处须附理由与日期。
    coverage_allowlist = {
        "subprotocols/paragraph_layout.md": "段内布局协议（自declared 骨架文件），Phase 3.2 直接引用",
        "subprotocols/arrangement_patterns.md": "段间组织模式库（含 pattern_id）——Phase 3.2 直接消费；是否并入骨架索引待语料扩展裁决（2026-09-15）",
        "subprotocols/reasoning_soundness_protocol.md": "Soundness 协议（warrant 五测试等），审计确认的独有协议文档",
        "subprotocols/character_ordering.md": "角色排序协议文档",
        "subprotocols/process_transition_operators.md": "过程转换算子协议文档",
        "subprotocols/B2_dual_track.md": "B2 双轨子协议文档（E 家族子协议索引引用）",
        "subprotocols/E1_categorical_moderation.md": "E1 分组调节子协议文档（E_moderation 子协议索引引用）",
        "subprotocols/board_governance_boundary_condition.md": "董事会治理边界条件子协议文档",
        "subprotocols/institutional_shock_lens.md": "制度冲击透镜子协议文档",
        "subprotocols/intra_tmt_persuasion.md": "TMT 内部说服子协议文档",
    }
    # ---- write-theory ----
    mod = _load_adapter("write-theory")
    tcorpus = REPO / "write-theory" / "corpus"
    reg = {rel for rel, _ in mod.VARIANT_FILES.values()}
    reg |= set(mod.SUBPROTOCOL_FILES) | set(mod.SENTENCE_FILES)
    for axis in ("variants", "subprotocols", "sentences"):
        for p in sorted((tcorpus / axis).glob("*.md")):
            rel = f"{axis}/{p.name}"
            if rel in reg or rel in coverage_allowlist:
                continue
            fail(f"write-theory: corpus/{rel} 未登记进解析清单（新文件漏登记；有意豁免请加入 coverage_allowlist 并附理由）")
    # 骨架行按归属文件分组：anchor = corpus/<rel>#<vid>
    rows: dict[str, list[tuple[str, str]]] = {}
    skel = tcorpus / "_skeleton"
    for skf in sorted(skel.glob("*.md")):
        if skf.name.startswith("_"):
            continue
        for ln in skf.read_text(encoding="utf-8").splitlines():
            if not ln.startswith("| `"):
                continue
            cells = [c.strip() for c in ln.strip("|").split("|")]
            # 7 列: id | func | citekey | status | kind | text | anchor
            anchor = cells[6].strip("`")
            pref, _, vid = anchor.partition("#")
            rows.setdefault(pref, []).append((cells[4], vid))
    unparsed = (skel / "_unparsed.md").read_text(encoding="utf-8")
    for rel in sorted(reg):
        lines = (tcorpus / rel).read_text(encoding="utf-8").splitlines()
        _, br_f = _fence_stats(lines)
        captured = rows.get(f"corpus/{rel}", [])
        tmpl = sum(1 for kind, _ in captured if kind == "模板")
        if br_f > tmpl:
            fail(f"write-theory {rel}: 含[槽位]围栏 {br_f} > 模板条目 {tmpl}（疑静默漏抽）")
        for ln in lines:
            m = mod.VARIANT_HDR_RE.match(ln.strip())
            if not m:
                continue
            # 变体覆盖检查仅适用于 variants/ 与 sentences/ 轴：两轴的条目锚点 vid
            # = 标题 token（或 变体-X/句式-X 形态）；subprotocols 的锚点 vid 是
            # pattern_id（解析器内部绑定），由登记检查 + 围栏覆盖保护。
            if not (rel.startswith("variants/") or rel.startswith("sentences/")):
                continue
            vid = m.group(1)
            # 命名节的块 vid 形态可能是 变体-X / 句式-X / _branch4_vid(title)
            title = ln.strip().lstrip("#").strip()
            cands = {vid, f"变体-{vid}", f"句式-{vid}", mod._branch4_vid(title)}
            bound = (cands & {v for _, v in captured}) or any(c in unparsed for c in cands)
            if not bound:
                fail(f"write-theory {rel}: 变体 {vid} 无索引条目且无 _unparsed 记录")

    # ---- write-results ----
    mod = _load_adapter("write-results")
    rcorpus = REPO / "write-results" / "corpus"
    reg = {f["file"] for f in mod.FAMILIES}
    for p in sorted(rcorpus.glob("*.md")):
        if p.name != "INDEX.md" and not p.name.startswith("_") and p.name not in reg:
            fail(f"write-results: corpus/{p.name} 未登记进 FAMILIES（新文件漏登记）")
    rows = {}
    skel = rcorpus / "_skeleton"
    for skf in sorted(skel.glob("*.md")):
        if skf.name.startswith("_"):
            continue
        for ln in skf.read_text(encoding="utf-8").splitlines():
            if not ln.startswith("| `"):
                continue
            cells = [c.strip() for c in ln.strip("|").split("|")]
            # 6 列: id | 槽位 | citekey | text | anchor | 状态
            anchor = cells[4].strip("`")
            pref, _, vid = anchor.partition("#")
            rows.setdefault(pref, []).append((cells[5], vid))
    # 已知「登记但零内容」的占位变体（蒸馏欠账，补内容后可移除）：
    unbound_allowlist = {
        ("SEM-moderated-mediation.md", "变体-7"): "变体 7 仅登记来源/槽位，无骨架与原文锚定（蒸馏欠账，2026-09-15）",
        ("定性过程研究.md", "变体-6"): "Power/Proof Quotes 引语选择决策表节——无句级底本，results 索引不含决策表内容（是否入索引属语料扩展决策，2026-09-15）",
    }
    unparsed = (skel / "_unparsed.md").read_text(encoding="utf-8")
    for rel in sorted(reg):
        lines = (rcorpus / rel).read_text(encoding="utf-8").splitlines()
        tot_f, _ = _fence_stats(lines)
        captured = rows.get(f"corpus/{rel}", [])
        tmpl = sum(1 for kind, _ in captured if kind == "模板")
        if tot_f > tmpl:
            fail(f"write-results {rel}: 围栏 {tot_f} > 模板条目 {tmpl}（疑静默漏抽）")
        for ln in lines:
            m = mod.VARIANT_HDR_RE.match(ln.strip())
            if not m:
                continue
            title = ln.strip()
            if "[来源论文]" in title and "YYYY-MM-DD" in title:
                continue  # 卡内格式说明标题，非真变体
            vid = f"变体-{m.group(1)}"
            if (rel, vid) in unbound_allowlist:
                continue
            if not (any(v == vid for _, v in captured) or vid in unparsed):
                fail(f"write-results {rel}: 变体 {vid} 无索引条目且无 _unparsed 记录")


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

    print("\n== 覆盖对账 ==")

    def _cov_fail(msg: str) -> None:
        failures.append(msg)
        print(f"  [FAIL] {msg}")

    coverage_gate(_cov_fail)

    print("\n== function-map ==")

    def _fm_fail(msg: str) -> None:
        failures.append(msg)
        print(f"  [FAIL] {msg}")

    function_map_gate(_fm_fail)

    if not args.skip_validators:
        print("\n== validators ==")
        r = run([sys.executable, "scripts/validate_write_methods.py"],
                REPO / "write-methods")
        check(r.returncode == 0, f"validate_write_methods.py exit 0 (got {r.returncode})")
        r = run([sys.executable, "scripts/validate_write_results.py"],
                REPO / "write-results")
        check(r.returncode == 0, f"validate_write_results.py exit 0 (got {r.returncode})")

    print("\n== pass-contract ==")
    r = run([sys.executable, "pass_contract_check.py"], REPO)
    check(r.returncode == 0, f"pass_contract_check.py exit 0 (got {r.returncode})")

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
