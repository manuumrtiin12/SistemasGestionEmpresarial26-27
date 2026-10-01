precioProducto = int(input("Dame el precio de un producto o pulsa 0 para salir: "))

while(precioProducto != 0):
    if(precioProducto < 20):
        print("Precio economico")

    elif(precioProducto > 20 and precioProducto < 100):
        print("Precio medio")

    else:
        print("Precio elevado")

    precioProducto = int(input("Dame el precio de un producto o pulsa 0 para salir: "))
