#-----------------------------------------------------------------------------------------------
# Break = Detiene todo el bucle	
# Continue = Salta a la siguiente vuelta del bucle
#-----------------------------------------------------------------------------------------------

# EJEMPLOS BREAK:
# numero_secreto = 7

# while True:
#     intento = int(input("Adivina el número: "))
#     if intento == numero_secreto:
#         print("¡Correcto!")
#         break  # 🔴 se sale del bucle
#     print("Sigue intentando...")
#-----------------------------------------------------------------------------------------------

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
#-----------------------------------------------------------------------------------------------

# break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")
#-----------------------------------------------------------------------------------------------
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter:
#     print("El número más grande es", largest_number)
#     print(bool(counter))
# else:
#     print("No has ingresado ningún número.")
#     print(bool(counter))
#-----------------------------------------------------------------------------------------------

# EJEMPLOS CONTINUE:
# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")
#-----------------------------------------------------------------------------------------------
# Ejercicios:
# No 1:
# palabra = input("Ingresa la palabra: ")

# for letra in palabra:
#     if letra.upper() in "AEIOU": # 🔴 si la letra es una vocal
#         continue  # 🔴 salta las vocales
#     print(f"{letra}")  # Imprime las letras excepto las vocales
# print("\nFin del programa.") 
#-----------------------------------------------------------------------------------------------

# No 2:
# word_without_vowels = ""

# user_word = input("Ingrese palabra: ")

# for letter in user_word:
#     if letter.upper() in "AEIOU":
#         continue 
#     word_without_vowels += letter # Agrega la letra a la variable si no es una vocal

# print(word_without_vowels, end=" ")
#-----------------------------------------------------------------------------------------------
# No 3:
# bloques = int(input("Ingresa la cantidad de bloques: "))
# altura = 0
# capa = 1  # bloques necesarios para cada nueva capa

# while bloques >= capa: # Mientras haya suficientes bloques para la capa actual
#     bloques -= capa      # gastas los bloques en esta capa
#     altura += 1          # aumentamos la altura de la pirámide
#     capa += 1            # la próxima capa necesita un bloque más

# print("La altura de la pirámide es:", altura)
# #-----------------------------------------------------------------------------------------------
# No 4:
c0 = int(input("Ingresa un número natural (mayor que 0): "))

if c0 <= 0:
    print("El número debe ser un natural positivo mayor que cero.")
else:
    pasos = 0

    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        pasos += 1

    print(1)  # mostrar el último 1
    print("Total de pasos:", pasos)