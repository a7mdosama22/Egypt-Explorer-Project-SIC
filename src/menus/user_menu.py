from .navigation import NavigationStack
from ..models import Maneger
from ..models.trip import Trip
from ..algorithms.search import binary_search, search_by_governorate, search_by_min_rating
from ..algorithms.sort import merge_sort_by_price
from ..utils.Validators import validate_number

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
        print("4. Search by Governorate")
        print("5. Search by Minimum Rating")
        print("6. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_attractions(category, navigation)
        elif choice == "2":
            search_category(category)
        elif choice == "3":
            sort_category(category)
        elif choice == "4":
            search_category_by_governorate(category)
        elif choice == "5":
            search_category_by_rating(category)
        elif choice == "6":
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
    attractions = Maneger.load_attractions()

    result = binary_search(attractions, name)

    if result:
        print(f"\nFound: {result}")
        print(result.full_details())
    else:
        print(f"\nNo attraction found with the name '{name}'.")

    input("\nPress Enter to continue...")

def search_category(category):
    print("\n" + "=" * 45)
    print(f"         SEARCH IN {category.upper()}")
    print("=" * 45)

    name = input("\nEnter attraction name: ").strip()
    attractions = Maneger.load_attractions()
    filtered = [a for a in attractions if a.category == category]

    result = binary_search(filtered, name)

    if result:
        print(f"\nFound: {result}")
        print(result.full_details())
    else:
        print(f"\nNo attraction found with the name '{name}' in {category}.")

    input("\nPress Enter to continue...")

def sort_category(category):
    print("\n" + "=" * 45)
    print("              SORT ATTRACTIONS")
    print("=" * 45)
    print("1. Ticket Price - Ascending")
    print("2. Ticket Price - Descending")
    print("3. Back")

    choice = input("\nEnter your choice: ").strip()

    attractions = Maneger.load_attractions()
    filtered = [a for a in attractions if a.category == category]

    if choice == "1":
        sorted_attractions = merge_sort_by_price(filtered, ascending=True)
    elif choice == "2":
        sorted_attractions = merge_sort_by_price(filtered, ascending=False)
    elif choice == "3":
        return
    else:
        print("\nInvalid choice.")
        return

    print(f"\n=== {category.upper()} (sorted by price) ===")
    for i, a in enumerate(sorted_attractions, start=1):
        print(f"{i}. {a}")

    input("\nPress Enter to continue...")

def search_category_by_governorate(category):
    print("\n" + "=" * 45)
    print("           SEARCH BY GOVERNORATE")
    print("=" * 45)

    governorate = input("\nEnter governorate: ").strip()
    attractions = Maneger.load_attractions()
    filtered = [a for a in attractions if a.category == category]

    results = search_by_governorate(filtered, governorate)

    if not results:
        print(f"\nNo attractions found in '{governorate}' within {category}.")
    else:
        print(f"\n=== Attractions in {governorate} ({category}) ===")
        for i, a in enumerate(results, start=1):
            print(f"{i}. {a}")

    input("\nPress Enter to continue...")


def search_category_by_rating(category):
    print("\n" + "=" * 45)
    print("          SEARCH BY MINIMUM RATING")
    print("=" * 45)

    is_valid, min_rating = validate_number(
        input("\nEnter minimum rating (0 to 5): ").strip(), min_value=0, max_value=5
    )
    while not is_valid:
        print("Invalid rating. Must be a number between 0 and 5.")
        is_valid, min_rating = validate_number(
            input("Enter minimum rating (0 to 5): ").strip(), min_value=0, max_value=5
        )

    attractions = Maneger.load_attractions()
    filtered = [a for a in attractions if a.category == category]

    results = search_by_min_rating(filtered, min_rating)

    if not results:
        print(f"\nNo attractions in {category} with rating >= {min_rating}.")
    else:
        print(f"\n=== {category} with rating >= {min_rating} ===")
        for i, a in enumerate(reversed(results), start=1):
            print(f"{i}. {a}")

    input("\nPress Enter to continue...")

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