"""
Login & Registration.
Owner: Member 1
"""

from src.models.user import User
from src.utils.data_manager import load_users, save_users


def login(email, password, users=None):
    """
    Check email/password against stored users.
    Returns the matching User object, or None if not found.
    """
    users = users if users is not None else load_users()
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None


def register(name, phone, email, gender, governorate,
             password, age, national_id):
    """
    Create a new normal user, save to users.json, and return the User object.
    Returns None if the email is already registered.
    """
    users = load_users()

    if any(u.email == email for u in users):
        return None  # email already exists

    # TODO: validate inputs (email format, phone format, age > 0, etc.)
    # See TODO in validators — decide together if validation lives here
    # or in a separate validators.py

    new_user = User(
        name=name, phone=phone, email=email, gender=gender,
        governorate=governorate, password=password, age=age,
        national_id=national_id, role="user",
    )
    users.append(new_user)
    save_users(users)
    return new_user
