importeCompra = int(input("¿Cuál ha sido el importe de la compra?: "))
esVip = int(input("Pulse 1 VIP | Pulse 2 si no es VIP: "))

descuento = 0

if esVip == 2 and importeCompra > 100:
    descuento = importeCompra * 0.05

elif esVip == 1:
    descuento = importeCompra * 0.1

importeTotal = importeCompra - descuento
print("El importe final es de:", importeTotal)
