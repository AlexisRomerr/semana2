# Validación de contraseña
# Con while, pide una contraseña hasta que sea correcta.
# Usa if para verificar si coincide.
# Después, usa for para mostrar cuántos intentos fallidos hubo.

contra_correcta = "hola"
conteo = 0

while True:
    contra = input("Ingrese la contraseña: ")
    if contra == contra_correcta:
        break
    else:
        print("Contraseña incorrecta")
        conteo += 1


for i in range(conteo):
    print("Intento numero:", i + 1)

print("Total de intentos fallidos: ", conteo)
