import re


def is_numeric(value):
    return _is_numeric_using_error(value)


def _is_numeric_regex(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        return bool(re.match(r"^-?\d+(\.\d+)?$", value))
    return False


def _is_numeric_regex_plus_isnumeric(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.isnumeric():
        return True
    if isinstance(value, str):
        return bool(re.match(r"^-?\d+(\.\d+)?$", value))
    return False


def _is_numeric_using_error(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def _str_isnumeric(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.isnumeric():
        return True
    return False
