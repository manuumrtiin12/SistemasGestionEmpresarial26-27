class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Email:", self.email)
        print("Teléfono:", self.telefono)


cliente1 = Cliente("Ana", "ana@gmail.com", "600123456")
cliente2 = Cliente("Carlos", "carlos@gmail.com", "611987654")

cliente1.mostrar_datos()
print()
cliente2.mostrar_datos()
