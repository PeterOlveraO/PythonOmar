import csv

with open ("Archivos/iris.csv","r") as archivo_entrada:
    lector = csv.reader(archivo_entrada)
    encabezado = next(lector)
    suma = 0
    cont = 0

    for fila in lector:
            cont+=1
            suma += float(fila[1])

print(f"El promedio es de: {suma/cont}")


