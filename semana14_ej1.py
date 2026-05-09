# 1. Crear una función que reciba una lista de números y retorne la cantidad de números pares e impares utilizando un bucle y estructuras condicionales.


def lista_numeros():
    numeros = []

    while True:
        num = int(input("Ingresa uno o varios numeros (0 para terminar): "))
        if num == 0:
            break
        numeros.append(num)

    pares = 0
    impares = 0
    for n in numeros:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Números ingresados:", numeros)
    print("Cantidad de pares:", pares)
    print("Cantidad de impares:", impares)


lista_numeros()
