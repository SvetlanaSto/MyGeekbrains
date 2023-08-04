import unittest
from hw14.gethex import get_hex


class TestGetHex(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_hex(0), '0')

    def test_values(self):
        self.assertEqual(get_hex(10), 'a')
        self.assertEqual(get_hex(16), '10')
        self.assertEqual(get_hex(255), 'ff')
        self.assertEqual(get_hex(1024), '400')

    def test_exception(self):
        self.assertRaises(TypeError, get_hex, 'hello')


if __name__ == '__main__':
    unittest.main()
