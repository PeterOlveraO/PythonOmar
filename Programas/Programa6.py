Cadena = "Hola mundo"

print(Cadena[0])
print(Cadena[-1])
#upper() Convierte todo en mayusculas
#lowe() Convierte todo en minusculas
#capitalize() Primera letra en mayuscula
#title() Primera letra de cada palabra
#strip() Elimina el espacios al inicio y al final

cadena = " hola python "

print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.strip())

texto = " mundo Hola mundo"
print(texto.replace("mundo","pedro")) #remplaza una palabra por otra

texto1 = "Python es genial. Python es facil"

print(texto1.find("genial")) # muestra -1 si no encuentra nada, si si encuentra muestra la posicion donde se encuentra la primera letra de la palabra
print(texto1.count("genial")) # muestra la cantidad de palabras que hay.

texto2 = "manzana,pera,sandia"

frutas = texto2.split(",")
print(frutas)

unidas = ",  ".join(frutas)
print(unidas)

#indezacion y rebanado (slicing)
#se puede acceder a caracteres
#induvuduales ausando inideices
#obtener subcadena
#con cadena[inicio:fin:paso]
texto4 = "Python"
print(texto4[0:3])#pyt
print(texto4[:3])#pyt
print(texto4[3:])#hon
print(texto4[::-1])#nohtyP