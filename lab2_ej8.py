def cambio_texto(texto, num):
    if num == 1:
        return texto.upper()
    elif num == 2:
        return texto.lower()
    elif num == 3:
        return texto.capitalize()
    else:
        return "Número inválido. Usa 1, 2 o 3."


print("---MENU PRINCIPAL---")
texto = input("Ingrese un texto: ")

while True:
    print("\nOpciones")
    print("1. Convertir en mayúsculas")
    print("2. Convertir en minúsculas")
    print("3. Convertir primera letra en mayúscula")
    print("4. Salir")

    num = int(input("Ingrese un número del 1 al 4: "))

    if num == 4:
        print("Adiós.")
        break

    if num not in (1, 2, 3):
        print("Solo se aceptan números del 1 al 3")
        continue

    resultado = cambio_texto(texto, num)
    print("Resultado:", resultado)
