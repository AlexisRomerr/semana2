def cambio_texto_y_contar(texto, num):
    if num == 1:
        cambio = texto.upper()
    elif num == 2:
        cambio = texto.lower()
    elif num == 3:
        cambio = texto.capitalize()
    else:
        return "Número inválido. Usa 1, 2 o 3."

    print("El texto cambiado es: ", cambio)

    cantidad = len(cambio.replace(" ", ""))
    return cantidad


texto_user = input("Ingrese un texto: ")

print(
    "Presione 1 para transformar todo a mayúsculas, 2 para minúsculas y 3 para colocar la primera letra en mayúscula"
)

num_user = int(input("Ingrese un número del 1 al 3: "))

while num not in (1, 2, 3):
    print("Solo se aceptan números del 1 al 3")
    num = int(input("Ingrese un número del 1 al 3: "))

total = cambio_texto_y_contar(texto_user, num_user)

print("La cantidad de caracteres son:", total)
