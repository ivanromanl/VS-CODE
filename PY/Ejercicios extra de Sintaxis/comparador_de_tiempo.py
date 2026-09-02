"""Compare a duration with ten minutes."""

print("============================")
print("TIME COMPARATOR")
print("============================")

seconds = int(input("Enter the time in seconds: "))

if seconds < 600:
    remaining_seconds = 600 - seconds
    print(f"{remaining_seconds} seconds remaining to reach 10 minutes.")
elif seconds > 600:
    print("The entered time is greater than 10 minutes.")
else:
    print("The entered time is exactly 10 minutes.")