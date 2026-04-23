""" 
This is the main module for the homework assignment. 
It provides a menu-driven interface to test the functions implemented in pycore_hw_03.py.
Users can choose to run predefined tests or input their own data
"""
import random
from datetime import datetime, timedelta
from pycore_hw_03 import (
    get_days_from_today,
    get_numbers_ticket,
    normalize_phone,
    get_upcoming_birthdays,
)

def print_menu() -> None:
    """Print the main menu options."""
    print("""
          \nSelect function:
          \n1 - get_days_from_today
          \n2 - get_numbers_ticket
          \n3 - normalize_phone
          \n4 - get_upcoming_birthdays
          \n0 - Exit
          """)


def run_predefined_tests(selected_method: int) -> None:
    """Run predefined tests for the selected option."""
    today = datetime.now().date()
    if selected_method == 1:
        today_string = (today).strftime("%Y-%m-%d")
        ten_days_forward = (today + timedelta(days=10)).strftime("%Y-%m-%d")
        seven_days_backward = (today - timedelta(days=7)).strftime("%Y-%m-%d")
        get_days_from_today(ten_days_forward)
        get_days_from_today(seven_days_backward)
        get_days_from_today(today_string)
        get_days_from_today(1)
        get_days_from_today("2026/04/16")

    elif selected_method == 2:
        random_min = random.randint(1, 500)
        random_max = random.randint(random_min + 1, 1000)
        random_quantity = random.randint(1, random_max - random_min + 1)
        get_numbers_ticket(random_min, random_max, random_quantity)

    elif selected_method == 3:
        raw_numbers = [
            "067\t123 4567",
            "(095) 234-5678\n",
            "+380 44 123 4567",
            "380501234567",
            "    +38(050)123-32-34",
            "     0503451234",
            "(050)8889900",
            "38050-111-22-22",
            "38050 111 22 11   ",
        ]

        sanitized = [normalize_phone(num) for num in raw_numbers]
        print(f"Normalized phone numbers: {sanitized}")

    elif selected_method == 4:
        weekday = today.weekday()

        if weekday <= 4:  # Mon–Fri
            days_until_saturday = 5 - weekday
            nearest_weekend = today + timedelta(days=days_until_saturday)
        else:

            nearest_weekend = today

        users = [
            {"name": "Jane Smith", "birthday": (today).strftime("%Y.%m.%d")},
            {"name": "Alina Naydysh", "birthday": (today + timedelta(days=3)).strftime("%Y.%m.%d")},
            {"name": "Fill Smith", "birthday": (today + timedelta(days=10)).strftime("%Y.%m.%d")},
            {"name": "John Doe", "birthday": (nearest_weekend).strftime("%Y.%m.%d")},
        ]

        print(f"Upcoming birthdays: {get_upcoming_birthdays(users)}")


def handle_user_input(selected_method: int) -> None:
    """Handle user input for the selected option."""
    try:
        if selected_method == 1:
            prompt = "Enter a date in \"YYYY-MM-DD\" format:"
            raw_input_data = input(prompt).strip()
            get_days_from_today(raw_input_data)

        elif selected_method == 2:
            prompt = "Enter min, max, and quantity separated by \";\" (semicolons):"
            raw_input_data = input(prompt).strip()
            parts = raw_input_data.split(";")
            min_val = int(parts[0])
            max_val = int(parts[1])
            quantity = int(parts[2])
            get_numbers_ticket(min_val, max_val, quantity)

        elif selected_method == 3:
            prompt = "Enter phone number:"
            raw_input_data = input(prompt).strip()
            normalized_phone = normalize_phone(raw_input_data)
            print(f"Normalized phone number: {normalized_phone}")

        elif selected_method == 4:
            prompt = (
                "Enter users as: name,birthday;name,birthday "
                "where birthday is in \"YYYY.MM.DD\" format "
                "(e.g., John Doe,1990.01.23;Jane Smith,1990.01.27):"
            )
            raw_input_data = input(prompt).strip()
            users_raw = raw_input_data.split(";")
            users = []
            for entry in users_raw:
                name, birthday = entry.split(",")
                users.append({
                    "name": name.strip(),
                    "birthday": birthday.strip()
                })

            days_from_today = get_upcoming_birthdays(users)
            print(f"Upcoming birthdays: {days_from_today}")

    except Exception as e:
        print(f"Error: {e}")


while True:
    print_menu()

    choice = input("Enter option: ").strip()

    if choice == "0":
        print("Exiting...")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid option.")
        continue

    option = int(choice)

    mode = input("Choose mode: 1 - predefined tests, 2 - manual input: ").strip()

    if mode == "1":
        run_predefined_tests(option)

    elif mode == "2":
        handle_user_input(option)
    else:
        print("Invalid mode.")
