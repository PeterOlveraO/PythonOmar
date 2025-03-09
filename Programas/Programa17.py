import matplotlib.pyplot as plt

Etiquetas = ["A","B","C","D","F"]
Valores = [5,2,4,6,4]

plt.bar(Etiquetas,Valores,color="blue")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Segunda grafica")
plt.grid()
plt.show()