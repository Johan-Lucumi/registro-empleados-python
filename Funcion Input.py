# Parametro = Es una variable que se define dentro de una función para recibir un valor cuando esa función se usa.

nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
print("Hola", nombre, ", su edad es", edad)

# Input/Entrada conversion de tipos (Texto a Numero)
print()
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
suma = numero_1 + numero_2
print("Resultado:", suma)

# Input/Entrada conversion de tipos (Texto a Numero)
print()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)


# Concatenacion (+)
print()
fnam = input("¿Me puedes dar tu nombre por favor?: ")
lnam = input("¿Me puedes dar tu apellido por favor?: ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

# Replicacion (*)
print()
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# Conversion de tipos (Numero a Texto)
print()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5)) # Para cambiar de (Tipo int a tipo cadena) se unsa str()

# Laboratorio 1 
print()
a = float(input("Ingrese numero: "))
b = float(input("Ingrese numero: "))

print("Suma: " + str(a + b))
print("Suma: " + str(a - b))
print("Suma: " + str(a * b))
print("Suma: " + str(a / b))

print("\n¡Eso es todo, amigos!")

# Laboratorio 2
print()
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

# Laboratorio 3
print()
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')


# Ejemplos
print()
x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
print(x * "5") # Muestra 2 veces 5

print()
x = input("Ingresa un número: ") # El usuario ingresa un 2
print(type(x)) # Muestra el tipo de dato (el input siempre mostrara 'str' independientemente que pongas un numero o no)
