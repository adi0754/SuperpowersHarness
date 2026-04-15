---
name: superpowers-harness
description: Superpowers Harness 工作流路由器。识别应使用哪个入口（sh-start、sh-pack、sh-run、sh-recover）并重定向。当用户提到 superpowers harness 但未指定入口时使用。
---

# Superpowers Harness — 入口路由器

本 Skill 负责将请求路由到正确的入口。每个入口都是独立的 Skill。

## 入口映射

| 入口 | Skill | 用途 |
| --- | --- | --- |
| `sh-start` | `/sh-start` | 新项目启动；在现有项目上启动大功能 |
| `sh-pack` | `/sh-pack` | 将已确认的方向压缩为一个当前执行包 |
| `sh-run` | `/sh-run` | 执行已编写好的执行包 |
| `sh-recover` | `/sh-recover` | 项目漂移或叙事漂移后重新掌控 |

## 你的任务

1. 阅读用户的消息。
2. 根据以下示例将其映射到最近的入口：
   - "启动这个项目" / "规划这个大功能" -> `sh-start`
   - "创建当前执行包" -> `sh-pack`
   - "开始实施" / "执行这个包" -> `sh-run`
   - "这个项目已经漂移了" / "重新掌控" -> `sh-recover`
3. 如果用户明确指定了入口，信任它。
4. 使用 Skill 工具调用匹配的 Skill（例如调用 `sh-run`）。
5. 如果无法确定入口，询问用户需要哪一个。

不要直接执行任何工作流 — 始终委托给匹配的 `sh-*` Skill。
