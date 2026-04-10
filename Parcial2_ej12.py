archivo = "ING. Alexis.txt"
print("Archivo normal:", archivo)

sinSufijo = archivo.removesuffix(".txt")
print("Archivo sin sufijo:", sinSufijo)

sinPrejifo = sinSufijo.removeprefix("ING. ")
print("Archivo sin prefijo:", sinPrejifo)

archivo_minus = sinPrejifo.lower()
print("Archivo en minusculas:", archivo_minus)

archivo_con_split = archivo_minus.split()
print("Archivo usando el split:", archivo_con_split)
