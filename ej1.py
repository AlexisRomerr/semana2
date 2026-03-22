nombre = input("ingrese su nombre completo:")

nombre_mayus = nombre.upper()
print(nombre_mayus)

nombre_minus = nombre.lower()
print(nombre_minus)

conteo = len(nombre.replace(" ", ""))
print("La cantidad de caracteres de su nombre son:", conteo)
