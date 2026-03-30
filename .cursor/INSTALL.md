# 为 Cursor 安装 Superpowers Harness

Cursor 会从 `%USERPROFILE%\.cursor\skills\` 发现本地 skills。

安装这套能力时，你只需要做三件事：

1. clone 一次仓库
2. 执行安装脚本
3. 重启 Cursor

如果你希望让 AI 帮你安装，可以直接这样说：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/adi0754/SuperpowersHarness/main/.cursor/INSTALL.md
```

## 1. 获取仓库

```powershell
git clone https://github.com/adi0754/SuperpowersHarness.git SuperpowersHarness
cd .\SuperpowersHarness
```

## 2. 安装 Skill

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -Platforms cursor
```

脚本会把：

`skills/SuperpowersHarness`

链接到：

`%USERPROFILE%\.cursor\skills\SuperpowersHarness`

## 3. 校验

```powershell
python .\scripts\quick_validate.py .\skills\SuperpowersHarness
```

## 4. 重启工具

安装完成后，重启 Cursor 或重新打开会话，让 Skill 元数据重新加载。

## 5. 开始使用

```text
use SuperpowersHarness to handle this request with sh-recover:

- 当前项目 / 功能：
- 最漂移的地方：
- 我这次最想先收回什么：
- 当前已有线索：
```
