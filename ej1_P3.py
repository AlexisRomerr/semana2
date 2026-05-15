etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "" or etiqueta is None:
    print("Error. Programa finalizado")
else:
    categoria = etiqueta[5:-3]
    print("La categoria es:", categoria)

    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print("Ruta:", ruta)
