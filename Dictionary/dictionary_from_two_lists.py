"""Create a dictionary from two lists."""
keys =["first_name", "last_name", "role"]
values = ["Alek", "Castillo", "sofware Engineer"]

person = dict(zip(keys, values))

print(person)
