import importlib.util
import pathlib
import tempfile
import textwrap
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "quick_validate.py"


def load_module():
    spec = importlib.util.spec_from_file_location("quick_validate", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QuickValidateTests(unittest.TestCase):
    def create_skill(self, root: pathlib.Path, skill_md: str, openai_yaml: str | None = None):
        skill_dir = root / "demo-skill"
        agents_dir = skill_dir / "agents"
        agents_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
        if openai_yaml is not None:
            (agents_dir / "openai.yaml").write_text(openai_yaml, encoding="utf-8")
        return skill_dir

    def test_valid_skill_folder_passes(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            skill_dir = self.create_skill(
                pathlib.Path(tmp_dir),
                textwrap.dedent(
                    """\
                    ---
                    name: demo-skill
                    description: Use when validating a demo skill folder.
                    ---

                    # Demo Skill

                    Keep the body short.
                    """
                ),
                textwrap.dedent(
                    """\
                    interface:
                      display_name: "Demo Skill"
                      short_description: "Validate a demo skill"
                      default_prompt: "Use demo-skill to validate this sample."
                    """
                ),
            )

            errors = module.validate_skill_directory(skill_dir)

            self.assertEqual(errors, [])

    def test_missing_description_is_reported(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            skill_dir = self.create_skill(
                pathlib.Path(tmp_dir),
                textwrap.dedent(
                    """\
                    ---
                    name: demo-skill
                    ---

                    # Demo Skill
                    """
                ),
            )

            errors = module.validate_skill_directory(skill_dir)

            self.assertIn("SKILL.md frontmatter is missing required field: description", errors)

    def test_repository_skill_passes_validation(self):
        module = load_module()

        skill_dir = REPO_ROOT / "skills" / "SuperpowersHarness"

        errors = module.validate_skill_directory(skill_dir)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
