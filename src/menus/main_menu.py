from menus.user_menu import user_menu
from menus.admin_menu import admin_menu

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

    # Temporary admin login
    if email == "admin@gmail.com" and password == "admin123":
        print("\nLogin successful. Welcome Admin!")
        admin_menu()
    else:
        # Temporary normal user flow
        print("\nLogin successful. Welcome User!")
        user_menu()

def register_menu():
    print("\n" + "=" * 45)
    print("                  REGISTER")
    print("=" * 45)

    print("\nRegistration form:")

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    gender = input("Gender: ").strip()
    governorate = input("Governorate: ").strip()
    password = input("Password: ").strip()
    age = input("Age: ").strip()
    national_id = input("National ID: ").strip()

    print("\nRegistration completed successfully!")
    print(f"Welcome, {name}!")
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()