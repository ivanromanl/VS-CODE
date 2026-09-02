"""Calculate the final price of a product after applying a discount."""

print("======================")
print("DISCOUNT CALCULATOR")
print("======================")

price = float(input("Enter the product price: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount

print(f"The final price is: ${final_price:.2f}")