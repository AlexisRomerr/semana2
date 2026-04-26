# Números pares en rango
# Pide al usuario un número n.
# Usa un for para recorrer de 1 a n.
# Usa un if para imprimir solo los números pares.
# Repite todo con while hasta que el usuario ingrese 0.


while True:
    n = int(input("Ingrese un numero o el 0 para salir: "))
    if n == 0:
        break
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
