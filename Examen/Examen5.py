#Calcular el factorial de un numero
n = int(input("Ingresa un numero: "))
multi = 1
for x in range(1,n+1):
    multi *= x
print(multi)

