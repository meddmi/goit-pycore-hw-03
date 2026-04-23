"""
This module contains functions from the third homework assignment of the Python Core course:
- Get days amount from today
- Create a set of unique random numbers within a given range
- Normalize phone numbers to a Ukrainian international format
- Calculate upcoming birthdays
"""

from datetime import datetime, date, timedelta
import random
import re


def get_days_from_today(target_date: str):
    """
    Calculate the number of days between the given date and today.
    :param target_date: Date in 'YYYY-MM-DD' format
    :return: Number of days (negative if date is in the future). 
    Returns None if input is invalid.
    """
    if not isinstance(target_date, str):
        print("Input must be a string in 'YYYY-MM-DD' format.")
        return None

    try:
        parsed_date = datetime.strptime(target_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Expected 'YYYY-MM-DD'.")
        return None

    today = datetime.today().date()
    delta = today - parsed_date
    days_from_today = delta.days
    print(f"{days_from_today} days from today to {target_date}")

    return days_from_today


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    Generate a sorted list of unique random numbers within a given range.
    :param min_value: Minimum value (>= 1)
    :param max_value: Maximum value (<= 1000)
    :param quantity: Amount of unique numbers to generate 
    (must be in range between min_value and max_value)
    :return: Sorted list of unique random numbers or empty list if invalid input
    """
    if min_value < 1:
        print(f"'min_value' should be not less then 1 -> {min_value}")
        return []

    if max_value > 1000:
        print(f"'max_value' should be not grater then 1000 -> {max_value}")
        return []

    if quantity > (max_value - min_value + 1) or quantity <= 0:
        print(f"'quantity' should be in the range \
              between 'min_value':{min_value} and 'max_value':{max_value}")
        return []

    all_numbers = range(min_value, max_value + 1)
    result = random.sample(all_numbers, quantity)
    sorted_result = sorted(result)
    print(f"Generating {quantity} unique numbers \
          between {min_value} and {max_value}: {sorted_result} ")

    return sorted_result


def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to Ukrainian international format. 
    Doesn't handle an incorrect phone length
    :param phone_number: Phone number as a string, which may contain various characters and formats
    :return: Normalized phone number or empty string if invalid input
    """
    if not isinstance(phone_number, str):
        return ""

    digits = re.sub(r"\D", "", phone_number)

    if digits.startswith("380"):
        return f"+{digits}"

    return f"+38{digits}"


def get_birthday_for_year(birthday: date, year: int) -> date:
    """
    Get the next birthday date for a given year, handling leap years.
    :param birthday: Original birthday date
    :param year: Year to calculate the next birthday
    :return: Next birthday date
    """
    try:
        return birthday.replace(year=year)
    except ValueError: #handle February 29
        return birthday.replace(year=year, day=28)


def shift_to_weekday(date_obj: date) -> date:
    """
    Shift weekend dates to next Monday.
    :param date_obj: Date to check
    :return: Original date if it's a weekday, or next Monday if it's a weekend
    """
    weekday = date_obj.weekday()

    if weekday >= 5:
        return date_obj + timedelta(days=7 - weekday)

    return date_obj


def get_upcoming_birthdays(users: list) -> list:
    """
    Find users with birthdays in the next 7 days, shifting weekend birthdays to Monday.
    :param users: list of dictionaries with 'name' and 'birthday' keys,
    where 'birthday' is in 'YYYY.MM.DD' format
    :return: list of dictionaries with 'name' and 'congratulation_date' keys 
    for users with birthdays in the next 7 days
    """
    today = datetime.today().date()
    results = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, ValueError):
            continue

        next_birthday = get_birthday_for_year(birthday, today.year)

        if next_birthday < today:
            next_birthday = get_birthday_for_year(birthday, today.year + 1)

        days_difference = (next_birthday - today).days

        if 0 <= days_difference <= 7:
            celebration_day = shift_to_weekday(next_birthday)
            user_to_congratulate = {
                "name": user.get("name", "Unknown"), 
                "congratulation_date": celebration_day.strftime("%Y.%m.%d")
                }
            results.append(user_to_congratulate)

    return results
