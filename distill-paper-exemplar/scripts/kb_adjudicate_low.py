#!/usr/bin/env python3
"""S3 adjudication: resolve LOW citations against the knowledge-base originals.

The user ruled that the LOW list's papers are findable in the KB (four folders
holding the source papers). For each unique LOW citation (grouped by the first
PARSEABLE source line — prose 原文锚点 quotes are skipped) this tool:

  1. indexes the KB roots by filename (first-author gate + year agreement;
     KB filenames usually carry only the first author)
  2. matches the citation against that index, tie-breaking by source priority
     (论文导入 > Clippings > 07 原文 > 00 工作台)
  3. for a matched file, reads its frontmatter/metadata to recover identity
  4. resolves to (a) an EXISTING family registry key, or (b) a NEW canonical
     key (S6 adds the registry entry), or (c) kb_not_found -> 不回填

Usage:
  py kb_adjudicate_low.py            # resolve + write adjudication report
  py kb_adjudicate_low.py --apply    # also mint markers for resolved blocks
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_views as rv  # noqa: E402
from backfill_source_lines import (  # noqa: E402
    SRC_RE, parse_citation, match_citation, registry_universe,
    build_cross_universes, variant_label, ROOTS)

KB_ROOTS = [
    r"D:\OneDrive\Obsidian Vault\文献笔记库\01 导入\论文导入",
    r"D:\OneDrive\Obsidian Vault\Clippings",
    r"D:\OneDrive\Obsidian Vault\共同所有权\07 原文",
    r"D:\OneDrive\Obsidian Vault\00 工作台\项目",
]
OUT = Path.home() / ".claude" / "distill-work" / "rebuild_views" / "kb_adjudication.yaml"
USER_RULINGS = Path.home() / ".claude" / "distill-work" / "rebuild_views" / "user_rulings.yaml"
SKILLS = Path(__file__).resolve().parent.parent.parent
TOKEN_CUT = re.compile(r"[^a-z0-9]+")


def build_kb_index() -> list[dict]:
    idx = []
    for r in KB_ROOTS:
        for f in Path(r).rglob("*"):
            if f.suffix.lower() not in (".md", ".pdf", ".html"):
                continue
            name = f.stem.lower()
            idx.append({"path": f, "name": name,
                        "tokens": set(t for t in TOKEN_CUT.split(name) if len(t) >= 3),
                        "years": set(rv.YEAR_IN_TOKEN_RE.findall(name))})
    return idx


def kb_match(cit: dict, idx: list[dict]) -> list[dict]:
    """First-surname gate (+ year agreement); remaining surnames and journal
    only feed the ranking. KB filenames usually carry just the first author.
    Surnames shorter than 4 chars (du, kim, lee) must match a token EXACTLY —
    prefix tolerance would match 'donkey'/'lee...' noise."""
    hits = []
    for e in idx:
        if cit["year"] and e["years"] and cit["year"] not in e["years"]:
            continue
        if not cit["surnames"]:
            continue
        first = cit["surnames"][0]
        toks = e["tokens"]
        hit_ok = False
        for t in toks:
            if len(t) < 3:
                continue
            if first == t or (len(first) >= 4 and
                              (t.startswith(first) or first.startswith(t))):
                hit_ok = True
                break
        if not hit_ok:
            continue
        sh = 0
        for s in cit["surnames"]:
            if any(t == s or (len(s) >= 4 and
                              (t.startswith(s) or s.startswith(t)))
                   for t in toks if len(t) >= 3):
                sh += 1
        jm = 1 if cit["journal"] and cit["journal"] in toks else 0
        hits.append({"entry": e, "score": sh, "journal_ok": jm})
    hits.sort(key=lambda h: (-h["score"], -h["journal_ok"]))
    return [h["entry"] for h in hits[:3]]


def file_metadata(f: Path) -> dict:
    try:
        head = f.read_text(encoding="utf-8", errors="ignore")[:2500]
    except OSError:
        return {}
    meta = {}
    fm = re.match(r"\A---\s*\n(.*?)\n---\s*\n", head, re.S)
    if fm:
        for k, v in re.findall(r"^([\w\-]+):\s*(.+)$", fm.group(1), re.M):
            meta[k.lower()] = v.strip().strip('"').strip("'")
    h1 = re.search(r"^#\s+(.+)$", head, re.M)
    meta["_h1"] = h1.group(1)[:120] if h1 else ""
    return meta


def propose_key(cit: dict, meta: dict, fname: str) -> str:
    """Canonical key from KB metadata, registry-style: authors_year_journal.
    Surname = LAST word of each author segment (Clippings frontmatter uses
    'Given Surname' order). The proposal is then alias-checked against the
    family registry keys — a same-paper key that already exists wins, so we
    never fragment a paper across two keys."""
    citekey = meta.get("citekey") or meta.get("citation_key") or meta.get("key")
    if citekey and re.fullmatch(r"[A-Za-z][\w\-]{3,60}", str(citekey)):
        return str(citekey)
    authors = []
    au = meta.get("authors") or meta.get("author") or ""
    for a in re.split(r";| and | & |, (?=[A-Z])", au):
        words = re.findall(r"[A-Za-z][\w\-']*", a.strip())
        if words and words[-1].lower() not in ("et", "al"):
            authors.append(words[-1].lower())
    if not authors:
        toks = [t for t in TOKEN_CUT.split(fname.lower()) if len(t) >= 4]
        authors = [t for t in toks if not t.isdigit()][:2]
    # guard: frontmatter authors contradicting the citation's first surname
    # (notes files carry their own metadata) -> fall back to the filename's
    # leading token, which for source files is usually the first author
    if cit["surnames"] and authors and authors[0] != cit["surnames"][0] and \
            not any(a == cit["surnames"][0] or
                    (len(cit["surnames"][0]) >= 4 and
                     (a.startswith(cit["surnames"][0]) or
                      cit["surnames"][0].startswith(a)))
                    for a in authors):
        for tt in TOKEN_CUT.split(fname.lower()):
            if tt.startswith(cit["surnames"][0][:4]):
                authors = [cit["surnames"][0]] + authors[:2]
                break
    year = cit.get("year") or ""
    if not year:
        m = rv.YEAR_IN_TOKEN_RE.search(fname)
        year = m.group(1) if m else ""
    jt = cit.get("journal") or ""
    parts = authors[:3] + ([year] if year else []) + ([jt] if jt else [])
    key = "_".join(parts) or "unresolved"
    return re.sub(r"[^a-z0-9_]", "", key.lower())[:60]


def alias_dedupe(proposed: str, cit: dict, family_uni: dict, family_alias,
                 kb_title: str = "") -> str:
    """If the proposed key is the same paper as an existing family key, use
    the existing key (never fragment a paper across two keys). Two signals:
    (a) the alias engine resolves the proposal to an existing key; (b) the KB
    title shares >=2 distinctive tokens with an existing key whose first
    surname matches (wowak_2020_female_directors_recalls vs a 2021-issue-year
    frontmatter citekey for the same title)."""
    resolved = family_alias.resolve(proposed)
    if resolved and resolved in family_uni:
        return resolved
    hits = match_citation(cit, family_uni)
    if len(hits) == 1:
        return hits[0]
    if kb_title:
        first = cit["surnames"][0] if cit["surnames"] else ""
        ttoks = {t for t in TOKEN_CUT.split(kb_title.lower()) if len(t) >= 5}
        best_key, best_hits = None, 0
        for k in family_uni:
            ktoks = re.findall(r"[a-z]{3,}", k.lower())
            if first and ktoks and ktoks[0] != first:
                continue
            n = len(ttoks & set(ktoks))
            if n > best_hits:
                best_key, best_hits = k, n
        if best_key and best_hits >= 2:
            return best_key
    return proposed


def source_priority(path: str) -> int:
    for i, tag in enumerate(PRIORITY_TAGS):
        if tag in path:
            pri = i
            break
    else:
        pri = len(PRIORITY_TAGS)
    # reading notes / AI drafts lose to original full texts at the same root:
    # a tie between 'So, Sue Me…If You Can!.md' and '深度阅读笔记 - X.md' must
    # resolve to the former
    if re.search(r"笔记|AI drafts|cards|90 AI", path):
        pri += 0.5
    return pri


PRIORITY_TAGS = ("论文导入", "Clippings", "07 原文", "00 工作台")


def first_parseable_line(body: str):
    """First 来源-ish line that parses as a citation; prose quotes skipped."""
    for ln in SRC_RE.findall(body):
        cit = parse_citation(ln)
        if cit["surnames"] or cit["year"]:
            return ln, cit
    return None, None


def norm_key(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def harvest_low(root: Path, scan) -> list[dict]:
    out = []
    for b in scan.all_blocks():
        if b.wb:
            continue
        body = "\n".join((root / b.rel).read_text(encoding="utf-8")
                         .split("\n")[b.start:b.end])
        line, cit = first_parseable_line(body)
        if not line:
            continue
        out.append({"block": b, "cite_line": norm_key(line), "cit": cit})
    return out


def load_user_rulings() -> list[dict]:
    """Human-verified mappings: {match: citation-substring, kb_file: path,
    key: explicit-canonical-key}. They take precedence over KB filename
    matching (the user read the originals; filenames can lack author names)."""
    if not USER_RULINGS.is_file():
        return []
    doc = yaml.safe_load(USER_RULINGS.read_text(encoding="utf-8")) or {}
    return doc.get("rulings") or []


def _family_entry(key: str) -> dict:
    """Registry-style universe entry for a family key: tokenized (with alpha
    prefixes for fused keys like malshe2015) + year extraction."""
    toks = set(re.findall(r"[a-z0-9]+", key.lower()))
    for t in list(toks):
        m = re.match(r"([a-z]{3,})\d*", t)
        if m:
            toks.add(m.group(1))
    return {"tokens": toks, "years": set(rv.YEAR_IN_TOKEN_RE.findall(key)),
            "meta": {}}


def resolve_all() -> dict:
    idx = build_kb_index()
    universes = {c: registry_universe(c, yaml.safe_load(
        (ROOTS[c] / "_evidence_registry.yaml").read_bytes().decode("utf-8")))
        for c in ROOTS}
    family_uni: dict = {}
    for u in universes.values():
        family_uni.update(u)
    # family-global: pull in the intro and theory key systems too, so a mint
    # never fragments a paper that another corpus already registered
    for src, ext in (("write-introduction/corpus/_evidence_registry.yaml",
                      "introduction"), ("write-theory/corpus/_evidence_registry.yaml",
                                        "theory")):
        doc = yaml.safe_load((SKILLS / src).read_bytes().decode("utf-8"))
        if ext == "introduction":
            for entries in (doc.get("evidence") or {}).values():
                for ed in entries.values():
                    if isinstance(ed, dict):
                        for pkey in rv.flowlist(ed.get("papers")):
                            k2 = rv.strip_journal(pkey)
                            family_uni.setdefault(k2, _family_entry(k2))
            for k2 in (doc.get("paper_index") or {}):
                family_uni.setdefault(k2, _family_entry(k2))
        else:
            for k2 in (doc.get("source_papers") or {}):
                family_uni.setdefault(k2, _family_entry(k2))
    family_alias = rv.AliasIndex(sorted(family_uni), [])
    groups: dict[str, dict] = {}
    for corpus in ROOTS:
        root = ROOTS[corpus]
        scan = rv.scan_corpus(root)
        for hb in harvest_low(root, scan):
            b = hb["block"]
            g = groups.setdefault(hb["cite_line"], {
                "citation": hb["cite_line"], "cit": hb["cit"], "blocks": []})
            g["blocks"].append({"corpus": corpus, "rel": b.rel,
                                "heading": b.heading})
    rulings = []
    user_rulings = load_user_rulings()
    for line_key, g in sorted(groups.items()):
        cit = g["cit"]
        if not cit.get("is_citation", True):
            rule = {"citation": g["citation"][:90], "ruling": "prose_no_citation",
                    "note": "来源行是引文原文而非引用——不可归源",
                    "n_blocks": len(g["blocks"]), "blocks": g["blocks"][:8]}
            rulings.append(rule)
            continue
        # user-verified ruling overrides KB filename matching
        ur = next((u for u in user_rulings
                   if u.get("match", "").lower() in line_key), None)
        if ur:
            key = ur.get("key")
            rule = {"citation": g["citation"][:90], "surnames": cit["surnames"],
                    "year": cit["year"], "journal": cit["journal"],
                    "ruling": "mint_existing_key" if ur.get("existing") else
                    "mint_new_key", "key": key,
                    "kb_file": ur.get("kb_file", "")[:130],
                    "note": "user-verified ruling",
                    "n_blocks": len(g["blocks"]), "blocks": g["blocks"][:8]}
            rulings.append(rule)
            continue
        # composite source line: every '/'-segment parses as its own citation
        # -> mint one marker PER PAPER; any unparseable segment means the '/'
        # was prose structure (technique lists) -> normal single-citation path
        seg_pairs = None
        parts = [p.strip() for p in re.split(r"\s*/\s*", g["citation"]) if p.strip()]
        if len(parts) >= 2 and len(g["citation"]) > 20:
            sub_cits = [parse_citation(p) for p in parts]
            if all(c.get("is_citation") for c in sub_cits):
                seg_pairs = list(zip(parts, sub_cits))
        if seg_pairs:
            sub_keys, all_ok = [], True
            for text, c in seg_pairs:
                hits = match_citation(c, family_uni)
                if len(hits) == 1:
                    sub_keys.append({"cite": text[:60], "key": hits[0]})
                    continue
                kbf = kb_match(c, idx)
                if len(kbf) == 1:
                    m2 = file_metadata(kbf[0]["path"])
                    sub_keys.append({"cite": text[:60],
                                     "key": propose_key(c, m2, kbf[0]["name"])})
                else:
                    all_ok = False
                    break
            if all_ok:
                rule = {"citation": g["citation"][:90],
                        "ruling": "mint_composite_keys", "sub_keys": sub_keys,
                        "n_blocks": len(g["blocks"]), "blocks": g["blocks"][:8]}
                rulings.append(rule)
                continue
            rule = {"citation": g["citation"][:90], "ruling": "composite_multi_paper",
                    "note": "复合行中部分论文无法归源——人工拆分",
                    "n_blocks": len(g["blocks"]), "blocks": g["blocks"][:8]}
            rulings.append(rule)
            continue
        kb = kb_match(cit, idx)
        rule = {"citation": g["citation"][:90], "surnames": cit["surnames"],
                "year": cit["year"], "journal": cit["journal"],
                "n_blocks": len(g["blocks"]), "blocks": g["blocks"][:8]}
        if not kb:
            rule.update({"ruling": "kb_not_found",
                         "note": "KB 未命中——不回填，登记缺口"})
            rulings.append(rule)
            continue
        best = min(kb, key=lambda e: (source_priority(str(e["path"])),))
        ties = [e for e in kb
                if source_priority(str(e["path"])) == source_priority(str(best["path"]))]
        meta = file_metadata(best["path"])
        fam_hits = match_citation(cit, family_uni)
        if len(ties) == 1:
            if len(fam_hits) == 1:
                rule.update({"ruling": "mint_existing_key", "key": fam_hits[0],
                             "kb_file": str(best["path"])[:130],
                             "kb_meta": {k: meta.get(k, "") for k in
                                         ("citekey", "title", "authors", "year")}})
            else:
                proposed = propose_key(cit, meta, best["name"])
                title = str((meta.get("title") or meta.get("_h1") or ""))
                key = alias_dedupe(proposed, cit, family_uni, family_alias,
                                   kb_title=title)
                rule.update({"ruling": "mint_existing_key" if key != proposed
                             else "mint_new_key", "key": key,
                             "proposed_key": proposed,
                             "kb_file": str(best["path"])[:130],
                             "kb_meta": {k: meta.get(k, "") for k in
                                         ("citekey", "title", "authors", "year")}})
        else:
            rule.update({"ruling": "kb_ambiguous",
                         "kb_files": [str(e["path"])[:130] for e in kb[:3]]})
        rulings.append(rule)
    return {"rulings": rulings, "n_groups": len(groups)}


def mint_from_rulings(rulings: list[dict]) -> int:
    minted = 0
    by_line: dict[str, list[str]] = defaultdict(list)
    for r in rulings:
        if r["ruling"] in ("mint_existing_key", "mint_new_key") and r.get("key"):
            by_line[norm_key(r["citation"])].append(r["key"])
        elif r["ruling"] == "mint_composite_keys":
            for sk in r.get("sub_keys", []):
                by_line[norm_key(r["citation"])].append(sk["key"])
    for corpus in ROOTS:
        root = ROOTS[corpus]
        scan = rv.scan_corpus(root)
        # per-file plan; blocks processed in DESCENDING span order so earlier
        # insertions never shift later blocks' line numbers
        plan: dict[str, list] = defaultdict(list)
        for hb in harvest_low(root, scan):
            keys = by_line.get(hb["cite_line"])
            if not keys or hb["block"].wb:
                continue
            b = hb["block"]
            base = f"legacy_{Path(b.rel).stem}_{variant_label(b.heading)}"
            plan[b.rel].append((b.end, base, keys))
        for rel, entries in plan.items():
            path = root / rel
            raw = path.read_bytes().decode("utf-8")
            eol = "\r\n" if "\r\n" in raw else "\n"
            lines = raw.split(eol)
            taken = {it for bb in scan.files[rel]["blocks"] for _c, it in bb.wb}
            for end, base, keys in sorted(entries, key=lambda x: -x[0]):
                markers = []
                for key in keys:
                    item, n = base, 2
                    while item in taken:
                        item = f"{base}_{n}"
                        n += 1
                    taken.add(item)
                    markers.append(f"<!-- wb:{key}:{item} -->")
                lines[end:end] = markers
                minted += len(markers)
            text = eol.join(lines)
            if not text.endswith(eol):
                text += eol
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(text)
    return minted
    return minted


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    apply_mode = "--apply" in sys.argv
    result = resolve_all()
    counts = defaultdict(int)
    for r in result["rulings"]:
        counts[r["ruling"]] += 1
    result["summary"] = dict(counts)
    print(f"unique LOW citations: {result['n_groups']}")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    if apply_mode:
        n = mint_from_rulings(result["rulings"])
        print(f"MINTED from KB rulings: {n}")
        result["minted"] = n
    OUT.write_text(yaml.safe_dump(result, allow_unicode=True, sort_keys=False,
                                  width=100), encoding="utf-8")
    print(f"adjudication -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
