# Area de un rectangulo
base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))
#area = base * altura
#print("Area:", area)

# Promedio notas
print()
nota_1 = float(input("Ingrese primera nota: "))
nota_2 = float(input("Ingrese segunda nota: "))
nota_3 = float(input("Ingrese tercera nota: "))
promedio = (nota_1 + nota_2 + nota_3) / 3
print("Promedio:", promedio)

# Grados celcius a fahrenheit 
print()
grados_c = float(input("Ingrese temperatura en celcius: "))
conversor = (grados_c * 9 / 5) + 32
print("A temperatura fahrenheit es: ", conversor)

# Imprimir division entera y modulo 
print()
numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: "))
div_ent = numero_1 // numero_2
modulo = numero_1 % numero_2
print("Division Entera:", div_ent)
print("Modulo:", modulo)

# Mostrar raiz cuadrada 
print()
numero = float(input("Ingrese un numero: "))
raiz = numero ** 0.5 
print("Raíz cuadrada:", round(raiz, 2))  # Muestra solo 2 decimales round(número, número_de_decimales)


# Declarar variables y separarlas con un asterisco
print()
nombre = "Jhon"
edad = "21"
aptitud = "Jugar"
print(nombre, edad, aptitud, sep="*")

# Operadores
print()
numero_1 = float(input("Ingrese primer numero:"))
numero_2 = float(input("Ingrese segundo numero:"))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
exponente = numero_1 ** numero_2
print(suma, resta, multiplicacion, division, exponente, sep="\n")

# De decimal a entero
print()
numero = float(input("Ingrese numero:"))
conversor = int(numero) 
print(conversor)

