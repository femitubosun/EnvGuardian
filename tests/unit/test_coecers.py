import unittest
from envguardian._coercers import string_coercer, enum_coercer, boolean_coercer, integer_coercer, float_coercer


class TestCoercers(unittest.TestCase):

    def test_string_coercer(self):
        self.assertEqual(string_coercer(123), "123")
        self.assertEqual(string_coercer(3.14), "3.14")
        self.assertEqual(string_coercer(True), "True")
        self.assertEqual(string_coercer(None), "None")
        self.assertEqual(string_coercer("Hello"), "Hello")

    def test_enum_coercer(self):
        self.assertEqual(enum_coercer(1), "1")
        self.assertEqual(enum_coercer("Option1"), "Option1")
        self.assertEqual(enum_coercer(True), "True")
        self.assertEqual(enum_coercer(None), "None")

    def test_integer_coercer(self):
        self.assertEqual(integer_coercer(123), 123)
        self.assertEqual(integer_coercer("456"), 456)
        self.assertEqual(integer_coercer(3.14), 3)
        self.assertEqual(integer_coercer(True), 1)
        self.assertEqual(integer_coercer(False), 0)

    def test_float_coercer(self):
        self.assertEqual(float_coercer(3.14), 3.14)
        self.assertEqual(float_coercer("2.71828"), 2.71828)
        self.assertEqual(float_coercer(42), 42.0)
        self.assertEqual(float_coercer(True), 1.0)
        self.assertEqual(float_coercer(False), 0.0)

    def test_boolean_coercer(self):
        self.assertEqual(boolean_coercer(0), False)
        self.assertEqual(boolean_coercer(1), True)
        self.assertEqual(boolean_coercer("True"), True)
        self.assertEqual(boolean_coercer("False"), True)  # Non-empty strings are considered True
        self.assertEqual(boolean_coercer(None), False)
        self.assertEqual(boolean_coercer(10), True)  # Any non-zero value is considered True
