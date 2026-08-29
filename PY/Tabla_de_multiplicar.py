print("====================")
print(" Tabla de multiplicar ")
print("====================")

numero = int(input("Ingrese un numero del 1 al 10: "))

if numero >= 1 and numero <= 10:
    print("\nTabla del", numero)

    for multiplicador in range(1, 13):
        resultado = numero * multiplicador 
        print(numero, "x", multiplicador, "=", resultado)

else:
    print("Error: debe ingresar un numero del 1 al 10")