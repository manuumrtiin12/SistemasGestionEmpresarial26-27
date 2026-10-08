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
        print(f"Stock actualizado: {self.stock}")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")

        elif cantidad > self.stock:
            print("No hay stock suficiente.")

        else:
            self.stock = self.stock - cantidad
            print(f"Venta realizada. Stock restante: {self.stock}")

    def valor_stock(self):
        total = self.stock * self.precio
        print(f"El valor total del stock es: {total} €")


producto1 = Producto(1, "Ordenador", 799.99, 10)
producto2 = Producto(2, "Teclado", 29.99, 25)

producto1.mostrar_datos()
producto2.mostrar_datos()

producto1.vender(3)
producto2.vender(30)

producto1.valor_stock()
producto2.valor_stock()
