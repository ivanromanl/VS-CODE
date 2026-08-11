print("=== Encontrar el numero mayor")

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print("El numero mayor es:", mayor)