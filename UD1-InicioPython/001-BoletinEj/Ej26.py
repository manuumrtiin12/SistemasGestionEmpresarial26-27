
clientes_tienda_a = {"Ana", "Luis", "Marta", "Carlos"}
clientes_tienda_b = {"Marta", "Carlos", "Lucía"}

print("Todos los clientes:", clientes_tienda_a | clientes_tienda_b)

print("En ambas tiendas:", clientes_tienda_a & clientes_tienda_b)

print("Solo en la tienda A:", clientes_tienda_a - clientes_tienda_b)
