def admin_menu():
    while True:
        print("\n" + "=" * 45)
        print("                 ADMIN MENU")
        print("=" * 45)
        print("1. View Attractions")
        print("2. Add Attraction")
        print("3. Update Attraction")
        print("4. Remove Attraction")
        print("5. Update Ticket Price")
        print("6. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_attractions()

        elif choice == "2":
            add_attraction()

        elif choice == "3":
            update_attraction()

        elif choice == "4":
            remove_attraction()

        elif choice == "5":
            update_ticket_price()

        elif choice == "6":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def view_attractions():
    print("\n" + "=" * 45)
    print("             ALL ATTRACTIONS")
    print("=" * 45)

    print("\nAttractions will be loaded from attractions.json.")
    input("\nPress Enter to continue...")

def add_attraction():
    print("\n" + "=" * 45)
    print("              ADD ATTRACTION")
    print("=" * 45)

    name = input("Name: ").strip()
    governorate = input("Governorate: ").strip()
    ticket_price = input("Ticket Price: ").strip()
    rating = input("Rating: ").strip()
    visit_time = input("Estimated Visit Time: ").strip()
    category = input("Category: ").strip()

    print(f"\nAttraction '{name}' will be added.")
    input("Press Enter to continue...")

def update_attraction():
    print("\n" + "=" * 45)
    print("            UPDATE ATTRACTION")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()

    print(f"\nUpdating: {name}")
    print("Update functionality will be connected here.")
    input("\nPress Enter to continue...")

def remove_attraction():
    print("\n" + "=" * 45)
    print("            REMOVE ATTRACTION")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()

    print(f"\nAttraction '{name}' will be removed.")
    input("\nPress Enter to continue...")

def update_ticket_price():
    print("\n" + "=" * 45)
    print("           UPDATE TICKET PRICE")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()
    new_price = input("Enter new ticket price: ").strip()

    print(f"\nTicket price for '{name}' will be updated to {new_price}.")
    input("\nPress Enter to continue...")