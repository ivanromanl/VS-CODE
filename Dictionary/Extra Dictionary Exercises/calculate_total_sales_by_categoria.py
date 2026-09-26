products = [
    {"name": "Monitor", "category": "Electronics", "price": 200},
    {"name": "Keyboard", "category": "Electronics", "price": 50},
    {"name": "Chair", "category": "Furniture", "price": 120},
    {"name": "Table", "category": "Furniture", "price": 180},
    {"name": "Mouse", "category": "Electronics", "price": 25},
]

totals_by_category = {}

for product in products:
    category = product["category"]
    price = product["price"]

    if category not in totals_by_category:
        totals_by_category[category] = 0

    totals_by_category[category] += price

print(totals_by_category)
