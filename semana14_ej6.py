# 6. Crear un programa que genere 10 números aleatorios, los guarde en un arreglo y mediante una función indique cuántos son mayores a 50.

import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))
print("Los numeros generados son:", numeros)


def mayores_a_50(lista):
    mayores = []
    for n in lista:
        if n > 50:
            mayores.append(n)

    if mayores:
        print("Los números mayores a 50 son:", end=" ")
        for num in mayores:
            print(num, end=" ")


mayores_a_50(numeros)
