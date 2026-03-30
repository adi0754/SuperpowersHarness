# 为 Codex 安装 Superpowers Harness

Codex 会从 `%USERPROFILE%\.codex\skills\` 发现本地 skills。

安装这套能力时，你只需要做三件事：

1. clone 一次仓库
2. 执行安装脚本
3. 重启 Codex

如果你希望让 AI 帮你安装，可以直接这样说：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/adi0754/SuperpowersHarness/main/.codex/INSTALL.md
```

## 1. 获取仓库

```powershell
git clone https://github.com/adi0754/SuperpowersHarness.git SuperpowersHarness
cd .\SuperpowersHarness
```

## 2. 安装 Skill

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Platforms codex
```

脚本会把：

`skills/SuperpowersHarness`

链接到：

`%USERPROFILE%\.codex\skills\SuperpowersHarness`

## 3. 校验

```powershell
python .\scripts\quick_validate.py .\skills\SuperpowersHarness
```

## 4. 重启工具

安装完成后，重启 Codex 或重新打开会话，让 Skill 元数据重新加载。

## 5. 开始使用

```text
use SuperpowersHarness to handle this request with sh-start:

- 当前项目 / 功能背景：
- 这次想解决的问题：
- 为什么现在做：
- 已知约束：
```
