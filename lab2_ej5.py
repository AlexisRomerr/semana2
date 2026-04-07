def numero_valido(texto, num):
    if num not in (1, 2, 3):
        print("opcion invalida")
        return False
    else:
        print("opcion valida")
        return True


texto_user = input("ingrese un texto: ")

num_user = int(input("Ingrese un número del 1 al 3: "))

numero_valido(texto_user, num_user)
