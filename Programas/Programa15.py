import csv


with open ("Archivos/iris.csv","r") as archivo_entrada:
    lector = csv.reader(archivo_entrada)
    encabezado = next(lector)

    filas_sentosa = []

    for fila in lector:
        if fila[-1] == "Iris-setosa":
            filas_sentosa.append(fila)

with open ("Archivos/iris.csv","w", newline ="") as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(encabezado)
    escritor.writerows(filas_sentosa)

print(f"Se agregaron {len(filas_sentosa)} filas en 'iris_sentoa'.csv")