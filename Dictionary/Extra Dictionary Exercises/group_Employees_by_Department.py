"""Grupo employess by department."""

employees = [
    {"name": "Carlos", "email": "carlos@empresas.com", "department": "sales"},
    {"name": "Ana", "email": "ana@empresas.com", "department": "IT"},
    {"name": "Luis", "email": "luis@empresas.com", "department": "sales"},
    {"name": "Sofia", "email": "Sofia@empresas.com", "department": "IT"},

]

employees_by_department = {}

for employee in employees:
    department = employee["department"]

    if department not in employees_by_department:
        employees_by_department[department] =[]

    employees_by_department[department].append(employee)

print(employees_by_department)
