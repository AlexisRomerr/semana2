while True:
    año = int(input("Ingrese un año para saber si es bisiesto o no: "))
    if año > 0:
        break
    else:
        print("Ingrese un año válido")

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es bisiesto")
else:
    print("El año", año, "no es bisiesto")
