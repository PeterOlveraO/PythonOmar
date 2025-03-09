import numpy as np

#Creacion array desde una lista

lista = [1,2,3,4,5]

array = np.array(lista)
print(array)

#Crear arreglos automaticamente
"""a = np.zeros(5)
b = np.ones(5)
c = np.arange(1,10)
d = np.linspace(0,1,5)

print(a)
print(b)
print(c)
print(d)"""

#Operaciones matematicas
print("Operaciones matematicas: ")
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

print(x + y)
print(x * y)
print(x ** 2)
print(np.sqrt(x))

#Indeccion y sligin
print("Ejericicio:")
a = np.array([10,20,30,40,50])
#Imprimir
print(a)
#Primer elemento
print(a[0])
#Ultimo
print(a[-1])
#Del 1 al 4
print(a[1:4])
#Primeros 3
print(a[:3])
#Cada 2
print(a[::2])

#Promedio y desviacion estandar
print("Promedio y desviacion estandar: ")

datos = np.random.randint(1,100, size = 10)
print(datos)

Promedio = np.mean(datos)
DE = np.std(datos)
print(Promedio)
print(DE)
print(np.max(datos))
print(np.min(datos))






