

def get_schema_key_value_pair_from_environment_variables(validation_schema, values_dict):
    """
    This function gets the key-value pair of the defined keys in the validation schema from another dictionary
    :param validation_schema:
    :param values_dict:
    :return: Dict[str, Any]
    """
    schema_keys = list(validation_schema)

    schema_values = {}

    for schema_key in schema_keys:
        schema_values[schema_key] = values_dict.get(schema_key, None)

    return schema_values


def validate_dictionary_against_validation_schema(validation_schema,
                                                  candidate_dict):
    """
    This function validates a candidate dict against a validation_schema

    :param validation_schema: Dict[str, Any]
    :param candidate_dict: Dict[str, Any]
    :return: [bool | str]
    """
    schema_keys = list(validation_schema)

    return [validation_schema[key][0](candidate_dict[key]) for key in schema_keys]
