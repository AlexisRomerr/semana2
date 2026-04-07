def texto_trans(texto, num):

    resultado = texto

    for i in num:
        if i == 1:
            resultado = resultado.upper()
        elif i == 2:
            resultado = resultado.lower()
        elif i == 3:
            resultado = resultado.capitalize()
        else:
            return "Número inválido. Usa 1, 2 y 3."
    return resultado


texto_user = input("Ingrese un texto: ")

print(
    "Presione 1 para transformar todo a mayúsculas, 2 para minúsculas y 3 para colocar la primera letra en mayúscula"
)

num_user = input("Ingrese los numeros del 1 al 3 separados por espacio: ")

lista = [int(i) for i in num_user.split()]

resultado_final = texto_trans(texto_user, lista)
print(resultado_final)
