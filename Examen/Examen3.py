#Converison de temperatura
F = 0.0
C = int(input("Ingresa la temperatura a convertir: "))

F = C * 1.8 + 32
K = C + 273.15

print(f"La temperatura en Fahremheit es de: {F}")
print(f"La temperatura en Kelvin es de: {K}")