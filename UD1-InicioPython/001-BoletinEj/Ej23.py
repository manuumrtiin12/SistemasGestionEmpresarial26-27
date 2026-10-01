
clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Marta", "email": "marta@email.com", "ciudad": "Málaga"}
]

email_buscado = input("Introduce el email a buscar: ").strip().lower()

encontrado = None
for cliente in clientes:
    if cliente["email"].lower() == email_buscado:
        encontrado = cliente
        break

if encontrado:
    print("Cliente encontrado:")
    print("Nombre:", encontrado["nombre"])
    print("Ciudad:", encontrado["ciudad"])
else:
    print("No existe ningún cliente con ese email.")
