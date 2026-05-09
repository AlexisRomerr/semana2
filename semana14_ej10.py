# 10. Diseñar un programa que permita ingresar 6 números en un arreglo y mediante una función ordenarlos de menor a mayor usando ciclos e instrucciones condicionales.


numeros = []
i = 0

while i < 6:
    numeros_user = int(input("Ingrese 6 numeros: "))
    i += 1
    numeros.append(numeros_user)


def menor_a_mayor(lista):

    for n in range(len(lista)):
        for k in range(len(lista) - 1):
            if lista[k] > lista[k + 1]:

                aux = lista[k]
                lista[k] = lista[k + 1]
                lista[k + 1] = aux
    return lista


ordenados = menor_a_mayor(numeros)
print("Los numeros de menor a mayor son:", ordenados)
