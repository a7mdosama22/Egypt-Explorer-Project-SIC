from ..models import Maneger
from ..models.user import NormalUser
from ..utils.Validators import (
    validate_email,
    validate_password,
    validate_phone,
    validate_age,
    validate_national_id
)

from .user_menu import user_menu
from .admin_menu import admin_menu

def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("       SMART TOURISM & TRIP PLANNING")
        print("=" * 45)
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            login_menu()
        elif choice == "2":
            register_menu()
        elif choice == "3":
            print("\nThank you for using Smart Tourism System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


def login_menu():
    print("\n" + "=" * 45)
    print("                    LOGIN")
    print("=" * 45)

    email = input("Email: ").strip()
    password = input("Password: ").strip()

    users = Maneger.load_users()

    for user in users:
        if user.email == email:
            if user.password == password:
                print("\nLogin successful.")
                print(f"Welcome, {user.name}")

                if user.user_type == "admin":
                    admin_menu()
                else:
                    user_menu()
                return

            print("\nIncorrect password.")
            return

    print("\nThis email is not registered.")

def register_menu():
    print("\n" + "=" * 45)
    print("                  REGISTER")
    print("=" * 45)

    name = input("Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()

    phone = input("Phone (11 digits): ").strip()
    while not validate_phone(phone):
        print("Invalid phone number. Must be 11 digits, numbers only.")
        phone = input("Phone (11 digits): ").strip()

    email = input("Email (name@example.com): ").strip()
    while not validate_email(email):
        print("Invalid email format.")
        email = input("Email (name@example.com): ").strip()

    gender = input("Gender (Male/Female): ").strip()

    governorate = input("Governorate: ").strip()

    password = input("Password (min 6 characters): ").strip()
    while not validate_password(password):
        print("Password must be at least 6 characters.")
        password = input("Password (min 6 characters): ").strip()

    age = input("Age : ").strip()
    while not validate_age(age):
        print("Invalid age. Must be a number ")
        age = input("Age  ").strip()

    national_id = input("National ID (14 digits): ").strip()
    while not validate_national_id(national_id):
        print("Invalid National ID. Must be exactly 14 digits.")
        national_id = input("National ID (14 digits): ").strip()

    users = Maneger.load_users()
    for user in users:
        if user.email == email:
            print("\nThis email is already registered.")
            return
        if user.national_id == national_id:
            print("\nThis National ID is already registered.")
            return

    new_user = NormalUser(
        name,
        phone,
        email,
        gender,
        governorate,
        password,
        int(age),
        national_id
    )

    users.append(new_user)
    Maneger.save_users(users)

    print("\nAccount created successfully!")
    input("Press Enter to continue...")