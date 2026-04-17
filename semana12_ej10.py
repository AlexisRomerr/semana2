user_real = "panjaja"
passw_real = "1234"

intentos = 0
while intentos < 3:

    user = input("Ingrese su usuario: ")
    passw = input("Ingres su contraseña: ")

    if user == user_real and passw == passw_real:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Acceso denegado")

if intentos == 3:
    print("Superó el limite de intentos")
