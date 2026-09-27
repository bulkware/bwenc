"""Test strict validation of release-note input."""

import importlib.util
from pathlib import Path
import sys
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/package_metadata.py"
MODULE_SPEC = importlib.util.spec_from_file_location("package_metadata", MODULE_PATH)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError(f"Cannot load {MODULE_PATH}")
PACKAGE_METADATA = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = PACKAGE_METADATA
MODULE_SPEC.loader.exec_module(PACKAGE_METADATA)


class PackageMetadataTests(unittest.TestCase):
    """Ensure native builds have an unambiguous published release."""

    def test_current_changelog_is_a_valid_published_release(self):
        release = PACKAGE_METADATA.parse_changelog(ROOT / "CHANGELOG.md")
        project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

        self.assertEqual(release.version, project["project"]["version"])
        self.assertTrue(release.entries)
