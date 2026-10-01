precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad del producto: "))

total = precio*cantidad

print(f"Subtotal: {total}")
print("IVA: 21%")

totalIVA = total*0.21

print(f"Total: {totalIVA}")