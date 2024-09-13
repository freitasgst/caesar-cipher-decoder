import unittest

from mathlib import dec_to_bin, dec_to_hex, bin_to_dec


class TestMathLib(unittest.TestCase):
    def test_dec_to_bin(self):
        result = dec_to_bin(67523)
        self.assertEqual(result, 10000011111000011)

    def test_dec_to_hex(self):
        result = dec_to_hex(67523)
        self.assertEqual(result, "107c3")

    def test_bin_to_dec(self):
        result = bin_to_dec(10000011111000011)
        self.assertEqual(result, 67523)
