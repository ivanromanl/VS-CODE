print("======================")
print("CALCULADORA DE DESCUENTO")
print("======================")

precio = float(input("Ingrese el precio del producto: "))

if precio < 100:
    descuento = precio * 0.02
else:
    descuento = precio * 0.10

precio_final = precio - descuento

print("El precio final es:", precio_final)