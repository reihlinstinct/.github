"""Offline funding and scope regressions."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FundingTests(unittest.TestCase):
    def test_exact_approved_link(self):
        self.assertEqual((ROOT / ".github/FUNDING.yml").read_text(), 'custom: ["https://paypal.me/reihalle"]\n')

    def test_only_funding_and_pr_template_are_inheritable(self):
        tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
        forbidden = {"SECURITY.md", "CONTRIBUTING.md", "SUPPORT.md", "CODE_OF_CONDUCT.md", "ACCESSIBILITY.md", "VULNERABILITY_REPORT.yml", "VULNERABILITY_REPORT.yaml"}
        self.assertFalse([p for p in tracked if Path(p).name in forbidden or "/ISSUE_TEMPLATE/" in p or "/DISCUSSION_TEMPLATE/" in p])

    def test_layout(self):
        subprocess.run(["python", "tools/check_repo_layout.py"], cwd=ROOT, check=True)

    def test_layout_rejects_root_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            contract = json.loads((ROOT / ".repo-layout.yml").read_text())
            contract["required"] = []
            (root / ".repo-layout.yml").write_text(json.dumps(contract))
            (root / "stray.py").write_text("# synthetic\n")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            result = subprocess.run(["python", str(ROOT / "tools/check_repo_layout.py"), "--root", tmp], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("denied at repository root: stray.py", result.stdout)
