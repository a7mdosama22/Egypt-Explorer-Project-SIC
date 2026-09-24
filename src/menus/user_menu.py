from menus.navigation import NavigationStack

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]

def user_menu():
    navigation = NavigationStack()

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
            my_trip()

        elif choice == "4":
            trip_summary()

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

        # Temporary data
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

    print("\n" + "=" * 45)
    print(f"          {category.upper()} ATTRACTIONS")
    print("=" * 45)

    print("\nAttractions will be loaded from attractions.json.")

    print("\n1. Open Attraction Details")
    print("2. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        attraction_details(navigation)
    elif choice == "2":
        navigation.back()

def attraction_details(navigation):
    navigation.push("Attraction Details")

    print("\n" + "=" * 45)
    print("            ATTRACTION DETAILS")
    print("=" * 45)

    print("\nName: [Attraction Name]")
    print("Governorate: [Governorate]")
    print("Ticket Price: [Price]")
    print("Rating: [Rating]")
    print("Estimated Visit Time: [Time]")

    print("\n1. Add to My Trip")
    print("2. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        print("\nAttraction added to My Trip!")
        input("Press Enter to continue...")
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

def my_trip():
    print("\n" + "=" * 45)
    print("                   MY TRIP")
    print("=" * 45)

    print("\nNo attractions selected yet.")
    print("\n1. Remove Attraction")
    print("2. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        print("\nRemove functionality will be connected here.")

def trip_summary():
    print("\n" + "=" * 45)
    print("                TRIP SUMMARY")
    print("=" * 45)

    print("\nSelected Attractions: [Will be loaded]")
    print("Tickets Cost: [Calculated]")
    print("Transportation Cost: [Calculated]")
    print("Total Trip Cost: [Calculated]")
    input("\nPress Enter to go back...")