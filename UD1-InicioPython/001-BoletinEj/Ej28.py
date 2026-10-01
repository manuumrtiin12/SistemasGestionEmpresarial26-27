stock = int(input("Dame el stock: "))
cantidadQuiereComprar = int(input("Cuanto quiere comprar el cliente? "))

if(stock > cantidadQuiereComprar):
    print("Venta posible")

else:
    print("La venta no es posible")