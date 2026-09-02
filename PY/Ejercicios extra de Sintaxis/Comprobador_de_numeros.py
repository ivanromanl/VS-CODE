"""Check whether a number or the total sum equals 30."""

print("======================")
print("NUMBER CHECKER")
print("======================")

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

total_sum = number_1 + number_2 + number_3

if number_1 == 30 or number_2 == 30 or number_3 == 30 or total_sum == 30:
    print("Correct")
else:
    print("Incorrect")