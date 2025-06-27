# Reto: Registro de empleados y cálculo de salarios
# Se crear las listas y contadores requeridas
empleado = []
horaTrabajada = []
valorHora = []
sueldo = []
excelente = 0
bueno = 0
bajo = 0
suma_salario = 0

# Ingresar numero de empleados que desea agregar
trabajadores = int(input("Cantidad de empleados que desea agregar: "))

for i in range(trabajadores):
    print(f"Empleado {i + 1}")
    nombre = input("Ingrese nombre del empleado: ") # Ingresar nombre de empleado
    empleado.append(nombre)
    horas = float(input("Ingrese horas trabajadas: ")) # Ingresar horas trabajadas
    horaTrabajada.append(horas)
    valor = float(input("Ingrese valor por hora: ")) # Ingresar valor por hora
    valorHora.append(valor)

    salario = horas * valor # Calcular el salario del empleado
    sueldo.append(salario)

    if salario > 2000000: 
        excelente += 1
    elif salario >= 1000000:
        bueno += 1
    else:
        bajo += 1
    
    suma_salario += salario # Sumar los salarios


print()

print(f"Lista de Empleados {empleado}") # Imprime empleados registrados
print(f"Lista de Salarios {sueldo}\n") # Imprime salario de cada empleado
if excelente or bueno or bajo:
    print(f"Excelente: {excelente}")
    print(f"Bueno: {bueno}")
    print(f"Bajo: {bajo}\n")

promedio_salario = suma_salario / len(sueldo) # Calcular el promedio salarial   
print(f"Promedio de Salarios: {promedio_salario}\n") # Imprime el promedio salarial

sueldo_max = sueldo.index(max(sueldo)) # El index sirve para buscar la pocision de un dato en la lista
print(f"Empleado con mejor salario: {empleado[sueldo_max]} - {max(sueldo)}") # Imprime el mejor salario con nombre





