from ..models.attraction import Attraction
from ..models import Maneger

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

    attractions = Maneger.load_attractions()
    if not attractions:
        print("\nNo attractions found.")
    else:
        for a in attractions:
            print(f"{a.id} {a}")   

    input("\nPress Enter to continue...")

def add_attraction():
    print("\n" + "=" * 45)
    print("              ADD ATTRACTION")
    print("=" * 45)

    name = input("Name: ").strip()
    governorate = input("Governorate: ").strip()
    category = input("Category: ").strip()
    visit_time = input("Estimated Visit Time: ").strip()

    ticket_price = float(input("Ticket Price: ").strip())
    rating = float(input("Rating: ").strip())


    attractions = Maneger.load_attractions()
    new_id = max((a.id for a in attractions), default=0) + 1

    new_attraction = Attraction(
        id=new_id, name=name, governorate=governorate,
        ticket_price=ticket_price, rating=rating,
        estimated_visit_time=visit_time, category=category,
    )
    attractions.append(new_attraction)
    Maneger.save_attractions(attractions)

    print(f"\nAttraction {name} added successfully.")
    input("Enter to continue")

def update_attraction():
    print("\n" + "=" * 45)
    print("            UPDATE ATTRACTION")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()
    attractions = Maneger.load_attractions()

    
    found = None
    for a in attractions:
        if a.name.lower() == name.lower():
            found = a
            break

    if not found:
        print(f"\nAttraction '{name}' not found.")
        input("Press Enter to continue")
        return

    print(f"\nUpdating: {found.name}")

    new_governorate = input(f"Governorate {found.governorate}: ").strip()
    new_category = input(f"Category {found.category}: ").strip()
    new_visit_time = input(f"Estimated Visit Time {found.estimated_visit_time}: ").strip()

    if new_governorate:
        found.governorate = new_governorate
    if new_category:
        found.category = new_category
    if new_visit_time:
        found.estimated_visit_time = new_visit_time

    Maneger.save_attractions(attractions)
    print(f"\n{found.name} updated successfully.")
    input("Press Enter to continue")
    
def remove_attraction():
    print("\n" + "=" * 45)
    print("            REMOVE ATTRACTION")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()
    attractions = Maneger.load_attractions()

    remaining = [a for a in attractions if a.name.lower() != name.lower()]

    if len(remaining) == len(attractions):
        print(f"\nAttraction {name} not found.")
    else:
        Maneger.save_attractions(remaining)
        print(f"\nAttraction {name} removed successfully.")

    input("Press Enter to continue")

def update_ticket_price():
    print("\n" + "=" * 45)
    print("           UPDATE TICKET PRICE")
    print("=" * 45)

    name = input("Enter attraction name: ").strip()
    attractions = Maneger.load_attractions()

    found = None
    for a in attractions:
        if a.name.lower() == name.lower():
            found = a
            break

    if not found:
        print(f"\nAttraction '{name} not found.")
        input("Press Enter to continue")
        return

    
    new_price = float(input("Enter new ticket price: ").strip())
    

    found.ticket_price = new_price
    Maneger.save_attractions(attractions)

    print(f"\nTicket price for {found.name} updated to {new_price}.")
    input("Press Enter to continue")