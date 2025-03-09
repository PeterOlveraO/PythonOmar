import matplotlib.pyplot as pit
from matplotlib.lines import lineStyles

x = [5,6,4,3,4,5]
y = [5,3,4,5,4,4]

pit.plot(x,y,marker="o", linestyle="-",color="red")
pit.xlabel("Eje x")
pit.ylabel("Eje y")
pit.title("Primera grafica")
pit.grid()
pit.show()