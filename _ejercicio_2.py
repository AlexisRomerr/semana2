# While o for
# pedir una palabra y comparar con una q escojamos

detener = True
palabra_correcta = "hola"
i = 0

while detener:
    if i == 10:
        break
    palabra = input("Ingrese una palabra para adivinar, intentos maximos 10: ")
    i += 1
    if palabra != palabra_correcta:
        print("Incorrecto, intente de nuevo")
    else:
        print("Ganaste")
        detener = False

if detener:
    print("Perdiste, no quedan mas intentos")
