total = 0
numeroVentas = 0

importe = float(input("Introduce el importe de la venta (0 para terminar): "))

while (importe != 0):
    total += importe
    numeroVentas += 1

    importe = float(input("Introduce el importe de la venta (0 para terminar): "))

print("Número de ventas:", numeroVentas)
print("Total vendido:", total)