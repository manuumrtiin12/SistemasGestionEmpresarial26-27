def buscar_producto(productos, nombre):
    for producto in productos:
        if producto == nombre:
            return True
    return False


productos = [
    "Teclado",
    "Monitor",
    "Webcam",
    "Ratón"
]

print(buscar_producto(productos, "Teclado"))
print(buscar_producto(productos, "Camara"))
