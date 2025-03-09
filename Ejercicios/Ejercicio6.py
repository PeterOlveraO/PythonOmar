
#Pedir al usuario a, b, c y calcular en x

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))


adentro = b**2 - 4 * a * c
afuera = -b + adentro
divi = afuera / 2*a

adentro1 = b**2 - 4 * a * c
afuera1 = -b - adentro1
divi1 = afuera1 / 2*a

print(divi)
print(divi1)


