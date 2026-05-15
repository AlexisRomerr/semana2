nombre_user = input("Ingrese su nombre completo: ")

nombre_lista_invertido = nombre_user.split()[::-1]

for palabra in nombre_lista_invertido:
    salida = ""
    for letra in palabra:
        salida += letra + "."
    print(salida[:-1])
