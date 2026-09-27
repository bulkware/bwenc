"""Test encoding conversion without a graphical display."""

from pathlib import Path
import tempfile
import unittest

from bwenc.encconv import EncConv


class EncConvTests(unittest.TestCase):
    """Verify success and useful validation failures."""

    def test_converts_a_text_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("H\xe4me", encoding="latin_1")

            converter = EncConv()
            self.assertTrue(converter.convert_encoding(str(path), "latin_1", "utf_8"))
            self.assertEqual(path.read_text(encoding="utf_8"), "H\xe4me")

    def test_rejects_an_empty_filename(self):
        converter = EncConv()

        self.assertFalse(converter.convert_encoding("", "utf_8", "latin_1"))
        self.assertEqual(converter.message, "Filename is empty.")
