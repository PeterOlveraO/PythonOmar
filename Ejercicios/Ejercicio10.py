#Numeros y estadisticas
contador = 0
numeros = []
for i in range(10):
    n = int(input("Ingresa un numero: "))
    numeros.append(n)

print(f"La suma de los numeros es: {sum(numeros)}")
print(f"El promedio de los numeros es: {sum(numeros) / 10}")
print(f"El numero mayor es: {max(numeros)}")
print(f"El numero menor es: {min(numeros)}")
