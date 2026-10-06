def calcular_total(ventas):
    suma = 0
    for numero in ventas:
        suma = suma + numero
    return suma


ventas = [10, 20, 15, 5]

print(calcular_total(ventas))
