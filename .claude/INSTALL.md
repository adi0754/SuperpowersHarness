# 为 Claude Code 安装 Superpowers Harness

Claude Code 会从 `%USERPROFILE%\.claude\skills\` 发现本地 skills。

安装这套能力时，你只需要做三件事：

1. clone 一次仓库
2. 执行安装脚本
3. 重启 Claude Code

如果你希望让 AI 帮你安装，可以直接这样说：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/adi0754/SuperpowersHarness/main/.claude/INSTALL.md
```

## 1. 获取仓库

```powershell
git clone https://github.com/adi0754/SuperpowersHarness.git SuperpowersHarness
cd .\SuperpowersHarness
```

## 2. 安装 Skill

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Platforms claude
```

脚本会把 `skills/` 下的 5 个 Skill 分别链接到对应平台目录：

- `superpowers-harness` — 路由器，自动分发到下面 4 个入口
- `sh-start` — 新项目启动
- `sh-pack` — 压执行包
- `sh-run` — 执行
- `sh-recover` — 漂移恢复

## 3. 校验

依次校验每个 Skill：

```powershell
python .\scripts\quick_validate.py .\skills\superpowers-harness
python .\scripts\quick_validate.py .\skills\sh-start
python .\scripts\quick_validate.py .\skills\sh-pack
python .\scripts\quick_validate.py .\skills\sh-run
python .\scripts\quick_validate.py .\skills\sh-recover
```

## 4. 重启工具

安装完成后，重启 Claude Code 或重新打开会话，让 Skill 元数据重新加载。

## 5. 开始使用

新项目？用 `/sh-start` 定方向：

```text
/sh-start

- 当前项目 / 功能背景：
- 这次想解决的问题：
- 为什么现在做：
- 已知约束：
```

方向已定？用 `/sh-pack` 压执行包。执行包就绪？用 `/sh-run` 开始执行。

## Platform Notes

Claude Code supports the `AskUserQuestion` tool, which enables **Mode A** (structured selection UI) for `sh-run` validation records. This is the richest interaction experience.

| Feature | Claude Code |
|---------|-------------|
| Mode A (AskUserQuestion) | Supported |
| Mode B (Quick Confirmation) | Supported |
| Skill discovery | `%USERPROFILE%\.claude\skills\` |
