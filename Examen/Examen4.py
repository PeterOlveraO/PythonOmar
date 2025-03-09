#Ingresar una frase y contar cuantas vocales tiene

frase = input("Ingresa la frase: ")
cont = 0
for x in frase:
    if x == "a":
        cont+= 1
    elif x == "e":
        cont += 1
    elif x == "i":
        cont += 1
    elif x == "o":
        cont += 1
    elif x == "u":
        cont += 1

print(f"La cantidad de vocales que tiene es de: {cont}")
