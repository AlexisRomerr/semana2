# Control de empleados: for lista, if salario, while menú, select case acciones.

empleados = [
    {"nombre": "Alexis", "salario": 500},
    {"nombre": "Robin", "salario": 600},
    {"nombre": "Kevin", "salario": 700},
    {"nombre": "Alex", "salario": 400},
]


def lista_nombres():
    for i in empleados:
        print(f"{i['nombre']}")


def buscar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    for i in empleados:
        if i["nombre"].lower() == nombre.lower():
            print(f"El empleado {i['nombre']} gana: {i['salario']}")
            return
    print("Empleado no encontrado")


def menu():

    while True:
        opcion = int(
            input("1: Lista de empledos, 2: Ver salario de empleado, 3: Salir -- ")
        )

        match opcion:
            case 1:
                lista_nombres()
            case 2:
                buscar_empleado()
            case 3:
                print("Programa finalizado")
                break
            case _:
                print("Opcion no valida")


menu()
