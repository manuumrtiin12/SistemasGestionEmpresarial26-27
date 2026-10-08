class Persona:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Cliente(Persona):

    def __init__(self, nombre, email, numeroCliente):
        super().__init__(nombre, email)
        self.numeroCliente = numeroCliente

class main:
    persona1 = Cliente("Sebas", "example@example.es", 54321)
    cliente1 = Cliente("Francisco", "example@example.com", 12345)

    print(persona1.nombre, " ", persona1.email)
    print(cliente1.nombre, " ", cliente1.email, " ", cliente1.numeroCliente)