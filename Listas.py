# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista con funcion len().

# del numbers[1] # del es una instruccion para eliminar elementos de una lista
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
# print(numbers[-1]) # Un elemento con un índice igual a -1 es el último en la lista.
# print(numbers[-2]) # Del mismo modo, el elemento con un índice igual a -2 es el anterior al último en la lista.


# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# numero = int(input("Ingrese un numero: "))
# hat_list[2] = numero

# del hat_list[-1]

# print("Longitud:", len(hat_list))

# print(hat_list)

# Agregando elementos a una lista: append() y insert()

# list.append(value) Agrega un elemento al final de la lista
# list.insert(location, value) Agrega un elemento en cualquier lugar de la lista

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)


# ###


# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)


# ###


# print(my_list)

# my_list = []  # Creando una lista vacía.
 
# for i in range(5):
#     my_list.insert(0, i + 1) # Cada número se inserta en la posición 0 
 
# print(my_list)

# ###

# my_list = [10, 1, 8, 3, 5]
 
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)
 
# beatles = []

# beatles.append("Jhon Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# print(beatles)

# for i in range(2):
#     beatles.append(input("Ingrese 2 miembros: "))

# print(beatles)

# del beatles[3]
# del beatles[-1  ]

# print(beatles)

# beatles.insert(0, "Ringo Starr")

# print(beatles)
# print("Los Fav", len(beatles))

# contrasena = input("Cree contrasena: ")

# while True:

#     intento = input("Ingrese contrasena: ")
#     if intento == contrasena:       
#         print("Contrasena correcta.")
#         break
#     else: 
#         print("Contrasena incorrecta.")


#########


# tareas = []

# print("Ingresa 5 tareas:")

# # Llenar la lista de tareas
# for i in range(5):
#     tarea = input(f"Ingrese tarea {i + 1}: ")
#     tareas.append(tarea)

# # Mostrar las tareas numeradas
# print("\nTus tareas:")
# for idx, tarea in enumerate(tareas, 1):
#     print(f"{idx}. {tarea}")

# # Eliminar tarea
# tarea_eliminar = input("\nEscribe exactamente el nombre de la tarea que deseas eliminar: ")

# if tarea_eliminar in tareas:
#     tareas.remove(tarea_eliminar)
#     print("\nTarea eliminada con éxito.")
# else:
#     print("\nEsa tarea no está en la lista.")

# # Mostrar lista actualizada
# print(f"\nTareas actualizadas: {tareas}")


#########


# numeros = []
# acumulada = []
# suma = 0

# for i in range(1, 11):
#     numeros.append(i)

# print(numeros)

# for j in numeros:
#     suma += j
#     acumulada.append(suma)

# print(acumulada)

#########



