print("======================")
print(" COMPOBADOR DE NUMEROS")
print("======================")

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))

suma = numero_1 + numero_2 + numero_3

if numero_1 == 30 or numero_2 == 30 or numero_3 == 30 or suma == 30:
    print("Correcto")
else:
    print("Incorrecto")