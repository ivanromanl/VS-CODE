# Exercise 5: Finding the Highest Number Entered by the User

numbers = []

for index in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        highest_number = number

print("Numbers entered:", numbers)
print("The highest number was:", highest_number)