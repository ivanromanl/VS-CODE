print("==============================")
print("     COMPARADOR DE TIEMPO")
print("==============================")

segundos = int(input("Ingrese el tiempo en segundos: "))

if segundos < 600:
    segundos_faltantes = 600 - segundos
    print("Faltan", segundos_faltantes, "segundos para llegar a 10 minutos.")

elif segundos > 600:
    print("Mayor")

else:
    print("Igual")