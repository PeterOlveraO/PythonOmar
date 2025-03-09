#verificar numeros primos

x = int(input("Ingresa un numero: "))
cont = 0
for i in range(1,10):
    if x % i == 0:       cont+=1

if cont == 2:
    print(f"El numero {x} es numero primo")
else:
    print(f"El numero {x} no es numero primo")
