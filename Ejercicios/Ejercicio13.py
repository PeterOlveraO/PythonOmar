#Palabra magica

palabras = input("Ingresa palabras separadas por espacios")
separadas = palabras.split(" ")
print(separadas)
print(f"La palabra mas larga es: {max(separadas, key=len)}")