# Find Numbers Above the Average
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

average = total / len(numbers)
above_average = []

for number in numbers:
    if number > average:
        above_average.append(number)

print(f"Average: {average}")
print(f"New list: {above_average}")