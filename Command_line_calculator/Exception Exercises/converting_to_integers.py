"""Convert strings to integers and handle invalid values."""


def convert_to_integer(values):
    """Try to convert each string to an integer"""
    for value in values:
        try:
            number = int(value)
        except ValueError:
            print(f"Could not convert the element: {value}")
        else:
            print(f"{value} converted to {number}")



def main():
    """Prepare the list and run the conversions."""
    my_list = ["4", "hello", "10", "5.2"]
    print("Result:")
    convert_to_integer(my_list)


if __name__ == "__main__":
    main()
