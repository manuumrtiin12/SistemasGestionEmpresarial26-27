nombreProducto = input("Dame un nombre de producto: ")
precio = float(input("Dame el precio del producto: "))
cantidad = int(input("Dame la cantidad del producto: "))

print(f"Nombre: {nombreProducto} Precio: {precio} Cantidad: {cantidad}")
print(f"Total: {cantidad * precio}")
