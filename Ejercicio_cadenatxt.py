# """Cree un programa en Python que analice una cadena de texto proporcionada por el usuario.
# programa debe almacenar el texto en una variable y luego eliminar los espacios al inicio y al final usando strip().
# Posteriormente debe mostrar el texto en mayúsculas con upper() y en minúsculas con lower().
# Después deberá verificar cuántas veces aparece una palabra específica dentro del texto utilizando count(), buscar la posición
# de esa palabra con find(), y reemplazar una palabra del texto por otra usando replace().
# Finalmente, el programa debe dividir el texto en una lista de palabras utilizando split() y luego unir nuevamente
# esas palabras en una sola cadena usando join(), mostrando cada resultado en pantalla"""

texto = input("Ingrese texto: ")
print(texto)


texto_sin_espacios = texto.strip()
print("Texto sin espacios:", texto_sin_espacios)

texto_mayus = texto_sin_espacios.upper()
print("Texto en mayusculas:", texto_mayus)

texto_minus = texto_sin_espacios.lower()
print("Texto en minusculas:", texto_minus)

palabra = "hola"
conteo = texto_sin_espacios.count(palabra)

posicion = texto_sin_espacios.find(palabra)
if posicion == -1:
    print("La palabra hola no aparece en el texto")
else:
    while posicion != -1:
        print("La palabra hola aparece en la posicion:", posicion)
        posicion = texto_sin_espacios.find(palabra, posicion + 1)

texto_nuevo = texto_sin_espacios.replace("hola", "beber")
if conteo == 0:
    print("No se puede reemplazar la palabra hola porque no aparece")
else:
    print("Texto cambiando 'hola' por 'beber':", texto_nuevo)

dividido = texto_nuevo.split()
print("Texto dividido:", dividido)

unido = " ".join(dividido)
print("Texto unido:", unido)
