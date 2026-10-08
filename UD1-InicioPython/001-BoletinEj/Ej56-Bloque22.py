class cliente: 

    def __init__(self, nombre, email, telefono):

        self.nombre = nombre
        self.email = email
        self.telefono = telefono


    def menu():
        print("1. Añadir cliente")
        print("2. Mostrar clientes")
        print("3. Buscar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

    menu()
    opcion = print(int(input("Que opcion quieres: ")))

    clientes = []

    while(opcion != 5):

        match opcion:
            case 1:
                



        