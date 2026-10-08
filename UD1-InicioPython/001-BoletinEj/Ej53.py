class Persona:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):

    def __init__(self, nombre, email, numeroCliente):
        super().__init__(nombre, email)
        self.numeroCliente = numeroCliente


class ClienteVIP(Persona):

    def __init__(self, nombre, email, descuento):
        super().__init__(nombre, email)
        self.descuento = descuento

    def calculaPrecio(self, precio):
        precioDescuento = (precio * self.descuento) / 100
        precioFinal = precio - precioDescuento

        print(f"Precio final con descuento: {precioFinal}")


class main:

    persona1 = Cliente("Sebas", "example@example.es", 54321)
    cliente1 = Cliente("Francisco", "example@example.com", 12345)
    clienteVIP1 = ClienteVIP("Manuel", "example@example.si", 20)

    print(persona1.nombre, " | ", persona1.email)
    print(cliente1.nombre, " | ", cliente1.email, " | ", cliente1.numeroCliente)
    print(clienteVIP1.nombre, " | ", clienteVIP1.email, " | ", clienteVIP1.descuento)

    clienteVIP1.calculaPrecio(100)