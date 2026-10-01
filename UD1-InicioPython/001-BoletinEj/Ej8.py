precio1 = float(input("Precio del producto: "))
precio2 = float(input("Cantidad del producto: "))

if(precio1 > precio2): print(f"{precio1} mayor que {precio2}")
if(precio2 > precio1): print(f"{precio2} mayor que {precio1}")
if(precio1 == precio2): print(f"Son iguales")