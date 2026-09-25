"""
Project A - Egypt Explorer
Login & Registration Module
----------------------------------------------------------------------
Owner: Ali (User / Login / Register)

This file is deliberately split into two layers so it plugs into ANY
interface (console, GUI, web) without rewriting logic:

  1. Data layer  -> User, UserManager, NavigationStack
     These NEVER call print()/input(). They just take arguments and
     return values (success flags, messages, user objects). Whoever
     builds the interface (e.g. Simon) should call these directly:

         from auth import UserManager, NavigationStack

         manager = UserManager()
         ok, msg = manager.register(name, phone, email, gender,
                                     governorate, password, age, national_id)
         user, msg = manager.login(email, password)

  2. Console layer -> register_flow(), login_flow(), main_menu()
     A simple text-based demo/reference implementation, and also a
     working fallback if no other interface is ready in time.

Persistence:
  All users (including anyone who registers) are saved to
  data/users.json automatically, the same way attraction data is
  saved under data/ by the rest of the team. Data survives closing
  and reopening the app.

Shared state teammates need:
  - `manager.users` -> dict {email: User}, for anything else that
    needs the current logged-in user's data (e.g. building "My Trip").
  - `NavigationStack` -> shared "go back" stack. Create ONE instance
    in main() and pass it into every page function.
"""

import json
import os
import re

# Fixed administrator account (per project spec)
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


class User:
    """Represents one registered user (normal user or admin)."""

    def __init__(self, name, phone, email, gender, governorate,
                 password, age, national_id, is_admin=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.national_id = national_id
        self.is_admin = is_admin

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "governorate": self.governorate,
            "password": self.password,
            "age": self.age,
            "national_id": self.national_id,
            "is_admin": self.is_admin,
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            gender=data.get("gender", ""),
            governorate=data.get("governorate", ""),
            password=data.get("password", ""),
            age=data.get("age", 0),
            national_id=data.get("national_id", ""),
            is_admin=data.get("is_admin", False),
        )

    def __repr__(self):
        return f"User({self.name}, {self.email}, admin={self.is_admin})"


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


class NavigationStack:
    """
    Simple LIFO stack for 'back' navigation between pages.
    Shared across the whole app: every teammate's page pushes its own
    name before navigating forward, and pops to go back.
    """

    def __init__(self):
        self._stack = []

    def push(self, page_name):
        self._stack.append(page_name)

    def pop(self):
        return self._stack.pop() if self._stack else None

    def peek(self):
        return self._stack[-1] if self._stack else None

    def is_empty(self):
        return len(self._stack) == 0


# ---------------------------------------------------------------------
# Console UI (reference implementation / fallback)
# ---------------------------------------------------------------------

def register_flow(manager: UserManager):
    print("\n--- Create New Account ---")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    gender = input("Gender (Male/Female): ")
    governorate = input("Governorate: ")
    password = input("Password: ")
    age = input("Age: ")
    national_id = input("National ID: ")

    success, message = manager.register(
        name, phone, email, gender, governorate, password, age, national_id
    )
    print(message)
    return success


def login_flow(manager: UserManager):
    print("\n--- Login ---")
    email = input("Email: ")
    password = input("Password: ")
    user, message = manager.login(email, password)
    print(message)
    return user


def main_menu():
    manager = UserManager()
    nav = NavigationStack()

    while True:
        try:
            print("\n=== Egypt Explorer ===")
            print("1) Login")
            print("2) Register")
            print("3) Exit")
            choice = input("Choose: ").strip()

            if choice == "1":
                user = login_flow(manager)
                if user:
                    nav.push("login")
                    if user.is_admin:
                        print(f"\nWelcome, Admin {user.name}!")
                        # TODO (teammate on Admin panel):
                        # admin_panel.run(user, nav)
                    else:
                        print(f"\nWelcome, {user.name}!")
                        # TODO (teammate on Home/Categories page):
                        # home.run(user, nav)
            elif choice == "2":
                register_flow(manager)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        except Exception as e:
            # last-resort guard so bad input never crashes the whole app
            print(f"Something went wrong, please try again. ({e})")


if __name__ == "__main__":
    main_menu()
