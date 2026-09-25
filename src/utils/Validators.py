import re


def validate_email(email):
    pattern = r"^[\w.\-]+@[\w.\-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(password):
    return len(password) >= 6


def validate_national_id(national_id):
    return national_id.isdigit() and len(national_id) == 14


def validate_phone(phone):
    return phone.isdigit() and 8 <= len(phone) <= 15


def validate_age(age):
    try:
        age = int(age)
        return 1 <= age <= 120
    except ValueError:
        return False
