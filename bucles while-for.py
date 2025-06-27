# #-----------------------------------------------------------------------------------------------
# # Almacena el actual número más grande aquí.
# largest_number = -999999999 
 
# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))
 
# # Imprime el número más grande.
# print("El número más grande es:", largest_number)

# #-----------------------------------------------------------------------------------------------
# # Un programa que lee una secuencia de números
# # y cuenta cuántos números son pares y cuántos son impares.
# # El programa termina cuando se ingresa un cero.
 
# odd_numbers = 0
# even_numbers = 0
 
# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

# #-----------------------------------------------------------------------------------------------
# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

# #-----------------------------------------------------------------------------------------------
# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un numero entero     |
# | y adivina que numero he        |
# | elegido para ti.               |
# +================================+
# """)

# numero = int(input("¿Cuál es el numero secreto?: "))

# while numero != secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     numero = int(input("¿Cuál es el numero secreto?: "))

# print("¡Bien hecho, muggle! Eres libre ahora.") # Esta línea se ejecutará cuando el bucle termine

# #-----------------------------------------------------------------------------------------------
# Bucle for (inicio, fin, incremento)
# for i in range(2, 8, 3):
#     print("El valor de i es", i)

# power = 1 # Inicia en 1
# for expo in range(16): # Toma valores de 0 a 15
#     print("2 a la potencia de", expo, "es", power) # Muestra cuánto es 2 a la potencia de expo
#     power *= 2 # Multiplica power por 2 para la siguiente vuelta


# #-----------------------------------------------------------------------------------------------
# import time
 
# for i in range(1, 6):
#     print(f"{i} Mississippi") 
#     time.sleep(1) # (segundos) detiene o pausa la ejecución del programa durante la cantidad de segundos que le indiques.
    
# print("¡Listos o no, ahí voy!")

# #-----------------------------------------------------------------------------------------------
# contrasena = input("Ingrese contraseña: ")

# while contrasena != "python123":
#     print("❌ Contraseña incorrecta.")
#     contrasena = input("Inténtalo de nuevo: ")

# print("✅ Ingresaste correctamente.")

# #-----------------------------------------------------------------------------------------------
# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
    
# print("¡Despegue!")

# #-----------------------------------------------------------------------------------------------
# print("Tabla de multiplicar")
# numero = int(input("Ingrese numero: "))

# for i in range (1, 11):
#     print(f"{numero} x {i} = {numero * i}")

#-----------------------------------------------------------------------------------------------
# for i in range(1,11):
#     if i % 3 != 0:
#         print(f"{i}")

x = 1

while x <= 10:
    if x % 2 == 0:
        x += 1  # ¡Importante! Evita bucle infinito
        continue
    print(x)
    x += 1  # Incrementa x para evitar bucle infinito

