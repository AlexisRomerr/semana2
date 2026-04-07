def transformar_lista(lista, num):
    lista_nueva = []
    for palabra in lista:
        if num == 1:
            lista_nueva.append(palabra.upper())
        elif num == 2:
            lista_nueva.append(palabra.lower())
        elif num == 3:
            lista_nueva.append(palabra.capitalize())

    return lista_nueva


texto = input("Ingrese varias palabras separadas con un espacio: ")
lista_de_usuario = texto.split()

print(
    "Presione 1 para transformar todo a mayúsculas, 2 para minúsculas y 3 para colocar la primera letra en mayúscula"
)

opcion = int(input("Ingrese un número del 1 al 3: "))


while opcion not in (1, 2, 3):
    print("Solo se aceptan números del 1 al 3")
    opcion = int(input("Ingrese un número del 1 al 3: "))

resultado = transformar_lista(lista_de_usuario, opcion)
print("Resultado:", resultado)
