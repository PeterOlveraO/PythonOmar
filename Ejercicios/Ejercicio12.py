#Filtrar numeros pares
pares = []
for i in range(10):
    x = int(input("Ingresa un numero: "))
    if x % 2 == 0:
        pares.append(x)
print(f"Los numeros pares son: {pares}")