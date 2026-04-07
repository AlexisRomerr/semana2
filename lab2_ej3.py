def cambio_texto(texto, num):
    if num == 1:
        print(texto.upper())
    elif num == 2:
        print(texto.lower())
    elif num == 3:
        print(texto.capitalize())
    else:
        print("Número inválido. Usa 1, 2 o 3.")


texto = input("Ingrese un texto: ")

print(
    "Presione 1 para transformar todo a mayúsculas, 2 para minúsculas y 3 para colocar la primera letra en mayúscula"
)

num = int(input("Ingrese un número del 1 al 3: "))

while num not in (1, 2, 3):
    print("Solo se aceptan números del 1 al 3")
    num = int(input("Ingrese un número del 1 al 3: "))


cambio_texto(texto, num)
