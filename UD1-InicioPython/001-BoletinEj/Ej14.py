productos = [
    "Teclado",
    "Ratón",
    "Monitor",
    "Webcam",
    "Impresora"
]

productoElegido = input("Cual producto quieres buscar: ")

if productoElegido in productos:
    print("Porducto encontrado")

else:
    print("Producto no encontrado ")