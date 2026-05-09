# 7. Desarrollar una función que reciba un arreglo de edades y determine cuántas personas son mayores de edad utilizando if y un ciclo.
def mayores_edad():
    edades = []
    while True:
        edades_user = int(input("Ingrese edades de personas (0 para cerrar): "))
        if edades_user == 0:
            break
        if edades_user < 0:  # validación para evitar negativos
            print("Edad inválida, ingrese un número positivo.")
            continue
        edades.append(edades_user)

    contador = 0
    for i in edades:
        if i >= 18:
            contador += 1
    print("Cantidad de personas mayores:", contador)


mayores_edad()
