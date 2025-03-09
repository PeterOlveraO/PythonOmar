#Ejercicios de lista - Lista de compras interactiva
productos = []
agregar = ""

while True:

    n = int(input(f"Elige una opcion: 1- Agregar un producto, 2- Eliminar un producto, 3- Mostrar la lista actualizada, 4-Salir :"))


    if n == 1:
        while True:
            agregar = input("Ingresa el producto: ")
            productos.append(agregar)
            print("Producto agregado")
            a = input("Quieres agregar otro producto? (si/no): ")
            if a == "no":
                break

    elif n == 2:

        while True:
            if agregar == "":
                print("No hay productos en la lista")
                break
            eliminar = input("Ingresa el producto: ")
            productos.remove(eliminar)
            print("Producto eliminado")
            a = input("Quieres eliminar otro producto? (si/no): ")
            if a == "no":
                break

    elif n == 3:
        print(productos)
        continue

    else:
        print("Saliendo del programa")
        break