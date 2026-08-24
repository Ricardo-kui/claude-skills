#!/usr/bin/env python3
"""
rhetoric-moves 查重护栏（Plagiarism Guard）—— 句子级 4-gram 重合检测

用户裁决（2026-08-24 三次裁定，终版；下限 2026-08-24 调为 10%；下限强度 2026-08-24 改软）：
  整体重复率：不高于 40%（硬拦截）、不低于 10%（软目标）
    - 整体 > 40% → 逼近查重风险，用跨源合成压低（硬拦截）
    - 整体 < 10% → 离范例修辞骨架较远，提示回写更靠近骨架（软提示，不判 FAIL）
  单句单篇重复率：不高于 50%（硬拦截）
    （单源 ⊆ 并集，故单句单篇 ≤ 该句的并集重合；但整体是各句加权平均，单句可高于整体——
      50% 专抓"整段稀释、单句照抄单篇"的情形，故按句单独设上限）
  唯一豁免：句子带引号直接引用一篇论文的整句（学术惯例，强调用）——
    引号内引文（"…" / “…”）从计算中整体剔除，不计入整体与单篇；
    整段皆为引文时自动豁免（非引文散文为空，视为通过）。
  下限豁免：非引文散文过短（<15 tokens，典型=引号引文 + 简短出处/过渡语）时，
    不提示下限（此时没有足够的改写散文去"吸收骨架"，只查上限与单句单篇）。

算法：
  1) 剥离引号段，得到非引文散文；
  2) 非引文散文整体重合 = |散文 ∩ ∪参照| / |散文|  → 须 ≤40%（硬）；<10% 为软提示；
  3) 逐句单篇重合 = 该句（非引文）与单篇参照的最大 4-gram 重合占比 → 建议 ≤50%（硬）；
  4) 引号段数计入报告（提示"已剔除 N 处直接引用"）。

用法：
  python guard.py "<候选>" --ref "<锚点A>" --ref "<锚点B>"
  python guard.py --candidate-file draft.md --ref-file anchor1.md --ref-file anchor2.md
  python guard.py "candidate" --ref "anchor" --overall-lo 0.10 --overall-hi 0.40 --single-hi 0.50

退出码：0 = PASS（整体入区间 且 各句单篇 ≤50%）；1 = FAIL；2 = 用法错误。

无外部依赖（stdlib），Windows 下自动 UTF-8 输出。
"""
import argparse
import re
import sys

QUOTE_RE = re.compile(r'["“][^"”\n]+["”]')
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
MIN_PROSE_TOKENS = 15  # 非引文散文低于此 token 数 → 下限豁免（引文+简短出处场景）


def ngrams(text, n):
    """把文本规整为小写 token 流后取连续 n-gram 集合。"""
    tokens = re.sub(r"[^a-z0-9 ]", " ", text.lower()).split()
    return {" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)} if len(tokens) >= n else set()


def split_sentences(text):
    """按句末标点切分（引号段已在调用前剔除，不干扰切分）。"""
    return [s for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]


def guard(candidate, references, n=4, overall_lo=0.10, overall_hi=0.40, single_hi=0.50):
    """候选对参照集的查重判定。

    返回 dict：overall（非引文散文整体重合）、per_sentence（各句单篇重合）、
    quoted_spans（被剔除的引号段数）、all_quoted（整段皆引文→豁免）、
    ok（bool）、reasons（未过的约束及提示）。
    """
    quoted_spans = QUOTE_RE.findall(candidate)
    prose = QUOTE_RE.sub(" ", candidate)
    sentences = split_sentences(prose)
    ref_ngrams_list = [ngrams(r, n) for r in references]
    union = set().union(*ref_ngrams_list) if ref_ngrams_list else set()

    per_sentence = []
    for s in sentences:
        sg = ngrams(s, n)
        single = 0.0
        if sg and ref_ngrams_list:
            single = max(len(sg & rn) / len(sg) for rn in ref_ngrams_list)
        per_sentence.append({"text": s.strip(), "single": single, "ok": single <= single_hi})

    cn = ngrams(prose, n)
    overall = 0.0
    if cn and union:
        overall = len(cn & union) / len(cn)
    all_quoted = not cn  # 非引文散文不足一个 n-gram → 整段为引文，自动豁免
    prose_tokens = len(prose.split())
    lower_applies = prose_tokens >= MIN_PROSE_TOKENS  # 散文过短（引文+简短出处）→ 下限豁免

    reasons = []
    if all_quoted:
        reasons.append("全部为引号直接引用，自动豁免（不计算重合）")
    else:
        if overall > overall_hi:
            reasons.append(
                f"整体重合 {overall:.3f} > 上限 {overall_hi:.2f}：逼近查重风险，需跨源合成压低（硬拦截）"
            )
        elif lower_applies and overall < overall_lo:
            reasons.append(
                f"整体重合 {overall:.3f} < 下限 {overall_lo:.2f}：离范例骨架较远，回写时可保留更多该 move 的信号句式（软提示，不判 FAIL）"
            )
        elif not lower_applies:
            reasons.append(
                f"非引文散文仅 {prose_tokens} tokens（<{MIN_PROSE_TOKENS}），下限豁免——引号引文已剔除"
            )
    for ps in per_sentence:
        if not ps["ok"]:
            reasons.append(
                f"单句单篇 {ps['single']:.3f} > {single_hi:.2f}：<{ps['text'][:50]}…>——"
                f"若非带引号直接引用，需重写或跨源合成（硬拦截）"
            )

    # 硬闸门 = 上限 40% + 各句单篇 50%；下限 10% 只提示不拦截（用户 2026-08-24 改软）
    ok = (all_quoted or overall <= overall_hi) and all(ps["ok"] for ps in per_sentence)
    return {
        "overall": overall,
        "overall_lo": overall_lo,
        "overall_hi": overall_hi,
        "single_hi": single_hi,
        "per_sentence": per_sentence,
        "quoted_spans": len(quoted_spans),
        "all_quoted": all_quoted,
        "prose_tokens": prose_tokens,
        "lower_applies": lower_applies,
        "ok": ok,
        "reasons": reasons,
    }


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError as exc:
        sys.stderr.write(f"读取失败: {path}: {exc}\n")
        sys.exit(2)


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="rhetoric-moves 查重护栏：整体 ≤40%（硬）、<10% 软提示，单句单篇 ≤50%（硬），引号直接引用豁免。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("candidate", nargs="?", help="候选句/段落（也可用 --candidate-file）")
    parser.add_argument("--candidate-file", help="从文件读取候选文本")
    parser.add_argument("--ref", action="append", default=[], help="单个参考来源文本，可多次（每个 --ref 视为独立来源）")
    parser.add_argument("--ref-file", action="append", default=[], help="参考来源文件，可多次")
    parser.add_argument("--overall-lo", type=float, default=0.10, help="整体重合下限（软约束：低于只提示'离骨架太远'，不判 FAIL；非引文散文<15 tokens 时不提示）")
    parser.add_argument("--overall-hi", type=float, default=0.40, help="整体重合上限（高于=需跨源合成）")
    parser.add_argument("--single-hi", type=float, default=0.50, help="单句单篇重合上限")
    parser.add_argument("--n", type=int, default=4, help="n-gram 阶数")
    args = parser.parse_args(argv)

    if args.candidate and args.candidate_file:
        parser.error("候选文本与 --candidate-file 只能给一个")
    if args.candidate_file:
        candidate = read_text(args.candidate_file)
    elif args.candidate:
        candidate = args.candidate
    else:
        parser.error("必须提供候选文本（位置参数）或 --candidate-file")

    references = list(args.ref)
    references += [read_text(p) for p in args.ref_file]
    if not references:
        parser.error("必须至少给一个参考来源：--ref <文本> 或 --ref-file <路径>")

    result = guard(
        candidate, references, n=args.n, overall_lo=args.overall_lo, overall_hi=args.overall_hi, single_hi=args.single_hi
    )
    prose_ngrams = len(ngrams(QUOTE_RE.sub(" ", candidate), args.n))
    print(f"candidate-ngrams(non-quote)={prose_ngrams}  sentences={len(result['per_sentence'])}  "
          f"refs={len(references)}  quoted-spans-exempt={result['quoted_spans']}")
    if result["all_quoted"]:
        band_label = "all-quoted (exempt)"
    elif result["overall"] > result["overall_hi"]:
        band_label = "OUT-OF-BAND (>上限，硬拦截)"
    elif result["lower_applies"] and result["overall"] < result["overall_lo"]:
        band_label = "below-floor (<下限，软提示不拦截)"
    elif not result["lower_applies"] and result["overall"] < result["overall_lo"]:
        band_label = "prose<{0}-tokens (下限豁免，仅 {1:.2f} 上限生效)".format(
            MIN_PROSE_TOKENS, args.overall_hi
        )
    else:
        band_label = "in-band [10%,40%]"
    print(f"overall-overlap={result['overall']:.3f}  band=[{args.overall_lo:.2f}, {args.overall_hi:.2f}]  "
          f"prose-tokens={result['prose_tokens']}  -> {band_label}")
    for i, ps in enumerate(result["per_sentence"], 1):
        mark = "ok" if ps["ok"] else f"> {args.single_hi:.2f} !!"
        print(f"  s{i} single-source={ps['single']:.3f}  [{mark}]  {ps['text'][:60]}")
    for r in result["reasons"]:
        print(f"  note: {r}")
    verdict = "PASS" if result["ok"] else "FAIL"
    print(f"verdict: {verdict}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
