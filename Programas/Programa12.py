def saludar():
    print("Hola, bienvenidoa la clase de python")

saludar()

def saludo(nombre):
    print(f"Hola {nombre}")

saludo("pepe")

def saludox(nombre="Nely"):
    print(f"hola {nombre}")

saludox("d")

def retorno(a,b):
    return a + b

resultado = retorno(3,4)
print(resultado)


f = lambda x,y: x+y
print(f(3,4))

numeros = [1,2,3,4]

cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)

