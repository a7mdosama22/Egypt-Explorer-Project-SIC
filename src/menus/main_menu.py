from menus.user_menu import user_menu
from menus.admin_menu import admin_menu
from auth import UserManager

manager = UserManager()

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

    user, message = manager.login(email, password)
    print(f"\n{message}")

    if user is None:
        return

    if user.is_admin:
        print(f"Welcome Admin, {user.name}!")
        admin_menu()
    else:
        print(f"Welcome, {user.name}!")
        user_menu()

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

    success, message = manager.register(
        name, phone, email, gender, governorate, password, age, national_id
    )
    print(f"\n{message}")
    if success:
        input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()