import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

#Cuadrado, punteada y roja
plt.plot(x,y,marker="D", linestyle="--",color="red")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Primera grafica")
plt.grid()
plt.show()

#Triangulo, puntos y azul
plt.plot(x,y,marker="v", linestyle=":",color="blue")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Primera grafica")
plt.grid()
plt.show()

#Estrella, punto y raya y verde
plt.plot(x,y,marker="*", linestyle="-.",color="black")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Primera grafica")
plt.grid()
plt.show()