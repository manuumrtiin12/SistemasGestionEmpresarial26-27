password_correcta = "python123"

contraseña = input("Contraseña: ")

while(contraseña != password_correcta):
    print("Incorrecto, vuelve a intentarlo")
    contraseña = input("Contraseña: ")
print("Acceso permitido")