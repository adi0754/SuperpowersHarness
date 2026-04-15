# 贡献指南

感谢你对 Superpowers Harness 的贡献兴趣！

## 如何贡献

1. Fork 本仓库
2. 创建功能分支
3. 进行修改
4. 运行校验：`python scripts/quick_validate.py skills/<your-skill>`
5. 运行测试：`python -m pytest tests/ -v`
6. 提交 Pull Request

## Skill 规范

- 每个 Skill 必须有包含有效 frontmatter（`name`、`description`）的 `SKILL.md`
- Skill 名称只能使用小写字母、数字和连字符
- 如果面向 OpenAI Codex，需包含 `agents/openai.yaml`

## 报告问题

请使用 GitHub Issue 模板提交 Bug 报告和功能请求。

## 本地开发环境

- Python 3.10+
- 安装测试依赖：`pip install pytest`
- 运行测试：`python -m pytest tests/ -v`
- 校验单个 Skill：`python scripts/quick_validate.py skills/<skill-name>`

## Skill 内容规范

- 4 个入口 Skill 的人类控制点 / 输出风格 / 护栏段落需保持同步
- 修改共性段落时，检查 `<!-- 共性段落 -->` 注释，同步更新 sh-start、sh-pack、sh-run、sh-recover
