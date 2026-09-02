"""Convert a temperature from Celsius to Fahrenheit and Kelvin."""

print("======================")
print("TEMPERATURE CONVERTER")
print("======================")

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("\nRESULTS")
print(f"Celsius: {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin: {kelvin:.2f} K")