"""Validate a user's name and age with exception handling."""


def get_name():
    """Read a name and reject names made entirely of digits."""
    name = input("Enter your name: ").strip()

    if name.isdigit():
        raise ValueError("The name cannot be a number.")

    return name


def get_age():
    """Read the user's age as an integer."""
    return int(input("Enter your age: "))


def main():
    """Read user details and display a greeting or an error."""
    try:
        name = get_name()
    except ValueError as error:
        print(error)
        return

    try:
        age = get_age()
    except ValueError:
        print("Invalid number.")
        return

    print(f"Hello {name}, your age is {age}.")


if __name__ == "__main__":
    main()