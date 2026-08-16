"""Programa para encontrar el mayor de tres numeros."""


numero1 = float(input("Escirbe el primer numero:"))
numero2 = float(input("Escribe el segundo numero: "))
numero3 = float(input("Escribir el tercer numero: "))

mayor = numero1

if numero2 > mayor:
    mayor = numero2

if numero3 > mayor:
    mayor = numero3

print("El numero mayor es:", mayor)