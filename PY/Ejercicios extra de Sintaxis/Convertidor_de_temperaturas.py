print("===================")
print(" CONVERTIDOR DE TEMPERATURA ")
print("===================")

celsius = float(input(" Ingrese la temperatura en Celsius "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("\nRESULTADOS")
print("Celsius:", celsius, "°C")
print("Fahrenheit:", fahrenheit, "°F")
print("Kelvin:", kelvin, "K")