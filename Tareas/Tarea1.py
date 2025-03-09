import random
cont = 0
ns = random.randrange(1, 21)
print(ns)

while True:
    
    n = int(input("Ingresa un numero: "))

    if n == ns:
        print("Felicidades, adivinaste el numero")
        break
    elif cont >= 4:
        print(f"Perdiste, el numero era:{ns}")
        break
    elif n < ns:
        print("El numero es mayor")
        cont+=1
    else:
        print("El numero es menor")
        cont+=1

