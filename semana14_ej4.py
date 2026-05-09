# 4. Elaborar un programa que llene un arreglo con 8 números ingresados por el usuario y, mediante una función, determine cuál es el número mayor.

numeros = []
entrada = 0

while entrada < 8:
    numeros_user = int(input("Ingrese un numero 8 veces: "))
    numeros.append(numeros_user)
    entrada += 1


def numero_mayor(lista):
    num_mayor = max(lista)
    print("El numero mayor es: ", num_mayor)


numero_mayor(numeros)
