# 9. Elaborar una función que reciba un arreglo de números y devuelva la suma total, pero solo sumando los números pares.


def numeros_suma():
    numeros = []
    while True:
        numeros_user = int(input("Ingrese números (0 para cerrar y sumar los pares): "))
        if numeros_user == 0:
            break
        numeros.append(numeros_user)

    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)

    resultado = sum(pares)
    print("La suma de los números pares es:", resultado)


numeros_suma()
