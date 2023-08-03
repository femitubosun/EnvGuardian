import unittest
import os
from envguardian._env import Env


class TestValidateIntegration(unittest.TestCase):
    def setUp(self):
        self.validation_schema = {
            'DATABASE_URL': Env.string(),
            'SECRET_KEY': Env.string(),
            'DEBUG': Env.boolean()
        }

        self.candidate_dict = {
            'name': 'John Doe',
            'age': 30,
            'is_employed': True,
            'salary': 45000.50,
            'address': '123 Main St.',
        }

    def test_validate_with_valid_environment(self):
        # Set up a sample environment with valid variables
        os.environ['DATABASE_URL'] = 'postgresql://user:password@localhost/db'
        os.environ['SECRET_KEY'] = 'mysecretkey'
        os.environ['DEBUG'] = 'True'

        try:
            # Simulate the validation process by calling the `validate` method
            Env.validate(self.validation_schema)
        except ValueError:
            self.fail("Validation should pass for a valid environment")

    def test_validate_with_invalid_environment(self):
        # Set up a sample environment with missing variables
        os.environ['DATABASE_URL'] = 'postgresql://user:password@localhost/db'
        os.environ['SECRET_KEY'] = 'mysecretkey'

        try:
            # Simulate the validation process by calling the `validate` method
            Env.validate(self.validation_schema)
        except ValueError as e:
            self.assertIn("DEBUG", str(e))
            self.assertNotIn("DATABASE_URL", str(e))
            self.assertNotIn("SECRET_KEY", str(e))
