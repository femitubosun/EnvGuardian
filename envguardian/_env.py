import functools
import importlib
import os

from ._coercers import string_coercer, float_coercer, boolean_coercer, enum_coercer, integer_coercer
from ._utils import get_schema_key_value_pair_from_environment_variables, \
    validate_dictionary_against_validation_schema
from ._validators import string_validator, float_validator, enum_validator, integer_validator, \
    boolean_validator


def get_schema():
    return getattr(importlib.import_module('Env'), 'env_schema', None)


class Env:

    def __init__(self, validation_schema):
        self.schema = validation_schema

    @staticmethod
    def string():
        """
        String Schema definition. Returns the string validator and coercer
        :return:
        """
        return string_validator, string_coercer

    @staticmethod
    def integer():
        """
        Integer Schema definition. Returns the int validator and coercer
        :return:
        """
        return integer_validator, integer_coercer

    @staticmethod
    def float():
        """
        Float schema definition. Returns the float validator and coercer
        :return:
        """
        return float_validator, float_coercer

    @staticmethod
    def enum(choices):
        """
        Enum schema definition. Returns the enum validator and coercer. Coercer casts to string
        :return:
        """
        return functools.partial(enum_validator, choices=choices), enum_coercer

    @staticmethod
    def boolean():
        """
        Boolean schema definition. Returns the boolean validator and coercer.
        :return:
        """
        return boolean_validator, boolean_coercer

    @staticmethod
    def validate(validation_schema=None):
        """
        Validate environment variable against the validation schema
        :return:
        """

        imported_schema = get_schema()

        if not imported_schema and not validation_schema:
            print('Invalid Validation Schema')

            return

        schema = validation_schema or imported_schema

        candidate_dict = get_schema_key_value_pair_from_environment_variables(schema, dict(os.environ))

        validation_results = validate_dictionary_against_validation_schema(schema, candidate_dict)

        failed_validations = {}

        for index, candidate in enumerate(candidate_dict):
            if validation_results[index] is True:
                continue

            failed_validations[candidate] = validation_results[index]

        if len(failed_validations):
            raise ValueError(str(failed_validations))

    @staticmethod
    def get(environment_variable, validation_schema=None):
        imported_schema = get_schema()

        if not imported_schema and not validation_schema:
            print('Invalid Validation Schema')

            return

        schema = validation_schema or imported_schema

        val = os.environ.get(environment_variable, None)

        if not val:
            return None

        return schema.get(environment_variable)[1](val)


__all__ = ['Env']
