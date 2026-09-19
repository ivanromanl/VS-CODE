#Count Occurrences in a list

user_input = input("Enter numbers separated by spaces: ")
numbers = []

for value in user_input.split():
    numbers.append(int(value))

target = int(input("Enter the number to search for: "))
count = 0

for number in numbers:
    if number == target:
        count += 1

print(f"The number {target} appears {count} time(s).")