print("===================")
print(" SUMA  DE  NUMERO  ")
print("===================")

numero = int(input("Ingrese un numero"))

suma = 0

for contador in range(1, numero +1):
    suma = suma + contador

print("El resultado de la suma es:", suma)