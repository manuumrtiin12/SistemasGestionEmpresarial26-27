class Producto:

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_datos(self):
        print("Codigo:", self.codigo,
              "- Nombre:", self.nombre,
              "- Precio:", self.precio,
              "- Stock:", self.stock)

    def reponer(self, cantidad):
        self.stock = self.stock + cantidad
        print(f"Cantidad inicial: {self.stock - cantidad}")
        print(f"Cantidad repuesta: {cantidad}")
        print(f"Stock final: {self.stock}")


producto1 = Producto(1, "Ordenador", 799.99, 10)
producto2 = Producto(2, "Teclado", 29.99, 25)

producto1.mostrar_datos()
producto2.mostrar_datos()

producto1.reponer(5)
producto2.reponer(10)

producto1.mostrar_datos()
producto2.mostrar_datos()
