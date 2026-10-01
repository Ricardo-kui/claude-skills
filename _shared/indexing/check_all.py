#!/usr/bin/env python3
"""维护期漂移门：四节原生索引、检索视图与来源绑定回归。

默认重生成后比对 Git 暂存区；--worktree 比对运行前的当前文件内容
（忽略 CRLF/LF 差异），无需把授权修改暂存。两种模式都会重写派生索引。
function-map 仅验证可达与非空；检索质量另见 _governance/exemplar-retrieval。
引用完整性门只覆盖归档来源特征行及 .sentences.md 引用，不覆盖全部内链。

门语义（先读再用）
------------------
对 write-results / write-methods / write-theory / write-introduction 依序执行：

1. 运行 ``python scripts/build_indices.py --verify``（会重写 ``corpus/_skeleton/``，
   与手工重建同一效果），断言 exit 0 且 SUMMARY 行 ``mismatch=0 anchor_miss=0``；
2. **blob 哈希门**：``git hash-object``（工作树）逐文件比对 ``git rev-parse :path``
   （Git暂存区）——全部相等即「生成物与暂存内容逐字节一致」。不用
   ``git status``：autocrlf 下 LF 工作树文件会出现内容相同却报 M 的幻影；
3. 串联 ``validate_write_methods.py`` / ``validate_write_results.py``（exit 0）。
4. **覆盖对账**（methods 登记；theory/results 登记与内容覆盖）：(a) 登记检查——corpus 内容文件必须登记在适配器
   解析清单（FAMILIES/VARIANT_FILES 等），新蒸馏文件漏登记即 FAIL；(b) 变体覆盖——
   每个变体标题必须有索引条目或 _unparsed 记录；(c) 围栏覆盖——含 [槽位] 的围栏块数
   ≤ 该文件模板条目数（E_moderation 型 H2 模板静默漏抽的自动拦截）。
5. **function-map 门**：`_shared/function-map.md`（功能→语料载体地图）的全部本仓
   指针可解析，且骨架/索引目标有表格数据行——「按句子功能取范本」的非空性由此
   被机器看守（地图即 fixtures 源）。
6. **注册表对账**（四节，含 introduction）：串联 `_governance/corpus_registry_reconcile.py`。
   上面第 1–5 项对的是「骨架索引 ↔ corpus」，本项对的是 **「注册表/治理台账 ↔ corpus」**
   （两者互补，缺一即有空档）。以 corpus 实况为事实源，检出 MISSING_IN_REGISTRY /
   GHOST_IN_REGISTRY / NAME_DRIFT / NUMBER_COLLISION / GOVERNANCE_DEAD。
7. **引用完整性**：串联 `_governance/corpus_reference_integrity.py`。前六项都对
   「结构/登记」，**没有一项校验语料文档里指向别的文件的路径引用** —— 2026-09-20
   即因此漏掉 6 处死指针（story-blueprints 一次 backfill 改名后引用侧未同步，
   含 1 处**跨技能**引用）。本项检出 MISSING / PLACEHOLDER / LINE_OOB。

判定纪律：corpus 未变时，本门 FAIL = 引擎/适配器漂移（查 git diff 即见）；
corpus 变更后默认模式 FAIL = 重建产物尚未与暂存区一致；用 --worktree
检查未暂存修改。默认门不检查是否已经 commit。

用法
----
    python _shared/indexing/check_all.py [--skip-validators]

在仓库任意位置可用（脚本自定位仓库根）。本文件是**维护期回归门**，
运行期写作路径不引用它（``_shared/README.md`` 边界判据的显式例外，
先例：``story-blueprints/tests/regression_retrieval.py``）。
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SKILLS = ["write-results", "write-methods", "write-theory", "write-introduction"]

failures: list[str] = []


def check(cond: bool, message: str) -> None:
    print(f"  [{'PASS' if cond else 'FAIL'}] {message}")
    if not cond:
        failures.append(message)


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
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
    """工作树 vs Git暂存区的逐文件 blob 哈希比对（免疫行尾幻影）。"""
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
    check(not drift, f"{skill}: {n} 个生成物与暂存内容逐字节一致{detail}")


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


def methods_registration_gate(fail) -> None:
    """Methods 设计类型文件须进入 FAMILIES，包括新建的子目录文件。

    _* 目录是派生/治理资产；micro-templates 是由其 INDEX 直接路由的
    微模板库，不属于 FAMILIES 设计类型轴；目录索引自身也不作为类型文件。
    """
    mod = _load_adapter('write-methods')
    corpus = REPO / 'write-methods' / 'corpus'
    registered = {Path(f['file']).as_posix() for f in mod.FAMILIES}
    for p in sorted(corpus.rglob('*.md')):
        rel = p.relative_to(corpus)
        if (any(part.startswith('_') for part in rel.parts)
                or rel.parts[0] == 'micro-templates' or p.name == 'INDEX.md'):
            continue
        if rel.as_posix() not in registered:
            fail(f'write-methods: corpus/{rel.as_posix()} 未登记进 FAMILIES（新文件漏登记）')
    for rel in sorted(registered):
        if not (corpus / rel).is_file():
            fail(f'write-methods: FAMILIES 登记的 corpus/{rel} 不存在（删除或改名后未同步）')


def artifact_hygiene_gate(fail) -> None:
    """四个 write skill 内只拦截明确的缓存、临时输出及备份。

    _skeleton 是运行索引；feedback/registry 是持久治理状态。
    draft/preview 等词也属于正式协议与功能名称，不据名称片段判定污染。
    """
    cache_dirs = {'__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache'}
    transient_names = {'catalog.json', 'candidates.yaml', 'writeback_plan.yaml',
                       'writeback_residuals.yaml', 'benchmark-results.json',
                       'batch-cli.json', 'retrieval-preview.json', '.DS_Store', 'Thumbs.db'}
    for skill in SKILLS:
        root = REPO / skill
        for p in sorted(root.rglob('*')):
            rel = p.relative_to(root)
            if any(part in cache_dirs for part in rel.parts[:-1]):
                continue  # 同一缓存目录只报一次。
            is_cache = p.is_dir() and p.name in cache_dirs
            is_temp = p.is_file() and (
                p.name in transient_names or p.suffix.lower() in {'.pyc', '.pyo', '.tmp', '.temp', '.bak', '.log'}
                or '.backup-' in p.name or '.backup_' in p.name or '.bak-' in p.name)
            if is_cache or is_temp:
                fail(f'{skill}: {rel.as_posix()} 是缓存/中间产物；移至仓库外工作目录或清理')


def coverage_gate(fail) -> None:
    """Methods 登记对账；theory/results 登记/变体/围栏覆盖对账。"""
    methods_registration_gate(fail)
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
    ap.add_argument('--worktree', action='store_true',
                    help='校验重生成与当前工作树一致；不要求修改已暂存到 Git')
    args = ap.parse_args(argv)

    print(f"repo = {REPO}")
    for skill in SKILLS:
        print(f"\n== {skill} ==")
        skel = REPO / skill / 'corpus/_skeleton'
        before = {p.relative_to(skel).as_posix(): hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest()
                  for p in skel.rglob('*') if p.is_file()}
        r = run([sys.executable, "scripts/build_indices.py", "--verify"],
                REPO / skill)
        check(r.returncode == 0,
              f"{skill}: build_indices --verify exit 0 (got {r.returncode})")
        kv = parse_summary(r.stdout or "")
        if skill == 'write-introduction':
            kv['mismatch'] = '0' if 'verbatim 回源校验:' in r.stdout and 'MISMATCH ' not in r.stdout else 'failed'
            kv['anchor_miss'] = '0' if '锚点局部性校验' in r.stdout and 'ANCHOR-MISS ' not in r.stdout else 'failed'
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
        if args.worktree:
            after = {p.relative_to(skel).as_posix(): hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest()
                     for p in skel.rglob('*') if p.is_file()}
            check(before == after, f'{skill}: 重生成与当前工作树一致（{len(after)} files）')
        else:
            blob_gate(skill)

    print('\n== 检索视图与来源绑定 ==')
    r = run([sys.executable, '-B', '_shared/indexing/build_catalog.py', '--check'], REPO)
    check(r.returncode == 0, 'catalog 与四节原生解析器一致')
    r = run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', '_shared/indexing/tests'], REPO)
    check(r.returncode == 0, 'ID、来源绑定与检索回归检查通过')
    if r.returncode:
        print(r.stderr[-3000:])

    print("\n== 覆盖对账 ==")

    def _cov_fail(msg: str) -> None:
        failures.append(msg)
        print(f"  [FAIL] {msg}")

    coverage_gate(_cov_fail)

    print('\n== 内部文件清洁 ==')
    artifact_hygiene_gate(_cov_fail)

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

    print("\n== 注册表对账 ==")
    r = run([sys.executable, "_governance/corpus_registry_reconcile.py"], REPO)
    check(r.returncode == 0,
          f"corpus_registry_reconcile.py exit 0 (got {r.returncode})")
    if r.returncode != 0:
        for ln in (r.stdout or "").splitlines():
            if ln.startswith("[") and not ln.startswith("[FAIL]"):
                print(f"  | {ln}")

    print("\n== 引用完整性 ==")
    r = run([sys.executable, "_governance/corpus_reference_integrity.py"], REPO)
    check(r.returncode == 0,
          f"corpus_reference_integrity.py exit 0 (got {r.returncode})")
    if r.returncode != 0:
        for ln in (r.stdout or "").splitlines():
            if ln.startswith("[") and not ln.startswith("[FAIL]"):
                print(f"  | {ln}")

    print("\n== pass-contract ==")
    r = run([sys.executable, "pass_contract_check.py"], REPO)
    check(r.returncode == 0, f"pass_contract_check.py exit 0 (got {r.returncode})")

    print("\n== 索引行对齐 ==")
    # 2026-09-28 加固（dewan 跑审计发现的工具盲区）：四节全部 Markdown 索引
    # 表的行 pipe 数须与表头一致。两档——列缺失（<表头）= FAIL（列错位，
    # 渲染与按列取值都断）；自由文本裸竖线（>表头）= WARN（历史内容问题，
    # 不阻塞，逐条列出作为治理待办）。
    index_files = sorted(
        {p for pat in ("write-*/corpus/INDEX.md", "write-*/corpus/**/INDEX.md",
                       "write-*/corpus/**/_index.md")
         for p in REPO.glob(pat) if p.is_file() and "_skeleton" not in p.parts})
    warn_rows: list[str] = []
    for f in index_files:
        rel = f.relative_to(REPO).as_posix()
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        blocks: list[list[tuple[int, str]]] = []
        cur: list[tuple[int, str]] = []
        for ln, line in enumerate(lines, 1):
            if line.lstrip().startswith("|"):
                cur.append((ln, line))
            elif cur:
                blocks.append(cur)
                cur = []
        if cur:
            blocks.append(cur)
        for blk in blocks:
            if len(blk) < 3:  # 无数据行的表不查
                continue
            header_pipes = blk[0][1].count("|")
            for ln, line in blk[2:]:  # blk[1] 是分隔行
                n = line.count("|")
                if n < header_pipes:
                    check(False, f"{rel}:{ln} 表格行列缺失（{n} pipes < 表头 "
                                 f"{header_pipes}）——列错位，需补齐或修表头")
                elif n > header_pipes:
                    warn_rows.append(f"{rel}:{ln} ({n}>{header_pipes})")
    if warn_rows:
        print(f"  [WARN] 自由文本含裸竖线 {len(warn_rows)} 行（不阻塞，治理待办）:")
        for w in warn_rows[:8]:
            print(f"    | {w}")

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
