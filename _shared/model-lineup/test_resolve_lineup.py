"""resolve_lineup.py 单元测试矩阵 — lineup-protocol v1.1/v1.2 不变量验证.

覆盖: 6/7/8 辩手槽 × 7/6/3/2/1 家族；--models 完整/部分/仅裁判/家族冲突/手动 A-B 同族/未知槽位/未验证模型；
single/cheap/max 档；tod A/B 异族（手动报错 vs 两家族自动降级）；截断注记；cursor 降优先；会话模型入池；
fallback 链（辩手排除裁判家族 + 末位 session-default；裁判 fail-closed：仅裁判家族 + 末位 orchestrator）；
placeholder/未知词干不入池；pick_model TIER_RANK；无 registry 全量手动。
核心不变量: 裁判家族 ∉ 辩手家族（除 single/单家族路径）；裁判回退链绝不进入辩手家族。

运行: python -m unittest discover -s . -p "test_resolve_lineup.py" -v   （或直接 python test_resolve_lineup.py）
子进程已内建 PYTHONUTF8=1 + UTF-8 捕获，普通 Windows 控制台无需预设环境变量。
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "resolve_lineup.py")
sys.path.insert(0, HERE)
import resolve_lineup as rl  # noqa: E402

TOC_SLOTS = "identification,construct,theory,scope,alternative,contribution,referee"
TOC8_SLOTS = TOC_SLOTS.replace(",referee", ",dynamic-1,dynamic-2,referee")
TOD_SLOTS = "A,B,referee"


def reg(lines, session="openai-codex/gpt-5.6-sol", truncated=False):
    body = "\n".join("  " + l for l in lines)
    if truncated:
        body += "\n  ... and 171 more"
    return f"Current session model:\n  {session}\n\nAvailable models in this session's registry (copy an exact provider/id when passing model):\n{body}\n"


FULL7 = reg([
    "zai-coding-cn/glm-5.3", "zai-coding-cn/glm-5.3-flash",
    "deepseek/deepseek-v4-pro", "deepseek/deepseek-flash",
    "openai-codex/gpt-5.6-terra", "openai-codex/gpt-5.6-luna", "openai-codex/gpt-5.6-sol",
    "github-copilot/claude-sonnet-5", "github-copilot/claude-haiku-4.5", "github-copilot/claude-opus-5",
    "github-copilot/gemini-3.8-flash",
    "github-copilot/grok-4.6", "github-copilot/grok-4.5",
    "kimi-coding/k3", "kimi-coding/kimi-for-coding",
])
NO_KIMI = FULL7.replace("  kimi-coding/k3\n  kimi-coding/kimi-for-coding\n", "")
THREE_FAM = reg([
    "zai-coding-cn/glm-5.3", "zai-coding-cn/glm-5.3-flash",
    "deepseek/deepseek-v4-pro", "deepseek/deepseek-flash",
    "openai-codex/gpt-5.6-terra", "openai-codex/gpt-5.6-sol",
], session="zai-coding-cn/glm-5.3")
TWO_FAM = reg([
    "zai-coding-cn/glm-5.3", "zai-coding-cn/glm-5.3-flash",
    "github-copilot/claude-sonnet-5", "github-copilot/claude-opus-5",
], session="zai-coding-cn/glm-5.3")
ONE_FAM = reg(["zai-coding-cn/glm-5.3"], session="zai-coding-cn/glm-5.3")


def run(registry_text, slots, lineup=None, models=None, require_distinct=False, use_registry=True):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(registry_text or "")
        path = f.name
    try:
        cmd = [sys.executable, SCRIPT, "--slots", slots]
        if use_registry:
            cmd += ["--registry", path]
        if lineup:
            cmd += ["--lineup", lineup]
        if models:
            cmd += ["--models", models]
        if require_distinct:
            cmd += ["--require-distinct-debaters"]
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=60,
                           env=dict(os.environ, PYTHONUTF8="1"))
        out = json.loads(p.stdout) if p.returncode == 0 and p.stdout.strip() else None
        return p.returncode, out, p.stderr
    finally:
        os.unlink(path)


def slotmap(out):
    return {s["slot"]: s for s in out["slots"]}


def referee_isolated(out):
    ref = slotmap(out)["referee"]["family"]
    debs = [s["family"] for s in out["slots"] if s["role"] == "debater"]
    return ref not in debs or ref == "-"


class TestFullCrossModel(unittest.TestCase):
    def test_full7_6slots_balanced(self):
        rc, out, _ = run(FULL7, TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertIs(out["degraded"], False)
        m = slotmap(out)
        self.assertEqual(m["referee"]["family"], "Claude")
        self.assertEqual(m["referee"]["model"], "github-copilot/claude-opus-5")
        self.assertTrue(referee_isolated(out))
        deb_fams = [s["family"] for s in out["slots"] if s["role"] == "debater"]
        self.assertEqual(len(deb_fams), len(set(deb_fams)))  # 6 槽 6 族
        for s in out["slots"]:
            if s["role"] == "debater" and s["family"] not in ("Gemini",):
                self.assertEqual(s["tier"], "mid")

    def test_full7_8slots_two_reuse(self):
        rc, out, _ = run(FULL7, TOC8_SLOTS)
        self.assertEqual(rc, 0)
        self.assertEqual(out["degraded"], "partial")
        self.assertIn("family reuse", out["degraded_reason"])
        self.assertTrue(referee_isolated(out))
        self.assertEqual(len([s for s in out["slots"] if s["role"] == "debater"]), 8)
        models = [s["model"] for s in out["slots"] if s["role"] == "debater"]
        self.assertNotIn("github-copilot/claude-opus-5", models)

    def test_6fam_partial(self):
        rc, out, _ = run(NO_KIMI, TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertEqual(out["degraded"], "partial")
        self.assertTrue(referee_isolated(out))

    def test_3fam_partial(self):
        rc, out, _ = run(THREE_FAM, TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertTrue(referee_isolated(out))
        m = slotmap(out)
        self.assertEqual(m["referee"]["family"], "GPT")  # 唯一 high 档家族
        deb_fams = set(s["family"] for s in out["slots"] if s["role"] == "debater")
        self.assertTrue(deb_fams <= {"GLM", "DeepSeek"})

    def test_2fam_referee_isolated_debaters_same_family(self):
        rc, out, _ = run(TWO_FAM, TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertEqual(out["degraded"], "partial")
        self.assertIn("2 families", out["degraded_reason"])
        m = slotmap(out)
        self.assertEqual(m["referee"]["family"], "Claude")
        deb_fams = set(s["family"] for s in out["slots"] if s["role"] == "debater")
        self.assertEqual(deb_fams, {"GLM"})
        self.assertTrue(any("共享" in n for n in out["notes"]))  # 单模型家族必然共享实例

    def test_1fam_single_path(self):
        rc, out, _ = run(ONE_FAM, TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertEqual(out["degraded"], True)
        self.assertIn("single-family", out["degraded_reason"])
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "orchestrator")
        for s in out["slots"]:
            if s["role"] == "debater":
                self.assertEqual(s["family"], "GLM")

    def test_session_model_pools_second_family(self):
        rc, out, _ = run(ONE_FAM, TOC_SLOTS)  # ONE_FAM session=glm → 仍 1 家族
        self.assertEqual(out["degraded"], True)
        # registry 只有 GLM 但会话模型是 GPT → 应成 2 家族
        gpt_session = reg(["zai-coding-cn/glm-5.3"], session="openai-codex/gpt-5.6-sol")
        rc2, out2, _ = run(gpt_session, TOC_SLOTS)
        self.assertEqual(rc2, 0)
        self.assertEqual(out2["degraded"], "partial")
        self.assertIn("2 families", out2["degraded_reason"])
        m = slotmap(out2)
        self.assertEqual(m["referee"]["family"], "GPT")
        self.assertEqual(m["referee"]["model"], "openai-codex/gpt-5.6-sol")  # 会话模型入池可被选为裁判


class TestLineups(unittest.TestCase):
    def test_single(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, lineup="single")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "session-default")
        self.assertTrue(all(s["model"] == "session-default" for s in out["slots"]))

    def test_cheap_debaters_referee_still_high(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, lineup="cheap")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["tier"], "high")
        for s in out["slots"]:
            if s["role"] == "debater":
                if s["family"] == "Grok":  # 家族无 cheap 档，就近取最低
                    self.assertEqual(s["tier"], "mid")
                else:
                    self.assertEqual(s["tier"], "cheap")

    def test_max_uses_highest(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, lineup="max")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "github-copilot/claude-opus-5")
        by_fam = {s["family"]: s for s in out["slots"] if s["role"] == "debater"}
        self.assertEqual(by_fam["GPT"]["model"], "openai-codex/gpt-5.6-sol")
        self.assertEqual(by_fam["Gemini"]["model"], "github-copilot/gemini-3.8-flash")  # 仅 cheap，就近

    def test_referee_pref_without_claude_then_gpt(self):
        rc, out, _ = run(NO_KIMI.replace("  github-copilot/claude-sonnet-5\n  github-copilot/claude-haiku-4.5\n  github-copilot/claude-opus-5\n", ""), TOC_SLOTS)
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["family"], "GPT")

    def test_referee_no_high_anywhere(self):
        nohigh = reg([
            "zai-coding-cn/glm-5.3", "deepseek/deepseek-v4-pro",
            "github-copilot/grok-4.6", "kimi-coding/k3",
        ], session="zai-coding-cn/glm-5.3")
        rc, out, _ = run(nohigh, TOC_SLOTS)
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertNotEqual(m["referee"]["family"], "-")
        self.assertTrue(any("high" in n for n in out["notes"]))


class TestManualModels(unittest.TestCase):
    def test_named_referee_only(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, models="referee=openai-codex/gpt-5.6-sol")
        self.assertEqual(rc, 0)
        self.assertEqual(out["lineup"], "manual")
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "openai-codex/gpt-5.6-sol")
        self.assertTrue(referee_isolated(out))
        self.assertNotIn("GPT", [s["family"] for s in out["slots"] if s["role"] == "debater"])

    def test_partial_manual(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, models="theory=deepseek/deepseek-v4-pro")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["theory"]["model"], "deepseek/deepseek-v4-pro")
        self.assertTrue(referee_isolated(out))

    def test_family_conflict_rejected(self):
        rc, out, err = run(FULL7, TOC_SLOTS,
                           models="referee=github-copilot/claude-opus-5,theory=github-copilot/claude-sonnet-5")
        self.assertEqual(rc, 2)
        self.assertIn("隔离", err)

    def test_tod_manual_same_family_rejected(self):
        rc, out, err = run(FULL7, TOD_SLOTS, models="A=zai-coding-cn/glm-5.3,B=zai-coding-cn/glm-5.3-flash",
                           require_distinct=True)
        self.assertEqual(rc, 2)
        self.assertIn("异族", err)

    def test_tod_auto_2fam_degrades_not_errors(self):
        rc, out, _ = run(TWO_FAM, TOD_SLOTS, require_distinct=True)
        self.assertEqual(rc, 0)
        self.assertEqual(out["degraded"], "partial")
        self.assertTrue(any("同家族" in n for n in out["notes"]))
        self.assertTrue(referee_isolated(out))

    def test_unknown_slot_rejected(self):
        rc, out, err = run(FULL7, TOC_SLOTS, models="foo=zai-coding-cn/glm-5.3")
        self.assertEqual(rc, 2)
        self.assertIn("合法槽位", err)

    def test_unverified_manual_model_kept_with_note(self):
        rc, out, _ = run(FULL7, TOC_SLOTS, models="referee=github-copilot/claude-opus-4.8")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "github-copilot/claude-opus-4.8")
        self.assertTrue(any("不在 registry" in n for n in out["notes"]))

    def test_missing_provider_prefix_rejected(self):
        rc, out, err = run(FULL7, TOC_SLOTS, models="referee=claude-opus-5")
        self.assertEqual(rc, 2)
        self.assertIn("provider", err)

    def test_no_registry_full_manual(self):
        rc, out, _ = run(None, TOD_SLOTS,
                         models="A=zai-coding-cn/glm-5.3,B=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5",
                         use_registry=False)
        self.assertEqual(rc, 0)
        self.assertEqual(out["lineup"], "manual")
        self.assertTrue(any("未提供 registry" in n for n in out["notes"]))

    def test_no_registry_partial_manual_rejected(self):
        rc, out, err = run(None, TOD_SLOTS, models="A=zai-coding-cn/glm-5.3", use_registry=False)
        self.assertEqual(rc, 2)


class TestRegistryParsing(unittest.TestCase):
    def test_truncated_note(self):
        rc, out, _ = run(reg([
            "zai-coding-cn/glm-5.3", "github-copilot/claude-opus-5",
        ], truncated=True), TOC_SLOTS)
        self.assertEqual(rc, 0)
        self.assertTrue(any("截断" in n for n in out["notes"]))

    def test_cursor_deprioritized(self):
        dup = reg([
            "cursor/claude-opus-5",
            "zai-coding-cn/glm-5.3", "zai-coding-cn/glm-5.3-flash",
            "deepseek/deepseek-v4-pro", "deepseek/deepseek-flash",
            "openai-codex/gpt-5.6-terra",
            "github-copilot/claude-opus-5",
        ])
        rc, out, _ = run(dup, "identification,referee")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["model"], "github-copilot/claude-opus-5")

    def test_minimal_2slots(self):
        rc, out, _ = run(FULL7, "identification,referee")
        self.assertEqual(rc, 0)
        self.assertEqual(len(out["slots"]), 2)
        m = slotmap(out)
        self.assertEqual(m["identification"]["family"], "GPT")  # 非 Claude 族目录序第一
        self.assertTrue(referee_isolated(out))


class TestFallbackChains(unittest.TestCase):
    def test_debater_chain_excludes_referee_family(self):
        rc, out, _ = run(FULL7, TOC_SLOTS)
        self.assertEqual(rc, 0)
        m = slotmap(out)
        for s in out["slots"]:
            if s["role"] == "debater":
                self.assertFalse(any("claude" in c for c in s["fallback_chain"]),
                                 f"{s['slot']} chain leaks referee family: {s['fallback_chain']}")
                self.assertLessEqual(len(s["fallback_chain"]), 6)

    def test_referee_chain_fail_closed(self):
        # 复审回归：裁判链只允许裁判家族内模型 + 末位 orchestrator；绝不进入辩手家族
        rc, out, _ = run(FULL7, TOC_SLOTS)
        self.assertEqual(rc, 0)
        ref = slotmap(out)["referee"]
        self.assertEqual(ref["family"], "Claude")
        chain = ref["fallback_chain"]
        self.assertEqual(chain[-1], "orchestrator")
        self.assertEqual(ref.get("fallback_exhausted_action"), "orchestrator")
        self.assertLessEqual(len(chain), 6)
        for c in chain[:-1]:
            self.assertIn("claude", c, f"裁判链含非裁判家族条目: {chain}")
        self.assertFalse(any(k in c for c in chain for k in ("gpt", "glm", "deepseek", "gemini", "grok", "kimi")),
                         f"裁判链泄漏辩手家族: {chain}")

    def test_referee_chain_excludes_debater_family_session_default(self):
        # 复审回归夹具：3 家族（Claude 裁判 + GLM/GPT 辩手），session=glm——
        # 旧实现裁判链为 [claude-sonnet, gpt-sol, glm-5.3, session-default:glm]，后三项均辩手族
        r = reg(["zai-coding-cn/glm-5.3", "openai-codex/gpt-5.6-sol",
                 "github-copilot/claude-sonnet-5", "github-copilot/claude-opus-5"],
                session="zai-coding-cn/glm-5.3")
        rc, out, _ = run(r, "A,B,referee")
        self.assertEqual(rc, 0)
        ref = slotmap(out)["referee"]
        self.assertEqual(ref["family"], "Claude")
        chain = ref["fallback_chain"]
        self.assertEqual(chain, ["github-copilot/claude-sonnet-5", "orchestrator"])

    def test_session_default_referee_family_excluded_from_debater_chains(self):
        # session 属裁判家族 → 辩手回退链不得引用 session-default（运行时隔离开口）
        r = reg(["zai-coding-cn/glm-5.3", "deepseek/deepseek-v4-pro",
                 "github-copilot/claude-opus-5"], session="github-copilot/claude-sonnet-5")
        rc, out, _ = run(r, "A,B,referee")
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertEqual(m["referee"]["family"], "Claude")
        for s in out["slots"]:
            if s["role"] == "debater":
                self.assertFalse(any(c.startswith("session-default") for c in s["fallback_chain"]),
                                 f"{s['slot']} chain uses referee-family session-default")
        self.assertTrue(any("裁判家族" in n for n in out["notes"]))

    def test_session_model_reachable_in_debater_chains(self):
        # 会话模型保证可派发 → 每个辩手回退链都应可达（普通条目或 session-default: 前缀）
        rc, out, _ = run(FULL7, TOC_SLOTS)  # FULL7 session = openai-codex/gpt-5.6-sol
        self.assertEqual(rc, 0)
        for s in out["slots"]:
            if s["role"] == "debater":
                chain = s["fallback_chain"]
                reachable = chain[-1].startswith("session-default") or any("gpt-5.6-sol" in c for c in chain)
                self.assertTrue(reachable, f"{s['slot']} session 模型不可达: {chain}")


class TestTodBasic(unittest.TestCase):
    def test_tod_ab_distinct_referee_isolated(self):
        rc, out, _ = run(FULL7, TOD_SLOTS, require_distinct=True)
        self.assertEqual(rc, 0)
        m = slotmap(out)
        self.assertNotEqual(m["A"]["family"], m["B"]["family"])
        self.assertTrue(referee_isolated(out))
        self.assertIs(out["degraded"], False)
        self.assertEqual(m["A"]["family"], "GPT")   # 目录序第一（Claude 留给裁判）
        self.assertEqual(m["B"]["family"], "GLM")
        self.assertEqual(m["referee"]["family"], "Claude")


class TestPureFunctions(unittest.TestCase):
    def test_placeholder_and_unknown_stems_have_no_family(self):
        # 复审回归：family_of('cursor/composer-2')/'cursor/auto' 旧实现返回虚假家族 'Cursor'
        for mid in ("composer-2", "composer", "auto", "default", "unknownmodel-1"):
            self.assertIsNone(rl.family_of(mid), mid)

    def test_known_stems_unchanged(self):
        self.assertEqual(rl.family_of("glm-5.3"), "GLM")
        self.assertEqual(rl.family_of("claude-opus-5"), "Claude")
        self.assertEqual(rl.family_of("gpt-5.6-sol"), "GPT")

    def test_pick_model_cheap_prefers_lowest_available(self):
        # 复审回归：字符串 min() 在 {mid, high} 上把 cheap 选成 high
        entries = [{"tier": "mid"}, {"tier": "high"}]
        self.assertEqual(rl.pick_model(entries, "cheap")["tier"], "mid")
        self.assertEqual(rl.pick_model(entries, "high")["tier"], "high")

    def test_pick_model_max_prefers_highest_available(self):
        entries = [{"tier": "cheap"}, {"tier": "mid"}]
        self.assertEqual(rl.pick_model(entries, "high")["tier"], "mid")
        self.assertEqual(rl.pick_model(entries, "cheap")["tier"], "cheap")

    def test_placeholder_models_not_pooled(self):
        r = reg(["cursor/composer-2", "cursor/auto",
                 "zai-coding-cn/glm-5.3", "github-copilot/claude-opus-5"],
                session="zai-coding-cn/glm-5.3")
        rc, out, _ = run(r, "A,B,referee")
        self.assertEqual(rc, 0)
        fams = {s["family"] for s in out["slots"]}
        self.assertNotIn("Cursor", fams)
        models = {s["model"] for s in out["slots"]}
        self.assertNotIn("cursor/composer-2", models)
        self.assertNotIn("cursor/auto", models)


if __name__ == "__main__":
    unittest.main(verbosity=2)
