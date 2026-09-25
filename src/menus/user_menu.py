from menus.navigation import NavigationStack
from models import Maneger
from models.trip import Trip
from algorithms.search import binary_search, search_by_governorate, search_by_min_rating
from algorithms.sort import merge_sort

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]

def user_menu():
    navigation = NavigationStack()
    navigation.push("Home")

    trip = Trip()

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
            browse_categories(navigation, trip)

        elif choice == "2":
            search_attraction(trip)

        elif choice == "3":
            my_trip(navigation, trip)

        elif choice == "4":
            trip_summary(navigation, trip)

        elif choice == "5":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")

def browse_categories(navigation, trip):
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
            category_page(category, navigation, trip)
        else:
            print("\nInvalid choice. Please try again.")

def category_page(category, navigation, trip):
    navigation.push(category)

    while True:
        print("\n" + "=" * 45)
        print(f"              {category.upper()}")
        print("=" * 45)

        print("\n1. View Attractions")
        print("2. Search by Name")
        print("3. Search by Governorate (Bonus)")
        print("4. Search by Minimum Rating (Bonus)")
        print("5. Sort")
        print("6. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_attractions(category, navigation, trip)

        elif choice == "2":
            search_category(category, trip)

        elif choice == "3":
            search_category_by_governorate(category, trip)

        elif choice == "4":
            search_category_by_rating(category, trip)

        elif choice == "5":
            sort_category(category)

        elif choice == "6":
            navigation.back()
            return

        else:
            print("\nInvalid choice. Please try again.")

def show_attractions(category, navigation, trip):
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
            attraction_details(selected, navigation, trip)
        else:
            print("\nInvalid choice. Please try again.")

def attraction_details(attraction, navigation, trip):
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

def search_attraction(trip):
    print("\n" + "=" * 45)
    print("              SEARCH ATTRACTION")
    print("=" * 45)

    name = input("\nEnter attraction name: ").strip()
    attractions = Maneger.load_attractions()

    if not attractions:
        print("\nNo attractions available.")
        input("Press Enter to continue...")
        return

    found = binary_search(attractions, name)

    if found:
        print("\nAttraction found!")
        print("-" * 45)
        print(found.full_details())

        print("\n1. Add to My Trip")
        print("2. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            if trip.add_attraction(found):
                print(f"\n'{found.name}' added to My Trip!")
            else:
                print(f"\n'{found.name}' is already in your trip.")

            input("Press Enter to continue...")

    else:
        print(f"\nAttraction '{name}' not found.")
        input("Press Enter to continue...")

def search_category(category, trip):
    print("\n" + "=" * 45)
    print(f"          SEARCH IN {category.upper()}")
    print("=" * 45)

    name = input("\nEnter attraction name: ").strip()
    attractions = Maneger.load_attractions()

    category_attractions = [
        a for a in attractions
        if a.category.lower() == category.lower()
    ]

    if not category_attractions:
        print("\nNo attractions in this category.")
        input("Press Enter to continue...")
        return

    found = binary_search(category_attractions, name)

    if found:
        print("\nAttraction found!")
        print("-" * 45)
        print(found.full_details())

        print("\n1. Add to My Trip")
        print("2. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            if trip.add_attraction(found):
                print(f"\n'{found.name}' added to My Trip!")
            else:
                print(f"\n'{found.name}' is already in your trip.")

            input("Press Enter to continue...")

    else:
        print(f"\nAttraction '{name}' not found in {category}.")
        input("Press Enter to continue...")


# Search by Governorate and by Minimum Rating.
def search_category_by_governorate(category, trip):
    print("\n" + "=" * 45)
    print(f"   SEARCH BY GOVERNORATE IN {category.upper()}")
    print("=" * 45)

    governorate = input("\nEnter governorate: ").strip()

    if not governorate:
        print("\nGovernorate cannot be empty.")
        input("Press Enter to continue...")
        return

    attractions = Maneger.load_attractions()
    category_attractions = [
        a for a in attractions
        if a.category.lower() == category.lower()
    ]

    if not category_attractions:
        print("\nNo attractions in this category.")
        input("Press Enter to continue...")
        return

    results = search_by_governorate(category_attractions, governorate)

    if not results:
        print(f"\nNo attractions found in governorate '{governorate}'.")
        input("Press Enter to continue...")
        return

    print(f"\nFound {len(results)} attraction(s) in '{governorate}':")
    print("-" * 45)
    for i, a in enumerate(results, start=1):
        print(f"{i}. {a}")

    print("\nEnter a number to add it to My Trip, or 0 to go back")
    choice = input("Enter your choice: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(results):
        selected = results[int(choice) - 1]
        if trip.add_attraction(selected):
            print(f"\n'{selected.name}' added to My Trip!")
        else:
            print(f"\n'{selected.name}' is already in your trip.")
        input("Press Enter to continue...")

def search_category_by_rating(category, trip):
    print("\n" + "=" * 45)
    print(f"  SEARCH BY MINIMUM RATING IN {category.upper()}")
    print("=" * 45)

    rating_input = input("\nEnter minimum rating (0-5): ").strip()

    try:
        min_rating = float(rating_input)
    except ValueError:
        print("\nRating must be a valid number.")
        input("Press Enter to continue...")
        return

    if not (0 <= min_rating <= 5):
        print("\nRating must be between 0 and 5.")
        input("Press Enter to continue...")
        return

    attractions = Maneger.load_attractions()
    category_attractions = [
        a for a in attractions
        if a.category.lower() == category.lower()
    ]

    if not category_attractions:
        print("\nNo attractions in this category.")
        input("Press Enter to continue...")
        return

    results = search_by_min_rating(category_attractions, min_rating)

    if not results:
        print(f"\nNo attractions with rating >= {min_rating}.")
        input("Press Enter to continue...")
        return

    # show highest rated first
    results = list(reversed(results))

    print(f"\nFound {len(results)} attraction(s) with rating >= {min_rating}:")
    print("-" * 45)
    for i, a in enumerate(results, start=1):
        print(f"{i}. {a}")

    print("\nEnter a number to add it to My Trip, or 0 to go back")
    choice = input("Enter your choice: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(results):
        selected = results[int(choice) - 1]
        if trip.add_attraction(selected):
            print(f"\n'{selected.name}' added to My Trip!")
        else:
            print(f"\n'{selected.name}' is already in your trip.")
        input("Press Enter to continue...")

def sort_category(category):
    print("\n" + "=" * 45)
    print(f"          SORT {category.upper()}")
    print("=" * 45)

    print("1. Ticket Price")
    print("2. Rating (Bonus)")
    print("3. Governorate (Bonus)")
    print("4. Back")

    attr_choice = input("\nSort by: ").strip()

    if attr_choice == "4":
        return

    sort_options = {
        "1": ("Ticket Price", lambda a: a.ticket_price),
        "2": ("Rating", lambda a: a.rating),
        "3": ("Governorate", lambda a: a.governorate.lower()),
    }

    if attr_choice not in sort_options:
        print("\nInvalid choice.")
        return

    label, key_func = sort_options[attr_choice]

    print("\n1. Ascending")
    print("2. Descending")
    print("3. Back")

    direction = input("\nEnter your choice: ").strip()

    if direction == "3":
        return

    if direction not in ["1", "2"]:
        print("\nInvalid choice.")
        return

    attractions = Maneger.load_attractions()

    category_attractions = [
        a for a in attractions
        if a.category.lower() == category.lower()
    ]

    if not category_attractions:
        print("\nNo attractions in this category.")
        input("Press Enter to continue...")
        return

    ascending = direction == "1"
    sorted_attractions = merge_sort(category_attractions, key=key_func, reverse=not ascending)

    print("\n" + "=" * 45)
    print(f"    SORTED BY {label.upper()} - {'ASCENDING' if ascending else 'DESCENDING'}")
    print("=" * 45)

    for i, attraction in enumerate(sorted_attractions, start=1):
        print(f"{i}. {attraction.name} - {attraction.governorate} - "
              f"{attraction.ticket_price} EGP - Rating: {attraction.rating}")

    input("\nPress Enter to continue...")

def my_trip(navigation, trip):
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

def trip_summary(navigation, trip):
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