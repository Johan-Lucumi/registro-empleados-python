# Asignacion variable y declalar
edad = 21
cantidadDinero = 1500.0
nombreCliente = "Juan Esteban"
print(nombreCliente, edad, cantidadDinero)
print(nombreCliente)

# Combinar texto con operador +
print()
version = "3.13.3"
print("Version de Python: " + version)

# Asignar valor nuevo
print()
num = 2
print(num)
num = num + 2
print(num)

# Resolviendo problema matematicos
print()
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)


print()
Juan = 3
Maria = 5
Adan = 6
print(Juan, Maria, Adan)
total_apples = Juan + Maria + Adan
print(total_apples)

# Operadores abreviados
print()
x = 5
sheep = 10

x = x * 2        # x ahora vale 10
sheep = sheep + 1  # sheep ahora vale 11

x *= 2           # x ahora vale 20
sheep += 1       # sheep ahora vale 12

print(x)      # Muestra: 20
print(sheep)  # Muestra: 12

# forma larga: i = i + 2 * j, forma abreviada: i += 2 * j
# forma larga: var = var / 2, forma abreviada: var /= 2
# forma larga: rem = rem % 10, forma abreviada: rem %= 10
# forma larga: j = j - (i + var + rem), forma abreviada: j -= (i + var + rem)
# forma larga: x = x ** 2, forma abreviada: x **= 2

# Convertidor simple
print()
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# Operadores y expresiones
print()
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
