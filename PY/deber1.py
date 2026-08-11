print("===CLASIFICACION DE PERSONAS SEGUN SU EDAD===")

nombre = input("ingrese su nombre:")
apellido = input("ingrese su apellido:")
edad = int(input("ingrese su edad:"))

if edad <0:
    categoria = "edad no valida"
elif edad <= 2:
    categoria = "bebe"
elif edad <= 9:
    categoria = "nino"
elif edad <= 12:
    categoria = "preadolescente"
elif edad <= 17:
    categoria = "adolescente"
elif edad <= 25:
    categoria = "adulto joven"
elif edad <= 59:
    categoria = "adulto mayor"

print(f"{nombre} {apellido} tiene {edad} anios y es {categoria}.")