"""Test small presentation helpers."""

import unittest

from bwenc.functions import convert_bytes


class ConvertBytesTests(unittest.TestCase):
    """Keep file-size formatting behaviour stable."""

    def test_formats_byte_sizes(self):
        self.assertEqual(convert_bytes(0), "0 B")
        self.assertEqual(convert_bytes(1024), "1024 B")
        self.assertEqual(convert_bytes(1025), "1.0 KB")
