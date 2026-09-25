from .navigation import NavigationStack
from ..models import Maneger
from ..models.trip import Trip

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]
trip = Trip()
def user_menu():
    navigation = NavigationStack()
    navigation.push("Home")

    while True:
        print("\n" + "=" * 45)
        print("                    HOME")
        print("=" * 45)
        print("1. Browse Categories")
        print("2. Search Attraction")
        print("3. My Trip")
        print("4. Trip Summary")
        print("5. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            browse_categories(navigation)

        elif choice == "2":
            search_attraction()

        elif choice == "3":
            my_trip(navigation)

        elif choice == "4":
            trip_summary(navigation)

        elif choice == "5":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def browse_categories(navigation):
    navigation.push("Categories")

    while True:
        print("\n" + "=" * 45)
        print("                 CATEGORIES")
        print("=" * 45)

        for i, category in enumerate(CATEGORIES, start=1):
            print(f"{i}. {category}")

        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            navigation.back()
            return

        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            category_page(category, navigation)
        else:
            print("\nInvalid choice. Please try again.")

def category_page(category, navigation):
    navigation.push(category)

    while True:
        print("\n" + "=" * 45)
        print(f"              {category.upper()}")
        print("=" * 45)

        
        print("\n1. View Attractions")
        print("2. Search by Name")
        print("3. Sort by Ticket Price")
        print("4. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_attractions(category, navigation)

        elif choice == "2":
            search_category(category)

        elif choice == "3":
            sort_category(category)

        elif choice == "4":
            navigation.back()
            return

        else:
            print("\nInvalid choice. Please try again.")

def show_attractions(category, navigation):
    navigation.push("Attractions")

    attractions = Maneger.load_attractions()
    filtered = [a for a in attractions if a.category == category]

    while True:
        print("\n" + "=" * 45)
        print(f"          {category.upper()} ATTRACTIONS")
        print("=" * 45)

        if not filtered:
            print("\nNo attractions in this category yet.")
        else:
            for i, a in enumerate(filtered, start=1):
                print(f"{i}. {a}")   

        print("\nEnter attraction number to view details, or 0 to go Back")
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            navigation.back()
            return

        if choice.isdigit() and 1 <= int(choice) <= len(filtered):
            selected = filtered[int(choice) - 1]
            attraction_details(selected, navigation)
        else:
            print("\nInvalid choice. Please try again.")

def attraction_details(attraction, navigation):
    navigation.push("Attraction Details")

    print("\n" + "=" * 45)
    print("            ATTRACTION DETAILS")
    print("=" * 45)

    print(f"\n{attraction.full_details()}")   

    print("\n1. Add to My Trip")
    print("2. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        added = trip.add_attraction(attraction)
        if added:
            print(f"\n'{attraction.name}' added to My Trip!")
        else:
            print(f"\n'{attraction.name}' is already in your trip.")
        input("Press Enter to continue...")
        navigation.back()
    elif choice == "2":
        navigation.back()

def search_attraction():
    print("\n" + "=" * 45)
    print("              SEARCH ATTRACTION")
    print("=" * 45)

    name = input("\nEnter attraction name: ").strip()

    print(f"\nSearching for: {name}")
    print("Binary Search will be connected here.")

def search_category(category):
    name = input("\nEnter attraction name: ").strip()

    print(f"\nSearching in {category}: {name}")
    print("Binary Search will be connected here.")

def sort_category(category):
    print("\n" + "=" * 45)
    print("              SORT ATTRACTIONS")
    print("=" * 45)
    print("1. Ticket Price - Ascending")
    print("2. Ticket Price - Descending")
    print("3. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        print("\nSorting by ticket price ascending...")
    elif choice == "2":
        print("\nSorting by ticket price descending...")
    elif choice != "3":
        print("\nInvalid choice.")

def my_trip(navigation):
    navigation.push("My Trip")

    while True:
        print("\n" + "=" * 45)
        print("                   MY TRIP")
        print("=" * 45)

        items = trip.view_trip()
        if not items:
            print("\nNo attractions selected yet.")
        else:
            for i, a in enumerate(items, start=1):
                print(f"{i}. {a}")

        print("\n1. Remove Attraction")
        print("2. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            if not items:
                print("\nYour trip is empty.")
                continue
            idx = input("Enter item number to remove: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(items):
                trip.remove_attraction(items[int(idx) - 1])
                print("\nRemoved successfully.")
            else:
                print("\nInvalid number.")
        elif choice == "2":
            navigation.back()
            return
        else:
            print("\nInvalid choice. Please try again.")
def trip_summary(navigation):
    navigation.push("Trip Summary")

    print("\n" + "=" * 45)
    print("                TRIP SUMMARY")
    print("=" * 45)

    summary = trip.get_summary()

    if not summary["attractions"]:
        print("\nYour trip is empty.")
    else:
        for a in summary["attractions"]:
            print(f"- {a.name} ({a.governorate}) — {a.ticket_price} EGP")

        print(f"\nTickets Cost: {summary['attractions_cost']} EGP")
        print(f"Transportation Cost: {summary['transportation_cost']} EGP")
        print(f"Total Trip Cost: {summary['total_cost']} EGP")

    input("\nPress Enter to go back")
    navigation.back()