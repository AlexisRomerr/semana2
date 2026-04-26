def pedirNumero():
    numero = input("ingrese un numero: ")
    return numero


def ValidarNumero(numero):
    validarNumero = numero.isdigit()
    return validarNumero


def parOImpar(numero):
    if numero % 2 == 0:
        print("el numero es par")
    elif numero % 2 != 0:
        print("el numero es impar")


def bucliwhile(intentos):
    control = True
    contador = 0
    while control:
        seleccion = pedirNumero()
        validado = ValidarNumero(seleccion)
        parOImpar(validado)
        contador += 1
        if contador == intentos:
            control = False


bucliwhile(3)
