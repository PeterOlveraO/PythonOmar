from pandas.core.dtypes.inference import is_number

try:
    numero = int(input(f"Introduuce un numero: "))
    print(f"El numero ingresado es: {numero}")

except ValueError:
    print(f"Error: Debes ingresar un numero valido")

try:
    a = int(input(f"Ingresa un numero entero "))
    b = int(input(f"Ingresa un numero entero "))
    resultado = a/b
    print(f"Resultado {resultado}")
except ValueError:
    print(f"Error: Debes ingrresar un numero valido")
except ZeroDivisionError:
    print("Error: No puedes dividir entre 0")


try:
    archivo = open("archivo.txt","r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Finalizando operacion")


try:
    numero1 = int(input("Introduce un numero"))
except ValueError:
    print("Error: No ingresaste un numero.")
else:
    print(f"El doble del numero es {numero1 * 2}")

try:
    with open("datosaa.txt","w") as archivo:
        archivo.write("Este es un texto de prueba.\n")
    print("archivo escrito exitosamente")
except Exception as e:
    print(f"Ocurrio un error: {e}")

