lista = ["Pedro","Alberto","Olvera","Ochoa"]
for i in range(1,5):
    try:
        print(lista[i])
    except IndexError:
        print(f"El indice ingresado esta fuera de la lista.")