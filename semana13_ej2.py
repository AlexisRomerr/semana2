# Contador de positivos y negativos
# Con while, permite ingresar números hasta que el usuario escriba 0.
# Dentro, usa if para contar cuántos son positivos y negativos.
# Al final, usa un for para mostrar un resumen de resultados.

positivo = 0
negativo = 0

while True:
    n = int(input("Ingrese un número (0 para cerrar): "))
    if n == 0:
        break

    if n > 0:
        positivo += 1
    elif n < 0:
        negativo += 1


for etiqueta, cantidad in [("positivos", positivo), ("negativos", negativo)]:
    print("La cantidad de números", etiqueta, "es:", cantidad)
