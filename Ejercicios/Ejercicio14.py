#Leer datos e imprimir,
# numeros de lineas,
# veces que se repite la palabra python,
# Los numeros como lista, Suma y promedio de los numeros,
# Imprimir las primeras 3 lineas

#Leo datos e imprimos
Archivo = open("Archivos/datos.txt","r")
Contenido = Archivo.read()
print(Contenido)
Archivo.close()

#numeros de lineas
Archivo = open("Archivos/datos.txt","r")
Lineas = Archivo.readlines()

cont = 0
for i in Lineas:
    cont+=1

print(f"Hay {cont} lineas")
Archivo.close()

#veces que se repite la palabra python
contador = 0
py = 0
for x in Lineas:
    auxiliar = Lineas[contador].split(" ")
    for y in auxiliar:
        if y.strip() == "Python":
            py += 1
    contador += 1
print(f"La palabra Python se repite {py} veces")

#Los numeros como lista, Suma y promedio de los numeros



#Imprimir las primeras 3 lineas
contador = 0

for x in Lineas:
    if contador < 3:
        print(Lineas[contador])
    contador += 1

