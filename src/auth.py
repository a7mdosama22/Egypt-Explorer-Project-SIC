"""
Project A - Egypt Explorer
Login & Registration Module
----------------------------------------------------------------------
Owner: Ali (User / Login / Register)

Data layer -> UserManager
These functions NEVER call print()/input(). They just take arguments
and return values (success flags, messages, user objects).

Usage from the interface (menus/main_menu.py):

    from auth import UserManager
    manager = UserManager()
    ok, msg = manager.register(name, phone, email, gender,
                                governorate, password, age, national_id)
    user, msg = manager.login(email, password)

Persistence:
  All users (including anyone who registers) are saved to
  data/users.json automatically. Data survives closing and
  reopening the app.
"""

import json
import os
import re

from models.user import User

# Fixed administrator account (per project spec)
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


class UserManager:
    """
    Handles registration, login, and persistence.
    Users are stored in a dict keyed by email -> O(1) average lookup,
    which is the 'suitable data structure' requirement from the slides.
    """

    def __init__(self, data_file=USERS_FILE):
        self.data_file = data_file
        self.users = {}  # email -> User
        self._load()

        # make sure the fixed admin account always exists
        if ADMIN_EMAIL not in self.users:
            self.users[ADMIN_EMAIL] = User(
                name="Administrator",
                phone="",
                email=ADMIN_EMAIL,
                gender="",
                governorate="",
                password=ADMIN_PASSWORD,
                age=0,
                national_id="",
                is_admin=True,
            )
            self._save()

    # ---------------- persistence ----------------
    def _load(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                raw = json.load(f)
            for email, user_data in raw.items():
                self.users[email] = User.from_dict(user_data)
        except (json.JSONDecodeError, OSError):
            # corrupted or unreadable file -> start clean instead of crashing
            self.users = {}

    def _save(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(
                {email: user.to_dict() for email, user in self.users.items()},
                f, ensure_ascii=False, indent=2,
            )

    # ---------------- validation helpers ----------------
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[\w.\-]+@[\w.\-]+\.\w+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def is_valid_phone(phone):
        return phone.isdigit() and 8 <= len(phone) <= 15

    @staticmethod
    def is_valid_national_id(national_id):
        return national_id.isdigit() and len(national_id) == 14

    # ---------------- core operations ----------------
    def register(self, name, phone, email, gender, governorate,
                 password, age, national_id):
        """Returns (success: bool, message: str)."""
        if not name.strip():
            return False, "Name cannot be empty."
        if not self.is_valid_email(email):
            return False, "Invalid email format."
        if email in self.users:
            return False, "An account with this email already exists."
        if not self.is_valid_phone(phone):
            return False, "Phone number must contain digits only (8 to 15 digits)."
        if not self.is_valid_national_id(national_id):
            return False, "National ID must be exactly 14 digits."
        try:
            age = int(age)
            if age <= 0 or age > 120:
                raise ValueError
        except (ValueError, TypeError):
            return False, "Age must be a valid, reasonable number."
        if len(password) < 6:
            return False, "Password must be at least 6 characters."

        self.users[email] = User(
            name, phone, email, gender, governorate,
            password, age, national_id, is_admin=False,
        )
        self._save()
        return True, "Account created successfully!"

    def login(self, email, password):
        """Returns (User or None, message: str)."""
        user = self.users.get(email)
        if user is None:
            return None, "This email is not registered."
        if user.password != password:
            return None, "Incorrect password."
        return user, "Login successful."