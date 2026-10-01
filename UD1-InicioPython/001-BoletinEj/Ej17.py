
producto = ("P001", "Teclado", 21)

print("Código:", producto[0])
print("Nombre:", producto[1])
print("Tipo de IVA:", producto[2], "%")

# Intentamos modificar el código del producto
try:
    producto[0] = "P002"
except TypeError as error:
    print("\nError al modificar la tupla:", error)

# Explicación:
# Las tuplas son inmutables: una vez creadas, sus elementos no se pueden
# cambiar, añadir ni eliminar. Por eso Python lanza un TypeError.
# Si se necesitan cambios, hay que crear una nueva tupla (o usar una lista).
