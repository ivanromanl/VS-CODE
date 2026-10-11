"""Calculate the sum of all numbers in a list"""


def add_numbers(numbers):
    """Return the sum of the numbers in the list."""
    total = 0
    for number in numbers:
        total += number
    return total

result = add_numbers([4, 6, 2, 29])
print(result)
