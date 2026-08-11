import random

print("=== ADIVINA EL NUMERO SECRETO ===")

numero_secreto = random.randint(1,10)
numero_usuario = 0

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Adivina el numero secreto del 1 al 10: "))

    if numero_usuario < numero_secreto:
        print("El numero secreto es mayor. Intenta nuevamente.")
    elif numero_usuario > numero_secreto:
        print("El numero secreto es menor. Intenta nuevamente.")
    else:
        print("¡Felicidades! Adivinaste el numero secreto" )