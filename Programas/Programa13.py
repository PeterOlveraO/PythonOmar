Archivo = open("Archivos/datos.txt", "r")
contenido = Archivo.read()
print(contenido)
Archivo.close()

with open("Archivos/datos.txt","r")as archivo:
    contenido = archivo.read()
    print(contenido)

Archivos = open("Archivos/datos.txt","r")
Lineas = Archivos.readlines()
print(Lineas)
Archivos.close()

Archivos = open("Archivos/datos.txt","r")
Lineas = Archivos.readlines()
print(Lineas[-1])
Archivos.close()