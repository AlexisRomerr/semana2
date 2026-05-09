# 5. Diseñar una función que reciba un arreglo de números y retorne un nuevo arreglo solo con los números positivos usando un bucle y condicionales.


def numeros_positivos():
    numeros = []

    while True:
        numeros_user = int(input("Ingrese numeros (0 para salir): "))

        if numeros_user == 0:
            break
        numeros.append(numeros_user)

    positivos = []
    for i in numeros:
        if i > 0:
            positivos.append(i)
    return positivos


resultado = numeros_positivos()
print("Los numeros positivos son:", resultado)
