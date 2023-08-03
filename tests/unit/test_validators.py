import unittest
from envguardian._validators import string_validator, enum_validator, integer_validator, boolean_validator, \
    float_validator


class TestValidators(unittest.TestCase):
    def test_string_validator(self):
        self.assertEqual(string_validator("hello"), True)
        self.assertEqual(string_validator(123), "`123` is not a string")
        self.assertEqual(string_validator([1, 2, 3]), "`[1, 2, 3]` is not a string")

    def test_enum_validator(self):
        self.assertEqual(enum_validator("A", ["A", "B", "C"]), True)
        self.assertEqual(enum_validator("D", ["A", "B", "C"]), "`D` is not one of: ['A', 'B', 'C']")
        self.assertEqual(enum_validator(1, ["A", "B", "C"]), "`1` is not one of: ['A', 'B', 'C']")

    def test_integer_validator(self):
        self.assertEqual(integer_validator(123), True)
        self.assertEqual(integer_validator("123"), True)
        self.assertEqual(integer_validator("B"), "`B` is not an integer")

    def test_float_validator(self):
        self.assertEqual(float_validator(3.14), True)
        self.assertEqual(float_validator("A"), "`A` is not a float")

    def test_boolean_validator(self):
        self.assertEqual(boolean_validator(True), True)
        self.assertEqual(boolean_validator(False), True)
        self.assertEqual(boolean_validator("True"), True)
        self.assertEqual(boolean_validator("False"), True)
        self.assertEqual(boolean_validator(1), "`1` is not a boolean")
        self.assertEqual(boolean_validator(0), "`0` is not a boolean")
        self.assertEqual(boolean_validator("hello"), "`hello` is not a boolean")
