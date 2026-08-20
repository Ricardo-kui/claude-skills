---
name: handoff
description: 把当前会话压缩成交接文档，让新会话或另一个 agent 无缝继续。Use when the user asks to hand off, wrap up a session, or continue the work in a new session。触发词：「交接」「handoff」「写个交接文档」「新会话继续」「换个窗口接着做」。
when_to_use: "触发词：交接、handoff、写交接文档、新会话继续、换个窗口接着做。"
whenToUse: Use when wrapping up the current session into a handoff document so a fresh session or another agent can continue seamlessly. Trigger words: 交接, handoff, 写个交接文档, 新会话继续, 换个窗口接着做
---

# Handoff — 会话交接

写一份交接文档，让零上下文的新 agent 直接继续当前工作。保存到系统临时目录（**不写进当前工作区**），并在聊天中报告完整路径。若用户附带参数，把它当作"下个会话的焦点"，按此裁剪详略。

## 文档内容

1. **目标与当前状态**：在做什么、进行到哪一步、明确的下一步动作。
2. **关键决策及依据**：只写本会话新产生、且尚未落入任何持久产物的决策。已有规范产物——`paper-state.yaml`、`PROJECT_STATUS.md`、Decision Register、代码 diff、commit——**按路径引用，不复制内容**。
3. **Suggested skills**：新会话应调用的技能清单及各自用途（如 `write-theory`、`staggered-did`、`grill-the-claim`）。
4. **环境事实**：关键路径、数据文件、运行中的后台任务、未解决的报错。

## 纪律

- **引用而非复制**：已被其他产物捕获的内容一律按路径/URL 引用；文档里只保留"哪里找"和"为什么这么定"。
- **脱敏**：API key、密码、个人可识别信息一律不写入。
- **证据完整性声明**：末尾附一句"哪些结论已验证、哪些是会话中未验证的判断"，让接手方知道该怀疑什么。
