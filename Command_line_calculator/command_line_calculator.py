"""Run a command-line calculator with exception handling."""

def run_calculator():
    """Show a menu and update the current number."""
    current_number = 0.0

    while True:
        print(f"\nCurrent number: {current_number}")
        print("1. Add")
        print("2. subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. clear result")
        print("6. Exit")

        option = input("Choose an option: ").strip()

        if option == "6":
            print("Goodbye!")
            break
        
        if option == "5":
            current_number = 0.0
            print("Result cleared.")
            continue

        if option not in ("1", "2", "3", "4"):
            print("Invalid option. Choose a number from 1 to 6.")
            continue

        try:
            number = float(input("Enter a number: "))

            if option == "1":
                current_number += number
            elif option == "2":
                current_number -= number
            elif option == "3":
                current_number *= number
            elif option == "4":
                current_number /= number

        except ValueError:
            print("Invalid number. Enter a number such as 5 or 2.5.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {current_number}")

run_calculator()