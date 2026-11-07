"""Sum valid numeric values and handle invalid elements."""

def sum_values(values):
    """Covert each element to a float and print the total"""
    total = 0.0

    for value in values:
        try:
            number = float(value)
        except (ValueError, TypeError):
            print(f"Invalid element: {value}")
        else:
            total += number
            print(f"{number} added successfully")

    print(f"Total sum: {total}")

def main():
    """Prepare the list and sum its valid values."""
    my_list = ["10", "apple", "5.5", "3", "n/a"]
    sum_values(my_list)

if __name__ == "__main__":
    main()
