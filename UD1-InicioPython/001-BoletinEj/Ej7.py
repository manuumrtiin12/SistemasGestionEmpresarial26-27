precio = float(input("Precio del producto: "))
descuento = int(input("Cantidad del producto: "))

precioDescuento = (precio*descuento)/100

print(f"Subtotal: {precio}")
print(f"Descuento: {descuento}%")
print(f"Total: {precio-precioDescuento}")