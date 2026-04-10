cadena = "Python2026"

cadena_verificada = cadena.isalnum()
print("Es alfanumerico?: ", cadena_verificada)

if cadena_verificada == True:
    cadena_minus = cadena.lower()
    print("Cadena en minuscula: ", cadena_minus)

    cadena_reemplazo = cadena_minus.replace("2026", "")
    print("Cadena reemplazada: ", cadena_reemplazo)
else:
    print("No es alfanumerico")
