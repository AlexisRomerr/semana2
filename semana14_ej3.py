# 3. Crear una función que reciba un arreglo de notas y devuelva el promedio. Además, usando if, indicar si el grupo aprueba o reprueba.


def notas_promedio():
    notas = []

    while True:
        notas_user = float(input("Ingrese sus notas (0 para terminar y calcular): "))
        if notas_user == 0:
            break
        elif notas_user < 0:
            print("nota invalida")
        else:
            notas.append(notas_user)

    if len(notas) > 0:
        promedio = sum(notas) / len(notas)

        if promedio < 6:
            print("Ha reprobado la materia con", promedio)
        else:
            print("Ha aprobado la materia con", promedio)


notas_promedio()
