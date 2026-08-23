print("=== SUMAS ENTRE DISTINTOS TIPOS DE DATOS ===")

# 1 string + string
print("\n1. string + string")
print("Resultado:", "hola" + "mundo")

# 2. string + int
print("\n2. string + int")
try:
    print("Resultados:" "Hola" + "mundo")
except TypeError as error:
    print("Error:", error)

# 3. int + string
print("\n3. int + string")
try:
    print("Resultado:", 18 + "años")
except TypeError as error:
    print("Error:", error)

# 4. list + list
print("\n4. list + list")
print("Resultado:", [1, 2] + [3,4])

# 5. string + list
print("\n5. string + list")
try:
    print("Resultado:", "Numeros: " + [1,2,3])
except TypeError as error:
    print("Error:", error)

# 6. float + int
print("\n6. float + int")
print("Resultado:", True + False)
