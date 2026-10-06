    
def aplicar_descuento(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return precio_final

aplicar_descuento(100)
aplicar_descuento(100, 10)
aplicar_descuento(250, 20)