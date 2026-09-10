// 过滤 pi-cursor-sdk 模型目录缓存（可选）。
// 2026-09-09：用户要求恢复 OpenAI / Anthropic / Gemini，故 BLOCKED_PREFIXES 置空。
// 脚本仍可手动运行；空前缀时不会删除任何模型。
//
// 用法：node C:\Users\admin\.pi\agent\filter-cursor-models.mjs
// 何时需要：若再次想从 /model 列表隐藏某些供应商，往 BLOCKED_PREFIXES 加 id 前缀后重跑。
//
// 注意：只改本地缓存 ~/.pi/agent/cursor-sdk-model-list.json，
// 不改扩展代码，不影响 keyFingerprint 与 fetchedAt（保持 TTL 语义不变）。

import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { join } from "node:path";

const agentDir = join(process.env.USERPROFILE || process.env.HOME, ".pi", "agent");
const cachePath = join(agentDir, "cursor-sdk-model-list.json");

// 置空 = 不过滤。若要再隐藏，例如：["claude", "gpt", "gemini"]
const BLOCKED_PREFIXES = [];

if (!existsSync(cachePath)) {
	console.error(`未找到缓存文件：${cachePath}`);
	console.error("先在 pi 里完成一次 /cursor-refresh-models 再运行本脚本。");
	process.exit(1);
}

const data = JSON.parse(readFileSync(cachePath, "utf8"));
if (!Array.isArray(data.models)) {
	console.error("缓存文件结构异常（models 不是数组），不修改。");
	process.exit(1);
}

if (BLOCKED_PREFIXES.length === 0) {
	console.log(`过滤已停用（BLOCKED_PREFIXES 为空）。当前缓存 ${data.models.length} 个模型，未修改。`);
	console.log(`模型：${data.models.map((m) => m.id).join(", ")}`);
	process.exit(0);
}

const before = data.models.length;
const removed = [];
data.models = data.models.filter((m) => {
	const id = typeof m?.id === "string" ? m.id.toLowerCase() : "";
	const hit = BLOCKED_PREFIXES.some((p) => id.startsWith(p));
	if (hit) removed.push(m.id);
	return !hit;
});

// fetchedAt / keyFingerprint / version 原样保留，扩展校验只要求条目含 id+displayName。
writeFileSync(cachePath, `${JSON.stringify(data, null, 2)}\n`, { mode: 0o600 });

console.log(`过滤完成：${before} → ${data.models.length} 个模型`);
console.log(`移除 ${removed.length} 个：${removed.join(", ")}`);
console.log(`保留：${data.models.map((m) => m.id).join(", ")}`);
