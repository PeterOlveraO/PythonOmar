#Sumar todos los digitos de un numero
num = str(input("Ingrese un numero: "))
sum = 0
for x in num:
    a = int(x)
    sum += a

print(f"La suma es de: {sum}")