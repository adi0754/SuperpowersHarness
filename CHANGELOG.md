# 更新日志

本项目的所有重要变更都会记录在此文件中。

## [未发布]

### 新增
- Skill 架构拆分：路由器（`superpowers-harness`）+ 4 个独立入口 Skill（`sh-start`、`sh-pack`、`sh-run`、`sh-recover`）
- 端到端示例：`examples/blog-ai-summary/`
- 5 分钟快速上手指南：`docs/quick-start.md`
- 自适应学习摘要（按复杂度分级：踩坑速记 / 探索旅程）
- Agent 自适应验收（Mode A: AskUserQuestion，Mode B: 快速确认协议）
- 短输入的最小触发规则
- MIT License、CONTRIBUTING.md、Issue 模板

### 变更
- README.md：新增 Mermaid 流程图、"何时不适用"章节
- 输出契约：新增 3 个违规示例
- sh-pack：新增任务粒度说明（为什么是 4-6 个任务）

### 修复
- 测试路径与实际目录名对齐
- INSTALL.md 路径与实际 Skill 目录结构对齐

### Round 3 Review 修复

- sh-recover 漂移诊断决策树（轻度/中度/重度三级分类）
- 多轮迭代指南（`docs/iteration-guide.md`）
- INSTALL.md 跨平台功能差异说明（Mode A/B）
- 共性段落同步注释（4 个入口 SKILL.md）
- docs/plans/ 状态标记和 README
- 全项目文档统一为中文
- sh-pack Handoff Rule
- 测试参数化覆盖 5 个 Skill
- INSTALL.md "开始使用"统一为斜杠命令格式
