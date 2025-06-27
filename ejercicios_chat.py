# print("Crear Cuenta")
# usuario = input("Ingrese usuario: ")
# contrasena = input("Ingrese contrasena: ")

# intentos = 3

# while intentos > 0:
#     print("Iniciar Sesion")
#     usuario_guardado = input("Ingrese usuario: ")
#     contrasena_guardada = input("Ingrese contrasena: ")

#     if usuario_guardado == usuario and contrasena_guardada == contrasena:
#         print("Bienvenido!!!")
#         break
#     else:
#         intentos -= 1
#         print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")

# if intentos == 0:
#     print("Has agotado tus intentos. Acceso denegado.")
        
# for i in range(1, 51):
#     if i % 2 == 0:
#         continue
#     print(i)  # Imprime los números impares del 1 al 50

excelentes = 0
aprobados = 0
reprobados = 0


rango = int(input("Ingrese cantidad de estudiantes a registrar: "))

for i in range(rango):
    nombre = input("Ingrese nombre: ")
    nota = float(input("Ingrese nota (0.0 a 5.0): "))

    if nota >= 4.5 and nota <= 5.0:
        excelentes += 1
    elif nota >= 3.0  and nota <= 4.4:
        aprobados += 1 
    elif nota >= 0.0 and nota <= 2.9:
        reprobados += 1
    else:
        print("Nota fuera del rango.Ingrese nota valida.")
        continue 

print("--- Resultados ---")
print(f"Excelentes: {excelentes}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")