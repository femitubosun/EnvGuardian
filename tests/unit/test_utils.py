import unittest
from envguardian._utils import get_schema_key_value_pair_from_environment_variables, \
    validate_dictionary_against_validation_schema
from envguardian._validators import string_validator, integer_validator, boolean_validator, float_validator


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.validation_schema = {
            'name': (string_validator,),
            'age': (integer_validator,),
            'is_employed': (boolean_validator,),
            'salary': (float_validator,),
        }

        self.candidate_dict = {
            'name': 'John Doe',
            'age': 30,
            'is_employed': True,
            'salary': 45000.50,
            'address': '123 Main St.',
        }

    def test_get_schema_key_value_pair_from_environment_variables(self):
        result = get_schema_key_value_pair_from_environment_variables(self.validation_schema, self.candidate_dict)
        expected_result = {
            'name': 'John Doe',
            'age': 30,
            'is_employed': True,
            'salary': 45000.50,
        }
        self.assertEqual(result, expected_result)

    def test_validate_dictionary_against_validation_schema(self):
        result = validate_dictionary_against_validation_schema(self.validation_schema, self.candidate_dict)
        expected_result = [True, True, True, True]
        self.assertEqual(result, expected_result)
