import re


def validate_email(email):
    pattern = r"^[\w.\-]+@[\w.\-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(password):
    return len(password) >= 6


def validate_phone(phone):
    return phone.isdigit() and 8 <= len(phone) <= 15


def validate_age(age):
    try:
        age = int(age)
        return age > 0
    except ValueError:
        return False

def validate_national_id(national_id):
    return national_id.isdigit() and len(national_id) == 14

def validate_number(value, min_value=0, max_value=None, allow_decimal=True):
    try:
        number = float(value) if allow_decimal else int(value)
    except (ValueError, TypeError):
        return False, None

    if number < min_value:
        return False, None

    if max_value is not None and number > max_value:
        return False, None

    return True, number