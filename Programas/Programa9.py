contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador +=1

frutas = ["manzana","pera","durazno"]

for fruta in frutas:
    if fruta == "pera":
        continue
    print(fruta)
print("listo")

while True:
    numero = int(input("Introduce un numero (0 para salir): "))
    if numero == 0:
        break