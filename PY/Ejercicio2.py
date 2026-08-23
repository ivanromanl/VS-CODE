print("=== CLASIFICACION DE PERSONAS SEGUN SU EDAD ===")

first_name = input("ingrese su nombre: ")
last_name = input("ingrese su apellido: ")
age = int(input("ingrese su edad: "))

if age < 0:
    category = "edad no valida"
elif age <= 2:
    category = "bebe"
elif age<= 9:
    category = "niño"
elif age <= 12:
    category = "preadolescente"
elif age <= 17:
    category = "adolescente"
elif age <= 25:
    category = "adulto joven"
elif age <= 59:
    category = "adulto"
else:
    category = "adulto mayor"

print(f"{first_name} {last_name} tiene {age} años y pertenece a la categoria: {category}.")