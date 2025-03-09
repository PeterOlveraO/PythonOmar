sum = 0
while True:
    n = int(input("Ingresa un numero (cuando dea 0 para): "))
    sum += n
    if n == 0:
        break
print(f"El resultado es: {sum}")