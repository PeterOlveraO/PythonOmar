

def RecopilarNumeros():
    numeros = []
    while True:
        try:
            num = int(input("Ingresa un numero: "))
        except ValueError as a:
            print(f"Error. Ingresa un valor entero: {a}")
        else:
            numeros.append(num)
            print(f"Numero agregado {num}")
            if len(numeros) >= 2:
                return numeros

def Calculo(lista):

    operacion = input("Elige el operador (+,-,*,/): ")

    if operacion == "+":
        resul = lista[0] + lista[1]
        return resul
    elif operacion == "-":
        resul = lista[0] - lista[1]
        return resul
    elif operacion == "*":
        resul = lista[0] * lista[1]
        return resul
    elif operacion == "/":
        try:
            resul = lista[0] / lista[1]
        except ZeroDivisionError as e:
            print(f"Error. No se puede dividir en 0. {e}")
        else:
            return resul
    else:
        print("Ingresa un operador valido.")
        Calculo(lista)

def Bucle():
    Desc = input("Deseas hacer otra operacion (s/n): ")
    if Desc == "s":
        return True
    elif Desc == "n":
        return False
    else:
        print("Ingresa una respuesta valida.")
        Bucle()

def main(resp):
    while resp:
        lista = RecopilarNumeros()
        resultado = Calculo(lista)
        print(f"El resultado es: {resultado}")
        resp = Bucle()




if __name__ == "__main__":
    resp = True
    main(resp)

