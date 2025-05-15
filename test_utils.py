import unittest
from utils import validate_input, format_name


class TestUtils(unittest.TestCase):
    def test_validate_input(self):
        self.assertTrue(validate_input("text"))
        self.assertFalse(validate_input(""))
        self.assertFalse(validate_input("   "))

    def test_format_name(self):
        self.assertEqual(format_name("john"), "John")
        self.assertEqual(format_name("JANE"), "Jane")
        self.assertEqual(format_name("  bob  "), "Bob")


if __name__ == "__main__":
    unittest.main() 