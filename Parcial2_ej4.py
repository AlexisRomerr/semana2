palabra = "CANTANDO"
print("Palabra normal:", palabra)

palabra_minus = palabra.lower()
print("Palabra en minusculas:", palabra_minus)

sinSufijo = palabra_minus.removesuffix("ando")
print("Palabra sin ando:", sinSufijo)

posicion = sinSufijo.find("t")
print("La t se encuentra en la posicion:", posicion)
