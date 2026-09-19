# Find the Smallest Number in a list
numbers = [9, 4, 7, 1, 5]
smallest = numbers [0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"The smallest numbers is {smallest}.")