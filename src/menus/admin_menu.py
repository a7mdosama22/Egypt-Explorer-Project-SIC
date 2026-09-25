from ..models.attraction import Attraction
from ..models import Maneger
from ..utils.Validators import validate_number

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]

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
    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()

    governorate = input("Governorate: ").strip()
    while not governorate:
        print("Governorate cannot be empty.")
        governorate = input("Governorate: ").strip()

    print(f"Category options: {', '.join(CATEGORIES)}")
    category = input("Category: ").strip()
    while category not in CATEGORIES:
        print(f"Invalid category. Must be one of: {', '.join(CATEGORIES)}")
        category = input("Category: ").strip()

    visit_time = input("Estimated Visit Time (e.g. 3 hours): ").strip()
    while not visit_time:
        print("Estimated Visit Time cannot be empty.")
        visit_time = input("Estimated Visit Time (e.g. 3 hours): ").strip()

    is_valid_price, ticket_price = validate_number(
        input("Ticket Price (number, 0 or more): ").strip(), min_value=0
    )
    while not is_valid_price:
        print("Invalid ticket price. Must be a number, 0 or more.")
        is_valid_price, ticket_price = validate_number(
            input("Ticket Price (number, 0 or more): ").strip(), min_value=0
        )

    is_valid_rating, rating = validate_number(
        input("Rating (0 to 5): ").strip(), min_value=0, max_value=5
    )
    while not is_valid_rating:
        print("Invalid rating. Must be a number between 0 and 5.")
        is_valid_rating, rating = validate_number(
            input("Rating (0 to 5): ").strip(), min_value=0, max_value=5
        )

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

    
    is_valid, new_price = validate_number(input("Enter new ticket price: ").strip(), min_value=0)
    if not is_valid:
        print("\nInvalid price. No changes made.")
        input("Press Enter to continue")
        return

    found.ticket_price = new_price
    Maneger.save_attractions(attractions)

    print(f"\nTicket price for {found.name} updated to {new_price}.")
    input("Press Enter to continue")