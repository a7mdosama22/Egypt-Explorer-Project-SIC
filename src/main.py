"""
Main entry point — ties all modules together into the CLI flow:
Login/Register -> Home -> Categories -> Attractions -> Details ->
My Trip -> Final Summary. Also routes into the Admin Panel.

Owner: Member 4 (feel free to restructure once everyone's modules are ready —
this file is meant as a working skeleton, not the final word).
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.auth.auth import login, register
from src.utils.data_manager import load_attractions
from src.algorithms.search import binary_search_by_name
from src.algorithms.sort import merge_sort_by_price, sort_by_name
from src.navigation.navigator import Navigator
from src.trip.trip_manager import TripManager
from src.admin import admin_panel

nav = Navigator()
trip = TripManager()


def print_header(title):
    print(f"\n=== {title} ===")


def start_screen():
    while True:
        print_header("Egypt Explorer")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            user = login(email, password)
            if user:
                print(f"\nWelcome, {user.name}!")
                if user.is_admin():
                    admin_menu()
                else:
                    home_menu(user)
            else:
                print("Invalid email or password.")
        elif choice == "2":
            do_register()
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option, try again.")


def do_register():
    print_header("Register")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    gender = input("Gender: ").strip()
    governorate = input("Governorate: ").strip()
    password = input("Password: ").strip()
    age_input = input("Age: ").strip()
    national_id = input("National ID: ").strip()

    # TODO: proper validation (age is a number, email format, etc.)
    age = int(age_input) if age_input.isdigit() else 0

    user = register(name, phone, email, gender, governorate,
                     password, age, national_id)
    if user:
        print("Registration successful! Please log in.")
    else:
        print("This email is already registered.")


def home_menu(user):
    while True:
        print_header("Home")
        print("1. Browse Categories")
        print("2. View My Trip")
        print("3. Search by Name")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            categories_menu()
        elif choice == "2":
            view_trip_menu()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            nav.clear()
            trip.selected_attractions = []
            return
        else:
            print("Invalid option, try again.")


def categories_menu():
    attractions = load_attractions()
    categories = sorted({a.category for a in attractions})
    # NOTE: sorted() here is just for displaying the category NAMES list,
    # not the required "Sort by Price" algorithmic feature — that one
    # must use merge_sort_by_price() below.

    while True:
        print_header("Categories")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")
        print(f"{len(categories) + 1}. Back")

        choice = input("Choose an option: ").strip()
        if choice == str(len(categories) + 1):
            return
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category_page(categories[int(choice) - 1])
        else:
            print("Invalid option, try again.")


def category_page(category_name):
    attractions = [a for a in load_attractions() if a.category == category_name]

    while True:
        print_header(category_name)
        for i, a in enumerate(attractions, start=1):
            print(f"{i}. {a}")

        print("a. Sort by Price (Asc/Desc)")
        print("b. Search by Name")
        print("c. View Details")
        print("d. Back")

        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            order = input("Ascending or Descending? (a/d): ").strip().lower()
            attractions = merge_sort_by_price(attractions, ascending=(order != "d"))
        elif choice == "b":
            name = input("Enter name to search: ").strip()
            sorted_by_name = sort_by_name(attractions)
            found = binary_search_by_name(sorted_by_name, name)
            if found:
                print(f"\nFound: {found}")
            else:
                print("Attraction not found.")
        elif choice == "c":
            idx = input("Enter attraction number to view: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(attractions):
                attraction_details(attractions[int(idx) - 1])
            else:
                print("Invalid number.")
        elif choice == "d":
            return
        else:
            print("Invalid option, try again.")


def attraction_details(attraction):
    print_header(attraction.name)
    print(attraction.full_details())
    print("\n1. Add to My Trip")
    print("2. Back")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        trip.add_to_trip(attraction)
        print(f"'{attraction.name}' added to your trip.")
    # choice == "2" or anything else just returns


def search_menu():
    name = input("Enter attraction name to search: ").strip()
    all_attractions = load_attractions()
    sorted_by_name = sort_by_name(all_attractions)
    found = binary_search_by_name(sorted_by_name, name)
    if found:
        attraction_details(found)
    else:
        print("Attraction not found.")


def view_trip_menu():
    while True:
        print_header("My Trip")
        items = trip.view_trip()
        if not items:
            print("(empty)")
        for i, a in enumerate(items, start=1):
            print(f"{i}. {a}")

        print("a. Remove an item")
        print("b. View Final Summary")
        print("c. Back")
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            idx = input("Enter item number to remove: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(items):
                trip.remove_from_trip(items[int(idx) - 1])
        elif choice == "b":
            final_summary_page()
        elif choice == "c":
            return
        else:
            print("Invalid option, try again.")


def final_summary_page():
    print_header("Trip Summary")
    summary = trip.get_final_summary()

    if not summary["attractions"]:
        print("Your trip is empty.")
        return

    for a in summary["attractions"]:
        print(f"- {a.name} ({a.governorate}) — {a.ticket_price} EGP")

    print(f"\nAttractions Cost: {summary['attractions_cost']} EGP")
    print(f"Transportation Cost: {summary['transportation_cost']} EGP")
    print(f"Total Trip Cost: {summary['total_cost']} EGP")


def admin_menu():
    while True:
        print_header("Admin Panel")
        print("1. Add Attraction")
        print("2. Update Attraction")
        print("3. Delete Attraction")
        print("4. View All Attractions")
        print("5. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            governorate = input("Governorate: ").strip()
            price = float(input("Ticket Price: ").strip() or 0)
            rating = float(input("Rating: ").strip() or 0)
            visit_time = input("Estimated Visit Time: ").strip()
            category = input("Category: ").strip()
            admin_panel.add_attraction(name, governorate, price, rating,
                                        visit_time, category)
            print("Attraction added.")
        elif choice == "2":
            aid = int(input("Attraction ID to update: ").strip())
            field = input("Field to update (name/governorate/ticket_price/"
                           "rating/estimated_visit_time/category): ").strip()
            value = input("New value: ").strip()
            result = admin_panel.update_attraction(aid, **{field: value})
            print("Updated." if result else "Attraction not found.")
        elif choice == "3":
            aid = int(input("Attraction ID to delete: ").strip())
            result = admin_panel.delete_attraction(aid)
            print("Deleted." if result else "Attraction not found.")
        elif choice == "4":
            for a in load_attractions():
                print(f"[{a.id}] {a}")
        elif choice == "5":
            return
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    start_screen()
