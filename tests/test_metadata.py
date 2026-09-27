"""Check installed-package metadata without native package toolchains."""

from pathlib import Path
from datetime import datetime
import re
import tomllib
import unittest
from xml.etree import ElementTree

from bwenc import __version__
from bwenc.resources import asset_path


ROOT = Path(__file__).resolve().parents[1]
SHORT_DESCRIPTION = "Desktop application for converting text-file encodings"
LONG_DESCRIPTION = "bwEnc converts supported text files between common character encodings."


class MetadataTests(unittest.TestCase):
    """Keep package metadata and bundled files synchronized."""

    def test_application_version_matches_project_and_appstream_metadata(self):
        project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        appstream = ElementTree.parse(ROOT / "data/org.bulkware.bwenc.metainfo.xml")
        release = appstream.find("releases/release")

        self.assertIsNotNone(release)
        version = project["project"]["version"]
        self.assertEqual(release.attrib["version"], version)
        self.assertEqual(__version__, version)
        self.assertIn(f"## [{version}]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_user_facing_descriptions_match_package_metadata(self):
        project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        desktop = (ROOT / "data/org.bulkware.bwenc.desktop").read_text(encoding="utf-8")
        appstream = ElementTree.parse(ROOT / "data/org.bulkware.bwenc.metainfo.xml")
        debian = (ROOT / "debian/control").read_text(encoding="utf-8")
        rpm = (ROOT / "packaging/rpm/bwenc.spec").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        main = (ROOT / "src/bwenc/main.py").read_text(encoding="utf-8")

        self.assertEqual(project["project"]["description"], f"{SHORT_DESCRIPTION}.")
        self.assertIn(f"{SHORT_DESCRIPTION}.", readme)
        self.assertIn(f'"""{SHORT_DESCRIPTION}."""', main)
        self.assertIn(f"Comment={SHORT_DESCRIPTION}", desktop)
        self.assertEqual(appstream.findtext("summary"), SHORT_DESCRIPTION)
        description = " ".join(appstream.find("description/p").itertext())
        self.assertEqual(" ".join(description.split()), LONG_DESCRIPTION)
        self.assertIn(f"Description: {SHORT_DESCRIPTION}", debian)
        self.assertIn(LONG_DESCRIPTION, debian.replace("\n ", " "))
        self.assertIn(f"Summary:        {SHORT_DESCRIPTION}", rpm)
        self.assertIn(LONG_DESCRIPTION, rpm.replace("\n", " "))

    def test_runtime_assets_are_available_without_the_working_directory(self):
        for name in ("icon.png", "about.png", "whitelist.csv"):
            self.assertTrue(Path(asset_path(name)).is_file(), name)

    def test_icon_licensing_is_documented_at_the_project_root(self):
        icons = (ROOT / "ICONS.md").read_text(encoding="utf-8")

        self.assertIn("## Application icons", icons)
        self.assertIn("## Oxygen icons", icons)
        self.assertIn("src/bwenc/assets/about.png", icons)

    def test_native_template_changelog_weekdays_match_their_dates(self):
        """Keep manually seeded native changelog entries valid for their builders."""
        rpm = (ROOT / "packaging/rpm/bwenc.spec").read_text(encoding="utf-8")
        debian = (ROOT / "debian/changelog").read_text(encoding="utf-8")
        rpm_match = re.search(r"^\* (?P<weekday>\w{3}) (?P<date>\w{3} \d{1,2} \d{4}) ",
                              rpm, re.MULTILINE)
        debian_match = re.search(r"^ -- .+  (?P<weekday>\w{3}), (?P<date>\d{1,2} \w{3} \d{4}) ",
                                 debian, re.MULTILINE)

        self.assertIsNotNone(rpm_match)
        self.assertIsNotNone(debian_match)
        rpm_date = datetime.strptime(rpm_match["date"], "%b %d %Y")
        debian_date = datetime.strptime(debian_match["date"], "%d %b %Y")
        self.assertEqual(rpm_match["weekday"], rpm_date.strftime("%a"))
        self.assertEqual(debian_match["weekday"], debian_date.strftime("%a"))
