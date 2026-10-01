print("1. Mostrar mensaje")
print("2. Mostrar fecha ficticia")
print("3. Salir")

accion = int(input("Opccion: "))

while(accion != 3):

    if(accion == 1):
        print("Hola que tal")

    elif(accion == 2):
        print("Fecha ficticia")

    else:
        print("Esa opcion no existe")

    print("1. Mostrar mensaje")
    print("2. Mostrar fecha ficticia")
    print("3. Salir")

    accion = int(input("Opccion: "))        

print("Hasta la proxima")