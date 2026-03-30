from __future__ import annotations

import argparse
import pathlib
import re
import sys


REQUIRED_FRONTMATTER_FIELDS = ("name", "description")
REQUIRED_OPENAI_KEYS = ("display_name", "short_description", "default_prompt")


def extract_frontmatter(markdown: str) -> dict[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", markdown, re.DOTALL)
    if not match:
        return {}

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_skill_markdown(skill_md_path: pathlib.Path) -> list[str]:
    errors: list[str] = []

    if not skill_md_path.exists():
        return [f"Missing file: {skill_md_path.name}"]

    content = skill_md_path.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(content)
    if not frontmatter:
        return ["SKILL.md is missing YAML frontmatter"]

    for field in REQUIRED_FRONTMATTER_FIELDS:
        if not frontmatter.get(field):
            errors.append(f"SKILL.md frontmatter is missing required field: {field}")

    name = frontmatter.get("name", "")
    if name and not re.fullmatch(r"[a-z0-9-]+", name):
        errors.append("SKILL.md frontmatter name must use lowercase letters, digits, and hyphens only")

    return errors


def validate_openai_yaml(openai_yaml_path: pathlib.Path) -> list[str]:
    if not openai_yaml_path.exists():
        return [f"Missing file: {openai_yaml_path.as_posix()}"]

    content = openai_yaml_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if "interface:" not in content:
        errors.append("agents/openai.yaml is missing top-level key: interface")

    for key in REQUIRED_OPENAI_KEYS:
        if not re.search(rf"^\s+{re.escape(key)}\s*:", content, re.MULTILINE):
            errors.append(f"agents/openai.yaml is missing required field: {key}")

    return errors


def validate_skill_directory(skill_dir: pathlib.Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_skill_markdown(skill_dir / "SKILL.md"))

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        errors.extend(validate_openai_yaml(openai_yaml))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a SuperpowersHarness skill folder.")
    parser.add_argument("skill_dir", type=pathlib.Path, help="Path to the skill folder to validate")
    args = parser.parse_args()

    errors = validate_skill_directory(args.skill_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {args.skill_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
