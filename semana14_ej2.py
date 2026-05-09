# 2. Desarrollar un programa que permita ingresar 10 nombres en un arreglo y luego, mediante una función, muestre solo los nombres que tengan más de 5 caracteres.


entradas = 0
nombres = []

while entradas < 10:
    nombres_user = input("Ingrese un nombre distinto 10 veces: ")
    nombres.append(nombres_user)
    entradas += 1


def mostrar_nombres(lista):
    print("Los nombres con mas de 5 caracteres son: ")
    for i in lista:
        if len(i) > 5:
            print(i)


mostrar_nombres(nombres)
