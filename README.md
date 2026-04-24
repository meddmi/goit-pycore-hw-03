# Python Core Utilities

This repository contains a set of utility functions and a simple CLI interface for practicing core Python concepts, including:

- Working with dates
- Generating random values
- String normalization
- Basic data processing

---

## Project Structure
```
.
├── .gitignore
├── main.py
├── pycore_hw_03.py
└── README.md
```
---

## Features

### 1. `get_days_from_today(date)`
Calculates the number of days between a given date and today.

- Input: string in format `YYYY-MM-DD`
- Output: integer (negative if date is in the future)
- Returns None if the input format is invalid.

---

### 2. `get_numbers_ticket(min, max, quantity)`
Generates a sorted list of unique random numbers within a given range.

- Ensures:
  - numbers are unique
  - result is sorted
- Returns empty list if input is invalid

---

### 3. `normalize_phone(phone_number)`
Normalizes phone numbers to Ukrainian international format.

- Removes all non-digit characters
- Ensures format: `+380XXXXXXXXX`

---

### 4. `get_upcoming_birthdays(users)`
Finds users with birthdays in the next 7 days.

- Shifts weekend birthdays to Monday
- Input format:
  ```
  {"name": "John", "birthday": "YYYY.MM.DD"}
  ```
- Output format:
  ```
  {"name": "John", "congratulation_date": "YYYY.MM.DD"}
  ```

---

## CLI Interface

The `main.py` script provides an interactive command-line interface
to test all available functions using either predefined test cases
or manual input.

---

## How to Run

1. Run the main script
  ```
  python main.py
  ```

2. Use the interactive menu

You will see:
  ```
  1 - get_days_from_today
  2 - get_numbers_ticket
  3 - normalize_phone
  4 - get_upcoming_birthdays
  0 - Exit
  ```

3. Choose mode

After selecting a function:
  ```
  1 - predefined tests
  2 - manual input
  ```

---

## Input Examples

1. get_days_from_today
  ```
  2026-04-16
  ```

2. get_numbers_ticket
  ```
  10;100;6
  ```

3. normalize_phone
  ```
  +38(050)123-32-34
  ```

4. get_upcoming_birthdays
  ```
  John,1990.01.23;Jane,1990.01.27
  ```

---

## Requirements

- Python 3.10+
