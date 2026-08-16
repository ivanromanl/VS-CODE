"""Programa para calcular las notas de un estudiante."""

total_de_notas = int(input("Ingrese la cantidad de notas: "))

contador_de_nota = 1

cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobada = 0

suma_de_notas_aprobadas = 0
suma_de_notas_desaprobadas = 0
suma_de_notas_total = 0

while contador_de_nota <= total_de_notas:
    nota_actual = float(
        input(f"Ingrese la nota numero {contador_de_nota}: ")
    )

    if nota_actual < 70:
        cantidad_de_notas_desaprobada += 1
        suma_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        suma_de_notas_aprobadas += nota_actual


        suma_de_notas_total += nota_actual
        contador_de_nota += 1

promedio_de_notas_total = suma_de_notas_total / total_de_notas

if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas = (
        suma_de_notas_aprobadas / cantidad_de_notas_aprobadas
    )
else:
    promedio_de_notas_aprobadas = 0

if  cantidad_de_notas_desaprobada > 0:
    promedio_de_notas_desaprobadas = (
        suma_de_notas_desaprobadas / cantidad_de_notas_desaprobada
    )
else:
    promedio_de_notas_desaprobadas = 0

print("\n----- RESULTADO -----")
print("Cantidad de notas aprobadas:", cantidad_de_notas_aprobadas)
print("Cantidad de notas desaprobadas:", cantidad_de_notas_desaprobada)
print("Promedio de todas las notas:", promedio_de_notas_total)
print("Promedio de las aprobadas:", promedio_de_notas_aprobadas)
print("Promedio de las desaprobadas:", promedio_de_notas_desaprobadas)