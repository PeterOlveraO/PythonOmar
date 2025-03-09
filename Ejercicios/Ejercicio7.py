ini = int(input("Ingresa el numero de inicio:"))
fin = int(input("Ingresa el numero para parar:"))

for i in range(ini, fin):
    if i == 0:
        print(f"{i}, es cero")
    elif i%2==0:
        print(f"{i}, es par")
    else:
        print(f"{i} es impar")