"""Display the multiplication table for a number from 1 to 10."""

print("======================")
print("MULTIPLICATION TABLE")
print("======================")

number = int(input("Enter a number from 1 to 10: "))

if 1 <= number <= 10:
    print(f"\nMultiplication table for {number}")

    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
else:
    print("Error: You must enter a number from 1 to 10.")