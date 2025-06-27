#-----------------------------------------------------------------------------------------------
# Metodo .lower()
palabra = input("Ingresa la palabra secreta: ")

while True:

    # El método .lower() convierte todo el texto ingresado a minúsculas.
    # Así se evita que el usuario tenga que escribir exactamente "chupacabra"
    # y se permite que lo escriba con mayúsculas o mezclado (por ejemplo: "Chupacabra", "CHUPACABRA", etc.).
    if palabra.lower() == "chupacabra":
        break
    else:
        print("Palabra incorrecta, intenta de nuevo.")
        palabra = input("Ingresa la palabra secreta: ")

print(f"{palabra} es la palabra secreta. ¡Felicidades!")
#-----------------------------------------------------------------------------------------------
# Metodo .upper()
palabra = input("Ingresa la palabra secreta: ")

while True:
    
    # El método .upper() convierte todo el texto ingresado a MAYÚSCULAS.
    # Así se evita que el usuario tenga que escribir exactamente "CHUPACABRA"
    # y se permite que lo escriba en cualquier forma (como "chupacabra", "Chupacabra", etc.).
    if palabra.upper() == "CHUPACABRA":
        break
    else:
        print("Palabra incorrecta, intenta de nuevo.")
        palabra = input("Ingresa la palabra secreta: ")

print(f"{palabra} es la palabra secreta. ¡Felicidades!")
#-----------------------------------------------------------------------------------------------
# Metodo .capitalize()
palabra = input("Ingresa la palabra secreta: ")

while True:
    # El método .capitalize() convierte solo la primera letra en mayúscula
    # y todas las demás en minúscula.
    # Así se permite aceptar la forma correcta tipo "Chupacabra" aunque el usuario la escriba mal (por ejemplo: "cHUPACABRA").
    if palabra.capitalize() == "Chupacabra":
        break
    else:
        print("Palabra incorrecta, intenta de nuevo.")
        palabra = input("Ingresa la palabra secreta: ")

print(f"{palabra} es la palabra secreta. ¡Felicidades!")
