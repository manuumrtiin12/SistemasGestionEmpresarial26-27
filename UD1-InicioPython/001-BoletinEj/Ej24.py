
clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Marta", "email": "marta@email.com", "ciudad": "Sevilla"},
    {"nombre": "Carlos", "email": "carlos@email.com", "ciudad": "Málaga"},
    {"nombre": "Lucía", "email": "lucia@email.com", "ciudad": "Sevilla"}
]

ciudad = input("Ciudad: ").strip()

contador = 0
for cliente in clientes:
    if cliente["ciudad"].lower() == ciudad.lower():
        contador += 1

print(f"Número de clientes de {ciudad}: {contador}")
