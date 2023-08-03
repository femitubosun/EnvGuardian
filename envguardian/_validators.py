def string_validator(candidate):
    return type(candidate).__name__ == 'str' or f"`{candidate}` is not a string"


def enum_validator(candidate, choices):
    return candidate in choices or f"`{candidate}` is not one of: {choices}"


def integer_validator(candidate):
    try:
        int(candidate)
        return True
    except:
        return f"`{candidate}` is not an integer"


def float_validator(candidate):
    try:
        float(candidate)
        return True
    except:
        return f"`{candidate}` is not a float"


def boolean_validator(candidate):
    if candidate == 'True' or candidate == 'False' or type(candidate).__name__ == 'bool':
        return True
    else:
        return f"`{candidate}` is not a boolean"
