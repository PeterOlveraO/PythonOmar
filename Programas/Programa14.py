import csv

with open("Archivos/iris.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

with open("Archivos/iris.csv", "r") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector) #Saltar la primera fila
    datos = list(lector) #Guardar el resto en una lista

    print(f"Encabezado: {encabezado}")
    print(f"primeras filas: {datos[:5]}")

