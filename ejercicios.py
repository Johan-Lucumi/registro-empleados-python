# nombre = input("Ingresa tu nombre: ")
# contrasena = input("Ingresa tu contraseña: ")

# while nombre != "admin" or contrasena != "1234":
#     print("Nombre o Contrasena incorrecta. Inténtalo de nuevo.")
#     nombre = input("Ingresa tu nombre: ")  
#     contrasena = input("Ingresa tu contraseña: ")
# print("¡Acceso concedido!")


# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)


# nota = float(input("Ingrese su nota: "))

# if 4.5 <= nota <= 5.0:
#     print("Excelente") 
# elif 3.0 <= nota < 4.5:
#     print("Aprobado")
# elif 0.0 <= nota < 3.0:
#     print("Reprobado")
# else:
#     print("Nota inválida. Debe estar entre 0.0 y 5.0.")


# pasos = 0 

# numero = int(input("Ingrese un número: "))
# if numero <= 0:
#     print("El número debe ser mayor que 0.")
#     exit()

# while numero != 1:
#     print(numero)
#     if numero % 2 == 0:
#         numero = numero // 2
#     else:

#        numero = numero * 3 + 1
#     pasos += 1
# print(numero)
# print(f"Pasos: {pasos}")

# palara = input("Ingresa una palabra: ")

# for letra in palara:
#     if letra.upper() in "AEIOU": # 🔴 si la letra es una vocal
#         continue # 🔴 salta las vocales
#     print(f"{letra}", end=" ") # Imprime las letras excepto las vocales

print("Este es el cajero automatico de Python")
print("Crea una cuenta")
print("Por favor, ingresa los siguientes datos para crear tu cuenta.")
# Solicita al usuario su nombre de usuario y contraseña

usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")

print("Cuenta creada exitosamente.")
print("Bienvenido al cajero automático, " + usuario + "!")
print("Por favor, inicia sesión para continuar.")

intentos= 3
saldo = 1000000

while intentos > 0:
    usuario_ingresado = input("Ingresa tu nombre de usuario: ")
    contrasena_ingresada = input("Ingresa tu contraseña: ")

    if usuario_ingresado == usuario and contrasena_ingresada == contrasena:
        print("Inicio de sesión exitoso.")
        
        print("Bienvenido al Cajero")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print(f"Tu saldo actual es: {saldo} pesos.")
        elif opcion == "2":
            cantidad_retirar = int(input("¿Cuánto dinero deseas retirar? "))
            if cantidad_retirar <= saldo:
                saldo -= cantidad_retirar
                print(f"Has retirado {cantidad_retirar} pesos. Tu nuevo saldo es: {saldo} pesos.")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        elif opcion == "3":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
    else:
        intentos -= 1
        print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")

