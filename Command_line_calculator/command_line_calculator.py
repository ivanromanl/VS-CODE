"""Run a calculator with separate functions and exception handling."""


def show_menu(current_number):
    """Display the current number and available options."""
    print(f"\nCurrent number: {current_number}")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def is_valid_option(option):
    """Return whether the option belongs to the menu."""
    return option in ("1", "2", "3", "4", "5", "6")


def get_number():
    """Read a number from the user."""
    return float(input("Enter a number: "))


def calculate(current_number, number, option):
    """Return the result of the selected arithmetic operation."""
    if option == "1":
        return current_number + number
    if option == "2":
        return current_number - number
    if option == "3":
        return current_number * number
    if option == "4":
        return current_number / number

    raise ValueError("Invalid arithmetic option.")


def run_calculator():
    """Coordinate the calculator's input, operations, and menu loop."""
    current_number = 0.0

    while True:
        show_menu(current_number)
        option = input("Choose an option: ").strip()

        if not is_valid_option(option):
            print("Invalid option. Choose a number from 1 to 6.")
            continue

        if option == "6":
            print("Goodbye!")
            break

        if option == "5":
            current_number = 0.0
            print("Result cleared.")
            continue

        try:
            number = get_number()
        except ValueError:
            print("Invalid number. Enter a number such as 5 or 2.5.")
            continue

        try:
            current_number = calculate(current_number, number, option)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {current_number}")


if __name__ == "__main__":
    run_calculator()