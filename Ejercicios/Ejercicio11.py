#Ordenar nombres

nombres = []
for i in range(5):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

print(f"Los nombres son: {nombres}")
print(f"Los nombres acomodades son: {sorted(nombres)}")
nombres.reverse()
print(f"Los nombres acomodades al reves son: {nombres}")
