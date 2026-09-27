"""Test changelog-driven release-metadata synchronization."""

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
MODULE_PATH = SCRIPTS / "prepare_release.py"
MODULE_SPEC = importlib.util.spec_from_file_location("prepare_release", MODULE_PATH)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError(f"Cannot load {MODULE_PATH}")
PREPARE_RELEASE = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = PREPARE_RELEASE
MODULE_SPEC.loader.exec_module(PREPARE_RELEASE)


class PrepareReleaseTests(unittest.TestCase):
    """Keep derived release metadata synchronized with published releases."""

    def test_updates_release_metadata_from_the_latest_changelog_release(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "CHANGELOG.md").write_text(
                "# Changelog\n\n## [Unreleased]\n\n## [1.6.1] - 2026-09-28\n\n"
                "### Fixed\n\n- Correct runtime version.\n",
                encoding="utf-8",
            )
            (root / "pyproject.toml").write_text(
                '[project]\nversion = "1.6.0"\n', encoding="utf-8"
            )
            (root / "data/org.bulkware.bwenc.metainfo.xml").write_text(
                "<component>\n  <releases>\n  </releases>\n</component>\n", encoding="utf-8"
            )
            PREPARE_RELEASE.sync_release(root)

            self.assertIn('version = "1.6.1"', (root / "pyproject.toml").read_text())
            self.assertIn('release version="1.6.1" date="2026-09-28"',
                          (root / "data/org.bulkware.bwenc.metainfo.xml").read_text())
