"""Calculate the sum of all integers from 1 to a given number."""

print("======================")
print("NUMBER SUM")
print("======================")

number = int(input("Enter a number: "))

total_sum = 0

for counter in range(1, number + 1):
    total_sum = total_sum + counter

print(f"The sum is: {total_sum}")