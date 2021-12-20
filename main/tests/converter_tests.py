from unittest import TestCase
from unittest import skip

from main.numeral_systems_converter import convert_10_to_62, convert_62_to_10


class TestConvert10To62(TestCase):

    def test_convert_7(self):
        self.assertEqual(convert_10_to_62(7), '7')

    def test_convert_15(self):
        self.assertEqual(convert_10_to_62(15), 'f')

    def test_convert_128(self):
        self.assertEqual(convert_10_to_62(128), '24')

    def test_convert_3844(self):
        self.assertEqual(convert_10_to_62(3844), '100')


class TestConvert62To10(TestCase):

    def test_convert_7(self):
        self.assertEqual(convert_62_to_10('7'), 7)

    def test_convert_15(self):
        self.assertEqual(convert_62_to_10('f'), 15)

    def test_convert_128(self):
        self.assertEqual(convert_62_to_10('24'), 128)

    def test_convert_3844(self):
        self.assertEqual(convert_62_to_10('100'), 3844)
