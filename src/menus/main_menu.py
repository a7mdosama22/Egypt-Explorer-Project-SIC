from models import Maneger
from models.user import NormalUser
from utils.Validators import (
    validate_email,
    validate_password,
    validate_national_id,
    validate_phone,
    validate_age
)

from menus.user_menu import user_menu
from menus.admin_menu import admin_menu


ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"


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

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        print("\nLogin successful.")
        print("Welcome Admin!")
        admin_menu()
        return

    users = Maneger.load_users()

    for user in users:
        if user.email == email:
            if user.password == password:
                print("\nLogin successful.")
                print(f"Welcome, {user.name}!")
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
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    gender = input("Gender: ").strip()
    governorate = input("Governorate: ").strip()
    password = input("Password: ").strip()
    age = input("Age: ").strip()
    national_id = input("National ID: ").strip()

    if not name:
        print("\nName cannot be empty.")
        return

    if not validate_phone(phone):
        print("\nInvalid phone number.")
        return

    if not validate_email(email):
        print("\nInvalid email format.")
        return

    if not validate_password(password):
        print("\nPassword must be at least 6 characters.")
        return

    if not validate_national_id(national_id):
        print("\nNational ID must be exactly 14 digits.")
        return

    if not validate_age(age):
        print("\nInvalid age.")
        return

    users = Maneger.load_users()

    for user in users:
        if user.email == email:
            print("\nThis email is already registered.")
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


if __name__ == "__main__":
    main_menu()
