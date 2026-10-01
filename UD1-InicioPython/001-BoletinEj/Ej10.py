nombre = input("Dame un nombre: ")

nombreSinEspacios = nombre.strip()
nombreMinusculas = nombreSinEspacios.lower()
nombreMayusculas = nombreSinEspacios.upper()
longitud = len(nombreSinEspacios)

print(f"Nombre sin espacios: {nombreSinEspacios}")
print(f"En minúsculas: {nombreMinusculas}")
print(f"En mayúsculas: {nombreMayusculas}")
print(f"Longitud: {longitud}")
