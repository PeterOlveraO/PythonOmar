mi_lista = [10,20,30]
print(mi_lista[0])
mi_lista[1] = 25
print(mi_lista)

#remove(elemento)
numeros = [1,2,3,2]
numeros.remove(2)
print(numeros)

#pop(elemento) elimina y devuelve el elemento del indice dado si no se ingresa un indice toma el ultimo
numero1 = [1,2,3]
eliminado = numero1.pop()
print(eliminado)
print(numero1)

#index(elemnto)

#count(elemento) cuantas veces aparece el elemtno en la lista
listaa = [3,2,4,1,2]
print(listaa.count(2))

#sort() ORdena la lista de menor a mayor(modifa la lista original

numero2 = [0,4,1,2,4]
numero2.sort()
print(numero2)

#reverse() Invierte el orden de la lista
numero3 = [1,2,3]
numero3.reverse()
print(numero3)