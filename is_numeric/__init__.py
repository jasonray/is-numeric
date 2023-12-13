import re


def is_numeric(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        return bool(re.match(r"^-?\d+(\.\d+)?$", value))
    return False
