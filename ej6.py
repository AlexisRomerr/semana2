nombre = input("Ingrese su nombre completo: ")

nombre_separado = nombre.split()
print(nombre_separado)

for palabra in nombre_separado:
    print(palabra)
